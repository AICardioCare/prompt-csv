import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

from modules.layout import Layout
from modules.sidebar import Sidebar
from modules.utils import Utilities


# To be able to update the changes made to modules in localhost (press r)
def reload_module(module_name):
    import importlib
    import sys

    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]


layout_module = reload_module("modules.layout")
sidebar_module = reload_module("modules.sidebar")
utils_module = reload_module("modules.utils")

Sidebar = sidebar_module.Sidebar

st.set_page_config(layout="wide", page_icon="❤️", page_title="AI Cardio Care | Speak to your Heart💓")

# Instantiate the main components
layout, sidebar, utils = Layout(), Sidebar(), Utilities()

layout.show_header()

user_api_key = utils.load_api_key()
uploaded_file = utils.handle_upload(["csv"])

if not user_api_key:
    layout.show_api_key_missing()

# Configure the sidebar
sidebar.show_options()
sidebar.about()

if user_api_key and uploaded_file:
    agent = create_csv_agent(OpenAI(temperature=0, openai_api_key=user_api_key), "titanic.csv", verbose=True)
    agent.run("how many rows are there?")
