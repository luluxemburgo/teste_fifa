import streamlit as st
import streamlit as st
import streamlit_authenticator as stauth

# --- Lista de usuários e senhas (criptografadas)
names = ['Lucas Carvalho', 'Aline Gomes']
usernames = ['lucas.carvalho', 'aline.gomes']

# Criptografando as senhas (você pode gerar novas se quiser)
passwords = stauth.Hasher(['lucasmu', 'aline1']).generate()

# --- Inicializar o autenticador
authenticator = stauth.Authenticate(
    names, usernames, passwords,
    'projeto_fifa', 'abcdef', cookie_expiry_days=1
)

# --- Exibir o formulário de login
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title(f'Oráculo da Loja do Pedrão 🔮')
    st.success(f'Bem-vindo(a), {name}!')
    st.write('Aqui vai o conteúdo exclusivo da empresa...')
    # Exemplo de conteúdo:
    st.write('📦 Estoque: 124 produtos\n💳 Cobranças pendentes: 5\n👥 Novos cadastros hoje: 2')

elif authentication_status is False:
    st.error('Usuário ou senha inválidos.')

elif authentication_status is None:
    st.warning('Por favor, insira suas credenciais.')



st.set_page_config(
    page_title="Jogadores",         
    page_icon="⚽",               
    layout="wide",                
)



df_data = st.session_state["data"]
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clubes',clubes)
df_players = df_data[df_data["Club"] == club]

# Selecionar jogador
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)
player_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stats['Photo'], width = 150)
st.title(player)

st.markdown(f"<p style='font-size:20px;'> <b>Clube: {player_stats['Club']}</b></p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:18px;'> <b>Posição: {player_stats['Position']}</b></p>", unsafe_allow_html=True)
[col1, col2, col3, col4] = st.columns(4)
col1.markdown(f"<p style='font-size:16px;'> <b>Idade: </b>{player_stats['Age']}</p>", unsafe_allow_html=True)
col2.markdown(f"<p style='font-size:16px;'> <b>Altura: </b>{player_stats['Height(cm.)']/100}m</p>", unsafe_allow_html=True)
col3.markdown(f"<p style='font-size:16px;'> <b>Peso: </b>{player_stats['Weight(lbs.)']*0.453:.2f}kg</p>", unsafe_allow_html=True)
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))
[col1, col2, col3, col4] = st.columns(4)



def metric_custom(label, value, cor="#000000", tamanho_valor="14px", tamanho_label="12px"):
    html = f"""
    <div style='text-align: left; padding: 10px'>
        <div style='font-size: {tamanho_label}; color: #666'>{label}</div>
        <div style='font-size: {tamanho_valor}; color: {cor}; font-weight: bold;'>{value}</div>
    </div>
    """
    return html

with col1:
    st.markdown(metric_custom(
        label='Valor de Mercado',
        value=f'£ {player_stats["Value(£)"]:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."),
        tamanho_valor="24px"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(metric_custom(
        label='Remuneração Semanal',
        value=f'£ {player_stats["Wage(£)"]:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."),
        tamanho_valor="24px"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(metric_custom(
        label='Cláusula de Rescisão',
        value=f'£ {player_stats["Release Clause(£)"]:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."),
        tamanho_valor="24px"
    ), unsafe_allow_html=True)

    #col1.metric(label='Valor de Mercado',value=f'£ {player_stats["Value(£)"]:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
    #col2.metric(label='Remuneração Semanal',value =f'£ {player_stats['Wage(£)']:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
    #col3.metric(label='Cláusula de Rescisão',value =f'£ {player_stats['Release Clause(£)']:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))



