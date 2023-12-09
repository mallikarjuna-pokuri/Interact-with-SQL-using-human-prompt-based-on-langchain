
import streamlit as st
from main import chain


st.title("Hospital Database ")

question = st.text_input("Question: ")

if question:
    response = chain(question)

    st.header("Answer")
    st.write(response['result'])
    st.subheader("SQL Query is ")
    st.write(response["intermediate_steps"][1])
