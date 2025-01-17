import numpy as np
import cv2
import wave
import pyaudio

file_name = "temp_video.avi"
audio_file = "temp_audio.wav"
window_name = "window"
interframe_wait_ms = 30

# Initialize video
cap = cv2.VideoCapture(file_name)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize audio
wf = wave.open(audio_file, 'rb')
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True
)

# Function to read and play audio in chunks
def play_audio():
    while True:
        data = wf.readframes(1024)
        if not data:
            break
        stream.write(data)

# Start audio playback in a separate thread
import threading
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# Display video frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video, exiting.")
        break

    cv2.imshow(window_name, frame)
    if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
        print("Exit requested.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
wf.close()
stream.stop_stream()
stream.close()
p.terminate()
