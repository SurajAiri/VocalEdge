from src.llm.model_runner import ModelRunner
from dotenv import load_dotenv

from src.utils.data_handler import DataHandler


def main():
    load_dotenv()
    runner = ModelRunner()
    print(runner.generate_question(activity="imprompto",topic="abstract topics like white, black, circle, and other topics also not these as these are already revealed", count=2))
    # print(runner.evaluate_speech("water", "swimming"))


