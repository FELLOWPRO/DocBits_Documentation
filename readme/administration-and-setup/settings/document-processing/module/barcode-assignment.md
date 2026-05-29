# Assegnazione tramite codice a barre

### Panoramica

L'impostazione **Assegnazione tramite codice a barre** (Barcode Assignment) consente a DocBits di utilizzare i **codici a barre all'interno di un file per separarlo in singoli documenti**. È utile quando più documenti vengono scansionati insieme in un unico PDF di grandi dimensioni e un codice a barre indica dove finisce un documento e inizia il successivo.

Questa impostazione è **disattivata per impostazione predefinita**.

### Cosa fa?

Quando questa impostazione è attivata, DocBits cerca i codici a barre in un file in entrata di più pagine e lo divide in documenti separati nelle posizioni contrassegnate. Ogni documento risultante viene poi elaborato singolarmente.

* **Attivata** — DocBits rileva i codici a barre e separa automaticamente un file combinato in singoli documenti in base ad essi.
* **Disattivata** — Il file viene elaborato come un unico documento; i codici a barre non vengono usati per dividerlo.

{% hint style="info" %}
Qui si tratta di **dividere e assegnare** le pagine in base ai codici a barre. La lettura dei dati codificati in un codice a barre (ad esempio per i codici QR di pagamento) è gestita separatamente in **Bar-Code / QR Code Extraction**.
{% endhint %}

### Vantaggi

* **Scansione in batch più rapida**: Scansiona un'intera pila di documenti in un solo passaggio, separati da fogli con codice a barre, invece di scansionare ogni documento singolarmente.
* **Meno smistamento manuale**: DocBits crea i singoli documenti al posto tuo, così nessuno deve dividere il PDF a mano.
* **Meno errori**: I documenti vengono separati esattamente nelle posizioni contrassegnate ogni volta.

### Come usarla

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione documenti**.
3. Seleziona **Modulo**.
4. Apri la sezione **Tipo di documento**.
5. Trova **Assegnazione tramite codice a barre** e attiva l'interruttore.

### Quando usare questa funzione

* **Scansione ad alto volume**: Quando scansioni molti documenti insieme e usi fogli separatori con codice a barre tra di essi.
* **Batch misti**: Quando un singolo file in entrata contiene più documenti diversi che devono essere elaborati separatamente.
* **Lasciala disattivata** se i tuoi documenti arrivano sempre come file separati: in tal caso la divisione non è necessaria.
