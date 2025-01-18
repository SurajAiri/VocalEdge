import streamlit as st
from streamlit_extras.let_it_rain import rain

# Data for the report
data = {
    "fluency": {
        "score": 6,
        "evaluation": "The candidate speaks at a generally steady pace with occasional hesitations. While they manage to convey their thoughts, some sentences are incomplete or difficult to understand, affecting overall fluency."
    },
    "pronunciation": {
        "score": 5,
        "evaluation": "The candidate's pronunciation is mostly clear, but there are instances of mispronounced words that hinder understanding. Issues such as 'vogity' and 'travel our foot' demonstrate some challenges in pronunciation."
    },
    "vocabulary": {
        "score": 6,
        "evaluation": "The candidate uses a variety of vocabulary related to technology and its impact on daily life. However, some phrases are awkwardly constructed, such as 'e-commerce size' and 'real time drama,' showing limited flexibility in vocabulary usage."
    },
    "grammar": {
        "score": 5,
        "evaluation": "The candidate exhibits basic grammar skills but struggles with sentence structure and coherence. Issues arise with verb tenses and sentence fragments that affect grammatical accuracy."
    },
    "coherence": {
        "score": 5,
        "evaluation": "Overall coherence is somewhat lacking, as transitions between ideas are unclear. The candidate jumps between topics—such as shopping, transportation, and entertainment—without smooth links, making it hard to follow the main argument."
    },
    "strengths": "The candidate demonstrates a clear understanding of the topic and presents relevant examples of technology's impact on daily life. They express a positive attitude towards technology when used wisely.",
    "weaknesses": "Pronunciation errors and grammatical inaccuracies reduce overall clarity. Additionally, the flow of ideas could be improved for better coherence. Some statements are vague or awkwardly phrased, which impacts overall communication.",
    "overall_performance": {
        "score": 5.5,
        "evaluation": "The candidate shows a fair understanding of the topic and has moments of clarity and relevance. However, improved fluency, coherence, and grammatical accuracy are needed for a stronger presentation."
    }
}

# Streamlit UI
st.set_page_config(page_title="Candidate Performance Report", layout="wide")

# Add animation for visual appeal
rain(emoji="🌟", font_size=54, falling_speed=5, animation_length="infinite")

# Title Section
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Candidate Performance Report</h1>", unsafe_allow_html=True)

# Performance Breakdown
st.markdown("<h2 style='text-align: center; color: #FF5722;'>Performance Breakdown</h2>", unsafe_allow_html=True)

# # Card-style display for categories
# for category, details in data.items():
#     if isinstance(details, dict):
#         st.markdown(
#             f"""
#             <div style="border: 1px solid #E0E0E0; border-radius: 10px; padding: 20px; margin: 10px 0; background-color: #F9F9F9;">
#                 <h3 style="color: #009688;">{category.capitalize()} (Score: {details['score']})</h3>
#                 <p style="color: #607D8B;">{details['evaluation']}</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# Card-style display for categories in two columns
col1, col2 = st.columns(2)
categories = list(data.items())
midpoint = len(categories) // 2 -1

# Left column
with col1:
    for category, details in categories[:midpoint]:
        if isinstance(details, dict):
            st.markdown(
                f"""
                <div style="border: 1px solid #D3D3D3; border-radius: 10px; padding: 20px; margin: 10px 0; background-color: #0f0f0f;">
                    <h3 style="color: #009688;">{category.capitalize()} (Score: {details['score']})</h3>
                    <p style="color: #607D8B;">{details['evaluation']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Right column
with col2:
    for category, details in categories[midpoint:]:
        if isinstance(details, dict):
            st.markdown(
                f"""
                <div style="border: 1px solid #D3D3D3; border-radius: 10px; padding: 20px; margin: 10px 0; background-color: #F0F0F0;">
                    <h3 style="color: #009688;">{category.capitalize()} (Score: {details['score']})</h3>
                    <p style="color: #607D8B;">{details['evaluation']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Strengths and Weaknesses
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='color: #2196F3;'>Strengths</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #455A64;'>{data['strengths']}</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='color: #E91E63;'>Weaknesses</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #455A64;'>{data['weaknesses']}</p>", unsafe_allow_html=True)

# Overall Performance
st.markdown("<h2 style='text-align: center; color: #9C27B0;'>Overall Performance</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 20px; color: #673AB7;'><strong>Score:</strong> {data['overall_performance']['score']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #3E2723;'>{data['overall_performance']['evaluation']}</p>", unsafe_allow_html=True)
