---
description: Come importare un Purchase Order BOD in DocBits manualmente tramite API
---

# Importare Ordini di Acquisto (Purchase Order BOD)

Gli ordini di acquisto arrivano normalmente in DocBits in automatico attraverso il flusso di dati ION. Questa pagina descrive come inviare un **Purchase Order BOD** manualmente — utile quando si vuole reimportare un ordine, caricare un lotto che non è mai arrivato o testare una nuova mappatura prima di attivare il flusso automatico.

## Due modi per inviare lo stesso BOD

Ci sono due endpoint e fanno la stessa cosa. L'unica differenza sta nel modo in cui si consegna il BOD:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-endpoints.png)

| Endpoint | Quando usarlo |
| --- | --- |
| `/import/purchase_order_bod` | Si ha il BOD come **file XML** e lo si vuole caricare. |
| `/import/purchase_order_bod_xml` | Si vuole inviare il **contenuto XML** nella richiesta invece di un file. Il BOD va incapsulato in JSON, quindi è adatto a XML brevi o a un altro sistema che chiama l'API — per un BOD completo a mano, caricare il file. |

Entrambi sono descritti di seguito. I passaggi 1 e 2 sono identici in entrambi i casi.

## Prima di iniziare

Serviranno:

* **Una API key.** Vedere [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) se non se ne ha ancora una.
* **Il BOD** — un file XML `SyncPurchaseOrder`, oppure il suo contenuto.
* **Il proprio Org ID**, se si importa in un'organizzazione diversa da quella a cui appartiene la propria chiave.

Per trovare l'Org ID, andare in **Settings → Integration & SSO** e aprire la sezione **ID**. Fare clic sull'icona di copia accanto al campo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** mostra la sotto-organizzazione selezionata nell'intestazione. Con **CROSS** selezionato — la vista su tutte le sotto-organizzazioni — mostra lo stesso valore di **Org ID**, ed è per questo che i due campi coincidono nella schermata qui sopra. Passare prima a una sotto-organizzazione specifica se ne serve l'ID.

Se non si sta importando in una sotto-organizzazione specifica, lasciare vuoto il campo `sub_org_id`.
{% endhint %}

## Istruzioni passo per passo

### 1. Aprire il link dell'API

Aprire l'interfaccia di test dell'API per l'ambiente e la regione con cui si sta lavorando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Sandbox API (Stati Uniti)](https://us.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Stati Uniti)](https://us.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)

Espandere l'endpoint desiderato facendoci clic sopra.

{% hint style="info" %}
Usare la regione in cui è ospitata la propria organizzazione — la stessa regione con cui si accede a DocBits. Gli ambienti europeo e americano sono separati, quindi un'importazione inviata alla regione sbagliata non comparirà nella propria organizzazione.

Gli indirizzi senza prefisso di regione — `api.docbits.com` e `sandbox.api.docbits.com` — puntano all'Europa. Li si incontra nella documentazione più vecchia e nelle configurazioni esistenti; sono lo stesso ambiente degli indirizzi `eu.` qui sopra.
{% endhint %}

### 2. Autorizzarsi

Tutto ciò che sta sotto **import** è bloccato finché non ci si autorizza. Ci sono due cose da inserire: la propria organizzazione e la propria API key.

* Fare clic sull'**icona del lucchetto** a destra dell'endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-swagger-lock.png)

* Si apre la finestra **Available authorizations** con due voci.
* Incollare il proprio **Org ID** in **X-ORG-ID** e fare clic su **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

* La voce mostra ora **Authorized** e nasconde il valore.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Scorrere fino a **X-API-KEY**, incollare la propria API key e fare clic su **Authorize**. In DocBits la si trova in **Settings → Integration & SSO**, nella sezione **API Key**, oppure si può [creare una nuova chiave](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#creare-una-chiave-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Fare clic su **Close**.

{% hint style="info" %}
Incollare la chiave da sola — non scrivere `Bearer` davanti. Entrambe le autorizzazioni restano impostate finché non si ricarica la pagina o si fa clic su **Logout**.
{% endhint %}

### 3. Compilare i campi

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-po.png)

Fare clic su **Try it out**, poi compilare il modulo dell'endpoint scelto.

#### Caricare un file — `/import/purchase_order_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-form.png)

| Campo | |
| --- | --- |
| **file** | Obbligatorio. Fare clic su **Choose file** e selezionare il proprio file XML `SyncPurchaseOrder`. |
| **org\_id** | Il proprio Org ID — lo stesso valore inserito in **X-ORG-ID** al passaggio 2. Indicarlo anche qui rende esplicito in quale organizzazione scrive la richiesta. Deve essere un'organizzazione a cui la propria API key ha accesso; qualsiasi altra viene rifiutata. |
| **sub\_org\_id** | Serve solo se si lavora con sotto-organizzazioni. Altrimenti lasciare vuoto. |
| **custom\_fields\_mapping** | Facoltativo. Legge campi di testata aggiuntivi dal BOD nei campi personalizzati dell'ordine. Vedere [Mappature dei campi personalizzati](#mappature-dei-campi-personalizzati) più sotto. |
| **custom\_line\_fields\_mapping** | Facoltativo. Lo stesso, per campi aggiuntivi sulle righe dell'ordine. |

