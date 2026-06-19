import streamlit as st
import plotly.express as px

def create_scatter_current_x_temp(df_filtrado):
    fig = px.scatter(
        df_filtrado,
        x="corrente_a",
        y="temperatura_motor",
        color="carga_pct",
        size="rpm",
        title="Temperatura × Corrente",
        hover_data=["timestamp"],
        trendline="ols"

    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True
        )