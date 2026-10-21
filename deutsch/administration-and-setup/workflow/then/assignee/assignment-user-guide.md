# Dokumentenzuweisung und Benutzerkarten

## Dokumentenzuweisung und Benutzerkarten – Vollständiger Leitfaden

**Umfasst:** 13 aufgaben- und benutzerbezogene Karten

***

Die Karten auf dieser Seite gehören zur Gruppe **Then** des Workflow Builder – die Aktionen, die ausgeführt werden, sobald die Wenn/Und-Bedingungen übereinstimmen:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow-Builder"><figcaption><p>Karten werden über <strong>Add Card</strong> zur <strong>Then</strong>-Gruppe hinzugefügt.</p></figcaption></figure>

***

### 📌 Versionsinformationen

**Mehrversionskarten:** DOC\_USER\_ASSIGN (v2 aktuell, v3 veraltet), DOC\_GROUP\_ASSIGN (v2 aktuell, v3 veraltet), OC\_ASSIGN\_DOC (v2)

**Wichtig:** v3-Versionen haben Entscheidungsbaumunterstützung hinzugefügt, sind jetzt jedoch veraltet. **Empfehlung:** Verwenden Sie v2 sowohl für DOC\_USER\_ASSIGN als auch für DOC\_GROUP\_ASSIGN

📖 [Vollständiger Versionsverlauf](../../release.md) | [Kartenversionen und Verhalten](../../cards-overview/card-versions-guide.md)

***

## Grundlegende Dokumentzuweisung

### Karte: DOC\_USER\_ASSIGN / Dokument dem Benutzer zuweisen

#### Zweck

Weist das Dokument einer bestimmten Person für deren Aktion zu

#### Wann zu verwenden

* Das Dokument muss von einer bestimmten Person überprüft werden
* Übergabe an einzelnes Teammitglied
* Nachverfolgung der Verantwortlichkeit
* Weisen Sie der benannten Person Arbeit zu

#### Wie es funktioniert

```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

#### Beispiel

```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

#### Parameter

```
User: [Select which person]
```

#### Hinweis

Zuweisen bedeutet:

* Das Dokument wird für diese Person als „Mir zugewiesen“ angezeigt
* Diese Person ist verantwortlich
* Andere können das Dokument weiterhin sehen (jedoch nicht in der ihnen zugewiesenen Form)
* Jeweils eine Aufgabe pro Dokument

***

### Karte: DOC\_GROUP\_ASSIGN / Dokument einer Gruppe zuordnen

#### Zweck

Weist das Dokument einer Gruppe zu (alle Mitglieder sehen es als ihnen zugewiesen)

#### Wann zu verwenden

* Dokument für das Team, nicht für Einzelpersonen
* Mehrere Personen können damit umgehen
* Geteilte Verantwortung
* Arbeitslastverteilung im Team

#### Wie es funktioniert

```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

#### Beispiel

```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

#### Parameter

```
Group: [Select which group]
```

#### Unterschied

```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

***

### Karte: ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE

#### Zweck

Weist ein Dokument basierend auf der Entscheidungstabellenlogik zu

#### Wann zu verwenden

* Unterschiedliche Lieferanten benötigen unterschiedliche Handler
* Zuordnung nach Betrag
* Komplexe Routing-Logik
* Mehrere Bedingungen für die Zuweisung

#### Wie es funktioniert

```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

#### Beispiel: Betragsmäßige Abtretung

```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

#### Beispiel: Lieferantenbasierte Zuordnung

```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

#### Parameter

```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

***

### Karte: ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL

#### Zweck

Ordnet Dokumente der Reihe nach basierend auf der Entscheidungstabelle mit Prioritäten zu

#### Wann zu verwenden

* Mehrere aufeinanderfolgende Genehmigungen
* Unterschiedliche Menschen auf unterschiedlichen Ebenen
* Genehmigungskette basierend auf Betrag
* Eskalationspfad

#### Wie es funktioniert

```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

#### Prioritätssystem

```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

#### Beispiel: Mehrstufige Genehmigung

```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

#### Parameter

```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL

#### Zweck

Weist das Dokument dem Benutzer mit fortlaufender Priorität zu

#### Wann zu verwenden

* Das Dokument benötigt eine bestimmte Person
* Klare sequentielle Verarbeitung
* Einzelauftrag mit Bestellung

#### Wie es funktioniert

```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

