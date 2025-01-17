import speech_recognition as sr
import wave
import os

# Initialize recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Filename for saving audio
OUTPUT_FILENAME = "output.wav"

def record_audio():
    print("Recording... Press Ctrl+C to stop.")
    frames = []

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            while True:
                # Record chunks of audio continuously
                audio_data = recognizer.record(source, duration=None)  # No fixed duration
                frames.append(audio_data.get_raw_data())
    except KeyboardInterrupt:
        print("\nRecording stopped manually.")
    return frames

def save_audio(frames, filename):
    # Save recorded audio to a .wav file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(microphone.SAMPLE_WIDTH)
        wf.setframerate(microphone.SAMPLE_RATE)
        wf.writeframes(b''.join(frames))
    print(f"Audio saved as {filename}")

def play_audio(filename):
    # Play the saved audio file
    import simpleaudio as sa

    if not os.path.exists(filename):
        print(f"File {filename} not found!")
        return

    print(f"Playing {filename}...")
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def transcribe_audio(filename):
    # Transcribe the audio file to text
    print("Transcribing audio...")
    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)  # Read the audio file
            text = recognizer.recognize_google(audio)  # Use Google Web Speech API
            print("Transcription:")
            print(text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Main workflow
frames = record_audio()
save_audio(frames, OUTPUT_FILENAME)
play_audio(OUTPUT_FILENAME)
transcribe_audio(OUTPUT_FILENAME)
