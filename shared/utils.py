import streamlit as st

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