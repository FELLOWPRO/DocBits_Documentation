---
description: Suporte a documentos eletrônicos BRAZIL NF-E no DocBits
---

# 🇧🇷 BRAZIL NF-E

| Propriedade | Valor |
| --- | --- |
| **País / Região** | Brasil |
| **Tipos de documento** | Fatura (Nota Fiscal Eletrônica) |
| **Formato** | XML |
| **Padrão** | NF-e 4.0 (Nota Fiscal Eletrônica — mercadorias e comércio interestadual) |
| **Idioma** | `pt_BR` |

A NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) é a nota fiscal eletrônica brasileira para mercadorias e comércio interestadual, regulamentada pela SEFAZ. Cada NF-e contém uma chave de acesso exclusiva de 44 dígitos (`chNFe`), itens de produto detalhados e dados tributários em vários níveis (ICMS, IPI, PIS, COFINS). O DocBits classifica a NF-e detectando o namespace `http://www.portalfiscal.inf.br/nfe`.

## Status de suporte

| Componente | Status |
| --- | --- |
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Visualização de NF-e do Brasil no DocBits"><figcaption><p>Visualização padrão do DocBits para um documento BRAZIL NF-E</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | XPath de origem | Observações |
| --- | --- | --- |
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Número da Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 com deslocamento BRT |
| `currency` | Fixo: `BRL` | Sempre real brasileiro |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Valor total da NF-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Valor total dos produtos |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Total do imposto ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nome da empresa emitente |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` ou `CPF` | CNPJ (14 dígitos) ou CPF (11 dígitos) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nome da empresa destinatária |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` ou `CPF` | CNPJ ou CPF |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `//*[local-name()='det']`

| Coluna | XPath relativo | Observações |
| --- | --- | --- |
| `POSITION` | `@nItem` | Número de sequência do item |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Código do produto |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Descrição do produto |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | Classificação aduaneira NCM |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Código fiscal de operação |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Unidade de medida |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Quantidade comercial |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Preço unitário |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Total da linha |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Imposto ICMS por linha |
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | Imposto PIS por linha |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Imposto COFINS por linha |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Alíquota de ICMS (%) |

## Regra de classificação

O DocBits detecta documentos BRAZIL NF-E verificando a seguinte string:

```
http://www.portalfiscal.inf.br/nfe
```

no namespace XML (`mod=55` para NF-e e `mod=65` para NFC-e são distinguidos separadamente).

## Relacionado

* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documentos Eletrônicos Suportados](./)
