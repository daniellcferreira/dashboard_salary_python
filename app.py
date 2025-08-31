import streamlit as st
import pandas as pd
import plotly.express as px

# configuração da pagina
# define o titulo da pagina e o layout para ocupar a largura inteira
st.set_page_config(page_title="Dashboard de Salários na Área de Dados", layout="wide")

# carrega os dados
df = pd.read_csv("dados.csv")

# barra lateral (filtros)
st.sidebar.header("Filtros")

# filtro de ano
anos_disponiveis = sorted(df["Ano"].unique())
anos_selecionados = st.sidebar.multiselect(
    "Ano", anos_disponiveis, default=anos_disponiveis
)

# filtro de senioridade
senioridade_disponiveis = sorted(df["senioridade"].unique())
senioridade_selecionadas = st.sidebar.multiselect(
    "Senioridade", senioridade_disponiveis, default=senioridade_disponiveis
)

# filtro tipo de contrato
contratos_disponiveis = sorted(df["contrato"].unique())
contratos_selecionados = st.sidebar.multiselect(
    "Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis
)

# filtro por tamanho da empresa
tamanhos_disponiveis = sorted(df["tamanho_empresa"].unique())
tamanhos_selecionados = st.sidebar.multiselect(
    "Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis
)

# filtragem do dataframe
# o dataframe principal é filtrado com base na seleções feitas na barra lateral
df_filtrado = df[
    (df["ano"].isin(anos_selecionados))
    & (df["senioridade"].isin(senioridade_selecionadas))
    & (df["contrato"].isin(contratos_selecionados))
    & (df["tamanho_empresa"].isin(tamanhos_selecionados))
]
