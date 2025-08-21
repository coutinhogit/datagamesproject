import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página
st.set_page_config(layout="wide")

# --- TÍTULO E INTRODUÇÃO ---
st.title('Dashboard de Análise de Vendas de Videogames 🎮')
st.markdown("""
Este dashboard apresenta uma análise visual das vendas globais de videogames, 
explorando tendências por gênero, plataforma e ao longo do tempo.
""")

# --- CARREGAMENTO DOS DADOS (COM CACHE) ---
# Esta linha é um truque de mágica do Streamlit. Ela guarda os dados em cache,
# o que garante que o app não precise recarregar e limpar o CSV toda vez,
# deixando tudo muito mais rápido.
@st.cache_data
def carregar_dados():
    df = pd.read_csv('vgsales.csv')
    df.dropna(inplace=True)
    df['Year'] = df['Year'].astype(int)
    return df

df = carregar_dados()

# --- GRÁFICOS E ANÁLISES ---
# Vamos usar colunas para organizar os gráficos lado a lado
col1, col2 = st.columns(2)

# Gráfico 1: Vendas por Gênero
with col1:
    st.header('Top Gêneros por Vendas')
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    vendas_por_genero = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    sns.barplot(x=vendas_por_genero.values, y=vendas_por_genero.index, palette='viridis', ax=ax1)
    ax1.set_title('Vendas Globais Totais por Gênero de Jogo', fontsize=16)
    ax1.set_xlabel('Vendas Globais (em milhões)', fontsize=12)
    ax1.set_ylabel('Gênero', fontsize=12)
    st.pyplot(fig1)
    st.caption("Essas são as vendas por Gênero de modo a generalizar as plataformas.")

# Gráfico 2: Vendas por Plataforma
with col2:
    st.header('Top Plataformas por Vendas')
    fig2, ax2 = plt.subplots(figsize=(10, 8))
    vendas_por_plataforma = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(15)
    sns.barplot(x=vendas_por_plataforma.values, y=vendas_por_plataforma.index, palette='rocket', ax=ax2)
    ax2.set_title('Top 15 Plataformas por Vendas Globais', fontsize=16)
    ax2.set_xlabel('Vendas Globais (em milhões)', fontsize=12)
    ax2.set_ylabel('Plataforma', fontsize=12)
    st.pyplot(fig2)
    st.caption("Essas são as top vendas por plataformas.")

# Gráfico 3: Evolução ao Longo do Tempo ("Guerra dos Consoles")
st.header('A "Guerra dos Consoles" ao Longo do Tempo')
principais_consoles = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(3).index
df_consoles = df[df['Platform'].isin(principais_consoles)]
vendas_consoles_ano = df_consoles.groupby(['Year', 'Platform'])['Global_Sales'].sum().reset_index()
vendas_consoles_ano = vendas_consoles_ano[vendas_consoles_ano['Year'].between(2005, 2016)]

fig3, ax3 = plt.subplots(figsize=(15, 7))
sns.lineplot(x='Year', y='Global_Sales', data=vendas_consoles_ano, hue='Platform', ax=ax3)
ax3.set_title('Vendas dos Principais Consoles ao Longo do Tempo', fontsize=16)
ax3.set_xlabel('Ano', fontsize=12)
ax3.set_ylabel('Vendas Globais (em milhões)', fontsize=12)
st.pyplot(fig3)
st.caption("Aqui está a guerra de consoles analisada a partir de um gráfico de linha ao longo do ano de 2005 até 2016.")

# Gráfico 4: Guerra dos consoles pela ótica do gráfico de colunas.
st.header('A "Guerra dos Consoles" pelas barras!')
main_consoles = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(3).index
df_console = df[df['Platform'].isin(main_consoles)]
vendas_csl_ano = df_console.groupby(['Year', 'Platform'])['Global_Sales'].sum().reset_index()
vendas_csl_ano = vendas_csl_ano[vendas_csl_ano['Year'].between(2005, 2013)]

fig4,ax4 = plt.subplots(figsize=(15,7))
sns.barplot(x='Year', y='Global_Sales', data=vendas_csl_ano, hue='Platform', ax = ax4)
ax4.set_title('Vendas dos Principais Consoles ao Longo do Tempo', fontsize=16)
ax4.set_xlabel('Ano', fontsize=12)
ax4.set_ylabel('Vendas Globais (em milhões)', fontsize=12)
st.pyplot(fig4)
st.caption("Aqui está a guerra de consoles analisada a partir de um gráfico de barras caso tenha preferência por ele :)")
