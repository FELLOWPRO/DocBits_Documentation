# Führen Sie die DocOperator-Eingabeaufforderung (Automatisierungsskript) aus.

***

Fügen Sie diese Karte zur Gruppe **Then** des Workflow Builder hinzu – den Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow-Builder"><figcaption><p>Karten werden über <strong>Add Card</strong> zur <strong>Then</strong>-Gruppe hinzugefügt.</p></figcaption></figure>

***

## 📌 Versionsinformationen

**Aktuelle Version:** v3 (Neueste und empfohlene) **Status:** ✅ Aktiv

**Versionsverlauf:**

* v2 → Ursprüngliche DocOperator-Implementierung
* **v3 → CURRENT** (Ausführungskontrollparameter hinzugefügt)
* v4 → Veraltet (Funktionen zurückgesetzt)

**Was sich geändert hat:** v3 hat den optionalen Parameter „Eingabeaufforderung ausführen“ für mehr Kontrolle hinzugefügt. Version 4 hat versucht, dies rückgängig zu machen, war jedoch veraltet.

📖 [Versionsverlauf und Änderungen](../../release.md) | [Vollständige Kartendatenbank](../../cards-overview/export-cards-guide.md)

***

## Zweck

Diese Karte führt mithilfe von DocOperator eine automatisierte Browseraktion oder ein Skript aus. Stellen Sie es sich als einen Roboter vor, der genau wie ein Mensch mit Websites oder Systemen interagieren kann – indem er auf Schaltflächen klickt, Formulare ausfüllt, Daten extrahiert usw.

**Beispiel aus der Praxis:** Ihr Unternehmen nutzt ein webbasiertes Einkaufssystem. Mit dieser Karte können Sie sich automatisch anmelden, nach einem Produkt suchen, die Verfügbarkeit prüfen und den aktuellen Preis abrufen – und das alles, ohne dass jemand dies manuell tun muss.

***

## Wann sollte diese Karte verwendet werden?

Verwenden Sie diese Karte, wenn Sie Folgendes benötigen:

* Automatisieren Sie Aufgaben auf Websites, die keine APIs haben
* Extrahieren Sie Daten aus Webseiten
* Füllen Sie Formulare automatisch aus
* Melden Sie sich bei Systemen an und rufen Sie Informationen ab
* Automatisieren Sie sich wiederholende manuelle Aufgaben
* Interagieren Sie mit nicht integrierten Legacy-Systemen

**Häufige Szenarien:**

* Melden Sie sich bei Lieferanten-Websites an und erhalten Sie Echtzeit-Bestände
* Füllen Sie Formulare automatisch auf externen Systemen aus
* Extrahieren Sie Daten von Webseiten, die keine APIs anbieten
* Überprüfen Sie den Lieferstatus auf Kurier-Websites
* Erhalten Sie Preise von Systemen ohne API-Zugriff

***

## Wie es funktioniert

1. **Karte ausgelöst**: Der Workflow erreicht diese Karte und die Bedingungen sind erfüllt
2. **Skript startet**: Der DocOperator-Bot beginnt mit der Ausführung Ihres Automatisierungsskripts
3. **Bot-Aktionen**: Der Bot führt Aktionen wie Klicken, Tippen, Scrollen und Extrahieren aus
4. **Datenextraktion**: Bot sammelt Informationen von Webseiten
5. **Daten zurückgeben**: Die Daten werden zur Verwendung in den nächsten Karten an DocFlow zurückgegeben
6. **Timeout-Behandlung**: Wenn das Skript zu lange dauert, stoppt es und gibt das zurück, was es hat

***

## Parameter erklärt

### DocOperator-Eingabeaufforderung/Skript

Das Automatisierungsskript, das DocOperator genau sagt, was zu tun ist

**Beispiel (Einfaches Englisch):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variablen

Daten, die Sie an das Skript übergeben möchten

**Beispiel:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Diese Variablen können im Skript wie folgt verwendet werden:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximale Schritte

Wie viele Aktionen der Bot ausführen darf

**Typische Werte:**

* Einfache Aufgabe (z. B. einen Preis ermitteln): 10–20 Schritte
* Mittlere Komplexität (Formular ausfüllen + extrahieren): 20–50 Schritte
* Komplexer Arbeitsablauf (Anmelden + Suchen + Validieren): 50–100 Schritte

**Warum es wichtig ist:** Verhindert Endlosschleifen und sehr lange laufende Skripte

### Maximale Wiederholungsversuche

Wie oft sollte der Bot es noch einmal versuchen, wenn eine Aktion fehlschlägt?

