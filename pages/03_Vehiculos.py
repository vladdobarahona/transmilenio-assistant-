import streamlit as st
from services.croma import CromaClient

st.title("🚍 Vehículos en vivo")

client = CromaClient(
    st.secrets["CROMA_API_KEY"]
)

ruta = st.text_input(
    "Código de ruta",
    value="B10"
)

if st.button("Consultar vehículos"):

    try:

        datos = client.obtener_vehiculos(ruta)

        st.success(
            f"Vehículos encontrados: {len(datos.get('vehicles', []))}"
        )

        st.json(datos)

    except Exception as e:

        st.error(str(e))
