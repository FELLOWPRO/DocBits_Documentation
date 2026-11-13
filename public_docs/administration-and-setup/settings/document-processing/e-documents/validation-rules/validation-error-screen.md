# La schermata di errore per una fattura elettronica rifiutata

> In questa versione alcuni testi dell’interfaccia possono essere ancora in inglese o tradotti in modo errato. La guida ne spiega il significato; le schermate mostrano l’interfaccia originale.

Quando carichi una fattura elettronica errata, DocBits non la perde. Il documento riceve lo stato **Error** e la schermata di errore ti dice cosa non va, dove e cosa fare dopo. Questa pagina mostra due esempi: un file XML non ben formato e una fattura che viola una regola aziendale.

> Una fattura riceve lo stato **Error** solo quando la validazione è **on** e **blocking** per il suo tipo di documento. Vedi [Validazione per ogni tipo di documento](validation-per-document-type.md).

Una e-invoice rifiutata dal validatore porta il proprio stato di validazione e-invoice invece di un semplice **Error**. Il badge di stato nella dashboard aggiunge un tooltip che indica perché il documento si è fermato, così puoi distinguere una fattura rifiutata dagli altri errori mentre filtri l'elenco dei documenti. La schermata di errore e il report qui sotto sono identici in entrambi i casi.

## Esempio 1: il file XML è danneggiato

Un fornitore invia un file XML in cui un tag di chiusura non corrisponde al tag di apertura. Il file non può essere letto, quindi DocBits si ferma al primo controllo, **L1 · Well-formedness**.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-xml-malformed-it.png" alt="The error screen for a damaged XML file. The faulty line is marked in the XML. Example file with fictional data."><figcaption><p>Schermata di errore di un XML fittizio con un tag di chiusura volutamente errato. In questa versione alcuni testi dell’interfaccia possono essere ancora in inglese o tradotti in modo errato. La guida ne spiega il significato; le schermate mostrano l’interfaccia originale.</p></figcaption></figure>

La schermata ha due lati:

* **A sinistra: il file XML.** DocBits mostra il file con i numeri di riga. La riga con il problema è evidenziata in rosso. Usa i pulsanti sopra il file per copiare l'XML o aprirlo in una nuova scheda.
* **A destra: la spiegazione.** La scheda **Rejected by** indica il controllo che ha fermato il file (qui **L1 · Well-formedness**) e il codice della regola (qui `XML-PARSE`). Sotto vedi un titolo in linguaggio semplice (*Il file XML non è ben formato*), una breve spiegazione e il blocco **Next step**.

Seleziona **View validation details** per aprire il [rapporto di convalida](validation-report.md) completo.

<figure><img src="../../../../../.gitbook/assets/einvoice-report-xml-malformed-it.png" alt="The report of the damaged file: one error at level 1 Syntax, with the technical message and the position"><figcaption><p>Rapporto del file danneggiato: un errore al livello 1 Sintassi, con il messaggio tecnico e la posizione.</p></figcaption></figure>

Il rapporto indica la posizione esatta (qui riga 5, colonna 4081) e riporta il messaggio tecnico del parser XML. Seleziona **Show in XML** per passare a quella riga. L'indicazione **How to fix** ti dice di chiedere al mittente un file corretto.

## Esempio 2: la fattura viola una regola aziendale

L'XML è corretto, ma manca un campo obbligatorio. Ad esempio, il venditore non può essere identificato perché non è presente alcun identificativo del venditore, identificativo di registrazione o identificativo IVA (regola `BR-CO-26`).

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view-it.png" alt="The error screen for a business-rule error: the layer L3 · Business Rules, the rule code and a next step"><figcaption><p>Schermata di errore di una fattura di esempio interamente fittizia: il livello L3 · Business Rules, il codice della regola e un passo successivo. In questa versione alcuni testi dell’interfaccia possono essere ancora in inglese o tradotti in modo errato. La guida ne spiega il significato; le schermate mostrano l’interfaccia originale.</p></figcaption></figure>

