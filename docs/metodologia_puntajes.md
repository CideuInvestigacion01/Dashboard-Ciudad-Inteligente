# Metodología de puntajes

## 1. Propósito de esta metodología

Esta metodología se diseñó para traducir las respuestas del instrumento de autoevaluación en un conjunto de resultados fáciles de leer, comparar e interpretar.

Su función principal es ayudar a responder una pregunta central:

**¿Qué tan avanzado se encuentra un territorio en su proceso de transición digital y en su desarrollo hacia una ciudad inteligente?**

La metodología no pretende sustituir una auditoría formal, una evaluación externa o una certificación. Su propósito es más práctico y orientador. Busca:

- resumir de forma clara los resultados del cuestionario,
- mostrar fortalezas y brechas en distintas áreas,
- facilitar conversaciones entre equipos técnicos, directivos y tomadores de decisión,
- y ayudar a definir prioridades de mejora.

En otras palabras, esta metodología sirve como una herramienta de diagnóstico y apoyo para la planificación.

---

## 2. Idea general del cálculo

El cuestionario contiene distintos tipos de preguntas. Algunas tienen una sola respuesta posible y otras permiten seleccionar varias opciones.

Para poder comparar todas las respuestas dentro de una misma lógica, cada pregunta se transforma primero a una escala común de **0 a 1**.

Después de eso, el proceso sigue estos pasos:

1. se calcula el puntaje de cada pregunta,
2. se promedian las preguntas de una misma dimensión,
3. ese promedio se convierte a una escala de 0 a 100,
4. y finalmente se calcula un puntaje global como promedio simple de las dimensiones.

Esto permite que el tablero muestre resultados comparables entre áreas distintas del instrumento.

---

## 3. Escala base de 0 a 1

La escala base funciona así:

- **0** representa el nivel más bajo de avance dentro de una pregunta,
- **1** representa el nivel más alto de avance,
- y los valores intermedios representan situaciones parciales o niveles de desarrollo intermedio.

Esta escala interna no se muestra directamente al usuario final en la mayoría de los casos, pero es la base del cálculo.

---

## 4. Conversión a escala de 0 a 100

Aunque internamente el cálculo usa valores entre 0 y 1, el tablero muestra los resultados en una escala más intuitiva para lectura pública:

- un valor de `0.00` equivale a `0 puntos`,
- un valor de `0.50` equivale a `50 puntos`,
- un valor de `1.00` equivale a `100 puntos`.

Esto facilita mucho la lectura de resultados para personas no técnicas.

---

## 5. Cómo se calcula el puntaje de una pregunta

La manera de calcular una pregunta depende del tipo de respuesta.

### 5.1 Preguntas de selección única ordinal

Estas preguntas tienen opciones que representan distintos niveles de desarrollo o madurez.

Cada opción recibe un valor previamente definido.

### Ejemplo conceptual

Una pregunta sobre gobernanza de datos podría ordenarse así:

- no existe política → `0.00`
- existen repositorios básicos → `0.25`
- hay datos abiertos básicos → `0.50`
- existe interoperabilidad → `0.75`
- existe un sistema integrado → `1.00`

En este tipo de preguntas, mientras más desarrollada sea la situación descrita por la respuesta, mayor será el puntaje.

### Qué significa esto en términos simples

Estas preguntas no se puntúan por opinión, sino por posición dentro de una escala de avance previamente definida.

---

### 5.2 Preguntas de selección múltiple

En estas preguntas, el puntaje se calcula según la cantidad de opciones válidas que fueron seleccionadas.

La fórmula general es:

**número de opciones seleccionadas / número total de opciones válidas**

### Ejemplo simple

Supongamos una pregunta con 5 opciones válidas.

- Si se selecciona 1 opción, el puntaje sería `1/5 = 0.20`
- Si se seleccionan 3 opciones, el puntaje sería `3/5 = 0.60`
- Si se seleccionan 5 opciones, el puntaje sería `5/5 = 1.00`

### Excepción importante

Cuando aparece una opción como:

- `Ninguna de las anteriores`
- o una opción equivalente que niega la existencia de acciones o capacidades,

el puntaje de esa pregunta se fuerza a `0`.

Esto se hace para evitar que una respuesta contradictoria genere un resultado artificialmente alto.

