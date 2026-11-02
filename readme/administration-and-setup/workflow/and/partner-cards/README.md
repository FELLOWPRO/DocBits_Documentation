# Partnerkarten: Testbedingungen

Mit diesen Partnerkarten prüfst du zwei unterschiedliche Ergebnisse: eine nicht erfüllte Bedingung und einen Ausführungsfehler. Füge sie unter **Und** in der Kategorie für Partnerkarten in einen kontrollierten Testworkflow ein. Welche Partnerkarten verfügbar sind, hängt von deiner Organisation ab.

## Passenden Test auswählen

- [Always Fail](always-fail.md) — Liefert absichtlich `FAILED`; DocFlow bildet dies auf `FAILED_CONDITION` ab.
- [Always Error](always-error.md) — Liefert absichtlich `ERROR`; Version 3 bietet den einstellbaren Parameter `reason`.

Diese Karten dienen zum Testen und prüfen keine Rechnungsdaten. Sie richten weder Wiederholungsregeln noch Fehlerzweige ein. Unterscheide im Workflow-Protokoll zwischen einer nicht erfüllten Bedingung und einem technischen Fehler.
