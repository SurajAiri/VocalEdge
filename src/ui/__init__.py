from src.llm.model_runner import ModelRunner
from src.ui.home_screen import home_screen
from src.ui.participate_screen import participate_ui
from src.ui.result_screen import result_screen
from src.ui.about_screen import about_screen

class Navigator:

    @staticmethod
    def HomeScreen(on_act_choose):
        return home_screen(on_act_choose)
    
    @staticmethod
    def ParticipateScreen( on_act_complete):
        return participate_ui( on_act_complete)
    
    @staticmethod
    def ResultScreen():
        return result_screen()
    
    @staticmethod
    def AboutScreen():
        return about_screen()
