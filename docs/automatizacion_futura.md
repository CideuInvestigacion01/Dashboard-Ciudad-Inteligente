# Automatización futura e integración con KoboToolbox

## 1. Propósito de este documento

Este documento describe posibles rutas de evolución para el tablero, desde el flujo más simple y de bajo costo operativo hasta una solución completamente automatizada con cuentas de usuario, integración con KoboToolbox y visualización personalizada de resultados.

La intención no es fijar una única arquitectura obligatoria, sino dejar claras las opciones posibles para que el equipo responsable pueda decidir según:

- presupuesto,
- capacidad técnica,
- urgencia de implementación,
- volumen de usuarios,
- sensibilidad de los datos,
- y nivel de autonomía que se quiera dar a cada ciudad u organización.

**Objetivo principal de acceso y visualización:** la solución debe evolucionar hacia un modelo en el que **cada ciudad solo pueda ver su propia información**. La posibilidad de visualizar información de múltiples ciudades en un solo dashboard puede existir como una función de uso interno o administrativo, pero **no se recomienda como modalidad general de operación**, ya que puede exponer información sensible de una ciudad ante otras ciudades.

---

## 2. Situación actual

Hoy la aplicación funciona con un esquema de **carga manual de archivos**.

Esto significa que:

1. una persona descarga un archivo exportado desde KoboToolbox,
2. ese archivo se carga manualmente en el dashboard,
3. el dashboard procesa las respuestas,
4. y muestra indicadores, gráficas, alertas y recomendaciones.

Este enfoque tiene ventajas importantes en una etapa inicial:

- bajo costo técnico,
- facilidad para validar metodología,
- rapidez para hacer ajustes al instrumento,
- facilidad para corregir errores en el proceso,
- y menor complejidad operativa.

También tiene limitaciones:

- depende de intervención humana en cada ciclo,
- no escala bien si hay muchas ciudades,
- no permite acceso directo de cada usuario a sus resultados,
- no guarda automáticamente historial,
- y dificulta automatizar seguimiento o notificaciones.

---

## 3. Enfoque actual del sistema: la ciudad como unidad principal

En la etapa actual, el instrumento y el dashboard están orientados principalmente a trabajar con **ciudades**.

Por ello, la automatización futura debe tomar como base que:

- cada evaluación corresponde a una ciudad,
- cada usuario o cuenta debe quedar asociada a una ciudad específica,
- cada ciudad debe poder consultar únicamente su propia información,
- y cualquier visualización agregada de varias ciudades debe tratarse como una función especial y controlada.

En otras palabras, la arquitectura futura debe diseñarse bajo el principio de:

**una ciudad = una unidad principal de consulta, control de acceso y visualización.**

---

## 4. Escenario más simple de operación

La forma más simple de operar el sistema es la siguiente:

1. la encuesta se envía a una persona u organización, o se publica en línea,
2. una persona u organización llena la información correspondiente a una ciudad,
3. la organización propietaria del formulario descarga manualmente los datos desde KoboToolbox,
4. esa organización comparte el archivo o los resultados con la ciudad que respondió la encuesta,
5. la ciudad que respondió entra al dashboard en línea,
6. y carga su archivo o sus resultados para visualizar su desempeño.

Este modelo tiene la ventaja de que:

- no requiere integración automática con Kobo,
- no requiere base de datos en una primera fase,
- no requiere sistema de usuarios complejo,
- y puede funcionar muy rápido como piloto.

Sin embargo, también implica que:

- el dueño del formulario sigue siendo un intermediario,
- la entrega de resultados depende de una persona u organización central,
- no hay trazabilidad automática,
- y el usuario final no consulta directamente Kobo ni recibe resultados en tiempo real.

Además, este modelo todavía no garantiza por sí mismo que cada ciudad vea únicamente su propia información, por lo que requiere controles manuales o de procedimiento.

---

## 5. Variaciones mínimas posibles sobre el flujo simple

Antes de construir una solución completa, existen varias mejoras intermedias de bajo o mediano esfuerzo que pueden reducir trabajo manual sin entrar todavía a una arquitectura compleja.

### 5.1 Carga manual centralizada
- la organización propietaria del formulario descarga el archivo,
- separa manualmente las filas correspondientes a cada ciudad,
- lo sube manualmente al dashboard,
- y comparte una captura, PDF o enlace con la ciudad evaluada.

### 5.2 Carga manual descentralizada
- la organización propietaria del formulario descarga el archivo,
- separa manualmente las filas correspondientes a cada ciudad,
- lo comparte con la ciudad evaluada,
- y cada ciudad carga su propio archivo en el dashboard cuando quiera consultar resultados.

