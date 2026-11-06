import requests
import streamlit as st


API_KEY = st.secrets["CROMA_API_KEY"]

if API_KEY == "PENDIENTE_CONFIGURAR":
    st.warning(
        "CROMA_API_KEY aún no configurada. Modo demostración."
    )


class CromaClient:

    def __init__(self, api_key: str):

        self.api_key = api_key

        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        self.base_url = "https://api.croma.run"

    def buscar_ruta(self, codigo):

        response = requests.post(
            f"{self.base_url}/co/transmilenio/routes-search/v1",
            headers=self.headers,
            json={
                "query": codigo
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()
        
    def buscar_paradero(self, texto):

    response = requests.post(
        f"{self.base_url}/co/transmilenio/stops-search/v1",
        headers=self.headers,
        json={
            "query": texto
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()
