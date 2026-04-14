"""Generación de recomendaciones automáticas."""

from __future__ import annotations

from typing import Any

from tablero_ciudad_inteligente.config import ResultadoDimension


def _recomendacion_dimension(clave: str) -> dict[str, Any]:
    base = {
        "A": {
            "dimension": "Visión estratégica y gobernanza",
            "siguiente_paso": "Formalizar o fortalecer una estrategia de transición digital con responsables, metas y seguimiento intersecretarial.",
            "literatura": "UN-Habitat - People-Centred Smart Cities",
        },
        "B": {
            "dimension": "Infraestructura y capacidades técnicas",
            "siguiente_paso": "Priorizar conectividad, digitalización de trámites y fortalecimiento de capacidades técnicas internas.",
            "literatura": "ISO 37122 + OECD Smart Cities and Inclusive Growth",
        },
        "C": {
            "dimension": "Gobernanza de datos, privacidad y ética",
            "siguiente_paso": "Definir política de datos, interoperabilidad mínima, privacidad y lineamientos de ética digital.",
            "literatura": "OECD Smart City Data Governance",
        },
        "D": {
            "dimension": "Participación ciudadana y equidad digital",
            "siguiente_paso": "Ampliar mecanismos digitales de participación y accesibilidad para grupos vulnerables.",
            "literatura": "UN-Habitat + OECD Inclusive Growth",
        },
        "E": {
            "dimension": "Economía creativa y patrimonio",
            "siguiente_paso": "Conectar cultura, patrimonio y digitalización mediante plataformas, archivos y laboratorios creativos.",
            "literatura": "UN-Habitat / agendas de cultura digital local",
        },
        "F": {
            "dimension": "Financiamiento y alianzas",
            "siguiente_paso": "Asegurar continuidad presupuestaria y construir alianzas con academia, sector privado y cooperación.",
            "literatura": "OECD / estrategias de financiamiento urbano",
        },
        "G": {
            "dimension": "Obstáculos y aprendizajes",
            "siguiente_paso": "Convertir obstáculos diagnosticados en una hoja de ruta priorizada con responsables y tiempos.",
            "literatura": "Roadmapping institucional y mejora continua",
        },
    }
    return base[clave]


def construir_recomendaciones(fila, dimensiones: list[ResultadoDimension]) -> list[dict[str, Any]]:
    recomendaciones: list[dict[str, Any]] = []

    for dimension in sorted(dimensiones, key=lambda x: x.puntaje)[:3]:
        if dimension.puntaje < 75:
            base = _recomendacion_dimension(dimension.clave)
            recomendaciones.append(
                {
                    "prioridad": "Alta" if dimension.puntaje < 50 else "Media",
                    "dimension": base["dimension"],
                    "diagnostico": f"La dimensión presenta un nivel {dimension.nivel.lower()} con puntaje de {dimension.puntaje}.",
                    "siguiente_paso": base["siguiente_paso"],
                    "literatura": base["literatura"],
                }
            )

    if not recomendaciones:
        recomendaciones.append(
            {
                "prioridad": "Seguimiento",
                "dimension": "Balance general",
                "diagnostico": "La ciudad muestra un perfil relativamente sólido en todas las dimensiones evaluadas.",
                "siguiente_paso": "Pasar de consolidación a monitoreo continuo con indicadores temporales, benchmarking y auditoría externa.",
                "literatura": "ISO 37122 + evaluación continua",
            }
        )

    return recomendaciones
