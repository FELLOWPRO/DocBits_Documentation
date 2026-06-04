---
hidden: true
---

# Workflow Card Release & Versionsverlauf

## Prinzipien der Versionskontrolle

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>Workflow Version Control System</figcaption></figure>

### Version 8.5.2024 - Kernfunktionen der Versionierung

Die DocBits Workflow Engine implementiert eine robuste Versionskontrolle für alle Workflow-Cards:

1. **Versionskontrolle**: Jede Card kann mehrere Versionen haben, die jeweils einen anderen Satz von Bedingungen oder Aktionen darstellen. Dadurch können Sie mit den Regeln experimentieren oder sie anpassen, ohne den aktuell aktiven Workflow zu beeinflussen.
2. **Nahtlose Upgrades**: Wenn Sie aufgrund von Änderungen Ihrer Dokumentenverarbeitungsanforderungen eine Regel oder Bedingung aktualisieren müssen, können Sie eine neue Version der Card erstellen. Dieser Ansatz stellt sicher, dass alle Änderungen bewusst vorgenommen und getestet werden, bevor sie die aktuelle Version ersetzen. So werden Fehler und mögliche Störungen in Ihrer Dokumentenverarbeitung minimiert.
3. **Konsistenz wahren**: Indem die ursprüngliche Card-Version unverändert bleibt, bis Sie sich für ein Upgrade entscheiden, wird sichergestellt, dass laufende Prozesse nicht beeinträchtigt werden. Sie können Tests und Validierungen für die neue Version durchführen, ohne Live-Daten oder Workflows zu beeinflussen.
4. **Flexibilität und Tests**: Mehrere Versionen ermöglichen das Testen verschiedener Szenarien in einer kontrollierten Umgebung. Sie können die Auswirkungen neuer Regeln oder Änderungen auf Ihren Dokumentenverarbeitungs-Workflow sehen, ohne dauerhafte Änderungen vorzunehmen. Sobald Sie mit den Ergebnissen zufrieden sind, können Sie die neue Version anwenden.

---

## Überblick über die Card-Versionierung

### Statistik

| Kennzahl | Wert |
|--------|-------|
| **Cards mit mehreren Versionen** | 30+ |
| **Gesamtzahl der Versionsdatensätze** | 90+ |
| **Aktuell aktive Versionen** | 81+ |
| **Veraltete Versionen** | 9 |
| **Vollständig deaktivierte Cards** | 2 |
| **Neueste Version (Max.)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Versionsbereich
- **Minimum:** v1
- **Maximum:** v5
- **Durchschnittliche Versionen pro Card:** 3

---

## Detaillierte Änderungen der Card-Versionen

### 🔧 ACTION CARDS - Externe Integration & Ausführung

#### 1. CALL_API
**Versionen:** v1, v2 (Aktuell: v2)

📖 **Anleitung:** [Call External API Guide](../then/action/call-api-guide.md)

| Version | Übersetzung | Status | Wesentliche Änderungen |
|---------|-------------|--------|-------------|
| v1 | Nein | Aktiv | Einfacher API-Aufruf ohne Übersetzungsschlüssel |
| v2 | Ja | ✅ Aktuell | `trnsl_%call_api` für Mehrsprachenunterstützung hinzugefügt |

**Was sich geändert hat:** Internationalisierungsunterstützung (i18n) mit Übersetzungsschlüsseln hinzugefügt. Die Funktionalität bleibt identisch.

