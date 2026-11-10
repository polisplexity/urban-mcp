# Urban MCP

Proyecto abierto para mantener cómo agentes y clientes MCP utilizan herramientas de urbanismo: software original, datos de entrada, preparación, instalación, operación y pruebas.

**Estado: catálogo en investigación y primer caso municipal ejecutable.** [Helsinki: inventario de bibliotecas y salud](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/cases/helsinki-service-inventory/README.md) ya recorre datos públicos, Docker, original, MCP y dos agentes. La admisión se limita a sus operaciones y parámetros comprobados; el resto del catálogo conserva su estado de investigación.

La unidad de contribución propuesta es un **paquete de capacidad**: herramienta original + interfaz admitida + requisitos de datos + fuentes y preparación + caso comprobable + guía operativa del agente. Las bibliotecas auxiliares y los estándares se mantienen como dependencias, sin convertirlos automáticamente en servidores MCP.

## Revisar y contribuir

- **[RFC y pull request #1](https://github.com/polisplexity/urban-mcp/pull/1):** propuesta técnica abierta, todavía sin fusionar ni fijar un framework global.
- **[Primer caso y comandos para repetir](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/cases/helsinki-service-inventory/README.md):** Helsinki, 12,455 registros cosechados, 34 distritos y población de 2025; [datos fijados por hash](https://github.com/polisplexity/urban-mcp/releases/tag/data-helsinki-20261110).
- **[Cobertura por función y origen](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/cases/helsinki-service-inventory/functionality.md):** MCP original GDAL + seis funciones nuevas para datos/inventario, con prueba de las 19 funciones expuestas.
- **[Orden de construcción y aceptación municipal](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/docs/cases/municipal-first.md):** inventario de equipamientos/población, accesibilidad peatonal y cobertura vegetal. Cada capacidad debe cosechar datos y demostrar un resultado municipal reproducible.
- **[Matriz de datos por herramienta](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/docs/data/tool-data-matrix.md):** 229 entradas, 48 perfiles iniciales y 33 canales de fuentes. Distingue alcance admitido por caso, candidatos, datos del operador y faltantes.
- **[Tareas para contribuir](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/docs/tasks.md):** casos municipales, reproducción e investigación por familias en siete hitos; consultar también las [issues abiertas](https://github.com/polisplexity/urban-mcp/issues).
- **[Guía de contribución](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/CONTRIBUTING.md)** y **[roadmap](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/roadmap.md)**.

La RFC inicial vive en `rfc/data-ready-capabilities`; la implementación del primer caso, en `feat/helsinki-municipal-inventory`. Para ejecutar:

```sh
git switch feat/helsinki-municipal-inventory
# En Linux/WSL, mapear el usuario propio para el workspace:
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
mkdir -p .urban-mcp/helsinki
docker compose --profile municipal build inventory
docker compose --profile municipal run --rm harvest harvest --mode snapshot
docker compose --profile municipal run --rm inventory prepare
docker compose --profile municipal run --rm inventory inventory --service-id 813 --run-id native-library
docker compose --profile municipal run --rm inventory test
```

El perfil `municipal` ejecuta el caso y sus pruebas reales. El perfil `preflight` sigue validando únicamente planificación/metadatos. SUMO Hello permanece como referencia sintética auxiliar, sin motor/MCP admitidos.

Codex y un perfil aislado de Hermes ejecutaron la misma tarea sin respuestas esperadas, con datos/resultados separados. La [evidencia del caso](https://github.com/polisplexity/urban-mcp/tree/feat/helsinki-municipal-inventory/cases/helsinki-service-inventory/evidence) distingue pruebas de protocolo, resultado nativo y comportamiento de los agentes. [Configurar otro cliente](https://github.com/polisplexity/urban-mcp/blob/feat/helsinki-municipal-inventory/tools/client_config.py) no exige un agente propio ni un archivo SOUL obligatorio.

El proyecto no exige un proveedor de IA ni un lenguaje único para los motores. La licencia de este repositorio no sustituye la de cada software, dataset, peso o servicio conectado.

Para crecer como proyecto libre, publicamos recetas, procedencia, decisiones, errores útiles y métodos de comprobación. Se puede aportar una fuente, una corrección, una reproducción, una traducción o un caso en otro municipio, conservando autoría y licencias originales.
