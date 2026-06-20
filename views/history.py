import streamlit as st

from dados_iot import formatar_dados
from views.history_metrics.metrics import create_max_metrics
from views.history_tabs.tabs import create_tabs


def render_history():
    st.header("📈 Histórico")
    df = formatar_dados()
    # create_max_metrics(df)
    create_tabs(df)


