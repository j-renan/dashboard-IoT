import streamlit as st

from dados_iot import formatar_dados
from shared.utils import filter_dataframe
from views.history_metrics.metrics import create_max_metrics
from views.history_tabs.tabs import create_tabs
from views.maintenance_graphcs.health.gauge_health import create_gauge_health
from views.maintenance_graphcs.wear.wear_x_time import create_graph_wear_x_time


def render_maintenance():
    st.header("🔧 Manutenção")

    df = formatar_dados()
    key = 'maintenance'
    df_filtrado = filter_dataframe(df, key)

    col1, col2 = st.columns(2)

    with col1:
        create_graph_wear_x_time(df_filtrado)

    with col2:
        create_gauge_health(df_filtrado)