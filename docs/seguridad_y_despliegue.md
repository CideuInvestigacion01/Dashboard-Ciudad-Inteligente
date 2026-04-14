# Seguridad y despliegue

## Por qué esta app no debería quedar abierta sin contraseña

Aunque el cuestionario no parezca altamente sensible a primera vista, sí puede revelar:

- debilidades institucionales,
- carencias de infraestructura digital,
- vacíos en protección de datos,
- ausencia de políticas o equipos,
- prioridades internas y restricciones presupuestarias.

En un entorno real, esa información puede ser sensible desde el punto de vista institucional, reputacional y operativo.

Además, la normativa mexicana exige medidas administrativas, técnicas y físicas para proteger datos personales, y los marcos internacionales de seguridad recomiendan autenticación robusta y buena gestión de sesiones. citeturn548820search5turn548820search8turn548820search0turn548820search6turn548820search4

## Nivel mínimo recomendado

Para una primera versión:

- contraseña de acceso,
- HTTPS,
- secretos fuera del repositorio,
- hash bcrypt de contraseñas,
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

- Streamlit + password
- Render / VM pequeña
- acceso restringido

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
