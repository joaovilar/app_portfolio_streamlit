import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
import io

# Conectar ao Azure Data Lake
def connect_to_datalake(account_name, account_key):
    try:
        service_client = DataLakeServiceClient(
            account_url=f"https://{account_name}.dfs.core.windows.net",
            credential=account_key
        )
        return service_client
    except Exception as e:
        print(f"Erro ao conectar ao Azure Data Lake: {e}")
        return None

# Ler arquivo JSON diretamente do Data Lake
def read_json_from_datalake(service_client, filesystem_name, file_path):
    try:
        filesystem_client = service_client.get_file_system_client(filesystem_name)
        file_client = filesystem_client.get_file_client(file_path)
        file_content = file_client.download_file().readall()

        # Processar JSON em DataFrame
        data = pd.read_json(io.BytesIO(file_content), convert_dates=False)
        return data
    except Exception as e:
        print(f"Erro ao ler JSON do Data Lake: {e}")
        return None

# Conexão e leitura
account_name = "datalakebikestore"
account_key = "gdrO0Er/Ec8TslO1M7d9ENURLu4p9wov4GL7WrsCWP/Iwxca9I0amu1m1QIOTS57JcMeoZD4rrNA+AStGvOJJw=="
filesystem_name = "json"
file_path = "V_OCORRENCIA_AMPLA.json"

# Estabelecer conexão
service_client = connect_to_datalake(account_name, account_key)

if service_client:
    df = read_json_from_datalake(service_client, filesystem_name, file_path)

    if df is not None:
        # Processar DataFrame como necessário
        print(df.head())
    else:
        print("Erro ao processar o arquivo.")
else:
    print("Erro ao conectar ao Data Lake.")
