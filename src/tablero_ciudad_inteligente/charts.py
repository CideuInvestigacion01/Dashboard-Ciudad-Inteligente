"""Funciones para construir gráficas del tablero."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from tablero_ciudad_inteligente.config import ResultadoTablero
from tablero_ciudad_inteligente.scoring import resultados_a_dataframe_dimensiones, resultados_a_dataframe_preguntas


def grafica_barras_dimensiones(resultado: ResultadoTablero):
    df = resultados_a_dataframe_dimensiones(resultado)
    fig = px.bar(
        df,
        x="dimensión",
        y="puntaje",
        text="puntaje",
        title="Puntaje por dimensión",
    )
    fig.update_layout(yaxis_title="Puntaje (0-100)", xaxis_title="")
    fig.update_traces(textposition="outside")
    return fig


def grafica_radar_dimensiones(resultado: ResultadoTablero):
    df = resultados_a_dataframe_dimensiones(resultado)
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
        polar={"radialaxis": {"visible": True, "range": [0, 100]}},
        title="Radar general de madurez digital",
        showlegend=True,
    )
    return fig


def grafica_radar_gobierno_datos(resultado: ResultadoTablero):
    preguntas_clave = [
        ("q2", "Estrategia"),
        ("q7", "Conectividad"),
        ("q14", "Datos"),
        ("q18", "Accesibilidad"),
        ("q22", "Continuidad"),
        ("q27", "Factores críticos"),
    ]

    mapa = resultados_a_dataframe_preguntas(resultado).set_index("pregunta")["puntaje"].to_dict()
    categorias = [etiqueta for _, etiqueta in preguntas_clave]
    valores = [float(mapa.get(q, 0.0)) for q, _ in preguntas_clave]
    categorias.append(categorias[0])
    valores.append(valores[0])

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill="toself",
            name="Capacidades clave",
        )
    )
    fig.update_layout(
        polar={"radialaxis": {"visible": True, "range": [0, 100]}},
        title="Radar de capacidades clave",
        showlegend=True,
    )
    return fig


def tabla_recomendaciones(resultado: ResultadoTablero) -> pd.DataFrame:
    return pd.DataFrame(resultado.recomendaciones)
