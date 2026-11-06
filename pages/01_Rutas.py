import streamlit as st
from services.croma import CromaClient

st.title("Prueba de conexión Croma")

client = CromaClient(
    st.secrets["CROMA_API_KEY"]
)

if st.button("Probar conexión"):

    try:

        respuesta = client._get("/")

        st.success("Conexión OK")
        st.json(respuesta)

    except Exception as e:

        st.error(str(e))

st.divider()

st.title("Consulta de rutas")

sistema = st.selectbox(
    "Clase",
    [
        "transmilenio",
        "sitp"
    ]
)

ruta = st.text_input(
    "Clave de ruta",
    placeholder="B10"
)

if st.button("Buscar"):

    resultados = client.search_route(
        route_key=ruta,
        mode=sistema
    )

    if len(resultados) == 0:

        st.warning("No encontrada")

    else:

        for r in resultados:

            st.json(r)
