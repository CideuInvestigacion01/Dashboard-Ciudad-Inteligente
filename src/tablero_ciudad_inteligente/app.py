"""Aplicación principal del dashboard."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from tablero_ciudad_inteligente.charts import (
    grafica_barras_dimensiones,
    grafica_radar_dimensiones,
    grafica_radar_gobierno_datos,
    tabla_recomendaciones,
)
from tablero_ciudad_inteligente.data_loader import cargar_archivo, seleccionar_fila
from tablero_ciudad_inteligente.scoring import calcular_resultados, resultados_a_dataframe_dimensiones


st.set_page_config(page_title="Tablero de Ciudad Inteligente", layout="wide")


@st.cache_data
def cargar_ejemplo() -> pd.DataFrame:
    return cargar_archivo(Path(__file__).resolve().parents[2] / "data" / "ejemplo_respuestas.csv")


st.title("Tablero de Autoevaluación de Transición Digital y Ciudades Inteligentes")
st.caption(
    "Diagnóstico visual del estado de madurez digital de una ciudad, país o región a partir de respuestas de encuesta."
)

with st.sidebar:
    st.markdown("### Fuente de datos")
    archivo = st.file_uploader("Sube un CSV o XLSX exportado desde KoboToolbox", type=["csv", "xlsx", "xls"])
    st.markdown("### Seguridad recomendada")
    st.info(
        "Esta versión no exige contraseña en el código. Para despliegues reales se recomienda autenticación, HTTPS y control de acceso por roles."
    )

if archivo is not None:
    temp_path = Path("/tmp") / archivo.name
    temp_path.write_bytes(archivo.getvalue())
    df = cargar_archivo(temp_path)
else:
    st.info("No se cargó archivo. Se usa el dataset de ejemplo incluido en el proyecto.")
    df = cargar_ejemplo()

if df.empty:
    st.error("No hay datos para mostrar.")
    st.stop()

columna_entidad = "entidad" if "entidad" in df.columns else ("ciudad" if "ciudad" in df.columns else None)
etiquetas = (
    df[columna_entidad].fillna("Sin nombre").astype(str).tolist()
    if columna_entidad
    else [f"Fila {i + 1}" for i in range(len(df))]
)
indice = st.sidebar.selectbox("Selecciona una evaluación", options=list(range(len(df))), format_func=lambda i: etiquetas[i])
fila = seleccionar_fila(df, indice)
resultado = calcular_resultados(fila)

a, b, c = st.columns(3)
a.metric("Territorio", resultado.ciudad)
b.metric("Puntaje global", f"{resultado.puntaje_global} / 100")
c.metric("Nivel global", resultado.nivel_global)

st.markdown("## Estado general")

if resultado.nivel_global == "Inicial":
    st.error("El territorio se encuentra en una fase inicial de transición digital. Se recomienda construir bases institucionales y de infraestructura.")
elif resultado.nivel_global == "Emergente":
    st.warning("El territorio muestra avances aislados o parciales. La prioridad es consolidar capacidades y continuidad.")
elif resultado.nivel_global == "En consolidación":
    st.info("El territorio cuenta con bases importantes. El siguiente paso es mejorar interoperabilidad, inclusión y sostenibilidad.")
else:
    st.success("El territorio presenta un perfil avanzado. Conviene pasar a monitoreo continuo, evidencia de impacto y mejora fina.")

st.markdown("## Indicadores por dimensión")
df_dimensiones = resultados_a_dataframe_dimensiones(resultado)
st.dataframe(df_dimensiones, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(grafica_barras_dimensiones(resultado), use_container_width=True)
with col2:
    st.plotly_chart(grafica_radar_dimensiones(resultado), use_container_width=True)

st.plotly_chart(grafica_radar_gobierno_datos(resultado), use_container_width=True)

st.markdown("## Alertas y hallazgos")
if resultado.alertas:
    for alerta in resultado.alertas:
        st.write(f"- {alerta}")
else:
    st.write("- No se detectaron alertas críticas en esta evaluación.")

st.markdown("## Recomendaciones")
st.dataframe(tabla_recomendaciones(resultado), use_container_width=True, hide_index=True)

st.markdown("## Literatura sugerida")
for item in resultado.literatura:
    st.markdown(f"**{item['titulo']}**")
    st.write(item["descripcion"])
    st.caption(item["fuente"])

st.markdown("## Recomendaciones de evolución técnica")
st.write(
    "En una siguiente fase, conviene separar la solución en tres capas: ingestión desde KoboToolbox, motor de scoring y visualización con autenticación por usuario."
)
st.write(
    "También se recomienda persistir resultados en base de datos para construir histórico, benchmarking entre territorios y alertas automáticas."
)
