import streamlit as st

# Title of the application
st.title("Login")

# Login fields
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Login button
if st.button("Login"):
    if username == "admin" and password == "admin":
        st.success("Login realizado com sucesso!")
        # Redirecionar para a janela de ações
        st.experimental_rerun()
    else:
        st.error("Usuário ou senha incorretos")
