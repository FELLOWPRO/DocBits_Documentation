---
description: Suporte à Nota Fiscal Eletrônica GST da Índia no DocBits
---

# 🇮🇳 Índia Nota Fiscal Eletrônica GST

| Propriedade | Valor |
|-------------|-------|
| **País / Região** | Índia |
| **Tipos de documentos** | Fatura (INV), Nota de crédito (CRN), Nota de débito (DBN) |
| **Formato** | XML (`<SignedInvoice>`) |
| **Padrão** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Localidade** | `en_IN` |

A Nota Fiscal Eletrônica GST da Índia é o padrão obrigatório de faturamento eletrônico no âmbito do regime de Imposto sobre Bens e Serviços (GST) da Índia, operado pelo GSTN (GST Network). Empresas acima do limite de faturamento prescrito devem gerar e-Faturas por meio do Portal de Registro de Faturas (IRP), que assina a fatura e retorna um **IRN** (Número de Referência da Fatura — um hash SHA-256 de 64 caracteres) e um código QR.

O DocBits detecta documentos de Nota Fiscal Eletrônica GST pela presença de `<SignedInvoice>` como elemento raiz. O formato inclui três componentes fiscais GST:

| Componente fiscal | Descrição |
|------------------|-----------|
| IGST | Integrated GST — aplicado em transações interestaduais |
| CGST | Central GST — aplicado em transações intraestaduais (componente federal) |
| SGST | State GST — aplicado em transações intraestaduais (componente estadual) |

O identificador do contribuinte é o **GSTIN** (Número de Identificação Fiscal GST), um código alfanumérico de 15 caracteres no formato `29AABCU9603R1ZM` (código de estado de 2 dígitos + PAN de 10 dígitos + número de entidade + dígito verificador). As datas utilizam o formato `DD/MM/AAAA`.

## Status de suporte

| Componente | Status |
|------------|--------|
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="india-gst-e-invoice-preview.png" alt="Visualização da Nota Fiscal Eletrônica GST da Índia no DocBits"><figcaption><p>Visualização padrão do DocBits para uma Nota Fiscal Eletrônica GST da Índia</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Número da fatura |
| `invoice_date` | `Invoice/DocDtls/Dt` | Data de emissão (`DD/MM/AAAA`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Fatura, CRN=Nota de crédito, DBN=Nota de débito |
| `currency` | Fixo: `INR` | Sempre rúpia indiana |
| `net_amount` | `Invoice/ValDtls/AssVal` | Valor tributável |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Valor total do GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Valor total da fatura incl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Valor do IGST |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Valor do CGST |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Valor do SGST |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Valor do Cess (se aplicável) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Nome legal do fornecedor |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN do fornecedor (15 car., ex. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nome comercial do fornecedor |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Endereço do fornecedor linha 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Cidade / localidade do fornecedor |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Código PIN do fornecedor |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Código de estado do fornecedor (2 dígitos) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Nome legal do comprador |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN do comprador |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nome comercial do comprador |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Endereço do comprador linha 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Cidade / localidade do comprador |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Código PIN do comprador |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Código de estado do comprador |
| `irn` | `Irn` | Número de Referência da Fatura (hash SHA-256 de 64 caracteres) |
| `ack_number` | `AckNo` | Número de confirmação do IRP |
| `ack_date` | `AckDt` | Data de confirmação do IRP |

### Tabela de linhas (`INVOICE_TABLE`)

Caminho de linha: `Invoice/ItemList/Item`

| Coluna | Elemento XML de origem | Observações |
|---|---|---|
| `POSITION` | `SlNo` | Número de sequência da linha |
| `DESCRIPTION` | `PrdDesc` | Descrição do produto / serviço |
| `QUANTITY` | `Qty` | Quantidade faturada |
| `UNIT` | `Unit` | Unidade de medida (ex. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Preço unitário |
| `VAT_RATE` | `GstRt` | Taxa GST em % (ex. 18%) |
| `VAT` | `IgstAmt` (ou `CgstAmt` + `SgstAmt`) | Valor do GST por linha |
| `NET_AMOUNT` | `AssAmt` | Valor tributável por linha |

## Regra de classificação

O DocBits detecta documentos de Nota Fiscal Eletrônica GST da Índia correspondendo o elemento raiz:

| Tipo de documento eletrônico | Padrão |
|------------------------------|--------|
| INDIA GST E-INVOICE | O elemento raiz contém `<SignedInvoice` |

## Relacionados

- [Padrões de e-fatura atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrônicos suportados](./)
