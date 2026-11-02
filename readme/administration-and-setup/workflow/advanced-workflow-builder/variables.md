# Variablen

Mit **Variablen** speichern Sie Werte einmal und verwenden sie über die Knoten eines Advanced Workflows hinweg wieder — zum Beispiel einen Schwellenwert, einen festen Empfänger oder einen Wert, den Sie aus dem Dokument lesen und an einen späteren Knoten weitergeben. Öffnen Sie das Variablen-Panel über die Schaltfläche **Variables** (das `{ }`-Symbol) in der Symbolleiste.

<figure><img src="../../../.gitbook/assets/workflow_advanced_variables.png" alt="Variablen-Panel nach Typ gruppiert mit einer Schaltfläche New Variable"><figcaption><p>Das Variables-Panel — Variablen nach Typ gruppiert, mit Suche und <strong>New Variable</strong>.</p></figcaption></figure>

## Variablentypen

Variablen werden nach ihrem Typ gruppiert:

- **Text** — ein Zeichenkettenwert (z. B. eine Beschreibung oder eine feste Bezeichnung).
- **Number** — ein numerischer Wert, etwa ein Schwellenwert ohne Währungssymbol.
- **Yes/No** — ein boolesches Kennzeichen (Yes / No).
- **Document** — eine Dokumentreferenz, die eine geeignete Workflow-Aktion setzt; das Formular nimmt keinen eingegebenen Dokument-Standardwert an.

Verwenden Sie das Suchfeld, um eine Variable schnell zu finden, wenn die Liste wächst.

## Eine Variable erstellen

Klicken Sie auf **New Variable**, geben Sie ihr einen Namen und einen Typ und legen Sie ihren Wert fest. Die Variable steht dann zur Verwendung in den Karten Ihrer Knoten zur Verfügung, sodass Sie die Konfiguration an einem Ort halten und ändern können, ohne jeden Knoten einzeln zu bearbeiten.

## Nächste Schritte

- Sehen Sie, wie Knoten diese Werte verwenden, unter [Knoten](nodes.md).
- Validieren und starten Sie den Workflow unter [Validierung & Test](validation-and-testing.md).

## Datenumfang und Speichern

Variablen gelten für die **Organisation**. Anlegen, Bearbeiten und Löschen werden sofort auf dem Server gespeichert. Andere Workflows können dieselben Werte verwenden. Speichern oder Verwerfen des Canvas macht diese Änderungen nicht rückgängig. Verwenden Sie für pro Rechnung unterschiedliche Werte die von der Karte unterstützten Dokumentdaten. [Das Ausführungsmodell](../workflow-execution-model.md) und [die Fehlerdiagnose](../workflow-troubleshooting.md) erklären den Zusammenhang.
