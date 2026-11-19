# Impostazioni avanzate

In alcuni documenti le strutture delle tabelle sono complesse: l'intestazione occupa più righe, le informazioni sono raggruppate oppure sono presenti righe extra non necessarie. Le _Impostazioni avanzate_ in modalità di allenamento ti consentono di ottimizzare l'estrazione delle tabelle in questi casi, migliorando precisione e coerenza.

Per aprire queste impostazioni, attiva la **Modalità di allenamento** e clicca sull'icona a ingranaggio **Impostazioni** nella barra delle azioni in alto:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-gear-it-20261112.png" alt="Schermata di estrazione delle tabelle in modalità di allenamento con il puntatore sull'icona a ingranaggio Impostazioni nella barra delle azioni in alto."><figcaption><p>L'icona a ingranaggio nella barra della modalità di allenamento apre le impostazioni avanzate.</p></figcaption></figure>

La finestra **Impostazioni** contiene tutte le opzioni descritte in questa pagina. Espandi la sezione **Impostazioni avanzate** per raggiungere le opzioni di raggruppamento, che restano compresse finché non le apri:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-it-20261112.png" alt="Finestra Impostazioni con Conteggio delle righe dell'intestazione 2 e la sezione Impostazioni avanzate espansa: Righe minime raggruppate 2, Massimo di righe raggruppate 3, Colonne di gruppo distinte, Raggruppamento inverso e Testo diviso."><figcaption><p>La sezione Impostazioni avanzate con tutte le opzioni di raggruppamento.</p></figcaption></figure>

Ogni opzione è descritta nella propria sezione, insieme all'effetto che produce sulla tabella estratta.

## Conteggio delle righe dell'intestazione

**Usa questa impostazione per definire da quante righe è composta l'intestazione della tabella.** Il tooltip dell'opzione chiede: _Di quante righe è composta l'intestazione della tabella?_

Alcune tabelle hanno intestazioni su più righe. Ad esempio, l'intestazione di questa tabella occupa due righe:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-two-lines-it-20261112.png" alt="Tabella di una fattura con l'intestazione su due righe (Preis in EUR e Betrag in EUR)."><figcaption><p>Un'intestazione di tabella che occupa due righe.</p></figcaption></figure>

Imposta il **Conteggio delle righe dell'intestazione** in base al numero di righe dell'intestazione:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-row-count-it-20261112.png" alt="Finestra Impostazioni con Conteggio delle righe dell'intestazione impostato su 2."><figcaption><p>Conteggio delle righe dell'intestazione impostato su 2 nella finestra Impostazioni.</p></figcaption></figure>

### Perché è importante?

Se non imposti questo valore, DocBits può considerare la seconda riga come dati anziché come parte dell'intestazione, causando errori di estrazione:

**Prima:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-before-it-20261112.png" alt="Tabella estratta con Conteggio delle righe dell'intestazione errato: la seconda riga dell'intestazione compare come riga di dati e le colonne non sono mappate."><figcaption><p>Prima: la seconda riga dell'intestazione viene trattata come dati.</p></figcaption></figure>

Dopo:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-after-it-20261112.png" alt="Tabella estratta con Conteggio delle righe dell'intestazione 2: le colonne sono mappate su Posizione, Descrizione, Quantità, Prezzo Unitario e Importo Netto e le righe sono corrette."><figcaption><p>Dopo: intestazione e righe di dati sono separate correttamente.</p></figcaption></figure>

## Spostare le righe extra in

**Usa questa opzione per eliminare le voci su più righe non desiderate, come le descrizioni che occupano più righe.** Il tooltip dell'opzione chiede: _In quale colonna si desidera spostare i dati non raggruppati?_

In questo esempio la descrizione si estende su più righe, ma solo la prima è rilevante:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-overflow-doc-it-20261112.png" alt="Tabella di una fattura in cui la descrizione di ogni articolo continua su righe di testo aggiuntive sotto l'articolo."><figcaption><p>La descrizione si estende su più righe, delle quali solo la prima è rilevante.</p></figcaption></figure>

Imposta **Spostare le righe extra in** su **Rifiuti** per rimuovere il testo in eccesso:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-move-extra-rows-it-20261112.png" alt="Finestra Impostazioni con Spostare le righe extra in impostato su Rifiuti."><figcaption><p>Spostare le righe extra in impostato su Rifiuti.</p></figcaption></figure>

