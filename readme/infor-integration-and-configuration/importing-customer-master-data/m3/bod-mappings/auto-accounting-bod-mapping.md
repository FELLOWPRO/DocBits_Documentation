# Auto Accounting BOD Mapping

El flujo de Auto-Accounting de DocBits consume dos BODs de Infor M3 para enriquecer las facturas de coste con dimensiones contables válidas:

- **`Sync.CodeDefinition`** — suministra la lista de valores válidos por dimensión contable (centro de coste, proyecto, grupo de cuentas, …).
- **`Sync.ChartOfAccounts`** — suministra el plan de cuentas junto con el perfil de dimensiones asignado a cada cuenta.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Referencia original del mapeo BOD (PDF)
{% endfile %}

## Sync.CodeDefinition

→ Tabla de datos maestros de DocBits: **m3flexdimension**

#### Caso 1: El mismo ID aparece en múltiples Dimensiones

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Caso 2: El ID aparece en una sola Dimensión

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Referencia de campos

| Campo de DocBits | Descripción |
|---|---|
| `ID` | Clave primaria en `m3flexdimension`. En el **Caso 1** se antepone el código de dimensión al `DocumentID/ID` de M3 para mantener únicas las entradas cuando el mismo código aparece en diferentes dimensiones; el **Caso 2** usa el ID puro de M3. |
| `Dimension` | Nombre de la dimensión (p. ej. centro de coste, proyecto). Se extrae de `CodeValue/@listID` mediante `substring(..., 21)` — ver la nota más abajo. |
| `ListID` | Valor completo y sin recortar de `ListID`. Se conserva junto con `Dimension` para que el prefijo de espacio de nombres original quede disponible para auditoría y herramientas downstream. |
| `CodeValue` | Valor real del código de dimensión (p. ej. número de centro de coste `1000`). |
| `Description` | Descripción legible del código (p. ej. "Marketing"). |

### Acerca de la expresión `substring(..., 21)`

El segundo argumento de la función XPath `substring()` es una posición de inicio en base 1. M3 emite `@listID` con un prefijo tipo espacio de nombres de 20 caracteres (por ejemplo `lng.m3.dimension.D1`), de modo que `substring(value, 21)` devuelve el código de dimensión tras ese prefijo (`D1` en el ejemplo). Si su M3 emite un prefijo de longitud diferente, el offset debe ajustarse — por favor envíenos un BOD de ejemplo antes de configurar Auto-Accounting contra un tenant no estándar.

### Cómo las dimensiones alimentan las facturas de coste

Cuando una factura se clasifica como factura de coste, DocBits propone líneas contables basadas en el plan de cuentas (ver más abajo). Para cada dimensión requerida por la cuenta nominal propuesta, la UI ofrece los valores almacenados en `m3flexdimension` — pre-llenados a partir de los últimos BODs `Sync.CodeDefinition`. El usuario AP elige el valor correcto o acepta la sugerencia automática, y el resultado se exporta de vuelta a M3 con el BOD `Sync.SupplierInvoice` correspondiente.

## Sync.ChartOfAccounts

→ Tabla de datos maestros de DocBits: **ChartOfAccounts**

```json
{
    "ID": "//DataArea/ChartOfAccounts/IDs/ID",
    "NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
    "AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
    "Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
    "DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
    "Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
    "Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
    "Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
    "Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
    "Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
    "Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
    "Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
    "Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
    "Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
    "Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
    "Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
    "Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
    "Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
    "Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
}
```
