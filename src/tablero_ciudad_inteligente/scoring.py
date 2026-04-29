"""Lógica de cálculo de puntajes del tablero."""

from __future__ import annotations

import pandas as pd

from tablero_ciudad_inteligente.config import (
    ACRONIMOS_DIMENSION,
    ALERTAS_CONFIG,
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
    if ";" in texto:
        return [parte.strip() for parte in texto.split(";") if parte.strip()]
    return [texto]


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


def _puntuar_ordinal_q2_flexible(texto: str) -> float:
    """Soporta tanto el formato antiguo como el nuevo wording del plan local."""
    if not texto:
        return 0.0

    exacto = OPCIONES_ORDINALES.get("q2", {}).get(texto)
    if exacto is not None:
        return exacto

    texto_norm = texto.lower()

    if "no existe" in texto_norm:
        return 0.0
    if "inicial" in texto_norm or "formulación" in texto_norm or "formulacion" in texto_norm:
        return 0.25
    if "vigente" in texto_norm or "acciones definidas" in texto_norm:
        return 0.5
    if "actualizado periódicamente" in texto_norm or "actualizado periodicamente" in texto_norm:
        if "seguimiento" in texto_norm or "evaluación" in texto_norm or "evaluacion" in texto_norm:
            return 1.0
        return 0.75

    return 0.0


def _puntuar_ordinal(pregunta: str, valor: object) -> float:
    texto = _a_texto(valor)

    if pregunta == "q2":
        return _puntuar_ordinal_q2_flexible(texto)

    return OPCIONES_ORDINALES.get(pregunta, {}).get(texto, 0.0)


def puntuar_pregunta(pregunta: str, valor: object) -> float:
    if pregunta in OPCIONES_ORDINALES:
        return _puntuar_ordinal(pregunta, valor)
    if pregunta in OPCIONES_MULTIPLE:
        return _puntuar_multiple(pregunta, valor)
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

    for pregunta in ("q14", "q18", "q22"):
        cfg = ALERTAS_CONFIG[pregunta]
        if puntuar_pregunta(pregunta, fila.get(pregunta, "")) < cfg["threshold"]:
            alertas.append(cfg["message"])

    prioridades = _parsear_multiple(fila.get("q24", ""))
    for prioridad in prioridades[: ALERTAS_CONFIG["q24_top_n"]]:
        if prioridad in PRIORIZACION_OBSTACULOS:
            alertas.append(ALERTAS_CONFIG["q24_message_template"].format(prioridad=prioridad))

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
        ciudad=_a_texto(fila.get("entidad", "Observación sin nombre")) or "Observación sin nombre",
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
                "dimensión": f"{d.nombre} ({ACRONIMOS_DIMENSION.get(d.clave, d.clave)})",
                "puntaje": d.puntaje,
                "nivel": d.nivel,
            }
            for d in resultado.dimensiones
        ]
    )


def resultados_a_dataframe_dimensiones_plots(resultado: ResultadoTablero) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dimensión": ACRONIMOS_DIMENSION.get(d.clave, d.clave),
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