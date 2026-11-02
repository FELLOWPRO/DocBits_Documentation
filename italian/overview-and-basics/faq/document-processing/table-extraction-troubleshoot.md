# Risoluzione dei Problemi di Estrazione delle Tabelle

## **Passaggio 1: Aprire la Vista OCR per Risultati di Estrazione Scadenti**

Se i risultati dell'addestramento all'estrazione delle tabelle non sono buoni:

1. Aprire la **Vista OCR** facendo clic sull'icona della lente d'ingrandimento con scritto **OCR**.
2. Esaminare i risultati dell'estrazione e verificare se il processo OCR può migliorare la cattura dei dati.
3. Se i risultati sembrano ancora scadenti, provare con un documento diverso per verificare se il problema è specifico del documento.
4. Se il problema è specifico del documento, utilizzare un altro documento per l'estrazione.
   * Se il problema persiste, seguire i passaggi successivi.

## **Passaggio 2: Verificare la Disponibilità dell'E-Text**

1. Verificare se il documento dispone di **e-text** disponibile.
   * È possibile verificare ciò utilizzando uno strumento come **Adobe Acrobat**.
   * Se il documento contiene e-text, seguire il **Passaggio 3**.
   * Se il documento non contiene e-text, seguire il **Passaggio 4**.

## **Passaggio 3: Attivare l'Estrazione dell'E-Text**

Se il documento contiene e-text, si hanno due opzioni:

1. **Attivare l'estrazione dell'e-text solo per questo fornitore**:
   * Tornare alla **Convalida dei Campi dei Documenti**.
   * Fare clic sul quadrato con i tre punti nella barra degli strumenti sul lato sinistro.
   * Qui, attivare l'opzione **Usa E-text se disponibile** per attivarla solo per questo fornitore.
2. **Attivare l'estrazione dell'e-text per tutti i fornitori**:
   * Andare a **Impostazioni** > **Elaborazione dei Documenti** > **Impostazioni OCR**.
   * In questa sezione, troverai l'opzione **Usa E-text se disponibile** e potrai attivarla per tutti i fornitori.
3. Dopo aver attivato l'estrazione dell'e-text, riprovare l'**addestramento all'estrazione delle tabelle**.
   * Se i risultati migliorano, il problema è risolto.
   * Se i risultati non sono ancora buoni, procedere al **Passaggio 4**.

## **Passaggio 4: Nessun E-Text Disponibile - Cambiare la Versione dell'AI OCR**

Se il documento non dispone di e-text disponibile:

1. Andare a **Impostazioni** > **Elaborazione dei Documenti** > **Impostazioni OCR**.
2. Cambiare la **Versione dell'AI OCR** con una versione diversa.
3. Tornare all'**Addestramento all'Estrazione delle Tabelle** e riprovare.
4. Se il risultato è migliore:
   * Verificare altri documenti da fornitori diversi per garantire che i risultati dell'estrazione per quei fornitori non siano influenzati da questo cambiamento.
   * **Fare attenzione, poiché questo cambiamento può influenzare i risultati di estrazione di altri fornitori.**
   * Questo cambiamento può influenzare altri fornitori, quindi assicurarsi di verificare attentamente i risultati per garantire che non influiscano negativamente sulle estrazioni dei documenti di altri fornitori.
5. Se il risultato non è migliorato dopo aver cambiato la versione dell'AI OCR, si prega di **contattarci** per ulteriore assistenza.

## Messaggi sulla tabella

L'estrazione può sembrare corretta e il documento rifiutare comunque l'approvazione. Questi sono i messaggi che DocBits mostra sulla tabella delle voci di riga o sotto di essa, cosa li provoca e come risolverli.

