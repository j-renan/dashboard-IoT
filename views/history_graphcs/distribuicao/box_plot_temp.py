import streamlit as st
import plotly.express as px

def create_box_plot_temp(df_filtrado):
    fig = px.box(
        df_filtrado,
        x="temperatura_motor",
        title="Anomalias Temperatura"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True
        )