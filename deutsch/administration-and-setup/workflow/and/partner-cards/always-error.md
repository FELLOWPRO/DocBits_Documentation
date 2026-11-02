# Always Error: Fehlerbehandlung testen

## Wann einsetzen

Mit **Always Error** prüfst du, wie die Überwachung und die eingerichtete Fehlerbehandlung auf eine fehlgeschlagene Kartenausführung reagieren. Die Karte liefert absichtlich `ERROR` und meldet nicht lediglich eine nicht erfüllte Bedingung.

## Konfiguration

Kartentyp: `partner_always_error` · Vorlagenversion: **3**.

Füge die Karte unter **Und** in der Kategorie für Partnerkarten hinzu. Trage beim Textparameter `reason` eine erkennbare Testmeldung ein, beispielsweise `Demo: error-path check`. Der Standardwert lautet `Forced error for testing`. Der Parameter legt den Testgrund fest; er ist weder Vergleichsoperator noch Einstellung für Wiederholungen.

## Beispiel und erwartetes Ergebnis

Lege einen kontrollierten Testworkflow mit dieser Karte als einziger Und-Bedingung an. Setze `reason` auf `Demo: error-path check` und löse den gewählten Start aus.

Erwartetes Ergebnis: Die Karte meldet `ERROR`, nicht `FAILED_CONDITION`. Prüfe den Fehler und den angegebenen Grund im Workflow-Protokoll. Kontrolliere die für den Workflow eingerichtete Überwachung oder Fehlerbehandlung gesondert; die Karte richtet diese nicht ein.

## Grenzen und Prüfung

Für eine gewöhnliche nicht erfüllte Bedingung verwendest du [Always Fail](always-fail.md). Always Error prüft keine Rechnungsdaten. Entferne die Karte für den erzwungenen Fehler nach dem Test, bevor du den Workflow zur normalen Dokumentverarbeitung verwendest.

[Alle Partner-Testbedingungen](README.md).
