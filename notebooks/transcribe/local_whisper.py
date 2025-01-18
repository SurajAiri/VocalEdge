import whisper

# Load the Whisper model
model = whisper.load_model("base")  # You can choose "tiny", "base", "small", "medium", "large"

# Specify the path to your audio file
audio_file = "output/temp/audio.wav"  # Supported formats: .mp3, .wav, .m4a, etc.

# Transcribe the audio
result = model.transcribe(audio_file)

# Print the transcription
print("Transcription:")
print(result["text"])


for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    text = segment["text"]
    print(f"[{start:.2f}s - {end:.2f}s]: {text}")

output_file = "output/temp/transcription_with_timestamps.txt"
with open(output_file, "w") as f:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        f.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
