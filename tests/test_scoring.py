from pathlib import Path

from tablero_ciudad_inteligente.data_loader import cargar_archivo
from tablero_ciudad_inteligente.scoring import calcular_resultados, nivel_desde_puntaje, puntuar_pregunta


def test_nivel_desde_puntaje():
    assert nivel_desde_puntaje(10) == "Inicial"
    assert nivel_desde_puntaje(40) == "Emergente"
    assert nivel_desde_puntaje(60) == "En consolidación"
    assert nivel_desde_puntaje(90) == "Avanzado"


def test_puntuar_ordinal_q7():
    assert puntuar_pregunta("q7", "Total o casi total (+90%)") == 1.0
    assert puntuar_pregunta("q7", "Menos de 50%") == 0.2


def test_puntuar_multiple_q6_ninguna():
    assert puntuar_pregunta("q6", "Ninguna de las anteriores.") == 0.0


def test_puntuar_multiple_q5():
    score = puntuar_pregunta(
        "q5",
        "Plataforma digital de participación o atención ciudadana.;Transversalización digital del trabajo entre secretarías.",
    )
    assert score > 0.0


def test_cargar_export_kobo_con_labels():
    ruta = Path("/mnt/data/CIDEU_SMRT_V2_Autoevaluación_-_all_versions_-_labels_-_2026-04-14-21-02-31.csv")
    df = cargar_archivo(ruta)
    assert "q1" in df.columns
    assert "q27" in df.columns
    assert "entidad" in df.columns
    resultado = calcular_resultados(df.iloc[0])
    assert resultado.ciudad