---

### 5.3 Preguntas que no entran al puntaje global

No todas las preguntas se usan para calcular el score.

En la lógica actual del dashboard, la pregunta **q24** relacionada con la priorización de obstáculos:

- **no entra al puntaje global**,
- **no modifica el puntaje de una dimensión**,
- y se usa únicamente para generar alertas y hallazgos.

Esto significa que sí aporta valor interpretativo, pero no afecta directamente la calificación numérica general.

---

## 6. Cómo se calcula el puntaje por dimensión

El instrumento agrupa las preguntas en varias dimensiones temáticas.

Cada dimensión reúne preguntas que evalúan un mismo ámbito del desarrollo digital, por ejemplo:

- visión estratégica y gobernanza,
- infraestructura y capacidades técnicas,
- gobernanza de datos,
- participación y equidad digital,
- economía creativa y patrimonio,
- financiamiento y alianzas,
- obstáculos y aprendizajes.

### Regla de cálculo

Para cada dimensión:

1. se calcula el puntaje de cada pregunta que la integra,
2. se suman esos puntajes,
3. se divide entre el número de preguntas de la dimensión,
4. y el resultado se multiplica por 100.

### Ejemplo sencillo

Supongamos una dimensión con 4 preguntas y estos resultados:

- pregunta 1 = `1.00`
- pregunta 2 = `0.50`
- pregunta 3 = `0.75`
- pregunta 4 = `0.25`

Promedio interno:

`(1.00 + 0.50 + 0.75 + 0.25) / 4 = 0.625`

Puntaje final de dimensión:

`0.625 × 100 = 62.5`

Entonces, esa dimensión tendría **62.5 puntos**.

---

## 7. Cómo se calcula el puntaje global

Una vez que cada dimensión tiene su puntaje, el tablero calcula un puntaje global.

### Regla actual

El puntaje global se obtiene como el **promedio simple de todas las dimensiones**.

Eso significa que, en la lógica actual, todas las dimensiones tienen el mismo peso dentro del resultado general.

### Ejemplo sencillo

Supongamos que un territorio obtiene estos puntajes por dimensión:

- Dimensión A = 70
- Dimensión B = 55
- Dimensión C = 40
- Dimensión D = 60
- Dimensión E = 50
- Dimensión F = 65
- Dimensión G = 45

El promedio sería:

`(70 + 55 + 40 + 60 + 50 + 65 + 45) / 7 = 55`

El puntaje global sería entonces **55 puntos**.

---

## 8. Clasificación de resultados por nivel

El tablero traduce el puntaje global a un nivel de desarrollo.

### Rangos actuales

- **Inicial**: menor a 25 puntos
- **Emergente**: desde 25 y menor a 50 puntos
- **En consolidación**: desde 50 y menor a 75 puntos
- **Avanzado**: 75 puntos o más

---

## 9. Qué significa cada nivel

### Inicial
El territorio presenta capacidades muy limitadas, fragmentadas o incipientes.

Esto suele indicar que:
- faltan estructuras institucionales,
- hay poca continuidad,
- la digitalización todavía no está suficientemente organizada,
- o los avances son muy aislados.

### Emergente
El territorio ya muestra algunas acciones, programas o herramientas, pero todavía de forma parcial o poco articulada.

Esto suele indicar que:
- existen primeros avances,
- hay esfuerzos en marcha,
- pero todavía faltan coordinación, continuidad y consolidación.

### En consolidación
El territorio cuenta con bases importantes y con capacidades en funcionamiento.

Esto suele indicar que:
- ya existen estructuras o mecanismos relevantes,
- hay un grado intermedio de madurez,
- y el siguiente paso es integrar mejor, sostener y ampliar lo construido.

### Avanzado
El territorio presenta un nivel más robusto de desarrollo dentro del instrumento.

Esto suele indicar que:
- hay mayor institucionalización,
- mejores capacidades de coordinación,
- continuidad más sólida,
- y condiciones más favorables para pasar a monitoreo, mejora fina e innovación más sofisticada.

---

## 10. Qué muestran realmente los puntajes

Es importante aclarar que un puntaje no representa “éxito total” o “fracaso total”.

