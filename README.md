# Tablero de autoevaluación de transición digital y ciudades inteligentes

Este proyecto implementa un dashboard en Python para visualizar el estado de desarrollo de un **territorio** frente a su transición digital y su avance hacia una ciudad o territorio inteligente.

El término territorio se usa de forma amplia: puede tratarse de una **ciudad, municipio, país, región o cualquier otra unidad subnacional o institucional** que responda el instrumento.

La app está basada en el instrumento de autoevaluación compartido por el usuario.

---

## 1. Objetivo

El tablero busca ayudar a responder una pregunta sencilla:

**¿En qué estado se encuentra un territorio en su transición hacia un modelo inteligente, digital, inclusivo y basado en datos?**

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

> `auth.py` puede conservarse como referencia para una futura autenticación, pero la versión actual de la app funciona sin exigir contraseña en el código.

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

## 6. Formato de datos soportado

La app acepta:

- `.csv`
- `.xlsx`

### Formato 1. Esquema simplificado interno

Un archivo con una fila por evaluación y columnas `q1` a `q27`.

### Formato 2. Export real de KoboToolbox

La app ya acepta directamente un export con **labels** con la estructura designada por los investigadores y por kobotoolbox, por ejemplo con columnas como:

- `¿Cuál de los siguientes supuestos describe mejor la situación de la estrategia o plan formal de ciudades inteligentes?`
- `¿Cómo se encuentra el nivel de gestión de datos urbanos (calidad, interoperabilidad, accesibilidad)?`
- `_submission_time`
- `_submitted_by`

Durante la carga, esas columnas se renombran internamente a `q1...q27` para reutilizar el motor de scoring.

### Identificación del territorio

La app intentará detectar automáticamente una columna para nombrar cada observación usando, en este orden aproximado:

- `ciudad`
- `municipio`
- `país` / `pais`
- `región` / `region`
- `territorio`
- `entidad`
- `nombre`
- `_submitted_by`

Si no encuentra una columna clara, asignará nombres automáticos como `Observación 1`, `Observación 2`, etc.

---

## 7. Seguridad de acceso

La versión actual **no trae una contraseña integrada en el código**.

Esto se hizo para que el repositorio sea más limpio, reusable y fácil de adaptar por otros equipos. Sin embargo, **sí se recomienda fuertemente** proteger el despliegue cuando la app se use con datos reales.

### Recomendación mínima

- autenticación al frente,
- HTTPS,
- secretos fuera del repositorio,
- control de acceso por usuario u organización.

Más detalle en `docs/seguridad_y_despliegue.md`.

---

## 8. KoboToolbox hoy y mañana

### Estado actual

Hoy la app está preparada para **cargar manualmente** un export descargado desde KoboToolbox.

### Ruta futura sugerida

1. El territorio responde el formulario.
2. KoboToolbox genera la observación.
3. Un proceso automático descarga la respuesta.
4. La respuesta se valida y se guarda.
5. El usuario inicia sesión.
6. El usuario visualiza solo sus resultados.

Más detalle en `docs/automatizacion_futura.md`.

---

## 9. Recomendaciones de despliegue

### Prototipo rápido

- Streamlit Community Cloud o Render para demo cerrada
- datos anonimizados
- acceso restringido por capa externa o red privada

### Entorno serio / institucional

- contenedor Docker
- Nginx o Traefik como reverse proxy
- HTTPS
- autenticación por usuario
- base de datos PostgreSQL
- secretos en variables de entorno o secret manager
- logs de acceso

---

## 10. Pruebas

```bash
poetry run pytest
```

---

## 11. Siguientes mejoras sugeridas

- autenticación por usuario y territorio,
- persistencia en base de datos,
- descarga automática desde KoboToolbox,
- historial temporal por territorio,
- benchmarking entre territorios,
- módulo de reportes PDF,
- panel de administración,
- control fino de permisos por rol.
