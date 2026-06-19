import streamlit as st
import plotly.express as px

def create_histogram_temp(df_filtrado):
    fig = px.histogram(
        df_filtrado,
        x="temperatura_motor",
        nbins=20,
        title="Nível Temperatura"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True
        )