---
description: Supporto in DocBits per il documento elettronico BRAZIL NFS-E
---

# 🇧🇷 BRAZIL NFS-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Brasile](countries/brazil.md). Sono famiglie di documenti diverse. Una versione NFS-e configurata non certifica ogni schema comunale né ogni tracciato nazionale di fattura per servizi.
{% endhint %}

| Proprietà             | Valore                                                                         |
| --------------------- | ------------------------------------------------------------------------------ |
| **Paese / Regione**   | Brasile                                                                        |
| **Tipi di documento** | Fattura di servizi (Nota Fiscal de Serviços Eletrônica)                        |
| **Formato**           | XML                                                                            |
| **Standard**          | NFS-e 2.04 (standard nazionale ABRASF per le fatture di servizi comunali)      |
| **Locale**            | `pt_BR`                                                                        |

La NFS-e (Nota Fiscal de Serviços Eletrônica) è la fattura elettronica brasiliana per i servizi, emessa a livello comunale. DocBits supporta lo schema standard ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais). I documenti NFS-e utilizzano una struttura XML diversa dalla NF-e: l'imposta principale è l'ISS (Imposto Sobre Serviços) anziché l'ICMS, e fornitore/acquirente sono denominati `PrestadorServico` / `TomadorServico`. L'elemento `Discriminacao` contiene la descrizione del servizio in testo libero.

## Stato del supporto

| Componente           | Stato         |
| -------------------- | ------------- |
| Anteprima            | ✅ Supportato |
| Estrazione dei campi | ✅ Supportato |
| Trasformazione       | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/brazil-nfse-preview.png" alt="Anteprima della NFS-e brasiliana in DocBits"><figcaption><p>Anteprima predefinita di DocBits per un documento BRAZIL NFS-E</p></figcaption></figure>

## Mappatura dei campi

### Campi di testata

| Campo DocBits   | XPath di origine                                                      | Note                                   |
| --------------- | --------------------------------------------------------------------- | -------------------------------------- |
| `invoice_id`    | `//*[local-name()='Numero']`                                          | Numero della NFS-e                     |
| `invoice_date`  | `//*[local-name()='DataEmissao']`                                     | Data di emissione ISO 8601             |
| `currency`      | Fisso: `BRL`                                                          | Sempre real brasiliano                 |
| `total_amount`  | `//*[local-name()='ValorServicos']`                                   | Valore lordo dei servizi               |
| `net_amount`    | `//*[local-name()='ValorLiquidoNfse']`                                | Valore netto dopo le detrazioni        |
| `tax_amount`    | `//*[local-name()='ValorIss']`                                        | ISS (imposta comunale sui servizi)     |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Nome del prestatore di servizi         |
| `supplier_id`   | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']`        | CNPJ del prestatore                    |
| `buyer_name`    | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']`   | Nome del committente del servizio      |
| `buyer_id`      | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']`          | CNPJ del committente                   |

> La NFS-e descrive un unico servizio nell'elemento `Discriminacao` anziché righe articolo. Non viene estratta alcuna `INVOICE_TABLE`.

## Regola di classificazione

DocBits riconosce i documenti BRAZIL NFS-E tramite il namespace:

```
http://www.abrasf.org.br/nfse.xsd
```

## Correlati

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [Documenti elettronici supportati](./)
