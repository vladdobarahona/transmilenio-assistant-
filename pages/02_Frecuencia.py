import streamlit as st

from services.croma import CromaClient

client = CromaClient(
    st.secrets["CROMA_API_KEY"]
)

st.title("Frecuencia de ruta")

sistema = st.selectbox(
    "Clase",
    [
        "transmilenio",
        "sitp"
    ]
)

ruta = st.text_input(
    "Ruta",
    "B10"
)

if st.button("Calcular"):

    resultado = client.estimate_frequency(ruta)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Vehículos activos",
            resultado["active_buses"]
        )

    with col2:

        st.metric(
            "Frecuencia estimada (min)",
            resultado["frequency"]
        )
