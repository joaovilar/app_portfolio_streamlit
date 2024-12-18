import streamlit as st
from azure.storage.filedatalake import DataLakeServiceClient

# Configuração da página
st.set_page_config(page_title="Gerenciamento de Arquivos no Azure Data Lake", layout="wide")

# Título da aplicação
st.title("Gerenciamento de Arquivos no Azure Data Lake")

st.markdown("<hr style='border-top: 3px solid #1E90FF; margin-top: 0;'>", unsafe_allow_html=True)

# Função para conectar ao Azure Data Lake
def connect_to_datalake(account_name, account_key):
    try:
        service_client = DataLakeServiceClient(
            account_url=f"https://{account_name}.dfs.core.windows.net",
            credential=account_key
        )
        return service_client
    except Exception as e:
        st.error(f"Erro ao conectar ao Azure Data Lake: {e}")
        return None

# Função para listar containers
def list_file_systems(service_client):
    try:
        file_systems = []
        file_systems_client = service_client.list_file_systems()
        for fs in file_systems_client:
            file_systems.append(fs.name)
        return file_systems
    except Exception as e:
        st.error(f"Erro ao listar containers: {e}")
        return []

# Função para listar diretórios dentro de um container
def list_directories(service_client, container_name):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container_name)
        paths = file_system_client.get_paths()
        directories = [path.name for path in paths if path.is_directory]
        return directories
    except Exception as e:
        st.error(f"Erro ao listar diretórios no container '{container_name}': {e}")
        return []

# Função para listar arquivos dentro de um diretório
def list_files_in_directory(service_client, container_name, directory_name):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container_name)
        paths = file_system_client.get_paths(path=directory_name)
        files = [path.name for path in paths if not path.is_directory]
        return files
    except Exception as e:
        st.error(f"Erro ao listar arquivos no diretório '{directory_name}': {e}")
        return []

# Função para fazer upload do arquivo
def upload_file(service_client, container_name, directory_name, file):
    try:
        file_system_client = service_client.get_file_system_client(file_system=container_name)

        # Definir o caminho do arquivo
        if directory_name == "Raiz (sem diretório)" or not directory_name:
            file_path = file.name  # Caminho direto na raiz
        else:
            file_path = f"{directory_name}/{file.name}"

        # Criando ou atualizando o arquivo no caminho especificado
        file_client = file_system_client.get_file_client(file_path)
        file_client.create_file()
        file_client.append_data(file.read(), 0)
        file_client.flush_data(len(file.read()))

        st.success(f"Arquivo '{file.name}' enviado com sucesso para '{file_path}' no container '{container_name}'!")
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo: {e}")

# Entrada para nome da conta e chave
account_name = st.text_input("Nome da conta do Data Lake")
account_key = st.text_input("Chave da conta", type="password")

# Verifica se os campos de entrada não estão vazios
if account_name and account_key:
    service_client = connect_to_datalake(account_name, account_key)

    if service_client:
        # Listando os containers
        file_systems = ["Selecione um container"] + list_file_systems(service_client)
        container_name = st.selectbox("Escolha o container", file_systems)

        if container_name != "Selecione um container":
            # Listando os diretórios no container selecionado
            directories = ["Raiz (sem diretório)"] + list_directories(service_client, container_name)
            directory_name = st.selectbox("Escolha o diretório", directories)
            selected_directory = "" if directory_name == "Raiz (sem diretório)" else directory_name

            if directory_name:
                # Listando arquivos no diretório selecionado
                st.subheader(f"Arquivos no diretório {selected_directory}:")
                files = list_files_in_directory(service_client, container_name, selected_directory)

                if files:
                    for file_name in files:
                        st.write(f"- {file_name}")
                else:
                    st.write("Nenhum arquivo encontrado no diretório.")

                # Permitir upload de arquivo para o diretório selecionado
                file = st.file_uploader("Escolha um arquivo para fazer o upload", type=["json", "csv", "txt", "xlsx"])

                if file:
                    if st.button("Fazer upload"):
                        upload_file(service_client, container_name, selected_directory, file)
