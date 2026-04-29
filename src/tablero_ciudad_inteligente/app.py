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
from tablero_ciudad_inteligente.config import (
    BIENVENIDA_CONFIG,
    EXPLICACION_DIMENSIONES,
    MENSAJES_NIVEL_GLOBAL,
    TEXTOS_APP,
)
from tablero_ciudad_inteligente.data_loader import (
    cargar_archivo,
    construir_etiquetas_evaluacion,
    seleccionar_fila,
)
from tablero_ciudad_inteligente.scoring import calcular_resultados, resultados_a_dataframe_dimensiones


st.set_page_config(page_title=TEXTOS_APP["page_title"], layout="wide")


@st.cache_data
def cargar_ejemplo() -> pd.DataFrame:
    return cargar_archivo(Path(__file__).resolve().parents[2] / "data" / "ejemplo_respuestas.csv")


def _csv_recomendaciones(resultado) -> bytes:
    df_recomendaciones = tabla_recomendaciones(resultado)
    return df_recomendaciones.to_csv(index=False).encode("utf-8-sig")


def render_bienvenida() -> None:
    st.title(BIENVENIDA_CONFIG["titulo"])
    st.caption(BIENVENIDA_CONFIG["subtitulo"])

    for parrafo in BIENVENIDA_CONFIG["introduccion"]:
        st.write(parrafo)

    st.markdown(BIENVENIDA_CONFIG["seccion_que_hace"])
    for item in BIENVENIDA_CONFIG["que_hace"]:
        st.write(f"- {item}")

    st.markdown(BIENVENIDA_CONFIG["seccion_como_se_calcula"])
    for item in BIENVENIDA_CONFIG["como_se_calcula"]:
        st.write(f"- {item}")

    st.markdown(BIENVENIDA_CONFIG["tipos_pregunta_titulo"])
    for tipo in BIENVENIDA_CONFIG["tipos_pregunta"]:
        st.markdown(f"**{tipo['nombre']}**")
        st.write(tipo["descripcion"])

    st.info(BIENVENIDA_CONFIG["nota_q24"])

    st.markdown(BIENVENIDA_CONFIG["seccion_dimensiones"])
    for _, info in EXPLICACION_DIMENSIONES.items():
        st.markdown(f"### {info['nombre']} ({info['acronimo']})")
        st.write(info["descripcion"])
        st.write(f"**Preguntas que la integran:** {', '.join(info['preguntas_etiqueta'])}")

    st.markdown(BIENVENIDA_CONFIG["seccion_niveles"])
    for nivel in BIENVENIDA_CONFIG["niveles"]:
        st.markdown(f"### {nivel['nivel']}")
        st.write(f"**Rango:** {nivel['rango']}")
        st.write(nivel["descripcion"])

    st.markdown(BIENVENIDA_CONFIG["seccion_graficas"])
    for grafica in BIENVENIDA_CONFIG["graficas"]:
        st.markdown(f"### {grafica['titulo']}")
        st.write(f"**Cómo se construye:** {grafica['como_se_construye']}")
        st.write(f"**Cómo se interpreta:** {grafica['como_se_interpreta']}")

    st.markdown(BIENVENIDA_CONFIG["seccion_ejemplo"])
    for item in BIENVENIDA_CONFIG["ejemplo"]:
        st.write(f"- {item}")

    st.markdown(BIENVENIDA_CONFIG["seccion_uso"])
    for item in BIENVENIDA_CONFIG["uso"]:
        st.write(f"- {item}")


st.title(TEXTOS_APP["main_title"])
st.caption(TEXTOS_APP["main_caption"])

with st.sidebar:
    st.markdown(TEXTOS_APP["sidebar_nav_title"])
    pagina = st.radio(
        TEXTOS_APP["sidebar_nav_label"],
        options=[TEXTOS_APP["sidebar_nav_home"], TEXTOS_APP["sidebar_nav_dashboard"]],
    )

