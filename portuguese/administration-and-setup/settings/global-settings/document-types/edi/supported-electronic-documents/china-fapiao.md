---
description: Suporte a documentos eletrônicos China Fapiao (FAPIAO, E-FAPIAO, Fatura IVA Geral, Fatura IVA Especial) no DocBits
---

# 🇨🇳 China Fapiao

| Propriedade | Valor |
|----------|-------|
| **País / Região** | China |
| **Tipos de documento** | Fatura IVA Geral (普通发票), Fatura IVA Especial (专用发票), E-Fapiao |
| **Formato** | XML |
| **Padrão** | Fapiao (发票), State Taxation Administration |
| **Localidade** | `zh_CN` |

Fapiao (发票) é o padrão chino de fatura fiscal emitido sob a autoridade da Administração Estatal de Tributação (STA / 国家税务总局). Todos os documentos Fapiao compartilham o namespace `urn:china:tax:fapiao:1.0`. O DocBits detecta automaticamente o tipo de Fapiao por meio do elemento `fapiao_type` e direciona para as regras de extração adequadas:

| Valor de fapiao_type | Tipo de documento |
|-------------------|--------------|
| 普通发票 | Fatura IVA Geral (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Fatura IVA Especial (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Supported |
| Extração de campos | ✅ Supported |
| Transformação | ✅ Supported |

## Pré-visualização padrão

<figure><img src="china-fapiao-preview.png" alt="Pré-visualização da Fatura IVA Geral China Fapiao no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma Fatura IVA Geral China Fapiao (普通发票)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Notas |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Número Fapiao — 8 dígitos (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Data de emissão (ISO 8601) |
| `currency` | Fixo: `CNY` | Sempre Yuan Renminbi chinês |
| `total_amount` | `total/total_with_tax` | Valor total incl. IVA (价税合计) |
| `net_amount` | `total/total_amount` | Valor líquido tributável excl. IVA (金额) |
| `tax_amount` | `total/total_tax` | Valor total do IVA (税额) |
| `supplier_name` | `seller/name` | Nome da empresa vendedora (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | CNPJ do vendedor — 18 caracteres (纳税人识别号) |
| `supplier_address` | `seller/address` | Endereço do vendedor |
| `supplier_country` | Fixo: `CN` | Sempre China |
| `iban` | `seller/bank_account` | Número da conta bancária do vendedor |
| `buyer_name` | `buyer/name` | Nome da empresa compradora (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | CNPJ do comprador (纳税人识别号) |
| `buyer_address` | `buyer/address` | Endereço do comprador |
| `buyer_country` | Fixo: `CN` | Sempre China |

### Tabela de itens de linha (`INVOICE_TABLE`)

Caminho da linha: `items/item`

| Coluna | Elemento XML de origem | Notas |
|---|---|---|
| `POSITION` | `seq` | Número de sequência da linha |
| `DESCRIPTION` | `name` + `spec` | Nome do item e especificação (concatenados) |
| `QUANTITY` | `quantity` | Quantidade |
| `UNIT` | `unit` | Unidade de medida (ex.: 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Preço unitário excl. IVA |
| `VAT_RATE` | `tax_rate` | Taxa de IVA em % (normalmente 6%, 9% ou 13%) |
| `VAT` | `tax_amount` | Valor do IVA por linha |
| `NET_AMOUNT` | `amount` | Total da linha excl. IVA |

## Regras de classificação

O DocBits detecta documentos China Fapiao correspondendo o namespace XML e o `fapiao_type`:

| Tipo de documento eletrônico | Padrão |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

O elemento raiz é `<fapiao>` com o namespace `urn:china:tax:fapiao:1.0`. A classificação utiliza o princípio **first-match-wins** ordenado por comprimento do padrão (o mais longo primeiro).

## Relacionado

- [Padrões de e-fatura atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrônicos suportados](./)
