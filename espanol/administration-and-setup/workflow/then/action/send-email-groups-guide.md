# Send Email to Groups

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Información de versión

**Estado:** ✅ Versión única (sin cambios incompatibles)
**Última versión:** v1 (Activa)
**Nota:** Esta tarjeta utiliza un modelo de versión única con soporte multilingüe mediante claves de traducción.

📖 [Complete Card Database](../../../../DocFlow/docs/card_version.md)

---

## Propósito
Esta tarjeta envía automáticamente notificaciones por correo electrónico a grupos de usuarios. En lugar de asignar el trabajo a personas individuales, envía el mensaje a un grupo y todos los miembros de ese grupo lo reciben.

**Ejemplo real:** Cuando llega una factura de alto valor, envíe automáticamente una notificación por correo electrónico a todos los miembros del grupo "Finance Team" para que sepan que necesita revisión.

---

## Cuándo usar esta tarjeta

Use esta tarjeta cuando necesite:
- Notificar a varias personas a la vez
- Enviar alertas a grupos de equipo
- Difundir actualizaciones a departamentos
- Notificar a grupos sobre cambios en el estado de los documentos
- Enviar recordatorios a los miembros de un grupo

**Escenarios comunes:**
- Notificar al equipo de compras sobre nuevos proveedores
- Alertar al equipo financiero sobre facturas de alto valor
- Notificar al equipo de almacén sobre los envíos
- Difundir cambios en el estado de los documentos

---

## Cómo funciona

1. **Comprobación de condiciones**: El flujo de trabajo comprueba las condiciones "Where" y "And"
2. **Preparar el correo electrónico**: El sistema prepara el correo electrónico usando una plantilla
3. **Obtener los miembros del grupo**: El sistema encuentra a todos los miembros del grupo especificado
4. **Enviar**: El correo electrónico se envía a cada miembro del grupo
5. **Registrar**: Se registra el envío del correo electrónico

---

## Explicación de los parámetros

### Email Template
El mensaje de correo electrónico que se va a enviar

**Opciones:**
- Elija entre las plantillas existentes
- Cada plantilla tiene un asunto, un cuerpo y un formato predefinidos
- Las plantillas pueden incluir marcadores de posición como {document_number}, {supplier_name}

**Plantilla de ejemplo:**
```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Group
El grupo de usuarios al que enviar el correo electrónico

**Grupos de ejemplo:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Pasos de configuración

### Paso 1: Elegir la plantilla de correo electrónico
1. Haga clic en "Select Email Template"
2. Elija la plantilla de la lista
3. Verifique el asunto y el contenido

### Paso 2: Seleccionar el grupo
1. Haga clic en "Select Group"
2. Elija el grupo que desea notificar
3. Verifique los miembros del grupo (normalmente muestra el recuento)

### Paso 3: Establecer las condiciones
1. Añada una condición: "When [condition] is true"
2. Ejemplo: "When invoice amount is greater than €5000"

### Paso 4: Probar
1. Pruebe con un documento de muestra
2. Verifique que el correo electrónico se envía al grupo
3. Compruebe la representación de la plantilla

---

## Ejemplos de plantillas de correo electrónico

### Plantilla 1: Alerta de factura de alto valor
```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Plantilla 2: Cambio de estado del proveedor
```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Plantilla 3: Documento listo para exportar
```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

---

## Casos de uso comunes

### Caso de uso 1: Alertas de control de calidad
**Disparador:** Cuando se encuentra una discrepancia entre la factura y el PO

**Grupo de correo electrónico:** Quality Team

**Contenido:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Caso de uso 2: Notificaciones de aprobación
**Disparador:** Cuando el documento alcanza un determinado estado

**Grupo de correo electrónico:** Approval Committee

**Contenido:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Caso de uso 3: Notificaciones de excepción
**Disparador:** Cuando no se cumplen las condiciones

**Grupo de correo electrónico:** Managers

**Contenido:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Caso de uso 4: Actualizaciones de estado
**Disparador:** Cuando cambia el estado del documento

**Grupo de correo electrónico:** Equipo responsable del siguiente paso

**Contenido:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Resolución de problemas

### "Email not received"

