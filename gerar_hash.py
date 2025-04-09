import streamlit_authenticator as stauth

senhas = ['lucasmu1', 'aline1']

# Aqui passa só a lista direto, sem nome de argumento
hashes = stauth.Hasher(senhas).generate()

for h in hashes:
    print(h)