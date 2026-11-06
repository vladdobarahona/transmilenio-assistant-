import streamlit as st
from services.croma import CromaClient

st.title("Consulta de rutas")

client = CromaClient(
    st.secrets["CROMA_API_KEY"]
)

ruta = st.text_input(
    "Código de ruta",
    value="B10"
)

if st.button("Buscar ruta"):

    try:

        datos = client.buscar_ruta(ruta)

        st.success("Consulta exitosa")
        st.json(datos)

    except Exception as e:

        st.error(str(e))
