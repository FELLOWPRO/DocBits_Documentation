---
description: Suporte para documentos eletrônicos CHILE DTE no DocBits
---

# 🇨🇱 CHILE DTE

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Chile |
| **Tipos de documento** | Fatura, Nota de crédito, Nota de débito, Guia de remessa |
| **Formato** | XML |
| **Padrão** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) é o padrão chileno de documentos fiscais eletrônicos regulamentado pelo Servicio de Impuestos Internos (SII). Todos os documentos DTE compartilham o namespace `http://www.sii.cl/SiiDte`. O DocBits detecta automaticamente o código de tipo DTE (`TipoDTE`) e encaminha para as regras de extração apropriadas:

| Código de tipo | Tipo de documento |
|-----------|--------------|
| 33 | Factura Electrónica (Fatura) |
| 34 | Factura No Afecta o Exenta (Fatura isenta) |
| 52 | Guía de Despacho (Guia de remessa) |
| 56 | Nota de Débito (Nota de débito) |
| 61 | Nota de Crédito (Nota de crédito) |

## Status de suporte

| Componente | Status |
|-----------|--------|
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="chile-dte-preview.png" alt="Visualização de fatura Chile DTE no DocBits"><figcaption><p>Visualização padrão do DocBits para uma CHILE DTE FACTURA (tipo 33)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
|---|---|---|
| `invoice_id` | `Folio` | Número de folio do documento |
| `invoice_date` | `FchEmis` | Data de emissão ISO 8601 |
| `due_date` | `FchVenc` | Data de vencimento |
| `currency` | Fixo: `CLP` | Sempre peso chileno |
| `total_amount` | `MntTotal` | Valor total com IVA incluído |
| `net_amount` | `MntNeto` | Valor líquido tributável |
| `tax_amount` | `IVA` | Valor do IVA (alíquota padrão 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nome da empresa emitente |
| `supplier_id` | `RUTEmisor` | RUT do emitente (ex. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Endereço do emitente |
| `supplier_city` | `CiudadOrigen` | Cidade do emitente |
| `supplier_country` | Fixo: `CL` | Sempre Chile |
| `buyer_name` | `RznSocRecep` | Nome da empresa destinatária |
| `buyer_id` | `RUTRecep` | RUT do destinatário |
| `buyer_address` | `DirRecep` | Endereço do destinatário |
| `buyer_city` | `CiudadRecep` | Cidade do destinatário |
| `buyer_country` | Fixo: `CL` | Sempre Chile |

### Tabela de linhas (`INVOICE_TABLE`)

Caminho da linha: `Detalle`

| Coluna | Elemento XML de origem | Observações |
|---|---|---|
| `POSITION` | `NroLinDet` | Número da linha |
| `DESCRIPTION` | `NmbItem` | Descrição do item |
| `QUANTITY` | `QtyItem` | Quantidade |
| `UNIT` | `UnmdItem` | Unidade de medida |
| `UNIT_PRICE` | `PrcItem` | Preço unitário sem IVA |
| `VAT_RATE` | `TasaIVA` (do cabeçalho) | Alíquota do IVA em % (tipicamente 19%) |
| `VAT` | Calculado | IVA por linha |
| `NET_AMOUNT` | `MontoItem` | Total da linha |

## Regras de classificação

O DocBits detecta documentos Chile DTE comparando o namespace XML e `TipoDTE`:

| Tipo de documento eletrônico | Padrão |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

O elemento envelope é `<EnvioDTE>` e cada DTE é encapsulado em `<DTE><Documento>`.

## Veja também

- [Padrões de e-faturação atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrônicos suportados](./)
