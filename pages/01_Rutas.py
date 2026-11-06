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

        rutas = datos["data"]["routes"]

        if not rutas:

            st.warning("No se encontraron rutas.")
            st.stop()

        r = rutas[0]

        st.success("Consulta exitosa")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Código",
                r["short_name"]
            )

        with col2:
            st.metric(
                "Route ID",
                r["route_id"]
            )

        with col3:
            st.metric(
                "Sistema",
                r["system_name"]
            )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Paradas",
                r["stops_count"]
            )

        with col2:
            st.metric(
                "Viajes/semana",
                r["trips_per_week"]
            )

        with col3:
            st.metric(
                "Modo",
                r["mode"]
            )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Inicio operación",
                r["first_departure"]
            )

        with col2:
            st.metric(
                "Fin operación",
                r["last_departure"]
            )

        st.subheader("Destino")

        st.info(
            r["long_name"]
        )

        st.expander("JSON completo").json(r)

    except Exception as e:

        st.error(str(e))