### 5.3 Dashboard privado con contraseña común
- el dashboard se publica en línea,
- se protege con una contraseña general o con una capa externa de acceso,
- y únicamente las organizaciones autorizadas pueden entrar a subir su archivo.

Esta opción mejora acceso restringido, pero **no es suficiente para garantizar separación estricta entre ciudades**, porque varias ciudades podrían compartir la misma puerta de entrada.

### 5.4 Envío semiautomático de resultados
- la organización propietaria del formulario descarga el archivo,
- corre un proceso interno para generar reportes individuales por ciudad,
- y envía automáticamente por correo o enlace los resultados a cada ciudad.

### 5.5 Actualización manual programada
- se define una frecuencia fija, por ejemplo semanal o mensual,
- una persona responsable descarga Kobo y actualiza el tablero,
- y las ciudades saben que los resultados se refrescan en esos cortes.

Estas variantes no eliminan la intervención manual, pero sí pueden mejorar mucho la operación sin exigir una reingeniería completa.

---

## 6. Escenarios intermedios de automatización

Entre el flujo totalmente manual y un sistema plenamente automatizado, hay varias opciones intermedias razonables.

### 6.1 Descarga automática desde Kobo, visualización manual
En este escenario:

- el sistema se conecta automáticamente a KoboToolbox,
- descarga respuestas nuevas mediante API,
- las guarda o normaliza,
- pero el acceso al dashboard sigue siendo relativamente simple o centralizado.

Ventajas:
- elimina parte del trabajo manual,
- reduce errores de exportación,
- mantiene una complejidad moderada.

### 6.2 Descarga automática y actualización interna del dashboard
En este escenario:

- un job programado consulta Kobo,
- identifica respuestas nuevas,
- valida y transforma datos,
- recalcula puntajes,
- y actualiza automáticamente la información visible en el dashboard.

Ventajas:
- el tablero siempre tiene información reciente,
- el equipo central no necesita descargar archivos a mano,
- mejora trazabilidad y control.

### 6.3 Acceso por ciudad sin integración total con Kobo
En este escenario:

- el dashboard ya tiene usuarios,
- cada ciudad entra con su cuenta,
- pero los datos pueden seguir siendo cargados o aprobados centralmente,
- sin que el usuario consulte Kobo directamente.

Ventajas:
- mejora control de acceso,
- permite personalización por ciudad,
- sin necesidad de una integración de extremo a extremo desde el primer día.

### 6.4 Revisión o aprobación humana antes de publicar
En este escenario:

- el sistema descarga automáticamente respuestas desde Kobo,
- pero no las publica de inmediato,
- sino que un administrador valida o aprueba antes de que aparezcan en el dashboard.

Ventajas:
- mayor control de calidad,
- útil cuando el instrumento cambia con frecuencia,
- o cuando hay riesgo de inconsistencias en los datos.

---

## 7. Escenario de sistema completo

Una versión más madura y robusta del sistema podría funcionar así:

1. una ciudad o su organización responsable crea una cuenta con usuario y contraseña,
2. el sistema registra su relación con una ciudad específica,
3. la ciudad responde el instrumento en KoboToolbox,
4. KoboToolbox recibe la respuesta,
5. un proceso automático detecta la nueva respuesta,
6. el sistema descarga los datos mediante la API de Kobo,
7. valida estructura, consistencia y versión del formulario,
8. normaliza los datos al formato interno del dashboard,
9. guarda la información en base de datos,
10. recalcula puntajes, alertas y recomendaciones,
11. asocia la evaluación con la ciudad y con el usuario correspondiente,
12. el usuario entra al dashboard con su cuenta,
13. y ve automáticamente su evaluación, su historial y sus resultados.

En una versión todavía más robusta, el sistema podría además:

- guardar múltiples mediciones por fecha,
- comparar resultados entre momentos de la misma ciudad,
- mostrar evolución temporal,
- enviar notificaciones,
- y generar reportes descargables automáticamente.

La regla general debería ser:

**cada ciudad accede únicamente a su propia información.**

---

## 8. Variantes posibles del sistema completo

No existe una sola forma “correcta” de automatizar esta solución. A continuación se describen combinaciones posibles.

### Variante A. Kobo como fuente externa y dashboard como visualizador
- Kobo sigue siendo el sistema principal de captura,
- el dashboard solo consulta y visualiza,
- y la lógica de usuario vive en el dashboard.

### Variante B. Kobo central + base de datos propia + dashboard privado
- Kobo recibe la información,
- una base de datos propia guarda una copia estructurada,
- y el dashboard consulta esa base en vez de leer directamente desde Kobo cada vez.

Esta variante suele ser más estable y escalable.