| Messaggio | Causa | Soluzione |
|---|---|---|
| **Colonna obbligatoria vuota** (cella evidenziata in rosso, nome della colonna nel tooltip) | Una colonna contrassegnata *Obbligatoria* nelle impostazioni delle colonne della tabella non ha valore in questa riga. | Compila la cella. Se il valore non esiste mai per questo tipo di documento, un amministratore toglie la spunta a *Obbligatoria* in Impostazioni → Tipi di Documento → Colonne della Tabella e tu riavvii il documento. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits controlla ogni riga: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, meno `DISCOUNT`, oppure × (100 − `DISCOUNT_PERCENT`) / 100, oppure meno `DISCOUNT_PER_UNIT × QUANTITY`, a seconda della colonna di sconto compilata. Una differenza superiore a 0,02 genera il messaggio. Il controllo viene eseguito solo quando quantità, prezzo unitario e totale sono tutti compilati. | Confronta i quattro valori con il documento. Di solito uno di essi è stato letto nella colonna sbagliata: il caso più frequente è un valore di oneri o sconto nella cella sbagliata. Correggi la cella; il messaggio scompare al salvataggio. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Stesso controllo, con la colonna di sconto compilata. | Come sopra; controlla prima la cella dello sconto. |
| **Line items add up to … but the net total is …** (avviso) | La somma di tutte le celle `TOTAL_AMOUNT` differisce dall'importo netto nell'intestazione. | Cerca una riga mancante, una riga duplicata o un importo netto dell'intestazione letto male. Un avviso non blocca l'approvazione. |
| **Total does not add up: expected …, got …** (intestazione) | Netto + imposta (+ spedizione nei layout USA) differisce dal totale dell'intestazione. | Controllo dell'intestazione, non un problema della tabella: correggi gli importi dell'intestazione. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | Il PO matching richiede queste quattro colonne predefinite e una di esse è nascosta o sostituita da una colonna personalizzata. | Amministratore: rendi di nuovo visibile la colonna predefinita in Colonne della Tabella, oppure mappa il valore su di essa nell'addestramento della tabella. |
| **Table is already extracted by AI. Do you want to train manually?** | Hai aperto l'addestramento della tabella per un fornitore la cui tabella proviene dall'AI. | Conferma per addestrare; le regole salvate sostituiscono quindi la tabella AI per questo fornitore. Annulla per mantenere la tabella AI. |
| **AI Table will display here. Enable in …** | L'estrazione AI delle tabelle è disattivata per l'organizzazione. | Amministratore: Impostazioni → Elaborazione del documento → Classificazione ed estrazione → *Estrazione AI delle tabelle*. |
| **No line items yet** | Non è stato estratto nulla: nessuna regola per questo fornitore e l'AI non ha trovato alcuna tabella, oppure il documento non ha testo leggibile. | Segui i Passaggi 1–4 qui sopra (vista OCR, E-Text). Poi addestra la tabella una volta, oppure aggiungi le righe manualmente con *Aggiungi nuova riga della tabella*. |

### L'AI continua a compilare una colonna con il valore sbagliato

Esempio riscontrato nella pratica: l'AI scrive il totale della riga in `CHARGES`. Ogni riga fallisce quindi il controllo del totale riga, perché gli oneri vengono sommati a quantità × prezzo unitario.

1. Se il fornitore ha regole salvate, togli la spunta a *Usa AI* su quella colonna (Impostazioni → Tipi di Documento → Colonne della Tabella) in modo che siano le regole a compilarla.
2. Se il fornitore non ha regole, addestra la tabella una volta in modo che la colonna sia legata alla sua posizione sulla pagina, oppure nascondi la colonna se il fornitore non stampa mai quel valore.
3. Aggiungi un [tag della tabella AI](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) come *"la colonna degli oneri è vuota per questo fornitore"*; i tag vengono salvati per fornitore.

### Disattivare i controlli sulla tabella

Impostazioni → Tipi di Documento → *il tuo tipo* → Altre impostazioni → **Salta la validazione della tabella** contrassegna come valida la tabella di ogni documento di quel tipo: le discrepanze del totale riga e le colonne obbligatorie vuote non vengono più segnalate. I controlli dell'intestazione (totale = netto + imposta) restano attivi. Usala solo per i tipi di documento le cui tabelle sono puramente informative e non vengono esportate nell'ERP.
