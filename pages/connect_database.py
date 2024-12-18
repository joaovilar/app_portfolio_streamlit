import streamlit as st
import pyodbc
import pandas as pd

# Configuração para deixar a página mais larga
st.set_page_config(layout="wide")

# Tela Streamlit
st.title('Database Manager')
st.header('Conectar ao Banco de Dados no Azure')

# Função para conectar ao banco de dados no Azure
@st.cache_resource
def connect_to_azure_sql(server, database, username, password):
    try:
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para listar tabelas
def get_table_details(conn):
    try:
        query = """
        SELECT 
            TABLE_CATALOG AS [Banco de Dados],
            TABLE_SCHEMA AS [Esquema],
            TABLE_NAME AS [Nome da Tabela],
            TABLE_TYPE AS [Tipo da Tabela]
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
        ORDER BY TABLE_SCHEMA, TABLE_NAME;
        """
        tables_df = pd.read_sql(query, conn)
        return tables_df
    except Exception as e:
        st.error(f"Erro ao listar tabelas: {e}")
        return pd.DataFrame()

# Função para listar colunas
def get_column_details(conn):
    try:
        query = """
        SELECT 
            TABLE_SCHEMA AS [Esquema],
            TABLE_NAME AS [Nome da Tabela],
            COLUMN_NAME AS [Nome da Coluna],
            DATA_TYPE AS [Tipo de Dados],
            CHARACTER_MAXIMUM_LENGTH AS [Tamanho Máximo],
            IS_NULLABLE AS [Aceita Nulo?]
        FROM INFORMATION_SCHEMA.COLUMNS
        ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;
        """
        columns_df = pd.read_sql(query, conn)
        return columns_df
    except Exception as e:
        st.error(f"Erro ao listar colunas: {e}")
        return pd.DataFrame()

# Função para listar índices
def get_index_details(conn):
    try:
        query = """
        SELECT 
            t.name AS [Nome da Tabela],
            i.name AS [Nome do Índice],
            i.type_desc AS [Tipo de Índice],
            i.is_unique AS [É Único?],
            c.name AS [Coluna]
        FROM sys.indexes i
        INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        WHERE i.is_primary_key = 0
        ORDER BY t.name, i.name;
        """
        indexes_df = pd.read_sql(query, conn)
        return indexes_df
    except Exception as e:
        st.error(f"Erro ao listar índices: {e}")
        return pd.DataFrame()

# Função para listar stored procedures
def get_procedure_details(conn):
    try:
        query = """
        SELECT 
            SPECIFIC_SCHEMA AS [Esquema],
            SPECIFIC_NAME AS [Nome da Procedure]
        FROM INFORMATION_SCHEMA.ROUTINES
        WHERE ROUTINE_TYPE = 'PROCEDURE'
        ORDER BY SPECIFIC_SCHEMA, SPECIFIC_NAME;
        """
        procedures_df = pd.read_sql(query, conn)
        return procedures_df
    except Exception as e:
        st.error(f"Erro ao listar stored procedures: {e}")
        return pd.DataFrame()

# Função para listar triggers
def get_trigger_details(conn):
    try:
        query = """
        SELECT 
            t.name AS [Nome da Tabela],
            tr.name AS [Nome do Trigger],
            OBJECT_DEFINITION(tr.object_id) AS [Definição do Trigger]
        FROM sys.triggers tr
        INNER JOIN sys.tables t ON tr.parent_id = t.object_id
        ORDER BY t.name, tr.name;
        """
        triggers_df = pd.read_sql(query, conn)
        return triggers_df
    except Exception as e:
        st.error(f"Erro ao listar triggers: {e}")
        return pd.DataFrame()

