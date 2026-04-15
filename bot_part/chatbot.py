import streamlit as st
import requests

st.title('AGENT')

demande_utilisateur = st.chat_input("écris-ici")

if demande_utilisateur:
    st.write(f"utilisateur : {demande_utilisateur}")
    reponse = requests.post('http://localhost:8002/transfert', json={'demande': demande_utilisateur})
    st.write("ok")

