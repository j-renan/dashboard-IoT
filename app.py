import streamlit as st

from dados_iot import formatar_dados
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

df = formatar_dados()

if pagina == "📊 Visão Geral":
    render_overview()

elif pagina == "📈 Histórico":
    render_history(df)

elif pagina == "🚨 Alertas":
    render_alerts(df)

elif pagina == "🔧 Manutenção":
    render_maintenance(df)
