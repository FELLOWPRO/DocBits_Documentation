---
description: Supporto per documenti elettronici MEXICO CFDI 3.3 in DocBits
---

# 🇲🇽 MEXICO CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Messico](countries/mexico.md). Verificate lo spazio dei nomi, la versione e TipoDeComprobante. Un importo negativo non basta a identificare una nota di credito; l’analisi del file non certifica l’autorizzazione del SAT.
{% endhint %}

| Proprietà             | Valore                                             |
| --------------------- | -------------------------------------------------- |
| **Paese / Regione**   | Messico                                            |
| **Tipi di documento** | Fattura, nota di credito, ricevuta di pagamento              |
| **Formato**           | XML                                                |
| **Standard**          | CFDI 3.3 (Comprobante Fiscal Digital por Internet) |

CFDI 3.3 è la generazione precedente dello standard messicano di ricevuta fiscale digitale emesso dal SAT (Servicio de Administración Tributaria). Sebbene sia stato sostituito da CFDI 4.0, molte fatture storiche utilizzano ancora questa versione. Include l'UUID (folio fiscal), gli identificativi RFC e i calcoli delle imposte IEPS/IVA.

## Stato del supporto

| Componente         | Stato       |
| ------------------ | ----------- |
| Anteprima          | ✅ Supported |
| Estrazione campi   | ✅ Supported |
| Trasformazione     | ✅ Supported |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="Anteprima di una fattura Mexico CFDI 3.3 in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura Mexico CFDI 3.3</p></figcaption></figure>

## Correlati

* [Documenti elettronici supportati](./)
