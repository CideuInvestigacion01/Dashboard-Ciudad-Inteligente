"""Lógica de cálculo de puntajes del tablero."""

from __future__ import annotations

from typing import Iterable

import pandas as pd

from tablero_ciudad_inteligente.config import (
    DIMENSIONES,
    LITERATURA,
    OPCIONES_MULTIPLE,
    OPCIONES_NEGATIVAS,
    OPCIONES_NULAS,
    OPCIONES_ORDINALES,
    PREGUNTAS_DIMENSION,
    PRIORIZACION_OBSTACULOS,
    ResultadoDimension,
    ResultadoTablero,
)
from tablero_ciudad_inteligente.recommendations import construir_recomendaciones


def _a_texto(valor: object) -> str:
    if pd.isna(valor):
        return ""
    return str(valor).strip()


def _parsear_multiple(valor: object) -> list[str]:
    texto = _a_texto(valor)
    if not texto:
        return []
    return [parte.strip() for parte in texto.split(";") if parte.strip()]


def _puntuar_multiple(pregunta: str, valor: object) -> float:
    seleccionadas = _parsear_multiple(valor)
    if not seleccionadas:
        return 0.0

    if pregunta in OPCIONES_NULAS and any(x in seleccionadas for x in OPCIONES_NULAS[pregunta]):
        return 0.0

    base = OPCIONES_MULTIPLE.get(pregunta, [])
    if not base:
        return 0.0

    positivas = [x for x in seleccionadas if x not in OPCIONES_NEGATIVAS.get(pregunta, [])]
    negativas = [x for x in seleccionadas if x in OPCIONES_NEGATIVAS.get(pregunta, [])]

    score = min(len(positivas), len(base)) / len(base)
    if negativas:
        score = max(score - 0.2 * len(negativas), 0.0)
    return min(score, 1.0)


def _puntuar_ordinal(pregunta: str, valor: object) -> float:
    texto = _a_texto(valor)
    return OPCIONES_ORDINALES.get(pregunta, {}).get(texto, 0.0)


def _puntuar_obstaculos_priorizados(valor: object) -> float:
    """No castiga fuertemente el reconocimiento de problemas.

    Si la ciudad puede identificar prioridades, se interpreta como madurez diagnóstica.
    """
    seleccionadas = _parsear_multiple(valor)
    if not seleccionadas:
        return 0.2
    return min(0.4 + (0.1 * len(seleccionadas)), 0.8)


def puntuar_pregunta(pregunta: str, valor: object) -> float:
    if pregunta in OPCIONES_ORDINALES:
        return _puntuar_ordinal(pregunta, valor)
    if pregunta in OPCIONES_MULTIPLE:
        return _puntuar_multiple(pregunta, valor)
    if pregunta == "q24":
        return _puntuar_obstaculos_priorizados(valor)
    return 0.0


def nivel_desde_puntaje(puntaje: float) -> str:
    if puntaje < 25:
        return "Inicial"
    if puntaje < 50:
        return "Emergente"
    if puntaje < 75:
        return "En consolidación"
    return "Avanzado"


def extraer_alertas(fila: pd.Series) -> list[str]:
    alertas: list[str] = []

    if puntuar_pregunta("q14", fila.get("q14", "")) < 0.5:
        alertas.append("La gobernanza de datos muestra un nivel bajo o fragmentado.")
    if puntuar_pregunta("q18", fila.get("q18", "")) < 0.5:
        alertas.append("La accesibilidad e inclusión digital requieren atención prioritaria.")
    if puntuar_pregunta("q22", fila.get("q22", "")) < 0.5:
        alertas.append("La continuidad presupuestaria es insuficiente para sostener la agenda digital.")

    prioridades = _parsear_multiple(fila.get("q24", ""))
    for prioridad in prioridades[:2]:
        if prioridad in PRIORIZACION_OBSTACULOS:
            alertas.append(f"Obstáculo priorizado detectado: {prioridad}.")

    return alertas


def calcular_resultados(fila: pd.Series) -> ResultadoTablero:
    resultados_dimensiones: list[ResultadoDimension] = []

    for clave_dim, preguntas in PREGUNTAS_DIMENSION.items():
        detalle = {pregunta: puntuar_pregunta(pregunta, fila.get(pregunta, "")) * 100 for pregunta in preguntas}
        puntaje_dimension = sum(detalle.values()) / max(len(detalle), 1)
        resultados_dimensiones.append(
            ResultadoDimension(
                clave=clave_dim,
                nombre=DIMENSIONES[clave_dim],
                puntaje=round(puntaje_dimension, 2),
                nivel=nivel_desde_puntaje(puntaje_dimension),
                detalle=detalle,
            )
        )

    puntaje_global = round(
        sum(d.puntaje for d in resultados_dimensiones) / max(len(resultados_dimensiones), 1),
        2,
    )
    recomendaciones = construir_recomendaciones(fila, resultados_dimensiones)

    return ResultadoTablero(
        ciudad=_a_texto(fila.get("ciudad", "Ciudad sin nombre")) or "Ciudad sin nombre",
        fecha=_a_texto(fila.get("fecha", "Sin fecha")) or "Sin fecha",
        puntaje_global=puntaje_global,
        nivel_global=nivel_desde_puntaje(puntaje_global),
        dimensiones=resultados_dimensiones,
        recomendaciones=recomendaciones,
        alertas=extraer_alertas(fila),
        literatura=LITERATURA["general"],
    )


def resultados_a_dataframe_dimensiones(resultado: ResultadoTablero) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dimensión": d.nombre,
                "puntaje": d.puntaje,
                "nivel": d.nivel,
            }
            for d in resultado.dimensiones
        ]
    )


def resultados_a_dataframe_preguntas(resultado: ResultadoTablero) -> pd.DataFrame:
    filas: list[dict[str, object]] = []
    for dimension in resultado.dimensiones:
        for pregunta, puntaje in dimension.detalle.items():
            filas.append(
                {
                    "dimensión": dimension.nombre,
                    "pregunta": pregunta,
                    "puntaje": round(puntaje, 2),
                }
            )
    return pd.DataFrame(filas)
