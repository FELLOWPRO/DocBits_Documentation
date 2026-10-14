# And: scegliere una scheda di condizione

Usa una scheda **And** per decidere se un workflow deve proseguire dopo il suo trigger **When**. Aggiungi i controlli necessari prima dell'azione **Then**. Ogni scheda mostra dei campi da compilare, come **Operator**, **Field Name** o **Value**; gli screenshot mostrano i template di scheda disponibili, non regole già compilate.

Nel **Workflow Builder**, seleziona **Add Card** sotto **And...**. Scegli una categoria a sinistra oppure digita il nome di una scheda in **Search Card**. Seleziona l'anteprima di una scheda per aggiungerla al workflow. Puoi scorrere l'elenco delle anteprime per vedere altre schede. Usa **×** per chiudere il selettore senza scegliere un'altra scheda. Dopo aver configurato le schede, salva il workflow. Consulta [Workflow](../README.md) per i passaggi **When**, **And** e **Then** che lo circondano.

## Compare with Purchase Order

Usa queste schede per confrontare i dati di un ordine o di una fattura con un ordine d'acquisto, ad esempio prezzo unitario, data di consegna promessa, costi aggiuntivi o quantità. Scegli i campi, l'operatore ed eventuali tolleranze richiesti dalla scheda selezionata. Consulta [Compare with Purchase Order](compare-with-purchase-order/README.md) per le singole schede.

<figure><img src="../../../.gitbook/assets/and-category-po-comparison-en.png" alt="Selettore delle schede And in inglese con Compare with Purchase Order selezionato; le anteprime visibili riguardano il confronto di prezzo unitario, data di consegna, costi aggiuntivi e quantità."><figcaption>Categoria Compare with Purchase Order nella Sandbox in inglese.</figcaption></figure>

## Document Field

Scegli questa categoria per controllare una casella di controllo o lo stato di un campo, confrontare un campo con un valore o confrontare due campi. Compila i segnaposto **Field Name** e **Operator** sulla scheda scelta. Alcuni confronti richiedono anche una tolleranza. Consulta [Document Field](document-field/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-field-en.png" alt="Selettore delle schede And in inglese con Document Field selezionato; le anteprime visibili controllano una casella di controllo, lo stato di un campo, i valori dei campi e confronti tra due campi."><figcaption>I controlli Document Field usano i valori del documento corrente.</figcaption></figure>

## Date & Time

Usa **Date & Time** per confrontare una data o un'ora con un intervallo, oppure per confrontare **Today** con una data scelta. Seleziona l'**Operator** e i valori di data nella scheda. Consulta [Date & Time](date-and-time/README.md).

<figure><img src="../../../.gitbook/assets/and-category-date-time-en.png" alt="Selettore delle schede And in inglese con Date & Time selezionato; due anteprime confrontano una data o un'ora con un intervallo e confrontano Today con una Date."><figcaption>Date & Time offre un controllo su un intervallo e un controllo rispetto a oggi.</figcaption></figure>

## Document

Usa queste schede quando un workflow deve dipendere dal **tipo di documento** o dalla **sotto-organizzazione**. Scegli il tipo o l'organizzazione indicati nella scheda. Consulta [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-en.png" alt="Selettore delle schede And in inglese con Document selezionato; le anteprime controllano il tipo di documento e l'appartenenza a una sotto-organizzazione."><figcaption>Le condizioni Document controllano il tipo o la sotto-organizzazione.</figcaption></figure>

## Logic

Questa categoria comprende controlli che usano una tabella decisionale, una risposta HTTPS, la disponibilità di un modulo, un prezzo di offerta di un articolo, un valore di probabilità o due valori. Apri la scheda specifica e compila i segnaposto indicati; ad esempio, la scheda HTTPS richiede un URL, un metodo e un codice di stato accettato. Consulta [Logic](logic/README.md).

<figure><img src="../../../.gitbook/assets/and-category-logic-en.png" alt="Selettore delle schede And in inglese con Logic selezionato; le anteprime comprendono tabella decisionale, richiesta HTTPS, modulo attivo, prezzo di offerta, probabilità e confronto tra valori."><figcaption>Logic offre diversi tipi di condizione; scegli quello che corrisponde alla tua regola.</figcaption></figure>

## Status

Usa **Status** per controllare se un documento ha uno stato scelto o se il suo stato rientra in un insieme selezionato. Scegli l'**Operator** e lo **Status** nella scheda. Consulta [Status](status/README.md).

<figure><img src="../../../.gitbook/assets/and-category-status-en.png" alt="Selettore delle schede And in inglese con Status selezionato; due anteprime confrontano lo stato del documento con uno Status o con un insieme di stati."><figcaption>Le condizioni Status controllano lo stato attuale del documento.</figcaption></figure>

## Table

Queste schede esaminano le righe delle tabelle del documento. Le opzioni visibili comprendono controlli sulle date, pattern di testo, durata di conservazione e confronti tra colonne. Seleziona il **Table name** e il **Column Name** prima di scegliere un operatore o un pattern. Consulta [Table](table/README.md).

<figure><img src="../../../.gitbook/assets/and-category-table-en.png" alt="Selettore delle schede And in inglese con Table selezionato; le anteprime visibili comprendono data, pattern regex, durata di conservazione e confronti tra colonne della tabella."><figcaption>Le condizioni Table usano righe e colonne di una tabella del documento.</figcaption></figure>

## Compare with Quote Price

Usa queste schede per confrontare un articolo con i dati del prezzo di offerta. Le scelte visibili riguardano ID articolo, tipo di fornitore, ID articolo del fornitore, prezzo unitario e unità di misura. L'**Operator** e i segnaposto dei dati dipendono dalla scheda selezionata.

<figure><img src="../../../.gitbook/assets/and-category-quote-price-en.png" alt="Selettore delle schede And in inglese con Compare with Quote Price selezionato; cinque anteprime riguardano ID articolo, tipo di fornitore, ID articolo del fornitore, prezzo unitario e unità di misura."><figcaption>Compare with Quote Price è una categoria separata nell'attuale selettore delle schede.</figcaption></figure>

## Assignee

Usa **Assignee** quando la condizione dipende dall'utente o dal gruppo assegnato. Scegli se confrontare con un singolo utente o gruppo oppure con un insieme selezionato. Consulta [Assignee](assignee/README.md).

<figure><img src="../../../.gitbook/assets/and-category-assignee-en.png" alt="Selettore delle schede And in inglese con Assignee selezionato; le anteprime confrontano l'utente o il gruppo assegnato con una o più scelte."><figcaption>Le condizioni Assignee controllano l'utente o il gruppo assegnato al documento.</figcaption></figure>