### Variante C. Kobo + validación + publicación por aprobación
- Kobo recibe respuestas,
- el sistema descarga,
- un administrador aprueba,
- y solo entonces se publica en el dashboard.

### Variante D. Kobo + cuentas por ciudad + historial
- cada ciudad tiene su cuenta,
- cada respuesta se asocia a su ciudad,
- el dashboard muestra todas sus evaluaciones históricas.

### Variante E. Kobo + autenticación + reportes automáticos
- además del dashboard, el sistema genera PDF, correo automático o resúmenes ejecutivos por cada nueva evaluación.

### Variante F. Sistema híbrido
- algunas ciudades operan con automatización completa,
- otras siguen usando carga manual,
- y ambas conviven durante una fase de transición.

Esta variante es especialmente útil cuando la madurez tecnológica de los usuarios finales es desigual.

---

## 9. Arquitectura futura sugerida por fases

### Fase 1. Operación manual
Objetivo:
- validar el instrumento,
- estabilizar la lógica del dashboard,
- probar el uso con ciudades reales.

Características:
- descarga manual desde Kobo,
- carga manual en el dashboard,
- sin base de datos ni usuarios persistentes.

### Fase 2. Integración automática con Kobo
Objetivo:
- reducir trabajo operativo manual.

Características:
- conexión con API de KoboToolbox,
- descarga automática de respuestas,
- validación de archivos,
- normalización al formato interno.

### Fase 3. Persistencia de datos
Objetivo:
- evitar depender solo de archivos.

Características:
- base de datos relacional, por ejemplo PostgreSQL,
- tabla de ciudades,
- tabla de usuarios,
- tabla de evaluaciones,
- tabla de historial de resultados,
- trazabilidad por fecha y versión del formulario.

### Fase 4. Acceso controlado por ciudad
Objetivo:
- dar autonomía al usuario final.

Características:
- inicio de sesión,
- permisos por ciudad,
- cada usuario ve solamente los datos de su ciudad,
- el administrador central ve resultados agregados o globales.

### Fase 5. Automatización avanzada
Objetivo:
- crear una experiencia integrada de extremo a extremo.

Características:
- sincronización automática con Kobo,
- actualización programada del dashboard,
- reportes automáticos,
- notificaciones,
- historial,
- comparaciones temporales,
- y eventualmente una vista agregada interna de múltiples ciudades bajo control estricto.

---

## 10. Recomendación técnica por capas

Para mantener el sistema ordenado y escalable, conviene separar claramente tres capas.

### 10.1 Capa de ingestión
Responsable de:
- conectarse a KoboToolbox,
- descargar respuestas,
- validar estructura,
- detectar cambios en el cuestionario,
- registrar errores de carga.

### 10.2 Capa de negocio
Responsable de:
- normalizar datos,
- calcular puntajes,
- generar alertas,
- producir recomendaciones,
- manejar historial,
- y aplicar reglas metodológicas.

### 10.3 Capa de visualización
Responsable de:
- mostrar resultados al usuario,
- manejar navegación,
- renderizar gráficas,
- exportar reportes,
- y controlar experiencia de acceso.

Esta separación es importante porque evita mezclar:
- integración con Kobo,
- reglas de negocio,
- y presentación visual.

---

## 11. Flujo técnico recomendado para una integración robusta

Un pipeline automatizado recomendable podría verse así:

1. KoboToolbox recibe respuestas nuevas.
2. Un job programado consulta la API.
3. El sistema identifica nuevas respuestas o cambios.
4. Se descarga la información.
5. Se valida contra el esquema esperado.
6. Se normalizan columnas y formatos.
7. Se construye o actualiza la identidad de la ciudad.
8. Se guarda la evaluación en base de datos.
9. Se recalculan puntajes, alertas y recomendaciones.
10. Se actualizan vistas y cachés del dashboard.
11. Se registra auditoría del proceso.
12. Se notifica al usuario si aplica.

Este flujo puede correr:
- por horario fijo,
- por lotes,
- o por evento, dependiendo de la infraestructura disponible.

---

## 12. Modelo de datos sugerido para una siguiente fase

En una implementación más robusta convendría tener, como mínimo:

### Tabla de ciudades
- id
- nombre visible
- país
- metadatos relevantes

### Tabla de usuarios
- id
- nombre
- correo
- hash de contraseña
- ciudad asociada
- rol
- estado de cuenta

### Tabla de evaluaciones
- id
- ciudad
- fecha de respuesta
- versión del formulario
- fuente de datos
- contenido normalizado
- estado de validación

### Tabla de resultados
- id de evaluación
- puntaje global
- nivel global
- resultados por dimensión
- alertas
- recomendaciones

### Tabla de trazabilidad
- fecha de sincronización
- origen
- errores
- cambios detectados
- versión del esquema