**Risultato dopo la mappatura:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-trash-result-it-20261112.png" alt="Schermata di estrazione delle tabelle: il documento di origine mostra la descrizione di ogni articolo su due righe, mentre la tabella estratta a destra contiene una riga pulita per articolo."><figcaption><p>Risultato dopo la mappatura: le righe in eccesso non ci sono più e restano solo le righe rilevanti.</p></figcaption></figure>

## Righe minime raggruppate

**Usa questa opzione quando le righe devono essere raggruppate sotto una riga principale (ad esempio articoli con più sottorighe).** Il tooltip dell'opzione chiede: _Quante righe ha la colonna minima raggruppata?_

Qui solo tre righe su sei sono rilevanti. Due colonne chiave sono mappate (ad esempio Posizione e Descrizione), mentre le altre sono trattate come campi personalizzati.

Inizia impostando il **Conteggio delle righe dell'intestazione** e le **Righe minime raggruppate**, cioè il numero minimo di righe che devono appartenere a un gruppo prima che DocBits le unisca:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-it-20261112.png" alt="Finestra Impostazioni con Conteggio delle righe dell'intestazione 2 e la sezione Impostazioni avanzate espansa con Righe minime raggruppate impostate su 2."><figcaption><p>Conteggio delle righe dell'intestazione e Righe minime raggruppate impostati nella finestra Impostazioni.</p></figcaption></figure>

Imposta anche **Spostare le righe extra in** su **Rifiuti** per eliminare i dati non rilevanti:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-trash-it-20261112.png" alt="Finestra Impostazioni con Conteggio delle righe dell'intestazione 2, Spostare le righe extra in Rifiuti e Righe minime raggruppate 2."><figcaption><p>In aggiunta, Spostare le righe extra in impostato su Rifiuti.</p></figcaption></figure>

