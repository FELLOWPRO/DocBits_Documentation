# Testen Sie Ihre BOD-Verbindung mit Postman

## Übersicht

Diese Seite erklärt, wie Sie die erfolgreiche Verarbeitung Ihres BOD (Business Object Document) mit Postman überprüfen. Sie werden den relevanten API-Endpunkt testen, indem Sie eine Anfrage mit Ihrer BOD-Mapping-Datei senden. Befolgen Sie die folgenden Schritte, um den Prozess abzuschließen.

## Zugriff auf Ihren API-Schlüssel und die BOD-Mapping-Datei

### Abrufen Ihres API-Schlüssels

1.  Gehen Sie zu **Einstellungen → Globale Einstellungen → Integration und SSO**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Sie können entweder Ihren **API-Schlüssel** manuell kopieren oder auf die Schaltfläche "Kopieren" klicken, um ihn in Ihre Zwischenablage zu kopieren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Herunterladen der BOD-Mapping-Datei**

1.  Gehen Sie zu **Einstellungen → Verarbeitung von Dokumenten → Exportieren**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Klicken Sie in der **Aktionen**-Spalte des relevanten Exporteintrags auf das Drei-Punkte-Menü und wählen Sie **Bearbeiten**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Suchen Sie die **BOD-Mapping-Datei** und klicken Sie auf die Schaltfläche **Herunterladen**, um sie zu speichern.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Testen Sie den Endpunkt in Postman

1.  **Fügen Sie den cURL-Befehl in Postman ein**

    Öffnen Sie Postman und fügen Sie den folgenden cURL-Befehl in den Abschnitt **Import** ein. Postman konfiguriert die Anfrage automatisch.

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
2.  **Setzen Sie den API-Schlüssel**\
    Gehen Sie zum **Headers**-Tab, suchen Sie den `X-API-KEY`-Header und fügen Sie Ihren API-Schlüssel in die **Value**-Spalte ein.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Laden Sie die BOD-Datei hoch**\
    Gehen Sie zum **Body**-Tab, suchen Sie den `file`-Schlüssel, klicken Sie dann auf **Select Files** in der **Value**-Spalte und laden Sie Ihre BOD-XML-Datei hoch.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Senden Sie die Anfrage**\
    Klicken Sie auf **Send**, um den API-Aufruf zu tätigen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Überprüfen Sie die Antwort**\
    Überprüfen Sie die Antwort, um zu bestätigen, dass Ihr BOD erfolgreich verarbeitet wurde.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
