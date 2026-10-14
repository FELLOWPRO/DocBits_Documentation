# SQL-Zugriff

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Einstellungen für den direkten SQL-Zugriff"><figcaption></figcaption></figure>

## Überblick

Im Einstellungsmodul von DocBits können Administratoren per SQL direkt auf die BI-Datenbank zugreifen. Diese Funktion ist für fortgeschrittenes Datenmanagement und individuelle Berichtsanforderungen vorgesehen.

### Auf den direkten SQL-Zugriff zugreifen

Navigieren Sie im Einstellungsmodul zum Bereich „SQL Direct Access“. Dort finden Sie die Zugangsdaten und Zugriffsdetails, darunter Benutzername, Passwort, Datenbankname und Host-Informationen.

* **Benutzername:** user\_23f3d6
* **Passwort:** _Verschlüsselt_
* **Datenbank:** demo
* **Host:** siehe Screenshot

## **Beispiel für Zugriffsdetails:**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Ergebnisse einer Beispielabfrage

Die folgenden Ergebnisse zeigen die Anzahl der Dokumente nach Status und Rechnungstyp:

* **Ready for Validation:** 71 Rechnungen, 6 nicht spezifiziert
* **Pending Confirmation:** 1 nicht spezifiziert
* **Finished:** 3 nicht spezifiziert, 1 Rechnung
* **Error:** 2 nicht spezifiziert

#### clickhouse-client für den Terminalzugriff verwenden

Entwickler, die lieber das Terminal verwenden, können den Zugriff über `clickhouse-client` herstellen:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Materialisierte Ansichten erstellen

Wir empfehlen, materialisierte Ansichten zu erstellen, um Daten vorab zu berechnen und die Leistung in Analysetools wie PowerBI zu verbessern:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Dieses Beispiel zeigt, wie Gesamtbeträge nach der Woche ihrer Erstellung gruppiert werden. Das ist hilfreich für wöchentliche Finanzübersichten oder Prüfpfade.

## Weitere Ressourcen

Für weitere Unterstützung oder erweiterte Konfigurationen wenden Sie sich bitte an unser Support-Team oder nutzen Sie unsere umfassenden Videoschulungen im Hilfebereich.
