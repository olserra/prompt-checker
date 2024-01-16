import os
import streamlit as st
from dotenv import load_dotenv
from helpers import generate_content, qa_analysis

load_dotenv()

st.set_page_config(page_title="Prompt Checker", page_icon="🌐")
st.header("Prompt Checker")
st.info("""
        A Streamlit-based Python application designed to test the consistency of prompt generations. Input your OpenAI
        API key, generation prompts, and specify the number of tests to run, ensuring consistent outputs from language
        models.
        """)


def main():
    if os.getenv("OPENAI_API_KEY"):
        openai_api_key = os.getenv("OPENAI_API_KEY")
    else:
        openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

    example_generation_prompt = """
               Create a table with 10 names for startups that combine 'AI and Market Research' and return as a table with 2 columns. The table 
               should be formatted as Markdown content.
               """
    generation_prompt = st.text_area("Enter the generation prompt")
    st.caption(example_generation_prompt)

    example_criteria_prompt = """
               The content is formatted as Markdown. It has a table with 1 column, where the header says 'Startup name', then 10 
               rows with names. Each name should be related somehow to 'AI and Market Research'.
               """
    criteria_prompt = st.text_area("Acceptance Criteria Prompt")
    st.caption(example_criteria_prompt)

    num_tests = st.number_input("Number of tests", min_value=1, value=5)

    if st.button("Run Tests"):
        if openai_api_key and generation_prompt and criteria_prompt:
            for i in range(1, num_tests + 1):
                content = generate_content(openai_api_key, generation_prompt)
                qa_result = qa_analysis(openai_api_key, content, criteria_prompt)

                st.subheader(f"Test {i}")
                with st.expander(f"Generated content"):
                    st.text(content)
                st.text('QA Result')
                st.text(qa_result)

        else:
            st.error("Please fill in all required fields.")


if __name__ == "__main__":
    main()
