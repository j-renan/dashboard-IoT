import streamlit as st
import pandas as pd
import plotly.express as px

from dados_iot import dados
from views.history_metrics.metrics import create_max_metrics
from views.history_tabs.tabs import create_tabs


def render_history():
    st.header("📈 Histórico")

    df = pd.DataFrame(dados)

    sensores = sorted(df["sensor_id"].unique())

    sensor = st.selectbox(
        "Selecione o sensor",
        sensores
    )

    df_filtrado = df[
        df["sensor_id"] == sensor
    ]

    create_max_metrics(df_filtrado)
    create_tabs(df_filtrado)




    # sensores_selecionados = st.sidebar.multiselect(
    #     "Selecione os sensores",
    #     options=sensores,
    #     default=sensores
    # )

    # Filtrar dataframe
    # df_filtrado = df[sensor]





    # fig_rpm = px.line(
    #     df_filtrado,
    #     x="rpm",
    #     y="temperatura_motor",
    #     title="RPM x Temperatura"
    # )
    #
    # with col5:
    #     with st.container(border=True):
    #         st.plotly_chart(
    #             fig_rpm,
    #             width='content'
    #         )

    # col6, col7 = st.columns(2)
    #
    # fig_corrente = px.line(
    #     df,
    #     x="corrente_a",
    #     y="temperatura_motor",
    #     title="Temperatura x Corrente"
    # )
    #
    # with col6:
    #     with st.container(border=True):
    #         st.plotly_chart(
    #             fig_corrente,
    #             width='content'
    #         )
    #
    # fig_corrente = px.histogram(
    #     df,
    #     x="timestamp",
    #     y="carga_pct",
    #     title="Carga x Tempo"
    # )
    #
    # with col7:
    #     with st.container(border=True):
    #         st.plotly_chart(
    #             fig_corrente,
    #             width='content'
    #         )

    st.subheader("Dados Históricos")

    st.dataframe(
        df_filtrado,
        use_container_width=True
    )

