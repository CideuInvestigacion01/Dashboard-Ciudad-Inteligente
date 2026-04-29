"""Carga, detección de formato y normalización de datos de entrada."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pandas as pd

from tablero_ciudad_inteligente.config import PREGUNTAS_KOBO_ALIASES


Q7_ORDEN = {
    "Menos de 50%": 0,
    "Entre 50% y 70%": 1,
    "Entre 70% y 90%": 2,
    "Total o casi total (+90%)": 3,
}


COLUMNAS_FECHA = ["fecha", "submission_time", "_submission_time", "start", "end"]
COLUMNAS_IDENTIDAD_FALLBACK = [
    "territorio",
    "entidad",
    "nombre",
    "nombre del territorio",
    "region",
    "región",
    "region_name",
    "territory_name",
    "_submitted_by",
]


def _leer_csv(path: Path) -> pd.DataFrame:
    """Lee CSV detectando el separador más probable."""
    muestra = path.read_text(encoding="utf-8-sig", errors="ignore")[:10000]
    try:
        dialect = csv.Sniffer().sniff(muestra, delimiters=";,|\t")
        sep = dialect.delimiter
    except csv.Error:
        sep = ";"
    return pd.read_csv(path, sep=sep, quotechar='"')


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


def _a_texto(valor: object) -> str:
    if pd.isna(valor):
        return ""
    return str(valor).strip()


def _es_verdadero(valor: object) -> bool:
    if pd.isna(valor):
        return False
    texto = str(valor).strip().lower()
    return texto in {"1", "true", "yes", "sí", "si", "x"}


def _buscar_columna(df: pd.DataFrame, candidatas: list[str]) -> str | None:
    columnas_normalizadas = {_normalizar_texto(col): col for col in df.columns}
    for candidata in candidatas:
        real = columnas_normalizadas.get(_normalizar_texto(candidata))
        if real:
            return real
    return None


def _buscar_columna_alias(df: pd.DataFrame, alias_key: str) -> str | None:
    return _buscar_columna(df, PREGUNTAS_KOBO_ALIASES.get(alias_key, []))


def _buscar_subcolumnas_opciones(df: pd.DataFrame, alias_key: str) -> list[str]:
    principales = PREGUNTAS_KOBO_ALIASES.get(alias_key, [])
    columnas = []

    for col in df.columns:
        col_norm = _normalizar_texto(col)
        for principal in principales:
            principal_norm = _normalizar_texto(principal)
            if col_norm.startswith(principal_norm + "/"):
                columnas.append(col)
                break

    return columnas


def _extraer_respuesta_unica(df: pd.DataFrame, alias_key: str) -> pd.Series:
    col = _buscar_columna_alias(df, alias_key)
    if col:
        return df[col].apply(_a_texto)
    return pd.Series([""] * len(df), index=df.index)


def _extraer_respuesta_multiple(df: pd.DataFrame, alias_key: str) -> pd.Series:
    opcion_cols = _buscar_subcolumnas_opciones(df, alias_key)

    if opcion_cols:
        valores = []
        for _, fila in df[opcion_cols].iterrows():
            seleccionadas = []
            for col in opcion_cols:
                if _es_verdadero(fila[col]):
                    seleccionadas.append(col.split("/", 1)[1].strip())
            valores.append(";".join(seleccionadas))
        return pd.Series(valores, index=df.index)

    col = _buscar_columna_alias(df, alias_key)
    if col:
        return df[col].apply(_a_texto)

    return pd.Series([""] * len(df), index=df.index)


def _sintetizar_q7(df: pd.DataFrame) -> tuple[pd.Series, pd.Series, pd.Series]:
    urbana = _extraer_respuesta_unica(df, "q7_urbana")
    rural = _extraer_respuesta_unica(df, "q7_rural")

    sintetica = []
    for u, r in zip(urbana, rural):
        if u and r:
            valor = u if Q7_ORDEN.get(u, 99) <= Q7_ORDEN.get(r, 99) else r
            sintetica.append(valor)
        elif u:
            sintetica.append(u)
        elif r:
            sintetica.append(r)
        else:
            sintetica.append("")

    return pd.Series(sintetica, index=df.index), urbana, rural


def _sintetizar_q24(df: pd.DataFrame) -> pd.Series:
    rank_cols = [
        _buscar_columna_alias(df, "q24_rank_1"),
        _buscar_columna_alias(df, "q24_rank_2"),
        _buscar_columna_alias(df, "q24_rank_3"),
        _buscar_columna_alias(df, "q24_rank_4"),
        _buscar_columna_alias(df, "q24_rank_5"),
    ]

    valores = []
    for _, fila in df.iterrows():
        prioridades = []
        for col in rank_cols:
            if col:
                texto = _a_texto(fila[col])
                if texto:
                    prioridades.append(texto)
        valores.append(";".join(prioridades))

    return pd.Series(valores, index=df.index)


def _construir_nombre_territorio(pais: str, ciudad: str, fallback: str) -> str:
    pais = _a_texto(pais)
    ciudad = _a_texto(ciudad)
    fallback = _a_texto(fallback)

    if pais and ciudad:
        return f"{pais} - {ciudad}"
    if ciudad:
        return ciudad
    if pais:
        return pais
    if fallback:
        return fallback
    return "Observación sin nombre"


def _agregar_columnas_base(df: pd.DataFrame) -> pd.DataFrame:
    nuevo = df.copy()

    if "pais" in nuevo.columns:
        nuevo["pais"] = nuevo["pais"].apply(_a_texto)
    else:
        col_pais = _buscar_columna_alias(nuevo, "pais")
        nuevo["pais"] = nuevo[col_pais].apply(_a_texto) if col_pais else ""

    if "ciudad" in nuevo.columns:
        nuevo["ciudad"] = nuevo["ciudad"].apply(_a_texto)
    else:
        col_ciudad = _buscar_columna_alias(nuevo, "ciudad")
        nuevo["ciudad"] = nuevo[col_ciudad].apply(_a_texto) if col_ciudad else ""

    if "entidad" in nuevo.columns:
        fallback_series = nuevo["entidad"].apply(_a_texto)
    else:
        col_fallback = _buscar_columna(nuevo, COLUMNAS_IDENTIDAD_FALLBACK)
        if col_fallback:
            fallback_series = nuevo[col_fallback].apply(_a_texto)
        else:
            fallback_series = pd.Series([""] * len(nuevo), index=nuevo.index)

    nuevo["entidad"] = [
        _construir_nombre_territorio(
            pais=nuevo.at[idx, "pais"],
            ciudad=nuevo.at[idx, "ciudad"],
            fallback=fallback_series.at[idx],
        )
        for idx in nuevo.index
    ]

    if "fecha" in nuevo.columns:
        nuevo["fecha"] = nuevo["fecha"].apply(_a_texto)
    else:
        col_fecha = _buscar_columna(nuevo, COLUMNAS_FECHA)
        if col_fecha:
            nuevo["fecha"] = nuevo[col_fecha].apply(_a_texto)
        else:
            nuevo["fecha"] = "Sin fecha"

    return nuevo


def _es_formato_interno(df: pd.DataFrame) -> bool:
    columnas_q = [f"q{i}" for i in range(1, 28)]
    presentes = sum(1 for col in columnas_q if col in df.columns)
    return presentes >= 20


def _normalizar_formato_interno(df: pd.DataFrame) -> pd.DataFrame:
    """Mantiene intacto el formato interno del dashboard y completa columnas base."""
    nuevo = df.copy()

    for col in ["pais", "ciudad", "fecha", "q7", "q7_urbana", "q7_rural", "q24",
                "extra_innovacion_gobierno", "extra_economia_patrimonio_municipio"]:
        if col in nuevo.columns:
            nuevo[col] = nuevo[col].apply(_a_texto)

    return _agregar_columnas_base(nuevo)


def _mapear_respuestas(df: pd.DataFrame) -> pd.DataFrame:
    nuevo = df.copy()

    multiples = ["q1", "q4", "q5", "q6", "q8", "q9", "q10", "q12", "q13", "q16", "q17", "q20", "q21", "q23", "q25", "q26", "q27"]
    unicas = ["q2", "q3", "q11", "q14", "q15", "q18", "q19", "q22"]

    for q in multiples:
        nuevo[q] = _extraer_respuesta_multiple(nuevo, q)

    for q in unicas:
        nuevo[q] = _extraer_respuesta_unica(nuevo, q)

    nuevo["q7"], nuevo["q7_urbana"], nuevo["q7_rural"] = _sintetizar_q7(nuevo)
    nuevo["q24"] = _sintetizar_q24(nuevo)

    # Extras narrativos, no usados en scoring
    nuevo["extra_innovacion_gobierno"] = _extraer_respuesta_multiple(nuevo, "extra_innovacion_gobierno")
    nuevo["extra_economia_patrimonio_municipio"] = _extraer_respuesta_multiple(nuevo, "extra_economia_patrimonio_municipio")

    return nuevo


def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza columnas y adapta formatos conocidos del instrumento."""
    nuevo = df.copy()

    if _es_formato_interno(nuevo):
        return _normalizar_formato_interno(nuevo)

    nuevo = _agregar_columnas_base(nuevo)
    nuevo = _mapear_respuestas(nuevo)
    return nuevo


