# Cómo contribuir

La propuesta inicial está en una RFC/PR. Se puede contribuir a investigar una interfaz, admitir un dataset, preparar un caso o implementar una capacidad. No hace falta instalar todos los motores.

1. Elige una tarea o abre una propuesta indicando herramienta, operación concreta y pregunta municipal. Define territorio y fuentes desde el inicio con la [plantilla de caso](docs/cases/municipal-case-template.md).
2. Revisa `registry/tools.json` y la ficha de datos. Comprueba si un MCP, binding o servicio original ya cubre la operación.
3. Identifica datos mínimos por operación. Registra fuente original, asset exacto, licencia/atribución, versión/hash, cobertura, unidades y calidad. Separa observaciones, modelos y supuestos.
4. Documenta las transformaciones y el binding final: qué entrada se convierte en qué archivo, sección, parámetro o argumento del motor. No basta con enlazar un portal.
5. Construye cosecha reproducible: filtros/paginación, versiones, caché, reintentos y recibo de obtenidos/faltantes/fallidos. Prepara una muestra permitida para CI; el caso municipal completo requiere adquisición reproducible y derechos revisados.
6. Ejecuta el caso directamente en el original. Conserva comandos, versiones, archivos y resultado de referencia antes de comparar MCP.
7. Implementa solo el delta que falte; prueba resultado, error relevante, ciclo de vida y recuperación. La skill debe permitir que otro agente identifique datos faltantes sin inventarlos.
8. Envía PR con evidencia y límites. Marca por separado fuente admitida, datos preparados, motor verificado, MCP verificado y agente verificado. La [aceptación final](docs/cases/municipal-first.md) exige resultado municipal y reproducción independiente: una fixture técnica no la sustituye.

## Comprobaciones de este PR de planificación

```sh
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
docker compose --profile preflight run --rm preflight
```

Los archivos `planning/*.tsv` son decisiones editables. `registry/` y la matriz Markdown se generan desde ellos. `tools/build_data_registry.py` reconstruye fuentes/perfiles/matriz; `tools/build_planning_catalog.py` solo se usa para importar una nueva revisión pública de investigación con el formato documentado.

Para cambios de Helsinki, seguir [el caso ejecutable](cases/helsinki-service-inventory/README.md): construir la imagen, adquirir el snapshot permitido, preparar y ejecutar la suite MCP. Se ensayan todas las funciones expuestas y las familias de recursos/prompts; ampliar parámetros/drivers exige casos nuevos y su contraste nativo. La admisión se deriva de `case.json` y evidencia revisada; no marcar un campo como verificado para hacer pasar CI.

## Cómo revisar una propuesta

- **Datos:** ¿realmente alimentan esa operación? ¿qué falta? ¿qué se transforma y qué se pierde?
- **Software:** ¿se reutiliza la capacidad original? ¿está justificado el código nuevo y su runtime?
- **Prueba:** ¿se compara con el original y un resultado conocido? ¿se distinguen datos de referencia y ciudad real?
- **Operación:** ¿se puede instalar, diagnosticar, detener y volver a usar sin estado oculto?

No subir motores, modelos, pesos o datasets de terceros sin revisar su alcance de distribución. No incorporar datos de productos privados existentes para facilitar una demo pública.

## Crecer como proyecto libre

Publicar también decisiones, errores y métodos de comprobación. Se puede contribuir admitiendo una fuente, reproduciendo un caso, corrigiendo datos/unidades, traduciendo la guía o transfiriendo un caso a otro municipio. Reconocer autoría y atribuciones upstream; el código y los datos conservan sus propias licencias. El recorrido público debe poder repetirse sin credenciales privadas del autor ni proveedor LLM de pago obligatorio.
