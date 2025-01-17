import whisper
import speech_recognition as sr
from tkinter import Tk, Button, Label, StringVar

class WhisperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whisper Transcription App")

        # Load the Whisper model
        self.model = whisper.load_model("base")
        
        # Initialize the speech recognizer and microphone
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        
        # Variables for audio data and transcription
        self.audio_data = None
        self.transcription = StringVar()
        self.transcription.set("Transcription will appear here.")

        # UI Elements
        self.record_button = Button(root, text="Record", command=self.record_audio, width=20)
        self.record_button.pack(pady=10)

        self.transcribe_button = Button(root, text="Transcribe", command=self.transcribe_audio, width=20)
        self.transcribe_button.pack(pady=10)

        self.exit_button = Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=10)

        self.transcription_label = Label(root, textvariable=self.transcription, wraplength=400, justify="left")
        self.transcription_label.pack(pady=20)

    def record_audio(self):
        try:
            with self.mic as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source)
                self.transcription.set("Recording... Please speak.")
                self.root.update()  # Update UI

                # Capture audio
                audio = self.recognizer.listen(source)
                self.audio_data = audio.get_wav_data()
                self.transcription.set("Recording complete. Ready to transcribe.")
        except Exception as e:
            self.transcription.set(f"Error during recording: {str(e)}")

    def transcribe_audio(self):
        if not self.audio_data:
            self.transcription.set("No audio recorded. Please record first.")
            return

        try:
            # Save audio to a temporary file
            with open("temp_audio.wav", "wb") as f:
                f.write(self.audio_data)

            # Transcribe audio using Whisper
            result = self.model.transcribe("temp_audio.wav")
            self.transcription.set(f"Transcription: {result['text']}")
        except Exception as e:
            self.transcription.set(f"Error during transcription: {str(e)}")

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = WhisperApp(root)
    root.mainloop()
