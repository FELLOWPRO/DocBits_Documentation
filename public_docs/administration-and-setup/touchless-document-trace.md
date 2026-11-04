# Touchless Intelligence: Tracciamento del documento

Inserite un ID documento in **Document ID**, oppure aprite un documento di esempio da un cluster, per vedere **che cosa è successo a questo documento**.

L'intestazione mostra il file, il suo stato (ad esempio **In corso**), l'esecuzione che state consultando e il suo primo bloccante, oltre a un pulsante **Documento** con l'ID del documento.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-it.png" alt="Dev NOVA: percorso e valori registrati nella prima esecuzione di prova"><figcaption><p>Nuova acquisizione da Dev NOVA 11.0.3 del 4 novembre 2026. La fattura fittizia si arresta alla convalida dei campi. Classificazione, ricerca del fornitore ed estrazione di intestazione e tabella contengono valori realmente registrati. Le schede mostrano documento e cronologia. È l’interfaccia del prodotto in funzione. In questa versione i nomi dei passaggi nel percorso restano in inglese. Nel confronto, Palcoscenico indica una fase del processo: è un errore di traduzione dell’interfaccia.</p></figcaption></figure>

Il **Percorso della condotta** mostra 14 passaggi: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Ogni passaggio porta un solo stato:

| Stato | Significato |
| --- | --- |
| **Superato** (verde) | Il passaggio è andato a buon fine |
| **Mi sono fermato qui** (arancione) | Il passaggio ha bloccato il documento |
| **Non raggiungibile** | Passaggio successivo al primo blocco nel percorso; controllare nel registro eventuali esecuzioni aggiuntive registrate |
| **Niente di registrato** (tratteggiato) | Per questo passaggio non è stato registrato alcun dato |
| **Non applicabile** | Il passaggio non si applica a questo documento |

### Registro dei passaggi

Il **registro dei passaggi** sotto il percorso elenca gli stessi passaggi con ciò che ciascuno ha registrato. Un punto di stato e la parola di stato si trovano a sinistra e a destra di ogni riga.

* Ogni valore è un **chip di valore**: un numero con la sua unità, ad esempio **Affidabilità 100 %**, **Soglia 60 %**, **Regole fallite 0**, **8 campi mancanti** o **0 lacune di abbinamento**. Le percentuali sono mostrate come `97 %`, mai come `0.97`.
* **Dettagli** apre l'elenco completo dei valori registrati da un passaggio, comprese le alternative che ha considerato.
* Il passaggio che ha bloccato il documento ne indica il motivo, ad esempio **Convalida del campo non riuscita**.
* Un valore che nessun passaggio ha registrato compare come **Non registrato**, mai come valore inventato. I valori sono numeri e termini fissi, mai testo del documento.
* **Mostra diagnostica grezza** attiva i dati grezzi quando l'assistenza li richiede.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-it.png" alt="Dev NOVA: registro con affidabilità, valori estratti e convalida bloccata"><figcaption><p>Prima esecuzione reale: affidabilità della classificazione del 100 %, 0 fornitori candidati, 1 riga e 7 lacune di abbinamento. Un passaggio superato conferma l’esecuzione, non l’identificazione del fornitore o la correttezza di tutti i valori. La convalida segnala un campo obbligatorio mancante.</p></figcaption></figure>

### Esecuzioni e modifiche

Il selettore permette di scegliere un tentativo; la cronologia ne mostra l’esito e il primo blocco. Le differenze registrate confrontano l’esecuzione selezionata con la precedente, non automaticamente con quella attuale. Ogni differenza comprende l’unità; i valori identici rimangono invariati.

La scheda Documento mostra tipo, fornitore, numero fattura, ordine, pagine e metodo di analisi registrato. Qui Manuale corrisponde al tipo indicato durante l’importazione di prova. Il 100 % non dimostra quindi in modo indipendente la precisione di una classificazione automatica.

### Leggere i dettagli del fornitore e della tabella

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-it.png" alt="Dev NOVA: identificativi rilevati, ricerca nei dati anagrafici e assegnazione del fornitore"><figcaption><p>Il nome è presente nella fattura e viene cercato nei dati anagrafici, ma non viene assegnato alcun fornitore. La fattura di prova non contiene partita IVA, IBAN, e-mail o GLN. Una corrispondenza anagrafica assente è diversa da un valore non trovato nella fattura.</p></figcaption></figure>

Controllate separatamente se l’identificativo era presente nel documento, se è stato cercato e se è stato assegnato un fornitore. Un passaggio verde non risponde da solo a queste tre domande.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-it.png" alt="Dev NOVA: dettagli della prima esecuzione con sette lacune di abbinamento"><figcaption><p>I dettagli indicano 7 lacune di abbinamento per 1 tabella e 1 riga. Verificate la mappatura delle colonne prima di concludere che l’estrazione sia errata. Il riepilogo del confronto in fondo non è una base valida per la prima esecuzione selezionata, che non ha una precedente.</p></figcaption></figure>

### Riconoscere un vero riavvio

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-it.png" alt="Dev NOVA: confronto di due esecuzioni reali con valori registrati invariati"><figcaption><p>La stessa fattura dopo un vero riavvio manuale, senza correzioni dei campi. Una nuova esecuzione prova un altro tentativo, non un miglioramento. I valori identici rimangono invariati; non sono state inventate differenze.</p></figcaption></figure>

Un riavvio manuale è un intervento umano. Il caso sarà AP Assisted solo dopo un eventuale completamento riuscito. Finché rimane in corso, è escluso dal denominatore dei documenti conclusi.

Limiti delle prove. Il caso non dimostra approvazione aziendale, esportazione riuscita o conferma ERP. Il motore di abbinamento precedente non fornisce qui un percorso decisionale registrato; non è una prova di confronto con Infor. In NOVA 11.0.3, il registro può mostrare una ricerca ordine superata dopo la convalida bloccata, mentre il percorso la presenta come passaggio successivo. Controllate entrambe le viste. Il riepilogo indica inoltre che il numero fattura non è registrato, benché sia presente nell’estrazione; confrontate originale e campi estratti.

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

Le cinque nuove immagini mostrano l’interfaccia localizzata di Dev NOVA 11.0.3 e la stessa fattura creata per la documentazione. Ogni immagine separata di originale e campi illustra solo tale confronto.
