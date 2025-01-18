import pyaudio
import wave
import threading
from src.utils.enums import AudioMode

class AudioHandler:
    def __init__(self, out_path='output/temp/audio.wav'):
        self.audio_mode = AudioMode.NOT_RECORDING
        self.out_path = out_path
        self.frames = []
        self.chunk = 1024  # Number of frames per buffer
        self.format = pyaudio.paInt16  # Audio format
        self.channels = 1  # Number of audio channels
        self.rate = 44100  # Sample rate (Hz)
        self.audio_interface = pyaudio.PyAudio()
        self.stream = None
        self.recording_thread = None

    def __del__(self):
        self.__release_audio__()

    def __release_audio__(self):
        self.audio_mode = AudioMode.NOT_RECORDING
        if self.stream and not self.stream.is_stopped():
            self.stream.stop_stream()
            self.stream.close()
        self.audio_interface.terminate()
        print("Audio resources released")

    def init_record(self):
        if self.audio_mode == AudioMode.RECORDING:
            print("Already recording")
            return
        self.audio_mode = AudioMode.RECORDING
        self.frames = []
        self.stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        print("Recording initialized")
        self.recording_thread = threading.Thread(target=self.__record_audio__)
        self.recording_thread.start()

    def __record_audio__(self):
        print("Start recording...")
        while self.audio_mode == AudioMode.RECORDING:
            try:
                data = self.stream.read(self.chunk, exception_on_overflow=False)
                self.frames.append(data)
            except Exception as e:
                print(f"Error during recording: {str(e)}")
        print("Recording stopped")

    def stop_and_save_audio(self):
        if self.audio_mode == AudioMode.NOT_RECORDING:
            print("Recording is not active")
            return
        self.audio_mode = AudioMode.NOT_RECORDING
        if self.recording_thread:
            self.recording_thread.join()
        
        print("Recording stopped")
        self.__save_audio__()

    def __save_audio__(self):
        print("Saving audio...")
        with wave.open(self.out_path, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio_interface.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
        print(f"Audio saved to {self.out_path}")

# Usage Example
if __name__ == "__main__":
    handler = AudioHandler(out_path='output/temp/audio.wav')
    try:
        handler.init_record()
        print("Recording for 10 seconds...")
        import time
        time.sleep(10)  # Simulate other work
        handler.stop_and_save_audio()
    finally:
        del handler
