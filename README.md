# Urban MCP

Proyecto abierto para mantener cómo agentes y clientes MCP utilizan herramientas de urbanismo: software original, datos de entrada, preparación, instalación, operación y pruebas.

**Estado: planificación pública.** El trabajo inicial se discute mediante una RFC y un pull request. Un repositorio investigado no equivale a un adaptador operativo ni a un modelo de ciudad listo.

La unidad de contribución propuesta es un **paquete de capacidad**: herramienta original + interfaz admitida + requisitos de datos + fuentes y preparación + caso comprobable + guía operativa del agente. Las bibliotecas auxiliares y los estándares se mantienen como dependencias, sin convertirlos automáticamente en servidores MCP.

## Revisar y contribuir

- **[RFC y pull request #1](https://github.com/polisplexity/urban-mcp/pull/1):** propuesta técnica abierta, todavía sin fusionar ni fijar un framework global.
- **[Orden de construcción y aceptación municipal](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/cases/municipal-first.md):** inventario de equipamientos/población, accesibilidad peatonal y cobertura vegetal. Cada capacidad debe cosechar datos y demostrar un resultado municipal reproducible.
- **[Matriz de datos por herramienta](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/data/tool-data-matrix.md):** 229 candidatos, 48 perfiles iniciales y 30 canales de fuentes. Distingue insumos abiertos, datos del operador, preparación y faltantes.
- **[Tareas para contribuir](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/tasks.md):** 35 tareas en siete hitos, incluyendo los primeros casos municipales e investigación por familias.
- **[Guía de contribución](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/CONTRIBUTING.md)** y **[roadmap](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/roadmap.md)**.

La propuesta vive en `rfc/data-ready-capabilities`. Para revisar archivos y comprobaciones desde un clon:

```sh
git switch rfc/data-ready-capabilities
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
docker compose --profile preflight run --rm --build preflight
```

Este contenedor **solo valida planificación/metadatos**. SUMO Hello es una referencia técnica auxiliar: seis assets upstream fijados por commit/hash, con revisión de referencias y aristas. Todavía faltan admisión del alcance de datos, runtime científico Docker, baseline nativo, comparación MCP y ensayo independiente del agente. No sustituye la aceptación municipal.

La pregunta y el municipio se definen desde el inicio. La prueba final recorre cosecha, preparación, ejecución nativa/MCP, resultado y reproducción independiente; la [plantilla municipal](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/cases/municipal-case-template.md) guía el expediente. Las fuentes candidatas no significan que ya haya datos suficientes. La [propuesta para agentes y skills](https://github.com/polisplexity/urban-mcp/blob/rfc/data-ready-capabilities/docs/agents/day-zero.md) no exige un agente propio ni un archivo SOUL obligatorio.

El proyecto no exige un proveedor de IA ni un lenguaje único para los motores. La licencia de este repositorio no sustituye la de cada software, dataset, peso o servicio conectado.

Para crecer como proyecto libre, publicamos recetas, procedencia, decisiones, errores útiles y métodos de comprobación. Se puede aportar una fuente, una corrección, una reproducción, una traducción o un caso en otro municipio, conservando autoría y licencias originales.