### Tabla o vista interna agregada
Opcionalmente, el sistema puede tener una vista agregada de múltiples ciudades para uso interno.

Esta vista **no debe exponerse como funcionalidad estándar para las ciudades usuarias**. Debe quedar restringida a personal autorizado y con reglas claras de uso.

---

## 13. Gestión de identidades y acceso

Cuando cada ciudad pueda entrar a ver sus resultados, ya no bastará una sola contraseña compartida.

En ese punto conviene implementar:

- usuarios por ciudad,
- restablecimiento seguro de contraseña,
- control por roles,
- auditoría de accesos,
- expiración de sesiones,
- MFA para administradores,
- y separación entre roles de administración y consulta.

### Principio de acceso recomendado
La regla recomendada es:

**cada ciudad solo puede ver la información de su propia ciudad.**

### Vista agregada de múltiples ciudades
La posibilidad de mostrar información de varias ciudades en un solo dashboard puede existir, pero solo bajo estas condiciones:

- uso estrictamente interno,
- acceso restringido a administradores o equipos autorizados,
- justificación institucional clara,
- y reglas explícitas sobre confidencialidad y tratamiento de datos.

No se recomienda que una ciudad usuaria pueda visualizar directamente la información detallada de otra ciudad, ya que esto puede ser sensible.

### Roles posibles
Por ejemplo:

- **administrador central**: ve todas las ciudades y controla configuración,
- **administrador de ciudad**: ve y gestiona solo su ciudad,
- **usuario lector**: solo consulta resultados de su ciudad,
- **revisor o aprobador**: valida evaluaciones antes de publicarlas.

---

## 14. Riesgos y decisiones importantes

Antes de automatizar conviene resolver varias preguntas.

### 14.1 ¿Quién es dueño del dato?
- la organización que creó el formulario,
- la ciudad que respondió,
- o ambas bajo reglas acordadas.

### 14.2 ¿Quién puede ver qué?
- solo la propia ciudad,
- el equipo central,
- ambos,
- o también ciertos perfiles internos autorizados.

### 14.3 ¿Existirá una vista comparativa de ciudades?
Si existe, debe ser una funcionalidad controlada y no una vista abierta para todas las ciudades.

### 14.4 ¿Habrá una sola versión del formulario o varias?
Si el cuestionario cambia con el tiempo, el sistema debe guardar la versión del instrumento usada en cada evaluación.

### 14.5 ¿Se publicarán resultados automáticamente o con revisión humana?
Esto define si el pipeline debe incluir una etapa de aprobación.

---

## 15. Recomendación práctica de evolución

Si el objetivo es avanzar de forma realista y controlada, una ruta razonable sería:

### Etapa 1
- mantener carga manual,
- estabilizar metodología,
- ajustar redacción, gráficas y recomendaciones.

### Etapa 2
- automatizar descarga desde Kobo,
- mantener revisión humana antes de publicar.

### Etapa 3
- agregar base de datos y cuentas de usuario,
- permitir consulta por ciudad.

### Etapa 4
- activar sincronización periódica,
- historial,
- notificaciones,
- y reportes automáticos.

### Etapa 5
- habilitar, si realmente se necesita, una vista agregada interna de múltiples ciudades con permisos restringidos.

Esta ruta evita sobrediseñar el sistema demasiado pronto y protege mejor la información sensible de cada ciudad.

---

## 16. Conclusión

La solución puede funcionar de muchas maneras, desde un flujo muy simple hasta una plataforma completa e integrada.

### Opción más simple
- formulario enviado o publicado,
- ciudad responde,
- equipo central descarga manualmente,
- comparte resultados,
- y la ciudad consulta el dashboard cargando su información.

### Opciones intermedias
- automatizar descarga,
- filtrar resultados por ciudad,
- mantener revisión humana,
- habilitar acceso privado al dashboard.

### Opción más robusta
- usuarios con cuenta y contraseña,
- integración automática con Kobo,
- base de datos,
- sincronización automática,
- resultados disponibles al iniciar sesión,
- historial,
- permisos por ciudad,
- y automatización del ciclo completo.

### Vista agregada de múltiples ciudades
Puede existir como una herramienta interna de administración, monitoreo o análisis, pero no se recomienda como modalidad abierta para usuarios de ciudades, ya que la información puede ser sensible y no debería exponerse entre ciudades.

La elección correcta dependerá de recursos, prioridades, volumen de uso y nivel de control deseado. En cualquier caso, la recomendación principal es clara:

**el sistema debe evolucionar para que cada ciudad vea únicamente su propia información, y cualquier vista agregada de múltiples ciudades quede restringida a uso interno y controlado.**
