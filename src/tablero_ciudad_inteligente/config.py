"""Configuración del instrumento, textos del dashboard y reglas de evaluación."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# =========================
# Textos generales del dashboard
# =========================

TEXTOS_APP = {
    "page_title": "Tablero de Ciudad Inteligente",
    "main_title": "Tablero de Autoevaluación de Transición Digital y Ciudades Inteligentes",
    "main_caption": "Diagnóstico visual del estado de madurez digital de una ciudad a partir de respuestas de encuesta.",
    "sidebar_nav_title": "### Navegación",
    "sidebar_nav_label": "Ir a",
    "sidebar_nav_home": "Inicio",
    "sidebar_nav_dashboard": "Tablero",
    "sidebar_data_title": "### Fuente de datos",
    "sidebar_uploader_label": "Sube un CSV o XLSX exportado desde KoboToolbox",
    "sidebar_security_title": "### Seguridad recomendada",
    "sidebar_security_info": "Esta versión no exige contraseña en el código. Para despliegues reales se recomienda autenticación, HTTPS y control de acceso por roles.",
    "example_dataset_info": "No se cargó archivo. Se usa el dataset de ejemplo incluido en el proyecto.",
    "no_data_error": "No hay datos para mostrar.",
    "evaluation_selector_label": "Selecciona una evaluación",
    "metric_territory": "Territorio",
    "metric_global_score": "Puntaje global",
    "metric_global_level": "Nivel global",
    "section_general_state": "## Estado general",
    "section_dimensions": "## Indicadores por dimensión",
    "section_alerts": "## Alertas y hallazgos",
    "section_recommendations": "## Recomendaciones",
    "section_literature": "## Literatura sugerida",
    "no_critical_alerts": "- No se detectaron alertas críticas en esta evaluación.",
    "recommendation_priority_label": "Prioridad",
    "recommendation_dimension_label": "Dimensión",
    "recommendation_diagnostic_label": "Diagnóstico",
    "recommendation_next_step_label": "Siguiente paso",
    "recommendation_literature_label": "Literatura asociada",
    "recommendation_case_studies_label": "Casos de referencia",
    "recommendations_download_button": "Descargar recomendaciones como CSV",
    "recommendations_download_filename": "recomendaciones.csv",
}


MENSAJES_NIVEL_GLOBAL = {
    "Inicial": "El territorio muestra avances aislados o parciales. La prioridad es consolidar capacidades y continuidad y reducir la fragmentación institucional. Fortalecer la coordinación interinstitucional y avanzar hacia interoperabilidad básica, integrando iniciativas existentes en una estrategia común.",
    "Emergente": "El territorio muestra avances aislados o parciales. La prioridad es consolidar capacidades y continuidad y reducir la fragmentación institucional. Fortalecer la coordinación interinstitucional y avanzar hacia interoperabilidad básica, integrando iniciativas existentes en una estrategia común.",
    "En consolidación": "El territorio cuenta con bases importantes en la integración de los elementos de una ciudad inteligente. El siguiente paso es mejorar interoperabilidad, inclusión y sostenibilidad. Profundizar en gobernanza de datos, evaluación de impacto y mecanismos de inclusión digital, incorporando métricas y monitoreo continuo.",
    "Avanzado": "El territorio presenta un perfil avanzado de integración a la transicisión digital. Conviene pasar a monitoreo continuo, evidencia de impacto y mejora fina. De esta manera se podrá transitar hacia innovación basada en datos, auditoría algorítmica, y modelos de gobernanza participativa del dato",
}


# =========================
# Página de bienvenida
# =========================

BIENVENIDA_CONFIG = {
    "titulo": "Bienvenida",
    "subtitulo": "Guía breve para entender el instrumento y leer los resultados del tablero",
    "introduccion": [
        "La presente matriz de autoevaluación forma parte central de la Caja de Herramientas de Autoevaluación para Ciudades Inteligentes en Iberoamérica, desarrollada como resultado estratégico de la investigación Transición Digital a Ciudades Inteligentes en Iberoamérica como parte del programa “El Centro Histórico de La Habana hacia un modelo de ciudad inteligente con énfasis en el fomento de la economía creativa” desarrollado en colaboración entre el CIDEU y la Oficina del Historiador de la Ciudad de La Habana con financiamiento de la Unión Europea y el Ayuntamiento de Barcelona.",
        "Su objetivo es ofrecer a los gobiernos locales un instrumento práctico, sistemático y contextualizado que les permita analizar el estado actual de sus procesos de transición digital y desarrollo de ciudades inteligentes, considerando las particularidades institucionales, tecnológicas y socioeconómicas de cada territorio.",
        "El diseño de las preguntas responde a un enfoque metodológico cualitativo–cuantitativo, basado en la sistematización de entrevistas semiestructuradas realizadas a actores clave del ámbito gubernamental local, así como en la revisión de marcos internacionales y experiencias regionales.",
        "El instrumento de autoevaluación está constituido por un conjunto de preguntas cerradas y de opción múltiple que permiten identificar patrones, brechas, avances y áreas prioritarias de intervención en dimensiones clave como la gobernanza digital, la infraestructura tecnológica, la modernización de los servicios públicos, la participación ciudadana, la equidad digital, la economía creativa y la gestión de datos urbanos.",
        "La autoevaluación no pretende establecer rankings ni comparaciones normativas entre ciudades, sino funcionar como una herramienta de diagnóstico reflexivo y orientador, promoviendo la generación de conocimiento situado y la toma de decisiones informada.",
        "Al facilitar la identificación de niveles diferenciados de desarrollo y capacidades, este instrumento busca fortalecer la planificación estratégica local, fomentar la mejora continua y apoyar la construcción de rutas de acción adaptadas a los distintos contextos urbanos de Iberoamérica, contribuyendo así a una transición digital más inclusiva, sostenible y con objetivos claros y diferenciados.",
    ],
    "seccion_que_hace": "## ¿Qué hace este tablero?",
    "que_hace": [
        "Este tablero transforma las respuestas de la autoevaluación en puntajes y visualizaciones que ayudan a identificar fortalezas, brechas y prioridades de acción.",
        "Los resultados están organizados por dimensiones temáticas para facilitar la lectura y apoyar conversaciones de planeación, mejora continua y toma de decisiones.",
    ],
    "seccion_como_se_calcula": "## ¿Cómo se calcula el porcentaje?",
    "como_se_calcula": [
        "Cada pregunta se transforma primero a una escala de 0 a 1.",
        "Después, los resultados de las preguntas de una misma dimensión se promedian.",
        "Ese promedio se multiplica por 100 para obtener el puntaje de la dimensión.",
        "Finalmente, el puntaje global se calcula como el promedio simple de todas las dimensiones.",
    ],
    "tipos_pregunta_titulo": "### Tipos de pregunta usados en el cálculo",
    "tipos_pregunta": [
        {
            "nombre": "Preguntas de selección única ordinal",
            "descripcion": "Son preguntas donde las opciones representan distintos niveles de avance. A cada opción se le asigna un valor entre 0 y 1 según su nivel de desarrollo.",
        },
        {
            "nombre": "Preguntas de selección múltiple",
            "descripcion": "Se calcula la proporción de opciones seleccionadas respecto al total de opciones válidas de esa pregunta. Si aparece una opción como “Ninguna de las anteriores”, el puntaje de esa pregunta se considera 0.",
        },
    ],
    "nota_q24": "La pregunta q24 sobre priorización de obstáculos no entra al puntaje global. Actualmente se usa para generar alertas y hallazgos.",
    "seccion_dimensiones": "## ¿Cómo está construida cada dimensión?",
    "seccion_niveles": "## ¿Qué significa cada nivel?",
    "niveles": [
        {
            "nivel": "Inicial",
            "rango": "Menor a 25 puntos",
            "descripcion": "Capacidades muy limitadas o fragmentadas. Todavía faltan bases institucionales, tecnológicas o de coordinación.",
        },
        {
            "nivel": "Emergente",
            "rango": "De 25 a menos de 50 puntos",
            "descripcion": "Existen avances aislados o parciales. Hay iniciativas en marcha, pero todavía no están suficientemente consolidadas.",
        },
        {
            "nivel": "En consolidación",
            "rango": "De 50 a menos de 75 puntos",
            "descripcion": "Existen bases importantes, estructuras o programas en funcionamiento. El reto principal es mejorar integración, continuidad e inclusión.",
        },
        {
            "nivel": "Avanzado",
            "rango": "75 puntos o más",
            "descripcion": "El territorio muestra un desarrollo más robusto. El siguiente paso es fortalecer monitoreo, evidencia de impacto y mejora continua.",
        },
    ],
    "seccion_graficas": "## ¿Cómo se construyen y cómo se leen las gráficas?",
    "graficas": [
        {
            "titulo": "Puntaje por dimensión",
            "como_se_construye": "Esta gráfica usa el puntaje final de cada dimensión. Cada barra representa el promedio de las preguntas que pertenecen a esa dimensión.",
            "como_se_interpreta": "Mientras más alta es la barra, mayor es el nivel de desarrollo reportado en esa dimensión.",
        },
        {
            "titulo": "Radar general de madurez digital",
            "como_se_construye": "Esta gráfica usa los mismos puntajes por dimensión que la gráfica de barras, pero los organiza en forma radial usando los acrónimos de cada dimensión.",
            "como_se_interpreta": "Una figura más amplia y equilibrada sugiere un desarrollo más homogéneo entre dimensiones. Una figura irregular muestra contrastes entre áreas fuertes y áreas rezagadas.",
        },
        {
            "titulo": "Radar de capacidades clave",
            "como_se_construye": "Esta gráfica no usa todas las preguntas del instrumento. Se construye a partir de seis componentes clave: la estrategia o plan local de transformación digital, la conectividad, la gestión de datos urbanos, la accesibilidad de los servicios digitales para grupos vulnerables, la continuidad presupuestaria de los proyectos digitales y los factores que han sido críticos para los avances logrados hasta ahora.",
            "como_se_interpreta": "Sirve para ver rápidamente cómo se comportan algunas capacidades consideradas centrales para la transición digital. Valores más altos muestran mayores avances reportados en cada componente, mientras que valores más bajos ayudan a identificar áreas prioritarias de atención.",
        },
    ],
    "seccion_ejemplo": "## Ejemplo sencillo de lectura",
    "ejemplo": [
        "Si una dimensión obtiene 60 puntos, eso significa que su resultado promedio se ubica en el nivel “En consolidación”.",
        "Si otra dimensión obtiene 30 puntos, eso indica un nivel “Emergente”, por lo que probablemente aparecerá entre las prioridades de mejora y podrá activar recomendaciones más urgentes.",
        "Si en la gráfica radar algunas dimensiones tienen valores altos y otras muy bajos, eso no significa que el territorio esté mal en todo, sino que tiene un desarrollo desigual entre temas.",
    ],
    "seccion_uso": "## ¿Cómo usar esta página?",
    "uso": [
        "Primero revisa esta sección de bienvenida para entender la lógica general del tablero.",
        "Después entra al apartado “Tablero” y carga un archivo exportado desde KoboToolbox o usa el ejemplo incluido.",
        "Finalmente, revisa el puntaje global, las dimensiones, las alertas, las recomendaciones y las gráficas para interpretar el resultado.",
    ],
}


# =========================
# Textos de gráficas
# =========================

TEXTOS_GRAFICAS = {
    "bar_dimensions_title": "Puntaje por dimensión",
    "bar_dimensions_yaxis": "Puntaje (0-100)",
    "bar_dimensions_xaxis": "",
    "radar_dimensions_title": "Radar general de madurez digital",
    "radar_key_capabilities_title": "Radar de capacidades clave",
    "radar_key_capabilities_name": "Capacidades clave",
    "radar_range_min": 0,
    "radar_range_max": 100,
}

RADAR_CAPACIDADES_CLAVE = [
    ("q2", "Estrategia"),
    ("q7", "Conectividad"),
    ("q14", "Datos"),
    ("q18", "Accesibilidad"),
    ("q22", "Continuidad"),
    ("q27", "Factores críticos"),
]


# =========================
# Configuración de dimensiones
# =========================

DIMENSIONES = {
    "A": "Visión Estratégica, Gobernanza y Acciones Gubernamentales",
    "B": "Infraestructura, Capacidades Técnicas y Plataformas",
    "C": "Gobernanza de Datos, Privacidad y Ética",
    "D": "Participación Ciudadana y Equidad Digital",
    "E": "Economía Creativa y Patrimonio",
    "F": "Financiamiento, Sostenibilidad y Alianzas",
    "G": "Obstáculos, Aprendizajes y Recomendaciones",
}

ACRONIMOS_DIMENSION = {
    "A": "VEG",
    "B": "ICTP",
    "C": "GDPE",
    "D": "PCED",
    "E": "ECP",
    "F": "FSA",
    "G": "OAR",
}

EXPLICACION_DIMENSIONES = {
    "A": {
        "nombre": "Visión Estratégica, Gobernanza y Acciones Gubernamentales",
        "acronimo": "VEG",
        "preguntas": ["q1", "q2", "q3", "q4", "q5", "q6"],
        "preguntas_etiqueta": [
            "Estrategia de transformación digital / ciudad inteligente local",
            "Situación del plan local de transformación digital",
            "Estructura institucional que gestiona la transición digital",
            "Hitos recientes en transición digital",
            "Acciones o programas actuales de la administración local",
            "Mecanismos de gobernanza y coordinación",
        ],
        "descripcion": "Evalúa la existencia de estrategia, estructura institucional, hitos, acciones y mecanismos de coordinación para impulsar la transición digital.",
    },
    "B": {
        "nombre": "Infraestructura, Capacidades Técnicas y Plataformas",
        "acronimo": "ICTP",
        "preguntas": ["q7", "q8", "q9", "q10", "q11", "q12"],
        "preguntas_etiqueta": [
            "Cobertura de servicios de internet",
            "Tipos de servicio disponibles en el municipio",
            "Plataformas digitales propias del municipio",
            "Tecnologías aplicadas en el ámbito local",
            "Método de incorporación de capital humano",
            "Percepción ciudadana sobre el trabajo en tecnología, transición digital y datos",
        ],
        "descripcion": "Evalúa conectividad, servicios tecnológicos disponibles, plataformas, capacidades técnicas y condiciones institucionales para operar lo digital.",
    },
    "C": {
        "nombre": "Gobernanza de Datos, Privacidad y Ética",
        "acronimo": "GDPE",
        "preguntas": ["q13", "q14", "q15"],
        "preguntas_etiqueta": [
            "Mecanismos o políticas para gestión y protección de datos",
            "Nivel de gestión de datos urbanos",
            "Marcos locales sobre uso ético de IA, algoritmos o automatización",
        ],
        "descripcion": "Evalúa políticas, prácticas y marcos relacionados con datos, privacidad, interoperabilidad y uso ético de tecnologías.",
    },
    "D": {
        "nombre": "Participación Ciudadana y Equidad Digital",
        "acronimo": "PCED",
        "preguntas": ["q16", "q17", "q18"],
        "preguntas_etiqueta": [
            "Mecanismos de participación digital",
            "Acciones para reducir la brecha digital",
            "Accesibilidad de los servicios digitales para grupos vulnerables",
        ],
        "descripcion": "Evalúa mecanismos de participación digital, acciones para reducir brechas y nivel de accesibilidad de los servicios digitales.",
    },
    "E": {
        "nombre": "Economía Creativa y Patrimonio",
        "acronimo": "ECP",
        "preguntas": ["q19", "q20"],
        "preguntas_etiqueta": [
            "Vinculación entre estrategia digital, economía creativa y patrimonio cultural",
            "Proyectos concretos realizados en este ámbito",
        ],
        "descripcion": "Evalúa la relación entre estrategia digital, patrimonio cultural, creatividad y acciones concretas en ese ámbito.",
    },
    "F": {
        "nombre": "Financiamiento, Sostenibilidad y Alianzas",
        "acronimo": "FSA",
        "preguntas": ["q21", "q22", "q23"],
        "preguntas_etiqueta": [
            "Fuentes de financiamiento de la transición digital",
            "Continuidad presupuestaria de los proyectos digitales",
            "Alianzas clave en el proceso de transición digital",
        ],
        "descripcion": "Evalúa fuentes de financiamiento, continuidad presupuestaria y alianzas clave para sostener iniciativas digitales.",
    },
    "G": {
        "nombre": "Obstáculos, Aprendizajes y Recomendaciones",
        "acronimo": "OAR",
        "preguntas": ["q25", "q26", "q27"],
        "preguntas_etiqueta": [
            "Principales obstáculos del proceso de transición digital",
            "Desafíos actuales para avanzar hacia una ciudad inteligente",
            "Factores críticos para los avances logrados",
        ],
        "descripcion": "Evalúa obstáculos, desafíos actuales y factores que han sido importantes para los avances logrados.",
    },
}

PREGUNTAS_DIMENSION = {
    "A": ["q1", "q2", "q3", "q4", "q5", "q6"],
    "B": ["q7", "q8", "q9", "q10", "q11", "q12"],
    "C": ["q13", "q14", "q15"],
    "D": ["q16", "q17", "q18"],
    "E": ["q19", "q20"],
    "F": ["q21", "q22", "q23"],
    "G": ["q25", "q26", "q27"],
}


# =========================
# Alias de preguntas Kobo
# =========================

PREGUNTAS_KOBO_ALIASES = {
    "pais": [
        "País",
        "Pais",
    ],
    "ciudad": [
        "Ciudad",
    ],
    "q1": [
        "¿Cuál de los siguientes apartados describe mejor la estrategia de transformación digital / ciudad inteligente local? (Seleccionar los que apliquen)",
        "¿Cuál de los siguientes apartados describe mejor la estrategia de transformación digital / ciudad inteligente local?",
    ],
    "q2": [
        "Si existe un Plan local de transformación digital, indique cuál de las siguientes opciones lo describe mejor (Seleccionar uno):",
        "Si existe un plan local de transformación digital, indique cuál de las siguientes opciones lo describe mejor (Seleccionar uno):",
    ],
    "q3": [
        "¿Cuál de los siguientes supuestos describe mejor la estructura institucional que gestiona la transición digital? (Seleccionar uno)",
        "¿Cuál de los siguientes supuestos describe mejor la estructura institucional que gestiona la transición digital?",
    ],
    "q4": [
        "¿Qué hitos relevantes se desarrollaron en el último año en materia de transición digital? (Seleccionar los que apliquen)",
        "¿Qué hitos relevantes se desarrollaron en el último año en materia de transición digital?",
    ],
    "q5": [
        "¿Con cuáles de las siguientes acciones o programas cuenta actualmente la administración local? (Seleccionar los que apliquen)",
        "¿Con cuáles de las siguientes acciones o programas cuenta actualmente la administración local?",
    ],
    "q6": [
        "¿Qué mecanismos de gobernanza y coordinación existen actualmente? (Seleccionar los que apliquen)",
        "¿Qué mecanismos de gobernanza y coordinación existen actualmente?",
    ],
    "q7_urbana": [
        "¿Cuál es la cobertura aproximada de servicios de internet en zona urbana del municipio? (Seleccionar uno)",
        "¿Cuál es la cobertura aproximada de servicios de internet en zona urbana del municipio?",
    ],
    "q7_rural": [
        "¿Cuál es la cobertura aproximada de servicios de internet en zona rural del municipio? (Seleccionar uno)",
        "¿Cuál es la cobertura aproximada de servicios de internet en zona rural del municipio?",
    ],
    "q8": [
        "¿Qué tipo de servicio está disponible en el municipio? (Seleccionar los que apliquen)",
        "¿Qué tipo de servicio está disponible en el municipio?",
    ],
    "q9": [
        "¿Con cuáles plataformas digitales propias cuenta actualmente el municipio? (Seleccionar los que apliquen)",
        "¿Con cuáles plataformas digitales propias cuenta actualmente el municipio?",
    ],
    "q10": [
        "¿Qué tecnologías se aplican o han sido aplicadas en el ámbito local? (Seleccionar los que apliquen)",
        "¿Qué tecnologías se aplican o han sido aplicadas en el ámbito local?",
    ],
    "q11": [
        "¿Cuál es el método más común para incorporar capital humano en temas de transición digital? (Seleccionar uno)",
        "¿Cuál es el método más común para incorporar capital humano en temas de transición digital?",
    ],
    "q12": [
        "¿Cómo percibe la ciudadanía el trabajo en temas de tecnología, transición digital y datos en el servicio público? (Seleccionar los que apliquen)",
        "¿Percibe la ciudadanía el trabajo en temas de tecnología, transición digital y datos en el servicio público?",
    ],
    "q13": [
        "¿Qué mecanismos o políticas existen para la gestión y protección de datos municipales?",
    ],
    "q14": [
        "¿Cómo se encuentra el nivel de gestión de datos urbanos (calidad, interoperabilidad, accesibilidad)? (Seleccionar uno)",
        "¿Cómo se encuentra el nivel de gestión de datos urbanos (calidad, interoperabilidad, accesibilidad)?",
    ],
    "q15": [
        "¿Existen marcos locales sobre uso ético de IA, algoritmos o automatización? (Seleccionar uno)",
        "¿Existen marcos locales sobre uso ético de IA, algoritmos o automatización?",
    ],
    "q16": [
        "¿Qué mecanismos de participación digital existen? (Seleccionar los que apliquen)",
        "¿Qué mecanismos de participación digital existen?",
    ],
    "q17": [
        "¿Qué acciones se realizan para reducir la brecha digital? (Seleccionar los que apliquen)",
        "¿Qué acciones se realizan para reducir la brecha digital?",
    ],
    "q18": [
        "¿Qué tan accesibles son los servicios digitales para grupos vulnerables? (Seleccionar uno)",
        "¿Qué tan accesibles son los servicios digitales para grupos vulnerables?",
    ],
    "q19": [
        "¿Cómo se vincula la estrategia digital con la economía creativa y el patrimonio cultural? (Seleccionar uno)",
        "¿Cómo se vincula la estrategia digital con la economía creativa y el patrimonio cultural?",
    ],
    "q20": [
        "¿Qué proyectos concretos se han realizado en este ámbito?",
    ],
    "q21": [
        "¿Cómo se financian las iniciativas de transición digital?",
    ],
    "q22": [
        "¿Hay continuidad presupuestaria en los proyectos digitales?",
    ],
    "q23": [
        "¿Qué alianzas han sido clave en el proceso de transición digital?",
    ],
    "q24_rank_1": ["1st choice"],
    "q24_rank_2": ["2nd choice"],
    "q24_rank_3": ["3rd choice"],
    "q24_rank_4": ["4th choice"],
    "q24_rank_5": ["5th choice"],
    "q25": [
        "¿Cuáles han sido los principales obstáculos en el proceso de transición digital?",
    ],
    "q26": [
        "¿Cuáles son los desafíos actuales para avanzar hacia una ciudad inteligente?",
    ],
    "q27": [
        "¿Qué factores han sido críticos para los avances logrados hasta ahora?",
    ],
    "extra_innovacion_gobierno": [
        "¿Qué acciones existen para promover una cultura de innovación dentro del gobierno local?  (Seleccionar los que apliquen)",
        "¿Qué acciones existen para promover una cultura de innovación dentro del gobierno local? (Seleccionar los que apliquen)",
    ],
    "extra_economia_patrimonio_municipio": [
        "En relación con la economía creativa y el patrimonio, el municipio (Seleccionar los que apliquen):",
        "En relación con la economía creativa y el patrimonio, el municipio (Seleccionar los que apliquen)",
    ],
}


# =========================
# Opciones de preguntas
# =========================

OPCIONES_MULTIPLE = {
    "q1": [
        "Existe un plan local de transformación digital.",
        "Existe una oficina / secretaría encargada de los temas de transformación digital.",
        "Existe un consejo / organismo ciudadano de transición digital.",
        "Existen proyectos, programas y/o acciones que trabajan en la transformación digital.",
        "Existen plataformas de atención ciudadana, participación ciudadana, consulta de información en un Sistema de Información Geográfica (SIG, monitoreo de acciones o proyectos en funcionamiento.",
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
        "Plan o estrategia local de transición digital.",
        "Transversalización digital del trabajo entre secretarías.",
        "Observatorio de la ciudad (datos, visualizaciones, etc.)",
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
        "Cobertura pública gratuita (parques, plazas.1, equipamientos)",
        "Otro",
    ],
    "q9": [
        "Desarrollo urbano (trámites de construcción, permisos)",
        "Servicios públicos (iluminación, limpieza.1, recolección)",
        "Trámites y pagos municipales",
        "Programas sociales y actividades municipales",
        "Seguridad",
        "Otro",
    ],
    "q10": [
        "Plataforma SIG y repositorios digitales",
        "Plataforma de trámites y atención ciudadana",
        "Sensores urbanos (tráfico, calidad del aire.1, movilidad)",
        "Sistemas de seguridad y respuesta en tiempo real",
        "Modelación y escenarios prospectivo",
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
        "Política municipal de datos abiertos",
        "Licencias de datos abiertos sobre información municipal",
        "Protocolos o normativas regionales/nacionales de datos públicos",
        "Procesos de prevención de pérdida o fuga de datos",
        "Avisos de privacidad de datos personales",
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
        "Ninguno",
    ],
    "q21": [
        "Presupuesto municipal",
        "Fondos estatales o nacionales",
        "Cooperación internacional",
        "Alianzas público-privadas",
        "Recursos propios o autogenerados",
        "No existe financiamiento específico",
    ],
    "q23": [
        "Universidades o centros de investigación",
        "Empresas del sector tecnológico",
        "Organizaciones de la sociedad civil",
        "Organismos internacionales",
        "Otros",
        "No existen alianzas relevantes",
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
    "q21": ["No existe financiamiento específico"],
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
        "No existe plan local de transformación digital": 0.0,
        "Existe un plan inicial o en formulación": 0.25,
        "Existe un plan vigente con acciones definidas": 0.5,
        "Plan actualizado periódicamente": 0.75,
        "Plan actualizado periódicamente y alineado a mecanismos de seguimiento y evaluación": 1.0,
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


# =========================
# Alertas
# =========================

PRIORIZACION_OBSTACULOS = {
    "Falta de política pública continua": "institucionalidad",
    "Carencia de presupuesto o infraestructura": "financiamiento",
    "Falta de capital humano capacitado": "capacidades",
    "Indiferencia o subestimación del tema": "liderazgo",
    "Resistencia al cambio y opacidad interna": "gobernanza",
}

ALERTAS_CONFIG = {
    "q14": {
        "threshold": 0.5,
        "message": "La gobernanza de datos muestra un nivel bajo o fragmentado. Valorar el desarrollo de una política integral de datos que incluya estándares de interoperabilidad, protección de datos personales y mecanismos de apertura progresiva.",
    },
    "q18": {
        "threshold": 0.5,
        "message": "La accesibilidad e inclusión digital requieren atención prioritaria. Se recomienda implementar estrategias de inclusión digital territorializadas, con énfasis en conectividad asequible, alfabetización digital y diseño intuitivo y accesible.",
    },
    "q22": {
        "threshold": 0.5,
        "message": "La continuidad presupuestaria es insuficiente para sostener la agenda digital. Explorar el establecimiento mecanismos de financiamiento multianual y diversificado (alianzas público-privadas, cooperación internacional, fondos urbanos, entre otros).",
    },
    "q24_top_n": 2,
    "q24_message_template": "Obstáculo priorizado detectado: {prioridad}. Traducir el obstáculo en una acción concreta dentro de una hoja de ruta con responsables, tiempos y métricas de seguimiento.",
}


# =========================
# Recomendaciones
# =========================

RECOMENDACIONES_DIMENSION = {
    "A": {
        "dimension": "Visión estratégica y gobernanza",
        "siguiente_paso": (
            "Formalizar o fortalecer una estrategia de transición digital con responsables, metas y seguimiento intersecretarial. "
            "Incorporar un enfoque de gobernanza multinivel y participación de actores locales (academia, sociedad civil), "
            "evitando modelos centralizados y fomentando un ecosistema de transición digital."
        ),
        "casos_referencia": [
            "Barcelona: plataforma Decidim como herramienta de gobernanza participativa.",
            "Medellín: creación de Ruta N como modelo de gobernanza articulado entre Alcaldía y sector privado.",
        ],
        "literatura": [
            "Gil-García, J. R., Zhang, J., & Puron-Cid, G. (2016). Conceptualizing smartness in government: An integrative and multi-dimensional view. Government Information Quarterly, 33(3), 524–534. https://doi.org/10.1016/j.giq.2016.03.002",
            "Meijer, A., & Bolívar, M. P. R. (2016). Governing the smart city: A review of the literature on smart urban governance. International Review of Administrative Sciences, 82(2), 392–408. https://doi.org/10.1177/0020852314564308",
            "ONU-Hábitat. (2022). People-centered smart cities playbook. Programa de las Naciones Unidas para los Asentamientos Humanos. https://unhabitat.org/programme/people-centered-smart-cities",
        ],
    },
    "B": {
        "dimension": "Infraestructura y capacidades técnicas",
        "siguiente_paso": (
            "Priorizar conectividad, digitalización de trámites y fortalecimiento de capacidades técnicas internas. "
            "Asegurar que la infraestructura esté alineada con las necesidades sociales de las comunidades "
            "e integrar el fortalecimiento del talento digital local."
        ),
        "casos_referencia": [
            "Mendoza: portal de datos abiertos y geoportal ciudadano.",
            "Montevideo: Montevidata (observatorio y datos abiertos), plataforma de visualización y descarga de datos oficiales sobre ambiente, movilidad, cultura y servicios urbanos.",
        ],
        "literatura": [
            "CAF. Banco de Desarrollo de América Latina. (2021). Transformación digital de los gobiernos subnacionales en América Latina. https://www.caf.com/es/conocimiento/visiones/2021/06/transformacion-digital-de-los-gobiernos-subnacionales-en-america-latina/",
            "CEPAL. Comisión Económica para América Latina y el Caribe. (2014). La economía digital para el cambio estructural y la igualdad. Naciones Unidas. https://repositorio.cepal.org/handle/11362/36766",
            "Mergel, I., Edelmann, N., & Haug, N. (2019). Defining digital transformation: Results from expert interviews. Government Information Quarterly, 36(4), 101385. https://doi.org/10.1016/j.giq.2019.06.002",
        ],
    },
    "C": {
        "dimension": "Gobernanza de datos, privacidad y ética",
        "siguiente_paso": (
            "Definir la política de gestión de datos, privacidad y lineamientos de ética digital para avanzar "
            "hacia modelos de soberanía tecnológica y control del datos de forma segura y transparente."
        ),
        "casos_referencia": [
            "Quito: procesos institucionalizados de calidad del dato, reuniones con custodios, validación formal y metas anuales.",
            "Curitiba: Ley municipal de IA (2024) para regular uso de inteligencia artificial con ética y privacidad.",
        ],
        "literatura": [
            "Janssen, M., Charalabidis, Y., & Zuiderwijk, A. (2012). Benefits, adoption barriers and myths of open data and open government. Information Systems Management, 29(4), 258–268.",
            "OCDE. Organización para la Cooperación y el Desarrollo Económicos. (2020). Marco de política de gobierno digital de la OCDE. OECD Publishing. https://www.oecd.org",
            "Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial intelligence and the public sector—Applications and challenges. International Journal of Public Administration, 42(7), 596–615. https://doi.org/10.1080/01900692.2018.1498103",
        ],
    },
    "D": {
        "dimension": "Participación ciudadana y equidad digital",
        "siguiente_paso": (
            "Ampliar mecanismos digitales de participación y accesibilidad para grupos vulnerables, "
            "integrando la participación híbrida (digital y presencial) y habilitando espacios de co-creación "
            "ciudadana en el diseño de las políticas públicas."
        ),
        "casos_referencia": [
            "Mendoza: Comité de Gobernanza de Datos y Comité Local de Inteligencia Artificial (CLIA).",
            "San Diego: Get It Done — plataforma de servicios municipales / atención ciudadana, trámites, solicitudes, mantenimiento urbano, reporte ciudadano y facilitación digital de servicios.",
        ],
        "literatura": [
            "Criado, J. I., & Gil-García, J. R. (2019). Creating public value through smart technologies and strategies: From digital services to artificial intelligence. Government Information Quarterly, 36(4), 101404. https://doi.org/10.1016/j.giq.2019.101404",
            "ONU-Hábitat. (2022). People-centered smart cities playbook. Programa de las Naciones Unidas para los Asentamientos Humanos. https://unhabitat.org/programme/people-centered-smart-cities",
            "Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial intelligence and the public sector—Applications and challenges. International Journal of Public Administration, 42(7), 596–615. https://doi.org/10.1080/01900692.2018.1498103",
        ],
    },
    "E": {
        "dimension": "Economía creativa y patrimonio",
        "siguiente_paso": (
            "Conectar cultura, patrimonio y digitalización mediante plataformas, archivos y laboratorios creativos. "
            "Impulsar la creación de ecosistemas creativos locales como motores de innovación urbana y apropiación tecnológica."
        ),
        "casos_referencia": [],
        "literatura": [
            "UNESCO. Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura. (2013). Informe sobre la economía creativa: Ampliar las vías del desarrollo local. UNESCO. https://unesdoc.unesco.org",
            "BID. Banco Interamericano de Desarrollo. (2017). La economía naranja: Una oportunidad infinita. BID. https://publications.iadb.org/publications/spanish/document/La-economia-naranja-Una-oportunidad-infinita.pdf",
            "British Council. (2021). The missing link: Creative economy and inclusive development in Latin America. British Council. https://www.britishcouncil.org",
            "Comunian, R., & Gilmore, A. (2016). Higher education and the creative economy: Creative graduates, knowledge transfer and regional impact debates. Geography Compass, 10(7), 391–402. https://doi.org/10.1111/gec3.12277",
        ],
    },
    "F": {
        "dimension": "Financiamiento y alianzas",
        "siguiente_paso": (
            "Asegurar continuidad presupuestaria y construir alianzas con academia, sector privado y cooperación. "
            "Generar una red de financiamiento e incorporar modelos experimentales de obtención de recursos para la digitalización."
        ),
        "casos_referencia": [],
        "literatura": [
            "BID. Banco Interamericano de Desarrollo. (2022). Guía de transformación digital del gobierno. https://publications.iadb.org/es/guia-de-transformacion-digital-del-gobierno",
            "KPMG. (2017). Smart cities: A roadmap for development. https://www.researchgate.net/publication/312106742_Smart_Cities_-_A_Roadmap_for_Development",
            "McKinsey Global Institute. (2018). Smart cities: Digital solutions for a more livable future. https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/smart%20cities%20digital%20solutions%20for%20a%20more%20livable%20future/mgi-smart-cities-full-report.pdf",
        ],
    },
    "G": {
        "dimension": "Obstáculos y aprendizajes",
        "siguiente_paso": (
            "Convertir obstáculos diagnosticados en una hoja de ruta priorizada con responsables y tiempos. "
            "Incorporar aprendizaje institucional continuo y evaluación adaptativa como parte del ciclo de política pública."
        ),
        "casos_referencia": [],
        "literatura": [
            "Mora, L., Bolici, R., & Deakin, M. (2017). The first two decades of smart-city research: A bibliometric analysis. Journal of Urban Technology, 24(1), 3–27. https://doi.org/10.1080/10630732.2017.1285123",
            "Matus Ruiz, Maximino, Ramírez Autrán, Rodrigo. (2016). Ciudades Inteligentes en Iberoamérica; ejemplos de iniciativas desde el sector privado, la sociedad civil, el gobierno y la academia, Fondo de Información y Documentación para la Industria (INFOTEC), Ciudad de México.",
            "Mergel, I., Edelmann, N., & Haug, N. (2019). Defining digital transformation: Results from expert interviews. Government Information Quarterly, 36(4), 101385. https://doi.org/10.1016/j.giq.2019.06.002",
        ],
    },
}

RECOMENDACIONES_CONFIG = {
    "high_priority_threshold": 50,
    "show_recommendations_below": 75,
    "priority_high_label": "Alta",
    "priority_medium_label": "Media",
    "priority_followup_label": "Seguimiento",
    "diagnostico_template": "La dimensión presenta un nivel {nivel} con puntaje de {puntaje}.",
    "fallback_dimension": "Balance general",
    "fallback_diagnostico": "El territorio muestra un perfil relativamente sólido en todas las dimensiones evaluadas.",
    "fallback_siguiente_paso": "Pasar de consolidación a monitoreo continuo con indicadores temporales, benchmarking y auditoría externa.",
    "fallback_literatura": "ISO 37122 + evaluación continua",
    "fallback_casos_referencia": [],
    "narrative_priority_label": "Complementaria",
}

RECOMENDACIONES_NARRATIVAS_EXTRAS = {
    "innovacion_gobierno_min_acciones": 2,
    "innovacion_gobierno_dimension": "Innovación institucional",
    "innovacion_gobierno_diagnostico": "Se observan pocas acciones orientadas a promover una cultura de innovación dentro del gobierno local.",
    "innovacion_gobierno_siguiente_paso": "Impulsar mecanismos internos de innovación pública, como laboratorios, formación, incentivos, pilotos y espacios de aprendizaje interáreas.",
    "innovacion_gobierno_literatura": "Innovación pública y transformación institucional",

    "economia_patrimonio_min_acciones": 2,
    "economia_patrimonio_dimension": "Economía creativa y patrimonio",
    "economia_patrimonio_diagnostico": "Se observan pocas acciones concretas del municipio para vincular digitalización, patrimonio y economía creativa.",
    "economia_patrimonio_siguiente_paso": "Fortalecer iniciativas que conecten patrimonio cultural, activación creativa, digitalización y plataformas de difusión o colaboración local.",
    "economia_patrimonio_literatura": "Cultura digital local y desarrollo territorial",
}


# =========================
# Literatura general
# =========================

LITERATURA = {
    "general": [
        {
            "titulo": "Albino, V., Berardi, U., & Dangelico, R. M. (2015)",
            "descripcion": "Smart cities: Definitions, dimensions, performance, and initiatives.",
            "fuente": "Journal of Urban Technology, 22(1), 3–21. https://doi.org/10.1080/10630732.2014.942092",
        },
        {
            "titulo": "BID. Banco Interamericano de Desarrollo. (2016)",
            "descripcion": "La ruta hacia las smart cities: Migrando de una gestión tradicional a la ciudad inteligente.",
            "fuente": "https://publications.iadb.org/publications/spanish/document/La-ruta-hacia-las-smart-cities-Migrando-de-una-gestion-tradicional-a-la-ciudad-inteligente.pdf",
        },
        {
            "titulo": "BID. Banco Interamericano de Desarrollo. (2020)",
            "descripcion": "Guía para gobiernos digitales.",
            "fuente": "BID. https://publications.iadb.org/es/guia-para-gobiernos-digitales",
        },
        {
            "titulo": "BID. Banco Interamericano de Desarrollo. (2022)",
            "descripcion": "Guía de transformación digital del gobierno.",
            "fuente": "https://publications.iadb.org/es/guia-de-transformacion-digital-del-gobierno",
        },
        {
            "titulo": "CEPAL. Comisión Económica para América Latina y el Caribe. (2014)",
            "descripcion": "La economía digital para el cambio estructural y la igualdad.",
            "fuente": "Naciones Unidas. https://repositorio.cepal.org/handle/11362/36766",
        },
        {
            "titulo": "CIPPEC. Centro de Implementación de Políticas Públicas para la Equidad y el Crecimiento. (2024)",
            "descripcion": "Transformación pública digital: La agenda municipal (Documento de Políticas Públicas No. 246).",
            "fuente": "https://www.cippec.org/wp-content/uploads/2024/07/DPP-246-EyG-Transformacion-publica-digital-la-agenda-municipal-07.24.pdf",
        },
        {
            "titulo": "Criado, J. I., & Gil-García, J. R. (2019)",
            "descripcion": "Creating public value through smart technologies and strategies: From digital services to artificial intelligence.",
            "fuente": "Government Information Quarterly, 36(4), 101404. https://doi.org/10.1016/j.giq.2019.101404",
        },
        {
            "titulo": "KPMG. (2017)",
            "descripcion": "Smart cities: A roadmap for development.",
            "fuente": "https://www.researchgate.net/publication/312106742_Smart_Cities_-_A_Roadmap_for_Development",
        },
        {
            "titulo": "McKinsey Global Institute. (2018)",
            "descripcion": "Smart cities: Digital solutions for a more livable future.",
            "fuente": "https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/smart%20cities%20digital%20solutions%20for%20a%20more%20livable%20future/mgi-smart-cities-full-report.pdf",
        },
        {
            "titulo": "Meijer, A., & Bolívar, M. P. R. (2016)",
            "descripcion": "Governing the smart city: A review of the literature on smart urban governance.",
            "fuente": "International Review of Administrative Sciences, 82(2), 392–408. https://doi.org/10.1177/0020852314564308",
        },
        {
            "titulo": "Mergel, I., Edelmann, N., & Haug, N. (2019)",
            "descripcion": "Defining digital transformation: Results from expert interviews.",
            "fuente": "Government Information Quarterly, 36(4), 101385. https://doi.org/10.1016/j.giq.2019.06.002",
        },
        {
            "titulo": "Matus Ruiz, Maximino, Ramírez Autrán, Rodrigo. (2016)",
            "descripcion": "Ciudades Inteligentes en Iberoamérica; ejemplos de iniciativas desde el sector privado, la sociedad civil, el gobierno y la academia.",
            "fuente": "Fondo de Información y Documentación para la Industria (INFOTEC), Ciudad de México.",
        },
        {
            "titulo": "ONU-Hábitat. (2022)",
            "descripcion": "People-centered smart cities playbook.",
            "fuente": "Programa de las Naciones Unidas para los Asentamientos Humanos. https://unhabitat.org/programme/people-centered-smart-cities",
        },
        {
            "titulo": "OCDE. Organización para la Cooperación y el Desarrollo Económicos. (2019)",
            "descripcion": "El camino hacia un sector público impulsado por datos.",
            "fuente": "OECD Publishing. https://doi.org/10.1787/059814a7-en",
        },
        {
            "titulo": "Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019)",
            "descripcion": "Artificial intelligence and the public sector—Applications and challenges.",
            "fuente": "International Journal of Public Administration, 42(7), 596–615. https://doi.org/10.1080/01900692.2018.1498103",
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