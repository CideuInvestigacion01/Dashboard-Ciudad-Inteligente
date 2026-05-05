# Tablero de autoevaluación de transición digital y ciudades inteligentes

Este proyecto implementa un dashboard en Python para visualizar el estado de desarrollo de un territorio frente a su transición digital y su avance hacia un modelo de ciudad o territorio inteligente.

El tablero está diseñado para:

- cargar resultados de una autoevaluación en formato de archivo,
- transformar respuestas en puntajes comparables,
- mostrar indicadores, alertas, recomendaciones y referencias,
- y servir como base para futuras integraciones con KoboToolbox, autenticación y persistencia.

La aplicación está pensada como una base de trabajo reutilizable. Su estructura actual permite que otros equipos la extiendan sin tener que rediseñar desde cero la lógica de carga, cálculo, visualización y recomendación.

---

## 1. Objetivo general

El tablero busca responder una pregunta central:

**¿En qué estado se encuentra un territorio en su proceso de transición digital y de desarrollo hacia una ciudad inteligente?**

Para ello, la aplicación:

- convierte respuestas del instrumento en puntajes normalizados,
- organiza el análisis por dimensiones temáticas,
- muestra alertas y hallazgos,
- genera recomendaciones narrativas,
- ofrece referencias bibliográficas y casos de referencia,
- y presenta visualizaciones orientadas a facilitar la interpretación.

---

## 2. Alcance funcional actual

En su estado actual, la aplicación permite:

- cargar manualmente un archivo `.csv`, `.xlsx` o `.xls`,
- aceptar tanto un **formato interno simplificado** como un **export real de KoboToolbox**,
- identificar automáticamente el territorio a partir de `pais` y `ciudad`,
- calcular puntajes por dimensión y puntaje global,
- mostrar niveles de madurez,
- desplegar alertas automáticas,
- generar recomendaciones por dimensión,
- enriquecer recomendaciones con información narrativa adicional,
- visualizar resultados con gráficas de barras y radares,
- y descargar las recomendaciones en formato CSV.

Además, la aplicación incluye una **página de bienvenida** pensada para personas no técnicas, donde se explica:

- qué es el instrumento,
- cómo se calculan los porcentajes,
- qué significa cada nivel,
- cómo está construida cada dimensión,
- y cómo se interpretan las gráficas.

---

## 3. Tecnologías usadas

- Python 3.11+
- Streamlit
- Plotly
- Pandas
- Poetry
- OpenPyXL

---

## 4. Estructura actual del proyecto

