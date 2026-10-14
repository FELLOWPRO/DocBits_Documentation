# Guida al File di Trasformazione EDI

## 1. Panoramica

Il **File di Trasformazione** definisce come l'XML strutturato—creato utilizzando il **File Descrittore della Struttura**—viene convertito in un formato XML personalizzato che corrisponde ai requisiti specifici del tipo di documento o modulo della tua organizzazione.

Questa trasformazione viene eseguita utilizzando **XSLT (Extensible Stylesheet Language Transformations)**, che può essere creato e mantenuto attraverso l'**Editor XSLT** nell'interfaccia di DocBits.

## 2. Scopo e Funzione

* Trasforma l'**XML intermedio** (output dal Descrittore della Struttura) in un **XML finale** allineato con lo schema del tuo documento.
* Consente flessibilità per adattarsi ai formati dei partner EDI e ai requisiti interni del sistema.
* Creato utilizzando le **regole XSLT**, che ti permettono di definire mappature, formattazione dei valori, logica condizionale e struttura.

## 3. Accesso e Modifica di Base

#### Accesso al File

1.  Vai su **Impostazioni → Tipo di Documento** → \[Il Tuo Documento (es. _Ordine di Acquisto_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Sotto la scheda **E-Doc**, seleziona il tuo formato (es. **EDI**).
3.  Clicca su **Trasformazione** per visualizzare o modificare.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Gestione delle Bozze

* **Crea una Bozza**: Clicca sull'icona della ✏️ matita.
* **Elimina Bozze**: Usa l'icona del 🗑️ cestino per rimuovere le bozze non utilizzate.
* **Attiva le Modifiche**: Clicca sul segno di spunta ✅ per pubblicare una versione.
  * **Nota**: Attivando una nuova versione si **disattiverà automaticamente** la precedente.

## 4. Editor XSLT

Il File di Trasformazione viene modificato utilizzando un **Editor XSLT** integrato che supporta l'evidenziazione della sintassi e la validazione.

* Aggiungi modelli per mappare percorsi specifici dall'XML di input alla struttura desiderata.
* Utilizza la logica condizionale (es. `<xsl:if>`, `<xsl:choose>`) per gestire formati di dati opzionali o variabili.
* Applica funzioni di formattazione secondo necessità (es. manipolazione di stringhe, formattazione delle date).

## 5. Funzione Anteprima (Anteprima XML Trasformato)

La **Funzione Anteprima** ti permette di testare e visualizzare come un file EDI caricato viene elaborato utilizzando il corrente **File di Trasformazione**.

#### Utilizzo

* Carica un file EDI tramite il flusso di caricamento standard.
* Copia l'**ID del Documento** del file caricato.
* Vai all'interfaccia del **File di Trasformazione**.
*   Apri la **Funzione Anteprima**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Inserisci l'**ID del Documento** nel campo e premi **Test**.
* Verrà visualizzato l'**output XML trasformato** risultante.

Questo è particolarmente utile per il debug delle mappature XSLT e per garantire che la struttura XML finale soddisfi i requisiti del tuo formato.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Video Guida

Una guida video per questo tipo di file è disponibile nella [pagina dei Video.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilizzala per seguire la configurazione, la modifica e l'anteprima.
