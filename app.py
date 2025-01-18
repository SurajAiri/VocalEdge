import streamlit as st
from src.activity.activity_model import Activity
from src.ui import Navigator
from src.utils.enums import AppScreen

def navigate_to(screen:AppScreen):
    st.session_state.screen = screen

def current_screen():
    return st.session_state.screen

def home_on_activity_choose(activity:Activity):
    navigate_to(AppScreen.PARTICIPATE)
    st.session_state.activity = activity.toJson()
    # st.rerun()

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
    if "is_working" not in st.session_state:
        st.session_state.is_working = False

    if "screen" not in st.session_state:
        print("no session screen found")
        st.session_state.screen = AppScreen.HOME

    sidebar_logic()
    navigation_logic()
    

if __name__ == "__main__":
    main() 