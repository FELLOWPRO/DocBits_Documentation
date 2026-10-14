---
description: Supporto in DocBits per il documento elettronico BRAZIL NF-E
---

# 🇧🇷 BRAZIL NF-E

| Proprietà             | Valore                                                           |
| --------------------- | ---------------------------------------------------------------- |
| **Paese / Regione**   | Brasile                                                          |
| **Tipi di documento** | Fattura (Nota Fiscal Eletrônica)                                 |
| **Formato**           | XML                                                              |
| **Standard**          | NF-e 4.0 (Nota Fiscal Eletrônica — merci e commercio interstatale) |
| **Locale**            | `pt_BR`                                                          |

La NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) è la fattura elettronica brasiliana per le merci e il commercio interstatale, regolamentata dalla SEFAZ. Ogni NF-e contiene una chiave di accesso univoca di 44 cifre (`chNFe`), righe articolo dettagliate e dati fiscali su più livelli (ICMS, IPI, PIS, COFINS). DocBits classifica la NF-e rilevando il namespace `http://www.portalfiscal.inf.br/nfe`.

## Stato del supporto

| Componente           | Stato         |
| -------------------- | ------------- |
| Anteprima            | ✅ Supportato |
| Estrazione dei campi | ✅ Supportato |
| Trasformazione       | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Anteprima della NF-e brasiliana in DocBits"><figcaption><p>Anteprima predefinita di DocBits per un documento BRAZIL NF-E</p></figcaption></figure>

## Mappatura dei campi

### Campi di testata

| Campo DocBits   | XPath di origine                                           | Note                                     |
| --------------- | ---------------------------------------------------------- | ---------------------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Numero della Nota Fiscal                 |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 con offset BRT                  |
| `currency`      | Fisso: `BRL`                                               | Sempre real brasiliano                   |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Valore totale della NF-e                 |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Valore totale dei prodotti               |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | Totale imposta ICMS                      |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Ragione sociale dell'emittente           |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` o `CPF` | CNPJ (14 cifre) o CPF (11 cifre)         |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Ragione sociale del destinatario         |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CNPJ']` o `CPF` | CNPJ o CPF                               |

### Tabella delle righe articolo (`INVOICE_TABLE`)

Percorso della riga: `//*[local-name()='det']`

| Colonna         | XPath relativo                                                                  | Note                             |
| --------------- | ------------------------------------------------------------------------------- | -------------------------------- |
| `POSITION`      | `@nItem`                                                                        | Numero progressivo dell'articolo |
| `ITEM_CODE`     | `*[local-name()='prod']/*[local-name()='cProd']`                                | Codice prodotto                  |
| `DESCRIPTION`   | `*[local-name()='prod']/*[local-name()='xProd']`                                | Descrizione del prodotto         |
| `NCM_CODE`      | `*[local-name()='prod']/*[local-name()='NCM']`                                  | Classificazione doganale NCM     |
| `CFOP_CODE`     | `*[local-name()='prod']/*[local-name()='CFOP']`                                 | Codice fiscale dell'operazione   |
| `UNIT`          | `*[local-name()='prod']/*[local-name()='uCom']`                                 | Unità di misura                  |
| `QUANTITY`      | `*[local-name()='prod']/*[local-name()='qCom']`                                 | Quantità commerciale             |
| `UNIT_PRICE`    | `*[local-name()='prod']/*[local-name()='vUnCom']`                               | Prezzo unitario                  |
| `TOTAL_AMOUNT`  | `*[local-name()='prod']/*[local-name()='vProd']`                                | Totale di riga                   |
| `ICMS_AMOUNT`   | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']`     | Imposta ICMS per riga            |
| `PIS_AMOUNT`    | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']`       | Imposta PIS per riga             |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Imposta COFINS per riga          |
| `VAT_RATE`      | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']`     | Aliquota ICMS (%)                |

## Regola di classificazione

DocBits riconosce i documenti BRAZIL NF-E verificando la presenza della stringa:

```
http://www.portalfiscal.inf.br/nfe
```

nel namespace XML (`mod=55` per la NF-e e `mod=65` per la NFC-e vengono distinti separatamente).

## Correlati

* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documenti elettronici supportati](./)
