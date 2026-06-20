import streamlit as st
import plotly.express as px
from dados_iot import formatar_dados


def render_alerts():
    st.header("🚨 Alertas")
    # Regras
    TEMP_ALERTA = 35
    RPM_ALERTA = 2000
    CORRENTE_ALERTA = 18
    DESGASTE_ALERTA = 7

    # Flags
    df = formatar_dados()
    df["alerta_temperatura"] = df["temperatura_motor"] > TEMP_ALERTA
    df["alerta_rpm"] = df["rpm"] > RPM_ALERTA
    df["alerta_corrente"] = df["corrente_a"] > CORRENTE_ALERTA
    df["alerta_desgaste"] = df["indice_desgaste"] > DESGASTE_ALERTA

    # Alertas ativos
    alertas = df[
        (df["alerta_temperatura"]) |
        (df["alerta_rpm"]) |
        (df["alerta_corrente"]) |
        (df["alerta_desgaste"])
    ].copy()

    # KPIs
    col1, col2, col3 = st.columns(3)

    col1.metric("🔴 Críticos", len(alertas))
    col2.metric("📡 Sensores afetados", alertas["sensor_id"].nunique() if not alertas.empty else 0)
    col3.metric("📊 Total registros", len(df))

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

    st.dataframe(alertas, use_container_width=True)

    # Gráfico
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

    st.plotly_chart(fig, use_container_width=True)
