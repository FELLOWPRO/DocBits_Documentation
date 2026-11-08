# Esempi pratici: prezzo e quantità

<!-- touchless-admin-video-v2-20261104:start -->
**Capitolo video (versione di verifica):** [Seguire un documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Esempio pratico: estrazione corretta, dati Infor diversi

Questo è un caso illustrativo, separato dalle schermate. La fattura mostra **10 unità a €10,00 ciascuna**, totale **€100,00**. DocBits estrae correttamente tutti e tre i valori. L'ordine Infor importato mostra **10 unità a €9,00 ciascuna**, totale **€90,00**. Supponi che i controlli di abbinamento configurati blocchino questa differenza di prezzo.

1. **Controlla l'estrazione:** confronta la fattura originale con la quantità, il prezzo unitario e l'importo di riga estratti. Corrispondono, quindi per questi valori non c'è un errore di estrazione dimostrato.
2. **Controlla la fonte:** confronta l'ordine importato con l'ordine Infor attuale, compresi unità di prezzo e momento dell'importazione. Un'importazione obsoleta e un ordine Infor errato richiedono correzioni diverse.
3. **Chiarisci il valore aziendale:** in questo esempio l'ufficio acquisti conferma che €10,00 era il prezzo concordato e corregge l'ordine Infor. Se il prezzo concordato fosse stato €9,00, sarebbe invece la fattura del fornitore a richiedere un chiarimento.
4. **Verifica l'importazione corretta:** controlla che i valori corretti dell'ordine siano effettivamente arrivati a DocBits prima di riprovare.
5. **Registra l'azione AP:** AP riavvia manualmente questa fattura in DocBits; dopo il completamento riuscito è **AP assisted**. Estrazione corretta e processo non touchless possono essere entrambi veri.
6. **Controlla le fatture successive:** verifica che abbinamento ed esportazione ora si completino senza un'altra correzione o un altro riavvio. La fattura già trattata resta trattata; le fatture successive forniscono la prova del miglioramento.

{% hint style="warning" %}
Non modificare un €10,00 estratto correttamente in €9,00 solo per corrispondere a un ordine errato, e non allargare una tolleranza al solo scopo di nascondere la discrepanza. Conferma il valore concordato e correggi il dato o la configurazione responsabile. Un bloccante di abbinamento indica dove il processo si è fermato, non chi lo ha causato.
{% endhint %}

Vedi [Touchless Intelligence](./) per l'esempio separato sulla qualità dell'estrazione e per il calcolo AP touchless, e [Tracciamento del documento](touchless-document-trace.md) per le prove da confrontare.

## Tre ordini dimostrativi propri: valori corrispondenti, prezzo e quantità

Questi ordini sono stati creati appositamente in **Dev**. Fornitore, articolo e fatture sono fittizi. Ogni fattura contiene **10 unità × €10 = €100 netti**. Le schede contengono ritagli reali dell'interfaccia inglese e dettagli numerici ingranditi. Non mostrano una connessione Infor di un cliente reale, un'estrazione dimostrata né un processo di fattura automatico completato con successo.

| Caso | Fattura | PO importato | Che cosa stabilisce il confronto |
| --- | --- | --- | --- |
| PO01 / RE01: valori corrispondenti | 10 × €10 = €100 | 10 × €10 = €100 | I valori di origine concordano; Pure Touchless richiede comunque un'estrazione corretta e un completamento confermato senza interventi né approvazione |
| PO02 / RE02: discrepanza di prezzo | 10 × €10 = €100 | 10 × €9 = €90 | Differenza di riga di €10; il prezzo unitario differisce di circa l'11,11% rispetto al prezzo del PO. Sono le regole attive effettive a decidere se blocca |
| PO03 / RE03: discrepanza di quantità | 10 × €10 = €100 | 8 × €10 = €80 | 2 unità in più, il 25% rispetto alla quantità ordinata. Controlla la quantità aperta/ricevuta e la quantità di confronto configurata |

<figure><img src="../../../.gitbook/assets/touchless-owned-po-match-it.png" alt="Scheda esplicativa FELLOW con il reale ordine di acquisto Dev inglese PO01 che mostra quantità dieci, prezzo unitario dieci e importo cento"><figcaption><p>Valori corrispondenti nel PO01 fittizio. La riga nativa ingrandita mostra quantità, prezzo unitario e importo. La sola concordanza non dimostra né un'estrazione corretta né Pure Touchless.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-it.png" alt="Scheda esplicativa FELLOW con il reale ordine di acquisto Dev inglese PO02 che mostra dieci unità a nove e un importo di novanta rispetto a un importo fattura di cento"><figcaption><p>Esempio di prezzo PO02: l'ordine importato mostra effettivamente 10 × 9 = 90, rispetto a 10 × 10 = 100 della fattura fittizia. Controlla prezzo concordato, unità di prezzo e importazione. Un intervento umano registrato seguito da un completamento riuscito è AP Assisted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-quantity-it.png" alt="Scheda esplicativa FELLOW con il reale ordine di acquisto Dev inglese PO03 che mostra otto unità a dieci, importo ottanta, rispetto a dieci unità fatturate"><figcaption><p>Esempio di quantità PO03: il PO importato contiene 8 unità, la fattura 10. La quantità ricevuta è vuota in questo test e non dimostra alcuna consegna. Queste schede spiegano il confronto; non dimostrano un abbinamento riuscito.</p></figcaption></figure>

## Pagine correlate

* [Touchless Intelligence](./)
* [Metriche e calcolo](../../touchless-metrics.md)
* [Usare il pannello](touchless-dashboard.md)
* [Diagnosi del fornitore e cluster di problemi](../../touchless-supplier-diagnosis.md)
* [Diagnosi dell'abbinamento ordini](../../touchless-po-matching-diagnosis.md)
* [Tracciamento del documento](touchless-document-trace.md)
* [Proposte di modifica e report](touchless-change-proposals.md)
* [Spiegare e migliorare Touchless con MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
