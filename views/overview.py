import streamlit as st

from dados_iot import temperatura_media, rpm_medio, corrente_media, carga_media, sensores_ativos, formatar_dados


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

    df = formatar_dados()

    st.subheader("Dados Recebidos")
    st.dataframe(df)