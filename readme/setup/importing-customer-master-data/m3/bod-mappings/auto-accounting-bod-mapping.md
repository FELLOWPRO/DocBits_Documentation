# Auto Accounting BOD Mapiranje

DocBits Auto-Accounting tok rada konzumira dva BOD-a iz Infor M3 da obogati troškovne fakture validnim računovodstvenim dimenzijama:

- **`Sync.CodeDefinition`** — pruža listu validnih vrednosti po računovodstvenoj dimenziji (centar troška, projekat, grupa naloga, …).
- **`Sync.ChartOfAccounts`** — pruža kontni plan zajedno sa profilom dimenzija povezanim sa svakim nalogom.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Originalna BOD referenca mapiranja (PDF)
{% endfile %}

## Sync.CodeDefinition

→ DocBits Tabela Matičnih Podataka: **m3flexdimension**

#### Slučaj 1: Isti ID se javlja u više dimenzija

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Slučaj 2: ID se javlja u jednoj dimenziji

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Referenca polja

| DocBits polje | Opis |
|---|---|
| `ID` | Primarni ključ u `m3flexdimension`. U **Slučaju 1**, kod dimenzije se dodaje ispred M3 `DocumentID/ID` da bi unosi ostali jedinstveni kada se isti kod javlja u različitim dimenzijama; **Slučaj 2** koristi sirov M3 ID. |
| `Dimension` | Naziv dimenzije (npr. centar troška, projekat). Izdvojeno iz `CodeValue/@listID` preko `substring(..., 21)` — vidi napomenu ispod. |
| `ListID` | Puna, neisečena vrednost `ListID`. Drži se uz `Dimension` kako bi originalni prefiks imenskog prostora ostao dostupan za reviziju i nizvodne alate. |
| `CodeValue` | Stvarna vrednost koda dimenzije (npr. broj centra troška `1000`). |
| `Description` | Čitljiv opis koda (npr. „Marketing"). |

### O izrazu `substring(..., 21)`

Drugi argument XPath funkcije `substring()` je početna pozicija u bazi 1. M3 emituje `@listID` sa prefiksom tipa imenski prostor dužine 20 znakova (na primer `lng.m3.dimension.D1`), tako da `substring(value, 21)` vraća kod dimenzije nakon tog prefiksa (`D1` u primeru). Ako vaš M3 emituje prefiks druge dužine, offset se mora prilagoditi — molimo kontaktirajte nas sa primerom BOD-a pre konfigurisanja Auto-Accounting-a na nestandardnom tenantu.

### Kako dimenzije ulaze u troškovne fakture

Kada se faktura klasifikuje kao troškovna faktura, DocBits predlaže računovodstvene linije na osnovu kontnog plana (vidi ispod). Za svaku dimenziju koju zahteva predloženi nominalni nalog, UI nudi vrednosti sačuvane u `m3flexdimension` — unapred popunjene iz poslednjih `Sync.CodeDefinition` BOD-ova. AP korisnik bira pravu vrednost ili prihvata automatski predlog, a rezultat se izvozi nazad u M3 odgovarajućim `Sync.SupplierInvoice` BOD-om.

## Sync.ChartOfAccounts

→ DocBits Tabela Matičnih Podataka: **ChartOfAccounts**

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
