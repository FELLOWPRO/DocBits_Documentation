---
description: Supporto per documenti elettronici KSEF in DocBits
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Polonia](countries/poland.md). FA2 e FA3 usano strutture diverse. Confermate lo schema sorgente e provate la mappatura appropriata; l’analisi del file non invia una fattura a KSeF.
{% endhint %}

| Proprietà             | Valore                                   |
| --------------------- | ---------------------------------------- |
| **Paese / Regione**   | Polonia                                  |
| **Tipi di documento** | Fattura, nota di credito, fattura correttiva |
| **Formato**           | XML                                      |
| **Standard**          | KSeF (Krajowy System e-Faktur)           |

KSeF è il Sistema nazionale polacco di fatturazione elettronica, gestito dal Ministero delle Finanze. Diventerà obbligatorio per tutte le imprese polacche registrate ai fini IVA. DocBits supporta le versioni di schema KSeF FA2 e FA3 per l'elaborazione delle fatture.

## Stato del supporto

| Componente         | Stato       |
| ------------------ | ----------- |
| Anteprima          | ✅ Supported |
| Estrazione campi   | ✅ Supported |
| Trasformazione     | ✅ Supported |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Anteprima di una fattura KSeF in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura KSeF della Polonia</p></figcaption></figure>

## Correlati

* [Documenti elettronici supportati](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
