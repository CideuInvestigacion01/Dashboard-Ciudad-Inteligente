# Seguridad y despliegue

## 1. Propósito de este documento

Este documento establece recomendaciones de seguridad, privacidad y despliegue para el tablero de autoevaluación de transición digital y ciudades inteligentes.

Su objetivo es ayudar a que cualquier equipo externo que continúe el desarrollo o implemente la solución entienda con claridad:

- qué riesgos existen,
- qué controles mínimos deben implementarse,
- qué buenas prácticas de despliegue conviene seguir,
- y qué obligaciones organizativas y normativas deben considerarse antes de operar la plataforma con datos reales.

Este documento no sustituye asesoría legal ni una política formal de cumplimiento, pero sí identifica medidas mínimas que no deberían omitirse.

---

## 2. Cambio aplicado en esta versión

La aplicación **no incluye una contraseña integrada en el código** ni depende de una variable obligatoria para funcionar.

Esto facilita que otros desarrolladores reutilicen el repositorio y evita acoplar la app a una credencial específica desde la primera versión.

Sin embargo, este cambio **no significa** que la aplicación deba desplegarse sin protección. Al contrario:

- el repositorio puede permanecer genérico y reutilizable,
- pero el entorno desplegado debe estar protegido,
- y la gestión de acceso debe resolverse en la arquitectura de despliegue o en una capa de autenticación adecuada.

---

## 3. Por qué sigue siendo importante proteger la aplicación

Aunque el tablero sea una herramienta de autoevaluación, puede revelar información sensible de una ciudad, por ejemplo:

- debilidades institucionales,
- carencias de infraestructura digital,
- vacíos en protección de datos,
- ausencia de políticas o equipos,
- restricciones presupuestarias,
- prioridades de mejora internas,
- niveles de madurez digital relativamente bajos,
- y obstáculos que una ciudad considera críticos.

En un entorno real, esta información puede ser sensible desde el punto de vista:

- institucional,
- reputacional,
- operativo,
- estratégico,
- e incluso político.

Por eso, aunque la contraseña ya no venga integrada en el código, **sí debe recomendarse y aplicarse protección real en despliegues con datos verdaderos**, idealmente con autenticación por usuario, control por ciudad y separación estricta de permisos.

---

## 4. Principio central de acceso

La recomendación principal para esta solución es la siguiente:

**cada ciudad debe poder ver únicamente su propia información.**

Esto implica que:

- una ciudad no debe ver los resultados detallados de otra ciudad,
- un usuario debe estar asociado a una ciudad concreta,
- el acceso debe depender de permisos explícitos,
- y cualquier vista agregada de múltiples ciudades debe considerarse una función especial de uso interno y no una vista normal para usuarios finales.

### Vista agregada de múltiples ciudades
La posibilidad de visualizar varias ciudades en un solo dashboard puede existir, pero solo bajo estas condiciones:

- uso estrictamente interno,
- acceso restringido a administradores o equipos autorizados,
- justificación institucional clara,
- y reglas expresas de confidencialidad y tratamiento de datos.

No se recomienda que usuarios de una ciudad puedan explorar libremente la información detallada de otras ciudades.

---

## 5. Obligación de política de uso de datos

Antes de operar la plataforma con datos reales, debe existir una **política explícita sobre el uso de los datos**.

Esta no debe considerarse opcional. Es una condición mínima de operación responsable.

### La política debe definir al menos:
- qué datos se recogen,
- con qué finalidad se utilizan,
- quién puede acceder a ellos,
- cuánto tiempo se conservan,
- si se compartirán con terceros,
- si se usarán para análisis internos, investigación o reportes,
- si existirán vistas agregadas de múltiples ciudades,
- cómo se protegerán,
- y cómo se corregirán o eliminarán si fuera necesario.

### Aceptación de la política
La organización o persona usuaria debe aceptar expresamente esta política antes de utilizar la plataforma con datos reales.

Esto puede implementarse, por ejemplo, mediante:
- una casilla de aceptación al registrarse,
- un consentimiento previo al primer acceso,
- o un proceso contractual / institucional de aceptación documentada.

### Qué no debería ocurrir
No debería permitirse que una ciudad:
- cargue información,
- acceda a resultados,
- o permanezca usando la plataforma,

sin que exista una aceptación clara de las condiciones de uso y tratamiento de datos.

---

## 6. Requisitos mínimos de protección de datos

Además de la política de uso, existen medidas mínimas de protección de datos que deberían considerarse obligatorias en una implementación seria.

