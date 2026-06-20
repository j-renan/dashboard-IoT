import pandas as pd

TEMP_MAX = 100
RPM_MAX = 3000
CORRENTE_MAX = 30
CARGA_MAX = 100

dados = [
    {
        "timestamp": "14:05",
        "sensor_id": 1,
        "temperatura_motor": 28.5,
        "rpm": 1800,
        "corrente_a": 15.2,
        "carga_pct": 40
    },
    {
        "timestamp": "14:10",
        "sensor_id": 1,
        "temperatura_motor": 31.4,
        "rpm": 1950,
        "corrente_a": 18.9,
        "carga_pct": 55
    },
    {
        "timestamp": "14:15",
        "sensor_id": 1,
        "temperatura_motor": 35.2,
        "rpm": 2100,
        "corrente_a": 19.3,
        "carga_pct": 60
    }
]

temperatura_media = sum(
    d["temperatura_motor"]
    for d in dados
) / len(dados)

rpm_medio = sum(
    d["rpm"]
    for d in dados
) / len(dados)

corrente_media = sum(
    d["corrente_a"]
    for d in dados
) / len(dados)

carga_media = sum(
    d["carga_pct"]
    for d in dados
) / len(dados)

sensores_ativos = len(dados)

def formatar_dados():
    df = pd.DataFrame(dados)
    df["temp_norm"] = df["temperatura_motor"] / TEMP_MAX
    df["rpm_norm"] = df["rpm"] / RPM_MAX
    df["corrente_norm"] = df["corrente_a"] / CORRENTE_MAX
    df["carga_norm"] = df["carga_pct"] / CARGA_MAX
    df["score"] = (
            df["temp_norm"] * 0.35 +
            df["rpm_norm"] * 0.25 +
            df["corrente_norm"] * 0.25 +
            df["carga_norm"] * 0.15
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["delta_min"] = (
            df["timestamp"]
            .diff()
            .dt.total_seconds()
            .fillna(0)
            / 60
    )
    df["desgaste_periodo"] = (
            df["score"]
            * df["delta_min"]
    )
    df["indice_desgaste"] = (
        df["desgaste_periodo"]
        .cumsum()
    )
    return df

# formatar_dados(dados)