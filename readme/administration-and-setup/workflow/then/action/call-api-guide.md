# Externe API aufrufen

***

Fügen Sie diese Karte zur Gruppe **Dann** des Workflow Builder hinzu – den Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-de.png" alt="Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus."><figcaption><p>Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus.</p></figcaption></figure>

***

## 📌 Versionsinformationen

**Aktuelle Version:** v2 (Neueste und empfohlene) **Status:** ✅ Aktiv

**Versionsverlauf:**

* v1 → Einfacher API-Aufruf (nicht mehr empfohlen)
* **v2 → AKTUELL** (mehrsprachige Unterstützung hinzugefügt)

**Was sich geändert hat:** v2 hat Internationalisierungsunterstützung (i18n) mit Übersetzungsschlüsseln hinzugefügt. Die Funktionalität bleibt identisch.

📖 [Versionsverlauf und Änderungen](../../release.md) | [Vollständige Kartendatenbank](../../cards-overview/export-cards-guide.md)

***

## Zweck

Mit dieser Karte können Sie Daten an eine externe Website oder einen externen Dienst senden und Informationen zurückerhalten. Stellen Sie sich das so vor, als würden Sie eine Frage an einen externen Dienst senden und eine Antwort erhalten, die Sie in Ihrem Workflow verwenden können.

**Beispiel aus der Praxis:** Ihr Unternehmen verwendet ein Preissystem auf einer anderen Website. Diese Karte kann das Preissystem automatisch nach dem aktuellen Preis eines Artikels fragen und diesen Preis in Ihr Dokument übernehmen.

***

## Wann sollte diese Karte verwendet werden?

Verwenden Sie diese Karte, wenn Sie Folgendes benötigen:

* Erhalten Sie Informationen von einem externen Dienst (z. B. Preis-, Validierungs- oder Suchdaten).
* Dokumentinformationen zur Verarbeitung an ein anderes System senden
* Integrieren Sie Dienste von Drittanbietern
* Daten automatisch abrufen, ohne manuelle Suche
* Verbinden Sie mehrere Geschäftssysteme miteinander

**Häufige Szenarien:**

* Suchen Sie in einer Datenbank nach Lieferanteninformationen
* Erhalten Sie Echtzeitpreise von einem Preisservice
* Validieren Sie Daten anhand eines externen Systems
* Holen Sie sich Versandinformationen von einem Logistikdienstleister

***

## Wie es funktioniert

1. **Bedingungsprüfung**: Der Workflow prüft zunächst, ob die Bedingungen in den Abschnitten „Wenn“ und „Und“ erfüllt sind
2. **Daten vorbereiten**: Die Karte sammelt die von Ihnen konfigurierten Parameter
3. **Anfrage senden**: Es sendet Ihre Daten an die externe API/den externen Dienst
4. **Receive Response**: Der externe Dienst antwortet mit Daten
5. **Weiter**: Der Workflow verwendet diese Daten in nachfolgenden Karten

***

## Parameter erklärt

### API-Endpunkt-URL

**Was es ist:** Die Adresse des externen Dienstes, mit dem Sie kommunizieren möchten

**Beispiel:** `https://api.supplier-system.com/product/pricing`

**So finden Sie es:** Fragen Sie Ihr IT-Team oder den Dienstanbieter nach seinem API-Endpunkt

***

### HTTP-Methode

**Was es ist:** Der Typ der zu sendenden Anfrage

**Optionen:**

* **GET**: Informationen anfordern (z. B. eine Frage stellen)
* **POST**: Neue Daten senden
* **PUT**: Vorhandene Daten aktualisieren
* **DELETE**: Daten entfernen

**Am häufigsten:** GET (zum Abrufen von Informationen)

***

### Überschriften

**Was es ist:** Zusätzliche Anweisungen für den Dienst, den Sie anrufen

**Beispiel:**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Warum es benötigt wird:** Dienste erfordern häufig eine Authentifizierung oder bestimmte Formatanweisungen

***

### Parameter (Abfrageparameter)

**Was es ist:** Zusätzliche Informationen, die in der URL übergeben werden

**Beispiel:**

```
?supplier_id=12345&currency=USD
```

**Echtes Beispiel:** Wenn Sie nach Preisen fragen, können die Parameter die Lieferanten-ID und die Währung umfassen

***

### Anforderungsdaten (Körper)

**Was es ist:** Die Informationen, die Sie an den Dienst senden

**Beispiel:**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Bei Verwendung:** Bei Verwendung der POST- oder PUT-Methoden

