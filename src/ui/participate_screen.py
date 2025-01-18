import time
import streamlit as st
from src.activity.activity_model import Activity
from src.media.audio_handler import AudioHandler
from src.media.video_handler import VideoHandler
from src.utils.enums import AppScreen, VideoMode

def change_recording_state(value:bool):
    st.session_state.is_working = value


def start_recording():
    change_recording_state(True)

def cancel_recording():
    change_recording_state(False)
    del st.session_state.audio_handler
    del st.session_state.video_handler
    st.session_state.screen = AppScreen.HOME    
    

def stop_recording(on_act_complete):
    audioHandler = st.session_state.audio_handler
    if audioHandler is not None:
        print("Trying to Stopping audio recording")
        audioHandler.stop_and_save_audio()
        del audioHandler
        del st.session_state.audio_handler
    if 'video_handler' in st.session_state:
        print("Trying to Stopping video recording")
        del st.session_state.video_handler

    on_act_complete()

def initiate_audio_video_handlers():
    if 'audio_handler' in st.session_state:
        del st.session_state.audio_handler
    if 'video_handler' in st.session_state:
        del st.session_state.video_handler

    aud = AudioHandler()
    aud.init_record()

    vid = VideoHandler()
    vid.set_read_mode(VideoMode.CAMERA)

    st.session_state.audio_handler = aud
    st.session_state.video_handler = vid

    print("Audio and Video handlers initialized")



# ui part
def participate_ui(on_act_complete):
    videoHandler = None
    audioHandler = None

    # 1. wait for question
    if 'question' not in st.session_state or st.session_state.question is None:
        with st.spinner('Waiting for question...'):
            while 'question' not in st.session_state or st.session_state.question is None:
                time.sleep(1)
        
    # 2. Display the current question from session state
    if 'activity' not in st.session_state:
        st.error("No activity found")
        return
    act = Activity(st.session_state.activity)
    display_activity_info(act)

    # 3. preparation time waiting
    preparation_timer(act)

    # 4. initialize audio video handlers
    initiate_audio_video_handlers()

    # 5. start recording
    stFrame = st.empty()
    video_handler = st.session_state.video_handler
    # audio_handler = st.session_state.audio_handler

    # 6. Cancel button
    st.button("Cancel", on_click=cancel_recording)
    st.button("Done", on_click=lambda: stop_recording(on_act_complete))
    
    while st.session_state.is_working:
        frame = video_handler.read_frame()
        if frame is None:
            st.error("Failed to read frame.")
            break

        # Convert the frame to RGB for Streamlit display
        stFrame.image(frame, channels="RGB")

        # Stop recording if the button is pressed
        if not st.session_state.is_working:
            break

    # 7. Stop recording button (after 30 seconds)
    # 8. on_act_complete callback
def forced_start():
    st.session_state.force_start = True
    start_recording()


def preparation_timer(activity:Activity):
    if st.session_state.done_preparation:
        return
    st.session_state.done_preparation = True

    if st.session_state.force_start:
        st.session_state.prep_time = 0
        # st.rerun()
    if 'prep_time' in st.session_state:
        prep_time = st.session_state.prep_time
    else:
        prep_time = activity.prepareTime  # Default preparation time in seconds
        # prep_time = 2

    placeholder = st.empty()
    st.button(label="Start Test",key="force_start_test",on_click=forced_start)
    for seconds in range(prep_time, 0, -1):
        if st.session_state.force_start:

            break

        placeholder.header(f"start in {seconds} sec")
        time.sleep(1)
    placeholder.empty()

    start_recording()


def display_activity_info(act:Activity):
    # activity info
    st.subheader(act.title)
    st.write(act.description)

    # question
    st.subheader("Q: "+st.session_state.question)
    if not st.session_state.done_preparation:
        print("first time preparation")
        # set preparation time
        st.session_state.prep_time = act.prepareTime
        st.session_state.force_start = False

