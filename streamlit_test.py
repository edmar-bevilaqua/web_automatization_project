import streamlit as st
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import warnings

load_dotenv()

link = os.getenv('LINK')
user_login = os.getenv('USER_LOGIN')
user_pw = os.getenv('USER_PASSWORD')
file_path = os.getenv('XLSX_FILEPATH')

warnings.filterwarnings("ignore")

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

st.markdown("<br><br><br>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Adicione o seu arquivo Excel abaixo:", type=["xlsx"])
if uploaded_file is not None:
    temp_df = pd.read_excel(uploaded_file)
    st.write("Escrevendo as primeiras linhas do arquivo Excel:")
    st.write(temp_df.head(5))
    if st.button("Usar este arquivo"):
        df = temp_df.copy()
        st.write("Arquivo Excel carregado com sucesso!")
        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # Col 1 - Operations
        # TODO: Garantee that there is only one N. Op per row (e.g. 1035/1036 cannot exist)
        col1.header("Operações identificadas:")
        list_nop_unique = list(df["N. Op"].unique())
        list_nop_unique = [str(i) for i in list_nop_unique]
        list_nop_unique.sort()
        col1.write(pd.Series(list_nop_unique, name="N. Op"))
        
        # Col 2 - Fazendas
        # TODO: Garantee that there is only one row for each Horto
        col2.header("Hortos Florestais Identificados:")
        list_hortos_unique = df.loc[:, ["Horto", "Projeto"]].drop_duplicates()
        col2.write(list_hortos_unique)