import whisper
import speech_recognition as sr
import torch

def transcribe_realtime():
    # Load the Whisper model (adjust model size as needed)
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for real-time transcription. Press Ctrl+C to stop.")
    
    try:
        while True:
            with mic as source:
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source)
                print("Speak now...")
                
                # Capture audio
                audio = recognizer.listen(source)
                print("Processing audio...")

                # Convert audio to WAV for Whisper compatibility
                audio_data = audio.get_wav_data()
                
                # Save audio to a temporary file
                with open("temp_audio.wav", "wb") as f:
                    f.write(audio_data)

                # Transcribe audio using Whisper
                result = model.transcribe("temp_audio.wav")
                transcription = result["text"]
                print(f"Transcription: {transcription}")

    except KeyboardInterrupt:
        print("\nReal-time transcription stopped.")

if __name__ == "__main__":
    transcribe_realtime()

