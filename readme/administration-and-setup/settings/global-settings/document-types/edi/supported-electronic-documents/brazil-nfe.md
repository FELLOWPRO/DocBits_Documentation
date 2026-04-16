---
description: Suporte ao documento eletrónico BRAZIL NF-E no DocBits
---

# 🇧🇷 BRAZIL NF-E

| Propriedade | Valor |
|-------------|-------|
| **País / Região** | Brasil |
| **Tipos de Documento** | Fatura (Nota Fiscal Eletrônica) |
| **Formato** | XML |
| **Norma** | NF-e 4.0 (Nota Fiscal Eletrônica — mercadorias e comércio interestadual) |
| **Localidade** | `pt_BR` |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) é a fatura eletrónica brasileira para mercadorias e comércio interestadual, regulada pela SEFAZ. Cada NF-e contém uma chave de acesso única com 44 dígitos (`chNFe`), itens de linha de produto detalhados e dados fiscais em múltiplos níveis (ICMS, IPI, PIS, COFINS). O DocBits classifica a NF-e ao detetar o namespace `http://www.portalfiscal.inf.br/nfe`.

## Estado de Suporte

| Componente | Estado |
|------------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de Campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização Padrão

<figure><img src="brazil-nfe-preview.png" alt="Pré-visualização Brazil NF-e no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para um documento BRAZIL NF-E</p></figcaption></figure>

## Mapeamento de Campos

### Campos de Cabeçalho

| Campo DocBits | XPath de Origem | Notas |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Número da Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 com offset BRT |
| `currency` | Fixo: `BRL` | Sempre Real Brasileiro |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Valor total da NF-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Valor total dos produtos |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Total do imposto ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nome do fornecedor (emit) |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` ou `CPF` | CNPJ (14 dígitos) ou CPF (11 dígitos) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nome do comprador (dest) |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` ou `CPF` | CNPJ ou CPF |

### Tabela de Itens (`INVOICE_TABLE`)

Caminho de linha: `//*[local-name()='det']`

| Coluna | XPath Relativo | Notas |
|---|---|---|
| `POSITION` | `@nItem` | Número de sequência do item |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Código do produto |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Descrição do produto |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | Classificação aduaneira NCM |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Código Fiscal de Operações |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Unidade de medida |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Quantidade comercial |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Preço unitário |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Total da linha |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Imposto ICMS por linha |
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | Imposto PIS por linha |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Imposto COFINS por linha |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Taxa ICMS (%) |

## Regra de Classificação

O DocBits deteta documentos BRAZIL NF-E ao verificar a cadeia de caracteres:

```
http://www.portalfiscal.inf.br/nfe
```

no namespace XML (`mod=55` para NF-e e `mod=65` para NFC-e são distinguidos separadamente).

## Relacionados

- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documentos Eletrónicos Suportados](./)
