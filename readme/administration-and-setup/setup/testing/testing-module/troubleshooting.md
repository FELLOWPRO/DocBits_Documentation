# Fehlerbehebung

## Ich finde Testing nicht in den Einstellungen

Die Seite sehen nur Organisations-Admins. Wenden Sie sich an einen Organisations-Admin Ihrer Organisation.

## Die Seite meldet, dass Testing ausgeschaltet ist

Ein Organisations-Admin muss oben auf der Seite **Testing für die Organisation aktivieren** einschalten. Bis dahin läuft
nichts, auch nicht über einen KI-Assistenten oder von außen.

## Mein Lauf ist fehlgeschlagen

Öffnen Sie das Protokoll im Reiter **Protokolle** und sehen Sie sich den ersten fehlgeschlagenen Schritt und seinen Fehlercode an:

| Sie sehen | Bedeutet meist | Was tun |
|---|---|---|
| Ein Element wurde nicht gefunden oder ist nicht sichtbar | Die Seite sieht in Ihrer Organisation anders aus oder lädt langsam | Seite selbst öffnen und prüfen; eigenes Template anpassen oder Werte der Eingabe prüfen |
| Ein Feld oder Status passt nicht | Das Dokument hat einen anderen Wert als erwartet | Dokument prüfen; erwarteten Wert in der Eingabe korrigieren |
| Die Seite ließ sich nicht öffnen | Falsche Dokument-ID oder fehlende Berechtigung | ID in der Eingabe und Rechte der Person prüfen, die den Tab geöffnet hat |
| Zeitüberschreitung | Schritt oder Test dauerte zu lange | Erneut starten; bei Wiederholung die Ladezeit der Seite prüfen |
| Von der Umgebung gesperrt | Der Test schreibt Daten in einer Kundenumgebung | Start bestätigen oder in einer Testumgebung ausführen |

## Mein Lauf ist „Blockiert"

Der Lauf ließ sich nicht bewerten: Schritte wurden übersprungen (etwa ein Screenshot-Schritt, den der Browser nicht
ausführen kann) oder eine Bestätigung fehlt. Ein blockierter Lauf zählt nie als bestanden. Entfernen Sie den Schritt aus
Ihrem eigenen Template oder starten Sie erneut mit Bestätigung.

## „Zum Start eine Browser-Sitzung registrieren" / kein Tab nimmt Starts an

Starts über einen KI-Assistenten oder von außen brauchen einen Browser-Tab mit eingeschaltetem **Start von außen erlauben**.
Öffnen Sie den Reiter Eingaben in einem Tab, der offen bleibt, schalten Sie es ein und verwenden Sie dessen Sitzungs-ID.
Neuladen beendet die Registrierung.

## Der Lauf bricht ab oder zeigt Abgebrochen / Nicht zustellbar

Der ausführende Tab wurde neu geladen, geschlossen oder hat die Verbindung verloren, oder kein Tab hat rechtzeitig
geantwortet. Lassen Sie den Tab offen und im Vordergrund, bis der Lauf endet, und starten Sie erneut. Ein Test mit einem Schritt
**Seite neu laden** endet ebenfalls so, wenn die Seite nicht innerhalb von etwa zwei Minuten zurückkommt
(siehe [Neu laden und fortsetzen](reload-and-resume.md)).

## „Playwright-Templates lassen sich hier noch nicht starten"

Templates mit dem **Ausführer** **Playwright** führt Ihre Testautomatisierung aus. Eingaben dafür können Sie speichern,
starten lassen sie sich von dieser Seite aus nicht.

## Ich kann ein Template nicht löschen

Nur eigene Templates Ihrer Organisation (**eigenes**) lassen sich löschen. Integrierte und Standard-Templates nicht; mit
**Kopie bearbeiten** erhalten Sie eine eigene Version.