{% hint style="warning" %}
**`string` è un valore, non un segnaposto.** Swagger riempie i campi facoltativi con la parola `string`, e viene inviata così com'è se la si lascia — un'importazione con `org_id` impostato a `string` fallirà.

Per ogni campo facoltativo che non si vuole usare, svuotare il campo. Svuotarlo abilita la casella **Send empty value** sottostante, che si può quindi spuntare. Nella schermata qui sopra è stato fatto per `sub_org_id`.
{% endhint %}

#### Mappature dei campi personalizzati

Entrambi i campi di mappatura accettano un oggetto JSON. Il **nome a sinistra deve essere uno dei campi personalizzati propri di DocBits** — da `custom_field_1` a `custom_field_5` per gli ordini di acquisto. Qualsiasi altro nome viene ignorato senza avvisi, quindi un errore di battitura qui appare esattamente come una mappatura che non ha funzionato.

Il valore a destra è l'XPath da cui leggere. Scriverlo senza prefissi di namespace — DocBits li aggiunge da sé:

```json
{"custom_field_2": "//PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Le mappature di riga usano gli stessi nomi `custom_field_1` … `custom_field_5`, ma i loro XPath vengono letti **relativamente a ciascuna riga dell'ordine**, quindi iniziano con `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Incollare l'XML — `/import/purchase_order_bod_xml`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-xml-form.png)

Questo endpoint non accetta il BOD come semplice incollaggio. Il campo **xml** è un oggetto, precompilato con:

```json
{
  "xml": "string"
}
```

Sostituire `string` con il contenuto del proprio BOD, mantenendo le virgolette e le parentesi graffe circostanti:

```json
{
  "xml": "<SyncPurchaseOrder ...>...</SyncPurchaseOrder>"
}
```

{% hint style="warning" %}
Il BOD sta dentro una stringa JSON, quindi ogni virgoletta doppia dell'XML va sottoposta a escape come `\"` — e un BOD ne è pieno (`releaseID="9.2"`, `xmlns="..."`). Se il risultato non è JSON valido, la richiesta fallisce con un **422** e non viene importato nulla.

Per un BOD reale farlo a mano è laborioso, quindi è preferibile **caricare il file**. Questo endpoint è la scelta migliore quando l'XML è breve, o quando un altro sistema costruisce la richiesta e sa codificare il JSON da sé.
{% endhint %}

I campi `org_id`, `sub_org_id` e `custom_fields_mapping` funzionano esattamente come sopra. Questo endpoint non ha un campo per le mappature di riga.

{% hint style="warning" %}
Verificare a quale ambiente e a quale organizzazione si punta prima di eseguire. Un'importazione scrive direttamente nei dati master di quell'organizzazione.
{% endhint %}

### 4. Eseguire

Prima di eseguire, controllare il menu a discesa **Servers** in fondo al modulo. Decide a quale ambiente viene effettivamente inviata la richiesta, e può differire dalla pagina che si è aperta.

Fare clic su **Execute**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

**Se si è caricato un file**, la risposta è:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-response.png)

```json
{
  "success": true,
  "message": "BOD processing started in the background."
}
```

{% hint style="info" %}
**Significa che il file è stato accettato, non che l'importazione sia terminata.** I file degli ordini di acquisto caricati vengono elaborati in background, così gli ordini di grandi dimensioni non bloccano il resto del sistema. Attendere un momento, poi verificare il risultato come descritto sotto.
{% endhint %}

**Se si è incollato l'XML**, l'importazione viene eseguita subito e la risposta è `"BOD processed successfully."` — quando la si vede, i dati sono già dentro.

Se qualcosa non andava nella richiesta, si ottiene `"success": false` insieme a un messaggio che descrive il problema. Le cause più comuni sono un contenuto che non è un BOD `SyncPurchaseOrder` e un Org ID a cui la propria API key non ha accesso.

### 5. Verificare che i dati siano arrivati

* In DocBits, andare in **Settings → Document Processing → Lookup Master Data**.
* Selezionare **BOD Input Data** a sinistra, poi aprire la scheda **Purchase Order**.
* Cercare il numero d'ordine del proprio BOD.

<!-- SCREENSHOT F: Lookup Master Data with BOD Input Data selected and the Purchase Order tab open -->

Se l'ordine è elencato, l'importazione ha funzionato e l'ordine di acquisto è disponibile per il PO matching.

{% hint style="info" %}
DocBits decide cosa fare del BOD leggendo il tipo che contiene, non in base all'endpoint di importazione usato. Se si invia qui un supplier BOD per errore, viene importato come dati fornitore anziché essere rifiutato — verificare quindi che la scheda in cui si trovano i dati sia quella attesa.
{% endhint %}