#### Beispiel

```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL

#### Zweck

Ordnet Dokumente nacheinander Gruppen zu

#### Wann zu verwenden

* Mehrere Gruppengenehmigungen
* Unterschiedliche Abteilungen in jeder Phase
* Teambasierte sequentielle Bearbeitung

#### Wie es funktioniert

```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

#### Beispiel

```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP

#### Zweck

Weist das Dokument einer bestimmten Einrichtungsgruppe zu

#### Wann zu verwenden

* Dokument für ein bestimmtes Lager/eine bestimmte Einrichtung
* Anlagenbasierter Betrieb
* Standortbezogene Verarbeitung

#### Beispiel

```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Zweck

Weist einrichtungsübergreifend nacheinander zu

#### Wann zu verwenden

* Verarbeitung an mehreren Standorten
* Der Versand erfolgt über Einrichtungen
* Standortbasierter Workflow

#### Beispiel

```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP

#### Zweck

Weist das Dokument der Beschaffungsabteilung zu

#### Wann zu verwenden

* Abwicklung durch das Beschaffungsteam
* Lieferantenbezogene Arbeiten
* Bestellbezogen

#### Beispiel

```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

***

### Karte: ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Zweck

Sequentielle Zuordnung innerhalb der Beschaffung

#### Wann zu verwenden

* Mehrstufiger Beschaffungsprozess
* Genehmigungskette im Einkauf

#### Beispiel

```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

***

### Karte: ACTION\_CHANGE\_DOC\_SUBORG / Unterorganisation des Dokuments ändern

#### Zweck

Weist das Dokument einer anderen Unterorganisation zu

#### Wann zu verwenden

* Falsche Organisation ausgewählt
* Muss in die richtige Abteilung wechseln
* Organisatorische Umstrukturierung

#### Wie es funktioniert

```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

#### Beispiel

```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

***

### Karte: ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT

#### Zweck

Ändert die Unterorganisation basierend auf dem Dokumentfeldwert

#### Wann zu verwenden

* Im Feld gespeicherte Unterorganisation
* Ordnen Sie den Speicherort des Dokuments dem Feld zu
* Automatische Organisationszuweisung

#### Wie es funktioniert

```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

#### Beispiel

```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

***

### Karte: ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Zweck

Weist dem Benutzer ein Dokument aus dem Feld zu, mit Fallback, wenn der Benutzer nicht gefunden wird

#### Wann zu verwenden

* Im Dokumentfeld gespeicherter Benutzername
* Möglicherweise nicht im System vorhanden
* Backup erforderlich, wenn der Benutzer nicht verfügbar ist

#### Wie es funktioniert

```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

#### Parameter

```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

#### Beispiel

```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

***

### Karte: ACTION\_ASSIGN\_USER\_TO\_SUPPLIER

#### Zweck

Weist das Dokument dem Benutzer zu, der diesen Lieferanten verwaltet

#### Wann zu verwenden

* Benutzer mit Lieferant verknüpft
* Lieferanten-Account-Manager
* Eigentümer der Lieferantenbeziehung

#### Wie es funktioniert

```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

***

## Zuweisungsentscheidungsbäume

### Entscheidungstabelle Beispiel 1: Betragsbasiert

```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

### Entscheidungstabelle Beispiel 2: Lieferantenbasiert

```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

### Entscheidungstabelle Beispiel 3: Dokumenttypbasiert

```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

***

## Beispiele für Zuweisungsworkflows

### Beispiel 1: Einfaches Routing

```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

### Beispiel 2: Sequentielle Genehmigung

```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

### Beispiel 3: Betragsbasiertes Routing

```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

### Beispiel 4: Einrichtungsbasiert

```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

***

## Best Practices für Aufgaben

✅ **Do:**

* Halten Sie Entscheidungstabellen einfach
* Testen Sie die Routing-Logik mit Beispielen
* Stellen Sie sicher, dass alle Wege irgendwohin führen
* Haben Sie einen Ersatz für fehlende Benutzer
* Entscheidungen zur Dokumentenweiterleitung

❌ **Nicht:**

