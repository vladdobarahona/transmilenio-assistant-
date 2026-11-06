import requests
import pandas as pd
from typing import Dict, List, Optional
import streamlit as st

API_KEY = st.secrets["CROMA_API_KEY"]

if API_KEY == "PENDIENTE_CONFIGURAR":
    st.error(
        "Configure CROMA_API_KEY antes de utilizar la aplicación."
    )
    st.stop()

class CromaClient:

    def __init__(self, api_key: str):

        self.api_key = api_key

        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Ajustar cuando validemos los endpoints reales
        self.base_url = "https://api.usecroma.com"

    def _get(self, endpoint: str, params=None):

        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ---------------------------------------------------------
    # RUTAS
    # ---------------------------------------------------------

    def get_routes(self):

        return self._get("/routes")

    def search_route(
        self,
        route_key: str,
        mode: Optional[str] = None
    ):

        routes = self.get_routes()

        resultados = []

        for route in routes:

            if route.get("key", "").upper() == route_key.upper():

                if mode:

                    if route.get("mode", "").lower() != mode.lower():
                        continue

                resultados.append(route)

        return resultados

    # ---------------------------------------------------------
    # VEHICULOS
    # ---------------------------------------------------------

    def get_live_vehicles(self):

        return self._get("/vehicles")

    def get_route_vehicles(self, route_key):

        vehicles = self.get_live_vehicles()

        return [
            v
            for v in vehicles
            if v.get("route_key", "").upper()
            == route_key.upper()
        ]

    # ---------------------------------------------------------
    # FRECUENCIA
    # ---------------------------------------------------------

    def estimate_frequency(self, route_key):

        buses = self.get_route_vehicles(route_key)

        cantidad = len(buses)

        if cantidad == 0:

            return {
                "route": route_key,
                "frequency": None,
                "active_buses": 0
            }

        # MVP:
        # posteriormente calcular por distancia acumulada
        # sobre geometría de ruta

        frecuencia_aprox = max(1, round(60 / cantidad, 1))

        return {
            "route": route_key,
            "frequency": frecuencia_aprox,
            "active_buses": cantidad
        }
