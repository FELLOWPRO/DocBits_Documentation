# Export

## Übersicht

Die Exportseite zeigt alle konfigurierten Exporteinstellungen an, einschließlich ihrer Aktivierung. Von hier aus können Benutzer:

* Vorhandene Exportkonfigurationen anzeigen und verwalten
* Neue Exportverbindungen erstellen (z. B. zu **Infor**, **Infor & IDM**, **Webhook** oder **SFTP**)
* Vorhandene Exportkonfigurationen bearbeiten oder löschen

## Wo finde ich es

Sie finden es unter: **Einstellungen** → **Dokumentenverarbeitung** → **Export**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Verwendung der Exportseite**

Wenn Sie die Exportseite öffnen, sehen Sie eine Liste aller vorhandenen Exportkonfigurationen.

Jede Zeile in der Liste zeigt an:

* **Statusanzeige**
  * **Grün** bedeutet, dass der Export aktiv ist
  * **Rot** bedeutet, dass der Export deaktiviert ist
* **Name** – der Name der Exportkonfiguration
* **Dokumententyp** – der Typ des Dokuments, für das der Export konfiguriert ist
* **Unterorganisation** – wenn der Export auf eine bestimmte Unterorganisation beschränkt ist
* **Exportmethode** – wohin das Dokument gesendet wird (z. B. Infor, IDM, SFTP)
* **Aktionen** – Schaltflächen zum **Bearbeiten, Löschen** oder **Aktivieren/Deaktivieren** der Konfiguration

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Wichtige Regeln für Exportkonfigurationen**

Für jeden **Dokumententyp** **innerhalb einer bestimmten Organisation oder Unterorganisation** gelten die folgenden Regeln:

* Sie können **nur einen aktiven Infor-Export** haben
* Sie können **nur einen aktiven Nicht-Infor-Export** haben (z. B. Webhook, SFTP)

Es ist jedoch möglich:

* **Einen aktiven Infor-Export** _und_ **einen aktiven Nicht-Infor-Export** gleichzeitig für denselben Dokumententyp zu haben
* **Unterschiedliche Exportkonfigurationen für verschiedene Unterorganisationen** — zum Beispiel einen Infor-Export für Unter-Org A und einen anderen Infor-Export für Unter-Org B

## **Erstellen eines neuen Exports**

Um einen neuen Export zu erstellen:

1. Klicken Sie auf die Schaltfläche **„Neu"**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Wählen Sie den **Exporttyp** aus, den Sie konfigurieren möchten (z. B. Infor, IDM, SFTP).
3. Füllen Sie die erforderlichen Felder basierend auf dem Exporttyp aus.
4. Speichern Sie die Konfiguration.

## Exportoptionen

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Export URL** Die Ziel-URL, wohin das Dokument exportiert werden soll.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Username** Der Benutzername zur Authentifizierung am SFTP-Server.
* **Password** Das entsprechende Passwort für das SFTP-Konto. Stellen Sie sicher, dass das Konto Schreibzugriff auf den angegebenen Ordner hat.
* **Server URL** Der Hostname oder die IP-Adresse des Ziel-SFTP-Servers.
* **Port** Der Port zur Verbindung mit dem SFTP-Server.
* **Folder** Der Pfad auf dem SFTP-Server, wohin Dokumente hochgeladen werden sollen (z. B. `/incoming/invoices/`). Muss existieren und beschreibbar sein.
*   **XSLT File (Optional)**

    Die **XSLT-Datei** ermöglicht die Transformation des Standard-DocBits-Exportformats.

    * **Wann zu verwenden:** Nur wenn das empfangende System eine andere Struktur oder spezifische Formatierung erfordert, die vom DocBits-Standard abweicht.
    * **Leer lassen**, wenn das Standardexportformat den Anforderungen entspricht.



**Erweiterte Einstellungen:**

* **Filename Export Mode** Gibt an, ob die exportierte Datei ihren ursprünglichen Dateinamen behält oder mit der DocBits-Dokument-ID umbenannt wird.
* **Include Document History** Wenn aktiviert, enthält die exportierte Datei den Dokumentenverlauf basierend auf den im Dashboard verfügbaren Protokollen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Infor-Export nach SFTP

<details>

<summary>Infor-Export nach SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe BOD-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** Der Pfad auf dem SFTP-Server, wohin Dokumente hochgeladen werden sollen (z. B. `/incoming/invoices/`). Muss existieren und beschreibbar sein.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Username** Der Benutzername zur Verbindung mit dem SMB-Share.
* **Password** Das entsprechende Passwort für die SMB-Authentifizierung.
* **Server URL** Die Adresse des SMB-Servers.
* **Port** Portnummer für den Zugriff auf den SMB-Share.
* **Folder** Der Ordnerpfad innerhalb des SMB-Shares, wohin Dokumente gespeichert werden sollen (z. B. `/incoming/invoices/`). Muss existieren und beschreibbar sein.
*   **JPL Mapping File (Optional)**

    Die **JPL-Datei** wird verwendet, um eine Transformation der exportierten Daten vorzunehmen, bevor sie in den SMB-Share geschrieben werden.

    * **Wann zu verwenden:** Nur wenn die exportierten Dokumentdaten angepasst werden müssen, um externen Formatierungs- oder Systemanforderungen zu entsprechen.
    * **Leer lassen**, wenn keine Transformation erforderlich ist.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Ein Schalter zur Angabe des Infor-Bereitstellungstyps:
  * **Cloud**: Wählen Sie dies, wenn Sie Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet wird.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **BOD Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe BOD-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Ein Schalter zur Angabe des Infor-Bereitstellungstyps:
  * **Cloud**: Wählen Sie dies, wenn Sie Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet wird.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe BOD-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Ein Schalter zur Angabe des Infor-Bereitstellungstyps:
  * **Cloud**: Wählen Sie dies, wenn Sie Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet wird.

</details>

### Für Infor CloudSuite-Kunden

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe LN-Mapping-Beispiel](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe M3-Mapping-Beispiel](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Feldbeschreibungen**

* **Title** Der Name der Exportkonfiguration. Dieser wird in der Exportliste angezeigt.
* **Sub-Organization** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Document Type** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager.
* **IDM Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager. [Benötigen Sie Hilfe bei der Erstellung? Siehe IDM-Mapping-Leitfaden](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Wählen Sie eine Mapping-Datei aus dem Dateimanager oder verwenden Sie die Option Toml auswählen, um ein mit dem Regel-Manager erstelltes toml zu verwenden. [Benötigen Sie Hilfe bei der Erstellung? Siehe Regel-Manager-Leitfaden](rule-manager/)

</details>
