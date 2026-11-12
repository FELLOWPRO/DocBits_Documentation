# Smart Search Ranking

Smart Search Ranking stellt die Dokumente, die Sie meinen, an den Anfang einer Dashboard-Suche. Eine Stichwortsuche findet jedes Dokument, das Ihr Wort enthält; Smart Search Ranking fügt einen Schritt hinzu: Eine KI liest die besten Treffer und stellt die Dokumente nach vorn, in denen es wirklich um Ihre Suche geht. Exakte Treffer – Rechnungsnummern, Bestellnummern, Lieferantennamen – bleiben immer ganz oben.

## Was sich ändert

| | Stichwort-Reihenfolge | Mit Smart Search Ranking |
| --- | --- | --- |
| Welche Dokumente gefunden werden | Dieselben | Dieselben |
| Reihenfolge der Ergebnisse | Nach Stichworttreffer | Dokumente, in denen es um Ihre Suche geht, zuerst |
| Exakte Treffer (Rechnungsnummer, Bestellnummer, Lieferant) | Vorn | Vorn |
| Spaltensortierung, `ocr:`- und Feldsuchen | Unverändert | Unverändert – sie behalten ihre eigene Reihenfolge |

## Beispiel

Elf Testrechnungen enthalten alle das Wort *Schrauben*: Edelstahlschrauben, ein Schraubenzieher-Set, die Wartung eines Schraubenkompressors, Flaschen mit Schraubverschluss, ein Schraubenbaum, Schraubensicherung, ein Cocktail „Schraubenzieher“, ein Spielzeug-Werkzeugkoffer.

* Suche nach **Schrauben**: In der Stichwort-Reihenfolge ist das Schraubenzieher-Set der erste Treffer, die Rechnung über Edelstahlschrauben steht auf Platz fünf. Mit Smart Search Ranking kommen die Schrauben zuerst, dann das Schrauben-Sortiment; das Schraubenzieher-Set rückt auf Platz vier.
* Suche nach **Schraubenzieher**: Das Schraubenzieher-Set ist in der Stichwort-Reihenfolge vorn und bleibt mit Smart Search Ranking vorn – diesmal ist es das, was Sie meinten. Die isolierten Schraubenzieher rücken auf Platz zwei; Cocktail und Spielzeug rücken nach hinten.

## Wo es gilt

* In der [Schnellsuche](quick-search.md) des Dashboards mit einfachem Text (nicht in den feldbezogenen `Feld:`-Chips).
* Der Anfang der Ergebnisliste wird neu sortiert; weiter unten behalten lange Ergebnislisten ihre Stichwort-Reihenfolge.
* Antwortet der Ranking-Dienst nicht innerhalb seines Zeitbudgets, zeigt die Suche die normale Stichwort-Reihenfolge. Nichts wird ausgeblendet, kein Ergebnis entfällt.

## So wird es eingeschaltet

Smart Search Ranking wird von DocBits pro Organisation aktiviert. Bitten Sie Ihren DocBits-Ansprechpartner, es einzuschalten. Es gilt innerhalb einer Minute für alle Benutzer der Organisation, ohne dass sich an der Bedienung der Suche etwas ändert.
