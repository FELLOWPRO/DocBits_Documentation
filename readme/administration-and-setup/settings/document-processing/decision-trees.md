# Entscheidungsbäume

{% embed url="https://youtu.be/omFWSkSjlL0" %}
So erstellen Sie einen Entscheidungsbaum in DocBits (Bedingungen, Policies, Testen & Export)
{% endembed %}

## Überblick

Entscheidungsbäume sind eine leistungsstarke Funktion, die eine automatisierte Weiterleitung und Entscheidungsfindung auf Basis vordefinierter Regeln ermöglicht. Diese Funktion ist besonders nützlich in komplexen Umgebungen, in denen verschiedene Bedingungen ausgewertet werden müssen, um die richtige Vorgehensweise zu bestimmen, etwa das Zuweisen von Preisen, das Ermitteln von Mengen oder das Weiterleiten von Dokumenten.

#### Wichtige Komponenten

* **Entscheidungsbaum-Liste**: Dies ist die zentrale Oberfläche, in der alle vorhandenen Entscheidungsbäume aufgelistet werden. Jeder Entscheidungsbaum kann einem bestimmten Dokumenttyp zugeordnet werden, etwa einer `INVOICE` oder einem `QUOTE`.
* **Entscheidungsbaum-Designer**: Diese Oberfläche ermöglicht das Erstellen und Bearbeiten von Entscheidungsbäumen. Hier können Sie Regeln, Operatoren und Aktionen definieren, die ausgeführt werden, wenn bestimmte Bedingungen erfüllt sind.

## Entscheidungsbaum-Oberfläche

#### Entscheidungsbaum-Liste

Die Entscheidungsbaum-Liste zeigt alle konfigurierten Entscheidungsbäume an. Öffnen Sie sie über **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Liste der Entscheidungsbäume"><figcaption><p>Die Liste der Entscheidungsbäume</p></figcaption></figure>

Jeder Eintrag zeigt:

| Spalte | Beschreibung |
|--------|-------------|
| **Name** | Der Name des Entscheidungsbaums. Klicken Sie darauf, um den Designer zu öffnen. |
| **Document Type** | Der Dokumenttyp, für den der Baum gilt (z. B. `INVOICE`, `QUOTE`). |
| **Last Modified By** | Der Benutzer, der den Baum zuletzt bearbeitet hat. |
| **Last Modified At** | Zeitstempel der letzten Änderung. |
| **Actions** | Drei-Punkte-Menü zum Bearbeiten, Kopieren, Exportieren oder Löschen des Baums. |

#### Einen Entscheidungsbaum erstellen

1. Klicken Sie oben rechts auf **+ Add Decision Tree**.
2. Geben Sie einen **Name** ein und wählen Sie den **Document Type** aus.
3. Verwenden Sie den Entscheidungsbaum-Designer (siehe unten), um Bedingungen, Policies und Ergebnisse zu definieren.

#### Einen Entscheidungsbaum importieren

Klicken Sie auf **Import Decision Tree**, um eine zuvor exportierte Entscheidungsbaum-Datei (im JSON-Format) hochzuladen. Dies ist hilfreich, um einen Baum zwischen Organisationen oder Umgebungen zu kopieren.

## Entscheidungsbaum-Designer

Der Entscheidungsbaum-Designer ermöglicht es Ihnen, Regeln zu konfigurieren, die festlegen, wie Entscheidungen getroffen werden.

### **Komponenten des Entscheidungsbaum-Designers**

* **Rules**: Jede Regel besteht aus Bedingungen und Aktionen.
* **Select Source**: Über dieses Dropdown geben Sie das auszuwertende Quellfeld an.
* **Select Operator**: Definiert den Logikoperator (z. B. `<=`, `>=`, `=`, `!=`), der auf das Quellfeld angewendet wird.
* **Result**: Definiert das Ergebnis oder die Aktion, die ausgeführt werden soll, wenn die Bedingungen erfüllt sind.
* **Add New Row**: Ermöglicht es Ihnen, weitere Regeln zum Entscheidungsbaum hinzuzufügen.

### Beispiel für eine Entscheidungsbaum-Konfiguration

Dieser Entscheidungsbaum wertet das Feld **Total Amount** aus und ordnet es auf Basis vordefinierter Bedingungen verschiedenen Gruppen zu. Jede Regel vergleicht den Gesamtbetrag mit einem bestimmten Wert, und je nachdem, welche Bedingung wahr ist, wird die entsprechende **Group** zurückgegeben.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Entscheidungsbaum-Beispiel Total Amount"><figcaption></figcaption></figure>

