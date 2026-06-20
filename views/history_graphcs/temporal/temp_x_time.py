import streamlit as st
import plotly.express as px

from shared.utils import filter_dataframe


def create_graphc_temp_x_time(df_filtrado):
    fig = px.line(
        df_filtrado,
        x="timestamp",
        y="temperatura_motor",
        title="Temperatura x Tempo"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width='content'
        )