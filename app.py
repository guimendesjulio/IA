from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="deepseek-r1-distill-llama-70b")


# Parâmetros iniciais da pagina de teste
st.set_page_config(page_title="Chat DeepSeek", layout="centered")
st.title("Teste com DeepSeek")

# Se não tiver session_state messages ele cria como uma lista vazia
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Aqui armazeno o tipo e o conteúdo de cada mensagem na lista criada
messages = st.session_state["messages"]
for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)

# Parâmetros do chat
in_message = st.chat_input("Envie sua pergunta:")
if in_message:
    messages.append(("human", in_message))
    chat = st.chat_message("human")
    chat.markdown(in_message)

    response = llm.invoke(messages).content
    messages.append(("ai", response))

    chat = st.chat_message("ai")
    chat.markdown(response)