Dieser Entscheidungsbaum wertet zwei zentrale Bedingungen aus, um zu bestimmen, welche Gruppe zugewiesen werden soll: **Total Amount** und **Warehouse Status**. Der Baum verwendet Schwellenwerte auf Basis des Gesamtbetrags, um festzulegen, welche Gruppe zurückgegeben wird, mit der zusätzlichen Unterscheidung, ob das Lager als „Warehouse Main", „Warehouse Sub" oder „Not Warehouse Main" gekennzeichnet ist.

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Entscheidungsbaum-Beispiel Warehouse Status"><figcaption></figcaption></figure>

Jede Regel wird nacheinander ausgewertet.

## Entscheidungsbaum-Policy

Die Entscheidungsbaum-Policy legt fest, wie mehrere Regeln innerhalb eines Entscheidungsbaums verarbeitet werden. Sie können aus mehreren Policies wählen:

### **1. Unique-Policy**

Stellt sicher, dass nur eine einzige Regel zutrifft. Wenn mehrere Regeln zutreffen, gibt der Entscheidungsbaum „false" zurück.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)
* **Regel 3**: Total Amount <= 5000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 3000 (trifft zu)

Da mehrere Regeln zutreffen (**Regel 2**, **Regel 3**, **Regel 4**, **Regel 5**), gibt der Entscheidungsbaum **false** zurück, weil die **Unique**-Policy sicherstellt, dass nur eine einzige Regel zutreffen darf.

### **2. First-Policy**

Die erste zutreffende Regel wird angewendet, und es werden keine weiteren Regeln ausgewertet.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu) → Der Entscheidungsbaum beendet die Auswertung weiterer Regeln und wendet **GROUP_2** an.

### **3. Priority-Policy**

Mit dieser Option können Sie für jede Regel Prioritäten festlegen. Je niedriger die gewählte Zahl, desto höher die Priorität (d. h. Priorität 1 hat die höchste Priorität). Die Regeln werden anhand ihrer Prioritätsreihenfolge ausgewertet. Die zutreffende Regel mit der höchsten Priorität wird angewendet.

**Beispiel:**

<table><thead><tr><th width="137">Regel</th><th width="110">Priorität</th><th width="268">Bedingung</th><th>Rückgabegruppe</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Da die Priorität in der Reihenfolge **5, 4, 3, 2, 1** angewendet wird, ist die zutreffende Regel mit der höchsten Priorität **Regel 5** (**GROUP_5**). Der Entscheidungsbaum gibt **GROUP_5** zurück, weil **Regel 5** die höchste Priorität hat (Priorität 1).

### **4. Collect-(sum)-Policy**

Diese Policy sammelt alle zutreffenden Regeln und summiert die Ergebnisse. Sie funktioniert nur für **Return Type Value**.

**Beispiel:**

| Regel | Bedingung            | Rückgabewert |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Für den Eingabewert **Total Amount = 3500** würde die Auswertung der Regeln wie folgt aussehen:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu, Rückgabewert = 3)
* **Regel 4**: Total Amount <= 4000 (trifft zu, Rückgabewert = 4)
* **Regel 5**: Total Amount <= 5000 (trifft zu, Rückgabewert = 5)

Da die **Collect-(sum)**-Policy angewendet wird, summieren wir die **Rückgabewerte** der zutreffenden Regeln, also **3, 4, 5**.

**Die Summe dieser Werte** ergibt:

* 5 + 4 + 3 = **12**

Das vom Entscheidungsbaum zurückgegebene Ergebnis wäre somit **12**, also die Summe aller zutreffenden Rückgabewerte.

### **5. Collect-(min/max/count)-Policy**

Diese Policy sammelt alle zutreffenden Regeln und wählt entweder das **Minimum**, das **Maximum** oder **zählt** die Vorkommen. Sie funktioniert nur für **Return Type Value**.

**Beispiel:**

| Regel | Bedingung            | Rückgabewert |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Wenn die Option **Collect (min)** ausgewählt ist, gibt das Ergebnis das **Minimum** der **Rückgabewerte** der zutreffenden Regeln zurück.
   * Für den Eingabewert **Total Amount = 3500** würde die Auswertung der Regeln wie folgt aussehen:
     * **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
     * **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
     * **Regel 3**: Total Amount <= 3000 (trifft zu, Rückgabewert = 3)
     * **Regel 4**: Total Amount <= 4000 (trifft zu, Rückgabewert = 4)
     * **Regel 5**: Total Amount <= 5000 (trifft zu, Rückgabewert = 5)
   * Die **zutreffenden Regeln** sind Regel 3, Regel 4 und Regel 5 mit **Rückgabewerten** von **3, 4 und 5**.
   * Da die **Collect-(min)**-Policy angewendet wird, ist das Ergebnis der **Minimalwert**, also **3**.
   * **Ergebnis**: **3**
2. Wenn die Option **Collect (max)** ausgewählt ist, gibt das Ergebnis das **Maximum** der **Rückgabewerte** der zutreffenden Regeln zurück.
   * Bei derselben Auswertung wie oben lautet das Ergebnis:
   * **Ergebnis**: **5**
