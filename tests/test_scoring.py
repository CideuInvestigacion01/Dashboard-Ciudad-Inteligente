from tablero_ciudad_inteligente.scoring import nivel_desde_puntaje, puntuar_pregunta


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
