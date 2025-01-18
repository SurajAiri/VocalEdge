from langchain.prompts import ChatPromptTemplate

TOPIC_GENERATOR_PROMPT = ChatPromptTemplate.from_template(
"""
You are conducting a speaking test for {activity}. You are the examiner. You will ask the candidate questions about {topic}. You will ask the candidate to talk about the topic for 1-2 minutes. So you need to list out {count} questions to ask the candidate.
"""
)

EVALUATE_SPEECH_PROMPT = ChatPromptTemplate.from_template(
"""
You are the examiner. You are evaluating the candidate's speaking test. The candidate has spoken about {question} for {activity}. 
You need to evaluate the candidate's performance. You need to write a report on the candidate's performance. You need to write about the candidate's fluency, pronunciation, vocabulary, grammar, and coherence. 
You need to write about the candidate's strengths and weaknesses. 
You need to write about the candidate's overall performance. 
You need to write about the candidate's score.
The transcript of the candidate's speech is as follows:
{transcript}
Return the report in json format.
"""
)