# Modelli di E-Mail

{% embed url="https://youtu.be/R5IrCpiP__4" %}

## **Panoramica**

I modelli di email ti consentono di personalizzare le notifiche email automatizzate inviate da DocBits. I modelli possono includere campi dinamici (ad es., `{{FieldID}}`), immagini e formattazione HTML.

## **Accesso ai Modelli di Email**

1.  Naviga su: **Impostazioni → Impostazioni Globali → Modelli di Email**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. La dashboard visualizza tutti i modelli con:
   * **Nome**
   * **Oggetto**
   * Data dell'**Ultima Modifica**
   * **Azioni** (Modifica o Elimina).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Creazione di un Nuovo Modello**

### **1 Configurazione Base**

* Clicca su **Nuovo**.
* Compila i campi sulla destra:
  * **Nome**: Identificatore del modello (ad es., "Errore del Documento").
  * **Oggetto**: Oggetto dell'email (ad es., "Azione Richiesta: Errore del Documento").
  *   **Tipo di Documento**: Seleziona dal menu a discesa (ad es., "Fattura").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Editor del Modello**

* **Menu**: Formatta il testo, aggiungi link o inserisci tabelle.
* **Editor HTML**: Clicca sull'icona `<>` per modificare l'HTML grezzo.
* **Aggiungi Immagini**: Usa la funzione **Carica**.
*   **Campi Dinamici**: Inserisci i valori dei campi del documento tramite

    * **Opzione Campo Variabile**: Seleziona dal menu a discesa.
    * **Inserimento Manuale**: Digita `{{FieldID}}` (ad es., `{{NumeroFattura}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Salvataggio**

* Clicca su **Salva** per memorizzare il modello.

## **Invio di una Email di Test**

1.  Apri il modello e clicca su **Invia Test**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Inserisci:
   * **Email del Destinatario** (obbligatorio).
   * **Valori dei Campi** (opzionale; dati di esempio per segnaposto). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Controlla l'email di test e modifica il modello se necessario.

## **Utilizzo dei Modelli nelle Notifiche**

I modelli salvati possono essere collegati ai flussi di lavoro delle [**Notifiche Emai**](email-notification/)**l** (ad es., promemoria di approvazione, aggiornamenti di stato).
