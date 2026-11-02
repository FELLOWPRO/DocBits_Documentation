# Bewährte Vorgehensweisen

## Standardspalten für Beträge und Mengen beibehalten

Die Positionsprüfungen (*Menge × Einzelpreis = Zeilensumme*) und der Bestellabgleich suchen nach den Standardspalten `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Wenn Sie stattdessen eigene Spalten für diese Werte anlegen, laufen die Prüfungen nicht, und der Bestellabgleich meldet fehlende Pflichtspalten. Benennen Sie den *Titel* um, wenn die Formulierung nicht passt; behalten Sie aber die Spalte.

## Ausblenden statt löschen

Standardspalten, die Sie nicht benötigen, werden ausgeblendet und nicht gelöscht; sie lassen sich ohnehin nicht löschen. Auch bei eigenen Spalten ist Ausblenden die sicherere Wahl, solange Sie nicht sicher wissen, ob ein Skript oder ein Export-Mapping die Spalte noch referenziert.

## Nur als erforderlich markieren, was den Export blockiert

Jede erforderliche Spalte muss in jeder Zeile gefüllt sein, bevor ein Benutzer das Dokument freigeben kann. Verwenden Sie dies für Werte, die das ERP bei Fehlen ablehnt (zum Beispiel die Kostenstelle in einem Buchungsexport), nicht für Werte, die lediglich nützlich sind.

## *Read Only* für nachgeschlagene Werte verwenden

Werte, die ein Skript oder ein Stammdaten-Lookup in die Tabelle schreibt (Artikelbeschreibung aus dem Artikelstamm, Steuercode vom Lieferanten), sollten schreibgeschützt sein, damit Benutzer die Quelle korrigieren statt der Kopie.

## Use AI pro Spalte, nicht pro Lieferant

Bei einem Lieferanten mit trainierten Regeln kommen die meisten Spalten aus den Regeln korrekt heraus. Ist eine Spalte unzuverlässig (lange Beschreibungen mit Zeilenumbruch, ein Rabatt, der manchmal an anderer Stelle steht), setzen Sie *Use AI* nur für diese Spalte. Die Regeln behalten den Rest.

## Spalten für das ERP benennen, nicht für das Dokument

Der *Column name* landet in Export-Mappings und Skripten. `COST_CENTRE` lässt sich einfacher zuordnen als `KST` und ändert sich nicht, wenn ein Lieferant es anders druckt.

## An einem neu gestarteten Dokument testen

Starten Sie nach einer Änderung ein bestehendes Dokument des Dokumenttyps neu und öffnen Sie es: Die neue Spalte erscheint, die ausgeblendete ist verschwunden, erforderliche Zellen sind markiert. Erst dann geben Sie die Änderung für die Benutzer frei.

## Eine Tabelle pro Positionsstruktur

Legen Sie eine zweite Tabelle nur an, wenn ein Dokumenttyp tatsächlich zwei voneinander unabhängige Tabellen hat (zum Beispiel Artikelzeilen und eine separate Tabelle für Nebenkosten). Zusätzliche leere Tabellen erscheinen bei jedem Dokument des Typs.
