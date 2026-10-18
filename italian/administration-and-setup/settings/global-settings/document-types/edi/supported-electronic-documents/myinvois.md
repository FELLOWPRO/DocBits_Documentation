---
description: Supporto per documenti elettronici MYINVOIS in DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Malaysia](countries/malaysia.md). Il percorso di estrazione esaminato si basa su XML. La piattaforma nazionale accetta anche JSON, ma ciò non dimostra il supporto per l’importazione JSON in questa mappatura DocBits.
{% endhint %}

| Proprietà             | Valore                                                |
| --------------------- | ----------------------------------------------------- |
| **Paese / Regione**   | Malesia                                               |
| **Tipi di documento** | Invoice, Credit Note, Debit Note, Self-Billed Invoice |
| **Formato**           | UBL 2.1 XML                                    |
| **Standard**          | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)          |

MyInvois è il sistema di fatturazione elettronica della Malesia, gestito dall'Agenzia delle entrate (LHDN). In vigore da agosto 2024 per le grandi imprese, richiede che tutte le fatture siano inviate al portale MyInvois per la convalida e ricevano un identificativo univoco. Il sistema utilizza UBL 2.1 e supporta sia il formato XML sia il formato JSON per l'invio.

## Stato del supporto

| Componente         | Stato       |
| ------------------ | ----------- |
| Anteprima          | ✅ Supported |
| Estrazione campi   | ✅ Supported |
| Trasformazione     | ✅ Supported |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="Anteprima di una fattura MyInvois in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura MyInvois della Malesia</p></figcaption></figure>

## Correlati

* [Documenti elettronici supportati](./)
