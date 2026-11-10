# Evidencia pública del primer caso

Snapshot: `20261110T112344Z-500b5c`, adquirido desde los publicadores en Docker y redistribuido legalmente con SHA-256 fijado. No se incluyen credenciales, configuración privada, prompts de sistema ni razonamiento de los agentes.

| Comprobación | Resultado observado |
|---|---|
| Contratos/adquisición | 18 pruebas: integridad, derechos/estados, duplicados/paginación, truncamiento y preservación del snapshot anterior ante fallo. |
| Operación MCP por subprocess stdio | 72 comprobaciones aprobadas; 19 funciones expuestas llamadas; comparación nativa de geometrías, IDs, píxeles, estadísticas y caso municipal; recursos/prompts y rechazos. |
| Pruebas del MCP original con compatibilidad aplicada | 69 aprobadas. Se usa el entorno sin workspace que espera su fixture unitaria; el MCP operativo conserva `/data` como límite. |
| Codex CLI 0.167.0-alpha.3.2, GPT-6.1-sol | 25 llamadas, 13 funciones distintas del servidor; sin otros tipos de llamadas a herramientas en la traza. |
| Hermes 0.18.2, Claude Sonnet 4.6 | 24 llamadas del servidor y sus helpers de protocolo; perfil/workspace nuevos, sin conectores de mensajería. |
| Resultado de bibliotecas, ID 813 | 46 puntos; los CSV de ambos agentes son idénticos al nativo (SHA-256 en `agents.json`). |
| Resultado de salud, ID 703 | 23 puntos; los CSV de ambos agentes son idénticos al nativo. |

`harvest.json` conserva el recibo y hashes de cada página; `native.json`, los comandos y resultados; `mcp.json`, el ensayo de protocolo; `mcp-tools.json`, el esquema realmente descubierto; `runtime.json`, versiones Python y bibliotecas nativas. Las ruedas Pyogrio y Rasterio incluyen versiones distintas de GDAL (3.10.3 y 3.9.3), registradas por separado. `reproduction.json` enlaza resultados/huellas de implementación; `agents.json` guarda llamadas y comparación de artefactos. Las respuestas finales se conservan en los dos Markdown adyacentes.

La tarea pública no contiene resultados esperados. Cada agente obtuvo el snapshot desde un workspace vacío, preparó, descubrió categorías, ejecutó inventarios, inspeccionó artefactos, reproyectó y produjo buffers, revisó el ráster y probó entradas inválidas. La cobertura de todas las funciones pertenece a la suite determinista; no se atribuye a cada agente la ejecución de todas ellas.

La revisión de las respuestas finales comprobó el alcance descriptivo y la distinción entre diferencia estadística de población y coordenadas de residentes, ráster categórico y población, buffer euclidiano y acceso peatonal. Los fallos anteriores se documentan en `../findings.md`. La evidencia no sustituye una revisión disciplinaria externa ni acredita otras ciudades, todas las variantes de drivers o un gemelo completo.
