import streamlit as st

from views.history_graphcs.correlation.scatter_current_x_temp import create_scatter_current_x_temp
from views.history_graphcs.distribuicao.box_plot_temp import create_box_plot_temp
from views.history_graphcs.distribuicao.temp_histogram import create_histogram_temp
from views.history_graphcs.temporal.current_x_time import create_graph_current_x_time
from views.history_graphcs.temporal.rpm_x_time import create_graph_rpm_x_time
from views.history_graphcs.temporal.temp_x_time import create_graphc_temp_x_time
from views.history_graphcs.correlation.scatter_rpm_x_temp import create_scatter_rpm_x_temp


def create_tabs(df_filtrado):
    tab1, tab2, tab3, tab4 = st.tabs([
        "Tendência Temporal",
        "Correlações",
        "Distribuição",
        "Comparação"
    ])
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            create_graphc_temp_x_time(df_filtrado)
        with col2:
            create_graph_rpm_x_time(df_filtrado)
        with col3:
            create_graph_current_x_time(df_filtrado)

    with tab2:
        col5, col6 = st.columns(2)
        with col5:
            create_scatter_rpm_x_temp(df_filtrado)
        with col6:
            create_scatter_current_x_temp(df_filtrado)

    with tab3:
        col7, col8 = st.columns(2)
        with col7:
            create_histogram_temp(df_filtrado)
        with col8:
            create_box_plot_temp(df_filtrado)

    return tab1, tab2