---
description: Suporte a documentos eletrônicos BRAZIL NFC-E no DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Propriedade            | Valor                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| **País / Região**      | Brasil                                                           |
| **Tipos de documento** | Nota fiscal ao consumidor (Nota Fiscal de Consumidor Eletrônica) |
| **Formato**            | XML                                                              |
| **Padrão**             | NFC-e 4.0 (nota fiscal ao consumidor no varejo / ponto de venda) |
| **Idioma**             | `pt_BR`                                                          |

A NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) é a nota fiscal eletrônica brasileira para vendas no varejo a consumidores finais. Ela compartilha o esquema XML da NF-e (namespace `nfeProc`), mas usa o código de modelo 65. Os documentos NFC-e normalmente trazem um CPF (identificação fiscal de pessoa física) para o comprador em vez de um CNPJ e não incluem PIS/COFINS por linha em transações simples de varejo.

## Status de suporte

| Componente         | Status      |
| ------------------ | ----------- |
| Visualização       | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação      | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Visualização de NFC-e do Brasil no DocBits"><figcaption><p>Visualização padrão do DocBits para um documento BRAZIL NFC-E</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits   | XPath de origem                                            | Observações                   |
| --------------- | ---------------------------------------------------------- | ----------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Número da Nota Fiscal         |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 com deslocamento BRT |
| `currency`      | Fixo: `BRL`                                                | Sempre real brasileiro        |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Valor total da NFC-e          |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Subtotal dos produtos         |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | Total do imposto ICMS         |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Nome do varejista             |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` ou `CPF` | CNPJ ou CPF                   |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Nome do consumidor            |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CPF']` ou `CNPJ` | CPF (pessoa física) ou CNPJ   |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `//*[local-name()='det']`

| Coluna         | XPath relativo                                                              | Observações                 |
| -------------- | --------------------------------------------------------------------------- | --------------------------- |
| `POSITION`     | `@nItem`                                                                    | Número de sequência do item |
| `ITEM_CODE`    | `*[local-name()='prod']/*[local-name()='cProd']`                            | Código do produto           |
| `DESCRIPTION`  | `*[local-name()='prod']/*[local-name()='xProd']`                            | Descrição do produto        |
| `NCM_CODE`     | `*[local-name()='prod']/*[local-name()='NCM']`                              | Classificação aduaneira NCM |
| `CFOP_CODE`    | `*[local-name()='prod']/*[local-name()='CFOP']`                             | Código fiscal de operação   |
| `UNIT`         | `*[local-name()='prod']/*[local-name()='uCom']`                             | Unidade de medida           |
| `QUANTITY`     | `*[local-name()='prod']/*[local-name()='qCom']`                             | Quantidade comercial        |
| `UNIT_PRICE`   | `*[local-name()='prod']/*[local-name()='vUnCom']`                           | Preço unitário              |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']`                            | Total da linha              |
| `ICMS_AMOUNT`  | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Imposto ICMS por linha      |
| `VAT_RATE`     | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Alíquota de ICMS (%)        |

## Regra de classificação

O DocBits detecta documentos BRAZIL NFC-E pelo padrão `<mod>65</mod>` dentro do XML do namespace `http://www.portalfiscal.inf.br/nfe`.

## Relacionado

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documentos Eletrônicos Suportados](./)
