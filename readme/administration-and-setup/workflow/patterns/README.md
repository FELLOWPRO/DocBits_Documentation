# Workflow-Pattern-Leitfäden

**Version:** 1.0
**Zuletzt aktualisiert:** 23. Oktober 2025

---

## Überblick

Dieser Bereich enthält umfassende Workflow-Pattern-Leitfäden, die zeigen, wie man mehrere Workflow-Karten kombiniert, um typische geschäftliche Szenarien zu lösen. Jedes Pattern bietet eine Schritt-für-Schritt-Anleitung, vollständige Beispiele und Best Practices.

**Was sind Workflow-Patterns?**

Workflow-Patterns sind bewährte, wiederverwendbare Lösungen für häufige Herausforderungen in der Dokumentenverarbeitung. Statt bei null anzufangen, können Sie diese Patterns als Vorlagen verwenden und an Ihre Anforderungen anpassen.

---

## Der Workflow-Builder auf einen Blick

Jedes Pattern auf dieser Seite wird im **Workflow-Builder** zusammengestellt. Sie erreichen ihn über **Workflow Dashboard → Workflow List → Add Workflow** (oder indem Sie einen bestehenden Workflow öffnen). Das Dashboard zeigt Ihnen den Ausführungsverlauf sowie die Erfolgs-/Fehlerquoten aller Ihrer Workflows:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard mit Lauf-Summen, Erfolgs- und Fehlerquoten, dem Lauf-Diagramm und der letzten Aktivität"><figcaption><p>Das Workflow Dashboard – Lauf-Summen, Erfolgs-/Fehlerquoten und letzte Aktivität für jeden Workflow.</p></figcaption></figure>

Der Reiter **Workflow List** listet jeden Workflow mit Typ, Ausführungsreihenfolge und Auslöser auf. Über **Add Workflow** legen Sie einen neuen an, oder Sie klicken einen Workflow an, um ihn im Builder zu öffnen:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Reiter Workflow List mit Workflows nach Typ, Ausführungsreihenfolge und Auslöser"><figcaption><p>Die Workflow List – jede Zeile ist ein Workflow, den Sie öffnen, ein-/ausschalten oder bearbeiten können.</p></figcaption></figure>

Ein Workflow besteht aus drei Kartengruppen – **When** (der Auslöser), **And** (zusätzliche Bedingungen) und **Then** (die auszuführenden Aktionen). Das Beispiel unten wird bei Rechnungen einer Unterorganisation ausgelöst und weist diese einem Benutzer zu:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow-Builder-Canvas mit When-, And- und Then-Karten"><figcaption><p>Die Workflow-Builder-Canvas. Jedes Pattern unten ist nur eine andere Kombination aus When- / And- / Then-Karten.</p></figcaption></figure>

Klicken Sie in einer beliebigen Gruppe auf **Add Card**, um die Kartenbibliothek zu öffnen. Die Karten sind nach Kategorie geordnet (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …), sodass Sie den Baustein finden, den das jeweilige Pattern benötigt:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Dialog Add Card mit den Kartenkategorien und verfügbaren Karten"><figcaption><p>Die <strong>Add Card</strong>-Bibliothek – jede in den Patterns unten genannte Karte wird hier ausgewählt.</p></figcaption></figure>

---

## Verfügbare Patterns

### 1. [API-Integrations-Pattern](api-integration-pattern.md)

**Komplexität:** Mittel | **Einrichtungszeit:** 45–60 Minuten

Lernen Sie, wie Sie DocBits in externe APIs integrieren, um Daten aus externen Systemen abzurufen, zu validieren und zu speichern.

**Anwendungsfälle:**
- Echtzeit-Preise aus externen Systemen abrufen
- Lieferanteninformationen gegen Stammdatenbanken validieren
- Produktdetails aus Katalogsystemen nachschlagen
- Wechselkurse aus Währungsdiensten beziehen
- Adressen per Geocoding-Dienst überprüfen

**Verwendete Karten:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Vollständiges Pattern ansehen →](api-integration-pattern.md)**

---

### 2. [Aufgabenverwaltungs-Pattern](task-management-pattern.md)

**Komplexität:** Niedrig-Mittel | **Einrichtungszeit:** 30–45 Minuten

Meistern Sie das Erstellen, Zuweisen, Verfolgen und Verwalten von Aufgaben in DocBits-Workflows für Freigabe- und Prüfprozesse.

**Anwendungsfälle:**
- Freigabe-Workflows erstellen
- Prüfaufgaben Benutzern zuweisen
- Ausnahmen behandeln, die manuelles Eingreifen erfordern
- Probleme an Vorgesetzte eskalieren
- Mehrstufige Freigabeketten erstellen
- Aufgabenabschluss und Fristen verfolgen

**Verwendete Karten:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Vollständiges Pattern ansehen →](task-management-pattern.md)**

---

### 3. [PO-Matching-Pattern](po-matching-pattern.md)