Poi definisci la colonna chiave di raggruppamento, ad esempio _Posizione_, aprendo il menu di quella colonna e scegliendo la voce **File di gruppo** (l'opzione che raggruppa le righe):

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-group-key-it-20261112.png" alt="Tabella estratta con il menu della colonna Posizione aperto: Cancellare la colonna, File di gruppo e Regex."><figcaption><p>Scegli File di gruppo nel menu della colonna chiave di raggruppamento (Posizione).</p></figcaption></figure>

Il raggruppamento stesso e gli altri strumenti delle colonne che funzionano insieme a esso (selezione manuale delle righe, mappatura delle colonne ed espressioni regolari) sono descritti passo dopo passo in [Strutturazione e Miglioramento dell'Estrazione delle Tabelle in DocBits](improving-table-extraction-with-regex.md).

**Risultato:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-grouped-result-it-20261112.png" alt="Schermata di estrazione delle tabelle: il documento di origine contiene sei righe fisiche, due per articolo, e la tabella estratta a destra mostra una riga raggruppata per articolo."><figcaption><p>Risultato: le sei righe fisiche sono raggruppate in tre articoli.</p></figcaption></figure>

### Massimo di righe raggruppate

**Usa questa opzione per limitare quante righe può contenere un gruppo.** Il suo tooltip chiede: _Quante righe ha la colonna massima raggruppata?_ È la controparte di Righe minime raggruppate: un gruppo che richiederebbe più righe di questo numero non viene unito.

Lascia il campo vuoto quando i gruppi possono avere qualsiasi dimensione. Impostalo quando un documento contiene articoli con molte sottorighe e vuoi che DocBits lasci i blocchi insolitamente grandi non raggruppati, così puoi controllarli tu stesso.

Il campo si trova nella stessa area della finestra di Righe minime raggruppate, subito sotto:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-it-20261112.png" alt="Finestra Impostazioni con Righe minime raggruppate 2 e Massimo di righe raggruppate 3; Colonne di gruppo distinte, Raggruppamento inverso e Testo diviso non selezionati."><figcaption><p>Massimo di righe raggruppate (qui 3) si trova subito sotto Righe minime raggruppate.</p></figcaption></figure>

### Colonne di gruppo distinte

**Usa questa opzione per mantenere solo valori unici nella colonna chiave di raggruppamento.** Il tooltip dell'opzione chiede: _Si vogliono solo valori unici per la colonna raggruppata?_

Attivala quando più gruppi porterebbero lo stesso valore nella colonna chiave e vuoi che DocBits mantenga quel valore una sola volta, così i gruppi ripetuti mostrano la chiave vuota invece del valore duplicato.

È una casella di controllo nella stessa sezione di Righe minime raggruppate:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-it-20261112.png" alt="Finestra Impostazioni con la casella Colonne di gruppo distinte selezionata sotto Massimo di righe raggruppate."><figcaption><p>Colonne di gruppo distinte è la casella di controllo sotto Massimo di righe raggruppate.</p></figcaption></figure>

### Raggruppamento inverso

**Usa questa opzione quando la riga di raggruppamento compare** _**dopo**_ **le righe che dovrebbe raggruppare.** Il tooltip dell'opzione chiede: _Si desidera combinare tutte le righe sopra l'attributo raggruppato?_

Attivala quando la riga che contiene la chiave di raggruppamento (ad esempio la posizione o l'importo) sta _sotto_ le sue righe di continuazione: DocBits unisce così al gruppo le righe sopra la chiave, invece di quelle sotto:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-doc-it-20261112.png" alt="Tabella di una fattura in cui la riga della descrizione si trova sopra la riga che contiene posizione, quantità e importi."><figcaption><p>La riga di raggruppamento compare dopo le righe che dovrebbe raggruppare.</p></figcaption></figure>

Attiva **Raggruppamento inverso**, raggruppa per una colonna principale (ad esempio Importo Netto) e imposta **Spostare le righe extra in** su **Rifiuti** se necessario:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-dialog-it-20261112.png" alt="Finestra Impostazioni con Raggruppamento inverso selezionato, Spostare le righe extra in Rifiuti e Conteggio delle righe dell'intestazione 2."><figcaption><p>Raggruppamento inverso attivo insieme a Spostare le righe extra in Rifiuti.</p></figcaption></figure>

**Risultato finale:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-result-it-20261112.png" alt="Tabella estratta con tre righe dopo il raggruppamento inverso per la colonna degli importi."><figcaption><p>Risultato finale con il raggruppamento inverso.</p></figcaption></figure>

### Testo diviso

**Usa questa opzione per dividere il testo di una cella esattamente in corrispondenza del separatore di colonna.** Il tooltip dell'opzione chiede: _Si vuole dividere il testo esattamente in corrispondenza del separatore di colonna?_

Attivala quando una cella estratta contiene il testo di due colonne che il separatore della tabella non ha separato. DocBits estrae di nuovo la tabella e taglia ogni valore nella posizione del separatore che hai definito, invece di memorizzare entrambi i valori in una sola cella.

Poiché la divisione ripete l'estrazione, DocBits ti chiede conferma prima di eseguirla: la richiesta compare appena selezioni la casella di controllo e la divisione viene applicata solo dopo aver cliccato **Procedere**.

La casella è l'ultima opzione della sezione Impostazioni avanzate:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-it-20261112.png" alt="Finestra Impostazioni con la casella Testo diviso selezionata come ultima opzione della sezione Impostazioni avanzate."><figcaption><p>Testo diviso è l'ultima casella di controllo della sezione.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-split-confirm-it-20261112.png" alt="Finestra di conferma con il testo Sei sicuro? La tabella verrà estratta di nuovo e i pulsanti Annulla e Procedere."><figcaption><p>Selezionando Testo diviso compare questa conferma; solo Procedere applica la divisione.</p></figcaption></figure>

## Riepilogo

Usa le _Impostazioni avanzate_ per insegnare a DocBits come gestire con precisione strutture di tabelle più complesse o irregolari. Queste impostazioni migliorano la precisione dell'estrazione tenendo conto di:

* Intestazioni su più righe
* Descrizioni su più righe
* Articoli raggruppati
* Ordine inverso dei dati raggruppati
* Testo da dividere in corrispondenza del separatore di colonna

Attivare queste opzioni durante l'allenamento garantisce che DocBits ricordi il layout corretto per i documenti futuri dello stesso fornitore. Quando l'estrazione è corretta, salva la configurazione con l'azione **Salva le regole**, descritta in [Salvare ed Eliminare Regole](save-and-delete-rules.md).
