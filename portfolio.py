import streamlit as st

# Configurações da página
st.set_page_config(page_title="Portfólio de Análise de Dados", layout="wide")



# Função para definir as páginas
def main_page():
    # Criando a estrutura com fundo azul no topo e imagem no canto superior
    st.markdown("""
    <div style="background-color: #1e3a8a; padding: 20px; text-align: left; display: flex; align-items: center; width: 100%; height: 150px;border-radius: 15px;">
        <img src="https://i.imghippo.com/files/SfTo5703ks.jpg" width="130" style="border-radius: 50%; margin-left: 20px;" />
    </div>
    """, unsafe_allow_html=True)

    # Criando colunas para o nome e os botões
    col1, col2 = st.columns([3, 1])

    # Coluna para o nome
    with col1:
        st.markdown("""
            <h1>João Vilar Braga</h1>
            <h4> Data Engineering | Azure Cloud | SQL, Python, Spark, Power BI, Databricks, Airflow, ADF, SSIS </h4>
        """, unsafe_allow_html=True)

    # Coluna para os ícones do GitHub e LinkedIn
    with col2:
    # Botões com espaçamento
        st.markdown("""
        <div style="margin-top: 20px;">
            <a href="https://github.com/joaovilar" target="_blank" style="margin-right: 15px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="50" />
            </a>
            <a href="https://www.linkedin.com/in/joao-vilar-braga/" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/016/716/470/non_2x/linkedin-icon-free-png.png" alt="LinkedIn" width="50" />
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Adicionando o CSS para hover nas imagens
    st.markdown("""
    <style>
    .hover-image {
        transition: transform 0.3s ease;
    }
    .hover-image:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Subtítulo
    #st.header("8 Anos de Experiência em Análise de Dados e Engenharia de Dados")

    # Seção de Introdução
    st.subheader("Sobre Mim")
    st.write("""
    Com 8 anos de experiência na área de dados, sou especializado na construção e otimização de pipelines de dados, abrangendo extração, transformação, carregamento (ETL) e análise. Minha trajetória inclui um sólido conhecimento em bancos de dados relacionais, integração de dados e ferramentas de visualização como Power BI. Atualmente, estou expandindo minhas habilidades em arquiteturas de nuvem, focando no ecossistema Microsoft Azure e Databricks, criando soluções escaláveis e orientadas para resultados.
    """)

     # Adicionando E-mail e Cidade
    st.write("""
    📧 **E-mail:** j.vilar12@gmail.com  
    🌍 **Cidade:** Brasília-DF, Brasil
    """)

    # Seção de Habilidades
    st.subheader("Habilidades")
    st.write("""
    - **Microsoft Azure:** Experiência com Azure Data Factory, Synapse Analytics, Azure Data Lake, SQL Database e integração com Databricks, desenvolvendo soluções de orquestração e armazenamento de dados na nuvem.
    - **ETL e Orquestração:** Criação de fluxos de dados utilizando Python, SQL, Airflow, IBM DataStage e SSIS, otimizando o processamento de dados para análise e tomada de decisão.
    - **Bancos de Dados:** MySQL, PostgreSQL, SQL Server, Google BigQuery, com foco em modelagem relacional e dimensional, e consultas NoSQL com MongoDB.
    - **Análise de Dados e Visualização:** Desenvolvimento de dashboards e relatórios em Power BI, Reporting Services, Looker e Qlik Sense, transformando dados em informações úteis.
    - **Bibliotecas Python:** Utilização de Pandas, NumPy, Matplotlib e Seaborn para análise de dados, visualização e processamento estatístico.
    - **Estatísticas e Análise:** Aplicação de conceitos de estatísticas descritivas como média, moda, mediana, variância, desvio padrão, curtose, distribuições simétricas e assimétricas, distribuição de frequência e boxplot.
    - **Ferramentas de Desenvolvimento e Versionamento:** Git/GitHub, Jupyter Notebook, Google Colab e Visual Studio Code, garantindo práticas ágeis e colaborativas no desenvolvimento de projetos.
    """)

    # Seção de Educação e Certificações
    st.subheader("Educação e Certificações")
    st.write("""
    - **Graduação em Análise e Desenvolvimento de Sistemas**
    - **MBA em Análise de Dados com BI e Big Data**
    - **Pós-graduação em Ethical Hacking e Cybersecurity**
    - **Certificações Microsoft:**
      - 70-762 - Desenvolvimento de Bancos de Dados SQL
      - 70-461 - Consultas em Microsoft SQL Server
    """)

    st.subheader("Idiomas")
    st.write("""
    - Português (Nativo)
    - Inglês (Intermediário - B1)
    - Espanhol (Básico) """)
    

    st.markdown("""
<div style="border-radius: 15px; background-color: #add8e6; padding: 8px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" style="width: 40px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Painéis em Power BI</h3>
        <h6>Clique na imagem para ser redirecionado</h6>
    </div>
</div>
""", unsafe_allow_html=True)

    # Primeira fileira de 3 imagens
    col1, col2, col3 = st.columns(3)

    img_path1 = "https://i.imghippo.com/files/RKsA5492oU.jpg"
    img_path2 = "https://i.imghippo.com/files/Aswz6308TwI.png"
    img_path3 = "https://i.imghippo.com/files/ki4653MFs.png"

    linkp1 ="https://app.powerbi.com/view?r=eyJrIjoiOWQxODI5NzEtODNiZi00MTI1LTlkZTktZDFmMWU0NDk2MzVlIiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    linkp=""
    linkp3 = "https://app.powerbi.com/view?r=eyJrIjoiOTdlYzY3ZjMtMzU2Mi00YzViLWFhODYtNmM0OGVhMjNlZDk1IiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp1}" target="_blank"><img src="{img_path1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Painel de Operações do Delivery Center - Visão geral das operações, destacando KPIs como a taxa de entrega e a performance do time', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp1}" target="_blank"><img src="{img_path2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Painel de Acompanhamento Financeiro', unsafe_allow_html=True)


    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp3}" target="_blank"><img src="{img_path3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Painel de Operações de People Analytics - Fornece uma visão detalhada sobre a diversidade no ambiente de trabalho</div>', unsafe_allow_html=True)

    # Segunda fileira de 3 imagens
    col1, col2, col3 = st.columns(3)

    img_path4 = "https://i.imghippo.com/files/xTka3895aic.png"
    img_path5 = "https://i.imghippo.com/files/Op5719xhw.png"
    img_path6 = "https://i.imghippo.com/files/OatX1265sU.jpg"

    link4="https://app.powerbi.com/view?r=eyJrIjoiNjgyZDZkNWUtNDhmNy00ODNmLWFmYTgtZDBjMzBiMDEwMDk5IiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    link5=""
    link6 = "https://app.powerbi.com/view?r=eyJrIjoiN2E2NWJmOGItNGMxNS00NzhhLTgzNTItZGJiNWY0MTFkZWZhIiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    
    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link4}" target="_blank"><img src="{img_path4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Relatório Geral de Vendas - Análise detalhada de vendas por categoria e produto</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link5}" target="_blank"><img src="{img_path5}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Painel de Distribuição de Produtos Farmacêuticos</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link6}" target="_blank"><img src="{img_path6}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Painel de Vendas de Viagens - Acompanhamento das vendas de pacotes de viagem</div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #ecb653; padding: 8px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Databricks_Logo.png/640px-Databricks_Logo.png" style="width: 85px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Scripts notebooks no Databricks</h3>
        <h6>Clique na imagem para ser redirecionado</h6>
    </div>
