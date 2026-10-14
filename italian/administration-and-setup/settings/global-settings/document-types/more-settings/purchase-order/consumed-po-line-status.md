# Stato della riga PO consumata

**Stato della riga PO consumata** colora le righe dell'ordine di acquisto (PO) nella schermata di abbinamento in base alla quantità di ciascuna riga già abbinata. Attivalo per il tipo di documento che usi per le fatture se il tuo team deve riconoscere rapidamente le righe PO non usate, parzialmente usate e completamente usate. Il colore è solo un aiuto visivo; controlla la **Quantità corrispondente** e la colonna della quantità PO selezionata prima di decidere se una riga può essere abbinata di nuovo.

## Attivare l'impostazione

1. Apri **Impostazioni → Tipi di Documento**. Trova il tipo di documento che usi per le fatture e seleziona l'icona dell'ingranaggio sulla sua scheda per aprire **Altre impostazioni**. Lo screenshot mostra la scheda **Fattura**. Lascia invariati gli interruttori **Attivare** ed **Extraction**.

   <figure><img src="../../../../../../.gitbook/assets/1-consumed-po-line-document-types-it.png" alt="Pagina Tipi di Documento con la scheda Fattura e l'ingranaggio di Altre impostazioni"><figcaption><p>Apri Altre impostazioni dalla scheda Fattura.</p></figcaption></figure>

2. Espandi **Ordine di acquisto** se è contratto. Trova **Stato della linea PO consumata** e attiva il suo interruttore. È un'impostazione separata da **Aggiorna lo stato dell'ordine di acquisto del documento**, più in basso nella stessa sezione.

   <figure><img src="../../../../../../.gitbook/assets/2-consumed-po-line-settings-it.png" alt="Sezione Ordine di acquisto di Altre impostazioni con l'interruttore Stato della linea PO consumata visibile"><figcaption><p>Scegli l'interruttore Stato della linea PO consumata.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/3-consumed-po-line-toggle-it.png" alt="Vista ravvicinata dell'etichetta Stato della linea PO consumata e del suo interruttore"><figcaption><p>In questo esempio l'interruttore è spento; attivalo per vedere i colori di abbinamento.</p></figcaption></figure>

3. Apri una fattura con l'abbinamento dell'ordine di acquisto e controlla le sue righe PO. Gli esempi qui sotto mostrano come i colori delle righe si collegano allo stato di abbinamento. Per i passaggi di abbinamento, vedi [Schermata di Abbinamento Ordini di Acquisto](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Leggere i colori delle righe PO

| Aspetto | Significato | Cosa controllare |
| --- | --- | --- |
| Neutro o bianco | Nessuna quantità di questa riga PO è ancora stata abbinata. | Controlla la quantità della PO e la riga della fattura prima di abbinare. |
| Tinta blu | Hai selezionato la riga nella schermata di abbinamento attuale. | La selezione è temporanea; non significa che la riga sia completamente abbinata. |
| Arancione pallido | Una parte della quantità è stata abbinata, ma la quantità corrispondente è inferiore alla quantità PO selezionata. | Controlla quanta quantità rimane. |
| Viola pallido | La quantità corrispondente raggiunge almeno la quantità PO selezionata. | Non dare per scontato che ci sia altra quantità disponibile. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="Riga PO con quantità corrispondente zero e nessun colore di stato"><figcaption><p>Nessuna quantità è ancora stata abbinata.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="Riga PO con tinta blu di selezione nella schermata di abbinamento"><figcaption><p>La riga è selezionata per l'abbinamento attuale.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="Riga PO con sfondo arancione pallido e quantità corrispondente inferiore alla quantità della PO"><figcaption><p>La riga è parzialmente usata.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="Riga PO con sfondo viola pallido e quantità corrispondente pari alla quantità della PO"><figcaption><p>La riga è completamente usata.</p></figcaption></figure>

Una riga barrata ha un altro significato: il suo stato PO potrebbe essere escluso da [Stati di disabilitazione dell'OP](purchase-order-disable-statuses.md). Controlla quell'impostazione se una riga non può essere selezionata.
