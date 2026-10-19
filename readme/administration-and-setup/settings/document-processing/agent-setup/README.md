# Agent Setup

<figure><img src="../../../../.gitbook/assets/agent_setup.png" alt="Agent Setup"><figcaption><p>Página de Agent Setup (Automation Hub)</p></figcaption></figure>

La página Agent Setup (Automation Hub) le permite gestionar agentes basados en IA que automatizan tareas dentro de DocBits. Se divide en dos pestañas: **Agents** y **Channels**.

## Pestaña Agents

### Your Agents

Agentes personalizados que usted crea para su organización. Haga clic en **+ Create Agent** para crear uno nuevo.

### System Agents

Agentes predefinidos proporcionados por DocBits. Cada uno se puede establecer como **Active** o **Inactive**:

| Agente | Descripción |
|-------|-------------|
| **System Router** | Enruta los mensajes del chat al agente especializado adecuado. Siempre activo y con la máxima prioridad. |
| **Document Status Agent** | Proporciona estadísticas de documentos, incluidos recuentos, estado de validación y resumen del procesamiento. |
| **Email Setup Wizard** | Asistente de varios pasos para configurar importaciones de correo electrónico (Gmail, Outlook, Yahoo). |
| **FTP Setup Agent** | Gestiona la configuración, la resolución de problemas y la supervisión de la importación por FTP. |
| **Invoice Validator** | Valida que los campos de la factura estén completos y sean correctos (importes, fechas, datos del proveedor). |
| **Usage Credits Agent** | Informa sobre el saldo de créditos, el uso de tokens y las estadísticas de consumo. |
| **PO Match Assistant** | Ayuda a hacer coincidir facturas con pedidos de compra e identifica discrepancias. |
| **Scheduled Report Agent** | Genera informes periódicos sobre las métricas de procesamiento de documentos. |
| **Integration Setup Wizard** | Guía la configuración de los canales de notificación (Teams, Slack, WhatsApp, Telegram). |
| **DocBits Guide** | Responde preguntas sobre DocBits utilizando la documentación técnica. |

Cada tarjeta de agente muestra su estado y un botón **Details** para ver o configurar el agente.

## Pestaña Channels

Configure los canales de notificación (p. ej., Microsoft Teams, Slack, Telegram) que los agentes pueden utilizar para enviar alertas e informes automatizados.
