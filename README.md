# Urban MCP

Proyecto abierto para mantener cómo agentes y clientes MCP utilizan herramientas de urbanismo: software original, datos de entrada, preparación, instalación, operación y pruebas.

**Estado: planificación pública.** El trabajo inicial se discute mediante una RFC y un pull request. Un repositorio investigado no equivale a un adaptador operativo ni a un modelo de ciudad listo.

La unidad de contribución propuesta es un **paquete de capacidad**: herramienta original + interfaz admitida + requisitos de datos + fuentes y preparación + caso comprobable + guía operativa del agente. Las bibliotecas auxiliares y los estándares se mantienen como dependencias, sin convertirlos automáticamente en servidores MCP.

## Revisar y contribuir

- **[RFC y pull request #1](https://github.com/polisplexity/urban-mcp/pull/1):** propuesta técnica abierta, todavía sin fusionar ni fijar un framework global.
- **[Matriz de datos por herramienta](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/data/tool-data-matrix.md):** 229 candidatos, 48 perfiles iniciales y 28 canales de fuentes. Distingue insumos abiertos, datos del operador, preparación y faltantes.
- **[Tareas para contribuir](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/tasks.md):** 31 tareas en siete hitos, incluyendo investigación por familias.
- **[Guía de contribución](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/CONTRIBUTING.md)** y **[roadmap](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/roadmap.md)**.

La propuesta vive en `rfc/data-ready-capabilities`. Para revisar archivos y comprobaciones desde un clon:

```sh
git switch rfc/data-ready-capabilities
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
docker compose --profile preflight run --rm --build preflight
```

Este contenedor **solo valida planificación/metadatos**. El primer caso propuesto es SUMO Hello: seis assets upstream fijados por commit/hash, con revisión de referencias y aristas. Todavía faltan admisión del alcance de datos, runtime científico Docker, baseline nativo, comparación MCP y ensayo independiente del agente.

La RFC separa un caso de referencia reproducible para empezar de un caso de ciudad real. Las fuentes candidatas no significan que un modelo ya tenga datos suficientes. La [propuesta para agentes y skills](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/agents/day-zero.md) conserva esa distinción y no exige un agente propio ni un archivo SOUL obligatorio.

El proyecto no exige un proveedor de IA ni un lenguaje único para los motores. La licencia de este repositorio no sustituye la de cada software, dataset, peso o servicio conectado.
