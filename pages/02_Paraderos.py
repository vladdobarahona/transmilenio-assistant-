import streamlit as st
from services.croma import CromaClient

client = CromaClient(
    st.secrets["CROMA_API_KEY"]
)

st.title("Buscar paradero")

texto = st.text_input(
    "Nombre",
    value="Portal Norte"
)

if st.button("Buscar"):

    datos = client.buscar_paradero(texto)

    st.json(datos)
