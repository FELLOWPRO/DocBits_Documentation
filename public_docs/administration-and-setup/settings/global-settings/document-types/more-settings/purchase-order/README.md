# Ordine di acquisto

La scheda **Ordine di acquisto** in **Altre impostazioni** di un tipo di documento controlla come i documenti di quel tipo vengono confrontati con gli ordini di acquisto. Le impostazioni valgono per un tipo di documento alla volta: apri quindi prima il tipo di documento che vuoi modificare in **Impostazioni → Tipi di Documento**.

Per trovare le impostazioni di una fattura:

1. Apri **Impostazioni → Tipi di Documento**.
2. Individua la scheda **Fattura** e seleziona l'icona a ingranaggio (**Altre impostazioni**).
3. Apri la sezione **Ordine di acquisto** per rivedere le sue opzioni di corrispondenza e convalida.

<figure><img src="../../../../../../.gitbook/assets/purchase-order-invoice-card-it-20261112.png" alt="Scheda Fattura del tipo di documento con l'icona a ingranaggio di Altre impostazioni in alto a destra"><figcaption><p>La scheda <strong>Fattura</strong> nella versione attuale della sandbox in italiano. L'icona a ingranaggio apre Altre impostazioni; gli altri controlli della scheda riguardano il tipo di documento.</p></figcaption></figure>

Sulla scheda compaiono anche **Attivare**, **Estrazione** e i collegamenti sotto il nome del documento. Questi controlli riguardano il tipo di documento stesso e sono spiegati nella pagina [Tipi di documento](../../README.md), in «Controlli su una scheda del tipo di documento». Che cosa sono le schede comprimibili di Altre impostazioni è descritto in [Altre impostazioni](../README.md).

<figure><img src="../../../../../../.gitbook/assets/purchase-order-po-section-it-20261112.png" alt="Sezione Ordine di acquisto compressa con il sottotitolo Corrispondenza e convalida degli ordini di acquisto"><figcaption><p>La sezione <strong>Ordine di acquisto</strong> in Altre impostazioni, compressa. Apri l'intestazione per vedere le opzioni; per questa cattura non è stata modificata alcuna impostazione.</p></figcaption></figure>

Inizia dalle regole di corrispondenza e dalle tolleranze, poi regola il comportamento dopo una corrispondenza e in fase di esportazione:

* [Regole di Corrispondenza degli Ordini di Acquisto](purchase-order-matching-rules.md) e [Impostazioni di tolleranza per gli ordini di acquisto / Ulteriore tolleranza per gli ordini di acquisto](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) definiscono come vengono confrontate le righe della fattura e dell'ordine di acquisto.
* [Opzioni di Auto Match & Export](auto-match-and-export-options.md), [Esporta righe di PO non corrispondenti](export-not-matched-po-lines.md) e [Esportazione alternativa](alternate-export.md) riguardano ciò che accade dopo una corrispondenza.
* [Tabella PO nel generatore di layout](po-table-in-layout-builder.md), [Stato della riga PO consumata](consumed-po-line-status.md) e [Calcolare il prezzo unitario del PO](calculate-po-unit-price.md) cambiano ciò che gli utenti vedono nella vista di corrispondenza.
* [Controllo automatico degli aggiornamenti PO](auto-check-for-po-updates.md), [Stati di disabilitazione dell'OP](purchase-order-disable-statuses.md) e [Aggiornare lo stato dell'ordine di acquisto del documento](update-document-purchase-order-status.md) controllano come i dati e gli stati degli ordini di acquisto restano aggiornati.
* [Mappa dei Numeri di Articolo Fornitore - Documentazione Amministrativa](supplier-item-number-map-admin-documentation.md) e la pagina generale [Ordine di acquisto](purchase-order.md) offrono ulteriori informazioni.

Le impostazioni possono influire sui documenti in lavorazione. Verifica le modifiche con un documento di prova prima di salvarle in produzione.

Questa panoramica mostra dove si trovano le impostazioni. Non conferma una corrispondenza PO né un'esportazione già eseguite.
