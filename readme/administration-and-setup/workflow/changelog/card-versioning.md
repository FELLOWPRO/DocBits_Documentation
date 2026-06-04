# Card-Versionierungssystem - Update Oktober 2025

**Dokument:** Überblick über die Workflow-Card-Versionierung
**Zuletzt aktualisiert:** 23. Oktober 2025
**Status:** Abgeschlossen

---

## Überblick

Die DocBits Workflow Engine verwendet eine **ganzzahlbasierte Versionierung**, um die Weiterentwicklung von Cards zu verwalten und gleichzeitig die Abwärtskompatibilität zu wahren. Dieses Dokument bietet einen Überblick über das Versionierungssystem.

---

## Was ist Card-Versionierung?

### Konzept
Jede Workflow-Card kann mehrere Versionen haben, wodurch das System Folgendes ermöglicht:
- Neue Funktionen hinzufügen, ohne bestehende Workflows zu beeinträchtigen
- Veraltete Funktionalität unterstützen, während sie schrittweise eingestellt wird
- Card-Fähigkeiten im Laufe der Zeit weiterentwickeln
- Abwärtskompatibilität wahren

### Versionsstruktur
- **Format:** Ganzzahlwerte (1, 2, 3, 4, 5...)
- **Identifikation:** Zusammengesetzter Schlüssel aus (card_type, card_version)
- **Status:** Jede Version hat deprecated/enabled-Flags

### Beispiel
Die Card `tasks_create` hat sich über 4 Versionen entwickelt:
- **v1:** Ursprüngliche Aufgabenerstellung (veraltet)
- **v2:** Übersetzungsunterstützung hinzugefügt (veraltet)
- **v3:** Experimentelle Decision-Tree-Unterstützung (veraltet)
- **v4:** Unterstützung generischer Arbeitselementtypen (aktuell aktiv)

---

## Wichtige Statistiken

### Überblick über die Versionierung
| Kennzahl | Wert |
|--------|-------|
| **Cards mit mehreren Versionen** | 30+ |
| **Gesamtzahl der Versionsdatensätze** | 90+ |
| **Versionen pro Card (Durchschnitt)** | 3 |
| **Maximale Versionen** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Veraltete Versionen** | 9 |
| **Vollständig deaktivierte Cards** | 2 |

### Versionsverteilung
- **2 Versionen:** 14 Cards (einfachere Entwicklung)
- **3 Versionen:** 11 Cards (moderate Entwicklung)
- **4 Versionen:** 4 Cards (erhebliche Entwicklung)
- **5 Versionen:** 1 Card (am weitesten entwickelt: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Häufige Versionierungsmuster

### Muster 1: Einführung von Übersetzungsschlüsseln (v1 → v2)

**Betroffen:** 15+ Cards

**Änderung:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Zweck:** Mehrsprachenunterstützung ermöglichen

**Cards:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS und weitere

**Migration:** Sicher – keine funktionalen Änderungen

---

### Muster 2: Decision-Tree-Integration (v2 → v3)

**Betroffen:** 5 Cards

**Änderung:** Hinzufügen eines Decision-Tree-Parameters

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Zweck:** Ergebnisse von Entscheidungstabellen unterstützen

**Cards:**
- tasks_create (v3 veraltet)
- ACTION_TASK_FOR_GROUP (v3 veraltet)
- DOC_USER_ASSIGN (v3 veraltet)
- DOC_GROUP_ASSIGN (v3 veraltet)
- ACTION_DECISION_TREE_CREATE_TASKS

**Status:** Veraltet – der Decision-Tree-Ansatz war experimentell

---

### Muster 3: Entwicklung zu generischen Typen (v3 → v4)

**Betroffen:** 4 Cards

**Änderung:** "Task" wird zu einem flexiblen Arbeitselementtyp

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Zweck:** Unterstützung von Tasks, Tickets, Issues und anderen Arbeitselementtypen

**Cards:**
- tasks_create (v4 aktuell)
- ACTION_TASK_FOR_GROUP (v4 aktuell)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 aktuell)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 aktuell)

**Aktueller Status:** Aktiv und empfohlen

---

### Muster 4: Toleranzparameter (PO-Cards)

**Betroffen:** 6 PO-Vergleichs-Cards

**Änderung:** Hinzufügen von Toleranz-/Abweichungsunterstützung

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Zweck:** Akzeptable Abweichungen beim Abgleich zulassen (z. B. 2 % Preisdifferenz in Ordnung)

