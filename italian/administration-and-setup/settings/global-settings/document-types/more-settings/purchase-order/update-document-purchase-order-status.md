# Aggiornare lo stato dell'ordine di acquisto del documento



## Panoramica

Quando abilitato, la colonna **Stato PO** sulla dashboard viene aggiornata automaticamente ogni volta che lo stato dell'ordine di acquisto cambia.

## Dove attivare

1. Vai a: **Impostazioni** → **Impostazioni globali** → **Tipo di documento**
2.  Seleziona il tipo di documento desiderato e fai clic su **Altre impostazioni**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  Nella sezione **Ordine di acquisto**, passa all'opzione **Aggiorna lo stato dell'ordine di acquisto del documento**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Come funziona

Quando questa impostazione è abilitata, la colonna **Stato PO** sulla dashboard rifletterà automaticamente lo stato attuale dell'ordine di acquisto. Ad esempio, se lo stato del PO viene aggiornato a _Ricevuto_ o _Fatturato_, la colonna della dashboard si aggiornerà di conseguenza per mostrare questo nuovo stato.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Configurazione

1. **Abilita l'impostazione** Vai alla posizione menzionata sopra e attiva l'impostazione.
2. **Aggiungi la colonna Stato PO (se non è visibile)** Se la colonna **Stato PO** non è già visibile sulla dashboard:
   *   Vai a: **Impostazioni avanzate** → **Imposta colonne della tabella per le organizzazioni**

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Aggiungi il campo dal tipo di documento cercando **Stato PO**
3. **Configura la configurazione di ricerca**
   *   Configura il campo Stato nell'intestazione dell'ordine di acquisto in questo modo:

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Nota:** **L'ordine di acquisto deve essere su Trigger automatico altrimenti gli aggiornamenti dello stato potrebbero non essere correttamente aggiornati**
   * Non sai come **Configurare la configurazione di ricerca? Ecco la** [**guida alla configurazione di ricerca**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Verifica** Ricevi o fattura un PO, quindi controlla la dashboard per confermare che lo stato sia stato aggiornato correttamente.
