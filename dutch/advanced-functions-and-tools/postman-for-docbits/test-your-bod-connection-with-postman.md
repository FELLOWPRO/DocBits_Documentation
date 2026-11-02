# Test uw BOD-verbinding met Postman

## Overzicht

Deze pagina legt uit hoe u de succesvolle verwerking van uw BOD (Business Object Document) kunt verifiëren met behulp van Postman. U zult de relevante API-endpoint testen door een verzoek te sturen met uw BOD-mappingbestand. Volg de onderstaande stappen om het proces te voltooien.

## Toegang tot uw API-sleutel en BOD-mappingbestand

### Ophalen van uw API-sleutel

1.  Ga naar **Instellingen → Globale instellingen → Integratie en SSO**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  U kunt uw **API-sleutel** handmatig kopiëren of op de kopieerknop klikken om deze naar uw klembord te kopiëren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Downloaden van het BOD-mappingbestand**

1.  Ga naar **Instellingen → Documentverwerking → Exporteren**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  In de kolom **Acties** van de relevante exportvermelding, klik op het menu met drie stippen en selecteer **Bewerking**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Zoek het **BOD-mappingbestand** en klik op de **Download**-knop om het op te slaan.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

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

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Stel de API-sleutel in**\
    Ga naar het **Headers**-tabblad, zoek de `X-API-KEY`-header en plak uw API-sleutel in de kolom **Value**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Upload het BOD-bestand**\
    Ga naar het **Body**-tabblad, zoek de `file`-sleutel, klik vervolgens op **Select Files** in de kolom **Value** en upload uw BOD XML-bestand.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Verzend het verzoek**\
    Klik op **Send** om de API-aanroep te doen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifieer de reactie**\
    Controleer de reactie om te bevestigen dat uw BOD succesvol is verwerkt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