### 6.1 Minimización de datos
Recoger únicamente la información realmente necesaria para operar la solución.

### 6.2 Limitación de finalidad
No usar los datos para fines distintos a los informados y aceptados.

### 6.3 Control de acceso
Restringir el acceso según rol, ciudad y necesidad operativa real.

### 6.4 Conservación limitada
Definir cuánto tiempo se almacenarán los datos y cuándo serán depurados, archivados o anonimizados.

### 6.5 Trazabilidad
Registrar accesos, cambios y procesos de carga cuando el sistema opere con datos reales.

### 6.6 Protección de credenciales
Las contraseñas nunca deben almacenarse en texto plano. Deben almacenarse como hash seguro.

### 6.7 Derecho de revisión y corrección
Debe existir un procedimiento para corregir datos erróneos y, si aplica legalmente, para solicitar eliminación o restricción de uso.

### 6.8 Manejo de incidentes
Debe existir un procedimiento básico para responder a:
- fuga de información,
- acceso no autorizado,
- exposición accidental,
- o pérdida de datos.

---

## 7. Requisitos regulatorios que deben revisarse

Dependiendo del país, la institución o el entorno de despliegue, puede ser obligatorio cumplir con marcos regulatorios específicos.

Aunque este documento no reemplaza revisión legal, como mínimo debe verificarse:

- legislación de protección de datos personales aplicable,
- reglas institucionales sobre almacenamiento y transferencia de datos,
- requisitos de consentimiento o aceptación informada,
- normas sobre retención de datos,
- restricciones de localización o residencia de datos,
- y reglas internas de seguridad de la organización propietaria del sistema.

### Recomendación mínima
Antes de operar con datos reales, el equipo responsable debería validar con su área jurídica, de cumplimiento o de protección de datos si existen obligaciones específicas en su jurisdicción.

---

## 8. Recomendación mínima para una primera versión con datos reales

Para una primera versión desplegada con datos reales, como mínimo debería existir:

- autenticación externa o en la propia app,
- HTTPS,
- secretos fuera del repositorio,
- control de acceso por ciudad,
- deshabilitar exposición pública innecesaria,
- política de uso de datos aceptada por el usuario,
- y definición explícita de quién puede ver información agregada.

---

## 9. Nivel recomendado para producción

En un entorno institucional o de producción, se recomienda implementar como mínimo:

- autenticación por usuario,
- autorización por rol,
- reverse proxy con TLS,
- logs de acceso,
- rate limiting,
- backup,
- base de datos administrada,
- segregación entre entornos de desarrollo, pruebas y producción,
- rotación de secretos,
- revisión periódica de permisos,
- y trazabilidad básica de cargas, accesos y publicaciones.

---

## 10. Recomendaciones de despliegue

### 10.1 Opción 1. Prototipo controlado
Adecuado para:
- validación metodológica,
- pruebas con pocos usuarios,
- demos cerradas,
- datos anonimizados o poco sensibles.

Características recomendadas:
- Streamlit sin contraseña embebida,
- acceso restringido por red privada, túnel seguro o autenticación del proveedor de hosting,
- datos anonimizados o controlados,
- sin exposición abierta al público,
- y preferiblemente sin almacenar datos reales a largo plazo.

### 10.2 Opción 2. Producción institucional
Adecuado para:
- operación continua,
- usuarios múltiples,
- datos reales,
- acceso por ciudad,
- historial y trazabilidad.

Características recomendadas:
- Docker,
- Nginx o reverse proxy equivalente,
- Streamlit detrás de proxy,
- PostgreSQL u otra base administrada,
- autenticación separada o SSO,
- monitoreo y alertas,
- backups automáticos,
- logs centralizados,
- y controles estrictos de permisos.

---

## 11. Gestión de usuarios y permisos

Cuando la solución evolucione hacia uso multiusuario, conviene establecer roles claros.

### Roles mínimos recomendados
- **Administrador central**: gestiona configuración, usuarios y acceso a vistas agregadas.
- **Administrador de ciudad**: consulta y gestiona información de su propia ciudad.
- **Usuario lector**: solo visualiza los resultados de su ciudad.
- **Revisor o aprobador**: valida información antes de publicar resultados si existe flujo de aprobación.

### Principio recomendado
Los permisos deben asignarse por el criterio de **mínimo privilegio**:

cada persona debe tener acceso solamente a lo estrictamente necesario para realizar su función.

---

## 12. Separación entre entornos

