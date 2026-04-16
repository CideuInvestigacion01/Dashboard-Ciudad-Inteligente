"""Generación de recomendaciones automáticas."""

from __future__ import annotations

from typing import Any

from tablero_ciudad_inteligente.config import (
    RECOMENDACIONES_CONFIG,
    RECOMENDACIONES_DIMENSION,
    ResultadoDimension,
)


def _recomendacion_dimension(clave: str) -> dict[str, Any]:
    return RECOMENDACIONES_DIMENSION[clave]


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

    return recomendaciones