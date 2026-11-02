# Mapeamento BOD de Purchase Order

Esta página documenta como o DocBits ingere os BODs `SyncPurchaseOrder` do Infor M3 e mapeia os campos para as tabelas internas `PURCHASE_ORDER_HEADER` e Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Referência original do mapeamento BOD (PDF)
{% endfile %}

## Princípios-chave

- **Sem conversão de moeda no DocBits.** Os valores são persistidos exatamente como o M3 os entrega no BOD, juntamente com o respectivo `@currencyID`. Três valores de cabeçalho estão disponíveis: `ExtendedAmount` (moeda da transação), `ExtendedBaseAmount` (moeda base da empresa), `ExtendedReportAmount` (moeda de relatório).
- **Sem conversão de unidade de medida no DocBits.** As quantidades são armazenadas com o respectivo `@unitCode`. `ReceivedBaseUOMQuantity` é o valor em UoM base pré-calculado pelo M3 — o DocBits armazena-o como está.
- **O status do cabeçalho é obtido do estágio SXE quando disponível.** O DocBits lê `UserArea/Property[@name='poeh.stagecd']` (valores `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) e usa-o como status autoritativo do cabeçalho. O `Status/Code` padrão também é armazenado como fallback para BODs em que `poeh.stagecd` não esteja preenchido — a emissão desta propriedade UserArea depende do tenant.
- **Sem lógica automática de status para quantidades parciais.** O DocBits não deriva um status a partir das quantidades recebidas vs. encomendadas; o status entregue pelo M3 é assumido 1:1.
- **`CONO`/`AccountingEntityID` não faz parte do BOD PurchaseOrder.** O roteamento por número da empresa aplica-se aos dados mestres de fornecedores (ver [Supplier BOD Mapping](supplier-bod-mapping.md)); as ordens de compra são associadas via `LocationID`. Note que `LocationID` **não é globalmente único** — quando uma empresa M3 (CONO) é copiada entre ambientes (por exemplo PRD → TST), o mesmo `LocationID` pode existir sob múltiplos CONOs. Nessas configurações, filtre o fluxo de BODs recebidos pela `AccountingEntity` esperada no seu DataFlow ION para evitar colisões entre ambientes.

## Mapeamento de Cabeçalho

→ Tabela de dados mestres DocBits: **PURCHASE\_ORDER\_HEADER**

```python
header_mappings = {
            "purchase_order_number": "//DataArea/PurchaseOrder/PurchaseOrderHeader/DocumentID/ID",
            "warehouse_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ShipToParty/Location[@type='Warehouse']/ID",
            "location_id": "//DataArea/Sync/LocationID",
            "status": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Status/Code",
            "supplier_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/PartyIDs/ID",
            "supplier_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/Name",
            "order_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/OrderDateTime",
            "requested_shipment_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/RequiredDeliveryDateTime",
            "total_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "buyer_contact_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/ID",
            "buyer_contact_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/Name",
            "order_last_modified_by": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationPerson/IDs/ID",
            "order_last_modified_on": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationDateTime",
            "disponent_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/IDs/ID",
            "disponent_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/Name",
            "extended_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "extended_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedBaseAmount",
            "extended_report_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedReportAmount",
            "canceled_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledAmount",
            "canceled_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledBaseAmount",
            "canceled_reporting_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledReportingAmount",
            "type_code": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification/Codes/Code[@listID='Purchase Order Types']",
            "type_description": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification[Codes/Code[@listID='Purchase Order Types']]/Description",
            "sxe_stage": "//DataArea/PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='poeh.stagecd']/text()",
        }
```

### Referência dos campos do cabeçalho

| Campo DocBits | Origem M3 | Descrição |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | Número da ordem de compra M3, chave primária. |
| `warehouse_id` | — | Lê `ShipToParty/Location[@type='Warehouse']/ID`. O atributo `@type='Warehouse'` raramente é definido pelo M3; o campo fica NULL nesse caso. Utilize `location_id` como armazém nativo do M3. |
| `location_id` | `MPHEAD.IAFACI` | Divisão/instalação (armazém) M3 onde o BOD foi gerado. Usado para roteamento organização/instalação dentro do DocBits, incluindo correspondência com instalações de faturas. |
| `status` | `MPHEAD.IAPUSL` | `Status/Code` bruto do BOD. Usado como fallback quando `sxe_stage` está vazio. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Status autoritativo do cabeçalho, lido da propriedade UserArea `poeh.stagecd`. Mapeia os códigos SXE M3 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Quando definido, prevalece sobre `status` para decisões de fluxo de trabalho. Com a preferência `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` ativa, o DocBits propaga este status para as faturas associadas. |
| `supplier_id` | `MPHEAD.IASUNO` | Número do fornecedor na ordem de compra. |
| `supplier_name` | `CIDMAS.IDSUNM` | Nome de exibição do fornecedor. |
| `order_date` | `MPHEAD.IAPUDT` | Data de criação da ordem de compra no M3. |
| `requested_shipment_date` | — | Lido de `RequiredDeliveryDateTime` ao nível de cabeçalho, se existir. A maioria das configurações M3 mantém apenas na linha; nesse caso use o `requested_ship_date` da linha. |
| `total_amount` | `MPHEAD.IAOURR` | Total da ordem na moeda de transação. Armazenado 1:1 de `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Mesma origem de `total_amount`. Mantido como coluna bruta separada para rastreabilidade e consumidores que esperam o caminho BOD canónico. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Total expresso na moeda base da empresa. Preenchido pelo M3 quando disponível — o preenchimento depende do tenant; se não conseguir reproduzir um valor preenchido, partilhe um BOD de exemplo. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Total expresso na moeda de relatório da empresa. O preenchimento depende do tenant (como `extended_base_amount`). |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Valores de cancelamento na moeda de transação / base / relatório. Preenchidos pelo M3 apenas após eventos de cancelamento. |
| `type_code` / `type_description` | — | Tipo de ordem de compra a partir de `Classification/Codes/Code[@listID='Purchase Order Types']` (e a respetiva `Description`). Exemplos: `P10` PO normal, `P20` PO de reposição. Armazenado apenas para exibição — sem lógica de filtragem. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / utilizador associado | Comprador atribuído à PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Campos de auditoria. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / utilizador associado | Referência do planeador. |

## Mapeamento de Linhas

→ Tabela de dados mestres DocBits: **Purchase Order**

```python
line_mappings = {
        "sub_line_number": "SubLineNumber",
        "item_id": [
            "Item/ItemID/ID[not(@schemeName)]",
            "Item/ItemID/ID[@schemeName='NonStock']",
        ],
        "supplier_item_id": [
            "Item/ItemID/ID[@schemeName='Supplier']",
            "Item/Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']",
            "Item/SupplierItemID/ID",
        ],
        "schedule_line_number ": "DocumentReference/ScheduleLineNumber",
        "description": "Item/Description",
        "note": "Note",
        "quantity": "Quantity",
        "open_quantity": "OpenQuantity",
        "confirmed_quantity": "BackOrderedQuantity",
        "received_quantity": "ReceivedQuantity",
        "received_base_mou_quantity": "ReceivedBaseUOMQuantity",
        "unit_of_measure": "Quantity/@unitCode",
        "unit_price": "UnitPrice/Amount",
        "unit_price_per": "UnitPrice/PerQuantity",
        "unit_code_price": "UnitPrice/PerQuantity/@unitCode",
        "total_amount": ["TotalAmount", "ExtendedAmount"],
        "extended_amount": "ExtendedAmount",
        "currency": ["TotalAmount/@currencyID", "ExtendedAmount/@currencyID"],
        "buyer_id": "BuyerParty/PartyIDs/ID",
        "buyer_name": "BuyerParty/Name",
        "status": "Status/Code",
        "geo_code": "UserArea/Property/NameValue[@name='GeoCode']",
        "delivery_method": "UserArea/Property/NameValue[@name='m3.DeliveryMethod']",
        "order_multiple": "Classification/Codes/Code[@listID='Order multiple']",
        "standard_quantity": "UserArea/Property/NameValue[@name='StandardQuantity']",
        "promised_delivery_date": "PromisedDeliveryDateTime",
        "requested_ship_date": "RequiredDeliveryDateTime",
    }
```

### Referência dos campos de linha

| Campo DocBits | Origem M3 | Descrição |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | Número do artigo M3. Fallback para `@schemeName='NonStock'` para artigos não-stock. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Número do artigo do lado do fornecedor. Resolvido através de três fallbacks (por ordem): `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Descrição do artigo da linha. |
| `note` | `MSYTXL.TLTX60` | Texto de nota da linha. |
| `quantity` | `MPLINE.IBORQA` | Quantidade encomendada. Armazenada com `unit_of_measure` (sem conversão). |
| `open_quantity` | `CFQA - RVQA` | Quantidade ainda em aberto (encomendada menos recebida). Mesmo `unit_of_measure`. |
| `confirmed_quantity` | — | Quantidade confirmada pelo fornecedor. O M3 deixa vazio; preenchido por ERPs que emitem `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Quantidade recebida. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (UoM base) | Quantidade recebida convertida na unidade de medida base pelo próprio M3. O DocBits não calcula — armazena o que o M3 envia. Útil para contabilidade de stock. |
| `unit_of_measure` | `MPLINE.IBPUUN` | UoM de transação. Aplica-se a `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Preço unitário na moeda de transação. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Preço-por quantidade e o seu código de unidade (modificador de preço, ex. preço por 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Total da linha. Resolvido por fallback `[TotalAmount, ExtendedAmount]` — quando `TotalAmount` está em falta, `total_amount` é igual a `extended_amount`. Quando ambos estão presentes, `TotalAmount` pode incluir impostos/descontos, enquanto `extended_amount` é `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | `ExtendedAmount` bruto (subtotal da linha sem impostos/descontos). |
| `currency` | `MPHEAD.IACUCD` | Moeda de transação. Lida de `TotalAmount/@currencyID`, com `ExtendedAmount/@currencyID` como fallback. |
| `status` | `MPLINE.IBPUST` | Status da linha. Armazenado para relatórios; nenhuma lógica de fluxo do DocBits deriva dele. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / utilizador associado | Comprador ao nível da linha. `buyer_name` é raramente preenchido pelo M3 na linha; a referência do comprador do fornecedor está em [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Código geográfico para motores fiscais US/CA. Preenchido apenas por ERPs que o emitem. |
| `delivery_method` | `MPLINE.IBMODL` | Método de entrega da linha (código `MODL` M3). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Data de entrega confirmada pelo fornecedor. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Data de expedição pretendida na linha — data de entrega desejada operacionalmente relevante. |
| `sub_line_number` | — | Identificador opcional de sub-linha. Armazenado se presente; o M3 normalmente deixa vazio. |
| `schedule_line_number` | — | Referência opcional à linha de cronograma para POs com entregas programadas. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Múltiplo de encomenda da linha (quantidade mínima) e quantidade-padrão de embalagem. |

## Perguntas frequentes

### Como é que o DocBits trata ordens de compra em moeda estrangeira?

O DocBits não converte moedas. O montante de transação (`total_amount`, `extended_amount`, `unit_price`) é armazenado juntamente com o respectivo `@currencyID`. Quando a empresa usa uma moeda base ou de relatório diferente, o M3 fornece valores pré-convertidos via `extended_base_amount` e `extended_report_amount` — armazenados como colunas adicionais no cabeçalho.

### Como é que o DocBits deriva o status de receção parcial?

Não deriva. O status do cabeçalho reflete o estágio SXE M3 (`poeh.stagecd`) no momento da emissão do BOD. Se precisar de um indicador de receção parcial, derive-o a partir de `open_quantity` vs. `quantity` na tabela das linhas.

### Qual a diferença entre `total_amount` e `extended_amount` na linha?

Ambas as colunas existem por compatibilidade histórica/UI. `total_amount` é resolvido por `[TotalAmount, ExtendedAmount]`, sendo igual a `extended_amount` sempre que `TotalAmount` está ausente. Quando o M3 emite os dois, `TotalAmount` pode incluir impostos ou descontos sobre o valor `quantity × unit_price` guardado em `extended_amount`.

### Por que é que o armazém é mapeado para dois caminhos diferentes?

`warehouse_id` lê `ShipToParty/Location[@type='Warehouse']/ID`, que a maioria das instalações M3 deixa vazio (o atributo `@type` raramente é definido). `location_id` lê `DataArea/Sync/LocationID`, sempre preenchido pelo M3 e correspondendo à divisão/instalação a que a PO pertence. Trate `location_id` como identificador de armazém nativo do M3.

### Alguns campos estão documentados mas sempre vazios (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Porquê estão mapeados?

Estes mapeamentos são defensivos: o esquema BOD permite os campos, e outros ERPs ou extensões M3 personalizadas podem preenchê-los. Quando o M3 os deixa vazios, as colunas são simplesmente NULL no DocBits.

### Devo filtrar `AccountingEntity` (CONO) no DataFlow ION mesmo que o BOD PurchaseOrder não contenha `CONO`?

Sim, em ambientes onde a mesma empresa M3 tenha sido copiada (por exemplo PRD → TST, ou dois tenants paralelos). O `LocationID` sozinho não é único entre CONOs nessas configurações, pelo que um BOD originado numa empresa copiada pode colidir com uma ativa. O padrão recomendado é filtrar o fluxo recebido pelo valor `AccountingEntity` esperado em ION antes de o BOD chegar ao DocBits.

### Os meus BODs nunca contêm `UserArea/Property[@name='poeh.stagecd']` — o que acontece?

O DocBits recorre ao elemento padrão `Status/Code` no cabeçalho. A emissão de `poeh.stagecd` depende do tenant. Se espera esta propriedade mas não a encontra nos seus BODs, partilhe um BOD de exemplo com a equipa DocBits para que possamos confirmar a personalização M3 que a produz.

### `ExtendedBaseAmount` / `ExtendedReportAmount` são realmente preenchidos no cabeçalho?

Sempre que o M3 os envia no cabeçalho, o DocBits armazena-os em colunas dedicadas (`extended_base_amount`, `extended_report_amount`). O preenchimento depende da configuração de moedas do M3: empresas com moeda base/relatório diferente da moeda de transação tipicamente recebem ambas. Se não conseguir reproduzir um valor preenchido no seu tenant, partilhe um BOD de exemplo para que possamos verificar as condições em conjunto.