# Função para listar as tabelas mais pesadas
def get_heavy_tables(conn):
    try:
        query = """
        SELECT 
            t.name AS [Tabela],
            SUM(ps.reserved_page_count) * 8 / 1024 AS [Tamanho em MB]
        FROM 
            sys.dm_db_partition_stats ps
        INNER JOIN 
            sys.tables t ON ps.object_id = t.object_id
        WHERE 
            ps.index_id IN (0,1)  -- Considera tabelas e índices clustered
        GROUP BY 
            t.name
        ORDER BY 
            [Tamanho em MB] DESC;
        """
        tables_df = pd.read_sql(query, conn)
        return tables_df
    except Exception as e:
        st.error(f"Erro ao listar tabelas pesadas: {e}")
        return pd.DataFrame()

# Função para verificar a fragmentação dos índices
def get_index_fragmentation(conn):
    try:
        query = """
        SELECT 
            t.name AS [Nome da Tabela],
            i.name AS [Nome do Índice],
            ips.avg_fragmentation_in_percent AS [Fragmentação (%)],
            CASE 
                WHEN ips.avg_fragmentation_in_percent >= 30 THEN 'Rebuild'
                WHEN ips.avg_fragmentation_in_percent BETWEEN 10 AND 30 THEN 'Reorganize'
                ELSE 'Nenhuma Ação Necessária'
            END AS [Ação Recomendada]
        FROM 
            sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED') ips
        INNER JOIN 
            sys.tables t ON ips.object_id = t.object_id
        INNER JOIN 
            sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
        WHERE 
            i.type_desc = 'CLUSTERED' OR i.type_desc = 'NONCLUSTERED'
        ORDER BY 
            ips.avg_fragmentation_in_percent DESC;
        """
        fragmentation_df = pd.read_sql(query, conn)
        return fragmentation_df
    except Exception as e:
        st.error(f"Erro ao verificar fragmentação de índices: {e}")
        return pd.DataFrame()


# Campos para inserir as credenciais
server = st.text_input('Servidor (ex: your_server.database.windows.net)')
database = st.text_input('Banco de Dados')
username = st.text_input('Usuário')
password = st.text_input('Senha', type='password')

# Variável de conexão inicializada como None
conn = None

# Botão para tentar a conexão
if st.button('Conectar'):
    if server and database and username and password:
        conn = connect_to_azure_sql(server, database, username, password)
        if conn:
            st.success('Conectado ao banco de dados com sucesso!')

            # Exibir detalhes úteis para DBA
            st.header("Detalhes das Tabelas")
            tables_df = get_table_details(conn)
            if not tables_df.empty:
                st.dataframe(tables_df)
            else:
                st.write("Nenhuma tabela encontrada.")

            st.header("Detalhes das Colunas")
            columns_df = get_column_details(conn)
            if not columns_df.empty:
                st.dataframe(columns_df)
            else:
                st.write("Nenhuma coluna encontrada.")

            st.header("Índices")
            indexes_df = get_index_details(conn)
            if not indexes_df.empty:
                st.dataframe(indexes_df)
            else:
                st.write("Nenhum índice encontrado.")

            st.header("Stored Procedures")
            procedures_df = get_procedure_details(conn)
            if not procedures_df.empty:
                st.dataframe(procedures_df)
            else:
                st.write("Nenhuma procedure encontrada.")

            st.header("Triggers")
            triggers_df = get_trigger_details(conn)
            if not triggers_df.empty:
                st.dataframe(triggers_df)
            else:
                st.write("Nenhum trigger encontrado.")
            
            st.header("Tamanho das Tabelas")
            tables_df = get_heavy_tables(conn)
            if not tables_df.empty:
                st.dataframe(tables_df)
            else:
                st.write("Nenhuma tabela encontrada.")

            st.header("Fragmentação dos Índices e Ações Recomendadas")
            fragmentation_df = get_index_fragmentation(conn)
            if not fragmentation_df.empty:
                st.dataframe(fragmentation_df)
            else:
                st.write("Nenhuma informação de fragmentação encontrada.")
        else:
            st.error("Erro ao conectar ao banco de dados.")
    else:
        st.error('Por favor, preencha todos os campos.')