3. Wenn die Option **Collect (count)** ausgewählt ist, zählt das Ergebnis die **Anzahl der zutreffenden Regeln**.
   * Bei derselben Auswertung wie oben lautet das Ergebnis:
   * **Ergebnis**: **3** (da 3 Regeln zutreffen).

### **6. Rule-Order-Policy**

Diese Policy wendet die Regeln in der Reihenfolge an, in der sie im Entscheidungsbaum erscheinen, und gibt das Ergebnis der zuerst zutreffenden Regel zurück.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Bei dem Eingabewert **Total Amount = 3500** würde die Auswertung der Regeln wie folgt aussehen:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Bei **Rule Order** verarbeitet der Baum die Regeln in der Reihenfolge, in der sie aufgeführt sind. Die zutreffenden Regeln sind also:

* **Regel 3**: GROUP_3
* **Regel 4**: GROUP_4
* **Regel 5**: GROUP_5

**Ergebnis**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Any-Policy**

Mehrere Regeln können wahr sein, aber das Ergebnis dieser Regeln muss identisch sein.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Wenn der Gesamtbetrag **2500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
* **Regel 3**: Total Amount <= 3000 (trifft zu)
* **Regel 4**: Total Amount <= 4000 (trifft zu)
* **Regel 5**: Total Amount <= 5000 (trifft zu)

Damit **Any** angewendet wird, müssen alle zutreffenden Regeln dieselbe **Group** zurückgeben. Da die Gruppen über die verschiedenen Regeln hinweg nicht übereinstimmen, wäre das Ergebnis **false**.

### **8. First-&-Adjacent-Policy**

Wählt das Ergebnis der Regel, die der ersten zutreffenden Regel benachbart ist.

**Beispiel:**

| Regel | Bedingung            | Rückgabegruppe |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Wenn der Gesamtbetrag **1500** ist, werden die Regeln wie folgt ausgewertet:

* **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
* **Regel 2**: Total Amount <= 2000 (trifft zu)

Da **Regel 2** die erste zutreffende Regel ist, würde **First & Adjacent** das Ergebnis von **Regel 3** anwenden: **GROUP_3**.

## **Den Entscheidungsbaum testen**

**Überblick:**
Der Entscheidungsbaum-Designer enthält eine Testfunktion, um die Logik der konfigurierten Regeln zu validieren. Mit dieser Funktion können Benutzer den Entscheidungsbaum testen, indem sie für die ausgewählten Felder bestimmte Eingabewerte angeben.

**Schritte zur Nutzung der Testfunktion:**

1.  **Den Test-Button finden:**

    * Suchen Sie im Entscheidungsbaum-Designer die Schaltfläche **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Entscheidungsbaum Test-Button" width="563"><figcaption></figcaption></figure>
2.  **Das Test-Popup öffnen:**

    * Klicken Sie auf die Schaltfläche **Test**.
    * Es erscheint ein Popup-Fenster mit Eingabefeldern, die den im Entscheidungsbaum verwendeten Kriterien entsprechen.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Entscheidungsbaum Test-Popup" width="421"><figcaption></figcaption></figure>
3. **Eingabewerte angeben:**
   *   Geben Sie Werte in die Eingabefelder ein, um ein reales Szenario zu simulieren.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Entscheidungsbaum Testeingabe" width="428"><figcaption></figcaption></figure>
4.  **Die Ergebnisse auswerten:**

    * Nach der Eingabe verarbeitet der Baum die Werte auf Basis der gewählten Policy.
    * Das System hebt die Regel(n) hervor, die den angegebenen Eingaben entsprechen.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Entscheidungsbaum Testergebnis" width="563"><figcaption></figcaption></figure>
5. **Rückmeldung bei fehlender Übereinstimmung prüfen:**
   * Wenn keine Regel hervorgehoben wird, zeigt das System eine Rückmeldung an, die erläutert, warum keine Regel zutraf.
   * Nutzen Sie diese Rückmeldung, um die Eingaben anzupassen oder die Konfiguration des Baums auf mögliche Probleme zu überprüfen.

## Export und Speichern

* **Save**: Speichert die aktuelle Konfiguration des Entscheidungsbaums.
* **Export**: Ermöglicht es Ihnen, die Konfiguration des Entscheidungsbaums zu exportieren, die anschließend in eine andere Umgebung importiert oder für Sicherungszwecke verwendet werden kann.

## Anwendungsfälle

* **Genehmigungs-Workflows** — Rechnungen je nach Betragsschwellen an verschiedene Genehmiger weiterleiten (zum Beispiel erfordern Beträge über 10.000 die Genehmigung durch einen Manager).
* **Validierungsregeln** — Feldwerte automatisch validieren und Dokumente markieren, die die konfigurierten Kriterien nicht erfüllen.
* **Sequenzielle Zuweisung** — Dokumente auf Basis von Bedingungen Benutzern in einer bestimmten Reihenfolge zuweisen.
