# from langchain_ollama.llms import OllamaLLM
from langchain_openai.chat_models import ChatOpenAI
from src.llm.prompts import EVALUATE_SPEECH_PROMPT, TOPIC_GENERATOR_PROMPT

class ModelRunner:
    def __init__(self):
        # self.llm = OllamaLLM(model="phi3.5")
        self.llm = ChatOpenAI(model='gpt-4o-mini')

    def generate_question(self, activity, topic, count):
        prompt = TOPIC_GENERATOR_PROMPT.format(activity=activity, topic=topic, count=count)
        return self.llm.invoke(prompt)
    
    def evaluate_speech(self, question, activity_title,transcript):

        prompt = EVALUATE_SPEECH_PROMPT.format(question=question, activity=activity_title, transcript=transcript)

        return self.llm.invoke(prompt)

