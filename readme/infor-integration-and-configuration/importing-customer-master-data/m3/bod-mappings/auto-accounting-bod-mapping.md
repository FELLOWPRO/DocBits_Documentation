# Auto Accounting BOD Mapping

O fluxo de Auto-Accounting do DocBits consome dois BODs do Infor M3 para enriquecer faturas de custo com dimensões contabilísticas válidas:

- **`Sync.CodeDefinition`** — fornece a lista de valores válidos por dimensão contabilística (centro de custo, projeto, grupo de contas, …).
- **`Sync.ChartOfAccounts`** — fornece o plano de contas juntamente com o perfil dimensional associado a cada conta.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Referência original do mapeamento BOD (PDF)
{% endfile %}

## Sync.CodeDefinition

→ Tabela de dados mestres DocBits: **m3flexdimension**

#### Caso 1: O mesmo ID ocorre em múltiplas Dimensões

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Caso 2: O ID ocorre numa única Dimensão

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Referência dos campos

| Campo DocBits | Descrição |
|---|---|
| `ID` | Chave primária em `m3flexdimension`. No **Caso 1**, o código de dimensão é anteposto ao `DocumentID/ID` M3 para manter as entradas únicas quando o mesmo código aparece em dimensões diferentes; o **Caso 2** usa o ID M3 puro. |
| `Dimension` | Nome da dimensão (ex. centro de custo, projeto). Extraído de `CodeValue/@listID` via `substring(..., 21)` — ver a nota abaixo. |
| `ListID` | Valor completo e não recortado de `ListID`. Mantido ao lado de `Dimension` para que o prefixo de namespace original permaneça disponível para auditoria e ferramentas downstream. |
| `CodeValue` | Valor real do código da dimensão (ex. número de centro de custo `1000`). |
| `Description` | Descrição legível do código (ex. "Marketing"). |

### Sobre a expressão `substring(..., 21)`

O segundo argumento da função XPath `substring()` é uma posição inicial baseada em 1 — **não é** um valor `listID`. O M3 emite `@listID` com um prefixo tipo namespace de 20 caracteres (por exemplo `lng.m3.dimension.D1`), pelo que `substring(value, 21)` devolve o código da dimensão após esse prefixo (`D1` no exemplo). Se o seu M3 emitir um prefixo de comprimento diferente, o offset tem de ser ajustado — contacte-nos com um BOD de exemplo antes de configurar Auto-Accounting num tenant não padrão.

A fonte canónica do valor do código da dimensão é `/SyncCodeDefinition/DataArea/CodeDefinition/DocumentID/ID`. A forma `substring(@listID, 21)` é mantida aqui como fallback para tenants em que `DocumentID/ID` não esteja preenchido. Alinhar o mapeamento para preferir `DocumentID/ID` e filtrar por `CodeDefinitionVariant='Accounting Dimension'` (ver próxima secção) é uma melhoria planeada. <!-- tracked in DOCB-12315 -->

### Que variantes de `CodeDefinition` o DocBits processa?

`Sync.CodeDefinition` é um BOD genérico que o M3 emite para muitos objetos diferentes (dimensões contabilísticas, códigos de estado, listas de classificação …). Para o fluxo de Auto-Accounting, apenas são relevantes as entradas que apresentem `Property/NameValue[@name='CodeDefinitionVariant']='Accounting Dimension'`. Até o processor aplicar este filtro nativamente, recomendamos filtrar por `CodeDefinitionVariant` no seu DataFlow ION antes de o BOD chegar ao DocBits — caso contrário, BODs `CodeDefinition` não-dimensão são ingeridos em `m3flexdimension` e atravancam o seletor na UI das faturas de custo. <!-- tracked in DOCB-12315 -->

### Como as dimensões alimentam as faturas de custo

Quando uma fatura é classificada como fatura de custo, o DocBits propõe linhas contabilísticas com base no plano de contas (ver abaixo). Para cada dimensão exigida pela conta nominal proposta, a UI oferece os valores armazenados em `m3flexdimension` — pré-preenchidos a partir dos últimos BODs `Sync.CodeDefinition`. O utilizador AP escolhe o valor correto ou aceita a sugestão automática, e o resultado é exportado de volta para o M3 com o BOD `Sync.SupplierInvoice` correspondente.

## Sync.ChartOfAccounts

→ Tabela de dados mestres DocBits: **ChartOfAccounts**

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
