# OCR-Fehler in einer Bestellnummer korrigieren

Das dritte Zeichen von `06O123` ist der **Buchstabe O**. Wird stattdessen `060123` extrahiert, können Sie das bekannte Muster mit einer bedingten Präfixtransformation ohne eigenes Skript korrigieren.

## Präfixkorrektur einrichten

1. Öffnen Sie **Einstellungen → Dokumenttypen → Zahnrad → Transformationsregeln → Transformationsregeln verwalten**. Ein Organisationsadministrator muss die Funktion für den ausgewählten Dokumenttyp aktivieren.
2. Erstellen Sie eine **Kopffeld**-Regel mit **Bestellung (`Purchase Order`)** als Ziel. Lesen Sie aus **dem Feld selbst**.
3. Wählen Sie unter **Nur wenn…** das Bestellfeld, **beginnt mit (`starts with`)** und `060`.
4. Entfernen Sie den anfänglichen Trim-Schritt. Fügen Sie **Affix → Präfix entfernen → `060`** und danach **Affix → Präfix hinzufügen → `06O`** hinzu. Geben Sie im zweiten Schritt den Großbuchstaben O ein. Die Bedingung begrenzt beide Schritte auf das betroffene Präfix; die restlichen Zeichen bleiben erhalten.
5. Prüfen Sie die Live-Vorschau, speichern Sie die Regel und öffnen Sie sie erneut. Testen Sie ein Dokument, speichern Sie es und laden Sie es neu, um die gespeicherte Bestellnummer zu kontrollieren.

## Ergebnis prüfen

| Beispieleingabe | Erwartetes Ergebnis | Begründung |
| --- | --- | --- |
| `060123` | `06O123` | Betroffenes Präfix |
| `060987` | `06O987` | Weiterer betroffener Wert; Endung bleibt erhalten |
| `06O123` | `06O123` | Bereits korrekt; Bedingung trifft nicht zu |
| `160123` | `160123` | Anderes Präfix; Bedingung trifft nicht zu |
| `1060123` | `1060123` | `060` innerhalb des Werts ist kein passendes Präfix |

Dieses Beispiel korrigiert ein bekanntes Extraktionsmuster. Es beweist weder die OCR-Genauigkeit noch die Existenz der Bestellung oder einen erfolgreichen Bestellabgleich. Verwenden Sie die Regel nur, wenn die Nummernkonvention `06O` verlangt: Ein berechtigtes `060`-Präfix würde ebenfalls verändert. Ergänzen Sie Lieferantenbedingungen, wenn die Konvention nur für bestimmte Lieferanten gilt.

## Warum zwei Affix-Schritte?

Der aktuelle Editor verlangt für positionsabhängige Schritte wie **Suchen und Ersetzen** ein separates Quellfeld, auch wenn **Nur einmal pro Dokument ausführen** aktiviert ist. Die beiden Präfix-Schritte funktionieren auf demselben Feld. Nach der Korrektur beginnt der Wert nicht mehr mit `060`; bei weiteren Speichervorgängen greift die Bedingung daher nicht mehr.

In der aufgenommenen Produktoberfläche ist `starts with` noch englisch; **Präfix entfernen** erscheint als **Streifenpräfix**. Gemeint ist das Entfernen des angegebenen Anfangs, nicht das Entfernen aller gleichlautenden Zeichenfolgen.
