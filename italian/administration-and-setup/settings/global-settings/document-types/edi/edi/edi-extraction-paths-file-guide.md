# Guida al File dei Percorsi di Estrazione EDI

## 1. Panoramica

Il **File dei Percorsi di Estrazione** definisce come i dati vengono estratti dal **XML strutturato** nei campi e tabelle specifiche all'interno dell'interfaccia. Mappa gli **ID dei campi** alle **espressioni XPath**, che vengono valutate per estrarre i valori dall'XML nei campi del documento corrispondenti. Questo file svolge un ruolo critico nell'assicurare che i dati estratti appaiano correttamente durante la convalida dei campi e l'elaborazione successiva.

## 2. Scopo e Funzione

* Mappa ogni campo del documento e colonna della tabella in una posizione specifica nell'XML strutturato utilizzando espressioni XPath.
* Assicura che i valori corretti siano popolati nei campi come `order_number`, `supplier_name` e `total_amount`.
* Supporta sia **singoli campi** (tramite un oggetto `fields`) che **tabelle** (tramite un array `tables` con percorsi delle righe e mappature delle colonne).
* Consente un controllo preciso su come i dati vengono recuperati dall'XML, inclusa l'uso di funzioni XPath come `sum()`.

Esempio di mappatura del campo:

Copy

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Accesso e Modifica di Base

#### **Accesso al File:**

1.  Vai su **Impostazioni** → **Tipo di Documento** → _\[Il Tuo Documento (es. Ordine di Acquisto)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sotto la scheda **E-Doc**, seleziona il tuo formato (es. **EDI**).
3.  Clicca su **Percorsi di Estrazione** per visualizzare o modificare il file.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Gestione delle Bozze:**

* **Crea una Bozza:** Clicca sull'icona della ✏️ matita.
* **Elimina le Bozze:** Usa l'icona del 🗑️ cestino per rimuovere le bozze non utilizzate.
* **Attiva le Modifiche:** Clicca sul segno di spunta ✅ per pubblicare una versione.
  * **Nota**: Attivare una nuova versione disattiverà **automaticamente** quella precedente.

## 4. Editor & Sintassi

Il File dei Percorsi di Estrazione è scritto in **JSON** e contiene due componenti principali:

* **fields**: Un dizionario in cui ogni chiave è un ID di campo e ogni valore è un'espressione XPath che definisce come estrarre i dati.
* **tables**: Un elenco di definizioni di tabelle che includono:
  * `name`: L'ID della tabella.
  * `row_path`: Un XPath che identifica ogni riga della tabella.
  * `columns`: Un elenco di mappature delle colonne (`name`, `path`).

Puoi anche utilizzare funzioni XPath (es. `sum()`) ed espressioni per calcolare valori dinamicamente da elementi ripetuti.

Copy

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Funzione Anteprima (Valutazione Estrazione)

La **Funzione Anteprima** ti permette di simulare come si comporteranno i percorsi di estrazione con un documento caricato effettivo.

**Utilizzo:**

* Carica un file EDI tramite il normale processo di caricamento.
* Copia l'**ID del Documento**.
* Vai all'interfaccia dei **Percorsi di Estrazione**.
* Apri la **Funzione Anteprima**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Inserisci l'ID del Documento e clicca su **Test**.
* Il risultato mostrerà come ogni campo e tabella è popolato in base ai percorsi configurati.

Questa funzionalità è essenziale per verificare che le tue espressioni XPath siano correttamente definite e che i valori attesi vengano estratti prima di attivare la bozza.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Video Guida

Una guida video per questo tipo di file è disponibile sulla [pagina dei Video.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Usala per seguire la configurazione, la modifica e l'anteprima.
