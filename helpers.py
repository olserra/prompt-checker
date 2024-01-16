from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

def generate_content(api_key, generation_prompt):
    chat = ChatOpenAI(temperature=0, openai_api_key=api_key, model_name='gpt-3.5-turbo')
    messages = [
        SystemMessage(content=generation_prompt)
    ]
    response = chat(messages)
    return response.content


def qa_analysis(api_key, content_to_be_reviewed, criteria_prompt):
    chat = ChatOpenAI(temperature=0, openai_api_key=api_key, model_name='gpt-4')

    final_prompt = f"""
            You are a QA Analyst and you need to make sure that the following acceptance criteria is met by the content
            below. The expected result is the list of unmet criteria found or "valid" if everything was met. No 
            explanation needed.

            # Acceptance Criteria are the following
            ---
            {criteria_prompt}
            ---
            # Content to be validated is the following
            ---
            {content_to_be_reviewed}
            ---
            """

    messages = [
        SystemMessage(
            content=final_prompt,
        )
    ]

    response = chat(messages)
    return response.content
