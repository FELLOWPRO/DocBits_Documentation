# Touchless Intelligence: Tracciamento del documento

Inserite un ID documento in **Document ID**, oppure aprite un documento di esempio da un cluster, per vedere **che cosa è successo a questo documento**.

L'intestazione mostra il file, il suo stato (ad esempio **In corso**), l'esecuzione che state consultando e il suo primo bloccante, oltre a un pulsante **Documento** con l'ID del documento.

<figure><img src="../.gitbook/assets/touchless-document-trace-pipeline-it.png" alt="La pagina Tracciamento del documento con l'intestazione del file, il Percorso della condotta a 14 passaggi e l'inizio del registro dei passaggi"><figcaption><p>Il tracciamento del documento: il percorso della condotta con tutti i passaggi e il registro dei passaggi con ciò che ognuno ha registrato.</p></figcaption></figure>

Il **Percorso della condotta** mostra 14 passaggi: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Ogni passaggio porta un solo stato:

| Stato | Significato |
| --- | --- |
| **Superato** (verde) | Il passaggio è andato a buon fine |
| **Mi sono fermato qui** (arancione) | Il passaggio ha bloccato il documento |
| **Prossimamente** | Il documento non è mai arrivato fin qui |
| **Niente di registrato** (tratteggiato) | Per questo passaggio non è stato registrato alcun dato |
| **Non applicabile** | Il passaggio non si applica a questo documento |

### Registro dei passaggi

Il **registro dei passaggi** sotto il percorso elenca gli stessi passaggi con ciò che ciascuno ha registrato. Un punto di stato e la parola di stato si trovano a sinistra e a destra di ogni riga.

* Ogni valore è un **chip di valore**: un numero con la sua unità, ad esempio **Affidabilità 100 %**, **Soglia 60 %**, **Regole fallite 0**, **8 campi mancanti** o **0 lacune di abbinamento**. Le percentuali sono mostrate come `97 %`, mai come `0.97`.
* **Dettagli** apre l'elenco completo dei valori registrati da un passaggio, comprese le alternative che ha considerato.
* Il passaggio che ha bloccato il documento ne indica il motivo, ad esempio **Convalida del campo non riuscita**.
* Un valore che nessun passaggio ha registrato compare come **Non registrato**, mai come valore inventato. I valori sono numeri e termini fissi, mai testo del documento.
* **Mostra diagnostica grezza** attiva i dati grezzi quando l'assistenza li richiede.

<figure><img src="../.gitbook/assets/touchless-document-trace-stage-log-it.png" alt="Il registro dei passaggi con i punti di stato, chip di valore come Soglia 60 percento e 8 campi mancanti, il passaggio bloccato Field Validation e la cronologia delle esecuzioni a destra"><figcaption><p>Ogni passaggio mostra ciò che ha registrato; il passaggio bloccato indica la sua causa.</p></figcaption></figure>

### Esecuzioni e modifiche

Il selettore di esecuzione in cima al registro dei passaggi (**Eseguire 1 · Attuale**) passa da un'esecuzione all'altra del documento. La **cronologia delle esecuzioni** a destra elenca ogni esecuzione con il suo esito e il punto in cui si è fermata. Quando un documento è stato eseguito più di una volta, scegliete un'esecuzione nel selettore per confrontarla con quella attuale: i valori modificati portano allora un contrassegno con la differenza e la sua unità, ad esempio **−2 campi** o **+3 %**.

La scheda **Documento** accanto al registro dei passaggi indica il tipo di documento, il fornitore, il numero di fattura, l'ordine d'acquisto, il numero di pagine e se l'analisi è basata su **regole** o scritta da un'IA.

**Esempio.** I documenti di un fornitore si fermano tutti al passaggio 8. Nel tracciamento vedete ogni volta gli stessi campi mancanti. Non è un problema di estrazione dei singoli documenti, ma un valore predefinito mancante nella configurazione dei campi: correggetelo una volta e l'intero cluster è recuperabile.

## Separare estrazione e dati di origine

Confrontate originale e campi/righe estratti prima delle correzioni. Poi confrontate l’ordine importato con Infor attuale, includendo unità, unità di prezzo e data di importazione. Distinguete originale contro estrazione, estrazione corretta contro ordine importato e Infor contro la sua copia. Un passaggio riuscito non certifica tutti i valori. Se la prova manca, lasciate aperta la causa.

**Esempio:** originale ed estrazione indicano 10 €, ordine importato 9 €. È una discrepanza con l’ordine, non un errore di estrazione dimostrato. Confermate il prezzo concordato. Un riavvio umano seguito da successo dà AP Assisted. Vedete [metriche e calcolo](touchless-metrics.md).

Campi mancanti ricorrenti provano un blocco ripetuto, non necessariamente un valore predefinito assente: verificate originale, estrazione, validazione e configurazione.

## Provare l’estrazione iniziale e seguire i blocchi successivi

1. Aprite il documento dalla traccia; verificate ID ed esecuzione. Confrontate numero d’ordine, valuta, quantità, unità, unità di prezzo, prezzi, importi delle righe e totali pertinenti.
2. Distinguete valori attuali e valori prima delle correzioni. Usate una prova storica di quell’esecuzione. Cambiare esecuzione non garantisce di ricostruire ogni vecchia cella.
3. Se manca il valore iniziale, indicate **non valutabile**, non corretto. Definite campi, righe, selezione e dimensione del campione prima di riferire la qualità.
4. Confrontate copia importata, data di importazione e Infor attuale per distinguere fonte errata e copia obsoleta.

Un’esecuzione può attendere l’ordine; dopo l’import una successiva può rivelare un divario di prezzo. La prima non prova che quel controllo fosse stato raggiunto. Il riavvio umano persiste dopo il successo come AP Assisted; un rifiuto ERP finale prevale come eccezione. **Non registrato** significa prova mancante.

Strumenti e classificazione delle azioni umane sono spiegati in [Touchless con MCP](touchless-mcp.md).

## Pagine correlate

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnosi del fornitore e cluster di problemi](touchless-supplier-diagnosis.md)
* [Diagnosi dell'abbinamento ordini](touchless-po-matching-diagnosis.md)

Le schermate di questa pagina mostrano l'interfaccia in italiano.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
