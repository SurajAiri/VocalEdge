import streamlit as st
from src.activity.activity_model import Activity
from src.utils.data_handler import DataHandler
from src.utils.constants import APP_TITLE, APP_TAGLINE

def activity_button_view(activity:Activity, on_click):
    """
    Custom button view for each activity with functionality on click.
    """
    st.markdown(
        f"""
        <div style="border: 2px solid #ccc; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 15px;">
            <h3>{activity.title}</h3>
            <p>{activity.description}</p>
            <p><strong>Topic:</strong> {activity.promptTopic}</p>
            <p><strong>Questions:</strong> {activity.questionCount}</p>
            <p><strong>Preparation Time:</strong> {activity.prepareTime} sec</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Button with custom functionality
    st.button(f"Start {activity.title}",on_click=lambda: on_click(activity), key=activity.title)
        # st.rerun()


        
def home_screen(on_activity_choose):
    activities = DataHandler.get_activities()

    st.title(APP_TITLE)
    st.write(APP_TAGLINE)

    # st.write("## Activities")
    st.write("Choose an activity to practice speaking.")
    # st.write("Click on the activity to start practicing.")

    # Arrange activities in a grid
    cols = st.columns(2)  # Adjust the number of columns as needed

    for idx, activity in enumerate(activities):
        with cols[idx % len(cols)]:
            activity_button_view( activity,on_click=on_activity_choose)

    # Display current activity status
    st.markdown("----")

