import streamlit as st


def create_max_metrics(df_filtrado):
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.metric(
                "🌡 Temp Máxima",
                f"{df_filtrado['temperatura_motor'].max()} °C"
            )

    with col2:
        with st.container(border=True):
            st.metric(
                "⚙ RPM Máximo",
                int(df_filtrado["rpm"].max())
            )

    with col3:
        with st.container(border=True):
            st.metric(
                "🔌 Corrente Máxima",
                f"{df_filtrado['corrente_a'].max()} A"
            )

    return col1, col2, col3