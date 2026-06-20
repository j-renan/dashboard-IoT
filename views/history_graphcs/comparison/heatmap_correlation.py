import streamlit as st
import plotly.express as px

def create_heatmap_correlation(df):
    colunas = [
        "temperatura_motor",
        "rpm",
        "corrente_a",
        "carga_pct"
    ]

    corr = (
        df[colunas]
        .corr()
    )

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Mapa de Correlação"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width='content'
        )