</div>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)
    img_pathd1 = "https://i.imghippo.com/files/MzNw9037WFM.png"
    img_pathd2 = "https://i.imghippo.com/files/EGb4758qCg.png"
    img_pathd3 = "https://i.imghippo.com/files/epj8217m.png"

    linkd1 = "https://github.com/joaovilar/azuresql-to-datalake-medallion-dbdelta"
    linkd2 = "https://github.com/joaovilar/create_deltatable_databricks"
    linkd3 = "https://github.com/joaovilar/migration_mysql_to_databricks"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd1}" target="_blank"><img src="{img_pathd1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Arquitetura lakehouse, tabelas no azure sql database para o databricks</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd2}" target="_blank"><img src="{img_pathd2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Criação de tabela em delta lendo de diretório do azure data lake para Databricks</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd3}" target="_blank"><img src="{img_pathd3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Migração de tabelas no MySQL para o Databricks em delta</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #b1ff9a; padding: 10px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/AirflowLogo.png/220px-AirflowLogo.png" style="width: 80px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Pipeline de dados no Airflow com Python</h3>
        <h6>Clique na imagem para ser redirecionado</h6>
    </div>
</div>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    img_path_air1="https://i.imghippo.com/files/pIHP2302qzM.png"
    img_path_air2=""
    img_path_air3=""

    link_air1="https://github.com/joaovilar/Python/tree/main/Airflow"
    link_air2=""
    link_air3=""

    with col1:
        st.markdown(f'<a href="{link_air1}"  target="_blank"><img src="{img_path_air1}" width="400" class="hover-image"/></a>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #d3d3d3; padding: 8px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://i.imghippo.com/files/JJeU2683EVQ.png" style="width: 100px; margin-left: 10px; margin-right: 20px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Manipulação de dados em Geral com Python - Visual Code, Jupyter Notebook, Google Colab</h3>
        <h6>Clique na imagem para ser redirecionado</h6>
    </div>
</div>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    img_path_py1="https://i.imghippo.com/files/eO5856QbM.png"
    img_path_py2="https://i.imghippo.com/files/zYTU1086Ng.png"
    img_path_py3="https://i.imghippo.com/files/VigW8461EoQ.png"

    link_py1="https://github.com/joaovilar/Python/blob/main/Python_Jupyter/DataManipulation%20(SQL_Python).ipynb"
    link_py2="https://github.com/joaovilar/Python/blob/main/Google_Colab/MatplotLib_vs_Seaborn.ipynb"
    link_py3="https://github.com/joaovilar/Python/blob/main/Google_Colab/Use_Spark.ipynb"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py1}" target="_blank"><img src="{img_path_py1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Manipulação de dados no Jupyter Notebook</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py2}" target="_blank"><img src="{img_path_py2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Gráficos com as bibliotecas python matplotlib e seaborn</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py3}" target="_blank"><img src="{img_path_py3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Execução de scripts com spark no google colab</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    img_path_p4 = "https://i.imghippo.com/files/byaq9041gq.png"
    img_path_p5="https://i.imghippo.com/files/ARja7567heg.png"
    img_path_p6="https://i.imghippo.com/files/zXTK8750qmA.png"

    link_py4 = "https://github.com/joaovilar/Python/blob/main/Python_Jupyter/files_azure_to_database.ipynb"
    link_py5="https://github.com/joaovilar/Python/blob/main/Python_Jupyter/Envia%20Consolidado%20Azure.ipynb"
    link_py6="https://github.com/joaovilar/Python/blob/main/Python_Jupyter/DataManipulation%20(SQL_Python).ipynb"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py4}" target="_blank"><img src="{img_path_p4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Extração de arquivos do azure datalake para tabelas no Azure SQL com tratamento de dados</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py5}" target="_blank"><img src="{img_path_p5}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Dataframe consolidado e envia para o Banco de Dados Azure SQL</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py6}" target="_blank"><img src="{img_path_p6}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Comparação de consultas usando python e sql</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #ff7b5a; padding: 10px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://seeklogo.com/images/S/streamlit-logo-B405F7E2FC-seeklogo.com.png" style="width: 80px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Desenvolvimento Python com Streamlit</h3>
        <h6>Clique na imagem para ser redirecionado</h6>
    </div>
