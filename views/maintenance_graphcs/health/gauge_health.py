import plotly.graph_objects as go
import streamlit as st

DESGASTE_MAXIMO = 10

def create_gauge_health(df_filtrado):

    if df_filtrado.empty:
        st.warning("Nenhum dado disponível.")
        return

    indice_desgaste_atual = (
        df_filtrado["indice_desgaste"]
        .iloc[-1]
    )

    saude = max(
        0,
        100 - (indice_desgaste_atual / DESGASTE_MAXIMO) * 100
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=saude,
            title={"text": "Saúde do Equipamento"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 40]},
                    {"range": [40, 70]},
                    {"range": [70, 100]}
                ]
            }
        )
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True
        )