# Auto Accounting BOD Mapping

DocBits' auto-accounting workflow consumes two BODs from Infor M3 to enrich cost invoices with valid accounting dimensions:

- **`Sync.CodeDefinition`** — supplies the list of valid values per accounting dimension (cost centre, project, account group, …).
- **`Sync.ChartOfAccounts`** — supplies the chart of accounts together with the dimension profile attached to each account.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — original BOD mapping reference (PDF)
{% endfile %}

## Sync.CodeDefinition

→ DocBits Master Data Lookup Table: **m3flexdimension**

#### Case 1: Same ID occurs in multiple Dimensions

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Case 2: ID occurs in a single Dimension

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Field reference

| DocBits field | Description |
|---|---|
| `ID` | Primary key in `m3flexdimension`. In **Case 1** the dimension code is prefixed onto the M3 `DocumentID/ID` to keep entries unique when the same code occurs in different dimensions; **Case 2** uses the raw M3 ID. |
| `Dimension` | Dimension name (e.g. cost centre, project). Extracted from `CodeValue/@listID` via `substring(..., 21)` — see the note below. |
| `ListID` | Full, unstripped `ListID` value. Kept alongside `Dimension` so the original namespace prefix is retained for audit and downstream tools. |
| `CodeValue` | The actual dimension code value (e.g. cost-centre number `1000`). |
| `Description` | Human-readable description of the code (e.g. "Marketing"). |

### About the `substring(..., 21)` expression

The second argument to XPath's `substring()` is a 1-based start position. M3 emits `@listID` with a namespace-style prefix of 20 characters (for example `lng.m3.dimension.D1`), so `substring(value, 21)` returns the dimension code after that prefix (`D1` in the example). If your M3 emits a different prefix length, the offset has to be adjusted — please share an example BOD before configuring auto-accounting against a non-standard tenant.

### How the dimensions feed into cost invoices

When an invoice is classified as a cost invoice, DocBits proposes accounting lines based on the chart of accounts (see below). For each dimension required by the proposed nominal account, the UI offers the values stored in `m3flexdimension` — pre-populated from the latest `Sync.CodeDefinition` BODs. The AP user picks the right value or accepts the auto-suggestion, and the result is exported back to M3 with the corresponding `Sync.SupplierInvoice` BOD.

## Sync.ChartOfAccounts

→ DocBits Master Data Lookup Table: **ChartOfAccounts**

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
