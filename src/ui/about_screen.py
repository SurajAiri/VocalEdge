import streamlit as st

def about_screen():
    st.title("About Us")

    # Introduction
    st.markdown("""
    **Vocal Edge: Master the Art of Speaking** is a web-based application designed to help you master the art of speaking.
    Our goal is to provide you with an interactive and personalized experience to improve your speaking skills through real-time feedback.
    The app uses advanced language models and speech recognition technology to help you enhance your fluency and confidence in speaking.
    """)

    # Team Section
    st.subheader("Our Team")
    st.markdown("""
    - **[Suraj Airi](https://www.linkedin.com/in/suraj-kiran-airi/)**: Creator and Developer of Vocal Edge. Passionate about natural language processing, Gen AI, and improving speaking skills.
    - **Contributors**: We welcome contributions from the community. If you are interested in helping, feel free to reach out!
    """)

    # Technology Section
    st.subheader("Technologies We Use")
    st.markdown("""
    Vocal Edge leverages cutting-edge technologies to provide an excellent user experience:
    - **Streamlit**: For creating the web-based interface.
    - **LangChain**: For natural language processing and understanding.
    - **Whisper**: For speech recognition and analysis.
    - **Ollama**: For advanced language modeling and feedback.
    - **OpenAI**: For leveraging advanced language models to enhance speaking exercises and feedback.
    """)

    # Contact Section
    st.subheader("Contact Us")
    st.markdown("""
    For any questions or feedback, please feel free to reach out:
    - Email: [surajairi.ml@gmail.com](mailto:surajairi.ml@gmail.com)
    """)

    # A little disclaimer or invitation to contribute
    st.markdown("""
    We are always looking for ways to improve Vocal Edge. If you have any suggestions or would like to contribute to the project, please check out our [GitHub Repository](https://github.com/SurajAiri/VocalEdge.git) and feel free to submit issues or pull requests.
    """)