**Beispiele:**

* 1: Versuchen Sie es einmal, wenn es fehlschlägt, fahren Sie fort
* 3: Versuchen Sie es dreimal, bevor Sie aufgeben
* 5: Sehr hartnäckig – versuchen Sie es fünfmal

***

## Schritt-für-Schritt-Beispiel

### Szenario: Lieferantenpreise von der Website abrufen

**Skriptdefinition:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variablen übergeben:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Skript mit Variablen:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Erwartetes Ergebnis:**

```
price: 45.50
quantity_available: 500
```

***

## Arten von Aktionen, die DocOperator ausführen kann

### Navigation

* Gehen Sie zur URL
* Klicken Sie auf Links
* Tasten drücken
* Seite scrollen

### Ausfüllen von Formularen

* Geben Sie Text in Felder ein
* Wählen Sie Dropdown-Optionen aus
* Aktivieren/deaktivieren Sie die Kontrollkästchen
* Klicken Sie auf die Schaltflächen

### Datenextraktion

* Lesen Sie den Text von der Seite
* Zahlen extrahieren
* Tabellendaten abrufen
* Informationen kopieren

### Warten

* Warten Sie, bis die Seite geladen ist
* Warten Sie, bis Elemente angezeigt werden
* Warten Sie auf dynamische Inhalte

### Bedingte Logik

* Wenn etwas existiert, tun Sie dies
* Wenn der Text übereinstimmt, dann...
* Zählen Sie die Ergebnisse und handeln Sie entsprechend

***

## Häufige Anwendungsfälle

### 1. Erhalten Sie Preise in Echtzeit

**Szenario:** Lieferant hat keine API, aber die Website zeigt Preise an

**Skript:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Überprüfen Sie die Lagerverfügbarkeit

**Szenario:** Sie müssen wissen, ob der Lieferant Lagerbestände hat

**Skript:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatische Formularübermittlung

**Szenario:** Sie müssen ein Formular auf einer externen Website ausfüllen

**Skript:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Überprüfung der Dateneingabe

**Szenario:** Überprüfen Sie die Datenübereinstimmung auf zwei verschiedenen Systemen

**Skript:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Konfigurationsschritte

### Schritt 1: Erstellen Sie das Skript

1. Definieren Sie, was Sie erreichen möchten
2. Teilen Sie es in kleine Schritte auf
3. Schreiben Sie jeden Schritt klar auf
4. Zuerst manuell testen (Website öffnen, selbst durchführen)
5. Dokumentieren Sie genau, was Sie anklicken, wo Sie tippen und was Sie extrahieren

### Schritt 2: Variablen identifizieren

1. Welche Daten ändern sich zwischen den Dokumenten?
2. Was soll an das Skript übergeben werden?
3. Variablennamen definieren
4. Geben Sie an, wo Variablen im Skript verwendet werden

### Schritt 3: Parameter festlegen

* **Maximale Schritte**: Basierend auf der Komplexität des Skripts
* **Maximale Wiederholungsversuche**: Wie persistent sollte der Bot sein?
* **Auszeit**: Wie lange soll auf Seiten gewartet werden?

### Schritt 4: Testen

1. Testen Sie mit Beispieldaten
2. Stellen Sie sicher, dass der Bot auf die Website zugreifen kann
3. Überprüfen Sie, ob die Extraktion korrekt ist
4. Überprüfen Sie, ob die Variablen ordnungsgemäß funktionieren

***

## Tipps zum Schreiben von Drehbüchern

### Klare Sprache

✅ **Do:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Nicht:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Spezifische Selektoren

✅ **Do:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Nicht:**

```
Click somewhere
Type in a field
```

### Fehlerbehandlung

✅ **Do:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Nicht:**

```
Click "Next" (assumes it's always there)
```

***

## Fehlerbehebung

### „Zeitüberschreitung des Skripts“

**Ursache:** Die Fertigstellung des Skripts hat zu lange gedauert

**Lösungen:**

* [ ] Reduzieren Sie die Anzahl der Aktionen
* [ ] Erhöhen Sie den Wert „Maximale Schritte“.
* [ ] Optimieren Sie das Skript für eine schnellere Ausführung
* [ ] Vereinfachen Sie, was Sie extrahieren möchten

### „Element nicht gefunden“

**Ursache:** DocOperator konnte die von Ihnen angegebene Schaltfläche/das von Ihnen angegebene Feld nicht finden

**Lösungen:**

