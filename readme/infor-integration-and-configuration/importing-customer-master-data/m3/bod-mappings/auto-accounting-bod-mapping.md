# Auto Accounting BOD Mapping

Il workflow Auto-Accounting di DocBits consuma due BOD da Infor M3 per arricchire le fatture di costo con dimensioni contabili valide:

- **`Sync.CodeDefinition`** — fornisce l'elenco dei valori validi per dimensione contabile (centro di costo, progetto, gruppo di conti, …).
- **`Sync.ChartOfAccounts`** — fornisce il piano dei conti con il profilo dimensionale associato a ciascun conto.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Riferimento originale della mappatura BOD (PDF)
{% endfile %}

## Sync.CodeDefinition

→ Tabella dati anagrafici DocBits: **m3flexdimension**

#### Caso 1: Lo stesso ID appare in più Dimensioni

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Caso 2: L'ID appare in una singola Dimensione

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Riferimento campi

| Campo DocBits | Descrizione |
|---|---|
| `ID` | Chiave primaria in `m3flexdimension`. Nel **Caso 1** il codice dimensione viene anteposto al `DocumentID/ID` M3 per mantenere univoche le voci quando lo stesso codice appare in dimensioni diverse; il **Caso 2** usa l'ID M3 grezzo. |
| `Dimension` | Nome della dimensione (es. centro di costo, progetto). Estratto da `CodeValue/@listID` tramite `substring(..., 21)` — vedi la nota sotto. |
| `ListID` | Valore `ListID` completo e non tagliato. Conservato accanto a `Dimension` affinché il prefisso namespace originale resti disponibile per audit e strumenti downstream. |
| `CodeValue` | Valore effettivo del codice dimensione (es. numero centro di costo `1000`). |
| `Description` | Descrizione leggibile del codice (es. "Marketing"). |

### Sull'espressione `substring(..., 21)`

Il secondo argomento della funzione XPath `substring()` è una posizione di inizio in base 1. M3 emette `@listID` con un prefisso tipo namespace di 20 caratteri (ad esempio `lng.m3.dimension.D1`), quindi `substring(value, 21)` restituisce il codice dimensione dopo quel prefisso (`D1` nell'esempio). Se il tuo M3 emette un prefisso di lunghezza diversa, l'offset deve essere regolato — contattaci con un BOD di esempio prima di configurare Auto-Accounting su un tenant non standard.

### Come le dimensioni alimentano le fatture di costo

Quando una fattura viene classificata come fattura di costo, DocBits propone righe contabili basate sul piano dei conti (vedi sotto). Per ciascuna dimensione richiesta dal conto proposto, l'UI offre i valori salvati in `m3flexdimension` — pre-popolati dagli ultimi BOD `Sync.CodeDefinition`. L'utente AP sceglie il valore corretto o accetta il suggerimento automatico, e il risultato viene esportato verso M3 tramite il BOD `Sync.SupplierInvoice` corrispondente.

## Sync.ChartOfAccounts

→ Tabella dati anagrafici DocBits: **ChartOfAccounts**

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
