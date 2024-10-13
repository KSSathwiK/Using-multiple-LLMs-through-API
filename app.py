from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate

# from langchain.chat_models import ChatOpenAI

from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

## Opena AI , needs API key which costs
# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"
# )
# model=ChatOpenAI()

## ollama Llam2
llm_1=Ollama(model="llama2")
llm_2=Ollama(model="gemma2:2b")

prompt1 = ChatPromptTemplate.from_template("Provide response from {query}")
prompt2 = ChatPromptTemplate.from_template("Provide response from {query}")



add_routes(
    app,
    prompt1|llm_1,
    path="/generation1"
)

add_routes(
    app,
    prompt2|llm_2,
    path="/generation2"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
