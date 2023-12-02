
import streamlit as st
from main import chain


st.title("Hospital Database ")

question = st.text_input("Question: ")

if question:
    response = chain.run(question)

    st.header("Answer")
    st.write(response)
