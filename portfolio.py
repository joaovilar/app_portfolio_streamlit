import streamlit as st

# Configurações da página
st.set_page_config(page_title="Data Analysis Portfolio", layout="wide")



# Função para definir as páginas
def main_page():
    # Criando a estrutura com fundo azul no topo e imagem no canto superior
    st.markdown("""
    <div style="background-color: #1e3a8a; padding: 20px; text-align: left; display: flex; align-items: center; width: 100%; height: 150px;border-radius: 15px;">
        <img src="https://i.postimg.cc/0NnzztLF/vilar.jpg" width="130" style="border-radius: 50%; margin-left: 20px;" />
    </div>
    """, unsafe_allow_html=True)

    # Criando colunas para o nome e os botões
    col1, col2 = st.columns([3, 1])

    # Coluna para o nome
    with col1:
        st.markdown("""
            <h1>João Vilar Braga</h1>
            <h4> Data Engineering | Business Intelligence | Azure Cloud | Databricks, SQL, Python, Spark, Power BI, Airflow, ADF, SSIS </h4>
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
    st.subheader("About Me")
    st.write("""
    I am a technology enthusiast. With 8 years of experience in the data field, I specialize in building and optimizing data pipelines, encompassing extraction, transformation, loading (ETL), and analysis. My journey includes solid knowledge of relational databases, data integration, and visualization tools like Power BI. Currently, I am expanding my skills in cloud architectures, focusing on the Microsoft Azure and Databricks ecosystem, creating scalable and results-driven solutions.
    """)

     # Adicionando E-mail e Cidade
    st.write("""
    📧 **E-mail:** j.vilar12@gmail.com  
    🌍 **City:** Brasília-DF, Brasil
    """)

    # Seção de Habilidades
    st.subheader("Skills")
    st.write("""
    - **Microsoft Azure:** Experience with Azure Data Factory, Synapse Analytics, Azure Data Lake, SQL Database, and integration with Databricks, developing orchestration and cloud data storage solutions.
    - **ETL and Orchestration:** Creating data flows using Python, SQL, Airflow, IBM DataStage, and SSIS, optimizing data processing for analysis and decision-making.
    - **Databases:** MySQL, PostgreSQL, SQL Server, Google BigQuery, with a focus on relational and dimensional modeling, and NoSQL queries with MongoDB.
    - **Data Analysis and Visualization:** Developing dashboards and reports in Power BI, Reporting Services, Looker, and Qlik Sense, transforming data into actionable insights.
    - **Python Libraries:** Using Pandas, NumPy, Matplotlib, and Seaborn for data analysis, visualization, and statistical processing.
    - **Statistics and Analysis:** Applying descriptive statistics concepts such as mean, mode, median, variance, standard deviation, kurtosis, symmetric and asymmetric distributions, frequency distribution, and boxplot.
    - **Development and Versioning Tools:** Git/GitHub, Jupyter Notebook, Google Colab, and Visual Studio Code, ensuring agile and collaborative practices in project development.
    """)


    # Seção de Educação e Certificações
    st.subheader("Education and Certifications")
    st.write("""
    - **Graduated in Systems Analysis and Development**
    - **MBA in Data Analysis with BI and Big Data**
    - **Postgraduate in Ethical Hacking and Cybersecurity**
    - **Microsoft Certifications:**
        - 70-762 - SQL Database Development
        - 70-461 - Queries in Microsoft SQL Server
    """)


    st.subheader("Languages")
    st.write("""
    - Portuguese (Native)
    - English (Intermediate - B1)
    - Spanish (Basic) """)
    

    st.markdown("""
<div style="border-radius: 15px; background-color: #add8e6; padding: 8px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" style="width: 40px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Power BI Dashboards</h3>
        <h6>Click on the image to be redirected</h6>
    </div>
</div>
""", unsafe_allow_html=True)

    # Primeira fileira de 3 imagens
    col1, col2, col3 = st.columns(3)

    img_path1 = "https://i.imghippo.com/files/kkA2467Hp.jpg"
    img_path2 = "https://i.postimg.cc/sfnmbzgQ/imagem.jpg"
    img_path3 = "https://i.imghippo.com/files/hmaQ5302PSg.jpg"

    linkp1 ="https://app.powerbi.com/view?r=eyJrIjoiOWQxODI5NzEtODNiZi00MTI1LTlkZTktZDFmMWU0NDk2MzVlIiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    linkp2="https://i.postimg.cc/sfnmbzgQ/imagem.jpg"
    linkp3 = "https://app.powerbi.com/view?r=eyJrIjoiOTdlYzY3ZjMtMzU2Mi00YzViLWFhODYtNmM0OGVhMjNlZDk1IiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp1}" target="_blank"><img src="{img_path1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Delivery Center Operations Dashboard- Overview of operations, highlighting KPIs such as delivery rate and team performance', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp2}" target="_blank"><img src="{img_path2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">The dashboard provides a consolidated view of Bills, Norms, and Regulations that are currently in progress or in effect', unsafe_allow_html=True)


    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{linkp3}" target="_blank"><img src="{img_path3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">People Analytics Operations Dashboard - Provides a detailed view of diversity in the workplace</div>', unsafe_allow_html=True)

    # Segunda fileira de 3 imagens
    col1, col2, col3 = st.columns(3)

    img_path4 = "https://i.postimg.cc/C1L90NTw/pw4.jpg"
    img_path5 = "https://i.imghippo.com/files/Op5719xhw.png"
    img_path6 = "https://i.imghippo.com/files/gIL1941mjY.jpg"

    link4="https://app.powerbi.com/view?r=eyJrIjoiNjgyZDZkNWUtNDhmNy00ODNmLWFmYTgtZDBjMzBiMDEwMDk5IiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    link5=""
    link6 = "https://app.powerbi.com/view?r=eyJrIjoiN2E2NWJmOGItNGMxNS00NzhhLTgzNTItZGJiNWY0MTFkZWZhIiwidCI6IjU1NjBlNDIwLTVmNzEtNDAwYy04YmJlLWU1MmZhZTcyZWI2YyJ9"
    
    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link4}" target="_blank"><img src="{img_path4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">General Sales Report - Detailed analysis of sales by category and product</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link5}" target="_blank"><img src="{img_path5}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Pharmaceutical Product Distribution Dashboard</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link6}" target="_blank"><img src="{img_path6}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Travel Sales Dashboard - Tracking sales of travel packages</div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #ecb653; padding: 8px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Databricks_Logo.png/640px-Databricks_Logo.png" style="width: 85px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Databricks Notebook Scripts</h3>
        <h6>Click on the image to be redirected</h6>
    </div>
</div>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)
    img_pathd1 = "https://i.postimg.cc/fWdh58K9/dbt1.jpg"
    img_pathd2 = "https://i.postimg.cc/3xm7Rnyh/dtb2.jpg"
    img_pathd3 = "https://i.postimg.cc/pd5jpNfT/img-dtb.jpg"
    img_pathd4="https://i.postimg.cc/hvk6RR1d/ss3-dtb.jpg"

    linkd1 = "https://github.com/joaovilar/azuresql-to-datalake-medallion-dbdelta"
    linkd2 = "https://github.com/joaovilar/create_deltatable_databricks"
    linkd3 = "https://github.com/joaovilar/migration_mysql_to_databricks"
    linkd4="https://github.com/joaovilar/Data-from-AWS-S3-in-Azure-Databricks/blob/main/Getting%20Data%20from%20Bucket%20S3.ipynb"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd1}" target="_blank"><img src="{img_pathd1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Lakehouse Architecture, tables in Azure SQL Database for Databricks</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd2}" target="_blank"><img src="{img_pathd2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Creating Delta table by reading from Azure Data Lake directory to Databricks</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd3}" target="_blank"><img src="{img_pathd3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Migrating MySQL tables to Databricks in Delta format</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{linkd4}" target="_blank"><img src="{img_pathd4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Getting data from Amazon S3 bucket in Azure Databricks as dataframe and table</div>', unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #b1ff9a; padding: 10px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/AirflowLogo.png/220px-AirflowLogo.png" style="width: 80px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Data Pipelines in Airflow with Python</h3>
        <h6>Click on the image to be redirected</h6>
    </div>
</div>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    img_path_air1="https://i.imghippo.com/files/MaA9943SI.jpg"
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
        <h3>General Data Manipulation with Python - Visual Code, Jupyter Notebook, Google Colab</h3>
        <h6>Click on the image to be redirected</h6>
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
        st.markdown(f'<div style="text-align: center; font-style: italic;">Data manipulation in Jupyter Notebook</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py2}" target="_blank"><img src="{img_path_py2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Charts with Python libraries matplotlib and seaborn</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py3}" target="_blank"><img src="{img_path_py3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Running scripts with Spark in Google Colab</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    img_path_p4 = "https://i.imghippo.com/files/byaq9041gq.png"
    img_path_p5="https://i.imghippo.com/files/ARja7567heg.png"
    img_path_p6="https://i.imghippo.com/files/zXTK8750qmA.png"

    link_py4 = "https://github.com/joaovilar/Python/blob/main/Python_Jupyter/files_azure_to_database.ipynb"
    link_py5="https://github.com/joaovilar/Python/blob/main/Python_Jupyter/Envia%20Consolidado%20Azure.ipynb"
    link_py6="https://github.com/joaovilar/Python/blob/main/Python_Jupyter/DataManipulation%20(SQL_Python).ipynb"

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py4}" target="_blank"><img src="{img_path_p4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Extracting files from Azure Data Lake to tables in Azure SQL with data processing</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py5}" target="_blank"><img src="{img_path_p5}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Consolidated dataframe and sending it to Azure SQL Database</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_py6}" target="_blank"><img src="{img_path_p6}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Comparison of queries using Python and SQL</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="border-radius: 15px; background-color: #ff7b5a; padding: 10px; display: flex; align-items: center; width: 100%; margin: auto; margin-bottom: 45px;">
    <img src="https://seeklogo.com/images/S/streamlit-logo-B405F7E2FC-seeklogo.com.png" style="width: 80px; margin-left: 10px;" />
    <div style="text-align: center; flex: 1;">
        <h3>Python Development with Streamlit Library</h3>
        <h6>Click on the image to be redirected</h6>
    </div>
</div>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    img_path_s1="https://i.imghippo.com/files/xqY2891gj.png"
    img_path_s2="https://i.imghippo.com/files/peIm9743KRg.png"
    img_path_s3="https://i.imghippo.com/files/kzNQ1558M.png"
    img_path_s4="https://i.imghippo.com/files/dfnm3816j.png"
    img_path_s5="https://i.imghippo.com/files/uVgh3793WnI.png"
    img_path_s6="https://i.imghippo.com/files/AJoA4596cmU.png"

    link_s1="https://github.com/joaovilar/report_streamlit_dataset_dash"
    link_s2="https://github.com/joaovilar/face_detection"
    link_s3="https://github.com/joaovilar/app_streamlit_upload_file_azure"
    link_s4="https://github.com/joaovilar/sistema-de-cadastro-de-pessoa"
    link_s5="https://github.com/joaovilar/login_screen"
    link_s6="https://data-vizualization-app.streamlit.app/"


    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s1}" target="_blank"><img src="{img_path_s1}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Report and dynamic dashboard using Streamlit</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s2}" target="_blank"><img src="{img_path_s2}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">System that identifies human faces using the OpenCV library</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s3}" target="_blank"><img src="{img_path_s3}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">File management system on Azure Data Lake, allowing directory listing and file upload</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s4}" target="_blank"><img src="{img_path_s4}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">People registration app, allowing information entry and photo capture using the webcam</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s5}" target="_blank"><img src="{img_path_s5}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Login application developed with Streamlit and connected to an Azure SQL database</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: center;"><a href="{link_s6}" target="_blank"><img src="{img_path_s6}" width="400" class="hover-image"/></a></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="text-align: center; font-style: italic;">Application that allows importing files and visualizing the data</div>', unsafe_allow_html=True)


def experience_page():
    st.markdown("""
    <h1 style="text-align: center;">Professional Experience</h1>
    <hr style="border: 1px solid #000; width: 80%; margin: 20px auto;">
    """, unsafe_allow_html=True)

    st.write("""
    ### Senior Business Intelligence Analyst  
    **Stefanini Group · Full-time**  
    **September 2022 - Present · 2 years 10 months (Work From Home)**  

    I have made significant contributions to monitoring defaults at **Banco do Brasil Seguros**, providing greater visibility into **thousands of reais** and automating data structuring based on internal strategies.  

    I handle demands from various departments, offering support in tracking processes and developing **SQL queries and scripts** in **MySQL, PostgreSQL, and DB2**, using **DBeaver**.  
    I create **dynamic dashboards and reports in Power BI** (Desktop and Report Server), providing strategic information, and also develop **ETL Jobs in IBM DataStage**.  

    I actively participate in daily interactions with the team, ensuring **alignment** and **delivery of results** according to product expectations.

    ### Business Intelligence Analyst  
    **G4F Soluções Corporativas | December 2019 - September 2022**  
    I made significant contributions to the Ministry of Economy in various areas:

    - Business Intelligence (BI): Development of interactive and intuitive reports in Power BI, offering strategic insights.
    - ETL Processes with SSIS: Building efficient ETL flows using SQL Server Integration Services.
    - SQL Queries and Scripts: Advanced queries in SQL Server, PostgreSQL, and MySQL, ensuring accurate data extraction.
    - Qlik Sense Environment: Development and support of custom dashboards in Qlik Sense, meeting the demands of specific areas.

    ### BI Systems Analyst  
    **Indra | Minsait | November 2021 - April 2022**  
    I worked on BI projects focusing on:

    - T-SQL Scripts and SSIS: Development of efficient scripts in SQL Server and ETL processes.
    - Reports with Power BI: Creation of interactive reports for strategic decision-making.
    - Scrum Methodology: Participation in agile and collaborative deliveries.
    - Detailed Documentation: Creation of documentation for future reference and usage.

    ### Mid-Level Business Intelligence Analyst  
    I played a crucial role in addressing Business Intelligence demands for the Ministry of Economy. My achievements included:

    - Development of Dashboards and Reports with Power BI: I created interactive dashboards and informative reports in Power BI, providing essential insights for strategic decisions.
    
    - T-SQL Scripting and Database Queries: I wrote T-SQL scripts in SQL Server and MySQL databases, streamlining data retrieval.

    - Support and Adjustments for OLAP Cubes and ETL Packages: I contributed to supporting and adjusting OLAP cubes and ETL packages, ensuring data flow integrity and efficiency. I worked on ETL projects that involved reading data directly from SharePoint, optimizing data integration.
    
    - Demand Management and Project Documentation: I handled maintenance and development requests in BI projects, while documenting solutions comprehensively.

    My dedication resulted in a positive impact, improving operations and providing effective Business Intelligence solutions.

    ### Database Administrator  
    Created Business Intelligence projects with SQL Server and Integration Services and developed Dashboards using Datazen.
    Developed Reports and Dashboards with Mobile Report integrated into Reporting Services 2016.

    Key Activities:
    - Planning and implementation of analytical dashboards and reports;
    - Installation and configuration of OLAP environments using Microsoft Datazen;
    - Installation and configuration of OLAP environments using Microsoft Reporting Services 2016;
    - Development and publication of KPIs and Dashboards using Datazen Publisher and Mobile Report;
    - Dashboard parameterization for Drill Through analysis;
    - Object and data security using Datazen Server and Row Level Security.
    - ETL packages with Integration Services.
    - Importing Excel spreadsheets via FTP into SQL Server.
    - Database migration, gathering all prerequisites, and performing necessary transformations.
    - Data development and maintenance using cloud databases - Azure SQL Database.
    - Queries and data manipulation.
    - Database user access control.
    - Procedures/Triggers/Functions/Views.
    - Backup and Restore of Databases.
    - Backup routine configuration.
    - Job creation.
    - Analysis and creation of indexes and query optimization.
    - Leadership of the support team, controlling and managing the daily activities of the team.
""")


# Configurando páginas
page = st.sidebar.selectbox("Select a page", ["About Me", "Experience"])

if page == "About Me":
    main_page()
elif page == "Experience":
    experience_page()
