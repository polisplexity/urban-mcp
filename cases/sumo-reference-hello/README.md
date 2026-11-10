# Referencia técnica auxiliar: SUMO Hello

Estado: **caso propuesto, no ejecutable admitido**. Ejemplo sintético upstream; no representa una ciudad real ni demanda calibrada.

La [aceptación final del proyecto](../../docs/cases/municipal-first.md) requiere un caso municipal con cosecha y reproducción independiente. Completar este ejemplo verifica una referencia técnica y no promueve por sí solo la herramienta a capacidad municipal admitida.

`case.json` identifica seis archivos originales en el commit `9a562c33fc452272ccd1fe5790632ae4e5ba7dc3`, con hashes SHA-256, tamaño y blob. Se verificaron bytes para preparar la propuesta; los archivos no se redistribuyen en Git.

## Trabajo de datos

- Revisar licencia/atribución y alcance de los archivos elegidos.
- Adquirir y comprobar el conjunto completo, conservando nombres relativos.
- Verificar que `hello.sumocfg` resuelve red/rutas/configuración y que las rutas usan aristas de la red.
- Registrar que las coordenadas son las del ejemplo; no inventar CRS geográfico.

## Trabajo del sandbox y MCP

1. Elegir una distribución SUMO y fijar imagen/versión compatibles.
2. Ejecutar el original con la configuración del ejemplo y semilla/tiempos explícitos.
3. Conservar baseline, logs, recuentos y límites de recursos; probar repetición y cierre.
4. Inspeccionar y seleccionar una operación de un MCP SUMO existente; fijar sus dependencias y mapear el mismo conjunto de entradas.
5. Comparar los mismos resultados y errores por MCP.
6. Ensayar skill/agente y documentar qué falta para un caso real.

El archivo `.sumocfg` es una entrada nativa, no el esquema de argumentos del MCP. La herramienta debe mapearlo explícitamente. Una comprobación de XML/hashes no acredita simulación correcta.
