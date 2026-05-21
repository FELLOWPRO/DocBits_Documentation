# Supplier BOD Mapping

Esta página documenta como o DocBits ingere os dados mestres de fornecedores do Infor M3 através dos BODs `SyncSupplierPartyMaster` e `SyncRemitToPartyMaster`. Ambos os BODs preenchem a mesma tabela de dados mestres `SUPPLIER` no DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Referência original do mapeamento BOD (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Referência original do mapeamento BOD (PDF)
{% endfile %}

## Princípios-chave

- **CONO + SUNO é a chave de correspondência.** Uma linha `supplier_header` no DocBits é identificada de forma única por `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Isto permite que uma única organização DocBits consolide múltiplas empresas M3.
- **`variationID` protege contra BODs fora de ordem.** O M3 pode emitir o mesmo registo mestre várias vezes em rápida sucessão; o `variationID` recebido tem de ser maior do que o armazenado para que uma atualização seja aceite. Ambos os BODs rastreiam o seu `variationID` de forma independente (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Sem substituição silenciosa.** SupplierPartyMaster e RemitToPartyMaster partilham vários campos (nome, telefone, NIF, banco, status). Cada BOD apenas atualiza os campos que possui e apenas se o seu `variationID` avançar. Dentro do conjunto partilhado, vence o BOD recebido mais recentemente (por tipo de BOD).
- **A sincronização multi-banco é controlada por preferência.** Comportamento padrão: a última `FinancialParty` é escrita em `bank_id` no cabeçalho. Com a preferência `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` ativa, cada entrada `FinancialParty` é persistida em `supplier_account` (IBAN, ID da conta, código de moeda, indicador de preferência).
- **Recorte opcional do sufixo CONO.** Algumas instalações M3 adicionam um sufixo de divisão ao número de empresa (ex. `100_01`). A preferência `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` corta sufixos `_*` para manter as chaves do DocBits consistentes. Atenção: com o recorte ativo, vários BODs RemitToPartyMaster emitidos por divisão colapsam numa única chave de correspondência — e vence o BOD com o `variationID` mais alto. Ver a FAQ "*O que acontece quando é emitido um BOD RemitToPartyMaster por divisão?*" abaixo.

## Sync.SupplierPartyMaster

→ Tabela de dados mestres DocBits: **SUPPLIER**

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

### Referência dos campos

| Campo DocBits | Origem M3 | Descrição |
|---|---|---|
| `sharedCONO` | Número de empresa M3 | Mapeia para `customer_number` em `supplier_header`. Parte da chave de correspondência. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | Número de fornecedor M3. Parte da chave de correspondência. |
| `variationID` | Atributo do BOD | Armazenado como `variation_id_supplier_bod`. BODs recebidos só são aceites se o seu `variationID` exceder o armazenado. Um atributo ausente é tratado como `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Nome de exibição do fornecedor. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Número de telefone do canal de comunicação `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | Identificador IVA. Lido de `PartyIDs/TaxID` (sem filtro `@schemeName` no caminho de ingestão M3). **EM ABERTO** — quando o M3 emite vários elementos `TaxID` com diferentes valores `@schemeName` (ex. `VatCode`, `TaxIdentificationNumber`), vence a primeira ocorrência. Está planeado um filtro `schemeName` configurável; partilhe um BOD de exemplo para definirmos o default correto. <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | Identificador de condições de pagamento. |
| `paymentMethodCode` | — | Código do método de pagamento, quando fornecido. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Comprador atribuído (referência de utilizador M3 e nome de exibição). |
| `supplier_category` | — | Lido de `Classification/Codes/Code[@listID='Supplier Categories']`. Extensão UserArea opcional; permanece NULL em instalações M3 padrão. |
| `supplier_group` | `CIDVEN.IISUCL` | Grupo de classificação do fornecedor. |
| `discount_terms_description` | — | Extensão UserArea opcional (`eam.UDFCHAR06`) usada pela lógica de data de desconto do DocBits. Quando o fornecedor envia aqui um valor de dias de desconto, o DocBits combina-o com a data da fatura para produzir uma data de vencimento de desconto para a equipa AP. |
| `status` | `CIDMAS.IDSTAT` | Status ativo/inativo do fornecedor, obtido de `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Conta bancária por defeito, obtida da *última* `FinancialParty`. Ative `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` para sincronizar cada `FinancialParty` na tabela `supplier_account`. |

## Sync.RemitToPartyMaster

→ Tabela de dados mestres DocBits: **SUPPLIER**

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

### Referência dos campos

| Campo DocBits | Origem M3 | Descrição |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | Empresa M3 / `CIDMAS.IDSUNO` | Mesma semântica de `SupplierPartyMaster`. Liga-se à mesma linha `supplier_header`. |
| `variationID` | Atributo do BOD | Armazenado como `variation_id_remit_to_party` — rastreado de forma independente do `variationID` do SupplierPartyMaster. |
| `supplierName` | `CIDMAS.IDSUNM` | Nome de exibição da parte remit-to. Escreve na coluna partilhada `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Número de telefone do bloco de comunicação remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | Identificador IVA da parte remit-to. Mesma limitação `@schemeName` que no SupplierPartyMaster — vence a primeira ocorrência. <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | Conta bancária remit-to (`FinancialParty[last()]`). Aplica-se a mesma preferência multi-banco. |
| `status` | `CIDMAS.IDSTAT` | Status ativo/inativo da parte remit-to. |

## Como os dois BODs interagem na tabela `SUPPLIER` partilhada

Ambos os BODs preenchem a mesma linha `supplier_header`. Para os campos partilhados (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), o DocBits aplica as seguintes regras:

1. Localizar a linha por `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Comparar o `variationID` recebido com o `variationID` armazenado *para o mesmo tipo de BOD*.
3. Se o `variationID` recebido for maior (ou `0`, force-update), atualizar os campos pertencentes a esse BOD. Caso contrário, descartar o BOD.
4. O `variationID` do outro tipo de BOD não é tocado; os seus valores previamente armazenados permanecem.

As linhas `supplier_address` e `supplier_account` associadas ao fornecedor são apagadas e reinseridas na atualização, para que as tabelas secundárias reflitam sempre o BOD mais recente. Isto tem um efeito colateral quando o M3 emite um BOD RemitToPartyMaster *por divisão* (alguns tenants fazem-no quando as ligações bancárias são mantidas tanto numa divisão vazia como em divisões específicas): depois de `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` cortar o sufixo de divisão, cada BOD por divisão visa a mesma chave `(customer_number, supplier_number)`. Vence o BOD com o `variationID` mais alto. Se esse BOD "vencedor" pertencer a uma divisão sem ligações bancárias, as contas bancárias do BOD anterior são apagadas no re-insert.

## Perguntas frequentes

### Por que é que o DocBits rastreia CONO se todos os meus fornecedores vêm de uma só empresa M3?

O roteamento CONO é obrigatório porque o DocBits é multi-tenant por desenho: uma organização pode ingerir BODs de várias empresas M3. CONO faz parte da chave de correspondência para que fornecedores de empresas diferentes não colidam. Com apenas uma empresa, pode ignorar o valor — mas a coluna-chave continua a ser preenchida.

### Ambos os BODs escrevem na mesma linha de fornecedor — o último BOD sobrescreve tudo?

Não. Cada tipo de BOD possui apenas os campos que envia, e as atualizações são governadas por um `variationID` independente. Um SupplierPartyMaster que altera apenas o nome do fornecedor não reverte o número de telefone que um RemitToPartyMaster posterior tenha escrito.

### `Supplier Categories` e `eam.UDFCHAR06` nunca são entregues pelo meu M3 — o que fazer?

Ambas são extensões UserArea opcionais. Sem a extensão, as colunas ficam NULL e nenhuma funcionalidade do DocBits depende delas. Ative a lógica de data de desconto apenas quando o seu M3 estiver configurado para emitir `eam.UDFCHAR06`.

### `vatNo` deve filtrar por `schemeName='TaxIdentificationNumber'`?

O caminho de ingestão BOD M3 lê atualmente `PartyIDs/TaxID` sem filtro `schemeName`. O filtro é usado nos caminhos XSLT de fatura eletrónica (Facturae, XRechnung, KSeF), não na ingestão M3. Quando o M3 emite vários elementos `TaxID` com diferentes valores `@schemeName`, vence a primeira ocorrência — o que pode produzir identificadores IVA incorretos. Está planeado um filtro configurável; um BOD de exemplo do seu tenant ajuda-nos a definir o `schemeName` default correto. <!-- tracked in DOCB-12313 -->

### O que acontece quando é emitido um BOD RemitToPartyMaster por divisão?

Alguns tenants M3 mantêm ligações bancárias tanto numa divisão vazia como em divisões específicas, o que faz com que o M3 emita um BOD RemitToPartyMaster separado por divisão. A chave de correspondência no DocBits é `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — a divisão não faz parte dela.

- Com a preferência `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` ativa, os BODs por divisão colapsam na mesma linha. Vence o BOD com o `variationID` mais alto, e as linhas `supplier_account` são reinseridas apenas a partir desse BOD. Se o BOD vencedor proceder de uma divisão sem ligações bancárias, as contas bancárias previamente armazenadas são apagadas.
- Com a preferência desativada (a CONO mantém o sufixo de divisão), os BODs por divisão visam chaves distintas e coexistem.

Se o seu tenant envia BODs RemitToPartyMaster por divisão e depende da lista bancária consolidada, contacte-nos com um exemplo para que possamos planear uma melhoria.

### Quero sincronizar todas as contas bancárias do fornecedor, não apenas a última. Como?

Ative a preferência `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Com a flag ativa, cada `FinancialParty` do BOD é persistida na tabela `supplier_account` (IBAN, ID da conta financeira, código de moeda, indicador de preferência). A coluna legacy `bank_id` no cabeçalho continua a manter a última entrada para compatibilidade retroativa.
