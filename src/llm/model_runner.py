# from langchain_ollama.llms import OllamaLLM
from langchain_openai.chat_models import ChatOpenAI
from src.llm.prompts import EVALUATE_SPEECH_PROMPT, TOPIC_GENERATOR_PROMPT

class ModelRunner:
    def __init__(self):
        # self.llm = OllamaLLM(model="phi3.5")
        self.llm = ChatOpenAI(model='gpt-4o-mini')

    def generate_question(self, activity, topic, count):
        prompt = TOPIC_GENERATOR_PROMPT.format(activity=activity, topic=topic, count=count)
        # print(prompt)
        return self.llm.invoke(prompt)
    
    def evaluate_speech(self, topic, activity):
        prompt = EVALUATE_SPEECH_PROMPT.format(topic=topic, activity=activity)
        return self.llm.generate(prompt)
    
    
