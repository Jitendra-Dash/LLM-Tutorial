import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM

load_dotenv()  # Load environment variables from .env file

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
# Set page config
st.set_page_config(page_title="Chat with Llama 🤖", page_icon="🤖", layout="centered", )

# Your title and input
st.title('Chat with Llama')
input_text = st.text_input("Ask Llama")

# ollama LLAma2 LLm 
llm=OllamaLLM(model="llama3.2:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

