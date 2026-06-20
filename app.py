import streamlit as st

from views.alerts import render_alerts
from views.maintenance import render_maintenance
from views.overview import render_overview
from views.history import render_history


st.set_page_config(
    page_title="Monitoramento Industrial",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Monitoramento Industrial")

pagina = st.segmented_control(
    label="Navegação",
    options=[
        "📊 Visão Geral",
        "📈 Histórico",
        "🚨 Alertas",
        "🔧 Manutenção"
    ],
    selection_mode="single",
    default="📊 Visão Geral"
)

if pagina == "📊 Visão Geral":
    render_overview()

elif pagina == "📈 Histórico":
    render_history()

elif pagina == "🚨 Alertas":
    render_alerts()

elif pagina == "🔧 Manutenção":
    render_maintenance()
