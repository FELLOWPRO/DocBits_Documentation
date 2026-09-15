---
description: Come importare un Receive Delivery BOD in DocBits manualmente tramite API
---

# Importare Entrate Merci (Receive Delivery BOD)

Le entrate merci arrivano normalmente in DocBits in automatico attraverso il flusso di dati ION. Questa pagina descrive come inviare un **Receive Delivery BOD** manualmente — utile quando si vuole reimportare un'entrata, caricare un lotto che non è mai arrivato o testare una mappatura dei campi prima di attivare il flusso automatico.

## Due modi per inviare lo stesso BOD

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-endpoints.png)

| Endpoint | Quando usarlo |
| --- | --- |
| `/import/receive_delivery_bod` | Si ha il BOD come **file XML** e lo si vuole caricare. |
| `/import/receive_delivery_bod_xml` | Si vuole inviare il **contenuto XML** nella richiesta invece di un file. Il BOD va incapsulato in JSON, quindi è adatto a XML brevi o a un altro sistema che chiama l'API — per un BOD completo a mano, caricare il file. |

Entrambi sono descritti di seguito. I passaggi 1 e 2 sono identici in entrambi i casi.

## Prima di iniziare

Serviranno:

* **Una API key.** Vedere [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) se non se ne ha ancora una.
* **Il BOD** — un file XML `SyncReceiveDelivery`, oppure il suo contenuto.
* **Il proprio Org ID**, da **Settings → Integration & SSO**, nella sezione **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** mostra la sotto-organizzazione selezionata nell'intestazione. Con **CROSS** selezionato — la vista su tutte le sotto-organizzazioni — mostra lo stesso valore di **Org ID**. Passare prima a una sotto-organizzazione specifica se ne serve l'ID.

Se non si sta importando in una sotto-organizzazione specifica, lasciare vuoto il campo `sub_org_id`.
{% endhint %}

## Istruzioni passo per passo

### 1. Aprire il link dell'API

Aprire l'interfaccia di test dell'API per l'ambiente e la regione con cui si sta lavorando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Sandbox API (Stati Uniti)](https://us.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Stati Uniti)](https://us.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)

Espandere l'endpoint desiderato facendoci clic sopra.

{% hint style="info" %}
Usare la regione in cui è ospitata la propria organizzazione — la stessa regione con cui si accede a DocBits. Gli ambienti europeo e americano sono separati, quindi un'importazione inviata alla regione sbagliata non comparirà nella propria organizzazione.

Gli indirizzi senza prefisso di regione — `api.docbits.com` e `sandbox.api.docbits.com` — puntano all'Europa. Li si incontra nella documentazione più vecchia e nelle configurazioni esistenti; sono lo stesso ambiente degli indirizzi `eu.` qui sopra.
{% endhint %}

### 2. Autorizzarsi

Tutto ciò che sta sotto **import** è bloccato finché non ci si autorizza. Ci sono due cose da inserire: la propria organizzazione e la propria API key.

* Fare clic sull'**icona del lucchetto** a destra dell'endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-lock.png)

* Si apre la finestra **Available authorizations** con due voci.
* Incollare il proprio **Org ID** in **X-ORG-ID** e fare clic su **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Scorrere fino a **X-API-KEY**, incollare la propria API key e fare clic su **Authorize**. In DocBits la si trova in **Settings → Integration & SSO**, nella sezione **API Key**, oppure si può [creare una nuova chiave](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#creare-una-chiave-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Fare clic su **Close**.

{% hint style="info" %}
Incollare la chiave da sola — non scrivere `Bearer` davanti. Entrambe le autorizzazioni restano impostate finché non si ricarica la pagina o si fa clic su **Logout**.
{% endhint %}

### 3. Compilare i campi

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-rd.png)

Fare clic su **Try it out**, poi compilare il modulo dell'endpoint scelto.

#### Caricare un file — `/import/receive_delivery_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-form.png)

