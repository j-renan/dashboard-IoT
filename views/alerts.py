import streamlit as st
import plotly.express as px
from dados_iot import formatar_dados
from shared.utils import create_alerts_metrics
from views.alerts_graphcs.graphc import create_alerts_graph
from views.alerts_graphcs.metrics import create_kpis_metrics


def render_alerts(df):
    st.header("🚨 Alertas")
    # df = formatar_dados()
    alertas = create_alerts_metrics(df)
    create_kpis_metrics(df, alertas)

    # Tabela
    st.subheader("📋 Eventos")

    if alertas.empty:
        st.success("Nenhum alerta ativo.")
        return

        # Severidade

    def severidade(row):
        if row["indice_desgaste"] > 8:
            return "🔴 CRÍTICO"
        elif row["indice_desgaste"] > 6:
            return "🟠 ALTO"
        else:
            return "🟡 MODERADO"

    alertas["severidade"] = alertas.apply(severidade, axis=1)

    st.dataframe(alertas, width='stretch')

    # Gráfico
    create_alerts_graph(alertas)
