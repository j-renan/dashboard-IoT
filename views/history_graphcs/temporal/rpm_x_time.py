import streamlit as st
import plotly.express as px

def create_graph_rpm_x_time(df_filtrado):
    fig = px.line(
        df_filtrado,
        x="timestamp",
        y="rpm",
        title="RPM x Tempo"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width='content'
        )