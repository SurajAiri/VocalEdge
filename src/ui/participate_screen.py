import streamlit as st

from src.media.audio_handler import AudioHandler
from src.media.video_handler import VideoHandler
from src.utils.enums import VideoMode


def change_recording_state(value:bool):
    st.session_state.is_working = value


def start_recording():
    change_recording_state(True)

def stop_recording(on_act_complete):
    global audio_handler
    if audio_handler is not None:
        print("Trying to Stopping audio recording")
        audio_handler.stop_and_save_audio()
        del audio_handler
    change_recording_state(False)
    on_act_complete()


audio_handler = None

def participate_ui(on_act_complete):
    global audio_handler
    vid_handler = None
    audio_handler = None

    stFrame = st.empty()


    # Button to start recording
    if not st.session_state.is_working:
        if vid_handler is not None:
            del vid_handler
        st.button("Start Recording",on_click= start_recording)
    else:
        if audio_handler is None:
            audio_handler = AudioHandler()
            audio_handler.init_record()

        if vid_handler is None:
            vid_handler = VideoHandler()
            vid_handler.set_read_mode(VideoMode.CAMERA)

        st.button("Stop Recording",on_click=lambda: stop_recording(on_act_complete))

    


    while st.session_state.is_working:
        # Initialize the video handler
        frame = vid_handler.read_frame()
        if frame is None:
            st.error("Failed to read frame.")
            break

        # Convert the frame to RGB for Streamlit display
        stFrame.image(frame, channels="RGB")

        # Stop recording if the button is pressed
        if not st.session_state.is_working:
            break
