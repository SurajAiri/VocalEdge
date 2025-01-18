import json
import streamlit as st
from pathlib import Path
from src.activity.activity_model import Activity
from src.llm.model_runner import ModelRunner
from src.transcribe.transcribe_audio import Transcriber
from src.utils.constants import TEMP_OUTPUT_DIR

from streamlit_extras.let_it_rain import rain

# flow: 
# 1. transcript of audio
# 2. llm evaluation
# 3. display the result

def transcript_audio():
    audio_path = Path(TEMP_OUTPUT_DIR+ "audio.wav")
    transcript_path = Path(TEMP_OUTPUT_DIR+ "transcription.txt")

    if not audio_path.exists():
        st.error("Audio file not found")
        return
    print('audio path:', audio_path)
    transcriber = Transcriber(model_name="base.en")
    # trans = transcriber.transcribe_with_timestamps(audio_file=audio_path, output_file=transcript_path,save_only=False)
    print("we are here to transcribe")
    trans = transcriber.transcribe_with_timestamps(audio_file=audio_path,output_file=transcript_path,save_only=False)
    print("transcription done")
    return trans


def evaluate_llm():
    transcript = transcript_audio()

    # llm evaluation
    ques = st.session_state.question
    print(ques)
    activity = Activity(st.session_state.activity)
    llmRunner = ModelRunner()
    res = llmRunner.evaluate_speech(question="Role of technology in daily life", transcript=transcript, activity_title=activity.title)
    return res.content


# def result_screen():
#     st.title("Whisper Transcription App")
#     act = Activity(st.session_state.activity)
#     st.subheader(act.title)
#     st.write(act.description)
#     res = evaluate_llm()
#     st.write(st.session_state.question)
#     st.write(res)
#     # for r in res:
#     #     st.write(r)



def score_card(category, details,bg_color = '#OFOFOF'):
    if isinstance(details, dict):
        st.markdown(
            f"""
            <div style="border: 1px solid #D3D3D3; border-radius: 10px; padding: 20px; margin: 10px 0; background-color: {bg_color};">
                <h3 style="color: #009688;">{category.capitalize()} ({details['score']} / 10)</h3>
                <p style="color: #607D8B;">{details['evaluation']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )



def result_screen():
    res = evaluate_llm()
    print("\n\n\n")
    print(res)
    print("\n\n\n")

    try:
        data = json.loads(res)
    except:
        try:
            data = json.loads(res.replace("```","").split("json")[1].strip())
        except:
            st.error("Error in parsing the result")
            return

#     data = {
#     "report": {
#         "candidate_performance": {
#             "fluency": { "score": 6, "evaluation": "The candidate spoke at a steady pace with some hesitations but managed to maintain fluency overall." },
#             "pronunciation": { "score": 6, "evaluation": "Most words were pronounced clearly, but there were a few mispronunciations that affected clarity." },
#             "vocabulary": { "score": 5, "evaluation": "The vocabulary used was sufficient for the topic, but there were moments of repetition and limited range." },
#             "grammar": { "score": 5, "evaluation": "There were several grammatical errors and awkward phrases that hindered understanding, such as 'travel our foot' and 'in vogity for negative'." },
#             "coherence": { "score": 6, "evaluation": "Overall ideas were presented logically, but transitions between points were sometimes unclear, leading to confusion." }
#         },
#         "overall_performance": { "score": 5.6, "evaluation": "The candidate demonstrated a basic understanding of the role of technology in daily life but needs improvement in clarity and overall coherence." },
#         "strengths": "The candidate showed a good structure in their argumentation and conveyed enthusiasm for the subject matter.",
#         "weaknesses": "There were noticeable grammatical errors, some pronunciation issues, and a limited vocabulary range that affected the overall clarity of the speech.",
#         "suggestions": "To improve, the candidate should focus on enhancing their vocabulary, practicing grammar for clearer expression, and working on smoother transitions between ideas."
#     }
# }

    # Add animation for visual appeal
    rain(emoji="🌟", font_size=54, falling_speed=5, animation_length="infinite")

    # Title Section
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Candidate Performance Report</h1>", unsafe_allow_html=True)

    # Performance Breakdown
    st.markdown("<h2 style='text-align: center; color: #FF5722;'>Performance Breakdown</h2>", unsafe_allow_html=True)

    data = data["report"]
    col1, col2 = st.columns(2)
    categories = list(data["candidate_performance"].items())
    midpoint = len(categories) // 2

    # Left column
    with col1:
        for category, details in categories[:midpoint]:
            score_card(category, details)

    # Right column
    with col2:
        for category, details in categories[midpoint:]:
            score_card(category, details,bg_color='#F0F0F0')



    # Strengths and Weaknesses
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='color: #2196F3;'>Strengths</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #ffffff;'>{data['strengths']}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='color: #E91E63;'>Weaknesses</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #ffffff;'>{data['weaknesses']}</p>", unsafe_allow_html=True)

    # Overall Performance Section
    st.markdown(
        """
        <div style="text-align: center; margin: 20px 0; padding: 20px; border: 2px solid #4CAF50; border-radius: 15px; background-color: #E8F5E9;">
            <h2 style="color: #4CAF50;">Overall Performance</h2>
            <p style="font-size: 24px; color: #388E3C; margin: 10px 0;">
                <strong>Score:</strong> {score} / 10
            </p>
            <p style="font-size: 18px; color: #2E7D32; margin: 10px 0;">
                {evaluation}
            </p>
        </div>
        """.format(
            score=data["overall_performance"]["score"],
            evaluation=data["overall_performance"]["evaluation"],
        ),
        unsafe_allow_html=True,
    )



            