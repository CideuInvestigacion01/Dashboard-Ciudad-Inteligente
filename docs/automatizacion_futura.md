# Automatización futura e integración con KoboToolbox

## Situación actual

La aplicación está pensada para cargar manualmente archivos exportados desde KoboToolbox.

Esto permite:

- validar la metodología,
- ajustar las gráficas,
- revisar el modelo de recomendaciones,
- probar el flujo con bajo costo técnico inicial.

## Arquitectura futura sugerida

### Fase 1. Export manual

- Una persona descarga el CSV/XLSX desde KoboToolbox.
- La persona autorizada sube el archivo al tablero.
- El tablero procesa el resultado y muestra el diagnóstico.

### Fase 2. Export automatizado desde KoboToolbox

Usar la API oficial de KoboToolbox para:

- autenticar con API key,
- identificar el `asset_uid` del formulario,
- generar exportaciones sincronizadas,
- descargar respuestas limpias para el tablero. citeturn839519search3turn839519search11

### Fase 3. Persistencia y cuentas de usuario

Agregar:

- base de datos PostgreSQL,
- tabla de municipios,
- tabla de usuarios,
- tabla de respuestas / evaluaciones,
- historial de mediciones por fecha,
- permisos por organización.

### Fase 4. Portal institucional

- inicio de sesión por usuario,
- cada municipio ve solo sus resultados,
- administración central ve comparativos agregados,
- generación de reportes descargables,
- alertas cuando baja una dimensión crítica.

## Recomendación de pipeline

1. KoboToolbox recibe respuestas.
2. Un job programado consulta API.
3. Se valida esquema.
4. Se normalizan columnas.
5. Se guarda en base de datos.
6. Se recalculan puntajes.
7. Se actualiza el dashboard.
8. Se envía notificación al usuario si aplica.

## Recomendación técnica

Para la siguiente fase conviene separar la solución en tres capas:

- **capa de ingestión**: descarga y validación de Kobo,
- **capa de negocio**: scoring, recomendaciones, benchmarking,
- **capa de visualización**: dashboard y reportes.

Así se evita mezclar lógica de datos con interfaz.

## Consideraciones de identidad y acceso

Cuando cada ciudad pueda entrar a ver sus resultados, ya no bastará una sola contraseña compartida. En ese punto conviene implementar:

- usuarios por organización,
- restablecimiento seguro de contraseña,
- control por roles,
- auditoría de accesos,
- expiración de sesiones,
- MFA para administradores.
