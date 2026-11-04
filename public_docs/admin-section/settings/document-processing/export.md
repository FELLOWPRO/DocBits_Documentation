# Export

## Übersicht

Die Exportseite zeigt alle konfigurierten Exporteinstellungen an, einschließlich ihrer Aktivierung. Von hier aus können Benutzer:

* Vorhandene Exportkonfigurationen anzeigen und verwalten
* Neue Exportverbindungen erstellen (z. B. zu **Infor**, **Infor & IDM**, **Webhook** oder **SFTP**)
* Vorhandene Exportkonfigurationen bearbeiten oder löschen

## Wo finde ich es

Sie finden es unter: **Einstellungen** → **Dokumentenverarbeitung** → **Export**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6ldlcI2sVUEgDdWb9U4%252Fimage.png%3Falt%3Dmedia%26token%3D8368818d-c899-4bee-ad21-a631d6be5c20\&width=768\&dpr=4\&quality=100\&sign=fbfcbd0c\&sv=2)

## **Verwendung der Exportseite**

Wenn Sie die Exportseite öffnen, sehen Sie eine Liste aller vorhandenen Exportkonfigurationen.

Jede Zeile in der Liste zeigt an:

* **Statusanzeige**
  * **Grün** bedeutet, dass der Export aktiv ist
  * **Rot** bedeutet, dass der Export deaktiviert ist
* **Name** – der Name der Exportkonfiguration
* **Dokumententyp** – der Typ des Dokuments, für das der Export konfiguriert ist
* **Unterorganisation** – wenn der Export auf eine spezifische Unterorganisation beschränkt ist
* **Exportmethode** – wohin das Dokument gesendet wird (z. B. Infor, IDM, SFTP)
* **Aktionen** – Schaltflächen zum **Bearbeiten, Löschen** oder **Aktivieren/Deaktivieren** der Konfiguration

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyN87I5gzXxwGoAqC6zMF%252Fimage.png%3Falt%3Dmedia%26token%3D7df9d573-7e57-4ace-99c6-15a83691b926\&width=768\&dpr=4\&quality=100\&sign=6221cb80\&sv=2)

#### **Wichtige Regeln für Exportkonfigurationen**

Für jeden **Dokumententyp innerhalb einer bestimmten Organisation oder Unterorganisation** gelten die folgenden Regeln:

* Sie können **nur einen aktiven Infor-Export haben**
* Sie können **nur einen aktiven Nicht-Infor-Export haben** (z. B. Webhook, SFTP)

Es ist jedoch möglich:

* **Einen aktiven Infor-Export** _und_ **einen aktiven Nicht-Infor-Export** gleichzeitig für denselben Dokumententyp zu haben
* **Unterschiedliche Exportkonfigurationen für verschiedene Unterorganisationen** zu haben — zum Beispiel einen Infor-Export für Sub-Org A und einen anderen Infor-Export für Sub-Org B

## **Erstellen eines neuen Exports**

Um einen neuen Export zu erstellen:

1. Klicken Sie auf die Schaltfläche **"Neu"**.\
   &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FTsHrIAUpe7EqenIzNAaJ%252Fimage.png%3Falt%3Dmedia%26token%3Dd2dbc996-b129-443c-a8df-9927a6f43a36\&width=300\&dpr=4\&quality=100\&sign=8769c331\&sv=2)
2. Wählen Sie den **Exporttyp** aus, den Sie konfigurieren möchten (z. B. Infor, IDM, SFTP).
3. Füllen Sie die erforderlichen Felder basierend auf dem Exporttyp aus.
4. Speichern Sie die Konfiguration.

## Exportoptionen

#### Webhook

<details>

<summary>Webhook</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCwXUqFdCbRI5lRW49ymw%252Fimage.png%3Falt%3Dmedia%26token%3D798c0f40-6c4a-4650-9320-af2c17634fe9\&width=768\&dpr=4\&quality=100\&sign=15836833\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Export-URL** Die Ziel-URL, wohin das Dokument exportiert werden soll.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzwUCWTdFETTvuTGl8qAn%252Fimage.png%3Falt%3Dmedia%26token%3D3f94b210-0128-4710-ae69-150a1363ce49\&width=768\&dpr=4\&quality=100\&sign=4ecd353\&sv=2)



#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Benutzername** Der Benutzername, der zur Authentifizierung gegen den SFTP-Server verwendet wird.
* **Passwort** Das entsprechende Passwort für das SFTP-Konto. Stellen Sie sicher, dass das Konto Schreibzugriff auf den angegebenen Ordner hat.
* **Server-URL** Der Hostname oder die IP-Adresse des Ziel-SFTP-Servers.
* **Port** Der Port, der zur Verbindung mit dem SFTP-Server verwendet wird.
* **Ordner** Der Pfad auf dem SFTP-Server, wohin Dokumente hochgeladen werden sollen (z. B. `/eingehend/rechnungen/`). Muss existieren und beschreibbar sein.
*   **XSLT-Datei (Optional)**

    Die **XSLT-Datei** ermöglicht die Transformation des Standard-DocBits-Exportformats.

    * **Wann zu verwenden:** Nur wenn das empfangende System eine andere Struktur oder spezifische Formatierung erfordert, die sich vom Standard-DocBits-Format unterscheidet.
    * **Leer lassen**, wenn das Standardexportformat den Anforderungen entspricht.

</details>

#### Infor-Export nach SFTP

<details>

