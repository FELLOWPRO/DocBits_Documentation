# Senden Sie E-Mails an Gruppen

***

Fügen Sie diese Karte zur Gruppe **Dann** des Workflow Builder hinzu – den Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-de.png" alt="Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus."><figcaption><p>Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus.</p></figcaption></figure>

***

## 📌 Versionsinformationen

**Status:** ✅ Einzelversion (keine wichtigen Änderungen) **Neueste Version:** v1 (Aktiv) **Hinweis:** Diese Karte verwendet ein Einzelversionsmodell mit mehrsprachiger Unterstützung über Übersetzungsschlüssel.

📖 [Vollständige Kartendatenbank](../../cards-overview/export-cards-guide.md)

***

## Zweck

Diese Karte sendet automatisch E-Mail-Benachrichtigungen an Benutzergruppen. Anstatt einzelnen Personen Arbeit zuzuweisen, senden Sie die Nachricht an eine Gruppe und alle Mitglieder dieser Gruppe erhalten sie.

**Beispiel aus der Praxis:** Wenn eine Rechnung mit hohem Betrag eintrifft, senden Sie automatisch eine E-Mail-Benachrichtigung an alle Mitglieder der Gruppe „Finanzteam“, damit sie wissen, dass die Rechnung überprüft werden muss.

***

## Wann sollte diese Karte verwendet werden?

Verwenden Sie diese Karte, wenn Sie Folgendes benötigen:

* Benachrichtigen Sie mehrere Personen gleichzeitig
* Senden Sie Benachrichtigungen an Teamgruppen
* Übertragen Sie Aktualisierungen an die Abteilungen
* Benachrichtigen Sie Gruppen über Dokumentstatusänderungen
* Senden Sie Erinnerungen an Gruppenmitglieder

**Häufige Szenarien:**

* Benachrichtigen Sie das Beschaffungsteam über neue Lieferanten
* Benachrichtigen Sie das Finanzteam über Rechnungen mit hohem Rechnungsbetrag
* Benachrichtigen Sie das Lagerteam über Sendungen
* Statusänderungen des Dokuments übertragen

***

## Wie es funktioniert

1. **Bedingungsprüfung**: Der Workflow prüft „Wo“- und „Und“-Bedingungen
2. **E-Mail vorbereiten**: Das System bereitet die E-Mail mithilfe einer Vorlage vor
3. **Gruppenmitglieder abrufen**: Das System findet alle Mitglieder der angegebenen Gruppe
4. **Senden**: E-Mail wird an jedes Gruppenmitglied gesendet
5. **Log**: Der E-Mail-Versand wird aufgezeichnet

***

## Parameter erklärt

### E-Mail-Vorlage

Die zu sendende E-Mail-Nachricht

**Optionen:**

* Wählen Sie aus vorhandenen Vorlagen
* Jede Vorlage verfügt über vordefinierte Betreff-, Text- und Formatierungsvorgaben
* Vorlagen können Platzhalter wie {Dokument\_Nummer}, {Lieferant\_Name} enthalten.

**Beispielvorlage:**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Gruppe

Die Benutzergruppe, an die die E-Mail gesendet werden soll

**Beispielgruppen:**

* Finanzteam
* Beschaffungsteam
* Lagerteam
* Genehmigungsausschuss
* Managementgruppe

***

## Konfigurationsschritte

### Schritt 1: Wählen Sie eine E-Mail-Vorlage

1. Klicken Sie auf „E-Mail-Vorlage auswählen“.
2. Wählen Sie eine Vorlage aus der Liste aus
3. Überprüfen Sie Betreff und Inhalt

### Schritt 2: Wählen Sie Gruppe aus

1. Klicken Sie auf „Gruppe auswählen“
2. Wählen Sie die Gruppe aus, die Sie benachrichtigen möchten
3. Gruppenmitglieder überprüfen (zeigt normalerweise die Anzahl an)

### Schritt 3: Bedingungen festlegen

1. Bedingung hinzufügen: „Wenn \[Bedingung] wahr ist“
2. Beispiel: „Wenn der Rechnungsbetrag größer als 5.000 € ist“

### Schritt 4: Testen

1. Testen Sie mit Beispieldokument
2. Überprüfen Sie den E-Mail-Versand an die Gruppe
3. Überprüfen Sie das Rendern der Vorlage

***

## Beispiele für E-Mail-Vorlagen

### Vorlage 1: Benachrichtigung über Rechnungen mit hohem Wert

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Vorlage 2: Änderung des Lieferantenstatus

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Vorlage 3: Dokument bereit zum Export

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## Häufige Anwendungsfälle

### Anwendungsfall 1: Qualitätskontrollwarnungen

**Auslöser:** Wenn eine Diskrepanz zwischen Rechnung und Bestellung festgestellt wird

**E-Mail-Gruppe:** Qualitätsteam

**Inhalt:**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Anwendungsfall 2: Genehmigungsbenachrichtigungen

**Auslöser:** Wenn das Dokument einen bestimmten Status erreicht

**E-Mail-Gruppe:** Genehmigungsausschuss

**Inhalt:**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Anwendungsfall 3: Ausnahmebenachrichtigungen

**Auslöser:** Wenn Bedingungen nicht erfüllt sind

**E-Mail-Gruppe:** Manager

**Inhalt:**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Anwendungsfall 4: Statusaktualisierungen

