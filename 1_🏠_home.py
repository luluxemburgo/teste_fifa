import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import webbrowser

# --- CONFIGURAÇÃO DE LOGIN ---
names = ['Lucas Carvalho', 'Aline Gomes']
usernames = ['lucas.carvalho', 'aline.gomes']

hashed_passwords = [
    '$2b$12$U3eBp2.nEXL0Af2ffNe9SeQSKS2VnYaNPYbUjE6O3vVlg5WzSY54.',  # lucasmu1
    '$2b$12$GBEq7/VhEmNjSvbTviR7TObB/dWgh9o1YxHlmOj4Jv2EJ5ORRBF8q'   # aline1
]

credentials = {
    "usernames": {
        usernames[0]: {"name": names[0], "password": hashed_passwords[0]},
        usernames[1]: {"name": names[1], "password": hashed_passwords[1]},
    }
}

# --- AUTENTICADOR ---
authenticator = stauth.Authenticate(
    credentials,
    "projeto_fifa",  # nome do cookie
    "12345",         # chave do cookie
    1                # dias de expiração
)

# --- LOGIN ---
authenticator.login(location='main')

# --- VERIFICA STATUS DE AUTENTICAÇÃO ---
if st.session_state["authentication_status"]:
    st.success(f"Bem-vindo(a), {st.session_state['name']}!")

    if 'data' not in st.session_state:
        df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
        st.session_state['data'] = df_data

    st.markdown(" <span style='font-size:30px'> :soccer: **FIFA** :rainbow[Official Data Set] :soccer: </span>", unsafe_allow_html=True)
    st.sidebar.markdown("Desenvolvido por [Loja do Pedrão](https://www.lojadopedrao.com.br)")

    if st.button("Acesse os dados do Kaggle"):
        webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

    st.markdown("""
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais.

    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes. 

    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol.
    """)

elif st.session_state["authentication_status"] is False:
    st.error("Usuário ou senha inválidos.")

elif st.session_state["authentication_status"] is None:
    st.warning("Por favor, insira suas credenciais.")