# Guida al File Anteprima EDI

## 1. Panoramica

Il **File Anteprima** definisce come i dati XML strutturati vengono resi in un formato leggibile dall'utente, simile a un PDF. Combina **HTML e CSS** per la presentazione visiva e utilizza le dichiarazioni **XSLT** `**select**` per inserire dinamicamente i dati dal XML personalizzato. Questa anteprima viene visualizzata durante la **validazione del campo** ed è inclusa anche quando i documenti vengono esportati in **IDM**.

## 2. Scopo e Funzione

* Converte il XML personalizzato leggibile dalla macchina in un'anteprima formattata visualmente (PDF).
* Consente una revisione e una convalida amichevoli per l'utente dei dati estratti.
* Garantisce il rendering coerente dei campi chiave del documento come intestazioni, tabelle, totali, ecc.
* Realizzato utilizzando **HTML + CSS** per il layout e il design, e **XSLT** per collegare i dati al layout.

## 3. Accesso e Modifica di Base

#### **Accesso al File:**

1.  Vai su **Impostazioni** → **Tipo di Documento** → _\[Il tuo Documento (es. Ordine di Acquisto)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sotto la scheda **E-Doc**, seleziona il tuo formato (es. **EDI**).
3.  Clicca su **Anteprima** per visualizzare o modificare il file.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Gestione delle Bozze:**

* **Crea una Bozza:** Clicca sull'icona della ✏️ matita.
* **Elimina le Bozze:** Usa l'icona del 🗑️ cestino per rimuovere le bozze non utilizzate.
* **Attiva le Modifiche:** Clicca sul segno di spunta ✅ per pubblicare una versione.
  * **Nota**: Attivando una nuova versione si **disattiverà automaticamente** la precedente.

## 4. Editor HTML/XSLT/CSS

Il **File Anteprima** viene modificato in un editor dedicato che supporta HTML, XSLT e CSS.

* **HTML** definisce la struttura del documento di output (es. tabelle, div, layout).
* **CSS** controlla lo stile (es. caratteri, spaziatura, colori, allineamento).
*   Le dichiarazioni **XSLT** `**select**` sono utilizzate per popolare dinamicamente i campi dal XML personalizzato, come:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* È possibile utilizzare anche la **logica XSLT** (`<xsl:if>`, `<xsl:for-each>`, ecc.) per gestire la visualizzazione condizionale o iterare sugli elementi di riga.

## 5. Funzione Anteprima (Output di Rendering)

La Funzione Anteprima ti consente di testare e verificare come un documento EDI viene reso con il File Anteprima attuale.

#### **Utilizzo:**

* Carica un file EDI attraverso il normale processo di caricamento.
* Copia l'**ID del Documento** del file caricato.
* Vai all'interfaccia **Anteprima**.
* Apri la **Funzione Anteprima**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Inserisci l'ID del Documento e clicca su **Test**.
* L'anteprima in stile PDF verrà visualizzata utilizzando la configurazione HTML/CSS/XSLT.

Questa funzionalità è cruciale per il debug dei collegamenti dei dati, il perfezionamento del layout e per garantire che il documento sia accurato e visivamente chiaro per gli utenti e i sistemi downstream come **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Video Guida

Una guida video per questo tipo di file è disponibile nella [pagina dei Video.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Usala per seguire la configurazione, la modifica e l'anteprima.
