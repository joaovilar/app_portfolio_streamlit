import pyodbc
import streamlit as st

# Definindo o servidor, banco de dados e as credenciais fixas no código
server = 'azure-sql-dev-1.database.windows.net'
database = 'login'
db_username = 'sqladmin'  # Substitua pelo usuário fixo
db_password = '153759Df.'  # Substitua pela senha segura

# Função para conectar ao banco de dados (com usuário fixo)
def conectar_ao_banco():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};PORT=1433;DATABASE={database};'
            f'UID={db_username};PWD={db_password}'
        )
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para validar o login e obter o nome do usuário
def validar_login_e_obter_nome(conn, username, password):
    try:
        cursor = conn.cursor()
        # Consulta para verificar o usuário e buscar o campo 'nome'
        query = "SELECT nome FROM tbusuario WHERE usuario = ? AND senha = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone() 
        if result:
            return result[0]  # Retorna o valor do campo 'nome'
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao verificar as credenciais: {e}")
        return None

# Inserindo o CSS customizado para melhorar o design e posicionar o botão de logout no topo
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Arial', sans-serif;
            padding-top: 50px;  /* Espaçamento para o botão de logout */
        }

        .stTextInput, .stPasswordInput {
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
            font-size: 16px;
        }

        .stTextInput input, .stPasswordInput input {
            border: 2px solid #5b8bff;
            background-color: #fff;
        }

        .stButton button {
            background-color: #5b8bff;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s;
        }

        .stButton button:hover {
            background-color: #4771e2;
        }

        .stSuccess, .stError {
            font-size: 18px;
            font-weight: bold;
        }

        h1 {
            color: #5b8bff;
            text-align: center;
            margin-bottom: 50px;
        }

        /* Estilo para o botão de logout fixado no topo */
        .logout-button {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #ff4d4d;
            color: white;
            padding: 5px 10px;
            font-size: 12px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }

        .logout-button:hover {
            background-color: #e60000;
        }

        /* Posicionando o título de boas-vindas e outros elementos */
        .welcome-section {
            margin-top: 70px; /* Ajusta a posição do título e conteúdo abaixo */
            padding-right: 50px;  /* Espaço para não encostar no botão de logout */
        }
    </style>
""", unsafe_allow_html=True)

# Função para exibir a página de boas-vindas
def pagina_bem_vindo():
    # Colocando o botão de logout no canto superior direito
    if st.button("Deslogar"):
        st.session_state.clear()  # Limpa todas as variáveis de sessão
        st.rerun()  # Recarrega a página para voltar ao login
    
    st.title("Bem-vindo!")
    st.write(f"Olá, {st.session_state.nome}!")  # Exibe o nome em vez do nome de usuário

# Tela de login no Streamlit
def pagina_login():
    # Se o usuário já estiver logado, redireciona para a página de boas-vindas
    if 'username' in st.session_state:
        pagina_bem_vindo()
    else:
        st.title("Login")

        username = st.text_input("Digite o nome de usuário")
        password = st.text_input("Digite a senha", type="password")

        if st.button("Conectar"):
            if username and password:
                conn = conectar_ao_banco()
                if conn:
                    # Valida o login diretamente na tabela tbusuario
                    nome = validar_login_e_obter_nome(conn, username, password)
                    if nome:
                        st.session_state.username = username  # Salva o nome de usuário na sessão
                        st.session_state.nome = nome  # Salva o nome na sessão
                        st.session_state.logged_in = True  # Marca o usuário como logado
                        st.success("Login bem-sucedido!")
                        st.rerun()  # Faz o Streamlit recarregar a página
                    else:
                        st.error("Nome de usuário ou senha incorretos.")
                else:
                    st.error("Não foi possível conectar ao banco de dados.")
            else:
                st.error("Por favor, preencha todos os campos.")

# Chama a função principal da aplicação
pagina_login()
