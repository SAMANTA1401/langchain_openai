## Intregrate out code with opoenai api
import os
from constants import openai_key
# from langchain.llms import OpenAi
from langchain_openai import ChatOpenAI

import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key
#streamlit framework
st.title('langchain demo with openai api')
input_text = st.text_input('Enter your text here')


##openai llms
llm = ChatOpenAI(temperature=0.8)

if input_text:
    st.write(llm.invoke(input_text))