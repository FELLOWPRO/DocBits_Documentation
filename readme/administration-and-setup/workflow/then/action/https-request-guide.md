# HTTPS-Anfrage senden

***

Fügen Sie diese Karte zur Gruppe **Dann** des Workflow Builder hinzu – den Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-de.png" alt="Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus."><figcaption><p>Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus.</p></figcaption></figure>

***

## 📌 Versionsinformationen

**Aktuelle Version:** v2 (Neueste und empfohlene) **Status:** ✅ Aktiv

**Versionsverlauf:**

* v1 → Einfache HTTP-Anfrage (nicht mehr empfohlen)
* **v2 → AKTUELL** (mehrsprachige Unterstützung hinzugefügt)

**Was sich geändert hat:** v2 hat Unterstützung für die Internationalisierung (i18n) hinzugefügt. Die Kernfunktionalität von Webhooks/Anfragen bleibt unverändert.

📖 [Versionsverlauf und Änderungen](../../release.md) | [Vollständige Kartendatenbank](../../cards-overview/export-cards-guide.md)

***

## Zweck

Die HTTPS-Anfragekarte verwendet eine konfigurierte HTTPS-URL und eigene Header. `call_api` verwendet einen relativen DocBits-API-Pfad und den aktuellen DocBits-Benutzerkontext; das Ergebnis wird aus dem Antworttext abgeleitet. Entscheidend sind Endpunkt und Antwortvertrag, nicht die Unterscheidung zwischen einfacher und komplexer API.

## Wann sollte diese Karte verwendet werden?

Verwenden Sie diese Karte, wenn Sie Folgendes benötigen:

* Senden Sie Webhook-Benachrichtigungen an externe Dienste
* Aktionen in anderen Systemen auslösen
* Fragen Sie einen einfachen Webdienst ab
* Senden Sie Statusaktualisierungen an andere Anwendungen
* Führen Sie einfache Integrationen ohne komplexe API-Anforderungen durch

***

## Wie es funktioniert

1. **Trigger-Prüfung**: Das System prüft, ob die Bedingungen „Wenn“ und „Und“ erfüllt sind
2. **Build-Anfrage**: Das System bereitet die HTTPS-Anfrage mit Ihren Parametern vor
3. **Sicher senden**: Daten werden über eine sichere HTTPS-Verbindung gesendet
4. **Receive Response**: Externer Dienst antwortet
5. **Weiter**: Der Workflow wird mit den Antwortdaten fortgesetzt

***

## Parameter

### URL

Die Website-Adresse, an die die Anfrage gesendet werden soll

**Beispiel:** `https://webhook.company.com/process`

### Überschriften

Besondere Hinweise für den Empfänger

**Beispiel:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Methode

* **GET**: Informationen anfordern
* **POST**: Daten senden
* **PUT**: Daten aktualisieren

### Parameter (Abfragezeichenfolge)

Zur URL hinzugefügte Daten

**Beispiel:** `?action=approve&user_id=123`

### Daten anfordern

Die tatsächlich gesendeten Informationen (im JSON-Format)

**Beispiel:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Schritt-für-Schritt-Beispiel

### Szenario: Rechnung an das Buchhaltungssystem senden

**Kartenkonfiguration:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Methode:** POST
* **Überschriften:** `Authorization: Bearer YOUR-TOKEN`
* **Daten anfordern:**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Erwartete Antwort:**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## Häufige Anwendungsfälle

### 1. Webhook-Benachrichtigungen

Senden Sie Echtzeitbenachrichtigungen an andere Systeme, wenn in DocFlow etwas passiert

**Beispiel:**

* Dokument genehmigt → Benachrichtigung an das Fulfillment-System senden
* Lieferant geändert → Einkaufsteam über Slack/Teams-Webhook benachrichtigen

### 2. Externe Systemintegration

Verbinden Sie DocFlow mit anderen Geschäftssystemen für den automatischen Datenaustausch

**Beispiel:**

* Nachdem das Dokument verarbeitet wurde → Mit ERP-System synchronisieren
* Neuer Lieferant hinzugefügt → Lieferantendatensatz im Stammdatensystem erstellen

### 3. Genehmigungsworkflows

Dokument an externes Genehmigungssystem senden und Entscheidung erhalten

**Beispiel:**

* Rechnung mit hohem Betrag → Zur Genehmigung an die Finanzabteilung senden
* Dokument mit Entscheidung an externes System zurücksenden

***

## Konfigurationshandbuch

### Schritt 1: Endpunktinformationen abrufen

Bitten Sie das Empfangssystem um Folgendes:

* [ ] HTTPS-URL
* [ ] Erforderliche Header
* [ ] Authentifizierungsmethode
* [ ] Erwartetes Anforderungsformat
* [ ] Erwartetes Antwortformat

### Schritt 2: Konfigurieren Sie die Karte

1. Geben Sie die HTTPS-URL ein
2. HTTP-Methode festlegen (normalerweise POST)
3. Fügen Sie bei Bedarf eine Authentifizierung hinzu
4. Formatieren Sie Anforderungsdaten als JSON
5. Fügen Sie alle benutzerdefinierten Header hinzu

### Schritt 3: Testen

