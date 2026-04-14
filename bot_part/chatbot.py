import streamlit as st

st.title('AGENT')

demande_utilisateur = st.chat_input("écris-ici")
reponse_LLM = 'non'

if demande_utilisateur:
    st.write(f'utilisateur: {demande_utilisateur}')
    st.write(f'assistant: {reponse_LLM}')

