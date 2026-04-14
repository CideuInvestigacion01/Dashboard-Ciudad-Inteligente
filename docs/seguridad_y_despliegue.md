# Seguridad y despliegue

## Cambio aplicado en esta versión

La aplicación ya **no incluye una contraseña integrada en el código ni depende de una variable obligatoria para funcionar**.

Esto facilita que otros desarrolladores reutilicen el repositorio y evita acoplar la app a una credencial específica desde la primera versión.

## Por qué sigue siendo importante proteger la app

Aunque el tablero sea de autoevaluación, puede revelar:

- debilidades institucionales,
- carencias de infraestructura digital,
- vacíos en protección de datos,
- ausencia de políticas o equipos,
- prioridades internas y restricciones presupuestarias.

En un entorno real, esa información puede ser sensible desde el punto de vista institucional, reputacional y operativo.

Por eso, aunque la contraseña ya no venga integrada, **sí debe recomendarse y aplicarse en despliegues reales**, idealmente junto con autenticación por usuario y control por organización.

## Recomendación mínima

Para una primera versión desplegada con datos reales:

- autenticación externa o en la propia app,
- HTTPS,
- secretos fuera del repositorio,
- control de acceso por organización,
- deshabilitar exposición pública innecesaria.

## Nivel recomendado para producción

- autenticación por usuario,
- autorización por rol,
- reverse proxy con TLS,
- logs de acceso,
- rate limiting,
- backup,
- base de datos administrada,
- segregación entre entornos de desarrollo, pruebas y producción.

## Recomendación de despliegue

### Opción 1. Prototipo controlado

- Streamlit sin contraseña embebida
- acceso restringido por red privada, túnel seguro o autenticación del proveedor de hosting
- datos anonimizados o controlados

### Opción 2. Producción institucional

- Docker
- Nginx
- Streamlit detrás de proxy
- PostgreSQL
- autenticación separada o SSO
- monitoreo y alertas

## Buenas prácticas de secretos

Nunca subir al repositorio:

- contraseñas reales,
- API keys de KoboToolbox,
- tokens de sesión,
- dumps de respuestas reales,
- archivos `.env`.