def construir_etiquetas_evaluacion(df: pd.DataFrame) -> list[str]:
    """Construye etiquetas legibles para el selector usando país y ciudad.

    Si se repite el mismo nombre base, agrega sufijos _2, _3, etc.
    """
    if df.empty:
        return []

    base_labels = []
    for _, fila in df.iterrows():
        pais = _a_texto(fila.get("pais", ""))
        ciudad = _a_texto(fila.get("ciudad", ""))
        entidad = _a_texto(fila.get("entidad", ""))

        if pais and ciudad:
            base = f"{pais} - {ciudad}"
        elif entidad:
            base = entidad
        elif ciudad:
            base = ciudad
        elif pais:
            base = pais
        else:
            base = "Observación sin nombre"

        base_labels.append(base)

    conteos: dict[str, int] = {}
    etiquetas: list[str] = []

    for base in base_labels:
        conteos[base] = conteos.get(base, 0) + 1
        n = conteos[base]
        etiquetas.append(base if n == 1 else f"{base}_{n}")

    return etiquetas


def seleccionar_fila(df: pd.DataFrame, indice: int) -> pd.Series:
    """Devuelve la fila seleccionada por índice."""
    if df.empty:
        raise ValueError("El archivo cargado no contiene filas.")
    if indice < 0 or indice >= len(df):
        raise IndexError("Índice fuera de rango.")
    return df.iloc[indice]