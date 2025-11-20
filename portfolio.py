import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Configuração da página para modo Wide (Largo)
st.set_page_config(
    layout="wide", 
    page_title="Portfólio - João Vilar",
    initial_sidebar_state="collapsed"
)

# --- CSS HACK PARA REMOVER BORDAS ---
# Isso é essencial para o HTML colar nas laterais e no topo
st.markdown("""
    <style>
        /* Remove o padding (espaçamento) padrão do bloco principal do Streamlit */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Remove a barra superior colorida (header) do Streamlit se quiser tela cheia total */
        header[data-testid="stHeader"] {
            display: none;
        }
        
        /* Ajustes para remover scroll duplo se possível */
        .main .block-container {
            overflow: hidden;
        }
        
        /* Remove margens do iframe gerado pelo componente */
        iframe {
            display: block; /* Remove espaços fantasmas inline */
        }
    </style>
""", unsafe_allow_html=True)

# Carregar o arquivo HTML
# Certifique-se de que o arquivo 'portfolio.html' está na mesma pasta que este script
try:
    html_path = Path("portfolio.html").read_text(encoding="utf-8")
    
    # Renderizar no Streamlit
    # A altura (height) deve ser grande o suficiente para caber seu site sem barra de rolagem interna dupla
    components.html(html_path, height=4500, scrolling=False)
    
except FileNotFoundError:
    st.error("Arquivo 'portfolio.html' não encontrado. Verifique se ele está na mesma pasta do portfolio.py")
