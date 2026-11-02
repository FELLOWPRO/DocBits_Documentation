# Impostazioni OCR

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR e testo elettronico spiegato: impostazioni, qualità ed estrazione dell'intestazione
{% endembed %}

## Panoramica

Nelle impostazioni **OCR (Riconoscimento ottico dei caratteri)**, puoi configurare il modo in cui OCR viene applicato durante l'elaborazione del documento. Ciò include la specifica della qualità minima richiesta, la scelta se utilizzare il testo incorporato (e-text), la selezione della versione OCR e altro ancora. Questa pagina fornisce una spiegazione dettagliata di tutte le impostazioni disponibili.

## Come accedere alle impostazioni OCR

Per accedere alle impostazioni OCR:

*   Passare a: **Impostazioni** → **Elaborazione documenti** → **Impostazioni OCR**

## Qualità OCR

In questa sezione è possibile impostare la qualità minima del documento richiesta per l'elaborazione OCR regolando il cursore della qualità. Spostare il dispositivo di scorrimento a sinistra o a destra per diminuire o aumentare rispettivamente la soglia di qualità.

Se un documento non soddisfa il livello di qualità definito, DocBits consente tre modalità di gestione:

* **Elaborazione anche sotto soglia**\
  Il documento verrà elaborato indipendentemente dalla sua qualità.
* **Eseguire nuovamente dopo la conferma**\
  **DocBits** farà una pausa e ti chiederà di confermare se procedere con l'elaborazione.
* **Interruzione con errore**\
  L'elaborazione del documento verrà interrotta completamente e verrà visualizzato un messaggio di errore che indica che il documento non ha raggiunto la soglia di qualità richiesta.

<figure><img src="../../../.gitbook/assets/ocr-quality-current-it.png" alt="Soglia minima di qualità OCR e comportamento per i documenti sotto soglia."><figcaption>Soglia minima di qualità OCR e comportamento per i documenti sotto soglia.</figcaption></figure>

## Impostazioni OCR generali

* **Utilizzare il testo elettronico, se disponibile**\
  Se abilitato, **DocBits** utilizzerà il testo elettronico incorporato (ad esempio, da PDF) invece di eseguire OCR. Ciò migliora sia la velocità che la precisione, poiché il testo viene estratto direttamente senza richiedere l'elaborazione OCR.
* **Utilizzare DESKEW se disponibile**\
  Questa opzione corregge automaticamente l'allineamento dei documenti scansionati. Il raddrizzamento delle immagini inclinate aiuta a migliorare la precisione OCR.
*   **Versione AI OCR**\
    Consente di selezionare una versione specifica del motore OCR basato su AI.\
    Questo può essere utile se:

    * Non stai ottenendo i risultati desiderati con la versione attualmente selezionata.
    * Stai risolvendo problemi relativi alle prestazioni o alla precisione di OCR.

<figure><img src="../../../.gitbook/assets/ocr-general-current-it.png" alt="Opzioni generali OCR: testo elettronico, raddrizzamento e versione del motore."><figcaption>Opzioni generali OCR: testo elettronico, raddrizzamento e versione del motore.</figcaption></figure>

## Impostazioni OCR per le tabelle

* **Utilizzare i dati AI per le tabelle, se disponibili**\
  Quando abilitato, DocBits utilizzerà i dati OCR per le tabelle invece del testo elettronico incorporato (E-Text) — anche se l'impostazione **Utilizzare il testo elettronico, se disponibile** è attivata.

<figure><img src="../../../.gitbook/assets/ocr-tables-current-it.png" alt="Opzione OCR per utilizzare i dati AI nelle tabelle, se disponibili."><figcaption>Opzione OCR per utilizzare i dati AI nelle tabelle, se disponibili.</figcaption></figure>

## Impostazioni OCR per i campi di intestazione

* **Estrazione basata su regole**\
  DocBits applicherà le regole di estrazione predefinite per identificare i campi di intestazione.
* **Utilizzare l’estrazione AI**\
  DocBits utilizzerà AI per rilevare ed estrarre automaticamente i campi di intestazione.

**Ordine di esecuzione:**\
Se entrambe le opzioni sono abilitate, **DocBits** eseguirà l'estrazione nel seguente ordine:\
**Estrazione basata su regole → Estrazione AI**\
\
<mark style="color:red;">**Nota**</mark>: per ottenere risultati ottimali e un comportamento coerente, abilitare entrambe le opzioni. Ciò consente a **DocBits** di utilizzare metodi basati su regole e AI in combinazione durante l'estrazione dell'intestazione.

<figure><img src="../../../.gitbook/assets/ocr-header-current-it.png" alt="Opzioni di estrazione dei campi di intestazione mediante regole e AI."><figcaption>Opzioni di estrazione dei campi di intestazione mediante regole e AI.</figcaption></figure>
