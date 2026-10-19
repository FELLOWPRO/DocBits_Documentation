---
description: Supporto per documenti elettronici INVOIC02 in DocBits
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Internazionale](countries/international.md). Le mappature per fatture, ordini, risposte e avvisi di spedizione sono distinte. L’elaborazione dei file non fornisce, di per sé, un punto di accesso Peppol o la connettività con i partner commerciali.
{% endhint %}

| Proprietà             | Valore                  |
| --------------------- | ----------------------- |
| **Paese / Regione**   | Internazionale          |
| **Tipi di documento** | Invoice                 |
| **Formato**           | EDIFACT                 |
| **Standard**          | UN/EDIFACT INVOIC D.02B |

INVOIC02 è un messaggio di fattura UN/EDIFACT basato sulla versione di directory D.02B. EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) è uno standard EDI molto diffuso nella logistica, nella vendita al dettaglio e nella produzione. DocBits analizza la struttura dei segmenti EDIFACT ed estrae i campi di intestazione, di riga e di riepilogo.

## Stato del supporto

| Componente         | Stato       |
| ------------------ | ----------- |
| Anteprima          | ✅ Supported |
| Estrazione campi   | ✅ Supported |
| Trasformazione     | ✅ Supported |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="Anteprima di una fattura INVOIC02 in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura INVOIC02</p></figcaption></figure>

## Correlati

* [Documenti elettronici supportati](./)
