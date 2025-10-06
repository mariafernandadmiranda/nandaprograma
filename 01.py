import streamlit as st


st.write("Oie mundo")

nome = st.text_input("Poderia digitar seu nome, por favor?!")
if nome:
  st.write(nome.upper())
