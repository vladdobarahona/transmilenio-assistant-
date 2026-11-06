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
        vehiculos = datos["data"]["vehicles"]
        st.write(datos)
        st.metric(
            "Vehículos activos",
            len(vehiculos)
        )

        if vehiculos:

            import pandas as pd

            df = pd.DataFrame(vehiculos)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info("No se encontraron vehículos.")

    except Exception as e:

        st.error(str(e))
