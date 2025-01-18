import asyncio
import whisper
import librosa 

class Transcriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file):
        audio = self.load_audio(audio_file)
        return self.model.transcribe(audio)
    
    def load_audio(self, audio_file):
        """Load the audio file and return it as a NumPy array."""
        audio, _ = librosa.load(audio_file, sr=16000, mono=True)
        return audio
    
    def transcribe_with_timestamps(self, audio_file, output_file,save_only=False):
        audio = self.load_audio(audio_file)
        result = self.model.transcribe(audio)
        transc = []
        with open(output_file, "w") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
                if not save_only:
                    transc.append(f"[{start:.2f}s - {end:.2f}s]: {text}\n")

        return transc
    
    async def transcribe_async(self, audio_file, output_file, callback=None, save_only=True):
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.model.transcribe, audio_file)
        transc = []
        with open(output_file, "w") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
                if not save_only:
                    transc.append(f"[{start:.2f}s - {end:.2f}s]: {text}\n")

        if callback:
            callback()

        return transc
    
    def __del__(self):
        del self.model

