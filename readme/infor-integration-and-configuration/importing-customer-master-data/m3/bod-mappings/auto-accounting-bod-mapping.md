# Auto Accounting BOD Mapping

Przepływ Auto-Accounting DocBits korzysta z dwóch BOD-ów z Infor M3, aby wzbogacić faktury kosztowe o prawidłowe wymiary księgowe:

- **`Sync.CodeDefinition`** — dostarcza listę prawidłowych wartości na wymiar księgowy (centrum kosztów, projekt, grupa kont, …).
- **`Sync.ChartOfAccounts`** — dostarcza plan kont wraz z profilem wymiarów powiązanym z każdym kontem.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Oryginalna referencja mapowania BOD (PDF)
{% endfile %}

## Sync.CodeDefinition

→ Tabela danych głównych DocBits: **m3flexdimension**

#### Przypadek 1: Ten sam ID występuje w wielu wymiarach

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Przypadek 2: ID występuje w pojedynczym wymiarze

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Referencja pól

| Pole DocBits | Opis |
|---|---|
| `ID` | Klucz podstawowy w `m3flexdimension`. W **Przypadku 1** kod wymiaru jest dodawany przed `DocumentID/ID` M3, aby wpisy pozostały unikalne, gdy ten sam kod występuje w różnych wymiarach; **Przypadek 2** używa surowego ID M3. |
| `Dimension` | Nazwa wymiaru (np. centrum kosztów, projekt). Wyciągana z `CodeValue/@listID` przez `substring(..., 21)` — zob. uwagę poniżej. |
| `ListID` | Pełna, nieobcięta wartość `ListID`. Przechowywana obok `Dimension`, aby oryginalny prefiks przestrzeni nazw pozostał dostępny dla audytu i narzędzi downstream. |
| `CodeValue` | Rzeczywista wartość kodu wymiaru (np. numer centrum kosztów `1000`). |
| `Description` | Czytelny opis kodu (np. „Marketing"). |

### O wyrażeniu `substring(..., 21)`

Drugi argument funkcji XPath `substring()` to pozycja początkowa w bazie 1. M3 emituje `@listID` z prefiksem typu przestrzeń nazw o długości 20 znaków (na przykład `lng.m3.dimension.D1`), więc `substring(value, 21)` zwraca kod wymiaru po tym prefiksie (`D1` w przykładzie). Jeśli twój M3 emituje prefiks o innej długości, offset musi zostać dostosowany — prosimy o przykładowy BOD przed konfiguracją Auto-Accounting dla niestandardowego tenanta.

### Jak wymiary trafiają do faktur kosztowych

Gdy faktura zostanie sklasyfikowana jako faktura kosztowa, DocBits proponuje linie księgowe na podstawie planu kont (zob. poniżej). Dla każdego wymiaru wymaganego przez proponowane konto nominalne UI oferuje wartości przechowywane w `m3flexdimension` — wstępnie zapełnione z ostatnich BOD-ów `Sync.CodeDefinition`. Użytkownik AP wybiera właściwą wartość lub akceptuje automatyczną sugestię, a wynik jest eksportowany z powrotem do M3 odpowiednim BOD-em `Sync.SupplierInvoice`.

## Sync.ChartOfAccounts

→ Tabela danych głównych DocBits: **ChartOfAccounts**

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
