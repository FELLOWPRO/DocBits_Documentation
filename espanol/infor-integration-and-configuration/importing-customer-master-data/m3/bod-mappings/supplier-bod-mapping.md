# Supplier BOD Mapping

Esta página documenta cómo DocBits ingiere los datos maestros de proveedores de Infor M3 a través de los BODs `SyncSupplierPartyMaster` y `SyncRemitToPartyMaster`. Ambos BODs llenan la misma tabla de datos maestros `SUPPLIER` en DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Referencia original del mapeo BOD (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Referencia original del mapeo BOD (PDF)
{% endfile %}

## Principios clave

- **CONO + SUNO es la clave de coincidencia.** Una fila de `supplier_header` en DocBits se identifica de manera única por `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Esto permite que una sola organización DocBits consolide múltiples empresas M3.
- **`variationID` protege contra BODs fuera de orden.** M3 puede emitir el mismo registro maestro varias veces en rápida sucesión; la `variationID` entrante debe ser mayor que la almacenada para que un update sea aceptado. Ambos BODs trackean su `variationID` de forma independiente (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Sin sobrescritura silenciosa.** SupplierPartyMaster y RemitToPartyMaster comparten varios campos (nombre, teléfono, IVA, banco, estado). Cada BOD actualiza sólo los campos que posee y sólo si su `variationID` avanza. Dentro del conjunto compartido, gana el BOD recibido más recientemente (por tipo de BOD).
- **El multi-banco se controla mediante preferencia.** Comportamiento por defecto: la última `FinancialParty` se escribe en `bank_id` en la cabecera. Con la preferencia `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` activada, cada entrada `FinancialParty` se persiste en `supplier_account` (IBAN, ID de cuenta, código de moneda, indicador de preferencia).
- **Recorte opcional del sufijo CONO.** Algunas instalaciones M3 añaden un sufijo de división al número de empresa (p. ej. `100_01`). La preferencia `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` corta los sufijos `_*` para mantener las claves DocBits consistentes. Tenga en cuenta que con el recorte activado, múltiples BODs RemitToPartyMaster por división colapsan en una única clave de coincidencia — y gana el BOD con la `variationID` más alta. Vea la FAQ "*¿Qué ocurre cuando se emite un BOD RemitToPartyMaster por división?*" más abajo.

## Sync.SupplierPartyMaster

→ Tabla de datos maestros de DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Referencia de campos

| Campo de DocBits | Origen en M3 | Descripción |
|---|---|---|
| `sharedCONO` | Número de empresa de M3 | Mapea a `customer_number` en `supplier_header`. Parte de la clave de coincidencia. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | Número de proveedor de M3. Parte de la clave de coincidencia. |
| `variationID` | Atributo del BOD | Se almacena como `variation_id_supplier_bod`. Los BODs entrantes sólo se aceptan si su `variationID` supera la almacenada. Un atributo ausente se trata como `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Nombre de visualización del proveedor. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Número de teléfono del canal de comunicación `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | Identificador IVA. Se lee de `PartyIDs/TaxID` (sin filtro `@schemeName` en la ruta de ingesta M3). **PENDIENTE** — cuando M3 emite múltiples elementos `TaxID` con distintos valores de `@schemeName` (p. ej. `VatCode`, `TaxIdentificationNumber`), gana la primera ocurrencia. Está planificado un filtro `schemeName` configurable; comparta un BOD de ejemplo para definir el default correcto. <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | Identificador de condiciones de pago. |
| `paymentMethodCode` | — | Código de método de pago, cuando se suministra. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Referencia (usuario M3) y nombre del comprador asignado. |
| `supplier_category` | — | Se lee de `Classification/Codes/Code[@listID='Supplier Categories']`. Extensión UserArea opcional; queda NULL en instalaciones M3 estándar. |
| `supplier_group` | `CIDVEN.IISUCL` | Grupo de clasificación del proveedor. |
| `discount_terms_description` | — | Extensión UserArea opcional (`eam.UDFCHAR06`) usada por la lógica de fecha de descuento de DocBits. Cuando el proveedor entrega aquí un valor de días de descuento, DocBits lo combina con la fecha de factura para producir una fecha de vencimiento de descuento para el equipo AP. |
| `status` | `CIDMAS.IDSTAT` | Estado activo/inactivo del proveedor, tomado de `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Cuenta bancaria por defecto, tomada de la *última* `FinancialParty`. Active `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` para sincronizar cada `FinancialParty` en la tabla `supplier_account`. |

## Sync.RemitToPartyMaster

→ Tabla de datos maestros de DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Referencia de campos

| Campo de DocBits | Origen en M3 | Descripción |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | Empresa M3 / `CIDMAS.IDSUNO` | Misma semántica que en `SupplierPartyMaster`. Se une a la misma fila `supplier_header`. |
| `variationID` | Atributo del BOD | Se almacena como `variation_id_remit_to_party` — trackeada de forma independiente del `variationID` de SupplierPartyMaster. |
| `supplierName` | `CIDMAS.IDSUNM` | Nombre de visualización de la parte remit-to. Escribe en la columna compartida `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Número de teléfono del bloque de comunicación remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | Identificador IVA de la parte remit-to. Misma limitación de `@schemeName` que en SupplierPartyMaster — gana la primera ocurrencia. <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | Cuenta bancaria remit-to (`FinancialParty[last()]`). Aplica la misma preferencia multi-banco. |
| `status` | `CIDMAS.IDSTAT` | Estado activo/inactivo de la parte remit-to. |

## Cómo interactúan los dos BODs sobre la tabla `SUPPLIER` compartida

Ambos BODs llenan la misma fila `supplier_header`. Para los campos que comparten (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits aplica las siguientes reglas:

1. Encontrar la fila por `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Comparar la `variationID` entrante con la `variationID` almacenada *para el mismo tipo de BOD*.
3. Si la `variationID` entrante es mayor (o `0`, force-update), actualizar los campos que posee ese BOD. De lo contrario, descartar el BOD.
4. La `variationID` del otro tipo de BOD no se toca y sus valores previamente almacenados permanecen.

Las filas `supplier_address` y `supplier_account` asociadas al proveedor se eliminan y reinsertan al actualizar, de modo que las tablas secundarias siempre reflejan el BOD más reciente. Esto tiene un efecto colateral cuando M3 emite un BOD RemitToPartyMaster *por división* (algunos tenants lo hacen cuando las conexiones bancarias se mantienen tanto en una división vacía como en divisiones específicas): después de que `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` elimina el sufijo de división, cada BOD por división apunta a la misma clave `(customer_number, supplier_number)`. Gana el BOD con la `variationID` más alta. Si ese BOD "ganador" pertenece a una división sin conexiones bancarias, las cuentas bancarias del BOD anterior se borran en el re-insert.

## Preguntas frecuentes

### ¿Por qué DocBits trackea CONO si todos mis proveedores vienen de una sola empresa M3?

El enrutamiento CONO es obligatorio porque DocBits es multi-tenant por diseño: una organización puede ingerir BODs de múltiples empresas M3. CONO es parte de la clave de coincidencia para que los proveedores de empresas distintas no colisionen. Si sólo tiene una empresa puede ignorar el valor, pero la columna clave se llena igual.

### Ambos BODs escriben en la misma fila de proveedor — ¿el último BOD sobrescribe todo?

No. Cada tipo de BOD posee sólo los campos que envía, y los updates se controlan mediante una `variationID` independiente. Un SupplierPartyMaster que cambia sólo el nombre del proveedor no revierte el número de teléfono que un RemitToPartyMaster posterior haya escrito.

### `Supplier Categories` y `eam.UDFCHAR06` nunca son entregados por mi M3 — ¿qué hago?

Ambas son extensiones UserArea opcionales. Sin la extensión las columnas quedan NULL y ninguna función de DocBits depende de ellas. Active la lógica de fecha de descuento sólo cuando su M3 esté configurado para emitir `eam.UDFCHAR06`.

### ¿`vatNo` debe filtrar por `schemeName='TaxIdentificationNumber'`?

La ruta de ingesta BOD de M3 lee actualmente `PartyIDs/TaxID` sin filtro `schemeName`. El filtro se usa en las rutas XSLT de e-factura (Facturae, XRechnung, KSeF), no en la ingesta M3. Cuando M3 emite múltiples elementos `TaxID` con distintos valores de `@schemeName`, gana la primera ocurrencia — lo que puede producir identificadores IVA incorrectos. Está planificado un filtro configurable; un BOD de ejemplo de su tenant nos ayuda a definir el `schemeName` default correcto. <!-- tracked in DOCB-12313 -->

### ¿Qué ocurre cuando se emite un BOD RemitToPartyMaster por división?

Algunos tenants M3 mantienen conexiones bancarias tanto en una división vacía como en divisiones específicas, lo que provoca que M3 emita un BOD RemitToPartyMaster separado por división. La clave de coincidencia en DocBits es `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — la división no forma parte de ella.

- Con `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` activado, los BODs por división colapsan en la misma fila. Gana el BOD con la `variationID` más alta, y las filas `supplier_account` se reinsertan únicamente desde ese BOD. Si el BOD ganador procede de una división sin conexiones bancarias, las cuentas bancarias almacenadas previamente se borran.
- Con la preferencia desactivada (la CONO mantiene su sufijo de división), los BODs por división apuntan a claves distintas y coexisten.

Si su tenant envía BODs RemitToPartyMaster por división y depende de la lista de bancos consolidada, contáctenos con un ejemplo para planificar una mejora.

### Quiero sincronizar todas las cuentas bancarias del proveedor, no sólo la última. ¿Cómo?

Active la preferencia `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Con el flag activo, cada `FinancialParty` del BOD se persiste en la tabla `supplier_account` (IBAN, ID de cuenta financiera, código de moneda, indicador de preferencia). La columna heredada `bank_id` en la cabecera sigue manteniendo la última entrada por compatibilidad.
