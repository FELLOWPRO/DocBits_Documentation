# Verbindung über schreibgeschützte Datenbank herstellen

Dieser Leitfaden führt Sie durch das Verbinden der **schreibgeschützten Datenbank von DocBits mit Power BI Desktop** mithilfe des **PostgreSQL ODBC-Treibers**. Er umfasst die Treiberinstallation, die ODBC-Konfiguration, die Power BI-Integration und die geplante Aktualisierung.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installieren des PostgreSQL ODBC-Treibers

* Laden Sie den neuesten PostgreSQL ODBC-Treiber (**psqlODBC**) von der offiziellen Website herunter:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Führen Sie den Installer aus und folgen Sie dem Einrichtungsassistenten.

### 2. Konfigurieren der ODBC-Datenquelle

* Öffnen Sie den **ODBC-Datenquellen-Administrator (64-Bit)** über die Systemsteuerung oder die Windows-Suche.
* Gehen Sie zum Register **System-DSN** und klicken Sie auf **Hinzufügen**.
* Wählen Sie den Treiber **PostgreSQL Unicode(x64)** aus der Liste und klicken Sie auf **Fertig stellen**.
* Füllen Sie die erforderlichen Felder mit Anmeldeinformationen aus: **DocBits → Einstellungen → Dokumentenverarbeitung → Modul → KI-Dashboard → Schreibgeschützter DB-Zugriff**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Erforderliche Felder:**

* **Name:** Ein Name für die Verbindung (z. B. `Sandbox-Read_Only`)
* **Server:** Kopieren Sie den Host-Wert von DocBits
* **Port:** Kopieren Sie den Port-Wert von DocBits
* **Datenbank:** Kopieren Sie den Datenbanknamen von DocBits
* **Benutzername:** Kopieren Sie den Benutzernamen von DocBits
* **Passwort:** Kopieren Sie das Passwort von DocBits
* **SSL-Modus:** Auf **Erforderlich** setzen (stellt verschlüsselte Kommunikation sicher)

### 3. Verbindung der schreibgeschützten DB mit Power BI herstellen

* Öffnen Sie **Power BI Desktop**.
*   Wählen Sie **Daten abrufen** → **ODBC** → **Verbinden**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Wählen Sie aus der DSN-Liste Ihre konfigurierte Quelle aus (z. B. `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Klicken Sie auf **OK**. Geben Sie die Anmeldeinformationen erneut ein, wenn Sie dazu aufgefordert werden.
  * **Hinweis:** Wenn Sie den Fehler **"Authentifizierung fehlgeschlagen für Benutzer"** sehen, versuchen Sie, Ihr Passwort in **geschweiften Klammern** `**{}**` einzugeben.

### 4. Daten laden und transformieren

* Im **Navigator**-Bereich die Schema-Liste erweitern.
* Öffnen Sie das `**public**`-Schema.
* Wählen Sie die Tabellen aus, die Sie importieren möchten.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Wählen Sie:
  * **Laden** → Direkt in Power BI importieren
  * **Daten transformieren** → Öffnen Sie Power Query zum Formen und Filtern vor dem Laden

### 5. Visualisieren Ihrer Daten

* Verwenden Sie die Power BI-Berichtsfläche, um Dashboards zu erstellen.
* Ziehen Sie Felder, fügen Sie Filter hinzu, wählen Sie Diagrammtypen aus und wenden Sie DAX-Berechnungen an.
* Verwenden Sie den **Power Query-Editor**, um Daten zu bereinigen oder zu verknüpfen, bevor Sie Visuals erstellen.
* Referenz: [Power BI-Dokumentation](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Geplante Aktualisierung aktivieren (optional)

**Hinweis:** **Erfordert Power BI Pro oder Premium + Gateway**

* Um Ihre Berichte mit ClickHouse synchron zu halten:
* Veröffentlichen Sie Ihre `.pbix`-Datei im **Power BI-Dienst**.
* Installieren Sie das **Power BI Gateway** (Standardmodus) auf einem Rechner mit Netzwerkzugriff auf ClickHouse.
* Im Power BI-Dienst:
  * Gehen Sie zu Ihrem Datensatz → **Einstellungen** → **Geplante Aktualisierung**
  * Ordnen Sie Ihre DSN zu und geben Sie Anmeldeinformationen an
* Weitere Informationen [hier](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Beispiel-Dashboards & Datenansichten

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