Debe existir una separación clara entre:

- desarrollo,
- pruebas,
- y producción.

### Esto implica, como mínimo:
- distintas configuraciones por entorno,
- distintas credenciales,
- distintos secretos,
- no usar bases de datos reales en desarrollo local,
- no reutilizar contraseñas entre entornos,
- y no mezclar archivos de prueba con datos reales.

---

## 13. Buenas prácticas de secretos

Nunca deben subirse al repositorio:

- contraseñas reales,
- API keys de KoboToolbox,
- tokens de sesión,
- secretos de despliegue,
- dumps de respuestas reales,
- archivos `.env`,
- claves privadas,
- o archivos de configuración con credenciales embebidas.

### Recomendación
Usar siempre:
- variables de entorno,
- secret managers,
- servicios seguros del proveedor de nube,
- o mecanismos equivalentes de gestión de secretos.

---

## 14. Buenas prácticas de almacenamiento de datos

### 14.1 Datos en tránsito
Toda comunicación entre usuario y sistema debe viajar por HTTPS.

### 14.2 Datos en reposo
Si se almacenan evaluaciones, deben guardarse en infraestructura protegida y con controles de acceso adecuados.

### 14.3 Backups
Deben existir copias de seguridad regulares y procedimientos de restauración probados.

### 14.4 Versionado del cuestionario
Si cambia el instrumento, debe guardarse la versión correspondiente a cada evaluación para evitar interpretaciones incorrectas.

### 14.5 Anonimización
Cuando se usen datos para pruebas, demos o desarrollo, se recomienda anonimizar información identificable de ciudades y usuarios siempre que sea posible.

---

## 15. Logs, monitoreo y auditoría

En producción, conviene registrar como mínimo:

- accesos exitosos y fallidos,
- cargas de archivos o sincronizaciones,
- errores de normalización o cálculo,
- cambios de permisos,
- y publicaciones o aprobaciones de resultados.

### Importante
Los logs también pueden contener información sensible. Por eso:
- deben protegerse,
- su acceso debe estar restringido,
- y deben tener política de retención.

---

## 16. Riesgos principales si no se protege adecuadamente

Si la aplicación se despliega sin medidas adecuadas, pueden ocurrir problemas como:

- acceso de una ciudad a información de otra ciudad,
- exposición pública de resultados sensibles,
- filtración de debilidades institucionales,
- uso no autorizado de datos,
- pérdida de confianza de los usuarios,
- incumplimiento normativo,
- y daño reputacional a las organizaciones involucradas.

---

## 17. Requisitos mínimos antes de habilitar uso real

Antes de abrir la plataforma a ciudades usuarias con datos reales, deberían estar resueltos al menos estos puntos:

1. existe una política de uso de datos,
2. existe un mecanismo de aceptación de esa política,
3. el acceso está restringido por usuario y ciudad,
4. la plataforma usa HTTPS,
5. los secretos no están en el repositorio,
6. existe un criterio claro para vistas agregadas internas,
7. existe una estrategia mínima de backup,
8. existe separación entre entornos,
9. y existe una persona o equipo responsable de seguridad operativa.

---

## 18. Recomendación práctica de madurez por etapas

### Etapa 1. Prototipo controlado
- acceso restringido,
- datos anonimizados o de prueba,
- sin exposición pública abierta.

### Etapa 2. Piloto con datos reales
- autenticación básica,
- política de uso aceptada,
- control de acceso por ciudad,
- HTTPS,
- y revisión manual de publicación.

### Etapa 3. Producción institucional
- autenticación sólida,
- autorización por rol,
- base de datos administrada,
- trazabilidad,
- backups,
- monitoreo,
- y vista agregada interna restringida.

---

## 19. Conclusión

La ausencia de una contraseña embebida en el código no debe interpretarse como ausencia de controles. Al contrario: la protección del sistema debe resolverse de manera más robusta en la arquitectura de despliegue y en la gestión de usuarios.

La regla operativa recomendada es clara:

**cada ciudad debe ver únicamente su propia información.**

Además:

- debe existir una política de uso de datos,
- esa política debe ser aceptada por quien use la plataforma,
- debe revisarse el cumplimiento regulatorio aplicable,
- y cualquier vista agregada de múltiples ciudades debe mantenerse como función interna, restringida y controlada.

En resumen, la seguridad no debe tratarse como un complemento opcional del proyecto, sino como una condición obligatoria para cualquier despliegue real con datos verdaderos.