***

## Schritt-für-Schritt-Beispiel

### Szenario: Erhalten Sie Lieferantenpreise in Echtzeit

**Einrichtung:**

1. **Kartentyp:** API aufrufen
2. **API-Endpunkt:** `https://api.suppliers.com/v1/prices`
3. **Methode:** POST
4. **Überschriften:** `Authorization: Bearer YOUR-API-KEY`
5.  **Daten anfordern:**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**Was passiert:**

1. Das Dokument kommt mit der Produkt-ID: ABC123, Menge: 100 an
2. Die Karte sendet eine Anfrage an die API des Lieferanten
3. Die API des Lieferanten antwortet mit: `{"unit_price": 25.50, "total_price": 2550}`
4. Der Workflow wird mit diesen Preisinformationen fortgesetzt
5. Next Card kann diese Daten verwenden, um den Rechnungspreis zu validieren

***

## Konfigurationsschritte

### 1. Holen Sie sich API-Informationen

Kontaktieren Sie den externen Dienstleister und fordern Sie an:

* [ ] API-Endpunkt-URL
* [ ] Authentifizierungsmethode (API-Schlüssel, Benutzername/Passwort, OAuth)
* [ ] Erforderliche Parameter
* [ ] Erwartetes Antwortformat
* [ ] Ratenlimits oder Kontingente

### 2. Konfigurieren Sie die Karte

1. Geben Sie die API-Endpunkt-URL ein
2. Wählen Sie die HTTP-Methode (normalerweise GET oder POST)
3. Fügen Sie bei Bedarf Authentifizierungsheader hinzu
4. Fügen Sie alle erforderlichen Parameter hinzu
5. Formatieren Sie Anforderungsdaten bei Bedarf als JSON

### 3. Testen Sie die Karte

1. Verwenden Sie ein Testdokument
2. Führen Sie den Workflow aus
3. Überprüfen Sie, ob die Antwort korrekt empfangen wurde
4. Überprüfen Sie, ob das Datenformat den Erwartungen entspricht

***

## Gängige Reaktionsszenarien

### Erfolgreiche Antwort (Statuscode 200)

```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```

✅ Die Daten stehen für die nächste Kartenverwendung zur Verfügung

### Fehlerreaktion (Statuscode 404)

```json
{
  "error": "Product not found"
}
```

⚠️ Die API konnte nicht finden, wonach Sie suchen

### Auszeit

Der externe Dienst hat nicht innerhalb des Zeitlimits geantwortet. ⚠️ Überprüfen Sie, ob der Dienst verfügbar ist oder ob die Endpunkt-URL korrekt ist

***

## Beispiel-Workflows

### Beispiel 1: Automatische Preisvalidierung

**Szenario:** Rechnungspreise anhand der aktuellen Preise des Lieferanten validieren

**Durchfluss:**

1. Beleg kommt mit Rechnungsposten an (Produkt: A123, Preis: 50 €)
2. **API-Karte aufrufen** → Fragt Lieferanten-API: „Wie hoch ist der aktuelle Preis für A123?“
3. Lieferant antwortet: „48 €“
4. **Konditionskarte** → Prüft, ob der Rechnungspreis (50 €) innerhalb von 5 % des aktuellen Preises (48 €) liegt.
5. **Genehmigungskarte** → Genehmigt, wenn innerhalb der Toleranz

### Beispiel 2: Automatische Lieferantensuche

**Szenario:** Erhalten Sie Lieferantenstammdaten aus der zentralen Datenbank

**Durchfluss:**

1. Die Rechnung kommt mit dem Lieferantencode SUPP-789 an
2. **API-Karte aufrufen** → Fragt das System: „Gib mir Details zum Lieferanten SUPP-789“
3. Das System antwortet mit: Name, Kontakt, Bedingungen usw.
4. **Feldkarten festlegen** → Dokumentfelder mit diesen Daten füllen
5. **Karte exportieren** → Export mit vollständigen Informationen

### Beispiel 3: Versandkosten in Echtzeit

**Szenario:** Erhalten Sie automatische Versandkosten basierend auf dem Zielort

**Durchfluss:**

1. Das Dokument hat eine Lieferadresse
2. **API-Karte aufrufen** → Versandanbieter fragen: „Wie hoch sind die Kosten nach \[Adresse]?“
3. Der Anbieter antwortet mit den Versandkosten
4. **Karte berechnen** → Versandkosten zum Gesamtrechnungsbetrag hinzufügen
5. **Karte exportieren** → Mit aktualisiertem Gesamtbetrag senden

