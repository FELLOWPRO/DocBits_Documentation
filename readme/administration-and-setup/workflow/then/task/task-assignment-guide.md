# Aufgabenzuweisungs- und Erstellungskarten

## Aufgabenzuweisungs- und Erstellungskarten – Vollständiger Leitfaden

**Umfasst:** 12 aufgabenbezogene Karten

***

Die Aufgabenkarten auf dieser Seite gehören zur Gruppe **Dann** des Workflow Builder – die Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-de.png" alt="Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus."><figcaption><p>Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus.</p></figcaption></figure>

***

### 📌 Versionsinformationen

**Am weitesten entwickelte Karte:** tasks\_create (4 Versionen, neueste Version 4) **Andere Karten mit mehreren Versionen:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Wichtige Änderungen:**

* **v3 → v4 Evolution:** Entscheidungsbaum-Ansatz entfernt, generische Arbeitselementtypen hinzugefügt (Aufgabe, Ticket, Problem)
* **v2 → v3 Migration:** Entscheidungsbaumunterstützung hinzugefügt (jetzt größtenteils veraltet)

📖 [Vollständiger Versionsverlauf](../../release.md) | [Kartenversionen und Verhalten](../../cards-overview/card-versions-guide.md)

***

### Übersicht

Aufgabenkarten erstellen Arbeitsaufträge für Teammitglieder. Wenn eine Rechnung genehmigt werden muss, können Sie automatisch eine Aufgabe erstellen und diese der richtigen Person zuweisen.

***

## Grundlegende Aufgabenerstellung

### Karte: tasks\_create / Aufgabe erstellen und dem Benutzer zuweisen

#### Zweck

Erstellt eine Aufgabe und weist sie einer bestimmten Person zu

#### Wann zu verwenden

* Die Rechnung muss von einer bestimmten Person überprüft werden
* Genehmigung der benannten Person erforderlich
* Übergabe an ein bestimmtes Teammitglied

#### Parameter

**Titel** Der Name/Betreff der Aufgabe

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Beschreibung** Details zur Aufgabe

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priorität**

* 🔴 **Hoch**: Dringend, sofort erledigen
* 🟡 **Mittel**: Normale Priorität
* 🟢 **Niedrig**: Kann später durchgeführt werden

**Zugewiesener Benutzer** Wer erhält die Aufgabe?

```
Example: John Smith (Finance Manager)
```

**E-Mail-Benachrichtigung** E-Mail-Benachrichtigung an zugewiesene Person senden?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Beispiel

```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

***

### Karte: ACTION\_TASK\_FOR\_GROUP / Aufgabe für Gruppe erstellen

#### Zweck

Erstellt eine Aufgabe und weist sie einer Gruppe zu (alle Mitglieder können sie sehen)

#### Wann zu verwenden

* Mehrere Personen können die Aufgabe erledigen
* Aufgabe für das Team, nicht für Einzelpersonen
* Die erste verfügbare Person sollte sich darum kümmern

#### Unterschied zur Einzelaufgabe

```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

#### Beispiel-Workflow

```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

***

### Karte: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Zweck

Erstellt Aufgaben basierend auf der Entscheidungstabellenlogik

#### Wie es funktioniert

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Wann zu verwenden

* Unterschiedliche Lieferanten benötigen unterschiedliche Genehmigungen
* Komplexes Routing basierend auf mehreren Faktoren
* Unterschiedliches Team je nach Dokumenttyp

#### Beispiel

```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

***

### Karte: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Zweck

Erstellt Aufgaben nacheinander auf der Grundlage der Entscheidungstabelle. Aufgaben werden einzeln nach Priorität zugewiesen

#### Wann zu verwenden

* Mehrere Genehmigungen nacheinander erforderlich
* Workflow-Genehmigungskette
* Jede Person überprüft und geht dann zur nächsten Person über

#### Wie es funktioniert

```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

#### Prioritätssystem

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Beispielkonfiguration

```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

***

### Karte: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Zweck

Weist das Dokument einem Benutzer zu UND erstellt eine sequentielle Aufgabe

#### Wann zu verwenden

* Dokument zuweisen UND gleichzeitig Aufgabe erstellen
* Das Dokument muss von einer bestimmten Person überprüft werden
* Verfolgen Sie sowohl die Aufgabenerstellung als auch die Aufgabenerstellung

#### Wie es funktioniert

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Beispiel

```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

***

### Karte: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Zweck

Weist das Dokument einer Gruppe zu UND erstellt eine Aufgabe

#### Wann zu verwenden

* Das Dokument erfordert die Aufmerksamkeit der Gruppe
* Sie möchten die Aufgabenerstellung verfolgen
* Erstellen Sie die erste Aufgabe und dokumentieren Sie dann die Zuweisung

#### Beispiel

```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

***

## Erweiterte Aufgabenerstellung

### Karte: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Zweck

Erstellt eine Aufgabe für eine bestimmte Einrichtungsgruppe

#### Wann zu verwenden

* Aufgabe für das Lager-/Facility-Team
* Einrichtungsspezifische Vorgänge
* Der physische Standort ist wichtig

#### Beispiel

```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

***

### Karte: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Zweck

Sequentielle Aufgabenzuweisung über Einrichtungen hinweg

#### Wann zu verwenden

* Betrieb mit mehreren Einrichtungen
* Aufgaben werden von Einrichtung zu Einrichtung weitergegeben
* Sequentielle Anlagenverarbeitung

#### Wie es funktioniert

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Beispiel

```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

