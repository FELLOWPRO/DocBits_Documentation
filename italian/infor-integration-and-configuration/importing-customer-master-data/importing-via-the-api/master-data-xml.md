---
description: Come importare dati master in un dataset di lookup da un file XML
---

# Importare Dati Master da XML

Oltre alle importazioni di BOD, DocBits può leggere dati master da **qualsiasi file XML** in un dataset di lookup a scelta. Si indica in quale dataset scrivere e da quale XPath leggere ciascuna colonna, quindi l'XML non deve seguire affatto un formato BOD.

Usarlo per i dati master che non arrivano come BOD — listini prezzi, centri di costo, attributi di articolo, qualunque cosa il proprio ERP sappia esportare in XML.

## Due modi per inviare l'XML

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Quando usarlo |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Si hanno i dati come **file XML** e lo si vuole caricare. |
| `/master_data_lookup/xml/import_xml_data` | Si vuole **incollare l'XML** nella richiesta. A differenza degli endpoint dei BOD, questo accetta l'XML come testo semplice — senza involucro JSON. |

Entrambi sono descritti di seguito. I passaggi 1 e 2 sono identici in entrambi i casi.

## Prima di iniziare

Serviranno:

* **Una API key.** Vedere [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) se non se ne ha ancora una.
* **L'XML** — come file o come contenuto da incollare.
* **Un tipo di dati** — il nome del dataset di lookup in cui scrivere.
* **Le mappature dei campi** — quale XPath riempie quale colonna.
* **Il proprio Org ID**, da **Settings → Integration & SSO**, nella sezione **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Istruzioni passo per passo

### 1. Aprire il link dell'API

Aprire l'interfaccia di test dell'API per l'ambiente e la regione con cui si sta lavorando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Stati Uniti)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Stati Uniti)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Questi endpoint si trovano sotto **master data lookup** anziché sotto **import**, più in basso nella pagina.

{% hint style="info" %}
Usare la regione in cui è ospitata la propria organizzazione — la stessa regione con cui si accede a DocBits. Gli ambienti europeo e americano sono separati, quindi un'importazione inviata alla regione sbagliata non comparirà nella propria organizzazione.
{% endhint %}

### 2. Autorizzarsi

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

L'autorizzazione funziona esattamente come per le importazioni di BOD: fare clic sull'**icona del lucchetto**, incollare il proprio **Org ID** in **X-ORG-ID**, incollare la propria API key in **X-API-KEY** e fare clic su **Authorize** su ciascuna.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Compilare i campi

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Fare clic su **Try it out**, poi compilare il modulo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Campo | |
| --- | --- |
| **data\_type** | Obbligatorio. Il dataset di lookup in cui scrivere. Viene convertito automaticamente in minuscolo, quindi `PriceList` e `pricelist` sono lo stesso dataset. |
| **field\_mappings** | Obbligatorio. Un oggetto JSON che abbina ciascuna colonna all'XPath da cui viene letta. Vedere sotto. |
| **file** | Obbligatorio su `import_xml_file`. Fare clic su **Choose file** e selezionare il proprio XML. |
| **xml** | Obbligatorio su `import_xml_data` al posto del file — incollarvi l'XML come testo semplice. |
| **org\_id** | Il proprio Org ID — lo stesso valore inserito in **X-ORG-ID** al passaggio 2. |
| **sub\_org\_id** | Serve solo se si importa in una sotto-organizzazione specifica. |

#### Mappature dei campi

`field_mappings` è un oggetto JSON con una voce per colonna. A differenza delle importazioni di BOD, dove i nomi sono fissati a `custom_field_1` … `custom_field_5`, qui li si sceglie:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

I nomi a sinistra diventano le colonne del dataset e sono a propria scelta. I valori a destra devono corrispondere alla struttura dell'XML che si sta caricando — nell'esempio qui sopra, `//Item/ID` preleva l'elemento `<ID>` dentro ciascun `<Item>`. I due lati sono indipendenti: la mappatura qui sopra legge `<UnitPrice>` in una colonna chiamata `Price`.

{% hint style="warning" %}
Vengono rifiutati solo gli XPath **malformati**, con un `400` che nomina il campo. Un XPath valido ma che non trova nulla nel proprio XML passa in silenzio e lascia semplicemente vuota quella colonna — un errore di battitura in un percorso sembra quindi un'importazione riuscita che però ha perso una colonna. Se è il percorso `ID` a non trovare nulla, l'importazione fallisce invece, segnalando che manca la colonna `ID` per quel record.
{% endhint %}

{% hint style="warning" %}
**Una delle colonne deve chiamarsi `ID`.** È ciò che identifica un record: reimportare gli stessi dati aggiorna la riga con quell'ID invece di aggiungerne una duplicata. Il nome non distingue maiuscole e minuscole, quindi `ID`, `Id` e `id` funzionano tutti, ma un nome come `ItemID` non vale — la richiesta viene rifiutata con `ID_FIELD_IS_MISSING` e non viene scritto nulla.
{% endhint %}

{% hint style="warning" %}
**Una richiesta importa un record.** Ogni XPath viene letto una volta, quindi se il proprio XML contiene più elementi viene usata solo la prima corrispondenza di ciascuno. Per caricare un elenco, inviare una richiesta per record oppure usare un'importazione CSV.
{% endhint %}

#### Scegliere un tipo di dati

`data_type` è la chiave del dataset in cui si sta scrivendo. Viene convertito in minuscolo e ripulito dagli spazi, quindi `Items` e `items` sono lo stesso dataset. Qualsiasi nome non già occupato crea un dataset proprio — `items_example`, `cost_centres`, `price_list` — e reimportarvi lo aggiorna.

{% hint style="danger" %}
Alcuni nomi non sono liberi: sono le tabelle di dati master proprie di DocBits, e importare in una di esse ci scrive direttamente dentro.

| Nome | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Rifiutati con `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Accettati, e sovrascrivono dati master reali.** Usarli solo se è davvero ciò che si intende fare. |

Per tutto il resto, scegliere un nome proprio.
{% endhint %}

{% hint style="warning" %}
Verificare a quale ambiente e a quale organizzazione si punta prima di eseguire. Un'importazione scrive direttamente nei dati master di quell'organizzazione.
{% endhint %}

### 4. Eseguire

Prima di eseguire, controllare il menu a discesa **Servers** in fondo al modulo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Fare clic su **Execute**. Un'importazione riuscita restituisce:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

A differenza delle importazioni di BOD, questi endpoint segnalano i problemi con un vero stato di errore anziché con un `200` che porta `"success": false` — un **400** significa che la richiesta è stata rifiutata e non è stato scritto nulla.

### 5. Verificare che i dati siano arrivati

* In DocBits, andare in **Settings → Document Processing → Lookup Master Data**.
* Selezionare **Imported** a sinistra, poi aprire la scheda del proprio tipo di dati.
* Le colonne sono i nomi usati sul lato sinistro di `field_mappings`.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
