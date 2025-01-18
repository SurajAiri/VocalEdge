from langchain.prompts import ChatPromptTemplate

TOPIC_GENERATOR_PROMPT = ChatPromptTemplate.from_template(
"""
You are conducting a speaking test for {activity}. You are the examiner. You will ask the candidate questions about {topic}. You will ask the candidate to talk about the topic for 1-2 minutes. So you need to list out {count} questions to ask the candidate.
"""
)



EVALUATE_SPEECH_PROMPT = ChatPromptTemplate.from_template(
"""
You are an examiner evaluating a candidate's speaking test. The candidate spoke on the topic {question} for the activity {activity}. Your task is to assess the candidate's performance and provide a detailed report.

Evaluation Criteria:
Fluency: Assess the candidate's ability to speak smoothly and maintain a steady pace.
Pronunciation: Evaluate the clarity of speech and correctness of word pronunciation.
Vocabulary: Judge the range and appropriateness of the candidate's vocabulary.
Grammar: Analyze grammatical accuracy and sentence structure.
Coherence: Review the logical flow and connectivity of ideas.
Additional Notes:
Highlight the candidate's strengths and weaknesses.
Provide an overall performance evaluation, including a final score.
Assign scores out of 10 for each criterion.
Transcript:
The candidate’s speech transcript is provided below: {transcript}

Format:
Return the evaluation in JSON format using the following structure:

{{
    "report": {{
        "candidate_performance": {{
            "fluency": {{ "score": null, "evaluation": "" }},
            "pronunciation": {{ "score": null, "evaluation": "" }},
            "vocabulary": {{ "score": null, "evaluation": "" }},
            "grammar": {{ "score": null, "evaluation": "" }},
            "coherence": {{ "score": null, "evaluation": "" }}
        }},
        "overall_performance": {{ "score": null, "evaluation": "" }},
        "strengths": "",
        "weaknesses": "",
        "suggestions": ""
    }}
}}
Guidelines:
Ensure evaluations are concise, clear, and professional.
Focus on actionable feedback.
Use the provided template without modification.
"""
)
# EVALUATE_SPEECH_PROMPT = ChatPromptTemplate.from_template(
# """
# You are the examiner. You are evaluating the candidate's speaking test. The candidate has spoken about {question} for {activity}. 
# You need to evaluate the candidate's performance. You need to write a report on the candidate's performance. You need to write about the candidate's fluency, pronunciation, vocabulary, grammar, and coherence. 
# You need to write about the candidate's strengths and weaknesses. 
# You need to write about the candidate's overall performance. 
# You need to write about the candidate's score.
# The transcript of the candidate's speech is as follows:
# {transcript}
# Return the report in json format.
# Generate a JSON response in the following template, evaluating a candidate's performance in a speaking test:
# {
#     "report": {
#         "candidate_performance": {
#             "fluency": { "score": null, "evaluation": "" },
#             "pronunciation": { "score": null, "evaluation": "" },
#             "vocabulary": { "score": null, "evaluation": "" },
#             "grammar": { "score": null, "evaluation": "" },
#             "coherence": { "score": null, "evaluation": "" },
#             "strengths": "",
#             "weaknesses": "",
#             "overall_performance": { "score": null, "evaluation": "" }
#         }
#     }
# }
# Ensure concise and clear evaluations, assigning scores out of 10 and focusing on strengths, weaknesses, and overall performance.
# """
# )