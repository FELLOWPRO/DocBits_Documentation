# Testa la tua connessione BOD con Postman

## Panoramica

Questa pagina spiega come verificare l'elaborazione riuscita del tuo BOD (Business Object Document) utilizzando Postman. Testerai l'endpoint API pertinente inviando una richiesta con il tuo file di mappatura BOD. Segui i passaggi qui sotto per completare il processo.

## Accesso alla tua Chiave API e File di mappatura BOD

### Recupero della tua Chiave API

1.  Vai a **Impostazioni → Impostazioni globali → Integrazione e SSO**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Puoi copiare manualmente la tua **Chiave API** oppure cliccare sul pulsante di copia per copiarla negli appunti.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Scaricare il File di mappatura BOD**

1.  Vai a **Impostazioni → Elaborazione dei documenti → Esportazione**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Nella colonna **Azioni** della voce di esportazione pertinente, clicca sul menu a tre punti e seleziona **Modifica**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Trova il **File di mappatura BOD** e clicca sul pulsante **Scaricare** per salvarlo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Testa l'Endpoint in Postman

1.  **Incolla il comando cURL in Postman**

    Apri Postman e incolla il seguente comando cURL nella sezione **Import**. Postman configurerà automaticamente la richiesta.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Imposta la Chiave API**\
    Vai alla scheda **Headers**, trova l'intestazione `X-API-KEY` e incolla la tua chiave API nella colonna **Value**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Carica il File BOD**\
    Vai alla scheda **Body**, trova la chiave `file`, quindi clicca su **Select Files** nella colonna **Value** e carica il tuo file XML BOD.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Invia la Richiesta**\
    Clicca su **Send** per effettuare la chiamata API.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifica la Risposta**\
    Controlla la risposta per confermare che il tuo BOD sia stato elaborato con successo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