| Campo | |
| --- | --- |
| **file** | Obbligatorio. Fare clic su **Choose file** e selezionare il proprio file XML `SyncReceiveDelivery`. |
| **org\_id** | Il proprio Org ID — lo stesso valore inserito in **X-ORG-ID** al passaggio 2. Indicarlo anche qui rende esplicito in quale organizzazione scrive la richiesta. Deve essere un'organizzazione a cui la propria API key ha accesso; qualsiasi altra viene rifiutata. |
| **sub\_org\_id** | Serve solo se si importa in una sotto-organizzazione specifica. |
| **custom\_fields\_mapping** | Facoltativo. Campi di testata aggiuntivi. Vedere [Mappature dei campi personalizzati](#mappature-dei-campi-personalizzati) più sotto. |
| **custom\_line\_fields\_mapping** | Facoltativo. Lo stesso, per campi aggiuntivi sulle righe dell'entrata. |
| **populate\_additional\_info** | Facoltativo, `false` per impostazione predefinita. Impostarlo a `true` perché DocBits recuperi informazioni aggiuntive sull'entrata dall'ERP dopo l'importazione. Lasciarlo a `false` a meno di sapere che serve — rende l'importazione più lenta. |

{% hint style="warning" %}
**`string` è un valore, non un segnaposto.** Swagger riempie i campi facoltativi con la parola `string`, e viene inviata così com'è se la si lascia — un'importazione con `org_id` impostato a `string` fallirà.

Per ogni campo facoltativo che non si vuole usare, svuotare il campo. Svuotarlo abilita la casella **Send empty value** sottostante, che si può quindi spuntare.
{% endhint %}

#### Mappature dei campi personalizzati

Entrambi i campi di mappatura accettano un oggetto JSON. Il **nome a sinistra deve essere uno dei campi personalizzati propri di DocBits** — da `custom_field_1` a `custom_field_10` per le entrate merci, il doppio di quanti ne consentano gli ordini di acquisto. Qualsiasi altro nome viene ignorato senza avvisi, quindi un errore di battitura qui appare esattamente come una mappatura che non ha funzionato.

Il valore a destra è l'XPath da cui leggere. Scriverlo senza prefissi di namespace — DocBits li aggiunge da sé:

```json
{"custom_field_2": "//ReceiveDelivery/ReceiveDeliveryHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Le mappature di riga usano gli stessi nomi `custom_field_1` … `custom_field_10`, ma i loro XPath vengono letti **relativamente a ciascuna riga dell'entrata**, quindi iniziano con `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Incollare l'XML — `/import/receive_delivery_bod_xml`

<!-- SCREENSHOT: the Try it out form of /import/receive_delivery_bod_xml -->

Questo endpoint non accetta il BOD come semplice incollaggio. Il campo **xml** è un oggetto, precompilato con `{"xml": "string"}`. Sostituire `string` con il contenuto del proprio BOD, mantenendo le virgolette e le parentesi graffe circostanti:

```json
{
  "xml": "<SyncReceiveDelivery ...>...</SyncReceiveDelivery>"
}
```

{% hint style="warning" %}
Il BOD sta dentro una stringa JSON, quindi ogni virgoletta doppia dell'XML va sottoposta a escape come `\"` — e un BOD ne è pieno. Se il risultato non è JSON valido, la richiesta fallisce con un **422** e non viene importato nulla.

Per un BOD reale farlo a mano è laborioso, quindi è preferibile **caricare il file**.
{% endhint %}

Questo endpoint accetta `org_id`, `sub_org_id` e `populate_additional_info`, ma **nessuna mappatura di campi** — né di testata né di riga. Se le proprie entrate hanno bisogno di campi personalizzati, caricare il file invece.

{% hint style="warning" %}
Verificare a quale ambiente e a quale organizzazione si punta prima di eseguire. Un'importazione scrive direttamente nei dati master di quell'organizzazione.
{% endhint %}

### 4. Eseguire

Prima di eseguire, controllare il menu a discesa **Servers** in fondo al modulo. Decide a quale ambiente viene effettivamente inviata la richiesta, e può differire dalla pagina che si è aperta.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-execute.png)

Fare clic su **Execute**. Un'importazione riuscita restituisce:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-response.png)

I receive delivery BOD vengono elaborati mentre si attende, quindi quando si vede questo messaggio i dati sono già dentro.

Se qualcosa non andava nella richiesta, si ottiene `"success": false` insieme a un messaggio che descrive il problema.

### 5. Verificare che i dati siano arrivati

* In DocBits, andare in **Settings → Document Processing → Lookup Master Data**.
* Selezionare **BOD Input Data** a sinistra, poi aprire la scheda dei dati importati.
* Cercare l'entrata merci o l'ordine di acquisto a cui appartiene.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the goods receipt data shown -->

{% hint style="info" %}
DocBits decide cosa fare del BOD leggendo il tipo che contiene, non in base all'endpoint di importazione usato. Se si invia qui un BOD diverso per errore, viene importato come quel tipo anziché essere rifiutato — verificare quindi che la scheda in cui si trovano i dati sia quella attesa.
{% endhint %}
