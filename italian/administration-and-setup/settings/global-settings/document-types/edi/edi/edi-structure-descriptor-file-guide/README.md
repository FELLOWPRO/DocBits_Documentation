# Guida al File Descrittore della Struttura EDI

## **1. Panoramica**

Il **File Descrittore della Struttura** definisce come i segmenti EDI ripetuti (ad esempio, `N1`–`N4`) sono raggruppati in JSON strutturato. Garantisce:

* **Analisi accurata** degli elementi correlati come unità singole.
* **Output coerente** per i sistemi downstream.

_Per un esempio completo con dettagli del segmento, vedere_ [_Esempio del Descrittore della Struttura_](edi-structure-descriptor.md)_._

## **2. Accesso e Modifica di Base**

#### **Accesso al File**

1.  **Impostazioni** → **Tipo di Documento** → \[Il Tuo Documento (ad esempio, _Ordine di Acquisto_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sotto **E-Doc**, seleziona il tuo formato (ad esempio, _EDI_ ).
3.  Clicca su **Descrittore della Struttura**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Gestione delle Bozze**

* **Crea una Bozza**: Clicca sull'icona della ✏️ matita per iniziare la modifica.
* **Elimina le Bozze**: Usa l'icona del 🗑️ cestino per rimuovere le bozze non utilizzate.
* **Attiva le Modifiche**: Clicca sull'icona del ✅ segno di spunta per approvare e pubblicare le modifiche.
  * **Nota**: Attivare una nuova versione **disattiverà automaticamente** quella precedente.

## 3. Funzione Anteprima (Anteprima XML Analizzato)

La **Funzione Anteprima** ti consente di testare e visualizzare come un file EDI caricato viene analizzato utilizzando il File Descrittore della Struttura corrente.

#### Utilizzo

* Carica un file EDI tramite il flusso di caricamento standard.
* Copia il **ID del Documento** del file caricato.
* Vai all'interfaccia del **File Descrittore della Struttura**.
*   Apri la **Funzione Anteprima**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Inserisci il **ID del Documento** nel campo e premi **Test**.
* Verrà visualizzato l'**output XML strutturato** risultante.

Questo è particolarmente utile per il debug dei mapping e la convalida dei raggruppamenti strutturali in tempo reale.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Video Guida

Una guida video per questo tipo di file è disponibile nella [pagina dei Video.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Usala per seguire la configurazione, la modifica e l'anteprima.
