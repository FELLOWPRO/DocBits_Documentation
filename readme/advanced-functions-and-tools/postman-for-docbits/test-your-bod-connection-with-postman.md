# Test uw BOD-verbinding met Postman

## Overzicht

Deze pagina legt uit hoe u de succesvolle verwerking van uw BOD (Business Object Document) kunt verifiëren met behulp van Postman. U zult de relevante API-endpoint testen door een verzoek te sturen met uw BOD-mappingbestand. Volg de onderstaande stappen om het proces te voltooien.

## Toegang tot uw API-sleutel en BOD-mappingbestand

### Ophalen van uw API-sleutel

1.  Ga naar **Instellingen → Globale instellingen → Integratie en SSO**.

    ![Instellingenpagina in DocBits met de Global Settings-navigatie open en Integrations & SSO gemarkeerd tussen Document Types en Email Templates](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  U kunt uw **API-sleutel** handmatig kopiëren of op de kopieerknop klikken om deze naar uw klembord te kopiëren.

    ![Pagina Integration & SSO in DocBits met het veld API Key en de bijbehorende kopieerknop boven de sectie SSO Service Provider Settings](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Downloaden van het BOD-mappingbestand**

1.  Ga naar **Instellingen → Documentverwerking → Exporteren**.

    ![Instellingenpagina in DocBits met de Document Processing-navigatie open met Import, OCR Settings, Classification and Extraction en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  In de kolom **Acties** van de relevante exportvermelding, klik op het menu met drie stippen en selecteer **Bewerking**.

    ![Pagina Export settings in DocBits met de rijen google Invoice webhook en Infor LN Test Invoice en het geopende menu Actions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Zoek het **BOD-mappingbestand** en klik op de **Download**-knop om het op te slaan.

    ![Infor ION-dialoogvenster met het veld Title Test en de downloadknoppen ION-Mapping File, IDM Mapping File en BOD-Mapping File](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Test de Endpoint in Postman

1.  **Plak de cURL-opdracht in Postman**

    Open Postman en plak de volgende cURL-opdracht in de sectie **Import**. Postman configureert het verzoek automatisch.

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

    ![Postman-werkruimte met het welkomstscherm, het tabblad History en de optie Create a new request](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![Postman-dialoogvenster Import met het veld voor het plakken van cURL open om het BOD-verzoek te importeren](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Stel de API-sleutel in**\
    Ga naar het **Headers**-tabblad, zoek de `X-API-KEY`-header en plak uw API-sleutel in de kolom **Value**.

    ![Postman-verzoek voor https://api.docbits.com/prod-api/import/purchase_order_bod met het tabblad Headers en de rij X-API-KEY](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Upload het BOD-bestand**\
    Ga naar het **Body**-tabblad, zoek de `file`-sleutel, klik vervolgens op **Select Files** in de kolom **Value** en upload uw BOD XML-bestand.

    ![Postman-request-tabblad Body met de form-data-sleutels org_id, sub_org_id, file met Select Files en custom_fields_mapping](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Verzend het verzoek**\
    Klik op **Send** om de API-aanroep te doen.

    ![Postman-request met het tabblad Authorization geopend en No Auth geselecteerd](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifieer de reactie**\
    Controleer de reactie om te bevestigen dat uw BOD succesvol is verwerkt.

    ![Postman-antwoordpaneel met status 200 OK en de bodymelding BOD processed successfully](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
