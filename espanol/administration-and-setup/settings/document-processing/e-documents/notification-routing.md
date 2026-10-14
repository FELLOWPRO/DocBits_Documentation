# Enrutamiento de notificaciones

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Rutas de notificación"><figcaption><p>Asignación de hallazgos de validación a agentes</p></figcaption></figure>

La página **Enrutamiento de notificaciones** (**Documentos electrónicos → Acciones**) asigna los hallazgos de validación a los **agentes de AI Workforce**. Cada hallazgo bloqueante activa exactamente un agente: aquel cuyo prefijo de código coincide más. Todo lo que no coincida recae en el agente de notificación al proveedor predeterminado.

## Rutas de notificación

Elija quién gestiona cada tipo de problema de factura. Todo lo que no figure va al agente predeterminado:

| Ruta | Hallazgos que cubre |
|------|---------------------|
| **Reglas de negocio colombianas** | Hallazgos de reglas de negocio específicas de Colombia. |
| **Reglas de negocio alemanas** | Hallazgos de reglas de negocio específicas de Alemania. |
| **Comprobaciones de IBAN / cuenta bancaria** | Hallazgos de datos de pago (suma de control del IBAN, longitud, país). |
| **Comprobaciones de NIF-IVA** | Hallazgos sobre el formato del NIF-IVA. |
| **Todo lo demás** | El respaldo predeterminado para todo lo no coincidente. |

Para cada ruta, elija el agente responsable en el menú desplegable. **Avanzado (reglas de código personalizadas)** permite enrutar por un código de hallazgo exacto cuando necesita un control más fino.

## Agentes disponibles

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registro de agentes disponibles"><figcaption><p>Registro de solo lectura de los agentes de AI Workforce</p></figcaption></figure>

La sección **Agentes disponibles** es un registro de solo lectura de los agentes de AI Workforce incluidos en su implementación, por ejemplo:

| Agente | Finalidad |
|--------|-----------|
| **Notificación de proveedor predeterminada** | Correo genérico de notificación al proveedor; el agente comodín cuando ningún agente más específico coincide. |
| **Banking Bot** | Plantilla especializada para hallazgos de datos de pago (correcciones de IBAN/BIC). |
| **Tax Bot** | Notificación al proveedor específica para NIF-IVA. |
| **Compliance Bot** | Gestiona los hallazgos de cumplimiento. |

Cada agente muestra su tarea de Celery y los prefijos de código de hallazgo que gestiona de forma predeterminada.
