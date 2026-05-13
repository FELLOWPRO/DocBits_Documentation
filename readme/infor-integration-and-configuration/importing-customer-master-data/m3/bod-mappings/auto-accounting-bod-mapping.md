# Auto Accounting BOD Mapping

Der DocBits Auto-Accounting-Workflow konsumiert zwei BODs aus Infor M3, um Kostenrechnungen mit gültigen Buchhaltungsdimensionen anzureichern:

- **`Sync.CodeDefinition`** — liefert die Liste der gültigen Werte pro Buchhaltungsdimension (Kostenstelle, Projekt, Kontogruppe, …).
- **`Sync.ChartOfAccounts`** — liefert den Kontenplan zusammen mit dem an jedem Konto hängenden Dimensions-Profil.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Original BOD Mapping Referenz (PDF)
{% endfile %}

## Sync.CodeDefinition

→ DocBits Stammdaten-Tabelle: **m3flexdimension**

#### Fall 1: Gleiche ID kommt in mehreren Dimensionen vor

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Fall 2: ID kommt nur in einer einzigen Dimension vor

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Feldreferenz

| DocBits Feld | Beschreibung |
|---|---|
| `ID` | Primärschlüssel in `m3flexdimension`. In **Fall 1** wird der Dimensions-Code dem M3 `DocumentID/ID` vorangestellt, damit Einträge eindeutig bleiben, wenn derselbe Code in verschiedenen Dimensionen vorkommt; **Fall 2** verwendet die rohe M3-ID. |
| `Dimension` | Dimensionsname (z. B. Kostenstelle, Projekt). Aus `CodeValue/@listID` per `substring(..., 21)` extrahiert — siehe Hinweis unten. |
| `ListID` | Vollständiger, ungeschnittener `ListID`-Wert. Wird zusammen mit `Dimension` gehalten, damit der ursprüngliche Namespace-Präfix für Audit-Zwecke und Downstream-Tools erhalten bleibt. |
| `CodeValue` | Der eigentliche Dimensions-Code (z. B. Kostenstellen-Nummer `1000`). |
| `Description` | Menschenlesbare Beschreibung des Codes (z. B. „Marketing"). |

### Zum Ausdruck `substring(..., 21)`

Das zweite Argument der XPath-Funktion `substring()` ist eine 1-basierte Startposition. M3 emittiert `@listID` mit einem 20 Zeichen langen Namespace-Präfix (zum Beispiel `lng.m3.dimension.D1`), sodass `substring(value, 21)` den Dimensions-Code nach dem Präfix zurückliefert (`D1` im Beispiel). Wenn Ihr M3 einen anderen Präfix verwendet, muss der Offset angepasst werden — kontaktieren Sie uns bitte mit einem Beispiel-BOD, bevor Sie Auto-Accounting gegen einen nicht-standardmäßigen Mandanten konfigurieren.

### Wie die Dimensionen in Kostenrechnungen einfließen

Wenn eine Rechnung als Kostenrechnung klassifiziert wird, schlägt DocBits Buchungszeilen anhand des Kontenplans vor (siehe unten). Für jede vom vorgeschlagenen Sachkonto benötigte Dimension bietet die UI die in `m3flexdimension` hinterlegten Werte zur Auswahl an — vorab gefüllt aus den letzten `Sync.CodeDefinition`-BODs. Der AP-User wählt den richtigen Wert oder bestätigt den Auto-Vorschlag, und das Ergebnis wird mit dem zugehörigen `Sync.SupplierInvoice`-BOD nach M3 zurückgeschickt.

## Sync.ChartOfAccounts

→ DocBits Stammdaten-Tabelle: **ChartOfAccounts**

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
