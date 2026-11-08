# Appearance

**Appearance** gibt einem Administrator die Möglichkeit, der Kopie von DocBits in seiner Organisation ein eigenes Erscheinungsbild zu geben: Farben, Eckenradius, Dichte und Schriftart. Jeder in der Organisation sieht das Ergebnis — im hellen wie im dunklen Modus — nach dem nächsten Neuladen. Das Layout und das Verhalten einer Funktion ändern sich nie, nur die Darstellung.

> **Zugriff:** Appearance ist eine Seite nur für Administratoren. Öffnen Sie **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Wer es ändern kann

Nur Organisationsadministratoren können **Settings → Appearance** öffnen und ein Theme speichern oder zurücksetzen. Alle anderen in der Organisation sehen nur das Ergebnis.

## Was auf der Seite steht

Die Seite ist in einen Editor links und eine Live-Vorschau rechts geteilt.

| Bereich | Inhalt |
|---|---|
| **General** | Der Name des Themes, die Schriftart, der Eckenradius und die Dichte. |
| **Colors** | Die Tabs Light und Dark, je Farbe ein Farbwähler plus ein Hex-Feld, gruppiert in Surfaces, Brand, Neutrals, Status und Charts. Ein schreibgeschütztes Panel „Derived colours“ darunter zeigt Farben, die DocBits für Sie aus den Farben oben berechnet (Hover-Zustände, Fokusringe und Ähnliches). |
| **Advanced overrides** | Eine Zeile `--token: value` pro Eintrag, für den seltenen Fall, dass die Bedienelemente für Farbe, Radius, Dichte und Schriftart oben nicht ausreichen — siehe [Advanced overrides](#advanced-overrides). |

### Farben ändern

Jede Farbe hat ein Farbfeld (ein Klick öffnet die Farbauswahl des Browsers) und daneben ein Hex-Feld, in das Sie tippen oder einfügen können. Lassen Sie eine Farbe leer, um den DocBits-Standard für dieses Token zu behalten — das Farbfeld zeigt dann einen gestrichelten Rahmen. Wechseln Sie über die Tabs **Light** / **Dark** über der Farbliste in den anderen Modus; eine Farbe, die Sie im dunklen Modus nicht setzen, behält ihren eigenen DocBits-Standard für dunkel und übernimmt nicht den hellen Wert.

{% hint style="info" %}
Farben werden als Hex eingegeben (`#2388ae` oder `#2388aeaa` mit Alpha). Es gibt keine Eingabe für Farbnamen oder `rgb()`.
{% endhint %}

### Eckenradius, Dichte und Schriftart

* **Corner radius** — `None`, `Small`, `Medium` (Standard), `Large` oder `Extra large`. Steuert, wie stark Karten, Buttons, Eingabefelder und Dialoge app-weit abgerundet sind.
* **Density** — `Compact`, `Comfortable` (Standard) oder `Spacious`. Steuert die Höhe von Buttons, Eingabefeldern und Tabellenzeilen sowie die Grundschriftgröße.
* **Font** — eine kurze Liste mitgelieferter Schriftarten (Geist ist der DocBits-Standard; außerdem Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit oder die Systemschrift des Besuchers). Jede Schriftart ist bereits enthalten, es muss nichts hochgeladen werden.

### Advanced overrides

Für ein Design-Token, das die Bedienelemente oben nicht direkt anbieten (zum Beispiel eine bestimmte Tabellenzeilenhöhe), ergänzen Sie eine Zeile unter **Advanced overrides**:

```
--table-row-h: 30px
```

Eine Überschreibung pro Zeile, `--token: value`. Eine ungültige Zeile — ein unbekanntes Token, ein Token, das sich nicht anpassen lässt, oder ein Wert, der nicht zu dem passt, was das Token erwartet — wird unter dem Feld als Fehler aufgeführt und nicht angewendet; alles andere auf der Seite wird trotzdem normal gespeichert.

## Vorschau

Jede Änderung aktualisiert das Panel **Preview** rechts sofort, ohne zu beeinflussen, was andere sehen — es berührt weder die laufende App noch das gespeicherte Theme. Die Vorschau hat eigene Tabs: eine Übersicht mit hell und dunkel nebeneinander, danach eigene Seiten für Buttons, Formularfelder, Flächen und Statusanzeigen, damit Sie Kontrast und Lesbarkeit in den für Farbe empfindlichsten Teilen der Oberfläche prüfen können.

<!-- screenshot: /settings/appearance dark -->

Macht eine Änderung das Theme ungültig (siehe unten), zeigt die Vorschau weiterhin die letzte gültige Version, statt zu brechen.

## Speichern und zurücksetzen

* **Save** schreibt das Theme für die gesamte Organisation. Der Button ist ausgegraut, bis sich tatsächlich etwas geändert hat und das Theme gültig ist.
* **Reset** fragt nach einer Bestätigung und entfernt dann das Theme der Organisation vollständig; alle kehren zum DocBits-Standard-Theme zurück. Das lässt sich auf der Seite nicht rückgängig machen — die Farben müssen von Hand neu eingegeben (oder neu importiert, siehe unten) werden, wenn die Organisation sie zurückhaben will.
* Ein fehlgeschlagenes Speichern oder Zurücksetzen (zum Beispiel wegen eines Validierungsproblems) führt das Problem über dem Editor auf und lässt die Seite unverändert; es wird nichts angewendet.

Vor dem Speichern gibt es keine Kontrastprüfung — siehe [Tipps](#tipps) unten.

## Export und Import

* **Export** lädt das aktuell im Editor angezeigte Theme (gespeichert oder nicht) als `.json`-Datei herunter, benannt nach dem Theme.
* **Import** liest eine `.json`-Theme-Datei und lädt sie in den Editor. Sie muss weiterhin geprüft und gespeichert werden, um zu wirken — der Import allein ändert nicht, was jemand sieht. Eine ungültige oder zu große Datei (über 32 KB) wird mit einem Fehler abgelehnt, und nichts ändert sich.

Export ist ein bequemer Weg, ein Theme vor Experimenten zu sichern oder das Aussehen einer Organisation auf eine andere zu übertragen.

## Was Benutzer sehen

Nach dem Speichern gilt das Theme für die gesamte Anwendung — jede Seite, im hellen wie im dunklen Modus — für jedes Mitglied der Organisation, nach dem nächsten Neuladen (nicht sofort für andere offene Sitzungen). Ein Benutzer, der die Organisation noch nie geladen hat, sieht den DocBits-Standard, bis die Einstellungen der Organisation einmal geladen sind; danach übernimmt das Theme.

Ein Zurücksetzen bringt alle beim nächsten Neuladen auf das DocBits-Standardaussehen zurück, genau als hätte es nie ein Organisationstheme gegeben.

## Tipps

* **Prüfen Sie den Kontrast in beiden Modi.** Der Editor warnt nicht vor Kombinationen mit geringem Kontrast (zum Beispiel eine helle Markenfarbe mit hellem Text). Nutzen Sie die hellen und dunklen Panels der Vorschau, um vor dem Speichern zu prüfen, ob der Text lesbar bleibt.
* **Lassen Sie Statusfarben in Ruhe, wenn Sie keinen Grund haben, sie zu ändern.** Destructive (Fehler), Success, Warning und Info behalten ihre Bedeutung in der gesamten App — eine Änderung kann dazu führen, dass ein Fehler auf den ersten Blick wie ein Erfolg aussieht. Ändern Sie die Markenfarbe und lassen Sie Statusfarben auf ihren Standardwerten, es sei denn, die Organisation braucht mehr als das übliche Rot/Grün/Gelb/Blau.
* **Starten Sie mit einer vollständigen Palette.** Ein Export des aktuellen Themes oder ein Start vom DocBits-Standard gibt jeder Grundfarbe einen Wert zum Bearbeiten, statt raten zu müssen, welche Tokens es gibt.
* **Eine Theme-Änderung wirkt für jeden Benutzer der Organisation sofort beim nächsten Neuladen.** Es gibt keinen Schritt, der die Vorschau auf eine Teilgruppe von Benutzern beschränkt; testen Sie das Ergebnis selbst in hell und dunkel, bevor Sie dem Team sagen, dass es fertig ist.