**Komplexität:** Mittel-Hoch | **Einrichtungszeit:** 60–90 Minuten

Implementieren Sie umfassende Bestellabgleich-Workflows, um Rechnungen toleranzbasiert gegen Bestellungen zu validieren.

**Anwendungsfälle:**
- Rechnungen gegen Bestellungen validieren
- Preisfehler vor der Zahlung erkennen
- Mengenabweichungen identifizieren
- Beschaffungskontrollen durchsetzen
- Doppelzahlungen verhindern
- Drei-Wege-Abgleich automatisieren

**Verwendete Karten:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Vollständiges Pattern ansehen →](po-matching-pattern.md)**

---

### 4. [Entscheidungslogik-Pattern](decision-logic-pattern.md)

**Komplexität:** Mittel | **Einrichtungszeit:** 30–45 Minuten

Implementieren Sie komplexe Entscheidungsbäume und bedingte Routing-Logik, um Dokumente anhand von Geschäftsregeln über verschiedene Pfade zu leiten.

**Anwendungsfälle:**
- Dokumente nach Betragsschwellen leiten
- Unterschiedliche Regeln für unterschiedliche Dokumenttypen anwenden
- Mehrstufige Freigabelogik implementieren
- Komplexe Geschäftsrichtlinien abbilden
- Dynamisches Routing anhand mehrerer Kriterien erstellen
- Freigabematrizen implementieren

**Verwendete Karten:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Vollständiges Pattern ansehen →](decision-logic-pattern.md)**

---

### 5. [Datentransformations-Pattern](data-transformation-pattern.md)

**Komplexität:** Mittel | **Einrichtungszeit:** 30–45 Minuten

Transformieren, berechnen, formatieren und anreichern Sie Dokumentdaten, um sie für den Export vorzubereiten, Berechnungen durchzuführen und Formate zu standardisieren.

**Anwendungsfälle:**
- Summen, Zwischensummen, Steuern berechnen
- Währungen oder Einheiten umrechnen
- Datums-, Zahlen- und Textformate anpassen
- Werte aus bestehenden Feldern ableiten
- Daten aus externen Quellen anreichern
- Datenformate standardisieren
- Berechnungen validieren

**Verwendete Karten:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Vollständiges Pattern ansehen →](data-transformation-pattern.md)**

---

## Pattern-Auswahlhilfe

### Nach Komplexität

| Komplexität | Patterns | Am besten für |
|------------|----------|----------|
| **Niedrig-Mittel** | [Aufgabenverwaltung](task-management-pattern.md) | Einsteiger, einfache Workflows |
| **Mittel** | [API-Integration](api-integration-pattern.md)<br>[Entscheidungslogik](decision-logic-pattern.md)<br>[Datentransformation](data-transformation-pattern.md) | Fortgeschrittene, Standard-Workflows |
| **Mittel-Hoch** | [PO-Matching](po-matching-pattern.md) | Profis, komplexe Validierung |

---

### Nach Anwendungsfall

| Ich möchte … | Dieses Pattern verwenden |
|--------------|------------------|
| In externe Systeme integrieren | [API-Integrations-Pattern](api-integration-pattern.md) |
| Freigabe-Workflows erstellen | [Aufgabenverwaltungs-Pattern](task-management-pattern.md) |
| Gegen Bestellungen validieren | [PO-Matching-Pattern](po-matching-pattern.md) |
| Anhand von Bedingungen routen | [Entscheidungslogik-Pattern](decision-logic-pattern.md) |
| Daten berechnen und transformieren | [Datentransformations-Pattern](data-transformation-pattern.md) |

---

### Nach Branche/Abteilung

| Branche/Abteilung | Empfohlene Patterns |
|---------------------|---------------------|
| **Finanzen/Buchhaltung** | [PO-Matching](po-matching-pattern.md), [Aufgabenverwaltung](task-management-pattern.md), [Datentransformation](data-transformation-pattern.md) |
| **Einkauf** | [PO-Matching](po-matching-pattern.md), [Entscheidungslogik](decision-logic-pattern.md), [API-Integration](api-integration-pattern.md) |
| **Betrieb** | [Aufgabenverwaltung](task-management-pattern.md), [Entscheidungslogik](decision-logic-pattern.md) |
| **IT/Integration** | [API-Integration](api-integration-pattern.md), [Datentransformation](data-transformation-pattern.md) |
| **Alle Abteilungen** | [Entscheidungslogik](decision-logic-pattern.md), [Aufgabenverwaltung](task-management-pattern.md) |

---

## So verwenden Sie diese Patterns

### Schritt 1: Pattern auswählen

1. Sehen Sie sich die Pattern-Beschreibungen oben an
2. Bestimmen Sie, welches Pattern zu Ihrem Anwendungsfall passt
3. Prüfen Sie Komplexität und geschätzte Einrichtungszeit
4. Lesen Sie den Abschnitt „Wann verwenden" im Pattern-Leitfaden

