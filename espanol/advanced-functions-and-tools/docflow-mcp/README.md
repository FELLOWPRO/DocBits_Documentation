# DocFlow MCP

DocFlow expone un servidor **Model Context Protocol (MCP)** que permite a los asistentes de IA gestionar flujos de trabajo y tarjetas de socios de forma programática. Cualquier cliente compatible con MCP — Claude Code, Claude Desktop, OpenAI Codex o integraciones personalizadas — puede conectarse y utilizar estas herramientas.

## ¿Qué puedes hacer?

Con DocFlow MCP puedes:

- **Listar, crear, actualizar y eliminar** flujos de trabajo avanzados
- **Probar flujos de trabajo** con documentos reales o simulados
- **Crear tarjetas personalizadas** usando el Partner Card SDK
- **Validar, probar, aprobar y gestionar** envíos de tarjetas de socios
- **Importar tarjetas** directamente desde repositorios de GitHub

## Resumen de herramientas

DocFlow MCP proporciona **18 herramientas** en cuatro categorías:

### Gestión de flujos de trabajo

| Herramienta | Descripción |
|------|-------------|
| `list_workflows` | Listar todos los flujos de trabajo de la organización actual |
| `get_workflow` | Obtener detalles de un flujo de trabajo específico por ID |
| `delete_workflow` | Eliminar un flujo de trabajo por ID |

### Pruebas de flujos de trabajo

| Herramienta | Descripción |
|------|-------------|
| `test_advanced_workflow` | Probar la ejecución de un flujo de trabajo avanzado con documento opcional |
| `list_test_scenarios` | Listar todos los escenarios de prueba de flujos de trabajo |
| `list_cards` | Listar las tarjetas/acciones de flujo de trabajo disponibles |

### Gestión del Card SDK

| Herramienta | Descripción |
|------|-------------|
| `sdk_list_submissions` | Listar todos los envíos de tarjetas de socios |
| `sdk_get_submission_status` | Obtener el estado de validación de un envío |
| `sdk_approve_card` | Aprobar una tarjeta de socio validada (admin) |
| `sdk_reject_card` | Rechazar un envío de tarjeta de socio (admin) |
| `sdk_delete_submission` | Desactivar o eliminar un envío (admin) |
| `sdk_list_cards_picker` | Listar todas las tarjetas habilitadas con indicadores de rol |

### Desarrollo del Card SDK

| Herramienta | Descripción |
|------|-------------|
| `sdk_create_card` | Crear una nueva tarjeta de socio a partir de código fuente |
| `sdk_validate_card` | Ejecutar validación de 5 etapas sin guardar |
| `sdk_test_card` | Ejecutar una tarjeta en un entorno aislado (sandbox) |
| `sdk_import_github` | Importar una aplicación de socio desde GitHub |

## Primeros pasos

1. [Configura tu cliente MCP](setup-and-configuration.md)
2. Aprende sobre las [Herramientas de flujos de trabajo](workflow-tools.md)
3. Explora las [Herramientas del Card SDK](card-sdk-tools.md)
4. Sigue los [Ejemplos](examples.md) de principio a fin

{% hint style="info" %}
DocFlow MCP utiliza transporte **Streamable HTTP**. El endpoint del servidor es `/api/mcp/` en tu host de la API de DocBits.
{% endhint %}
