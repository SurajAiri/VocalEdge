import streamlit as st
from src.media.audio_handler import AudioHandler
from src.media.video_handler import VideoHandler, ReadMode

def change_recording_state(value:bool):
    st.session_state.is_working = value


def start_recording():
    change_recording_state(True)

def stop_recording():
    global audio_handler
    if audio_handler is not None:
        print("Trying to Stopping audio recording")
        audio_handler.stop_and_save_audio()
        del audio_handler
    change_recording_state(False)

audio_handler = None

def main():
    global audio_handler
    vid_handler = None
    st.header("Video Recorder with OpenCV and Streamlit")

    stFrame = st.empty()


    if "is_working" not in st.session_state:
        st.session_state.is_working = False

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
            vid_handler.set_read_mode(ReadMode.CAMERA)

        st.button("Stop Recording",on_click=stop_recording)

    


    while st.session_state.is_working:
        # Record audio
        # audio_handler.record_audio()

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



if __name__ == "__main__":
    main() 