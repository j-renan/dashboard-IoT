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