**Wichtige Cards:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (zu v5 mit Toleranz entwickelt)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Vorteil:** Realistischere Vergleichskriterien

---

### Muster 5: Vergleichsmodus-Parameter

**Betroffen:** 3 PO-Vergleichs-Cards

**Änderung:** Unterstützung verschiedener Vergleichsalgorithmen

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Zweck:** Flexible Vergleichsmethoden

**Cards:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Muster 6: Workflow-Trigger

**Betroffen:** Nur STAUS_CHANGE

**Änderung:** Automatisches Auslösen von Workflows bei Statusänderung

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Zweck:** Statusänderungen über Workflows hinweg kaskadieren

---

## Am weitesten entwickelte Cards

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 Versionen)

**Entwicklungspfad:** v2 → v3 → v4 → v5

- **v2:** Einfacher Stückpreisvergleich
- **v3:** Gleicher Übersetzungsschlüssel (v2)
- **v4:** Vergleichsmodus-Parameter hinzugefügt
- **v5:** Toleranzschwellen-Parameter hinzugefügt

**Aktuell:** v5 (mit Toleranzunterstützung)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 Versionen)

**Entwicklungspfad:** v1 → v2 → v3 → v4

- **v1:** Einfacher Positionsabgleich (veraltet)
- **v2:** Parameter für die Vergleichsmethode hinzugefügt
- **v3:** Mit Übersetzungsschlüsseln erweitert
- **v4:** Vergleichsmodus-Parameter hinzugefügt

**Aktuell:** v4

**Vermeiden:** v1 (veraltet)

---

### 3. tasks_create (4 Versionen)

**Entwicklungspfad:** v1 → v2 → v3 → v4

- **v1:** Ursprüngliche Implementierung (veraltet)
- **v2:** Übersetzungsunterstützung hinzugefügt (veraltet)
- **v3:** Decision Tree hinzugefügt (veraltet)
- **v4:** Generische Arbeitselementtypen (aktuell)

**Aktuell:** v4 (empfohlen)

**Zeitstrahl:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Veraltungsstatus

### Vollständig veraltete Versionen (Nicht verwenden)

| Card | Version | Grund | Alternative |
|------|---------|--------|-------------|
| tasks_create | v1 | Sehr alt | v4 verwenden |
| tasks_create | v3 | Decision Tree veraltet | v4 verwenden |
| ACTION_TASK_FOR_GROUP | v3 | Decision Tree veraltet | v4 verwenden |
| DOC_USER_ASSIGN | v3 | Decision Tree veraltet | v2 verwenden |
| DOC_GROUP_ASSIGN | v3 | Decision Tree veraltet | v2 verwenden |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Sehr alt | v2 verwenden |
| CONDITION_OC_TO_PO_ITEMS | v1 | Sehr alt | v4 verwenden |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funktionen zurückgesetzt | v3 verwenden |

### Vollständig deaktivierte Cards (Nicht nutzbar)

| Card | Versionen | Hinweise |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Nicht unterstützte Funktionalität |
| RUN_SCRIPT | v2, v3 | Ersetzt durch ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Versionsempfehlungen

### Nach Anwendungsfall

**Erstellung neuer Workflows:**
- Verwenden Sie immer die **höchste aktivierte Versionsnummer**
- Bietet neueste Funktionen und Verbesserungen
- Unterstützt und dokumentiert

**Wartung bestehender Workflows:**
- Verwenden Sie weiterhin die aktuelle Version, wenn sie funktioniert
- Planen Sie die Migration, wenn möglich
- Kein dringender Aktualisierungsbedarf

**Migration von Legacy-Workflows:**
- Identifizieren Sie die aktuell verwendete Version
- Planen Sie den Upgrade-Pfad
- Testen Sie gründlich vor der Bereitstellung

---

## Wie Versionen funktionieren

### Versionsauswahl
Beim Erstellen eines Workflows wählen Sie, welche Version einer Card verwendet werden soll. Beispiel:
- Verwenden Sie `tasks_create v4` für die Erstellung neuer Aufgaben (empfohlen)
- Verwenden Sie `tasks_create v2`, falls Legacy-Systeme dies erfordern (älter, funktioniert aber)
- Verwenden Sie NICHT `tasks_create v1` (veraltet)

### Abwärtskompatibilität
- Neuere Versionen beeinträchtigen ältere Workflows nicht
- Alte Workflows funktionieren weiterhin mit ihrer ursprünglichen Version
- Workflows können schrittweise aktualisiert werden

