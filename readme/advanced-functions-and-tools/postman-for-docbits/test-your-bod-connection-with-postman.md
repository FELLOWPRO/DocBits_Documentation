# Testa la tua connessione BOD con Postman

## Panoramica

Questa pagina spiega come verificare l'elaborazione riuscita del tuo BOD (Business Object Document) utilizzando Postman. Testerai l'endpoint API pertinente inviando una richiesta con il tuo file di mappatura BOD. Segui i passaggi qui sotto per completare il processo.

## Accesso alla tua Chiave API e File di mappatura BOD

### Recupero della tua Chiave API

1.  Vai a **Impostazioni → Impostazioni globali → Integrazione e SSO**.

    ![Pagina delle impostazioni in DocBits con la navigazione Global Settings aperta ed Integrations & SSO evidenziato tra Document Types ed Email Templates](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Puoi copiare manualmente la tua **Chiave API** oppure cliccare sul pulsante di copia per copiarla negli appunti.

    ![Pagina Integration & SSO in DocBits che mostra il campo API Key con il relativo pulsante di copia sopra la sezione SSO Service Provider Settings](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Scaricare il File di mappatura BOD**

1.  Vai a **Impostazioni → Elaborazione dei documenti → Esportazione**.

    ![Pagina delle impostazioni in DocBits con la navigazione Document Processing aperta che elenca Import, OCR Settings, Classification and Extraction e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Nella colonna **Azioni** della voce di esportazione pertinente, clicca sul menu a tre punti e seleziona **Modifica**.

    ![Pagina Export settings in DocBits con le righe google Invoice webhook e Infor LN Test Invoice e il menu Actions aperto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Trova il **File di mappatura BOD** e clicca sul pulsante **Scaricare** per salvarlo.

    ![Finestra di dialogo Infor ION con il campo Title Test e i pulsanti di download ION-Mapping File, IDM Mapping File e BOD-Mapping File](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

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

    ![Area di lavoro Postman con la schermata di benvenuto, la scheda History e l'opzione Create a new request](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![Finestra di dialogo Import di Postman con il campo per incollare cURL aperto per importare la richiesta BOD](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Imposta la Chiave API**\
    Vai alla scheda **Headers**, trova l'intestazione `X-API-KEY` e incolla la tua chiave API nella colonna **Value**.

    ![Richiesta Postman per https://api.docbits.com/prod-api/import/purchase_order_bod con la scheda Headers e la riga X-API-KEY](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Carica il File BOD**\
    Vai alla scheda **Body**, trova la chiave `file`, quindi clicca su **Select Files** nella colonna **Value** e carica il tuo file XML BOD.

    ![Scheda Body della richiesta Postman con le chiavi form-data org_id, sub_org_id, file con Select Files e custom_fields_mapping](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Invia la Richiesta**\
    Clicca su **Send** per effettuare la chiamata API.

    ![Richiesta Postman con la scheda Authorization aperta e No Auth selezionato](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifica la Risposta**\
    Controlla la risposta per confermare che il tuo BOD sia stato elaborato con successo.

    ![Pannello di risposta Postman con stato 200 OK e il messaggio del corpo BOD processed successfully](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
