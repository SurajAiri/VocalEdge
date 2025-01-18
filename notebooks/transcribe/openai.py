import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Specify the path to your audio file
audio_file = "path_to_your_audio_file.mp3"

# Open the audio file in binary mode
with open(audio_file, "rb") as file:
    # Use OpenAI's Whisper API
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=file
    )

# Print the transcription
print("Transcription:")
print(response["text"])

# pip install openai