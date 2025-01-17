import streamlit as st
import cv2

def change_recording_state(value:bool):
    st.session_state.is_recording = value


# Function to start video recording
def record_video():
    st.title("Video Recorder with OpenCV and Streamlit")

    # Initialize OpenCV video capture
    if "is_recording" not in st.session_state:
        st.session_state.is_recording = False

    # Button to start recording
    if not st.session_state.is_recording:
        st.button("Start Recording",on_click=lambda: change_recording_state(True))
    else:
        st.button("Stop Recording",on_click=lambda: change_recording_state(False))

    # Placeholder for video frames
    stframe = st.empty()

    # Video recording logic
    if st.session_state.is_recording:
        cap = cv2.VideoCapture(0)
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

        while st.session_state.is_recording:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to read from camera.")
                break

            # Flip the frame (optional)
            frame = cv2.flip(frame, 1)

            # Write the frame to the video file
            # out.write(frame)

            # Convert the frame to RGB for Streamlit display
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(rgb_frame, channels="RGB")

            # Stop recording if the button is pressed
            if not st.session_state.is_recording:
                break

        # Release resources
        cap.release()
        # out.release()
        cv2.destroyAllWindows()
        st.success("Recording saved as 'output.mp4'")

# Run the app
record_video()
