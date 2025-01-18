import streamlit as st
from src.activity.activity_model import Activity
from src.llm.model_runner import ModelRunner
from src.ui import Navigator
from src.utils.enums import AppScreen

def navigate_to(screen:AppScreen):
    st.session_state.screen = screen

def current_screen():
    return st.session_state.screen

def home_on_activity_choose(activity:Activity):
    global llmRunner
    st.session_state.done_preparation = False
    st.session_state.activity = activity.toJson()
    question = llmRunner.generate_question(activity.title, activity.promptTopic, activity.questionCount)
    # print(question.content)
    # question = {}
    # question['content'] = "What is your name?"
    st.session_state.question = question.content
    # st.session_state.question = "question.content"
# 
    navigate_to(AppScreen.PARTICIPATE)
    # navigate_to(AppScreen.RESULT)

def participate_test_complete():
    navigate_to(AppScreen.RESULT)


def navigation_logic():
    if AppScreen.PARTICIPATE == st.session_state.screen:
        Navigator.ParticipateScreen(on_act_complete=participate_test_complete)
    elif AppScreen.RESULT == st.session_state.screen:
        Navigator.ResultScreen()
    elif AppScreen.ABOUT == st.session_state.screen:
        Navigator.AboutScreen()
    else:
        st.session_state.question = None
        Navigator.HomeScreen(on_act_choose=home_on_activity_choose)

def sidebar_logic():
    scr = current_screen()
    if scr != AppScreen.PARTICIPATE:
        st.sidebar.title("Navigation")
        if scr != AppScreen.HOME:
            st.sidebar.button("Home",on_click=lambda: navigate_to(AppScreen.HOME))
        if scr != AppScreen.ABOUT:
            st.sidebar.button("About Us",on_click=lambda: navigate_to(AppScreen.ABOUT))


def main():
    global llmRunner
    if "is_working" not in st.session_state:
        st.session_state.is_working = False

    if 'done_preparation' not in st.session_state:
        st.session_state.done_preparation = False

    if "screen" not in st.session_state:
        st.session_state.screen = AppScreen.HOME
    st.set_page_config(layout="wide")
    

    llmRunner = ModelRunner()

    sidebar_logic()
    navigation_logic()
    

if __name__ == "__main__":
    main() 