**Vorher (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Nachher (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Empfehlung:** Verwenden Sie v2 für alle neuen Workflows (enthält Sprachunterstützung)
**Abwärtskompatibilität:** ✅ v1 funktioniert weiterhin

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versionen:** v1, v2 (Aktuell: v2)

| Version | Übersetzung | Status | Wesentliche Änderungen |
|---------|-------------|--------|-------------|
| v1 | Nein | Aktiv | Einfache HTTP-Anfrage |
| v2 | Ja | ✅ Aktuell | `trnsl_%send_https_request`-Übersetzungsschlüssel hinzugefügt |

**Was sich geändert hat:** Übersetzungsunterstützung hinzugefügt. Die Kernfunktionalität für Webhook/Anfrage bleibt unverändert.
**Empfehlung:** Verwenden Sie v2 (Mehrsprachenunterstützung)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versionen:** v2 (Aktuell), v3, v4 (Veraltet & Deaktiviert)

| Version | Übersetzung | Status | Wesentliche Änderungen |
|---------|-------------|--------|-------------|
| v2 | Ja | Aktiv | Ursprüngliche DocOperator-Implementierung |
| v3 | Ja | Aktiv | Parameter „Execute the prompt" für zusätzliche Steuerung hinzugefügt |
| v4 | Ja | ❌ VERALTET & DEAKTIVIERT | Parameter „Execute" entfernt (zurückgesetzt) |

**Entwicklungspfad:** v2 → v3 (Parameter hinzugefügt) → v4 (zurückgesetzt – nicht empfohlen)

**Was sich geändert hat:**
- v2 → v3: Optionaler Parameter zur Ausführungssteuerung für mehr Flexibilität hinzugefügt
- v3 → v4: Der Parameter wurde nach weiterer Analyse entfernt (veraltet)

**Empfehlung:** Verwenden Sie v3 für neue Workflows (neueste aktive Version mit allen Funktionen)
**Migration:** Wenn Sie v4 verwenden, wechseln Sie zu v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versionen:** v2, v3 (Veraltet), v4 (Aktuell)

📖 **Anleitung:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

| Version | Änderungen | Status | Type-Parameter |
|---------|---------|--------|-----------------|
| v2 | Ursprüngliche Implementierung | Aktiv | "Task" (fest) |
| v3 | + Decision-Tree-Unterstützung | ❌ VERALTET | "Task" (fest) |
| v4 | - Decision Tree, + Generischer Typ | ✅ Aktuell | Generischer Typ (flexibel) |

**Entwicklung:** v2 → v3 (Decision-Tree-Experiment) → v4 (generische Typen, Decision Tree entfernt)

**Änderung v2 → v3 (Decision-Tree-Experiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Änderung v3 → v4 (Generische Typen + Entfernung des Decision Tree):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Was sich geändert hat:**
- v2 → v3: Parameter `decision tree, if available: [param]` hinzugefügt
- v3 → v4:
  - ❌ Decision-Tree-Parameter entfernt
  - ✅ "Task" → generisches `[param]` geändert (unterstützt Task, Ticket, Issue usw.)
  - Übersetzungsschlüssel `trnsl_%task_for_group_v4` hinzugefügt

**Warum:** Der Decision-Tree-Ansatz von v3 war experimentell. v4 bietet bessere Flexibilität mit generischen Arbeitselementtypen.
**Empfehlung:** Verwenden Sie v4 (aktuell, am flexibelsten)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versionen:** v2, v3 (Aktuell)

| Version | Aufgabentyp | Status | Wesentlicher Unterschied |
|---------|-----------|--------|-----------------|
| v2 | "task" (fest) | Aktiv | Ursprüngliche Version |
| v3 | Generischer Typ | ✅ Aktuell | Geändert zu flexiblem `[param]` |

**Was sich geändert hat:** v2 → v3: "Create a new task" → "Create a new [param]" (unterstützt jeden Arbeitselementtyp)
**Empfehlung:** Verwenden Sie v3

---

#### 6. RUN_WORKFLOW
**Versionen:** v1, v2 (Aktuell)

**Was sich geändert hat:** v1 → v2: `trnsl_%run_workflow`-Übersetzungsschlüssel hinzugefügt
**Empfehlung:** Verwenden Sie v2

---

### 📊 PO-VERGLEICHS- & VALIDIERUNGS-CARDS

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (Am weitesten entwickelt – 5 Versionen)
**Versionen:** v2, v3, v4, v5 (Aktuell)

📖 **Anleitung:** [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Version | Änderungen | Status | Toleranz | Vergleich |
|---------|---------|--------|-----------|------------|
| v2 | Einfacher Preisvergleich | Aktiv | ❌ Nein | Einfach |
| v3 | Wie v2 | Aktiv | ❌ Nein | Einfach |
| v4 | + Vergleichsmodus-Parameter | Aktiv | ❌ Nein | ✅ Ja |
| v5 | + Toleranzparameter | ✅ Aktuell | ✅ Ja (Betrag + Einheit) | ✅ Ja |

**Entwicklungspfad:** v2 → v3 (keine Änderung) → v4 (Vergleichsmodi) → v5 (Toleranzschwellen)

**v2 → v3:** Keine funktionale Änderung (gleicher Übersetzungsschlüssel)

**Änderung v3 → v4 (Vergleichsmodus hinzugefügt):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Änderung v4 → v5 (Toleranzparameter hinzugefügt):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Was sich geändert hat:**
- **v2 → v3:** Keine funktionale Änderung
- **v3 → v4:** `Compare as [param]` hinzugefügt – Unterstützung verschiedener Vergleichsoperatoren
- **v4 → v5:** Toleranzparameter hinzugefügt:
  - `with tolerance of [amount] [unit]`
  - Beispiel: "with tolerance of 2 %" oder "with tolerance of 100 EUR"
  - Unterstützt: %, EUR, $ und andere Währungen

**Anwendungsfälle:**
- v2/v3: Strikte Übereinstimmung (nur exakte Preise)
- v4: Verschiedene Vergleichsmethoden
- v5: Flexible Akzeptanz von Abweichungen (z. B. Preisdifferenzen von 2 % akzeptieren) ✅ EMPFOHLEN

**Empfehlung:** Verwenden Sie v5 für moderne PO-Matching-Workflows

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versionen:** v1 (Veraltet), v2, v3, v4 (Aktuell)

| Version | Änderungen | Status | Vergleichsfunktion |
|---------|---------|--------|-----------------|
| v1 | Keine Übersetzung, keine Methode | ❌ VERALTET | Einfach |
| v2 | + Übersetzungsschlüssel, + Methode | Aktiv | Einfache Methode |
| v3 | Wie v2 | Aktiv | Einfache Methode |
| v4 | + Vergleichsmodus-Parameter | ✅ Aktuell | ✅ Flexibel |

**Was sich geändert hat:**
- **v1 → v2:** `trnsl_%in_order_confirmations_matches_purchase_order` + Parameter für die Vergleichsmethode hinzugefügt
- **v2 → v3:** Keine Änderung
- **v3 → v4:** `Compare as [param1] [param2]` für flexible Vergleichsmodi hinzugefügt

**Empfehlung:** Verwenden Sie v4 (vermeiden Sie das veraltete v1)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versionen:** v2, v3 (Aktuell)

| Version | Toleranztage | Akzeptierte Toleranztage | Status |
|---------|-----------------|------------------------|--------|
| v2 | ❌ Nein | ❌ Nein | Aktiv |
| v3 | ✅ Ja | ✅ Ja | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3: Toleranzparameter hinzugefügt:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Beispiel:** Lieferdaten innerhalb von 5 Tagen des zugesagten Datums akzeptieren
**Empfehlung:** Verwenden Sie v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versionen:** v2, v3, v4 (Aktuell)

| Version | Vergleichsmodus | Status |
|---------|-----------------|--------|
| v2 | Einfach | Aktiv |
| v3 | Einfach (keine Änderung) | Aktiv |
| v4 | ✅ Flexible Modusauswahl | ✅ Aktuell |

**Was sich geändert hat:** v3 → v4: `compare [param]` für verschiedene Vergleichsansätze hinzugefügt
**Empfehlung:** Verwenden Sie v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versionen:** v2, v3, v4 (Aktuell)

| Version | Vergleichsmodus | Status |
|---------|-----------------|--------|
| v2 | Standard | Aktiv |
| v3 | Standard (keine Änderung) | Aktiv |
| v4 | ✅ Flexibel | ✅ Aktuell |

**Was sich geändert hat:** v3 → v4: Parameter `compare [param]` hinzugefügt
**Empfehlung:** Verwenden Sie v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versionen:** v2, v3 (Aktuell)

| Version | Liefertyp | Stammdatentabelle | Status |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (fest) | Feste Referenz | Aktiv |
| v3 | [Konfigurierbarer Parameter] | Dynamisch [param] | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3:
- "Confirmed delivery" → `[param] delivery` geändert (flexibler Liefertyp)
- Feste Tabellenreferenz → `stored in [param]` geändert (dynamische Tabellenauswahl)

**Flexibilität:** v3 erlaubt verschiedene Lieferdatumstypen und Lieferantentabellen
**Empfehlung:** Verwenden Sie v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versionen:** v2, v3 (Aktuell)

| Version | Lieferantentabellen-Referenz | Status |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (fest) | Aktiv |
| v3 | [Dynamischer Parameter] | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3: Feste Tabellenreferenz → `stored in [param]` (ermöglicht dynamische Tabellenauswahl)
**Empfehlung:** Verwenden Sie v3

---

### 👥 ZUWEISUNGS- & ROUTING-CARDS

#### 1. DOC_USER_ASSIGN
**Versionen:** v1, v2, v3 (Veraltet)

| Version | Übersetzung | Decision Tree | Status |
|---------|-------------|---------------|--------|
| v1 | Nein | ❌ Nein | Aktiv |
| v2 | Ja | ❌ Nein | ✅ Aktuell |
| v3 | Ja | ✅ Ja | ❌ VERALTET |

**Entwicklung:** v1 (kein i18n) → v2 (mit i18n) → v3 (+ Decision-Tree-Experiment, jetzt veraltet)

**Was sich geändert hat:**
- v1 → v2: Übersetzungsschlüssel hinzugefügt
- v2 → v3: Decision-Tree-Unterstützung hinzugefügt (experimentell, veraltet)

**Empfehlung:** Verwenden Sie v2 (stabil mit i18n-Unterstützung)

---

#### 2. DOC_GROUP_ASSIGN
**Versionen:** v2, v3 (Veraltet)

| Version | Decision Tree | Status |
|---------|---------------|--------|
| v2 | ❌ Nein | ✅ Aktuell |
| v3 | ✅ Ja | ❌ VERALTET |

**Was sich geändert hat:** v2 → v3: `Use decision tree, if available [param]` hinzugefügt (später veraltet)
**Empfehlung:** Verwenden Sie v2

---

#### 3. OC_ASSIGN_DOC
**Versionen:** v1, v2 (Aktuell)

**Was sich geändert hat:** v1 → v2: `trnsl_%oc_assign_doc`-Übersetzungsschlüssel hinzugefügt
**Empfehlung:** Verwenden Sie v2

---

### 📋 TASK-MANAGEMENT-CARDS

#### 1. tasks_create ⭐ (Am weitesten entwickelte Task-Card – 4 Versionen)
**Versionen:** v1 (Veraltet), v2 (Veraltet), v3 (Veraltet), v4 (Aktuell)

📖 **Anleitung:** [Task Assignment Guide](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Version | Übersetzung | Decision Tree | Arbeitselementtyp | Status |
|---------|-------------|---------------|-----------------|--------|
| v1 | Nein | Nein | "Task" (fest) | ❌ VERALTET |
| v2 | Ja | Nein | "Task" (fest) | ❌ VERALTET |
| v3 | Ja | Ja | "Task" (fest) | ❌ VERALTET |
| v4 | Ja | Nein | [Generischer Parameter] | ✅ Aktuell |

**Entwicklungszeitstrahl:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Änderung v1 → v2 (Übersetzungsschlüssel hinzugefügt):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Änderung v2 → v3 (Decision-Tree-Experiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Änderung v3 → v4 (Generische Typen + Entfernung des Decision Tree):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Was sich geändert hat:**
- **v1 → v2:** `trnsl_%tasks_create`-Übersetzungsschlüssel hinzugefügt
- **v2 → v3:**
  - Decision-Tree-Unterstützung hinzugefügt: `Use decision tree, if available: [param]`
  - "assign to user" → "assign it to the user" geändert
- **v3 → v4:**
  - ❌ Decision-Tree-Parameter entfernt
  - ✅ "Task" → generisches `[param]` geändert (unterstützt Task, Ticket, Issue usw.)
  - Übersetzungsschlüssel auf `trnsl_%tasks_create_v4` aktualisiert

**Hinweis zum Decision Tree:** v3 verwendete Decision Trees, um Aufgaben dynamisch zuzuweisen. Dieser Ansatz war experimentell und wurde in v4 zugunsten einer direkten, parameterbasierten Auswahl des Arbeitselementtyps verworfen.

**Empfehlung:** Verwenden Sie für neue Workflows ausschließlich v4
**Migration:** Wenn Sie v1, v2 oder v3 verwenden, führen Sie ein Upgrade auf v4 durch ✅

---

#### 2. OC_TASK
**Versionen:** v1, v2 (Aktuell)

**Was sich geändert hat:** v1 → v2: `trnsl_%oc_task`-Übersetzungsschlüssel hinzugefügt
**Empfehlung:** Verwenden Sie v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versionen:** v1, v3 (Aktuell – v2 übersprungen)

| Version | Arbeitselementtyp | Status |
|---------|-----------------|--------|
| v1 | "Task" (fest) | Aktiv |
| v3 | [Generischer Parameter] | ✅ Aktuell |

**Was sich geändert hat:** v1 → v3: Entwicklung zum generischen Typ (v2 wurde in der Produktion übersprungen)
**Empfehlung:** Verwenden Sie v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versionen:** v2, v3 (Aktuell)

| Version | Zuweisungstext | Status |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Aktiv |
| v3 | "Assign [generic] with title" | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3:
- "Assign task" → "Assign [generic param]" geändert
- "return of decision" → "return of decision table" geändert (klarere Terminologie)

**Empfehlung:** Verwenden Sie v3

---

### 🔄 DOKUMENTENSTEUERUNGS-CARDS

#### APPROVE
**Versionen:** v1, v2 (Aktuell)
**Änderung:** `trnsl_%approve_doc`-Übersetzungsschlüssel hinzugefügt
**Empfehlung:** Verwenden Sie v2

---

#### REJECT
**Versionen:** v1, v2 (Aktuell)
**Änderung:** `trnsl_%reject_doc`-Übersetzungsschlüssel hinzugefügt
**Empfehlung:** Verwenden Sie v2

---

#### STAUS_CHANGE (Statusänderung)
**Versionen:** v1, v2, v3 (Aktuell)

| Version | Workflow-Auslöser | Status |
|---------|-----------------|--------|
| v1 | ❌ Nein | Aktiv |
| v2 | ❌ Nein | Aktiv |
| v3 | ✅ Ja | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3: `trigger Workflows [param]` hinzugefügt – Automatisches Auslösen von Workflows bei Statusänderung
**Empfehlung:** Verwenden Sie v3

---

#### EXPORT
**Versionen:** v1, v2, v3 (Aktuell)

| Version | Validierung | Status |
|---------|------------|--------|
| v1 | ❌ Nein | Aktiv |
| v2 | ❌ Nein | Aktiv |
| v3 | ✅ Ja | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3: `Start Export with Validation: [param]` hinzugefügt
**Empfehlung:** Verwenden Sie v3

---

### 🧮 DATENMANIPULATIONS-CARDS

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Muster:** v1 → v2 (Übersetzungsschlüssel hinzugefügt)
**Empfehlung:** Verwenden Sie für alle v2

---

#### CONDITION_DECISION_TREE_DATA
**Versionen:** v2, v3 (Aktuell)

| Version | Datennutzung | Status |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Aktiv |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Aktuell |

**Was sich geändert hat:** v2 → v3: Explizitere Steuerung der Datenextraktion aus dem Decision Tree
**Empfehlung:** Verwenden Sie v3

---

### ❌ DEAKTIVIERTE CARDS (Nicht verwenden)

#### DOC_SUBORG_CHANGE
**Versionen:** v1, v2 (beide deaktiviert)
**Status:** Nicht mehr unterstützt
**Alternative:** Verwenden Sie die Funktionen zur Dokumentenzuweisung

---

#### RUN_SCRIPT
**Versionen:** v2, v3 (beide deaktiviert)
**Status:** Ersetzt durch ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternative:** Verwenden Sie ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Häufige Versionierungsmuster

### Muster 1: Einführung von Übersetzungsschlüsseln (v1 → v2)
**Betroffen:** 15+ Cards

**Änderung:** `trnsl_%[card_name]`-Übersetzungsschlüssel hinzugefügt
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Cards:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS und weitere
**Auswirkung:** Ermöglicht Mehrsprachenunterstützung

---

### Muster 2: Decision-Tree-Integration (v2 → v3) - VERALTET
**Betroffen:** 5 Cards (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Änderung:** Optionaler Decision-Tree-Parameter hinzugefügt
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Status:** ❌ Größtenteils veraltet (außer ACTION_DECISION_TREE_CREATE_TASKS)
**Grund:** Einfacherer Ansatz mit direkten Parametern bevorzugt

---

### Muster 3: Entwicklung zu generischen Typen (v3 → v4)
**Betroffen:** 4 Cards (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Änderung:** "Task" → generischer Typ-Parameter
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Auswirkung:** Unterstützt Task, Ticket, Issue und andere Arbeitselementtypen
**Vorteil:** Größere Flexibilität und Wiederverwendbarkeit

---

### Muster 4: Toleranzparameter (PO-Cards)
**Betroffen:** 6 Cards (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY usw.)

**Änderung:** Toleranz-/Abweichungsunterstützung hinzugefügt
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Beispiele:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Auswirkung:** Realistische Vergleichskriterien (nicht alle Werte müssen exakt übereinstimmen)

---

### Muster 5: Vergleichsmodus-Parameter
**Betroffen:** 3 Cards (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Änderung:** Flexible Auswahl der Vergleichsmethode hinzugefügt
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Auswirkung:** Unterstützung verschiedener Vergleichsalgorithmen

---

## ✅ Versionsempfehlungen

### Für neue Workflows
**Regel:** Verwenden Sie immer die höchste aktivierte Versionsnummer
- Bietet die neuesten Funktionen
- Beste Unterstützung
- Am gründlichsten getestet
- Empfohlener Ansatz

### Für bestehende Workflows
**Sicherer Ansatz:**
- Verwenden Sie weiterhin die aktuelle Version, wenn sie funktioniert
- Planen Sie eine schrittweise Migration zu neueren Versionen
- Testen Sie Upgrades zuerst in der Sandbox

### Migrationspriorität

| Priorität | Cards | Aktion |
|----------|-------|--------|
| **Hoch** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Upgrade auf aktuelle Version |
| **Mittel** | Andere v1/v2-Übersetzungs-Upgrades, PO-Cards v2/v3 | Upgrade in Erwägung ziehen |
| **Niedrig** | Cards ohne funktionale Änderungen | Optional |

---

## ⚠️ Veraltete Versionen – Nicht verwenden

| Card | Version | Grund | Stattdessen verwenden |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Sehr alt oder Decision Tree veraltet | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Decision-Tree-Ansatz veraltet | v4 |
| DOC_USER_ASSIGN | v3 | Decision-Tree-Ansatz veraltet | v2 |
| DOC_GROUP_ASSIGN | v3 | Decision-Tree-Ansatz veraltet | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Sehr alt | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Sehr alt | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funktionen zurückgesetzt | v3 |

---

## 🔄 Vollständig deaktivierte Cards – Nicht nutzbar

| Card | Versionen | Grund | Alternative |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Nicht mehr unterstützt | Cards zur Dokumentenzuweisung |
| RUN_SCRIPT | v2, v3 | Ersetzt durch DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Verwandte Dokumentation

- 📖 [Card Versioning Reference](../changelog/card-versioning.md) - Detaillierte Versionsinformationen
- 📚 [Workflow Guides](../) - Schrittweise Card-Nutzung
- 🔄 [Card Version Database](../docs/card_version.md) - Vollständiger Versionsverlauf
- 📋 [Workflow Logs](../workflow-logs/) - Ausführung und Fehlerbehebung

---

**Zuletzt aktualisiert:** 23. Oktober 2025
**Status:** Vollständiger Versionsverlauf
**Datenbankquelle:** postgres-dev-docflow
