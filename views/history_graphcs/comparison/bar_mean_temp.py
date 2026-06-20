import streamlit as st
import plotly.express as px

def create_graph_mean_temp(df, metrica):
    df_agrupado = (
        df.groupby("sensor_id")[metrica]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        df_agrupado,
        x="sensor_id",
        y=metrica,
        title=f"{metrica} média por sensor"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width='content'
        )