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
    Please select "Open AI" or "CSV Agent" from left side bar to analyze your data</h5>

    Open AI - With Open AI agent, the data is sent to OpenAI and answers are returned by OpenAI
    CSV Agent - Uses Open AI to understand the question, and then uses the response from OpenAI to query the data (data is NOT sent to OpenAI)
    """,
    unsafe_allow_html=True,
)
st.markdown("---")