Más bien, el resultado muestra una **posición relativa de avance dentro del instrumento**.

Por eso, un territorio puede:

- tener un puntaje global intermedio,
- pero mostrar una dimensión muy fuerte y otra muy débil,
- o tener un resultado relativamente alto, pero todavía arrastrar brechas importantes en áreas específicas.

La utilidad del tablero está precisamente en hacer visibles esas diferencias.

---

## 11. Cómo leer los resultados de manera práctica

Una lectura útil del tablero puede seguir este orden:

### 1. Revisar el puntaje global
Ayuda a ubicar rápidamente el nivel general del territorio.

### 2. Revisar los puntajes por dimensión
Permite identificar en qué temas hay mayor avance y en cuáles hay más rezago.

### 3. Revisar alertas y hallazgos
Ayuda a detectar puntos críticos que requieren atención más inmediata.

### 4. Revisar recomendaciones
Permite traducir los resultados en acciones de mejora.

### 5. Revisar las gráficas
Ayudan a ver rápidamente patrones, contrastes y equilibrio entre dimensiones.

---

## 12. Ejemplo completo de interpretación

Supongamos el siguiente escenario:

- puntaje global = 58
- nivel global = **En consolidación**
- una dimensión obtiene 72
- otra obtiene 34
- otra obtiene 80

### Cómo se podría interpretar

- El territorio no está en una fase inicial; ya cuenta con capacidades y avances importantes.
- Sin embargo, no todas las áreas están igualmente desarrolladas.
- La dimensión con 80 puntos muestra una fortaleza clara.
- La dimensión con 34 puntos muestra una brecha importante.
- Eso significa que el siguiente paso no es empezar desde cero, sino fortalecer los temas que aún están rezagados.

Este tipo de lectura ayuda a orientar la conversación hacia prioridades concretas.

---

## 13. Límites de la metodología

Aunque esta metodología es útil para lectura rápida y comparativa, tiene límites que conviene tener presentes.

### 13.1 No sustituye una evaluación profunda
El tablero no reemplaza:
- una auditoría,
- una evaluación externa,
- una revisión normativa,
- ni un análisis institucional detallado.

### 13.2 Depende de la calidad de las respuestas
Si las respuestas del cuestionario son incompletas, inconsistentes o poco precisas, el resultado también lo será.

### 13.3 No mide todos los matices
Al convertir respuestas complejas a una escala de puntaje, siempre se simplifica parte de la realidad.

### 13.4 No implica comparación normativa entre ciudades
El instrumento no fue diseñado para construir rankings oficiales ni clasificaciones rígidas entre territorios.

Su propósito es orientar diagnóstico y mejora, no etiquetar territorios como “buenos” o “malos”.

---

## 14. Valor práctico del enfoque

A pesar de esos límites, esta metodología tiene ventajas claras:

- hace legible un instrumento amplio,
- facilita la comparación entre temas,
- ayuda a detectar brechas,
- traduce respuestas en resultados visuales,
- y permite convertir un cuestionario en una conversación estratégica.

Por eso es especialmente útil en etapas de:
- autoevaluación,
- planificación,
- priorización,
- seguimiento interno,
- y diseño de rutas de mejora.

---

## 15. Ajustes recomendados para una siguiente fase

En futuras versiones, la metodología podría fortalecerse con ajustes como:

- validar ponderaciones con especialistas temáticos,
- aplicar pesos distintos por dimensión,
- incorporar evidencia documental,
- agregar serie temporal,
- comparar resultados por tipo de ciudad o tamaño poblacional,
- y diferenciar resultados según versión del instrumento.

Estos ajustes no son obligatorios para el uso actual, pero sí pueden mejorar la robustez analítica del tablero en versiones futuras.

---

## 16. Resumen final

En términos simples, la metodología funciona así:

- cada respuesta se convierte en un valor entre 0 y 1,
- esos valores se agrupan por dimensión,
- cada dimensión se convierte a una escala de 0 a 100,
- el puntaje global es el promedio de las dimensiones,
- y el resultado final se clasifica en uno de cuatro niveles.

Este enfoque permite que el tablero ofrezca una lectura clara, rápida y explicable del estado de madurez digital de un territorio, ayudando a orientar decisiones y prioridades de mejora.
