from langchain_community.llms import OpenLLM
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langfuse.callback import CallbackHandler
import openllm
import streamlit as st
import os

# LANGFUSE_HOST = os.environ.get("LANGFUSE_HOST")
# LANGFUSE_PUBLIC_KEY = os.environ.get("LANGFUSE_PUBLIC_KEY")
# LANGFUSE_SECRET_KEY = os.environ.get("LANGFUSE_SECRET_KEY")
OPENLLM_HOST = os.environ.get("OPENLLM_HOST")
OPENLLM_PORT = os.environ.get("OPENLLM_PORT")


# handler = CallbackHandler(LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY)

# handler.auth_check()

server_url = f"http://{OPENLLM_HOST}:{OPENLLM_PORT}"

def generate_response_langchain(input_text):
    llm = OpenLLM(server_url=server_url)
    st.info(llm(input_text))

def generate_response_openllm(input_text):
    client = openllm.client.HTTPClient('http://localhost:3000')
    ret = client.query('Explain to me the difference between "further" and "farther"')
    st.info(ret)

with st.form("my_form"):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response_openllm(text)