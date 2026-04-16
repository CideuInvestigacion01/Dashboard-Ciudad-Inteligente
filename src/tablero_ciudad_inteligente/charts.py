"""Funciones para construir gráficas del tablero."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from tablero_ciudad_inteligente.config import (
    RADAR_CAPACIDADES_CLAVE,
    TEXTOS_GRAFICAS,
    ResultadoTablero,
)
from tablero_ciudad_inteligente.scoring import (
    resultados_a_dataframe_dimensiones_plots,
    resultados_a_dataframe_preguntas,
)


def grafica_barras_dimensiones(resultado: ResultadoTablero):
    df = resultados_a_dataframe_dimensiones_plots(resultado)
    fig = px.bar(
        df,
        x="dimensión",
        y="puntaje",
        text="puntaje",
        title=TEXTOS_GRAFICAS["bar_dimensions_title"],
    )
    fig.update_layout(
        yaxis_title=TEXTOS_GRAFICAS["bar_dimensions_yaxis"],
        xaxis_title=TEXTOS_GRAFICAS["bar_dimensions_xaxis"],
    )
    fig.update_traces(textposition="outside")
    return fig


def grafica_radar_dimensiones(resultado: ResultadoTablero):
    df = resultados_a_dataframe_dimensiones_plots(resultado)
    categorias = df["dimensión"].tolist()
    valores = df["puntaje"].tolist()
    categorias.append(categorias[0])
    valores.append(valores[0])

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill="toself",
            name=resultado.ciudad,
        )
    )
    fig.update_layout(
        polar={
            "radialaxis": {
                "visible": True,
                "range": [TEXTOS_GRAFICAS["radar_range_min"], TEXTOS_GRAFICAS["radar_range_max"]],
            }
        },
        title=TEXTOS_GRAFICAS["radar_dimensions_title"],
        showlegend=True,
    )
    return fig


def grafica_radar_gobierno_datos(resultado: ResultadoTablero):
    mapa = resultados_a_dataframe_preguntas(resultado).set_index("pregunta")["puntaje"].to_dict()
    categorias = [etiqueta for _, etiqueta in RADAR_CAPACIDADES_CLAVE]
    valores = [float(mapa.get(q, 0.0)) for q, _ in RADAR_CAPACIDADES_CLAVE]
    categorias.append(categorias[0])
    valores.append(valores[0])

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill="toself",
            name=TEXTOS_GRAFICAS["radar_key_capabilities_name"],
        )
    )
    fig.update_layout(
        polar={
            "radialaxis": {
                "visible": True,
                "range": [TEXTOS_GRAFICAS["radar_range_min"], TEXTOS_GRAFICAS["radar_range_max"]],
            }
        },
        title=TEXTOS_GRAFICAS["radar_key_capabilities_title"],
        showlegend=True,
    )
    return fig


def tabla_recomendaciones(resultado: ResultadoTablero) -> pd.DataFrame:
    return pd.DataFrame(resultado.recomendaciones)