# import plotly.express as px
# import streamlit as st
# import pandas as pd
#
# from dados_iot import *
#
# pagina = st.segmented_control(
#     "Menu",
#     ["📊 Visão Geral", "📈 Histórico"]
# )
#
# def pagina_visao_geral():
#     st.header("📊 Visão Geral")
#
# def pagina_historico():
#     st.header("📈 Histórico")
#
# if pagina == "📊 Visão Geral":
#     pagina_visao_geral()
#
# elif pagina == "📈 Histórico":
#     pagina_historico()
#
# st.set_page_config(layout="wide")
#
# st.title("🏭 Monitoramento Industrial")
#
# col1, col2, col3, col4, col5 = st.columns(5)
#
# with col1:
#     with st.container(border=True):
#         st.metric(
#             "🌡 Temperatura Média",
#             f"{round(temperatura_media, 2)}",
#         )
#
# with col2:
#     with st.container(border=True):
#         st.metric(
#             "⚙ RPM Médio",
#             f"{round(rpm_medio,2)}",
#         )
#
# with col3:
#     with st.container(border=True):
#         st.metric(
#             "🔌 Corrente Média",
#             f"{round(corrente_media,2)}",
#         )
#
# with col4:
#     with st.container(border=True):
#         st.metric(
#             "📊 Carga Média",
#             f"{round(carga_media,2)}",
#         )
#
# with col5:
#     with st.container(border=True):
#         st.metric(
#             "📡 Sensores Ativos",
#             f"{sensores_ativos}",
#         )
#
# if temperatura_media < 50:
#     status = "NORMAL"
# elif temperatura_media < 70:
#     status = "ATENÇÃO"
# else:
#     status = "CRÍTICO"
#
# st.subheader("Status Geral")
#
# if status == "NORMAL":
#     st.success(status)
# elif status == "ATENÇÃO":
#     st.warning(status)
# else:
#     st.error(status)
#
# df = pd.DataFrame(dados)
#
# st.subheader("Dados Recebidos")
# st.dataframe(df)

import streamlit as st

from views.overview import render_overview
from views.history import render_history
# from views.alerts import render as render_alerts
# from views.maintenance import render as render_maintenance


st.set_page_config(
    page_title="Monitoramento Industrial",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Monitoramento Industrial")

pagina = st.segmented_control(
    label="Navegação",
    options=[
        "📊 Visão Geral",
        "📈 Histórico",
        "🚨 Alertas",
        "🔧 Manutenção"
    ],
    selection_mode="single",
    default="📊 Visão Geral"
)

if pagina == "📊 Visão Geral":
    render_overview()

elif pagina == "📈 Histórico":
    render_history()

# elif pagina == "🚨 Alertas":
#     render_alerts()
#
# elif pagina == "🔧 Manutenção":
#     render_maintenance()