<summary>Infor-Export nach SFTP</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FU0W4Qdy7ZlNoCn3E9wX5%252Fimage.png%3Falt%3Dmedia%26token%3D33673a12-55c4-479b-8ca8-b7c95e7a6a89\&width=768\&dpr=4\&quality=100\&sign=4af07f48\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Benötigen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **BOD-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Benötigen Sie Hilfe bei der Erstellung? Sehen Sie sich den BOD-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Ordner** Der Pfad auf dem SFTP-Server, wohin Dokumente hochgeladen werden sollen (z. B. `/eingehend/rechnungen/`). Muss existieren und beschreibbar sein.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6e4B9BWQWgHvcHhduXKb%252Fimage.png%3Falt%3Dmedia%26token%3D09e9534e-9268-4221-bd7b-89b621c80670\&width=768\&dpr=4\&quality=100\&sign=b03835a\&sv=2)



#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **Benutzername** Der Benutzername, der zur Verbindung mit dem SMB-Share verwendet wird.
* **Passwort** Das entsprechende Passwort für die SMB-Authentifizierung.
* **Server-URL** Die Adresse des SMB-Servers.
* **Port** Portnummer, die zum Zugriff auf den SMB-Share verwendet wird.
* **Ordner** Der Ordnerpfad innerhalb des SMB-Shares, wohin Dokumente gespeichert werden sollen (z. B. `/eingehend/rechnungen/`). Muss existieren und beschreibbar sein.
*   **JPL-Mapping-Datei (Optional)**

    Die **JPL-Datei** wird verwendet, um eine Transformation der exportierten Daten vorzunehmen, bevor sie in den SMB-Share geschrieben werden.

    * **Wann zu verwenden:** Nur wenn die exportierten Dokumentendaten angepasst werden müssen, um dem externen Format oder den Systemerwartungen zu entsprechen.
    * **Leer lassen**, wenn keine Transformation erforderlich ist.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FQ1AtdmTRZr1sGkH6oLwP%252Fimage.png%3Falt%3Dmedia%26token%3D720a4184-3f91-4b70-b3da-b846f3cce030\&width=768\&dpr=4\&quality=100\&sign=dc678c2c\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Benötigen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **Cloud / On-Prem-Umschalter** Ein Schalter, um den Infor-Bereitstellungstyp anzugeben:
  * **Cloud**: Wählen Sie dies, wenn Sie ein Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet ist.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FcYDXwDYH4RSc5vcY4fmr%252Fimage.png%3Falt%3Dmedia%26token%3Da9cfac80-9795-4e8f-a664-e268c9b4856c\&width=768\&dpr=4\&quality=100\&sign=5a4b0bd0\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumententyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **BOD-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den BOD-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem-Umschalter** Ein Schalter, um den Infor-Bereitstellungstyp anzugeben:
  * **Cloud**: Wählen Sie dies, wenn Sie ein Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet wird.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FY13EX2xxOKLZzliAAHB0%252Fimage.png%3Falt%3Dmedia%26token%3D94335922-6342-405f-8c6d-29fdf2f31a2e\&width=768\&dpr=4\&quality=100\&sign=c0322806\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumenttyp** Dropdown-Liste aller verfügbaren Dokumenttypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **BOD-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den BOD-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file)
* **Cloud / On-Prem-Umschalter** Ein Schalter, um den Infor-Bereitstellungstyp anzugeben:
  * **Cloud**: Wählen Sie dies, wenn Sie ein Infor CloudSuite-Kunde sind.
  * **On-Prem**: Wählen Sie dies, wenn Infor selbst gehostet wird.

</details>

### Für Infor CloudSuite Kunden

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4SfGDqhA4KDrPfJ5vcsT%252Fimage.png%3Falt%3Dmedia%26token%3D4833c0dc-af8b-48a1-a977-6cc8ded20277\&width=768\&dpr=4\&quality=100\&sign=6301596\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die gewählte Unterorganisation.
* **Dokumenttyp** Dropdown-Liste aller verfügbaren Dokumenttypen. Dies bestimmt, auf welchen Dokumenttyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **LN-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich das LN-Mapping-Beispiel an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAN4T0aQEoogbUA8PUgy9%252Fimage.png%3Falt%3Dmedia%26token%3Da2b91153-858f-4711-abcc-4ed7ad60d49a\&width=768\&dpr=4\&quality=100\&sign=bb6bda83\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumententyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **M3-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich das M3-Mapping-Beispiel an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>



![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCdoduCkkbnomw3ahZgul%252Fimage.png%3Falt%3Dmedia%26token%3D4e5c7d08-5eaf-4c3e-9918-5cce58d8e3b3\&width=768\&dpr=4\&quality=100\&sign=e984c4e0\&sv=2)

#### **Feldbeschreibungen**

* **Titel** Der Name der Exportkonfiguration. Dies wird in der Exportliste angezeigt.
* **Unterorganisation** _(optional)_ Ein Dropdown mit allen verfügbaren Unterorganisationen.
  * Wenn leer gelassen: gilt für die Hauptorganisation.
  * Wenn ausgewählt: gilt der Export nur für die ausgewählte Unterorganisation.
* **Dokumententyp** Dropdown-Liste aller verfügbaren Dokumententypen. Dies bestimmt, auf welchen Dokumententyp diese Exportkonfiguration angewendet wird.
* **ION-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus.
* **IDM-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den IDM-Mapping-Leitfaden an](https://docs.docbits.com/infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file)
* **M3 toml-Mapping-Datei** Wählen Sie eine Mapping-Datei aus dem Dateimanager aus oder verwenden Sie die Option Toml auswählen, um ein mit dem Regel-Manager erstelltes toml zu verwenden. [Brauchen Sie Hilfe bei der Erstellung? Sehen Sie sich den Regel-Manager-Leitfaden an](https://docs.docbits.com/administration-and-setup/settings/document-processing/rule-manager)

</details>