### Schritt 2: Voraussetzungen prüfen

Jeder Pattern-Leitfaden listet auf:
- Erforderliches Wissen
- Zuerst zu lesende verwandte Leitfäden
- Verwendete Karten
- Konfigurationsanforderungen

### Schritt 3: Schritt-für-Schritt-Anleitung befolgen

Jedes Pattern bietet:
- Vollständiges Workflow-Beispiel
- Schritt-für-Schritt-Umsetzungsanleitung
- Konfigurationsvorlagen
- Praxisbeispiele
- Tipps zur Fehlerbehebung

### Schritt 4: An Ihre Anforderungen anpassen

- Passen Sie das Beispiel an Ihre Geschäftsregeln an
- Justieren Sie Schwellen und Toleranzen
- Ändern Sie die Routing-Logik
- Fügen Sie Schritte hinzu oder entfernen Sie sie
- Testen Sie gründlich vor dem Produktiveinsatz

### Schritt 5: Überwachen und optimieren

- Verfolgen Sie die Workflow-Leistung
- Überwachen Sie die Erfolgsquoten
- Sammeln Sie Benutzer-Feedback
- Verfeinern Sie die Konfiguration
- Dokumentieren Sie Anpassungen

---

## Pattern-Kombinationen

Viele reale Szenarien erfordern die Kombination mehrerer Patterns:

### Beispiel 1: Vollständige Rechnungsverarbeitung

```
1. API-Integrations-Pattern → Aktuelle Preise abrufen
2. Datentransformations-Pattern → Summen berechnen
3. PO-Matching-Pattern → Gegen Bestellung validieren
4. Entscheidungslogik-Pattern → Anhand der Abweichung routen
5. Aufgabenverwaltungs-Pattern → Freigabeaufgaben erstellen
```

### Beispiel 2: Freigabe hochwertiger Rechnungen

```
1. Datentransformations-Pattern → Beträge berechnen
2. Entscheidungslogik-Pattern → Schwellen prüfen
3. Aufgabenverwaltungs-Pattern → Mehrstufige Freigabe
4. API-Integrations-Pattern → Externe Systeme benachrichtigen
```

### Beispiel 3: Ausnahmebehandlung

```
1. PO-Matching-Pattern → Abweichungen erkennen
2. Entscheidungslogik-Pattern → Schweregrad der Ausnahme einstufen
3. Aufgabenverwaltungs-Pattern → Prüfaufgaben erstellen
4. Datentransformations-Pattern → Auswirkung berechnen
```

---

## Pattern-Vorlagen

Jedes Pattern enthält diese standardisierten Abschnitte:

1. **Überblick** – Was das Pattern macht
2. **Wann verwenden** – Geeignete Anwendungsfälle
3. **Vollständiges Beispiel** – Reales Szenario
4. **Schritt für Schritt** – Umsetzungsanleitung
5. **Konfiguration** – Vorlagen zur Kartenkonfiguration
6. **Workflow-Diagramm** – Visuelle Darstellung
7. **Erweiterte Varianten** – Alternative Umsetzungen
8. **Fehlerbehandlung** – Häufige Probleme und Lösungen
9. **Test-Checkliste** – Validierungsschritte
10. **Verwandte Patterns** – Ergänzende Patterns
11. **Verwandte Leitfäden** – Referenzdokumentation

---

## Hilfe erhalten

### Support-Ressourcen für Patterns

**Dokumentation:**
- [Vollständiger Workflow-Leitfaden-Index](../README.md)
- [Einzelne Kartenleitfäden](../then/action/)
- [Referenz der Bedingungskarten](../and/condition-cards-complete-guide.md)

**Kontakt:**
- Pattern-Feedback: docs@docbits.com
- Technischer Support: support@docbits.com
- Implementierungshilfe: consulting@docbits.com

---

## Nächste Schritte

**Neu bei Workflow-Patterns?**
1. Beginnen Sie mit dem [Aufgabenverwaltungs-Pattern](task-management-pattern.md) – am einfachsten zu verstehen
2. Sehen Sie sich das [Entscheidungslogik-Pattern](decision-logic-pattern.md) an – grundlegend für alle Workflows
3. Erkunden Sie das [API-Integrations-Pattern](api-integration-pattern.md) – häufiger Integrationsbedarf

**Bereit zur Umsetzung?**
1. Wählen Sie Ihr Pattern aus der Liste oben
2. Lesen Sie den vollständigen Pattern-Leitfaden
3. Prüfen Sie Voraussetzungen und verwandte Leitfäden
4. Befolgen Sie die Schritt-für-Schritt-Anleitung
5. Testen Sie mit Beispiel-Dokumenten
6. Gehen Sie in Produktion
7. Überwachen und optimieren

---

**Zuletzt aktualisiert:** 23. Oktober 2025
**Betreut von:** Dokumentations-Team
**Version:** 1.0