***

## Fehlerbehebung

### Fehler „Verbindungszeitüberschreitung“.

**Ursache:** Der API-Dienst antwortet nicht

**Lösungen:**

* [ ] Überprüfen Sie, ob der Dienst verfügbar ist (besuchen Sie die Website)
* [ ] Überprüfen Sie, ob die Endpunkt-URL korrekt ist (keine Tippfehler).
* [ ] Internetverbindung prüfen
* [ ] Wenden Sie sich an den Dienstanbieter
* [ ] Überprüfen Sie, ob der Dienst Ratenbeschränkungen hat (Sie senden zu viele Anfragen)

### Fehler „Unautorisiert“ oder „403 Verboten“.

**Ursache:** Authentifizierung fehlgeschlagen

**Lösungen:**

* [ ] Überprüfen Sie, ob Ihr API-Schlüssel korrekt ist
* [ ] Überprüfen Sie, ob Ihr API-Schlüssel abgelaufen ist
* [ ] Stellen Sie sicher, dass der Authentifizierungsheader korrekt formatiert ist
* [ ] Stellen Sie sicher, dass Sie über Berechtigungen für diesen Endpunkt verfügen

### „Ungültige Anfrage“ oder „400-Fehler“

**Ursache:** Das Anforderungsdatenformat ist falsch

**Lösungen:**

* [ ] Überprüfen Sie die JSON-Syntax (fehlende Kommas, Anführungszeichen usw.)
* [ ] Überprüfen Sie, ob alle erforderlichen Felder enthalten sind
* [ ] Überprüfen Sie, ob die Parameternamen mit den Erwartungen des Dienstes übereinstimmen
* [ ] Konsultieren Sie die API-Dokumentation

### „Antwort funktioniert nicht wie erwartet“

**Lösungen:**

* [ ] Testen Sie die API mit einem Tool wie Postman
* [ ] Vergleichen Sie das tatsächliche Antwortformat mit dem erwarteten Format
* [ ] Überprüfen Sie, ob sich die Dokumentation der API geändert hat
* [ ] Überprüfen Sie, ob die von Ihnen gesendeten Daten korrekt sind

***

## Verwendung von Antwortdaten

Sobald Sie Daten von der API zurückerhalten, können die nächsten Karten diese verwenden:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

***

## Sicherheitshinweise

⚠️ **Wichtig:** Geben Sie niemals vertrauliche Informationen in die Kartenkonfiguration ein, die für andere Benutzer sichtbar sein könnten

* Codieren Sie Passwörter nicht fest
* Verwenden Sie API-Schlüssel sicher
* Fügen Sie keine personenbezogenen Daten in Protokolle ein
* Verwenden Sie HTTPS-Endpunkte (nicht HTTP)

***

## Tipps und Best Practices

✅ **Do:**

* Testen Sie zunächst mit einer kleinen Auswahl von Dokumenten
* Halten Sie API-Aufrufe einfach und fokussiert
* Fügen Sie Fehlerbehandlung mit Bedingungskarten hinzu
* Überwachen Sie die API-Nutzung/-Kosten
* Dokumentieren Sie die API-Anforderungen für Ihr Team

❌ **Nicht:**

* Rufen Sie APIs für jede einzelne Anfrage auf, wenn Sie Daten zwischenspeichern können
* Antwortfehlercodes ignorieren
* Verwenden Sie Test-APIs in der Produktion
* Vergessen Sie, Authentifizierungsheader hinzuzufügen
* Gehen Sie davon aus, dass die API immer verfügbar ist

***

## Verwandte Karten

* **ACTION\_HTTPS\_REQUEST** – Ähnliche, aber einfachere HTTPS-Anfragen
* **CONDITION\_HTTPS\_REQUEST\_STATUS** – Überprüfen Sie, ob der API-Aufruf erfolgreich war
* **ACTION\_SEND\_EMAIL** – Daten per E-Mail statt über API senden
* **CALL\_API** (andere Version) – Alternative API-Aufrufmethode

***

## Brauchen Sie Hilfe?

* Bitten Sie Ihr IT-/Integrationsteam um eine API-Dokumentation
* Verwenden Sie das Postman-Tool, um zunächst API-Endpunkte zu testen
* Überprüfen Sie das Support-Portal des Dienstanbieters
* Sehen Sie sich die API-Dokumentation für erforderliche Formate an