```text
.
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
│       ├── charts.py
│       ├── config.py
│       ├── data_loader.py
│       ├── recommendations.py
│       └── scoring.py
├── tests/
│   └── test_scoring.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

### Descripción de cada archivo principal

#### `app.py`
Punto de entrada de la aplicación Streamlit.

Responsabilidades:
- define la navegación entre **Inicio** y **Tablero**,
- carga el archivo subido o el dataset de ejemplo,
- permite seleccionar una observación,
- renderiza métricas, tablas, gráficas, alertas, recomendaciones y literatura,
- y ofrece descarga de recomendaciones en CSV.

#### `config.py`
Archivo central de configuración.

Aquí se concentran:
- textos visibles de la app,
- textos de bienvenida,
- mensajes globales por nivel,
- títulos de gráficas,
- definición de dimensiones,
- acrónimos,
- explicación amigable de dimensiones,
- alias del export de Kobo,
- opciones válidas por pregunta,
- alertas,
- configuración de recomendaciones,
- referencias generales,
- y estructuras tipo `dataclass`.

Este archivo es la referencia principal para cualquier ajuste editorial o metodológico.

#### `data_loader.py`
Módulo de carga y normalización de datos.

Responsabilidades:
- leer CSV o Excel,
- detectar si el archivo ya está en formato interno o si es un export crudo de Kobo,
- mapear columnas del export de Kobo al esquema interno,
- reconstruir preguntas de selección múltiple,
- sintetizar `q7` a partir de cobertura urbana y rural,
- reconstruir `q24` desde columnas de ranking,
- construir el nombre del territorio,
- y generar etiquetas legibles para el selector de evaluaciones.

#### `scoring.py`
Lógica de cálculo de puntajes.

Responsabilidades:
- puntuar preguntas ordinales,
- puntuar preguntas múltiples,
- calcular resultados por dimensión,
- calcular puntaje global,
- extraer alertas,
- y transformar resultados a `DataFrame` para tabla y gráficas.

#### `recommendations.py`
Generación de recomendaciones automáticas.

Responsabilidades:
- generar recomendaciones por dimensión según puntaje,
- asignar prioridad alta, media o seguimiento,
- incorporar casos de referencia y literatura asociada,
- y añadir recomendaciones narrativas extra usando campos que no afectan el score.

#### `charts.py`
Construcción de gráficas con Plotly.

Responsabilidades:
- crear gráfica de barras por dimensión,
- radar general de madurez digital,
- y radar de capacidades clave.

#### `data/ejemplo_respuestas.csv`
Dataset interno de ejemplo que se usa cuando el usuario no sube archivo.

Características actuales:
- está anonimizado,
- incluye `pais` y `ciudad`,
- contiene más de una fila,
- e incluye duplicados de `País - Ciudad` para probar el comportamiento del selector con sufijos `_2`, `_3`, etc.

#### `data/esquema_columnas.csv`
Describe el formato interno esperado por el dashboard.

#### `tests/test_scoring.py`
Pruebas básicas sobre scoring y carga.

---

## 5. Instalación

### Con Poetry

```bash
poetry install
```

### Activar entorno

```bash
poetry shell
```

### Ejecutar la app

```bash
poetry run streamlit run src/tablero_ciudad_inteligente/app.py
```

La aplicación abrirá una interfaz web local.

---

## 6. Navegación dentro de la aplicación

La aplicación tiene actualmente dos vistas principales:

### Inicio
Página de bienvenida para usuarios no técnicos.

Contiene:
- descripción del instrumento,
- lógica general de cálculo,
- explicación de niveles,
- explicación de dimensiones,
- explicación de gráficas,
- y ejemplo básico de lectura.

### Tablero
Vista operativa del dashboard.

Contiene:
- carga de archivo,
- selección de evaluación,
- métricas principales,
- indicadores por dimensión,
- gráficas,
- alertas,
- recomendaciones,
- literatura sugerida,
- y descarga de recomendaciones.

---

## 7. Formatos de entrada soportados

La aplicación acepta:

- `.csv`
- `.xlsx`
- `.xls`

### Formato 1. Esquema interno simplificado

Este formato ya trae columnas normalizadas, por ejemplo:

- `pais`
- `ciudad`
- `fecha`
- `q1 ... q27`
- `q7_urbana`
- `q7_rural`
- `q24`
- `extra_innovacion_gobierno`
- `extra_economia_patrimonio_municipio`

Este formato es el que usa el archivo de ejemplo del proyecto.

### Formato 2. Export real de KoboToolbox

La aplicación también acepta un export real de Kobo con labels largos, incluyendo:

- preguntas principales,
- subcolumnas de selección múltiple,
- columnas de ranking (`1st choice`, `2nd choice`, etc.),
- campos de país y ciudad,
- y metadatos de envío.

Durante la carga:
- el loader detecta aliases definidos en `config.py`,
- reconstruye preguntas múltiples a partir de subcolumnas binarias,
- sintetiza `q7`,
- reconstruye `q24`,
- y normaliza la observación al esquema interno del dashboard.

---

## 8. Lógica de detección del formato de archivo

`data_loader.py` distingue dos casos:

### A. Archivo ya normalizado al formato interno
Si detecta suficientes columnas `q1...q27`, lo considera un archivo interno y:
- no remapea preguntas,
- no reconstruye selección múltiple,
- y solo completa columnas base si faltan.

### B. Export crudo de Kobo
Si no detecta el formato interno:
- busca columnas usando aliases definidos en `config.py`,
- reconstruye preguntas múltiples,
- sintetiza preguntas especiales,
- y genera el formato interno que usa el resto de la app.

Esta distinción es importante porque evita “romper” el dataset de ejemplo al volver a procesarlo como si fuera un export crudo.

---

## 9. Identificación del territorio

La app usa actualmente `pais` y `ciudad` como forma principal de construir la identidad del territorio.

### Regla actual
- si existen `pais` y `ciudad` → se muestra `País - Ciudad`
- si falta uno de los dos → usa el valor disponible
- si no existen → usa una columna fallback (`entidad`, `nombre`, `_submitted_by`, etc.)
- si tampoco existe fallback → asigna `Observación n`

### Selector de evaluaciones
El selector lateral muestra cada observación con una etiqueta legible.

Si hay observaciones repetidas con el mismo nombre base:
- `País A - Ciudad A`
- `País A - Ciudad A_2`
- `País A - Ciudad A_3`

Esto es útil para probar respuestas múltiples de un mismo territorio o distintas mediciones temporales.

---

## 10. Estructura del cálculo

### Escala base
Cada pregunta se transforma a una escala entre `0` y `1`.

### Cálculo por dimensión
Para cada dimensión:
1. se calculan los puntajes de las preguntas que la integran,
2. se promedian esos puntajes,
3. el promedio se multiplica por 100.

### Cálculo global
El puntaje global se obtiene como el promedio simple de todas las dimensiones.

---

## 11. Dimensiones del tablero

Las dimensiones actuales son:

### A. Visión Estratégica, Gobernanza y Acciones Gubernamentales (VEG)
Preguntas:
- q1
- q2
- q3
- q4
- q5
- q6

### B. Infraestructura, Capacidades Técnicas y Plataformas (ICTP)
Preguntas:
- q7
- q8
- q9
- q10
- q11
- q12

### C. Gobernanza de Datos, Privacidad y Ética (GDPE)
Preguntas:
- q13
- q14
- q15

### D. Participación Ciudadana y Equidad Digital (PCED)
Preguntas:
- q16
- q17
- q18

### E. Economía Creativa y Patrimonio (ECP)
Preguntas:
- q19
- q20

### F. Financiamiento, Sostenibilidad y Alianzas (FSA)
Preguntas:
- q21
- q22
- q23

### G. Obstáculos, Aprendizajes y Recomendaciones (OAR)
Preguntas:
- q25
- q26
- q27

### Nota importante sobre `q24`
La pregunta `q24`:
- **no entra al score global**,
- **no entra al score de dimensión**,
- y actualmente se usa únicamente para alertas y hallazgos.

---

## 12. Niveles de resultado global

El tablero clasifica el puntaje global de esta forma:

- **Inicial**: menor a 25
- **Emergente**: desde 25 y menor a 50
- **En consolidación**: desde 50 y menor a 75
- **Avanzado**: 75 o más

Los textos asociados a cada nivel están centralizados en `config.py`.

---

## 13. Alertas automáticas

Actualmente existen alertas automáticas para:

### Gobernanza de datos
Se activa cuando el resultado de `q14` es menor a `0.5`.

### Accesibilidad e inclusión digital
Se activa cuando el resultado de `q18` es menor a `0.5`.

### Continuidad presupuestaria
Se activa cuando el resultado de `q22` es menor a `0.5`.

### Obstáculos priorizados
A partir de `q24`, se toman las primeras prioridades registradas y se muestran como hallazgos.

La lógica y los textos de alertas están en `ALERTAS_CONFIG` dentro de `config.py`.

---

## 14. Recomendaciones

La app genera recomendaciones a partir de dos fuentes distintas.

### A. Recomendaciones por puntaje de dimensión
Se generan según el puntaje de cada dimensión.

Regla actual:
- **Alta** si la dimensión tiene puntaje menor a 50
- **Media** si la dimensión tiene puntaje desde 50 y menor a 75
- sin recomendación específica si la dimensión tiene 75 o más

Si todas las dimensiones tienen 75 o más, se genera una recomendación general de seguimiento.

Cada recomendación puede incluir:
- prioridad,
- dimensión,
- diagnóstico,
- siguiente paso,
- casos de referencia,
- literatura asociada.

### B. Recomendaciones narrativas extra
No modifican el score, pero enriquecen la salida narrativa.

Actualmente se alimentan de:
- `extra_innovacion_gobierno`
- `extra_economia_patrimonio_municipio`

Estas preguntas no se usan para puntuar, pero sí sirven para añadir recomendaciones complementarias cuando se detectan vacíos.

---

## 15. Estructura interna de una recomendación

`recommendations.py` construye recomendaciones como diccionarios con esta estructura:

```python
{
    "prioridad": "...",
    "dimension": "...",
    "diagnostico": "...",
    "siguiente_paso": "...",
    "casos_referencia": [...],
    "literatura": [...],
}
```

Esto implica que:
- `casos_referencia` se maneja como lista,
- `literatura` se maneja como lista,
- y `app.py` debe iterar ambas para mostrarlas correctamente.

---

## 16. Gráficas incluidas

### A. Puntaje por dimensión
- usa el puntaje final de cada dimensión
- en el eje X usa el acrónimo de cada dimensión
- en la tabla previa, la dimensión aparece como `Nombre completo (ACRÓNIMO)`

### B. Radar general de madurez digital
- usa los mismos puntajes por dimensión
- muestra los acrónimos de dimensión en formato radial

### C. Radar de capacidades clave
No usa todas las preguntas del instrumento. Usa seis componentes clave:
- estrategia o plan local de transformación digital
- conectividad
- gestión de datos urbanos
- accesibilidad de servicios digitales
- continuidad presupuestaria
- factores críticos de avance

Estas gráficas se construyen en `charts.py`.

---

## 17. Página de bienvenida

La página de bienvenida está diseñada para usuarios no técnicos.

Se alimenta desde:
- `BIENVENIDA_CONFIG`
- `EXPLICACION_DIMENSIONES`

Todo el contenido editorial de la bienvenida está centralizado en `config.py`.

Esto facilita que un equipo externo:
- cambie redacción,
- ajuste explicaciones,
- añada contexto metodológico,
- o adapte el lenguaje a otro público,
sin tocar lógica de negocio.

---

## 18. Archivos de ejemplo y datos

### `data/ejemplo_respuestas.csv`
Archivo de ejemplo por defecto usado por el dashboard cuando no se sube archivo.

Características:
- anonimizado,
- con `pais` y `ciudad`,
- con más de una observación,
- incluye duplicados para probar el selector.

### `data/esquema_columnas.csv`
Describe el formato interno de columnas esperado por el dashboard.

---

## 19. Qué está centralizado en `config.py`

Actualmente `config.py` concentra:

- textos generales de la app,
- textos de la página de bienvenida,
- mensajes globales por nivel,
- títulos de gráficas,
- acrónimos de dimensiones,
- explicaciones de dimensiones,
- aliases de Kobo,
- opciones válidas de preguntas,
- configuración de alertas,
- configuración de recomendaciones,
- referencias generales,
- y estructuras de datos base.

Esto permite modificar gran parte del comportamiento editorial y metodológico sin tocar código operativo.

---

## 20. Qué partes son más sensibles al cambiar el instrumento

Si cambia el cuestionario, las zonas más sensibles del código son:

### `config.py`
- aliases del export Kobo,
- opciones válidas,
- preguntas por dimensión,
- explicaciones,
- alertas,
- recomendaciones,
- literatura.

### `data_loader.py`
- lógica de parsing de preguntas múltiples,
- síntesis de preguntas especiales,
- reconocimiento de columnas nuevas,
- y compatibilidad entre formato interno y export crudo.

### `scoring.py`
- reglas de puntuación ordinal,
- reglas de puntuación múltiple,
- dimensiones y agregación.

### `recommendations.py`
- estructura de salida de recomendaciones,
- y uso narrativo de preguntas no incluidas en el score.

---

## 21. Seguridad y autenticación

La versión actual no incluye autenticación en el código base.

Eso fue una decisión deliberada para:
- simplificar el repositorio,
- facilitar reutilización,
- y evitar acoplar la app a una credencial fija.

Sin embargo, para despliegues reales se recomienda:

- autenticación al frente o en una capa dedicada,
- HTTPS,
- control de acceso por usuario u organización,
- secretos fuera del repositorio,
- y separación entre entornos.

Más detalle en `docs/seguridad_y_despliegue.md`.

---

## 22. Estado actual de KoboToolbox

### Hoy
La app funciona con carga manual de archivos exportados desde KoboToolbox.

### Futuro recomendado
1. El territorio responde el instrumento.
2. Kobo genera la respuesta.
3. Un proceso automático descarga y valida la información.
4. Los datos se guardan en base de datos.
5. El usuario inicia sesión.
6. El usuario ve solo sus resultados.

Más detalle en `docs/automatizacion_futura.md`.

---

## 23. Pruebas

Ejecutar pruebas:

```bash
poetry run pytest
```

Recomendación mínima para el equipo externo:
- ampliar `tests/test_scoring.py`
- incorporar pruebas del loader con:
  - archivo interno,
  - export crudo Kobo,
  - casos con duplicados,
  - y casos con columnas faltantes

---

## 24. Recomendaciones para el equipo externo de desarrollo

### A. No editar textos directamente en lógica de app si no es necesario
Antes de cambiar algo en:
- `app.py`
- `charts.py`
- `recommendations.py`

revisar si puede resolverse desde `config.py`.

### B. Mantener separación entre:
- carga de datos,
- scoring,
- recomendaciones,
- visualización,
- y contenido editorial.

### C. Si cambia el instrumento:
1. actualizar aliases en `config.py`,
2. revisar parsing en `data_loader.py`,
3. revisar opciones válidas,
4. validar scoring,
5. actualizar ejemplos y tests.

### D. Si cambian las recomendaciones:
- revisar `RECOMENDACIONES_DIMENSION`
- revisar `RECOMENDACIONES_CONFIG`
- revisar `RECOMENDACIONES_NARRATIVAS_EXTRAS`
- y validar cómo se despliegan en `app.py`

### E. Si cambian las gráficas:
- revisar `charts.py`
- revisar `TEXTOS_GRAFICAS`
- y validar que la estructura del dataframe de salida siga siendo compatible

---

## 25. Despliegue sugerido

### Prototipo rápido
- Streamlit Community Cloud o Render
- datos anonimizados
- acceso controlado externamente

### Entorno más robusto
- Docker
- reverse proxy
- HTTPS
- autenticación externa o dedicada
- PostgreSQL
- gestión de secretos
- monitoreo
- logs

---

## 26. Siguientes mejoras sugeridas

- autenticación por usuario y territorio,
- persistencia en base de datos,
- descarga automática desde KoboToolbox,
- historial temporal por territorio,
- benchmarking entre territorios,
- generación de reportes PDF,
- panel de administración,
- control fino de permisos por rol,
- trazabilidad de versiones del cuestionario,
- pruebas automáticas del loader ante cambios de export Kobo.

---

## 27. Observación final para mantenimiento

Este proyecto ya no es solo una demo visual. En su estado actual tiene varias capas de lógica:

- contenido editorial,
- parsing de datos,
- normalización,
- scoring,
- recomendaciones,
- narrativa adicional,
- y visualización.

Por eso, cualquier cambio en el instrumento o en la salida esperada debe revisarse de forma integral y no solo en la pantalla.

La referencia principal para entender el sistema es:

1. `config.py`
2. `data_loader.py`
3. `scoring.py`
4. `recommendations.py`
5. `app.py`
