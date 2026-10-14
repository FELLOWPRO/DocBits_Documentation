---
description: Supporto in DocBits per il documento elettronico BRAZIL CT-E
---

# 🇧🇷 BRAZIL CT-E

| Proprietà            | Valore                                                    |
| -------------------- | --------------------------------------------------------- |
| **Paese / Regione**  | Brasile                                                   |
| **Tipi di documento**| Fattura di trasporto (Conhecimento de Transporte Eletrônico) |
| **Formato**          | XML                                                       |
| **Standard**         | CT-e 3.0 (lettera di vettura / polizza di trasporto elettronica) |
| **Locale**           | `pt_BR`                                                   |

Il CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) è il documento di trasporto elettronico brasiliano emesso da aziende di logistica e spedizioni. Documenta il servizio di trasporto, il valore del carico, i comuni di origine e destinazione (`cMunIni` / `cMunFim`) e il prezzo del nolo (`vTPrest`). A differenza della NF-e, il CT-e utilizza `cteProc` come elemento radice e fa riferimento ai documenti NF-e collegati.

## Stato del supporto

| Componente             | Stato        |
| ---------------------- | ------------ |
| Anteprima              | ✅ Supportato |
| Estrazione dei campi   | ✅ Supportato |
| Trasformazione         | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/brazil-cte-preview.png" alt="Anteprima del CT-e brasiliano in DocBits"><figcaption><p>Anteprima predefinita di DocBits per un documento BRAZIL CT-E</p></figcaption></figure>

## Mappatura dei campi

### Campi di testata

| Campo DocBits   | XPath di origine                                       | Note                                  |
| --------------- | ------------------------------------------------------ | ------------------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nCT']`        | Numero del CT-e                       |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`      | ISO 8601 con offset BRT               |
| `currency`      | Fisso: `BRL`                                           | Sempre real brasiliano                |
| `total_amount`  | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Valore totale del servizio di trasporto |
| `net_amount`    | `//*[local-name()='vPrest']/*[local-name()='vRec']`    | Importo da ricevere                   |
| `tax_amount`    | `//*[local-name()='ICMS']//*[local-name()='vICMS']`    | ICMS sul servizio di trasporto        |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`     | Nome del vettore (transportadora)     |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']`      | CNPJ del vettore                      |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`     | Nome del destinatario (destinatário)  |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CNPJ']`      | CNPJ del destinatario                 |

> Il CT-e non include una tabella di righe articolo: il servizio di trasporto è un unico addebito a livello di documento.

## Regola di classificazione

DocBits riconosce i documenti BRAZIL CT-E tramite:

```
http://www.portalfiscal.inf.br/cte
```

nel namespace XML (elemento radice `<cteProc>`).

## Correlati

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documenti elettronici supportati](./)
