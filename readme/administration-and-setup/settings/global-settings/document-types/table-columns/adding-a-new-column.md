# Aggiungere una nuova colonna

Aggiungi una colonna quando per ogni voce di riga deve essere acquisito un valore che le colonne predefinite non coprono: un centro di costo, un numero di progetto, un codice articolo interno.

## Prima di iniziare

* Decidi a quale **tabella** appartiene la colonna. La maggior parte dei tipi di documento ha una sola tabella (ad esempio `INVOICE_TABLE`). Se l'elenco è vuoto, fai prima clic su **Crea nuova tabella**; la finestra di dialogo chiede solo il nome della tabella.
* Decidi il **tipo**: `AMOUNT` per gli importi, `NUMBER` per le quantità, `DATE`, `BOOLEAN` per sì/no, `CURRENCY` per un codice valuta ISO, `STRING` per tutto il resto. Il tipo non può essere modificato dopo il salvataggio.
* Verifica se esiste già una **colonna predefinita** con lo stesso significato ma nascosta. Le colonne nascoste compaiono nell'elenco con il flag *Nascosta* attivo: rendila di nuovo visibile invece di creare un duplicato.

## Passaggi

1. Apri **Impostazioni → Impostazioni Globali → Tipi di Documento → Colonne della Tabella**.
2. Fai clic su **Aggiungi nuova colonna della tabella**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Finestra di dialogo Aggiungi nuova colonna della tabella con Titolo, La colonna è obbligatoria, Seleziona tipo di colonna e Seleziona tabella"><figcaption><p>Aggiungi nuova colonna della tabella</p></figcaption></figure>

3. Compila la finestra di dialogo:

| Campo | Cosa inserire |
|---|---|
| **Titolo** | L'etichetta che l'utente vede nella schermata di validazione, ad esempio `Cost Centre`. Solo lettere e numeri. DocBits ne ricava il *Nome colonna* tecnico (`COST_CENTRE`). |
| **La colonna è obbligatoria?** | Spunta la casella quando il documento non deve essere approvato finché la colonna è vuota in una qualsiasi riga. |
| **Seleziona tipo di colonna** | Vedi l'elenco dei tipi qui sopra. |
| **Seleziona tabella** | La tabella che riceve la colonna. |

4. Fai clic su **Procedi**. La colonna compare nell'elenco con *Sola lettura*, *Nascosta* e *Usa AI* disattivati. Se necessario, attiva questi flag nell'elenco, vedi [Modifica ed eliminazione delle colonne](editing-and-deleting-columns.md).

## Dopo l'aggiunta

* La colonna è **vuota sui documenti esistenti**. Viene compilata sui documenti caricati o riavviati dopo la modifica.
* Per i fornitori con **regole addestrate**, apri uno dei loro documenti nell'addestramento della tabella e mappa la nuova colonna, altrimenti la colonna resta vuota per quel fornitore. Vedi [Definizione Tabelle e Colonne](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Con l'**estrazione AI della tabella**, l'AI compila la colonna se il valore è riconoscibile sul documento. Contrassegna la colonna come *Usa AI* se il fornitore ha regole addestrate ma questa colonna deve comunque provenire dall'AI.
* Aggiungi la colonna alla **mappatura di esportazione** se l'ERP deve riceverla, vedi [Esportazione](../../../document-processing/export.md).

## Messaggi

| Messaggio | Significato |
|---|---|
| *Column name already exists* | Nella tabella esiste già una colonna con questo nome tecnico. Scegli un titolo diverso. |
| *Column name already exists – Please activate it in Table Column settings* | Una colonna predefinita nascosta ha questo nome. Disattiva il suo flag *Nascosta* invece di crearne una nuova. |
| *No table exists. Please create table before creating columns.* | Il tipo di documento non ha ancora una tabella: fai prima clic su **Crea nuova tabella**. |
