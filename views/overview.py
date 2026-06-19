import streamlit as st
import pandas as pd
import plotly.express as px

from dados_iot import *


def render_overview():
    st.set_page_config(layout="wide")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        with st.container(border=True):
            st.metric(
                "🌡 Temperatura Média",
                f"{round(temperatura_media, 2)}",
            )

    with col2:
        with st.container(border=True):
            st.metric(
                "⚙ RPM Médio",
                f"{round(rpm_medio,2)}",
            )

    with col3:
        with st.container(border=True):
            st.metric(
                "🔌 Corrente Média",
                f"{round(corrente_media,2)}",
            )

    with col4:
        with st.container(border=True):
            st.metric(
                "📊 Carga Média",
                f"{round(carga_media,2)}",
            )

    with col5:
        with st.container(border=True):
            st.metric(
                "📡 Sensores Ativos",
                f"{sensores_ativos}",
            )

    if temperatura_media < 50:
        status = "NORMAL"
    elif temperatura_media < 70:
        status = "ATENÇÃO"
    else:
        status = "CRÍTICO"

    st.subheader("Status Geral")

    if status == "NORMAL":
        st.success(status)
    elif status == "ATENÇÃO":
        st.warning(status)
    else:
        st.error(status)

    df = pd.DataFrame(dados)

    st.subheader("Dados Recebidos")
    st.dataframe(df)