**Auslöser:** Wenn sich der Dokumentstatus ändert

**E-Mail-Gruppe:** Team, das für den nächsten Schritt verantwortlich ist

**Inhalt:**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## Fehlerbehebung

### „E-Mail nicht erhalten“

**Mögliche Ursachen:**

* [ ] Benutzer in der Gruppe haben keine E-Mail-Adressen
* [ ] E-Mail durch Spamfilter blockiert
* [ ] Die E-Mail-Adresse in der Gruppe ist falsch
* [ ] Gruppe hat keine Mitglieder

**Lösungen:**

1. Stellen Sie sicher, dass alle Gruppenmitglieder über E-Mail-Adressen verfügen
2. Überprüfen Sie den Spam-/Junk-Ordner
3. Überprüfen Sie, ob die Gruppenmitgliedschaft korrekt ist
4. Fügen Sie Benutzer zur Gruppe hinzu, falls sie fehlen
5. Erkundigen Sie sich bei der IT-Abteilung, ob der E-Mail-Dienst funktioniert

### „Vorlage wird nicht korrekt gerendert“

**Ursache:** Platzhaltervariablen nicht gefunden

**Lösung:**

* [ ] Überprüfen Sie, ob die Feldnamen genau übereinstimmen
* [ ] Überprüfen Sie, ob das Feld im Dokument einen Wert hat
* [ ] Richtiges Platzhalterformat verwenden: {field\_name}
* [ ] Testen Sie mit einem Beispieldokument, das alle Felder enthält

### „Manche Leute bekommen E-Mails, andere nicht“

**Ursache:** Unvollständige Gruppenmitgliedschaft oder ungültige E-Mails

**Lösungen:**

* [ ] Stellen Sie sicher, dass alle Mitglieder über eine gültige E-Mail-Adresse verfügen
* [ ] Überprüfen Sie, ob sich einige Benutzer abgemeldet haben
* [ ] Überprüfen Sie, ob die Gruppenmitgliedschaft aktuell ist
* [ ] Kontaktieren Sie die IT, um E-Mail-Adressen zu validieren

### „Möchten Sie Personen zur Gruppe hinzufügen/entfernen“

**Lösung:**

* Kontaktieren Sie Ihren Administrator
* Gruppen werden in den Systemeinstellungen verwaltet
* Kann von dieser Karte aus nicht geändert werden
* Fordern Sie Änderungen der Gruppenmitgliedschaft in der IT an

***

## Anpassung der E-Mail-Vorlage

### Verfügbare Platzhalter

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Erstellen benutzerdefinierter Platzhalter

Wenn Sie zusätzliche Daten in E-Mails benötigen:

1. Kontaktieren Sie Ihren Administrator
2. Fordern Sie einen neuen Platzhalter an
3. Fügen Sie dem Dokument das erforderliche Feld hinzu
4. E-Mail-Vorlage aktualisieren

***

## Best Practices

✅ **Do:**

* Halten Sie den E-Mail-Inhalt kurz und klar
* Fügen Sie Aktionspunkte hinzu (was sollen Empfänger tun?)
* Fügen Sie einen Link oder Anweisungen zum Zugriff auf das Dokument hinzu
* Testvorlage mit Beispieldaten
* An die richtige Gruppe senden (nicht überbenachrichtigen)
* Verwenden Sie aus Konsistenzgründen Vorlagen

❌ **Nicht:**

* Zu viele E-Mails versenden (Benachrichtigungsmüdigkeit)
* Fügen Sie sensible Daten in E-Mails ein
* An Gruppen senden, die keine Informationen benötigen
* Verwenden Sie unklare Betreffzeilen
* Vergessen Sie nicht anzugeben, wie Sie Maßnahmen ergreifen können
* E-Mails an Einzelpersonen senden (stattdessen eine Gruppe verwenden)

***

## Leistungshinweise

* Der Versand jeder E-Mail dauert ~1 Sekunde
* Große Gruppen können einige Zeit dauern (100 Personen = ~100 Sekunden)
* Erstellen Sie keine Schleifen, die Tausende von E-Mails versenden
* Überwachen Sie die Kapazität des E-Mail-Dienstes
* Erwägen Sie die Stapelung mehrerer Dokumente

***

## Verwandte Karten

* **ACTION\_SEND\_EMAIL** – An einzelne Person senden
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** – Aufgabe zuweisen statt nur benachrichtigen
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** – Aufgabe erstellen und benachrichtigen
* **STAUS\_CHANGE** – Status ändern und benachrichtigen

***

## Typisches Workflow-Beispiel

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## FAQ

**F: Kann ich an mehrere Gruppen senden?** A: Erstellen Sie separate Karten für jede Gruppe

**F: Was passiert, wenn die E-Mail einer Person zurückgeschickt wird?** A: E-Mail wird als fehlgeschlagen protokolliert, die IT-Abteilung kann das Problem beheben

**F: Kann ich die E-Mail-Vorlage ändern?** A: Wenden Sie sich an Ihren Administrator, um Vorlagen zu ändern

**F: Kann ich unter bestimmten Bedingungen senden?** A: Ja! Verwenden Sie „Wo“- und „Und“-Bedingungen, um zu steuern, wann E-Mails gesendet werden

**F: Woher weiß ich, ob eine E-Mail empfangen wurde?** A: Überprüfen Sie die E-Mail-Protokolle in DocBits auf den Sendestatus
