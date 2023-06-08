import streamlit as st

# Config
st.set_page_config(layout="wide", page_icon="❤️", page_title="AI Cardio Care | Speak to your Heart💓")


# Title
st.markdown(
    """
    <h2 style='text-align: center;'>❤️AI Cardio Care ❤️</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


# Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm AI Cardio Care, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    </h5>

    <br>
    <h5>
    Please select "Open AI" or "CSV Agent" from left side bar to analyze your data
    <br>
    <br>
    Open AI - With Open AI agent, the data is sent to OpenAI and answers are returned by OpenAI
    <br>
    <br>
    CSV Agent - Uses Open AI to generate python code for the user question, and then executes the code against the data (data is NOT sent to OpenAI).

    </h5>
    """,
    unsafe_allow_html=True,
)
st.markdown("---")