* [ ] Überprüfen Sie, ob der Schaltflächen-/Feldname genau korrekt ist
* [ ] Überprüfen Sie, ob sich das Website-Layout geändert hat
* [ ] Wartezeit vor dem Klicken hinzufügen
* [ ] Überprüfen Sie, ob die Schaltfläche nur unter bestimmten Bedingungen angezeigt wird

### „Anmeldung fehlgeschlagen“

**Ursache:** Authentifizierung fehlgeschlagen

**Lösungen:**

* [ ] Überprüfen Sie, ob Benutzername und Passwort korrekt sind
* [ ] Überprüfen Sie, ob das Passwort Sonderzeichen enthält
* [ ] Stellen Sie sicher, dass das Konto nicht gesperrt ist
* [ ] Überprüfen Sie, ob sich der Anmeldevorgang geändert hat

### „Daten nicht korrekt extrahiert“

**Ursache:** Das Skript wurde ausgeführt, extrahierte jedoch falsche Informationen

**Lösungen:**

* [ ] Überprüfen Sie, ob das richtige Feld ausgewählt wurde
* [ ] Überprüfen Sie, ob sich die Daten am erwarteten Speicherort befinden
* [ ] Extraktionslogik manuell testen
* [ ] Debugging-Schritte hinzufügen, um zu überprüfen, was auf der Seite steht

### „Skript läuft langsam“

**Ursache:** Zu viele Schritte oder langsame Website

**Lösungen:**

* [ ] Entfernen Sie unnötige Schritte
* [ ] Wartezeiten optimieren
* [ ] Internetverbindung prüfen
* [ ] Überlegen Sie, ob eine API-Alternative existiert

***

## Best Practices

✅ **Do:**

* Testen Sie Skripte gründlich, bevor Sie sie bereitstellen
* Halten Sie Skripte einfach und fokussiert
* Fügen Sie Kommentare hinzu, die jeden Schritt erläutern
* Verwenden Sie aussagekräftige Variablennamen
* Überwachen Sie die Skriptleistung
* Haben Sie eine Ausweichlösung für den Fall, dass Skripte fehlschlagen

❌ **Nicht:**

* Erstellen Sie extrem lange Skripte (>100 Schritte)
* Speichern Sie vertrauliche Passwörter in Protokollen
* Verlassen Sie sich auf genaue Koordinaten (Websites ändern sich)
* Erstellen Sie Schleifen ohne Beendigungsbedingungen
* Fehlermeldungen ignorieren

***

## Leistungstipps

* **Unbenutzte Schritte entfernen** – Jeder Schritt braucht Zeit
* **Ähnliche Aktionen kombinieren** – Gruppieren Sie verwandte Klicks
* **Wartezeiten optimieren** – Verwenden Sie nur notwendige Verzögerungen
* **Cache-Daten** – Extrahieren Sie dieselben Daten nicht zweimal
* **Parallele Verarbeitung** – Führen Sie nach Möglichkeit mehrere Skripte aus

***

## Sicherheitsüberlegungen

⚠️ **Wichtig:**

* Speichern Sie keine Passwörter in DocFlow
* Verwenden Sie sichere Methoden zur Weitergabe von Anmeldeinformationen
* Protokollieren Sie keine sensiblen Daten
* Überwachen Sie, was extrahiert wird
* Stellen Sie sicher, dass die Bot-Aktivität protokolliert und überprüfbar ist

***

## Beispiel für Variablen

### Verfügbare Variablen, die Sie verwenden können:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Skript mit Variablen:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Vergleich: Wann sollte DocOperator vs. API verwendet werden?

| Situation              | Verwenden Sie DocOperator | API verwenden     |
| ---------------------- | --------------- | ----------- |
| Die Website verfügt über eine API        | ❌ Nein            | ✅ Ja       |
| Die Website ist interaktiv | ✅ Ja           | ❌ Nein        |
| Erfordert eine Anmeldung         | ✅ Ja           | Hängt davon ab     |
| Sehr schnell benötigt       | ❌ Nein            | ✅ Ja       |
| Komplexer Arbeitsablauf       | ✅ Ja           | ❌Vielleicht nicht |
| Daten ändern sich täglich     | ✅ Ja           | ✅ Ja       |

***

## Verwandte Karten

* **CALL\_API** – Verwenden Sie stattdessen, wenn API verfügbar ist
* **ACTION\_HTTPS\_REQUEST** – Einfachere Anfragen
* **ACTION\_SET\_FIELD\_TO\_TEXT** – Extrahierte Daten verwenden
* **CONDITION\_HTTPS\_REQUEST\_STATUS** – Anfragestatus prüfen
