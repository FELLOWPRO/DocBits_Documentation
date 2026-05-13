# Auto Accounting BOD Mapping

De Auto-Accounting-workflow van DocBits consumeert twee BODs uit Infor M3 om kostenfacturen te verrijken met geldige boekhoudkundige dimensies:

- **`Sync.CodeDefinition`** — levert de lijst met geldige waarden per boekhoudkundige dimensie (kostenplaats, project, rekeninggroep, …).
- **`Sync.ChartOfAccounts`** — levert het rekeningschema samen met het dimensieprofiel dat aan elke rekening hangt.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Oorspronkelijke BOD mapping referentie (PDF)
{% endfile %}

## Sync.CodeDefinition

→ DocBits Stamgegevenstabel: **m3flexdimension**

#### Geval 1: Zelfde ID komt voor in meerdere Dimensies

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Geval 2: ID komt voor in één enkele Dimensie

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Veld-referentie

| DocBits veld | Beschrijving |
|---|---|
| `ID` | Primaire sleutel in `m3flexdimension`. In **Geval 1** wordt de dimensiecode voorgevoegd bij de M3 `DocumentID/ID` om de invoer uniek te houden wanneer dezelfde code in verschillende dimensies voorkomt; **Geval 2** gebruikt het ruwe M3-ID. |
| `Dimension` | Dimensienaam (bv. kostenplaats, project). Geëxtraheerd uit `CodeValue/@listID` via `substring(..., 21)` — zie de opmerking hieronder. |
| `ListID` | Volledige, ongesneden `ListID`-waarde. Wordt naast `Dimension` bewaard zodat het originele namespace-prefix beschikbaar blijft voor audit en downstream-tools. |
| `CodeValue` | De daadwerkelijke waarde van de dimensiecode (bv. kostenplaatsnummer `1000`). |
| `Description` | Leesbare beschrijving van de code (bv. "Marketing"). |

### Over de expressie `substring(..., 21)`

Het tweede argument van de XPath-functie `substring()` is een 1-gebaseerde startpositie. M3 emitteert `@listID` met een namespace-achtig prefix van 20 tekens (bijvoorbeeld `lng.m3.dimension.D1`), zodat `substring(value, 21)` de dimensiecode na dat prefix teruggeeft (`D1` in het voorbeeld). Als jouw M3 een prefix van een andere lengte emitteert, moet de offset worden aangepast — deel a.u.b. een voorbeeld-BOD voordat je Auto-Accounting tegen een niet-standaard tenant configureert.

### Hoe de dimensies in kostenfacturen terechtkomen

Wanneer een factuur als kostenfactuur wordt geclassificeerd, stelt DocBits boekingsregels voor op basis van het rekeningschema (zie hieronder). Voor elke dimensie die de voorgestelde grootboekrekening vereist, biedt de UI de in `m3flexdimension` opgeslagen waarden aan — vooraf gevuld uit de laatste `Sync.CodeDefinition`-BODs. De AP-gebruiker kiest de juiste waarde of accepteert de automatische suggestie, en het resultaat wordt met de bijbehorende `Sync.SupplierInvoice`-BOD terug naar M3 geëxporteerd.

## Sync.ChartOfAccounts

→ DocBits Stamgegevenstabel: **ChartOfAccounts**

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
