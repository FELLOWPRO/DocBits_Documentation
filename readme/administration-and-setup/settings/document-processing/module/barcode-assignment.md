# Assegnazione tramite codice a barre

### Panoramica

L'impostazione **Assegnazione tramite codice a barre** (Barcode Assignment) aggiunge uno strumento per i codici a barre alla **schermata di validazione dei documenti**. Legge i codici a barre e i codici QR presenti in un documento e ti consente di **assegnare i loro valori ai campi del documento** — ad esempio, compilare un numero di riferimento, d'ordine o di bolla di consegna da un codice a barre invece di digitarlo.

Questa impostazione è **disattivata per impostazione predefinita**.

### Cosa fa?

Quando questa impostazione è attivata, durante la validazione di un documento compare un piccolo **pulsante codice a barre** (un'icona di codice QR) nella barra degli strumenti. Facendo clic su di esso vengono mostrati i codici a barre che DocBits ha trovato nel documento e puoi assegnare ciascuno a un campo. Il campo viene quindi compilato con il valore letto dal codice a barre.

* **Attivata** — Il pulsante codice a barre è mostrato nella schermata di validazione. Puoi leggere i codici a barre del documento e assegnarne i valori ai campi.
* **Disattivata** — Il pulsante è nascosto e i valori dei codici a barre non vengono proposti per l'assegnazione durante la validazione.

{% hint style="info" %}
**Questo serve a leggere un valore di codice a barre/QR e ad assegnarlo a un campo durante la validazione.** L'estrazione automatica di dati strutturati dai codici di pagamento (come Swiss QR Bill o GiroCode) — e la divisione di un file di più pagine in corrispondenza delle pagine separatrici con codice a barre — sono gestite da un'impostazione **diversa**: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Vantaggi

* **Inserimento più rapido e senza errori**: Prendi i valori direttamente da un codice a barre invece di leggerli e digitarli a mano.
* **Meno errori di battitura**: Un valore scansionato è esattamente ciò che è codificato nel codice a barre.
* **Mantieni il controllo**: Decidi tu quale codice a barre va in quale campo durante la validazione.

### Come usarla

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione documenti**.
3. Seleziona **Modulo**.
4. Apri la sezione **Tipo di documento**.
5. Trova **Assegnazione tramite codice a barre** e attiva l'interruttore.
6. In seguito, durante la validazione di un documento, fai clic sul **pulsante codice a barre** nella barra degli strumenti e assegna i valori dei codici a barre rilevati ai campi corrispondenti.

### Quando usare questa funzione

* **Documenti con codici a barre**: Quando i tuoi documenti contengono codici a barre/QR i cui valori appartengono a campi specifici (es. numeri d'ordine o di riferimento).
* **Flussi di validazione manuale**: Quando una persona esamina i documenti e vuole compilare rapidamente i campi dai codici a barre.
* **Lasciala disattivata** se i tuoi documenti non hanno codici a barre utilizzabili, o se ti serve solo l'**estrazione** automatica dei codici a barre/QR — vedi [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
