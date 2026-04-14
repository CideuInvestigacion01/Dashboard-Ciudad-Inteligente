"""Carga y normalización de datos de entrada."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def cargar_archivo(path: str | Path) -> pd.DataFrame:
    """Carga un CSV o XLSX y devuelve un DataFrame."""
    path = Path(path)
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    else:
        raise ValueError("Formato no soportado. Usa CSV o XLSX.")

    return normalizar_columnas(df)


def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nombres de columnas a minúsculas y elimina espacios laterales."""
    nuevo = df.copy()
    nuevo.columns = [str(col).strip().lower() for col in nuevo.columns]
    return nuevo


def seleccionar_fila(df: pd.DataFrame, indice: int) -> pd.Series:
    """Devuelve la fila seleccionada por índice."""
    if df.empty:
        raise ValueError("El archivo cargado no contiene filas.")
    if indice < 0 or indice >= len(df):
        raise IndexError("Índice fuera de rango.")
    return df.iloc[indice]
