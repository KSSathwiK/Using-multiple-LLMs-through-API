import requests
import streamlit as st

def get_llama2(input_text):
    response=requests.post("http://localhost:8000/generation1/invoke",
                           json={'input':{'query':input_text}})
    
    return response.json()['output']


def get_codegemma(input_text):
    response=requests.post("http://localhost:8000//generation2/invoke",
                           json={'input':{'query':input_text}})
    
    return response.json()['output']


st.title("Llama2 & Gemma2 Bot through Langchain")
input_text1=st.text_input("Chat with Llama2")
input_text2=st.text_input("Chat with Gemma2")

if input_text1:
    st.write(get_llama2(input_text1))

if input_text2:
    st.write(get_codegemma(input_text2))