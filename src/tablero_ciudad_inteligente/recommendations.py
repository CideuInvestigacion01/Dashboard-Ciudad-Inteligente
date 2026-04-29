"""Generación de recomendaciones automáticas."""

from __future__ import annotations

from typing import Any

from tablero_ciudad_inteligente.config import (
    RECOMENDACIONES_CONFIG,
    RECOMENDACIONES_DIMENSION,
    RECOMENDACIONES_NARRATIVAS_EXTRAS,
    ResultadoDimension,
)


def _a_texto(valor: object) -> str:
    if valor is None:
        return ""
    return str(valor).strip()


def _parsear_multiple(valor: object) -> list[str]:
    texto = _a_texto(valor)
    if not texto:
        return []
    return [parte.strip() for parte in texto.split(";") if parte.strip()]


def _recomendacion_dimension(clave: str) -> dict[str, Any]:
    return RECOMENDACIONES_DIMENSION[clave]


def _agregar_recomendaciones_extras(fila, recomendaciones: list[dict[str, Any]]) -> list[dict[str, Any]]:
    existentes = {r["dimension"] for r in recomendaciones}

    acciones_innovacion = _parsear_multiple(fila.get("extra_innovacion_gobierno", ""))
    if len(acciones_innovacion) < RECOMENDACIONES_NARRATIVAS_EXTRAS["innovacion_gobierno_min_acciones"]:
        recomendaciones.append(
            {
                "prioridad": RECOMENDACIONES_CONFIG["narrative_priority_label"],
                "dimension": RECOMENDACIONES_NARRATIVAS_EXTRAS["innovacion_gobierno_dimension"],
                "diagnostico": RECOMENDACIONES_NARRATIVAS_EXTRAS["innovacion_gobierno_diagnostico"],
                "siguiente_paso": RECOMENDACIONES_NARRATIVAS_EXTRAS["innovacion_gobierno_siguiente_paso"],
                "literatura": RECOMENDACIONES_NARRATIVAS_EXTRAS["innovacion_gobierno_literatura"],
            }
        )

    acciones_economia = _parsear_multiple(fila.get("extra_economia_patrimonio_municipio", ""))
    if (
        len(acciones_economia) < RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_min_acciones"]
        and RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_dimension"] not in existentes
    ):
        recomendaciones.append(
            {
                "prioridad": RECOMENDACIONES_CONFIG["narrative_priority_label"],
                "dimension": RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_dimension"],
                "diagnostico": RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_diagnostico"],
                "siguiente_paso": RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_siguiente_paso"],
                "literatura": RECOMENDACIONES_NARRATIVAS_EXTRAS["economia_patrimonio_literatura"],
            }
        )

    return recomendaciones


def construir_recomendaciones(fila, dimensiones: list[ResultadoDimension]) -> list[dict[str, Any]]:
    recomendaciones: list[dict[str, Any]] = []

    for dimension in sorted(dimensiones, key=lambda x: x.puntaje):
        if dimension.puntaje < RECOMENDACIONES_CONFIG["show_recommendations_below"]:
            base = _recomendacion_dimension(dimension.clave)
            recomendaciones.append(
                {
                    "prioridad": (
                        RECOMENDACIONES_CONFIG["priority_high_label"]
                        if dimension.puntaje < RECOMENDACIONES_CONFIG["high_priority_threshold"]
                        else RECOMENDACIONES_CONFIG["priority_medium_label"]
                    ),
                    "dimension": base["dimension"],
                    "diagnostico": RECOMENDACIONES_CONFIG["diagnostico_template"].format(
                        nivel=dimension.nivel.lower(),
                        puntaje=dimension.puntaje,
                    ),
                    "siguiente_paso": base["siguiente_paso"],
                    "literatura": base["literatura"],
                }
            )

    if not recomendaciones:
        recomendaciones.append(
            {
                "prioridad": RECOMENDACIONES_CONFIG["priority_followup_label"],
                "dimension": RECOMENDACIONES_CONFIG["fallback_dimension"],
                "diagnostico": RECOMENDACIONES_CONFIG["fallback_diagnostico"],
                "siguiente_paso": RECOMENDACIONES_CONFIG["fallback_siguiente_paso"],
                "literatura": RECOMENDACIONES_CONFIG["fallback_literatura"],
            }
        )

    recomendaciones = _agregar_recomendaciones_extras(fila, recomendaciones)

    return recomendaciones