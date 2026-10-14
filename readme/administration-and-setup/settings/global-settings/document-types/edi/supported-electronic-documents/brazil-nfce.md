---
description: Supporto in DocBits per il documento elettronico BRAZIL NFC-E
---

# 🇧🇷 BRAZIL NFC-E

| Proprietà             | Valore                                                  |
| --------------------- | ------------------------------------------------------- |
| **Paese / Regione**   | Brasile                                                 |
| **Tipi di documento** | Fattura al consumatore (Nota Fiscal de Consumidor Eletrônica) |
| **Formato**           | XML                                                     |
| **Standard**          | NFC-e 4.0 (fattura al consumatore per il commercio al dettaglio / punto vendita) |
| **Locale**            | `pt_BR`                                                 |

La NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) è la fattura elettronica brasiliana per le vendite al dettaglio ai consumatori finali. Condivide lo schema XML della NF-e (namespace `nfeProc`) ma utilizza il codice modello 65. I documenti NFC-e riportano in genere un CPF (codice fiscale della persona fisica) per l'acquirente al posto di un CNPJ e, per le semplici transazioni al dettaglio, non includono PIS/COFINS per riga.

## Stato del supporto

| Componente           | Stato         |
| -------------------- | ------------- |
| Anteprima            | ✅ Supportato |
| Estrazione dei campi | ✅ Supportato |
| Trasformazione       | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/brazil-nfce-preview.png" alt="Anteprima della NFC-e brasiliana in DocBits"><figcaption><p>Anteprima predefinita di DocBits per un documento BRAZIL NFC-E</p></figcaption></figure>

## Mappatura dei campi

### Campi di testata

| Campo DocBits   | XPath di origine                                           | Note                          |
| --------------- | ---------------------------------------------------------- | ----------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Numero della Nota Fiscal      |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 con offset BRT       |
| `currency`      | Fisso: `BRL`                                               | Sempre real brasiliano        |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Valore totale della NFC-e     |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Subtotale dei prodotti        |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | Totale imposta ICMS           |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Nome del rivenditore          |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` o `CPF` | CNPJ o CPF                    |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Nome del consumatore          |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CPF']` o `CNPJ` | CPF (persona fisica) o CNPJ   |

### Tabella delle righe articolo (`INVOICE_TABLE`)

Percorso della riga: `//*[local-name()='det']`

| Colonna        | XPath relativo                                                              | Note                              |
| -------------- | --------------------------------------------------------------------------- | --------------------------------- |
| `POSITION`     | `@nItem`                                                                    | Numero progressivo dell'articolo  |
| `ITEM_CODE`    | `*[local-name()='prod']/*[local-name()='cProd']`                            | Codice prodotto                   |
| `DESCRIPTION`  | `*[local-name()='prod']/*[local-name()='xProd']`                            | Descrizione del prodotto          |
| `NCM_CODE`     | `*[local-name()='prod']/*[local-name()='NCM']`                              | Classificazione doganale NCM      |
| `CFOP_CODE`    | `*[local-name()='prod']/*[local-name()='CFOP']`                             | Codice fiscale dell'operazione    |
| `UNIT`         | `*[local-name()='prod']/*[local-name()='uCom']`                             | Unità di misura                   |
| `QUANTITY`     | `*[local-name()='prod']/*[local-name()='qCom']`                             | Quantità commerciale              |
| `UNIT_PRICE`   | `*[local-name()='prod']/*[local-name()='vUnCom']`                           | Prezzo unitario                   |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']`                            | Totale di riga                    |
| `ICMS_AMOUNT`  | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Imposta ICMS per riga             |
| `VAT_RATE`     | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Aliquota ICMS (%)                 |

## Regola di classificazione

DocBits riconosce i documenti BRAZIL NFC-E tramite il pattern `<mod>65</mod>` all'interno di documenti XML con namespace `http://www.portalfiscal.inf.br/nfe`.

## Correlati

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documenti elettronici supportati](./)