Senden Sie eine Testanfrage und überprüfen Sie die Antwort

***

## Antworthandhabung

Ihre HTTPS-Anfrage wird beantwortet. Häufige Antworten:

### Erfolg (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Ungültige Anfrage (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Nicht autorisiert (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Serverfehler (500)

Das Empfangssystem hat ein internes Problem

***

## Fehlerbehebung

### „Zertifikatfehler“

**Ursache:** Problem mit dem HTTPS-Sicherheitszertifikat

**Lösung:**

* Überprüfen Sie, ob die URL korrekt ist
* Überprüfen Sie, ob das Zertifikat der Website gültig ist
* Stellen Sie sicher, dass Sie HTTPS (nicht HTTP) verwenden.

### „Verbindung abgelehnt“

**Ursache:** Es kann keine Verbindung zum Server hergestellt werden

**Lösung:**

* Überprüfen Sie, ob die URL/IP-Adresse korrekt ist
* Überprüfen Sie, ob der Dienst ausgeführt wird
* Überprüfen Sie die Firewall-Regeln
* Überprüfen Sie die Internetverbindung

### „Keine Antwort/Timeout“

**Ursache:** Server antwortet nicht innerhalb des Zeitlimits

**Lösung:**

* Prüfen Sie, ob der Dienst verfügbar ist
* Überprüfen Sie die Endpunkt-URL
* Prüfen Sie, ob es Tarifbegrenzungen gibt
* Wenden Sie sich an den Systemadministrator

### „Ungültiger JSON“

**Ursache:** Die Anforderungsdaten sind fehlerhaft

**Lösung:**

* Suchen Sie nach fehlenden Kommas in JSON
* Überprüfen Sie, ob alle Zitate korrekt sind
* JSON-Format validieren (Online-JSON-Validator verwenden)
* Suchen Sie nach Sonderzeichen

***

## Beispiele

### Beispiel 1: An Webhook-Dienst senden

```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Beispiel 2: Externes System aktualisieren

```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Beispiel 3: Externen Dienst abfragen

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Unterschied zur „Call API“-Karte

Die HTTPS-Anfragekarte verwendet eine konfigurierte HTTPS-URL und eigene Header. `call_api` verwendet einen relativen DocBits-API-Pfad und den aktuellen DocBits-Benutzerkontext; das Ergebnis wird aus dem Antworttext abgeleitet. Entscheidend sind Endpunkt und Antwortvertrag, nicht die Unterscheidung zwischen einfacher und komplexer API.

***

## Sicherheitsüberlegungen

✅ **Verwenden Sie immer HTTPS** (sichere Verbindung)

⚠️ **Niemals:**

* Geben Sie Passwörter in die URL ein
* API-Schlüssel in Protokollen offenlegen
* Persönliche Daten in Parameter einbeziehen
* Verwenden Sie HTTP für sensible Daten

***

## Best Practices

✅ **Do:**

* Testen Sie zunächst mit kleinen Datenmengen
* Beziehen Sie die Fehlerbehandlung ein
* Protokollieren Sie wichtige Anfragen
* Dokumentieren Sie die Integration
* Auf Fehler überwachen

❌ **Nicht:**

* Rufen Sie denselben Endpunkt wiederholt auf, wenn er nicht benötigt wird
* Antwortfehler ignorieren
* Fügen Sie sensible Daten im Klartext hinzu
* Serviceratengrenzen überschreiten

***

## Verwandte Karten

* **CALL\_API** – Erweiterte API-Integration
* **CONDITION\_HTTPS\_REQUEST\_STATUS** – Überprüfen Sie, ob die Anfrage erfolgreich war
* **ACTION\_SEND\_EMAIL** – Stattdessen per E-Mail senden
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** – Automatisierte Skripte

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Beispiel für eine HTTPS-Aktion

**Konfiguration:** Wählen Sie die Methode `POST`, ersetzen Sie `DEMO_WEBHOOK_URL` durch Ihren autorisierten Testendpunkt, fügen Sie Header `Content-Type: application/json` und Text `{"document_number":"DEMO-001"}` hinzu. Konfigurieren Sie die Authentifizierung nur nach Bedarf für diesen Endpunkt. Kopieren Sie niemals ein echtes Geheimnis in die Dokumentation.

**Erwartetes Ergebnis und Gegenbeispiel:** Die Aktion sendet die konfigurierte Anfrage, wenn ihre Workflow-Route ausgeführt wird. Überprüfen Sie die HTTP-Antwort und den Empfangstestdienst. Eine Zeitüberschreitung ist kein Beweis dafür, dass der Dienst nichts getan hat, und diese Aktion „Dann“ ist von der Karte „Und“ getrennt, die einen HTTP-Status überprüft. Diese illustrative Anfrage wurde nicht gesendet.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.

## Lernweg und Rückschreibvertrag

[P1: API-Aufruf und Weiterverwendung der Antwort prüfen](../../masterclass/api-response-contract.md) erklärt Simulation, Antwortauswertung und den ausdrücklich zu vereinbarenden Rückschreibweg. Eine erfolgreiche Anfrage stellt nicht automatisch ein Feld wie `api.response.cost_center` bereit.
