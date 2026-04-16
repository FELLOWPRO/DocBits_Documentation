---
description: Suporte a documentos eletrônicos CHILE DTE no DocBits
---

# 🇨🇱 CHILE DTE

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Chile |
| **Tipos de Documento** | Fatura (Factura), Nota de Crédito, Nota de Débito, Guia de Despacho |
| **Formato** | XML |
| **Padrão** | DTE (Documento Tributario Electrónico), SII |
| **Localidade** | `es_CL` |

DTE (Documento Tributario Electrónico) é o padrão chileno de documentos fiscais eletrônicos regulado pelo Servicio de Impuestos Internos (SII). Todos os documentos DTE compartilham o namespace `http://www.sii.cl/SiiDte`. O DocBits detecta automaticamente o código de tipo DTE (`TipoDTE`) e encaminha para as regras de extração apropriadas:

| Código de Tipo | Tipo de Documento |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Status de Suporte

| Componente | Status |
|-----------|--------|
| Visualização | ✅ Suportado |
| Extração de Campos | ✅ Suportada |
| Transformação | ✅ Suportada |

## Visualização Padrão

<figure><img src="chile-dte-preview.png" alt="Visualização do Chile DTE Factura no DocBits"><figcaption><p>Visualização padrão do DocBits para uma CHILE DTE FACTURA (tipo 33)</p></figcaption></figure>

## Mapeamento de Campos

### Campos de Cabeçalho

| Campo DocBits | Elemento XML Fonte | Notas |
|---|---|---|
| `invoice_id` | `Folio` | Número de fólio do documento |
| `invoice_date` | `FchEmis` | Data de emissão ISO 8601 |
| `due_date` | `FchVenc` | Data de vencimento do pagamento |
| `currency` | Fixo: `CLP` | Sempre Peso Chileno |
| `total_amount` | `MntTotal` | Valor total incl. IVA |
| `net_amount` | `MntNeto` | Valor líquido tributável |
| `tax_amount` | `IVA` | Valor do IVA (taxa padrão de 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nome da empresa emissora |
| `supplier_id` | `RUTEmisor` | RUT do emissor (ex.: `76123456-7`) |
| `supplier_address` | `DirOrigen` | Endereço do emissor |
| `supplier_city` | `CiudadOrigen` | Cidade do emissor |
| `supplier_country` | Fixo: `CL` | Sempre Chile |
| `buyer_name` | `RznSocRecep` | Nome da empresa receptora |
| `buyer_id` | `RUTRecep` | RUT do receptor |
| `buyer_address` | `DirRecep` | Endereço do receptor |
| `buyer_city` | `CiudadRecep` | Cidade do receptor |
| `buyer_country` | Fixo: `CL` | Sempre Chile |

### Tabela de Itens de Linha (`INVOICE_TABLE`)

Caminho da linha: `Detalle`

| Coluna | Elemento XML Fonte | Notas |
|---|---|---|
| `POSITION` | `NroLinDet` | Número sequencial da linha |
| `DESCRIPTION` | `NmbItem` | Nome do item |
| `QUANTITY` | `QtyItem` | Quantidade |
| `UNIT` | `UnmdItem` | Unidade de medida |
| `UNIT_PRICE` | `PrcItem` | Preço unitário excl. IVA |
| `VAT_RATE` | `TasaIVA` (do cabeçalho) | Taxa de IVA em % (normalmente 19%) |
| `VAT` | Calculado | IVA por linha |
| `NET_AMOUNT` | `MontoItem` | Total da linha |

## Regras de Classificação

O DocBits detecta documentos Chile DTE correspondendo o namespace XML e `TipoDTE`:

| Tipo de Documento Eletrônico | Padrão |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

O elemento envelope é `<EnvioDTE>` e cada DTE está encapsulado em `<DTE><Documento>`.

## Relacionado

- [Padrões de E-Fatura Atualmente Suportados](../../currently-supported-e-invoice-standards/)
- [Documentos Eletrônicos Suportados](./)
