from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

def get_llm():
    return ChatGroq(model="llama-3.1-8b-instant")
    #return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    #return ChatGroq()


if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("What is the capital of France?")
    print(response)