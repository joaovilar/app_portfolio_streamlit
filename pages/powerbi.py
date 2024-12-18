import msal
import requests
import streamlit as st

# Credenciais da sua aplicação registrada no Azure AD
CLIENT_ID = "faaee941-379d-4603-9b37-a2eca027d32b"
CLIENT_SECRET = "cF38Q~s_SDOynusLB.d1EL-keY6OKLa22dQbza5a"
TENANT_ID = "5560e420-5f71-400c-8bbe-e52fae72eb6c"

# Escopo necessário para acessar a API do Power BI
scopes = ["https://analysis.windows.net/powerbi/api/.default"]

# Autoridade do Azure AD
authority = f"https://login.microsoftonline.com/{TENANT_ID}"

# Função para obter o token de acesso usando o fluxo de credenciais do cliente
def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=authority,
        client_credential=CLIENT_SECRET
    )
    
    # Solicitar o token com o fluxo de credenciais do cliente
    result = app.acquire_token_for_client(scopes=scopes)
    
    if "access_token" in result:
        return result["access_token"]
    else:
        st.error(f"Erro ao obter token de acesso: {result.get('error_description')}")
        return None

# Função para listar relatórios do Power BI
def list_reports():
    token = get_access_token()
    if token is None:
        return

    # Definindo o cabeçalho de autenticação com o token de acesso
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    # API para listar os relatórios
    url = "https://api.powerbi.com/v1.0/myorg/reports"
    
    # Teste: mostrando o token e a URL para confirmar
    st.write("Token obtido: ", token[:30])  # Exibe apenas uma parte do token para depuração
    st.write("Fazendo requisição para: ", url)
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        reports = response.json()
        st.write("Relatórios do Power BI encontrados:")
        for report in reports["value"]:
            st.write(f"Nome: {report['name']}, ID: {report['id']}")
    else:
        st.error(f"Erro ao listar relatórios: {response.status_code} - {response.text}")

# Interface do Streamlit para exibir os relatórios
def main():
    st.title("Listar Relatórios do Power BI")
    
    if st.button("Listar Relatórios"):
        list_reports()

if __name__ == "__main__":
    main()
