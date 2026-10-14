# Assegnazione tramite codice a barre

### Panoramica

L'impostazione **Assegnazione tramite codice a barre** (Barcode Assignment) aggiunge uno strumento per i codici a barre alla **schermata di validazione dei documenti**. Legge i codici a barre e i codici QR presenti in un documento e ti consente di **assegnare i loro valori ai campi del documento** — ad esempio, compilare un numero d'ordine, di riferimento o di bolla di consegna da un codice a barre invece di digitarlo.

Questa impostazione è **disattivata per impostazione predefinita**.

### Cosa ottieni attivandola

Una volta attivata l'impostazione, un nuovo **pulsante codice a barre** (un'icona di codice QR) compare nella barra degli strumenti sul lato destro della **schermata di validazione** (`/field_validation_v1/…`). Questo pulsante è il punto di accesso all'intera funzione — senza l'impostazione, l'icona resta nascosta.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="L'icona codice a barre (codice QR) nella barra degli strumenti di validazione"><figcaption><p>Con l'impostazione attivata, l'icona codice a barre compare nella barra degli strumenti di validazione.</p></figcaption></figure>

Ecco l'icona nel suo contesto, sulla schermata di validazione, accanto al documento in esame:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Schermata di validazione con l'icona codice a barre disponibile"><figcaption><p>La schermata di validazione — l'icona codice a barre (evidenziata, barra degli strumenti di destra) è mostrata solo quando l'Assegnazione tramite codice a barre è attivata.</p></figcaption></figure>

### Come vengono letti i codici a barre

DocBits rileva i codici a barre durante l'elaborazione del documento e offre i loro valori decodificati per l'assegnazione. Uno stesso documento può contenere più tipi di codici a barre — ad esempio un **codice QR**, un **Code 128** e un **EAN-13** — ciascuno dei quali codifica un valore diverso, come un numero d'ordine, un numero di fattura o un GLN del fornitore.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Fattura dimostrativa contenente più tipi di codici a barre"><figcaption><p>Esempio di fattura dimostrativa DocBits contenente tre tipi di codici a barre (codice QR → numero d'ordine, Code 128 → numero di fattura, EAN-13 → GLN del fornitore), ciascuno dei quali codifica un valore assegnabile a un campo.</p></figcaption></figure>

{% hint style="info" %}
Quali tipi di codici a barre vengono rilevati è determinato dall'impostazione **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`). Se la finestra di dialogo mostra *«no barcodes extracted found»*, assicurati che l'estrazione dei codici a barre sia attivata e che i tipi attesi (es. `QRCODE`, `CODE128`, `EAN13`) siano selezionati. Vedi [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Usare la finestra di dialogo di Assegnazione tramite codice a barre

1. Apri un documento nella **schermata di validazione**.
2. Fai clic sull'**icona codice a barre** nella barra degli strumenti di destra.
3. La finestra di dialogo **Assegnazione tramite codice a barre** elenca ogni codice a barre rilevato da DocBits nel documento, mostrato come `Barcode <n> : <valore>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Finestra di dialogo di Assegnazione tramite codice a barre con i codici rilevati"><figcaption><p>La finestra di dialogo di Assegnazione tramite codice a barre elenca ogni codice rilevato con un menu a discesa per scegliere il campo di destinazione.</p></figcaption></figure>

4. Per ogni codice a barre, apri il suo menu a discesa e scegli il campo in cui deve andare il valore.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Scelta del campo di destinazione per un codice a barre"><figcaption><p>Ogni codice a barre può essere assegnato a un qualsiasi campo del documento — es. Numero d'ordine, Numero di fattura, ID fornitore.</p></figcaption></figure>

5. Non appena selezioni un campo, questo viene compilato con il valore del codice a barre.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Codice a barre assegnato al campo Numero d'ordine"><figcaption><p>Dopo aver selezionato un campo (qui Numero d'ordine), il campo viene compilato con il valore del codice a barre.</p></figcaption></figure>

### Come attivarla

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione documenti**.
3. Seleziona **Modulo**.
4. Apri la sezione **Tipo di documento**.
5. Trova **Assegnazione tramite codice a barre** e attiva l'interruttore.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Interruttore Assegnazione tramite codice a barre"><figcaption><p>L'interruttore Assegnazione tramite codice a barre in Impostazioni → Elaborazione documenti → Modulo.</p></figcaption></figure>

### Vantaggi

* **Inserimento più rapido e senza errori**: Prendi i valori direttamente da un codice a barre invece di leggerli e digitarli a mano.
* **Meno errori di battitura**: Un valore scansionato è esattamente ciò che è codificato nel codice a barre.
* **Mantieni il controllo**: Decidi tu quale codice a barre va in quale campo durante la validazione.

### Quando usare questa funzione

* **Documenti con codici a barre**: Quando i tuoi documenti contengono codici a barre/QR i cui valori appartengono a campi specifici (es. numeri d'ordine o di riferimento).
* **Flussi di validazione manuale**: Quando una persona esamina i documenti e vuole compilare rapidamente i campi dai codici a barre.
* **Lasciala disattivata** se i tuoi documenti non hanno codici a barre utilizzabili, o se ti serve solo l'**estrazione** automatica dei codici a barre/QR — vedi [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**Questo serve a leggere un valore di codice a barre/QR e ad assegnarlo a un campo durante la validazione.** L'estrazione automatica di dati strutturati dai codici di pagamento (come Swiss QR Bill o GiroCode) — e la divisione di un file di più pagine in corrispondenza delle pagine separatrici con codice a barre — sono gestite da un'impostazione **diversa**: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
