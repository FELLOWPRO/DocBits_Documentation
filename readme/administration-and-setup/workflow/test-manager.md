# Test Manager

Mit dem **Test Manager** können Sie wiederverwendbare **Testszenarien** für Ihre Workflows speichern und gemeinsam ausführen — so können Sie sicherstellen, dass sich ein Workflow auch nach einer Änderung noch korrekt verhält. Er funktioniert sowohl für Standard- als auch für Advanced-Workflows.

Öffnen Sie ihn über **Workflow Dashboard → Test Manager List**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List with test scenarios, status and Run All Tests"><figcaption><p>Die Test Manager List — jedes gespeicherte Szenario zeigt ein Bestanden/Fehlgeschlagen-Ergebnis.</p></figcaption></figure>

## Was ein Testszenario ist

Ein Testszenario erfasst einen Workflow, eine Beispieleingabe und das **erwartete Ergebnis**. Wenn Sie es ausführen, spielt der Test Manager den Workflow gegen diese Eingabe ab und vergleicht das Resultat mit Ihrer Erwartung — wodurch die Zeile **grün** (bestanden) oder **rot** (fehlgeschlagen) wird.

## Arbeiten mit Szenarien

- **Add Test Scenario** — erstellen Sie ein neues Szenario aus einem Workflow und einem Beispieldokument.
- **Run All Tests** — führen Sie alle Szenarien auf einmal aus und sehen Sie auf einen Blick, welche Workflows noch bestehen.
- **View Details** — öffnen Sie ein Szenario, um sein Ergebnis zu prüfen.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Workflow test scenario details with status, run time and data"><figcaption><p>Szenario-Details — Name, Status, Laufzeit sowie die tatsächlichen und extrahierten Daten, die der Lauf erzeugt hat.</p></figcaption></figure>

Die Detailansicht zeigt den Szenarionamen und **Status**, den **Workflow-Namen**, die **Laufzeit** sowie die **tatsächlichen** und **extrahierten Daten**, die der Lauf erzeugt hat — so können Sie genau erkennen, warum ein Szenario bestanden oder fehlgeschlagen ist.

## Test Manager vs. Testen im Builder

Das sind zwei verschiedene Dinge:

- **Test Manager** (diese Seite) — *gespeicherte, wiederholbare* Szenarien mit erwarteten Ergebnissen, die gemeinsam mit **Run All Tests** ausgeführt werden. Verwenden Sie ihn für Regressionstests nach Änderungen.
- **Testen im Builder** — die direkten Steuerelemente **Validate** und **Test** innerhalb des Advanced Workflow-Builders, für schnelle Prüfungen während des Erstellens. Siehe [Validierung & Testen](advanced-workflow/validation-and-testing.md).