</div>
""", unsafe_allow_html=True)



    col1, col2, col3 = st.columns(3)

    img_path_s1="https://i.imghippo.com/files/xqY2891gj.png"
    img_path_s2="https://i.imghippo.com/files/peIm9743KRg.png"
    img_path_s3="https://i.imghippo.com/files/kzNQ1558M.png"

    link_s1="https://github.com/joaovilar/report_streamlit_dataset_dash"
    link_s2="https://github.com/joaovilar/face_detection"
    link_s3="https://github.com/joaovilar/app_streamlit_upload_file_azure"


    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s1}" target="_blank"><img src="{img_path_s1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Relatório e Dashboard dinâmico utilizando streamlit</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s2}" target="_blank"><img src="{img_path_s2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Sistema que identifica o rosto humano utilizando a biblioteca opencv</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s3}" target="_blank"><img src="{img_path_s3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Gerencimento de arquivos no Azure Datalake, possibilitando listar os diretórios e fazer upload</div>', unsafe_allow_html=True)


def experience_page():
    st.markdown("""
    <h1 style="text-align: center;">Experiência Profissional</h1>
    <hr style="border: 1px solid #000; width: 80%; margin: 20px auto;">
    """, unsafe_allow_html=True)

    st.write("""
    ### Senior Business Intelligence Analyst  
    **Stefanini Group · Tempo integral**  
    **Setembro de 2022 - o momento · 2 anos 4 meses (Home Office)**  

    Tenho contribuído significativamente para o monitoramento de inadimplências no **Banco do Brasil Seguros**, proporcionando maior visibilidade sobre **milhares de reais** e automatizando a estruturação de dados com base em estratégias internas.  

    Atendo demandas de diversas áreas, oferecendo suporte no acompanhamento de processos e desenvolvendo **consultas SQL e scripts** em **MySQL, PostgreSQL e DB2**, utilizando **DBeaver**.  
    Crio **dashboards e relatórios dinâmicos no Power BI** (Desktop e Report Server), fornecendo informações estratégicas, além de desenvolver **Jobs de ETL no IBM DataStage**.  

    Participo ativamente de interações diárias com a equipe, garantindo **alinhamento** e **entrega de resultados** conforme as expectativas do produto.


    ### Business Intelligence Analyst  
    **G4F Soluções Corporativas | Dezembro de 2019 - Setembro de 2022**  
    Contribuí significativamente para o Ministério da Economia em diversas frentes:

    - Business Intelligence (BI): Desenvolvimento de relatórios interativos e intuitivos no Power BI, oferecendo insights estratégicos.
    - Processos ETL com SSIS: Construção de fluxos eficientes de ETL utilizando o SQL Server Integration Services.
    - Consultas e Scripts SQL: Consultas avançadas em SQL Server, PostgreSQL e MySQL, garantindo extração de dados precisa.
    - Ambiente Qlik Sense: Desenvolvimento e suporte de painéis personalizados no Qlik Sense, atendendo demandas de áreas específicas.

    ### BI systems analyst  
    **Indra | Minsait | Novembro de 2021 - Abril de 2022**  
    Atuei em projetos de BI com foco em:

    - Script T-SQL e SSIS: Desenvolvimento de scripts eficientes no SQL Server e processos de ETL.
    - Relatórios com Power BI: Criação de relatórios interativos para tomada de decisões estratégicas.
    - Metodologia Scrum: Participação em entregas ágeis e colaborativas.
    - Documentação Detalhada: Elaboração de documentação para uso e referência futura.

    ### Mid-Level Business Intelligence Analyst  
    Desempenhei um papel crucial ao atender demandas de Business Intelligence para o Ministério da Economia. Minhas realizações incluíram:

    - Desenvolvimento de Painéis e Relatórios com Power BI: Criei painéis interativos e relatórios informativos no Power BI, oferecendo insights essenciais para decisões estratégicas.

    - Scripting T-SQL e Consultas em Bancos de Dados: Escrevi scripts T-SQL no SQL Server e em bancos de dados MySQL, agilizando a obtenção de dados.

    - Suporte e Ajustes de Cubos e Pacotes ETL: Contribuí com suporte e ajustes em cubos de análise e pacotes ETL, garantindo a integridade e eficiência dos fluxos de dados. Lidei com projetos de ETL que envolveram a leitura de dados diretamente do SharePoint, otimizando a integração de informações.

    - Gestão de Demandas e Documentação de Projetos: Lidei com demandas de manutenção e desenvolvimento em projetos de BI, enquanto documentava soluções de forma abrangente.

    Minha dedicação resultou em um impacto positivo, aprimorando operações e fornecendo soluções eficazes de Business Intelligence.

    ### Database Administrator  
    Criação de projetos de Business Intelligence com a SQL Server e Integration Services e desenvolvimento de Dashboards usando o Datazen.
    Desenvolvimento de Relatórios e Dashboards com Mobile Report integrado ao Reporting Services 2016

    Principais atividades desenvolvidas:
    - Planejamento e implementação de painéis analíticos e relatórios;
    - Instalação e configuração de ambientes OLAP utilizando o Microsoft Datazen;
    - Instalação e configuração de ambientes OLAP utilizando o Microsoft Reporting Services 2016;
    - Desenvolvimento e publicação de KPIs e Dashboards usando o Datazen Publisher e Mobile Report;
    - Parametrização de Dashboards para análises de Drill Through;
    - Segurança de objetos e dados usando o Datazen Server e Row Level Security.
    - Pacotes ETL com Integration Services
    - Importação de planilhas em Excel via FTP para SQL Server
    - Migração de banco de dados, realizando o levantamento de todos os pré-requisitos e realizando as transformações necessárias.
    - Desenvolvimento e manutenção de dados utilizando banco de dados na nuvem - Azure SQL Database
    - Consultas e manipulação de dados;
    - Controle de acesso dos usuários no Banco de Dados;
    - Procedures/Triggers/Functions/Views
    - Backup e Restore de Base de Dados
    - Configuração de rotina de Backup
    - Criação de job 
    - Análise e criação de índice e otimização de consultas
    - Liderança de equipe de sustentação, controlando e administrando as atividades do time de atividades diárias.
    """)

# Configurando páginas
page = st.sidebar.selectbox("Selecione a página", ["Sobre Mim", "Experiência"])

if page == "Sobre Mim":
    main_page()
elif page == "Experiência":
    experience_page()