***

### Karte: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Zweck

Erstellt eine Aufgabe für die Beschaffungsabteilung

#### Wann zu verwenden

* Aufgabe für das Beschaffungsteam
* Aufgaben im Lieferantenmanagement
* Kaufbezogene Arbeiten

#### Beispiel

```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

***

### Karte: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Zweck

Sequentielle Aufgabenverteilung innerhalb der Beschaffung

#### Wann zu verwenden

* Mehrstufige Beschaffungsprozesse
* Genehmigungskette im Einkauf
* Eskalationspfad

#### Beispiel

```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

***

### Karte: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Zweck

Benutzer aus Dokumentfeld abrufen, Aufgabe zuweisen. Wenn Benutzer nicht gefunden wird, Ersatzbenutzer verwenden

#### Wann zu verwenden

* Benutzer im Dokumentfeld gespeichert
* Das Dokument legt fest, wer prüfen soll
* Halten Sie eine Ersatzperson bereit, wenn der angegebene Benutzer nicht verfügbar ist

#### Wie es funktioniert

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Beispiel

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parameter

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Allgemeine Aufgabenparameter

Alle Aufgabenkarten verwenden diese Parameter:

#### Titel

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Beschreibung

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Prioritätsstufen

```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

#### Fälligkeitsdatum (falls verfügbar)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Aufgaben-Workflow-Szenarien

### Szenario 1: Einfache Genehmigung

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Szenario 2: Mehrstufige Genehmigung

```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

### Szenario 3: Parallele Aufgaben

```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

### Szenario 4: Bedingtes Routing

```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

***

## Best Practices für die Aufgabenzuweisung

✅ **Do:**

* Geben Sie im Aufgabentitel spezifische Details an
* Legen Sie geeignete Prioritätsstufen fest
* Setzen Sie realistische Fristen
* Benachrichtigen Sie die Beauftragten
* Fügen Sie einen Link zum Dokument hinzu
* Verwenden Sie klare, umsetzbare Beschreibungen

❌ **Nicht:**

* Erstellen Sie vage Aufgabentitel („Review this“)
* Stellen Sie alles auf „Hohe Priorität“.
* Vergessen Sie, die zugewiesene Person zu benachrichtigen
* Erstellen Sie mehrere Aufgaben für dieselbe Arbeit
* Nicht verfügbaren Personen zuweisen

***

## Aufgaben zur Fehlerbehebung

### „Aufgabe ist niemandem zugewiesen“

**Ursache:** Benutzer existiert nicht oder Gruppe ist leer

**Lösung:**

* Überprüfen Sie die Schreibweise des Benutzernamens
* Überprüfen Sie, ob der Benutzer im System aktiv ist
* Überprüfen Sie, ob die Gruppe Mitglieder hat
* Verwenden Sie bei Bedarf einen Fallback

### „Person sagt, sie habe keine Benachrichtigung erhalten“

**Ursache:** E-Mail-Benachrichtigung deaktiviert oder E-Mail falsch

**Lösung:**

* Überprüfen Sie, ob das Kontrollkästchen „E-Mail senden“ aktiviert ist
* Überprüfen Sie die E-Mail-Adresse des Empfängers
* Überprüfen Sie den Spam-Ordner
* Benachrichtigung manuell erneut senden

### „Die falsche Person hat die Aufgabe bekommen“

**Ursache:** Routing-Logik falsch

**Lösung:**

* Überprüfen Sie die Bedingungen der Entscheidungstabelle
* Überprüfen Sie die Fallback-Einstellungen
* Testen Sie mit Beispieldokument
* Überprüfen Sie die Benutzernamen auf Tippfehler

### „Zu viele Aufgaben erstellt“

**Ursache:** Karte wird mehrmals ausgelöst

**Lösung:**

* Die Prüfbedingungen sind spezifisch genug
* Stellen Sie sicher, dass die Karte nur einmal pro Dokument ausgeführt wird
* Überprüfen Sie die „Und“-Bedingungen
* Fügen Sie zusätzliche Filter hinzu

***

## Vergleichstabelle der Aufgabenkarten

| Karte                                                        | Erstellt eine Aufgabe | Weist zu            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Ja          | Individuell            | Immer      |
| ACTION\_TASK\_FOR\_GROUP                                    | Ja          | Gruppe                 | Immer      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Ja          | Ergebnis der Entscheidungstabelle | Bedingt |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Ja          | Mehrere (sequentiell) | Bedingt |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Ja          | Benutzer + Dokument       | Bedingt |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Ja          | Gruppe + Dokument      | Bedingt |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Ja          | Einrichtungsgruppe        | Bedingt |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Ja          | Mehrere Einrichtungen   | Bedingt |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Ja          | Beschaffungsteam      | Bedingt |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Ja          | Mehrere (sequentiell) | Bedingt |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Ja          | Feld/Fallback        | Bedingt |

***

## Verwandte Karten

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Dokument zuweisen, ohne Aufgabe zu erstellen
* **ACTION\_SEND\_EMAIL** – Personen direkt benachrichtigen
* **STAUS\_CHANGE** – Status ändern statt Aufgabe erstellen
* **RUN\_WORKFLOW** – Lösen Sie stattdessen einen anderen Workflow aus
