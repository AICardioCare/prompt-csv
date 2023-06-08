import os

import pandas as pd
import streamlit as st

from modules.chatbot import Chatbot
from modules.embedder import Embedder


class Utilities:
    @staticmethod
    def load_api_key():
        """
        Loads the OpenAI API key from the user's input and returns it
        """
        if hasattr(st.session_state, "api_key") and st.session_state.api_key is not None:
            user_api_key = st.session_state.api_key
            st.sidebar.success("API key loaded from previous input", icon="🚀")
        else:
            user_api_key = st.sidebar.text_input(
                label="#### Your OpenAI API key 👇",
                placeholder="sk-...",
                type="password",
            )
            if user_api_key:
                st.session_state.api_key = user_api_key

        return user_api_key

    @staticmethod
    def handle_upload(file_types):
        """
        Handles and display uploaded_file
        :param file_types: List of accepted file types, e.g., ["csv"]
        """
        uploaded_file = st.sidebar.file_uploader("upload", type=file_types, label_visibility="collapsed")
        if uploaded_file is not None:

            def show_csv_file(uploaded_file):
                file_container = st.expander("Your CSV file :")
                uploaded_file.seek(0)
                shows = pd.read_csv(uploaded_file)
                file_container.write(shows.head())

            show_csv_file(uploaded_file)

        else:
            st.session_state["reset_chat"] = True

        # print(uploaded_file)
        return uploaded_file

    @staticmethod
    def setup_chatbot(uploaded_file, model, temperature, openai_api_key):
        """
        Sets up the chatbot with the uploaded file, model, and temperature
        """
        embeds = Embedder()

        with st.spinner("Processing..."):
            uploaded_file.seek(0)
            file = uploaded_file.read()
            # Get the document embeddings for the uploaded file
            vectors = embeds.getDocEmbeds(file, uploaded_file.name)

            # Create a Chatbot instance with the specified model and temperature
            chatbot = Chatbot(model, temperature, vectors, openai_api_key)
        st.session_state["ready"] = True

        return chatbot