La scheda indica il livello **L3 · Business Rules** e il codice `BR-CO-26`. Il rapporto elenca tutti gli esiti della fattura, vedi [Rapporto di convalida](validation-report.md).

## Quando DocBits non ha potuto controllare il documento

Non ogni errore è un rifiuto. Se il validatore non riesce a leggere il file, il messaggio inizia con _could not check this document_ e indica il controllo che lo ha fermato, per esempio `XML-PARSE` per un file XML danneggiato o `PDF-UNREADABLE` per un PDF che non si apre. DocBits mostra la stessa scheda di spiegazione di una fattura rifiutata, con il nome del controllo, il codice e il messaggio tecnico.

Si tratta di un guasto tecnico, non di un giudizio sulla fattura:

* DocBits non contrassegna il documento come rifiutato.
* Un riavvio può riuscire, perché la causa può risiedere nella lettura del file. Seleziona **Restart Processing** prima di chiedere al mittente una nuova fattura.
* Se lo stesso codice ricompare dopo un riavvio, invia il file e il codice al tuo amministratore.

## Il riquadro Next step e i pulsanti

Per una fattura elettronica non valida la pagina inizia con un riquadro **Next step**. Contiene l'azione che aiuta in questo caso:

| Azione | Cosa fa |
| --- | --- |
| **Reject** | Rifiuta il documento. La finestra indica il file, il fornitore e il numero di fattura, ti informa che il documento riceve lo stato **Rejected** con una nota nella sua cronologia e che il fornitore non viene avvisato, e spiega come annullare il rifiuto. Chiede un motivo e conferma con **Reject now**. Se qualcosa fallisce, il messaggio compare nella finestra e puoi riprovare. |
| **Download invoice XML** | Scarica il file così come è stato ricevuto, ad esempio per verificarlo fuori da DocBits o per restituirlo al fornitore. |
| **Print report** | Stampa il [rapporto di convalida](validation-report.md). |

La scheda nomina inoltre il controllo in parole comprensibili, con il codice della regola come piccolo riferimento.

**Restart Processing** esegue di nuovo l'elaborazione del documento, ad esempio dopo aver modificato un'impostazione; il controllo usa le impostazioni attuali. Si trova sotto il riquadro Next step perché un riavvio di un file invariato fallisce allo stesso modo. Gli altri pulsanti restano accanto:

| Pulsante | Cosa fa |
| --- | --- |
| **Restart Processing** | Esegue di nuovo l'elaborazione del documento, ad esempio dopo aver modificato un'impostazione. Il controllo usa le impostazioni attuali. |
| **View DocFlow** | Mostra il workflow del documento. |
| **Copy Details** | Copia i dettagli dell'errore, ad esempio per un messaggio al tuo amministratore. |
| **Create ticket** | Apre un ticket di supporto con i dettagli dell'errore. |

Seleziona **Show technical details** sulla scheda per le informazioni tecniche grezze.

Mentre il motivo si carica, la pagina mostra un segnaposto invece di una scheda scritta a metà. Se il motivo non può essere caricato, la pagina propone di ricaricarlo, e un passo il cui nome è sconosciuto viene contrassegnato come tale invece di mostrare un campo vuoto. Su uno schermo stretto XML e spiegazione sono impilati invece di stare fianco a fianco.

## Cosa fare dopo

* **Errori:** chiedi al mittente una fattura corretta oppure [rifiuta il documento](validation-next-step-and-reject.md). Una fattura corretta è un nuovo documento.
* **Solo avvertenze:** il documento non è bloccato. Puoi continuare.

## Pagine correlate

* [Rapporto di convalida](validation-report.md): tutti i risultati, livello per livello.
* [Passo successivo e rifiuto di un documento](validation-next-step-and-reject.md)
* [Validazione per ogni tipo di documento](validation-per-document-type.md): attiva la validazione e imposta il blocco.
