# Verbindung über schreibgeschützte Datenbank

Diese Anleitung führt Sie durch die Verbindung der **schreibgeschützten Datenbank von DocBits mit Power BI Desktop** über den **PostgreSQL-ODBC-Treiber**. Sie behandelt die Treiberinstallation, die ODBC-Konfiguration, die Power-BI-Integration und die geplante Aktualisierung.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. PostgreSQL-ODBC-Treiber installieren

* Laden Sie den aktuellen PostgreSQL-ODBC-Treiber (**psqlODBC**) von der offiziellen Website herunter:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Starten Sie das Installationsprogramm und folgen Sie dem Setup-Assistenten.

#### 2. ODBC-Datenquelle konfigurieren

* Öffnen Sie den **ODBC-Datenquellen-Administrator (64-Bit)** über die Systemsteuerung oder die Windows-Suche.
* Wechseln Sie zur Registerkarte **System-DSN** und klicken Sie auf **Hinzufügen**.
* Wählen Sie den Treiber **PostgreSQL Unicode(x64)** aus der Liste aus und klicken Sie auf **Fertig stellen**.
* Tragen Sie in die erforderlichen Felder die Zugangsdaten aus folgendem Bereich ein:\n  **DocBits → Settings → Document Processing → Module → AI Dashboard → Read-Only DB Access**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt=""><figcaption></figcaption></figure>

**Erforderliche Felder:**

* **Name:** Ein Name für die Verbindung (z. B. `Sandbox-Read_Only`)
* **Server:** Kopieren Sie den Host-Wert aus DocBits
* **Port:** Kopieren Sie den Port-Wert aus DocBits
* **Database:** Kopieren Sie den Datenbanknamen aus DocBits
* **Username:** Kopieren Sie den Benutzernamen aus DocBits
* **Password:** Kopieren Sie das Passwort aus DocBits
* **SSL Mode:** Setzen Sie den Wert auf **Require** (stellt eine verschlüsselte Kommunikation sicher)

#### 3. Schreibgeschützte Datenbank mit Power BI verbinden

* Öffnen Sie **Power BI Desktop**.
*   Wählen Sie **Daten abrufen** → **ODBC** → **Verbinden**.

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI: Daten abrufen über ODBC"><figcaption></figcaption></figure>
* Wählen Sie in der DSN-Liste Ihre konfigurierte Datenquelle aus (z. B. `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt=""><figcaption></figcaption></figure>

* Klicken Sie auf **OK**. Geben Sie die Zugangsdaten erneut ein, wenn Sie dazu aufgefordert werden.
  * Prüfen Sie bei `password authentication failed for user` Host, Datenbank, Benutzername und Passwort. Geben Sie im Anmeldedialog das tatsächliche Passwort ein. Die Maskierung mit geschweiften Klammern in einem ODBC-Verbindungsstring ist Treibersyntax und keine allgemeine Lösung für fehlgeschlagene Anmeldungen.

#### 4. Daten laden und transformieren

* Erweitern Sie im Bereich **Navigator** die Schemaliste.
* Öffnen Sie das Schema **`public`**.
* Wählen Sie die Tabellen aus, die Sie importieren möchten.

![](../../.gitbook/assets/connect_read_only_1.png)

![](../../.gitbook/assets/connect_read_only_2.png)

* Wählen Sie:
  * **Laden** → Direkter Import in Power BI
  * **Daten transformieren** → Öffnet Power Query zum Aufbereiten und Filtern vor dem Laden

#### 5. Daten visualisieren

* Erstellen Sie Dashboards auf der Berichtsfläche von Power BI.
* Ziehen Sie Felder, fügen Sie Datenschnitte hinzu, wählen Sie Diagrammtypen aus und wenden Sie DAX-Berechnungen an.
* Bereinigen oder verknüpfen Sie Daten mit dem **Power Query-Editor**, bevor Sie Visualisierungen erstellen.
* Referenz: [Power BI-Dokumentation](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Geplante Aktualisierung aktivieren (optional)

Die geplante Aktualisierung hängt von Lizenz bzw. Kapazität des Arbeitsbereichs, Connector und Verbindungsmodus ab. Konfigurieren Sie für diese ODBC-Verbindung ein erreichbares Gateway mit passendem Treiber, DSN und Zugangsdaten. Prüfen Sie die aktuellen Voraussetzungen in der offiziellen Dokumentation.

* So halten Sie Ihre Berichte mit PostgreSQL synchron:
* Veröffentlichen Sie Ihre `.pbix`-Datei im **Power BI-Dienst**.
* Installieren Sie das **Power BI Gateway** (Standardmodus) auf einem Rechner mit Netzwerkzugriff auf PostgreSQL.
* Im Power BI-Dienst:
  * Gehen Sie zu Ihrem Dataset → **Einstellungen** → **Geplante Aktualisierung**
  * Ordnen Sie Ihren DSN zu und geben Sie die Zugangsdaten an
* Weitere Informationen finden Sie [hier](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Beispiel-Dashboards und Datenansichten&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Power-BI-Dashboard, Beispiel 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Power-BI-Dashboard, Beispiel 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Power-BI-Dashboard, Beispiel 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Power-BI-Dashboard, Beispiel 4"><figcaption></figcaption></figure></div>

[Offizielle Dokumentation — ODBC](https://learn.microsoft.com/en-us/power-query/connectors/odbc)

[Offizielle Dokumentation — psqlODBC](https://odbc.postgresql.org/docs/config-opt.html)

[Offizielle Dokumentation — Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
