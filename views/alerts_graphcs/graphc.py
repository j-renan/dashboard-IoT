import streamlit as st
import plotly.express as px


def create_alerts_graph(alertas):
    alertas_por_sensor = (
        alertas.groupby("sensor_id")
        .size()
        .reset_index(name="qtd_alertas")
    )

    fig = px.bar(
        alertas_por_sensor,
        x="sensor_id",
        y="qtd_alertas",
        title="Alertas por Sensor"
    )

    with st.container(border=True):
        st.plotly_chart(fig, width='stretch')