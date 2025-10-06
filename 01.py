import streamlit as st
st.title("esse é o meu progama")

st.write("Oie mundo")

nome = st.text_input("Poderia digitar seu nome, por favor?!")
if nome:
  st.writte(nome.upper())
