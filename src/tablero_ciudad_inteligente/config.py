"""Configuración del instrumento y reglas de evaluación."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


DIMENSIONES = {
    "A": "Visión Estratégica, Gobernanza y Acciones Gubernamentales",
    "B": "Infraestructura, Capacidades Técnicas y Plataformas",
    "C": "Gobernanza de Datos, Privacidad y Ética",
    "D": "Participación Ciudadana y Equidad Digital",
    "E": "Economía Creativa y Patrimonio",
    "F": "Financiamiento, Sostenibilidad y Alianzas",
    "G": "Obstáculos, Aprendizajes y Recomendaciones",
}

PREGUNTAS_DIMENSION = {
    "A": ["q1", "q2", "q3", "q4", "q5", "q6"],
    "B": ["q7", "q8", "q9", "q10", "q11", "q12"],
    "C": ["q13", "q14", "q15"],
    "D": ["q16", "q17", "q18"],
    "E": ["q19", "q20"],
    "F": ["q21", "q22", "q23"],
    "G": ["q24", "q25", "q26", "q27"],
}

OPCIONES_MULTIPLE = {
    "q1": [
        "Existe un plan local de transformación digital.",
        "Existe una oficina / secretaría encargada de los temas de transformación digital.",
        "Existe un consejo / organismo ciudadano de transición digital.",
        "Existen proyectos, programas y/o acciones que trabajan en la transformación digital.",
        "Existen plataformas de atención ciudadana, participación ciudadana, consulta de información SIG, monitoreo de acciones o proyectos en funcionamiento.",
    ],
    "q4": [
        "Inauguración de un proyecto relevante (SIG, participación ciudadana, atención ciudadana u otros).",
        "Entrega de apoyos o servicios para reducir la brecha digital en población vulnerable.",
        "Presentación o renovación de un plan o estrategia local de transición digital.",
        "Sesión activa del consejo u organismo ciudadano de transición digital.",
        "Firma de convenios con entidades del sector privado, público o internacional.",
        "Colocación de sensores, cámaras u otros dispositivos para monitoreo urbano.",
    ],
    "q5": [
        "Plataforma digital de participación o atención ciudadana.",
        "Plataforma SIG para desarrollo urbano, servicios públicos o medio ambiente.",
        "Programas o acciones para disminuir la brecha digital en población vulnerable.",
        "Plan o estrategia local de transición digital con consejo ciudadano.",
        "Transversalización digital del trabajo entre secretarías.",
    ],
    "q6": [
        "Mesas de trabajo con sociedad civil, universidades, organismos públicos o ciudadanía.",
        "Consejo ciudadano para la transición digital.",
        "Gabinetes de trabajo internos para proyectos digitales.",
        "Acuerdos de coordinación entre niveles de gobierno.",
    ],
    "q8": [
        "4G/5G",
        "Servicio satelital",
        "Fibra óptica dedicada",
        "Cobertura pública gratuita (parques, plazas, equipamientos)",
        "Otro",
    ],
    "q9": [
        "Desarrollo urbano (trámites de construcción, permisos)",
        "Servicios públicos (iluminación, limpieza, recolección)",
        "Trámites y pagos municipales",
        "Programas sociales y actividades municipales",
        "Seguridad",
        "Otro",
    ],
    "q10": [
        "Plataforma SIG y repositorios digitales",
        "Plataforma de trámites y atención ciudadana",
        "Sensores urbanos (tráfico, calidad del aire, movilidad)",
        "Sistemas de seguridad y respuesta en tiempo real",
        "Modelación y escenarios prospectivos",
        "Flujos de trabajo digitalizados entre secretarías",
    ],
    "q12": [
        "Oportunidad de crecimiento profesional",
        "Participación en el cambio social a través de la tecnología",
        "Espacio para participación de jóvenes",
        "Aprendizaje de retos complejos",
        "Estigmatización o resistencia interna",
    ],
    "q13": [
        "Comités de ética de datos",
        "Política municipal de datos abiertos.",
        "Licencias de datos abiertos sobre información municipal",
        "Protocolos o normativas regionales/nacionales de datos públicos",
        "Procesos de prevención de pérdida o fuga de datos",
        "Avisos de privacidad de datos personales.",
    ],
    "q16": [
        "Consultas públicas o referéndums digitales",
        "Presupuesto participativo digital",
        "Reporte ciudadano de problemáticas urbanas",
        "Mecanismos de denuncia o inconformidad",
        "Otros",
    ],
    "q17": [
        "Capacitación digital para población en general",
        "Programas especializados para adultos mayores",
        "Acciones con enfoque de género",
        "Acciones para comunidades indígenas o rurales",
        "Préstamo o apoyo para acceso a dispositivos",
    ],
    "q20": [
        "Digitalización de archivos o patrimonio cultural",
        "Festivales, ferias o eventos creativos con componente digital",
        "Incubadoras o laboratorios creativos",
        "Plataformas para creadores locales basadas en datos abiertos",
        "Otro",
    ],
    "q21": [
        "Presupuesto municipal",
        "Fondos estatales o nacionales",
        "Cooperación internacional",
        "Alianzas público-privadas",
        "Recursos propios o autogenerados",
    ],
    "q23": [
        "Universidades o centros de investigación",
        "Empresas del sector tecnológico",
        "Organizaciones de la sociedad civil",
        "Organismos internacionales",
        "Otros",
    ],
    "q25": [
        "Obstáculos técnicos",
        "Obstáculos institucionales",
        "Obstáculos políticos",
        "Obstáculos sociales (desconfianza o baja adopción)",
        "Obstáculos presupuestarios",
        "Otros",
    ],
    "q26": [
        "Mejora de infraestructura digital",
        "Interoperabilidad y calidad de datos",
        "Creación de capacidades humanas",
        "Escalabilidad de proyectos piloto",
        "Mayor participación ciudadana",
        "Sostenibilidad económica de iniciativas",
    ],
    "q27": [
        "Liderazgo político",
        "Coordinación entre secretarías",
        "Participación ciudadana",
        "Financiamiento estable",
        "Colaboración con universidades o sector privado",
        "Capacidades internas",
    ],
}

OPCIONES_NULAS = {
    "q1": ["Ninguna de las anteriores."],
    "q6": ["Ninguna de las anteriores."],
    "q17": ["Ninguna de las anteriores"],
    "q20": ["Ninguno"],
    "q23": ["No existen alianzas relevantes"],
}

OPCIONES_NEGATIVAS = {
    "q12": ["Estigmatización o resistencia interna"],
}

OPCIONES_ORDINALES = {
    "q2": {
        "No existe un plan o estrategia formal, ni hay proyectos que trabajen la transición digital.": 0.0,
        "En el plan de gobierno de corto plazo existen acciones para la transición digital, pero no se ha consolidado un plan o estrategia formal.": 0.25,
        "Existe un plan o estrategia formal, pero no hay una oficina que le dé seguimiento.": 0.5,
        "Existe un plan o estrategia formal, proyectos y acciones gestionadas por una oficina especializada.": 0.75,
        "El plan o estrategia es parte de un proceso continuo de transición digital, gerenciado por una oficina especializada con acompañamiento ciudadano.": 1.0,
    },
    "q3": {
        "No existe un equipo especializado, pero algunas secretarías cuentan con capital humano informalmente dedicado al tema.": 0.2,
        "Varias secretarías cuentan con equipos que atienden aspectos digitales, pero sin coordinación transversal.": 0.35,
        "Existe una coordinación o dirección especializada dentro de una secretaría.": 0.5,
        "Existe una secretaría u oficina operativa encargada de la transición digital que depende directamente de la autoridad local.": 0.75,
        "Existe una secretaría u oficina operativa que lidera la transición digital y coordina transversalmente con equipos especializados en cada secretaría.": 1.0,
    },
    "q7": {
        "Menos de 50%": 0.2,
        "Entre 50% y 70%": 0.45,
        "Entre 70% y 90%": 0.75,
        "Total o casi total (+90%)": 1.0,
    },
    "q11": {
        "Recomendaciones o referencias del sector privado": 0.25,
        "Convocatorias abiertas a ciudadanía": 0.4,
        "Búsqueda de talento nacional o internacional": 0.55,
        "Capacitación y desarrollo de talento interno": 0.75,
        "Servicio profesional de carrera público": 1.0,
    },
    "q14": {
        "No existe una política de datos ni repositorios organizados.": 0.0,
        "Existen repositorios básicos por secretaría sin interoperabilidad.": 0.25,
        "Hay una plataforma de datos abiertos con algunos estándares mínimos.": 0.5,
        "Existen protocolos de calidad e interoperabilidad entre secretarías.": 0.75,
        "La ciudad cuenta con un sistema integrado de datos urbanos con acceso público y uso sistemático.": 1.0,
    },
    "q15": {
        "No existe regulación ni discusión institucional.": 0.0,
        "Existe discusión interna, pero sin documentos o lineamientos.": 0.25,
        "Existen lineamientos básicos de ética digital y uso de IA.": 0.5,
        "Existen protocolos y evaluaciones de impacto algorítmico.": 0.75,
        "Existe un marco avanzado con participación ciudadana y auditorías externas.": 1.0,
    },
    "q18": {
        "No existen adaptaciones ni accesos especiales": 0.0,
        "Existen adaptaciones mínimas (manuales, apoyo presencial)": 0.25,
        "Existen servicios básicos adaptados para grupos específicos": 0.5,
        "Los servicios están ampliamente adaptados con accesibilidad universal": 0.75,
        "Existen protocolos de inclusión digital sistemática": 1.0,
    },
    "q19": {
        "No existe vinculación.": 0.0,
        "Existen acciones aisladas en cultura o patrimonio.": 0.25,
        "Existen programas digitales para promoción cultural o creativa.": 0.5,
        "Existen iniciativas con creadores locales en plataformas digitales.": 0.75,
        "La ciudad tiene una estrategia formal que integra cultura, creatividad y digitalización.": 1.0,
    },
    "q22": {
        "No existe continuidad.": 0.0,
        "Existe financiamiento ocasional.": 0.25,
        "Hay continuidad parcial según área.": 0.5,
        "Existe continuidad y programación multianual.": 0.75,
        "La continuidad está garantizada mediante instrumentos formales.": 1.0,
    },
}

PRIORIZACION_OBSTACULOS = {
    "Falta de política pública continua": "institucionalidad",
    "Carencia de presupuesto o infraestructura": "financiamiento",
    "Falta de capital humano capacitado": "capacidades",
    "Indiferencia o subestimación del tema": "liderazgo",
    "Resistencia al cambio y opacidad interna": "gobernanza",
}

LITERATURA = {
    "general": [
        {
            "titulo": "UN-Habitat - International Guidelines on People-Centred Smart Cities",
            "descripcion": "Marco para orientar una transición digital centrada en personas, inclusión y gobernanza.",
            "fuente": "UN-Habitat",
        },
        {
            "titulo": "OECD - Smart City Data Governance",
            "descripcion": "Buenas prácticas para gobernanza, interoperabilidad y uso responsable de datos urbanos.",
            "fuente": "OECD",
        },
        {
            "titulo": "ISO 37122 - Indicators for Smart Cities",
            "descripcion": "Conjunto de indicadores para medir desempeño y madurez de ciudades inteligentes.",
            "fuente": "ISO",
        },
    ]
}


@dataclass
class ResultadoDimension:
    clave: str
    nombre: str
    puntaje: float
    nivel: str
    detalle: dict[str, float]


@dataclass
class ResultadoTablero:
    ciudad: str
    fecha: str
    puntaje_global: float
    nivel_global: str
    dimensiones: list[ResultadoDimension]
    recomendaciones: list[dict[str, Any]]
    alertas: list[str]
    literatura: list[dict[str, str]]
