import streamlit as st

TEMP_ALERTA = 35
RPM_ALERTA = 2000
CORRENTE_ALERTA = 18
DESGASTE_ALERTA = 7

def create_kpis_metrics(df, alertas):
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric("🔴 Críticos", len(alertas))

    with col2:
        with st.container(border=True):
            st.metric("📡 Sensores afetados", alertas["sensor_id"].nunique() if not alertas.empty else 0)

    with col3:
        with st.container(border=True):
            st.metric("📊 Total registros", len(df))


# def create_alerts_metrics(df):
#     df["alerta_temperatura"] = df["temperatura_motor"] > TEMP_ALERTA
#     df["alerta_rpm"] = df["rpm"] > RPM_ALERTA
#     df["alerta_corrente"] = df["corrente_a"] > CORRENTE_ALERTA
#     df["alerta_desgaste"] = df["indice_desgaste"] > DESGASTE_ALERTA
#
#     # Alertas ativos
#     alertas = df[
#         (df["alerta_temperatura"]) |
#         (df["alerta_rpm"]) |
#         (df["alerta_corrente"]) |
#         (df["alerta_desgaste"])
#         ].copy()
#
#     return alertas