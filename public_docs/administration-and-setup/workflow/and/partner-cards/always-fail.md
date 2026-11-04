# Always Fail: nicht erfüllte Bedingung testen

## Wann einsetzen

Mit **Always Fail** prüfst du, ob eine von einer Und-Bedingung abhängige Aktion bei einer nicht erfüllten Bedingung ausbleibt. Die Karte liefert absichtlich `FAILED`; DocFlow protokolliert dies als `FAILED_CONDITION`. Das ist ein anderer Zustand als ein Ausführungsfehler.

## Konfiguration

Kartentyp: `partner_always_fail` · Vorlagenversion: **2**.

Füge die Karte unter **Und** in der Kategorie für Partnerkarten hinzu. Diese Version hat keine Eingabefelder. Feldname, Operator und Vergleichswert sind nicht erforderlich.

## Beispiel und erwartetes Ergebnis

Lege einen Testworkflow mit einem gezielt auslösbaren Start, **Always Fail als einziger Und-Bedingung** und einer unkritischen Dann-Aktion an, deren Ausführung du nachvollziehen kannst.

Erwartetes Ergebnis: Die Bedingung ist nicht erfüllt. Die davon abhängige Aktion darf nicht ausgeführt werden. Prüfe im Workflow-Protokoll `FAILED_CONDITION`; das SDK-Ergebnis lautet `FAILED`. Vergleiche dies mit einem separaten erfolgreichen Test, um auch die Konfiguration der Dann-Aktion zu prüfen.

## Grenzen und Prüfung

Verwende [Always Error](always-error.md), um einen Ausführungsfehler zu testen. Always Fail prüft kein Dokumentfeld und sagt nichts über die Richtigkeit der Rechnung aus. Solange die Karte im erforderlichen Bedingungspfad bleibt, kann dieser Pfad nicht erfolgreich durchlaufen werden.

[Alle Partner-Testbedingungen](README.md).