### Technische Implementierung
Versionen werden auf Datenbankebene verwaltet:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## Für Dokumentationszwecke

### Versionsinformationen verstehen
Wenn Sie in der Dokumentation "Card v3" sehen:
- Bezieht es sich auf Version 3 dieser spezifischen Card
- Prüfen Sie die [Full Versioning Reference](../../docs/card_version.md) für Details
- Überprüfen Sie, welche Version empfohlen wird

### Ihre Version prüfen
So erfahren Sie, welche Version Sie verwenden:
1. Öffnen Sie die Card in Ihrem Workflow
2. Prüfen Sie die angezeigte Versionsnummer
3. Vergleichen Sie sie mit den Empfehlungen in den Anleitungen

### Zeitstrahl der Versionsentwicklung
- **2024-2025:** Laufende Weiterentwicklung
- **Oktober 2025:** Vollständige Dokumentation der Versionierung
- **Zukunft:** Fortlaufende Verbesserungen

---

## Verwandte Dokumentation

### Umfassende Referenz
→ [Full Card Versioning Reference](../../docs/card_version.md)

Beinhaltet:
- Alle 30+ Cards mit Versionen
- Detaillierte Textentwicklung für jede
- Spezifische Parameteränderungen
- SQL-Abfragen zur Versionssuche

### Card-spezifische Anleitungen
→ [Workflow Guides](../)

Dokumentation für jede Card mit Versionsempfehlungen

### Details zum Versionsverlauf
Jede Anleitung enthält Versionsinformationen und Migrationshinweise

---

## Schnellreferenz

### Cards mit den meisten Versionen
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 Versionen
2. CONDITION_OC_TO_PO_ITEMS - 4 Versionen
3. tasks_create - 4 Versionen
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 Versionen
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 Versionen

### Häufigstes Entwicklungsmuster
**Einführung von Übersetzungsschlüsseln (v1 → v2)** - 15+ Cards

### Bedeutendste Änderung
**Entwicklung zu generischen Typen (v3 → v4)** - Wechsel von "Task" zu flexiblem Arbeitselementtyp

### Vollständig deaktiviert
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Häufig gestellte Fragen

### F: Welche Version sollte ich verwenden?
A: Verwenden Sie die **höchste aktivierte Version**, sofern Sie keinen bestimmten Grund haben, eine ältere Version zu verwenden.

### F: Kann ich meinen Workflow auf eine neuere Version aktualisieren?
A: Ja, aber testen Sie gründlich. Einige Versionen haben unterschiedliche Parameteranforderungen.

### F: Was passiert, wenn ich eine veraltete Version verwende?
A: Sie funktioniert weiterhin, aber Sie erhalten keine neuen Funktionen. Migration empfohlen.

### F: Kann ich eine deaktivierte Card verwenden?
A: Nein, deaktivierte Cards können nicht verwendet werden. Verwenden Sie stattdessen die empfohlene Alternative.

### F: Woran erkenne ich, ob meine Card aktualisiert werden muss?
A: Prüfen Sie die [Full Versioning Reference](../../docs/card_version.md) für Ihren Card-Typ und befolgen Sie die Empfehlungen.

---

## Best Practices

1. **Neue Workflows:** Verwenden Sie die neueste stabile Version
2. **Updates:** Prüfen Sie regelmäßig auf neue Versionen
3. **Testen:** Testen Sie Versions-Upgrades zuerst in der Sandbox
4. **Dokumentation:** Beziehen Sie sich auf card-spezifische Anleitungen für Versionsdetails
5. **Migration:** Planen Sie Upgrades schrittweise
6. **Support:** Kontaktieren Sie den Support bei Fragen zur Versionskompatibilität

---

## Zusammenfassungstabelle

| Card-Typ | Aktuelle Version | Versionen insgesamt | Status | Hinweise |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Aktiv | Am weitesten entwickelt; v3 veraltet |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Aktiv | Höchste Versionsanzahl |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Aktiv | v1 veraltet |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Aktiv | v3 veraltet |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Aktiv | v4 veraltet/deaktiviert |
| Die meisten Cards | 2 | 2 | Aktiv | v1 → v2 Muster |

---

## Siehe auch

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Zuletzt aktualisiert:** 23. Oktober 2025
**Quelle:** postgres-dev-docflow-Datenbank
**Status:** Vollständige Referenz
