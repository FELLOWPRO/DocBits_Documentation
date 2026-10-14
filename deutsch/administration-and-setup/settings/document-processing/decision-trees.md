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

* [Einzigartig](decision-trees/unique-policy.md)
* [Erste](decision-trees/first-policy.md)
* [Priorität](decision-trees/priority-policy.md)
* [Sammeln (Summe)](decision-trees/collect-sum-policy.md)
* [Sammeln (Min/Max/Zählen)](decision-trees/collect-min-max-count-policy.md)
* [Regel Bestellung](decision-trees/rule-order-policy.md)
* [Irgendeine](decision-trees/any-policy.md)
* [Erste & Angrenzende](decision-trees/first-and-adjacent-policy.md)

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
