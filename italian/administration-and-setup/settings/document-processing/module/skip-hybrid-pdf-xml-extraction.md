# Salta l'estrazione XML dai PDF ibridi

### Panoramica

L'impostazione **Salta l'estrazione XML dai PDF ibridi** (Skip Hybrid PDF XML Extraction) controlla come DocBits gestisce i **PDF ibridi** — fatture PDF che contengono una fattura elettronica strutturata incorporata (ZUGFeRD / Factur-X). Determina se l'**XML strutturato all'interno del PDF** è il documento guida per l'elaborazione automatica, oppure se viene elaborato il **PDF stesso** tramite OCR come documento principale.

Questa impostazione è particolarmente rilevante per i **clienti statunitensi**. A differenza dell'UE/Germania, gli Stati Uniti non hanno un obbligo generale di fatturazione elettronica B2B, quindi le organizzazioni statunitensi di solito desiderano che il PDF venga trattato come la fattura principale e leggibile dall'uomo, anche quando una controparte invia un file ZUGFeRD/Factur-X con XML incorporato.

### Cosa fa?

Un file ZUGFeRD/Factur-X è un singolo PDF che contiene anche una fattura XML leggibile dalla macchina. Per impostazione predefinita, DocBits rileva quell'XML incorporato e lo utilizza come fonte guida per l'estrazione (percorso elettronico strutturato).

* **Disattivata (predefinita)** — DocBits rileva l'XML della fattura elettronica incorporato ed elabora il documento sul **percorso elettronico strutturato**. L'XML è la fattura guida. Questo è il comportamento legalmente corretto per UE/Germania, dove la fattura elettronica strutturata è la fattura rilevante e il PDF è solo una visualizzazione / copia di lettura.
* **Attivata** — DocBits **ignora l'XML incorporato** e instrada il documento al **processore PDF (OCR)**. Il PDF diventa il documento di elaborazione principale. Questa è la scelta tipica per le **organizzazioni statunitensi** che desiderano un'elaborazione incentrata sul PDF.

{% hint style="info" %}
Questa impostazione riguarda solo i **PDF ibridi** (ZUGFeRD / Factur-X = un `.pdf` con XML incorporato). Un file XRechnung/EDI puro caricato come `.xml` viene sempre elaborato sul percorso elettronico strutturato — non esiste un PDF che possa diventare il documento principale.
{% endhint %}

### Audit e conformità — l'originale viene sempre conservato

Attivare questa impostazione **non scarta** la fattura elettronica. L'artefatto originale viene sempre conservato:

* Il **PDF** ZUGFeRD/Factur-X originale — **incluso il suo XML incorporato — rimane archiviato** e scaricabile. Nulla viene eliminato dalla copia archiviata del documento.
* L'elaborazione modifica solo **quale contenuto guida l'estrazione** (PDF/OCR rispetto all'XML incorporato), non ciò che viene archiviato.

In questo modo un'organizzazione statunitense può elaborare il PDF come principale mentre la fattura elettronica strutturata rimane disponibile per l'audit.

{% hint style="warning" %}
Per le organizzazioni UE/Germania, lasciare questa impostazione **disattivata**. In base alle regole di fatturazione elettronica del 2025, una fattura elettronica strutturata (ZUGFeRD/Factur-X, XRechnung) è la fattura legalmente rilevante; un semplice PDF è solo una copia di lettura. Elaborare il PDF come principale anziché i dati strutturati non è appropriato quando è presente una fattura elettronica valida.
{% endhint %}

### Come usarla

1. **Aprire l'impostazione**:
   * Vai su **Impostazioni**.
   * Seleziona **Elaborazione documenti**.
   * Seleziona **Modulo**.
   * Apri la sezione **Tipo di documento**.
   * Trova **Salta l'estrazione XML dai PDF ibridi** e attiva l'interruttore.
2. **Scegliere la modalità**:
   * **Organizzazioni statunitensi / incentrate sul PDF** → attiva l'interruttore affinché i PDF ZUGFeRD/Factur-X vengano elaborati tramite OCR come documento principale.
   * **Organizzazioni UE/Germania** → lascia l'interruttore disattivato affinché la fattura elettronica strutturata rimanga il documento guida.
3. **Verificare**:
   * Carica un PDF ZUGFeRD/Factur-X e controlla il risultato dell'elaborazione — con l'interruttore attivo viene trattato come un normale PDF (OCR); con esso disattivato vengono estratti i dati della fattura elettronica incorporata.

### Quando usare questa funzione

* **Clienti statunitensi / senza obbligo di fattura elettronica**: attivala affinché il consueto PDF sia il documento di elaborazione principale mentre la fattura elettronica incorporata rimane archiviata.
* **Flussi misti/incentrati sul PDF**: attivala quando i processi a valle, la validazione o la revisione si basano sul layout del PDF anziché sull'XML.
* **Conformità UE/Germania**: lasciala disattivata affinché i dati strutturati della fattura elettronica guidino l'elaborazione, come richiesto.
