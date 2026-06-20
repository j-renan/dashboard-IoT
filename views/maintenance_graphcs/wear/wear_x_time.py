import streamlit as st
import plotly.express as px


LIMITE_CRITICO = 10

def create_graph_wear_x_time(df_filtrado):
    fig = px.line(
        df_filtrado,
        x="timestamp",
        y="indice_desgaste",
        title="Índice de Desgaste"
    )

    fig.add_hline(
        y=LIMITE_CRITICO,
        line_dash="dash",
        annotation_text="Limite Crítico"
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width='content'
        )