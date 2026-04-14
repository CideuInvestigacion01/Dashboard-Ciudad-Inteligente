# Tablero de Autoevaluación de Transición Digital y Ciudades Inteligentes

Aplicación en **Python + Streamlit** para transformar respuestas de un instrumento de autoevaluación en un tablero con:

- indicadores por dimensión,
- gráficas comparativas,
- radar / spider charts,
- diagnóstico automático del nivel de madurez,
- recomendaciones prácticas,
- bibliografía sugerida,
- base técnica preparada para futura integración con **KoboToolbox**.

La estructura del instrumento parte de las dimensiones compartidas por el usuario: visión estratégica, infraestructura, gobernanza de datos, participación, economía creativa, financiamiento y obstáculos. fileciteturn0file0L1-L112

---

## 1. Objetivo

El tablero busca ayudar a una ciudad o municipio a responder una pregunta sencilla:

**¿En qué estado se encuentra su transición hacia una ciudad inteligente, digital, inclusiva y basada en datos?**

La app convierte respuestas del cuestionario en puntajes normalizados, interpreta fortalezas y brechas, y sugiere acciones de mejora.

---

## 2. Tecnologías

- Python 3.11+
- Streamlit
- Plotly
- Pandas
- Poetry

---

## 3. Estructura del proyecto

```text
.
├── .streamlit/
│   └── config.toml
├── data/
│   ├── ejemplo_respuestas.csv
│   └── esquema_columnas.csv
├── docs/
│   ├── automatizacion_futura.md
│   ├── metodologia_puntajes.md
│   └── seguridad_y_despliegue.md
├── src/
│   └── tablero_ciudad_inteligente/
│       ├── __init__.py
│       ├── app.py
│       ├── auth.py
│       ├── charts.py
│       ├── config.py
│       ├── data_loader.py
│       ├── recommendations.py
│       └── scoring.py
├── tests/
│   └── test_scoring.py
├── .env.example
├── pyproject.toml
└── README.md
```

---

## 4. Instalación

### Con Poetry

```bash
poetry install
```

### Activar entorno

```bash
poetry shell
```

---

## 5. Ejecución

```bash
poetry run streamlit run src/tablero_ciudad_inteligente/app.py
```

La aplicación abrirá una interfaz web local.

---

## 6. Formato de datos esperado

La app acepta:

- `.csv`
- `.xlsx`

El archivo debe contener una fila por ciudad o evaluación.

Por defecto, el proyecto espera columnas `q1` a `q27`, donde:

- preguntas de selección única guardan un valor de texto,
- preguntas múltiples guardan valores separados por `;`,
- preguntas de prioridad pueden guardarse como texto separado por `;` respetando el orden.

Ejemplo:

```text
ciudad,fecha,q1,q2,q3,...,q27
Ciudad Ejemplo,2026-04-14,"Existe un plan local de transformación digital.;Existe una oficina / secretaría encargada de los temas de transformación digital.","Existe un plan o estrategia formal, proyectos y acciones gestionadas por una oficina especializada.",...
```

El archivo `data/esquema_columnas.csv` documenta el esquema base.

---

## 7. Lógica de evaluación

### Dimensiones evaluadas

1. Visión estratégica, gobernanza y acciones gubernamentales
2. Infraestructura, capacidades técnicas y plataformas
3. Gobernanza de datos, privacidad y ética
4. Participación ciudadana y equidad digital
5. Economía creativa y patrimonio
6. Financiamiento, sostenibilidad y alianzas
7. Obstáculos, aprendizajes y recomendaciones

### Resultado por dimensión

Cada dimensión se transforma en un puntaje de **0 a 100**.

### Resultado global

Se calcula como promedio simple de las 7 dimensiones.

### Niveles interpretativos

- **0 a 24** → Inicial
- **25 a 49** → Emergente
- **50 a 74** → En consolidación
- **75 a 100** → Avanzado

> Esta metodología es intencionalmente transparente y editable. La idea es que el equipo pueda recalibrarla conforme valide el instrumento con expertos sectoriales.

---

## 8. Seguridad básica de acceso

La app incluye autenticación sencilla por contraseña usando variables de entorno.

Archivo `.env` sugerido:

```env
APP_PASSWORD_HASH=$2b$12$ejemplo_hash_bcrypt
```

Para generar un hash bcrypt desde Python:

```python
from passlib.context import CryptContext
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd.hash("tu_password_seguro"))
```

### ¿Por qué proteger la app?

Aunque hoy se use como autoevaluación, en una fase posterior el tablero podría mostrar:

- respuestas institucionales no públicas,
- capacidades internas de gobierno,
- vacíos de ciberseguridad,
- información sensible sobre debilidades operativas,
- metadatos de personas usuarias o responsables institucionales.

Por eso conviene desplegarlo al menos con:

- autenticación,
- HTTPS,
- control de acceso por rol,
- trazabilidad de sesiones,
- almacenamiento seguro de secretos.

Más detalle en `docs/seguridad_y_despliegue.md`.

---

## 9. KoboToolbox hoy y mañana

### Estado actual

Hoy la app está preparada para **cargar manualmente un export** descargado desde KoboToolbox.

### Ruta futura sugerida

1. Formulario respondido en KoboToolbox.
2. Export automático vía API.
3. Ingesta validada en una base de datos.
4. Asociación de resultados a una cuenta o municipio.
5. Acceso seguro al tablero con autenticación.
6. Actualización automática de indicadores y reportes.

Más detalle en `docs/automatizacion_futura.md`.

---

## 10. Recomendaciones de despliegue

### Prototipo rápido

- Streamlit Community Cloud o Render para demo cerrada
- contraseña simple
- datos anonimizados

### Entorno serio / institucional

- contenedor Docker
- Nginx o Traefik como reverse proxy
- HTTPS
- autenticación por usuario
- base de datos PostgreSQL
- secretos en variables de entorno o secret manager
- logs de acceso

---

## 11. Bibliografía base sugerida

El proyecto incorpora recomendaciones automáticas apoyadas en marcos ampliamente usados para ciudades inteligentes, gobernanza de datos y transformación digital:

- **UN-Habitat**: guías de smart cities centradas en las personas. citeturn839519search0turn839519search4
- **OECD**: smart city data governance y smart cities & inclusive growth. citeturn839519search1turn839519search9turn839519search25
- **ISO 37122**: indicadores para smart cities. citeturn839519search2turn839519search22
- **KoboToolbox API**: automatización de exportaciones y sincronización futura. citeturn839519search3turn839519search11

---

## 12. Pruebas

```bash
poetry run pytest
```

---

## 13. Siguientes mejoras sugeridas

- autenticación por usuario y municipio,
- persistencia en base de datos,
- descarga automática desde KoboToolbox,
- historial temporal por ciudad,
- benchmarking entre ciudades,
- módulo de reportes PDF,
- panel de administración,
- control fino de permisos por rol.

