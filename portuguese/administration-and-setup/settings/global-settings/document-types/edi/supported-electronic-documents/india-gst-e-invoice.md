---
description: Suporte para a fatura eletrónica GST da Índia no DocBits
---

# 🇮🇳 India GST E-Invoice

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Índia |
| **Tipos de documento** | Fatura (INV), Nota de crédito (CRN), Nota de débito (DBN) |
| **Formato** | XML (`<SignedInvoice>`) |
| **Padrão** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

A fatura eletrónica GST da Índia é o padrão obrigatório de faturação eletrónica no âmbito do regime GST (Goods and Services Tax) indiano, operado pelo GSTN (GST Network). As empresas acima do limiar de faturação prescrito devem gerar e-faturas através do portal IRP (Invoice Registration Portal), que assina a fatura e devolve um **IRN** (Invoice Reference Number — um hash SHA-256 de 64 caracteres) e um código QR.

O DocBits deteta documentos GST E-Invoice pela presença de `<SignedInvoice>` como elemento raiz. O formato inclui três componentes fiscais GST:

| Componente fiscal | Descrição |
|--------------|-------------|
| IGST | GST integrado — aplicado em transações entre estados |
| CGST | GST central — aplicado em transações dentro do estado (componente central) |
| SGST | GST estadual — aplicado em transações dentro do estado (componente estadual) |

O identificador do contribuinte é o **GSTIN** (Goods and Services Tax Identification Number), um código alfanumérico de 15 caracteres no formato `29AABCU9603R1ZM` (código de estado de 2 dígitos + PAN de 10 dígitos + número de entidade + dígito de controlo). As datas usam o formato `DD/MM/AAAA`.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura eletrónica GST da Índia</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML fonte | Notas |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Número da fatura |
| `invoice_date` | `Invoice/DocDtls/Dt` | Data de emissão (`DD/MM/AAAA`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Fatura, CRN=Nota de crédito, DBN=Nota de débito |
| `currency` | Fixo: `INR` | Sempre em rupia indiana |
| `net_amount` | `Invoice/ValDtls/AssVal` | Valor tributável / sujeito a imposto |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Valor total do GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Valor total da fatura incl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Valor do GST integrado |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Valor do GST central |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Valor do GST estadual |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Valor do cess (se aplicável) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Nome legal do vendedor |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN do vendedor (15 caracteres, ex. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nome comercial do vendedor |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Morada do vendedor linha 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Cidade / localização do vendedor |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Código PIN do vendedor |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Código de estado do vendedor (2 dígitos) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Nome legal do comprador |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN do comprador |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nome comercial do comprador |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Morada do comprador linha 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Cidade / localização do comprador |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Código PIN do comprador |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Código de estado do comprador |
| `irn` | `Irn` | Número de referência da fatura (hash SHA-256 de 64 caracteres) |
| `ack_number` | `AckNo` | Número de confirmação IRP |
| `ack_date` | `AckDt` | Data de confirmação IRP |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `Invoice/ItemList/Item`

| Coluna | Elemento XML fonte | Notas |
|---|---|---|
| `POSITION` | `SlNo` | Número de sequência da linha |
| `DESCRIPTION` | `PrdDesc` | Descrição do produto / serviço |
| `QUANTITY` | `Qty` | Quantidade faturada |
| `UNIT` | `Unit` | Unidade de medida (ex. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Preço unitário |
| `VAT_RATE` | `GstRt` | Taxa GST em % (ex. 18%) |
| `VAT` | `IgstAmt` (ou `CgstAmt` + `SgstAmt`) | Valor GST por linha |
| `NET_AMOUNT` | `AssAmt` | Valor tributável por linha |

## Regra de classificação

O DocBits deteta documentos India GST E-Invoice correspondendo ao elemento raiz:

| Tipo de documento eletrónico | Padrão |
|--------------------------|---------|
| INDIA GST E-INVOICE | O elemento raiz contém `<SignedInvoice` |

## Relacionados

- [Padrões de fatura eletrónica atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrónicos suportados](./)
