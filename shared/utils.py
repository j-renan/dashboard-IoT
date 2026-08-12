import streamlit as st

TEMP_ALERTA = 35
RPM_ALERTA = 2000
CORRENTE_ALERTA = 18
DESGASTE_ALERTA = 7

def filter_dataframe(df, key):
    sensores = sorted(df["sensor_id"].unique())

    sensor = st.selectbox(
        "Selecione o sensor",
        sensores,
        key=key
    )

    df_filtrado = df[
            df["sensor_id"] == sensor
        ]
    return df_filtrado


def select_metric():
    metrica = st.selectbox(
        "Métrica",
        [
            "temperatura_motor",
            "rpm",
            "corrente_a",
            "carga_pct"
        ]
    )
    return metrica


def create_alerts_metrics(df):
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

    return alertas