* Zirkuläre Aufgaben erstellen (A→B→A)
* Nicht vorhandenen Benutzern zuweisen (ohne Fallback)
* Machen Sie das Routing zu komplex
* Vergessen Sie, das Routing zu testen
* Nicht verfügbaren Personen zuweisen

***

## Aufgabe zur Fehlerbehebung

### „Dokument nicht zugeordnet“

**Ursache:** Bedingung nicht erfüllt oder Benutzer existiert nicht

**Lösung:**

* Überprüfen Sie, ob die Bedingung wahr ist
* Überprüfen Sie, ob der Benutzer im System vorhanden ist
* Überprüfen Sie die Fallback-Einstellungen
* Überprüfen Sie die Logik der Entscheidungstabelle

### „Falsche Person zugewiesen“

**Ursache:** Entscheidungstabelle oder Routing-Logik falsch

**Lösung:**

* Testentscheidungstabelle
* Konditionen prüfen
* Überprüfen Sie die Benutzerzuordnung
* Überprüfen Sie die Feldwerte

### „Aufgabe scheint jemanden zu überspringen“

**Ursache:** Reihenfolge falsch

**Lösung:**

* Überprüfen Sie die Prioritätsnummern
* Überprüfen Sie, ob die Reihenfolge korrekt ist
* Mit Probe testen
* Überprüfen Sie die Reihenfolge der Entscheidungstabellen

***

## Vergleich der Aufgabenkarten

| Karte                                                    | Weist zu               | Routentyp  | Anwendungsfall                   |
| ------------------------------------------------------- | ------------------------ | ----------- | -------------------------- |
| DOC\_USER\_ASSIGN                                       | Individuell               | Direkt      | Einfache Zuordnung          |
| DOC\_GROUP\_ASSIGN                                      | Gruppe                    | Direkt      | Teamzuordnung            |
| ACTION\_ASSIGN\_DOC\_BASED\_ON\_DECISION\_TABLE         | Entscheidungsergebnis          | Bedingt | Komplexes Routing            |
| ACTION\_ASSIGN\_DOC\_DECISION\_TABLE\_SEQUENTIAL        | Mehrere (sequentiell)    | Bedingt | Genehmigungskette             |
| ACTION\_ASSIGN\_DOC\_TO\_USER\_SEQUENTIAL               | Benutzer (sequentiell)        | Bestellt     | Sequentielle Benutzerschritte      |
| ACTION\_ASSIGN\_DOC\_TO\_GROUP\_SEQUENTIAL              | Gruppen (sequentiell)      | Bestellt     | Sequentielle Gruppenschritte     |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP                | Einrichtungsgruppe           | Direkt      | Einrichtungsspezifisch          |
| ACTION\_ASSIGN\_DOC\_TO\_FACILITY\_GROUP\_SEQUENTIAL    | Einrichtungen (sequentiell)  | Bestellt     | Multi-Einrichtung             |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP             | Beschaffung              | Direkt      | Beschaffungsworkflow       |
| ACTION\_ASSIGN\_DOC\_TO\_PROCUREMENT\_GROUP\_SEQUENTIAL | Beschaffung (sequenziell) | Bestellt     | Beschaffungsgenehmigungskette |
| ACTION\_CHANGE\_DOC\_SUBORG                             | Unterorganisation         | Direkt      | Abteilungswechsel          |
| ACTION\_CHANGE\_DOC\_SUBORG\_BY\_FIELD\_TEXT            | Unterorganisation nach Feld         | Bedingt | Feldbezogene Zuordnung     |
| ACTION\_ASSIGN\_USER\_FROM\_FIELD\_WITH\_FALLBACK       | Feld/Fallback           | Bedingt | Dynamische Benutzerzuweisung    |

***

## Verwandte Karten

* **ACTION\_CREATE\_TASK\_FOR\_USER** – Aufgabe derselben Person zuweisen
* **ACTION\_SEND\_EMAIL** – Zugeordnete Person benachrichtigen
* **CONDITION\_USER\_IS\_ISNOT** – Überprüfen Sie, ob die richtige Person zugewiesen ist
* **CONDITION\_GROUP\_IS\_ISNOT** – Überprüfen Sie, ob die richtige Gruppe zugewiesen ist
