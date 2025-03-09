import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

link = os.getenv('LINK')
user_login = os.getenv('USER_LOGIN')
user_pw = os.getenv('USER_PASSWORD')
file_path = os.getenv('XLSX_FILEPATH')


# Title of the application
st.title("Credenciais para o SGF")

# Login fields
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Function to verify login credentials
def verify_login(username, password):
    url = link  # Replace with the actual login URL
    payload = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        st.error(f"Erro de conexão: {e}")
        return False

# Login button
if st.button("Login"):
    if verify_login(username, password):
        st.success("Credenciais validadas com sucesso!")
        # Redirecionar para a janela de ações
    else:
        st.error("Usuário ou senha incorretos")