**Posibles causas:**
- [ ] Los usuarios del grupo no tienen direcciones de correo electrónico
- [ ] El correo electrónico fue bloqueado por el filtro de spam
- [ ] La dirección de correo electrónico es incorrecta en el grupo
- [ ] El grupo no tiene miembros

**Soluciones:**
1. Verifique que todos los miembros del grupo tienen direcciones de correo electrónico
2. Compruebe la carpeta de spam/correo no deseado
3. Verifique que la pertenencia al grupo es correcta
4. Añada usuarios al grupo si faltan
5. Compruebe con TI que el servicio de correo electrónico funciona

### "Template not rendering correctly"

**Causa:** No se encuentran las variables de marcador de posición

**Solución:**
- [ ] Verifique que los nombres de los campos coinciden exactamente
- [ ] Compruebe si el campo tiene un valor en el documento
- [ ] Use el formato de marcador de posición correcto: {field_name}
- [ ] Pruebe con un documento de muestra que tenga todos los campos

### "Algunas personas reciben el correo electrónico y otras no"

**Causa:** Pertenencia incompleta al grupo o correos electrónicos no válidos

**Soluciones:**
- [ ] Verifique que todos los miembros tienen un correo electrónico válido
- [ ] Compruebe si algunos usuarios se han dado de baja
- [ ] Verifique que la pertenencia al grupo está actualizada
- [ ] Contacte con TI para validar las direcciones de correo electrónico

### "Desea añadir/eliminar personas del grupo"

**Solución:**
- Contacte con su administrador
- Los grupos se gestionan en la configuración del sistema
- No se pueden cambiar desde esta tarjeta
- Solicite cambios en la pertenencia al grupo a TI

---

## Personalización de la plantilla de correo electrónico

### Marcadores de posición disponibles
```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Creación de marcadores de posición personalizados
Si necesita datos adicionales en los correos electrónicos:
1. Contacte con su administrador
2. Solicite un nuevo marcador de posición
3. Añada el campo necesario al documento
4. Actualice la plantilla de correo electrónico

---

## Buenas prácticas

✅ **Haga:**
- Mantenga el contenido del correo electrónico breve y claro
- Incluya elementos de acción (¿qué deben hacer los destinatarios?)
- Incluya un enlace o instrucciones para acceder al documento
- Pruebe la plantilla con datos de muestra
- Envíe al grupo correcto (no notifique en exceso)
- Use plantillas para mantener la coherencia

❌ **No haga:**
- Enviar demasiados correos electrónicos (fatiga de notificaciones)
- Incluir datos confidenciales en los correos electrónicos
- Enviar a grupos que no necesitan la información
- Usar líneas de asunto poco claras
- Olvidar incluir cómo realizar la acción
- Enviar correos electrónicos a personas individuales (use un grupo en su lugar)

---

## Notas de rendimiento

- Cada correo electrónico tarda ~1 segundo en enviarse
- Los grupos grandes pueden tardar tiempo (100 personas = ~100 segundos)
- No cree bucles que envíen miles de correos electrónicos
- Supervise la capacidad del servicio de correo electrónico
- Considere el envío por lotes si hay muchos documentos

---

## Tarjetas relacionadas

- **ACTION_SEND_EMAIL** - Enviar a una persona individual
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Asignar una tarea en lugar de solo notificar
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Crear una tarea y notificar
- **STAUS_CHANGE** - Cambiar el estado y notificar

---

## Ejemplo de flujo de trabajo típico

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

---

## Preguntas frecuentes

**P: ¿Puedo enviar a varios grupos?**
R: Cree tarjetas separadas para cada grupo

**P: ¿Qué ocurre si el correo electrónico de alguien rebota?**
R: El correo electrónico se registra como fallido; TI puede solucionar el problema

**P: ¿Puedo cambiar la plantilla de correo electrónico?**
R: Contacte con su administrador para modificar las plantillas

**P: ¿Puedo enviar según condiciones?**
R: ¡Sí! Use las condiciones "Where" y "And" para controlar cuándo se envían los correos electrónicos

**P: ¿Cómo sé si se recibió el correo electrónico?**
R: Compruebe los registros de correo electrónico en DocBits para ver el estado de envío