if pagina == TEXTOS_APP["sidebar_nav_home"]:
    render_bienvenida()
    st.stop()

with st.sidebar:
    st.markdown(TEXTOS_APP["sidebar_data_title"])
    archivo = st.file_uploader(
        TEXTOS_APP["sidebar_uploader_label"],
        type=["csv", "xlsx", "xls"],
    )
    st.markdown(TEXTOS_APP["sidebar_security_title"])
    st.info(TEXTOS_APP["sidebar_security_info"])

if archivo is not None:
    temp_path = Path("/tmp") / archivo.name
    temp_path.write_bytes(archivo.getvalue())
    df = cargar_archivo(temp_path)
else:
    st.info(TEXTOS_APP["example_dataset_info"])
    df = cargar_ejemplo()

if df.empty:
    st.error(TEXTOS_APP["no_data_error"])
    st.stop()

etiquetas = construir_etiquetas_evaluacion(df)
indice = st.sidebar.selectbox(
    TEXTOS_APP["evaluation_selector_label"],
    options=list(range(len(df))),
    format_func=lambda i: etiquetas[i],
)
fila = seleccionar_fila(df, indice)
resultado = calcular_resultados(fila)

a, b, c = st.columns(3)
a.metric(TEXTOS_APP["metric_territory"], resultado.ciudad)
b.metric(TEXTOS_APP["metric_global_score"], f"{resultado.puntaje_global} / 100")
c.metric(TEXTOS_APP["metric_global_level"], resultado.nivel_global)

st.markdown(TEXTOS_APP["section_general_state"])

if resultado.nivel_global == "Inicial":
    st.error(MENSAJES_NIVEL_GLOBAL["Inicial"])
elif resultado.nivel_global == "Emergente":
    st.warning(MENSAJES_NIVEL_GLOBAL["Emergente"])
elif resultado.nivel_global == "En consolidación":
    st.info(MENSAJES_NIVEL_GLOBAL["En consolidación"])
else:
    st.success(MENSAJES_NIVEL_GLOBAL["Avanzado"])

st.markdown(TEXTOS_APP["section_dimensions"])
df_dimensiones = resultados_a_dataframe_dimensiones(resultado)
st.dataframe(df_dimensiones, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(grafica_barras_dimensiones(resultado), use_container_width=True)
with col2:
    st.plotly_chart(grafica_radar_dimensiones(resultado), use_container_width=True)

st.plotly_chart(grafica_radar_gobierno_datos(resultado), use_container_width=True)

st.markdown(TEXTOS_APP["section_alerts"])
if resultado.alertas:
    for alerta in resultado.alertas:
        st.write(f"- {alerta}")
else:
    st.write(TEXTOS_APP["no_critical_alerts"])

st.markdown(TEXTOS_APP["section_recommendations"])

for i, recomendacion in enumerate(resultado.recomendaciones, start=1):
    st.markdown(f"### {i}. {recomendacion['dimension']}")
    st.write(f"**{TEXTOS_APP['recommendation_priority_label']}:** {recomendacion['prioridad']}")
    st.write(f"**{TEXTOS_APP['recommendation_diagnostic_label']}:** {recomendacion['diagnostico']}")
    st.write(f"**{TEXTOS_APP['recommendation_next_step_label']}:** {recomendacion['siguiente_paso']}")
    st.write(f"**{TEXTOS_APP['recommendation_literature_label']}:** {recomendacion['literatura']}")

st.download_button(
    label=TEXTOS_APP["recommendations_download_button"],
    data=_csv_recomendaciones(resultado),
    file_name=TEXTOS_APP["recommendations_download_filename"],
    mime="text/csv",
)

st.markdown(TEXTOS_APP["section_literature"])
for item in resultado.literatura:
    st.markdown(f"**{item['titulo']}**")
    st.write(item["descripcion"])
    st.caption(item["fuente"])