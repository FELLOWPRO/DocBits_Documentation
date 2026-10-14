# E-Mail-Vorlagen

## **Übersicht**

{% embed url="https://youtu.be/R5IrCpiP__4" %}

E-Mail-Vorlagen ermöglichen es Ihnen, automatisierte E-Mail-Benachrichtigungen anzupassen, die von DocBits gesendet werden. Vorlagen können dynamische Felder (z. B. `{{FieldID}}`), Bilder und HTML-Formatierung enthalten.

## **Zugriff auf E-Mail-Vorlagen**

1.  Navigieren Sie zu: **Einstellungen → Globale Einstellungen → E-Mail-Vorlagen**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. Das Dashboard zeigt alle Vorlagen mit:
   * **Name**
   * **Betreff**
   * **Zuletzt geändert am** Datum
   * **Aktionen** (Bearbeiten oder Löschen).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Erstellen einer neuen Vorlage**

### **1 Grundlegende Einrichtung**

* Klicken Sie auf **Neu**.
* Füllen Sie die Felder auf der rechten Seite aus:
  * **Name**: Vorlagenkennung (z. B. "Dokumentfehler").
  * **Betreff**: E-Mail-Betreffzeile (z. B. "Aktion erforderlich: Dokumentfehler").
  *   **Dokumenttyp**: Auswahl aus dem Dropdown-Menü (z. B. "Rechnung").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Vorlagen-Editor**

* **Menü**: Text formatieren, Links hinzufügen oder Tabellen einfügen.
* **HTML-Editor**: Klicken Sie auf das `<>`-Symbol, um den Roh-HTML-Code zu bearbeiten.
* **Bilder hinzufügen**: Verwenden Sie die **Hochladen**-Funktion.
*   **Dynamische Felder:** Fügen Sie Dokumentfeldwerte ein, indem Sie

    * **Variable Feldoption**: Aus einem Dropdown-Menü auswählen.
    * **Manuelle Eingabe**: Geben Sie `{{FieldID}}` ein (z. B. `{{InvoiceNumber}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Speichern**

* Klicken Sie auf **Speichern**, um die Vorlage zu speichern.

## **Senden einer Test-E-Mail**

1.  Öffnen Sie die Vorlage und klicken Sie auf **Test senden**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Geben Sie ein:
   * **Empfänger-E-Mail** (erforderlich).
   * **Feldwerte** (optional; Platzhalter für Testdaten).\
     <br>
3. Überprüfen Sie die Test-E-Mail und passen Sie die Vorlage bei Bedarf an.

## **Verwendung von Vorlagen in Benachrichtigungen**

Gespeicherte Vorlagen können mit [**E-Mail-Benachrichtigungen**](email-notification.md) verknüpft werden (z. B. Genehmigungserinnerungen, Statusaktualisierungen).
