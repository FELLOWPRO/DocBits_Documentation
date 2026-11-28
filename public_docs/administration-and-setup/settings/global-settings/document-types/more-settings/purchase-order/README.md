# Ordine di acquisto

La scheda **Purchase Order** nei **More Settings** di un tipo di documento controlla come i documenti di quel tipo vengono abbinati agli ordini di acquisto. Le impostazioni valgono per un tipo di documento alla volta, quindi apri prima il tipo di documento che vuoi modificare in **Settings → Document Types**.

Per trovare le impostazioni di una fattura:

1. Apri **Settings → Document Types**.
2. Trova la scheda **Invoice** e seleziona l'icona a ingranaggio (**More Settings**).
3. Apri la sezione **Purchase Order** per esaminare le opzioni di abbinamento e validazione.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>La scheda Invoice nell'attuale ambiente di test Dev inglese. Usa l'icona a ingranaggio per aprire More Settings; gli altri controlli si applicano al tipo di documento.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>La sezione Purchase Order in More Settings, mostrata chiusa. Espandi l'intestazione per vedere le opzioni; per questa acquisizione non è stata modificata alcuna impostazione.</p></figcaption></figure>

Inizia con le regole di abbinamento e le tolleranze, poi regola il comportamento di abbinamento ed esportazione:

* [Regole di Corrispondenza degli Ordini di Acquisto](purchase-order-matching-rules.md) e [Impostazioni di tolleranza per gli ordini di acquisto / Ulteriore tolleranza per gli ordini di acqui](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) definiscono come vengono confrontate le righe di fattura e di ordine.
* [Opzioni di Auto Match & Export](auto-match-and-export-options.md), [Esporta righe di PO non corrispondenti](export-not-matched-po-lines.md) e [Esportazione alternativa](alternate-export.md) descrivono cosa succede dopo un abbinamento.
* [Quantità esportata nell'unità di misura base](export-quantity-in-base-unit-of-measure.md) converte la quantità e il prezzo unitario esportati nell'unità di misura base, per l'esportazione verso Infor LN.
* [Table PO dans le Constructeur de Mise en Page](po-table-in-layout-builder.md), [Stato della riga dell'ordine d'acquisto consumato](consumed-po-line-status.md) e [Calcolare il prezzo unitario del PO](calculate-po-unit-price.md) cambiano ciò che gli utenti vedono nella vista di abbinamento.
* [Controllo automatico degli aggiornamenti PO](auto-check-for-po-updates.md), [Stati di disabilitazione dell'OP](purchase-order-disable-statuses.md) e [Aggiornare lo stato dell'ordine di acquisto del documento](update-document-purchase-order-status.md) controllano come vengono mantenuti aggiornati i dati e gli stati dell'ordine di acquisto.
* [Mappa dei Numeri di Articolo Fornitore - Documentazione Amministrativa](supplier-item-number-map-admin-documentation.md) e la pagina generale [Ordine di acquisto](purchase-order.md) forniscono ulteriore contesto.

Le impostazioni possono influire sui documenti in produzione. Verifica le modifiche con un documento di prova prima di salvarle in produzione.

Questa panoramica mostra dove trovare le impostazioni. Non verifica un abbinamento PO né un'esportazione completati.
