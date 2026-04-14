"""Carga, detección de formato y normalización de datos de entrada."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pandas as pd


PREGUNTAS_KOBO = {
    "q1": "¿Cuál de los siguientes apartados describe mejor la estrategia de transformación digital / ciudad inteligente local?",
    "q2": "¿Cuál de los siguientes supuestos describe mejor la situación de la estrategia o plan formal de ciudades inteligentes?",
    "q3": "¿Cuál de los siguientes supuestos describe mejor la estructura institucional que gestiona la transición digital?",
    "q4": "¿Qué hitos relevantes se desarrollaron en el último año en materia de transición digital?",
    "q5": "¿Con cuáles de las siguientes acciones o programas cuenta actualmente la administración local?",
    "q6": "¿Qué mecanismos de gobernanza y coordinación existen actualmente?",
    "q7": "¿Cuál es la cobertura aproximada de servicios de internet en zona urbana y rural del municipio?",
    "q8": "¿Qué tipo de servicio está disponible en el municipio?",
    "q9": "¿Con cuáles plataformas digitales propias cuenta actualmente el municipio?",
    "q10": "¿Qué tecnologías se aplican o han sido aplicadas en el ámbito local?",
    "q11": "¿Cuál es el método más común para incorporar capital humano en temas de transición digital?",
    "q12": "¿Percibe la ciudadanía el trabajo en temas de tecnología, transición digital y datos en el servicio público?",
    "q13": "¿Qué mecanismos o políticas existen para la gestión y protección de datos municipales?",
    "q14": "¿Cómo se encuentra el nivel de gestión de datos urbanos (calidad, interoperabilidad, accesibilidad)?",
    "q15": "¿Existen marcos locales sobre uso ético de IA, algoritmos o automatización?",
    "q16": "¿Qué mecanismos de participación digital existen?",
    "q17": "¿Qué acciones se realizan para reducir la brecha digital?",
    "q18": "¿Qué tan accesibles son los servicios digitales para grupos vulnerables?",
    "q19": "¿Cómo se vincula la estrategia digital con la economía creativa y el patrimonio cultural?",
    "q20": "¿Qué proyectos concretos se han realizado en este ámbito?",
    "q21": "¿Cómo se financian las iniciativas de transición digital?",
    "q22": "¿Hay continuidad presupuestaria en los proyectos digitales?",
    "q23": "¿Qué alianzas han sido clave en el proceso de transición digital?",
    "q24": "¿Cuál es el principal impedimento para la continuidad de las políticas de transición digital?",
    "q25": "¿Cuáles han sido los principales obstáculos en el proceso de transición digital?",
    "q26": "¿Cuáles son los desafíos actuales para avanzar hacia una ciudad inteligente?",
    "q27": "¿Qué factores han sido críticos para los avances logrados hasta ahora?",
}

COLUMNAS_IDENTIDAD = [
    "ciudad",
    "municipio",
    "país",
    "pais",
    "región",
    "region",
    "territorio",
    "entidad",
    "nombre",
    "nombre del territorio",
    "nombre de la ciudad",
    "nombre del municipio",
    "country",
    "region_name",
    "territory_name",
    "_submitted_by",
]

COLUMNAS_FECHA = ["fecha", "submission_time", "_submission_time", "start", "end"]


def _leer_csv(path: Path) -> pd.DataFrame:
    """Lee CSV detectando automáticamente el separador más probable."""
    muestra = path.read_text(encoding="utf-8-sig", errors="ignore")[:5000]
    try:
        dialect = csv.Sniffer().sniff(muestra, delimiters=",;\t|")
        sep = dialect.delimiter
    except csv.Error:
        sep = ";" if muestra.count(";") > muestra.count(",") else ","
    return pd.read_csv(path, sep=sep)


def cargar_archivo(path: str | Path) -> pd.DataFrame:
    """Carga un CSV o XLSX y devuelve un DataFrame normalizado."""
    path = Path(path)
    if path.suffix.lower() == ".csv":
        df = _leer_csv(path)
    elif path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    else:
        raise ValueError("Formato no soportado. Usa CSV o XLSX.")

    return normalizar_columnas(df)


def _normalizar_texto(texto: str) -> str:
    texto = str(texto).strip().lower()
    texto = re.sub(r"\s+", " ", texto)
    return texto


def _renombrar_desde_kobo(nuevo: pd.DataFrame) -> pd.DataFrame:
    """Renombra columnas del export de Kobo con labels a q1..q27 si aplica."""
    mapeo: dict[str, str] = {}
    columnas_normalizadas = {_normalizar_texto(col): col for col in nuevo.columns}

    for codigo, pregunta in PREGUNTAS_KOBO.items():
        clave = _normalizar_texto(pregunta)
        columna_real = columnas_normalizadas.get(clave)
        if columna_real:
            mapeo[columna_real] = codigo

    if mapeo:
        nuevo = nuevo.rename(columns=mapeo)
    return nuevo


def _buscar_columna(df: pd.DataFrame, candidatas: list[str]) -> str | None:
    columnas_normalizadas = {_normalizar_texto(col): col for col in df.columns}
    for candidata in candidatas:
        real = columnas_normalizadas.get(_normalizar_texto(candidata))
        if real:
            return real
    return None


def _agregar_columnas_base(df: pd.DataFrame) -> pd.DataFrame:
    """Asegura columnas base para identificar territorio y fecha."""
    nuevo = df.copy()

    if "entidad" not in nuevo.columns:
        col_entidad = _buscar_columna(nuevo, COLUMNAS_IDENTIDAD)
        if col_entidad:
            nuevo["entidad"] = nuevo[col_entidad].fillna("Observación sin nombre").astype(str)
        else:
            nuevo["entidad"] = [f"Observación {i + 1}" for i in range(len(nuevo))]

    if "fecha" not in nuevo.columns:
        col_fecha = _buscar_columna(nuevo, COLUMNAS_FECHA)
        if col_fecha:
            nuevo["fecha"] = nuevo[col_fecha].astype(str)
        else:
            nuevo["fecha"] = "Sin fecha"

    return nuevo


def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza columnas y adapta formatos conocidos del instrumento."""
    nuevo = df.copy()
    nuevo.columns = [str(col).strip().lower() for col in nuevo.columns]
    nuevo = _renombrar_desde_kobo(nuevo)
    nuevo = _agregar_columnas_base(nuevo)
    return nuevo


def seleccionar_fila(df: pd.DataFrame, indice: int) -> pd.Series:
    """Devuelve la fila seleccionada por índice."""
    if df.empty:
        raise ValueError("El archivo cargado no contiene filas.")
    if indice < 0 or indice >= len(df):
        raise IndexError("Índice fuera de rango.")
    return df.iloc[indice]
