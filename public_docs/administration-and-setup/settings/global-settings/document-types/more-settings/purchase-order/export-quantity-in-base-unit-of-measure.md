# Exportmenge in Basismaßeinheit

Der Schalter **Export quantity in base unit of measure** steht im Abschnitt **Purchase Order** der **More Settings** eines Dokumenttyps. Er ändert die Menge und den Stückpreis, die der Infor-LN-Export für zugeordnete Bestellzeilen schreibt.

Sie öffnen ihn unter **Settings → Document Types**, wählen auf der Karte des Dokumenttyps das Zahnradsymbol (**More Settings**) und klappen **Purchase Order** auf.

## Was der Schalter bewirkt

* **Off:** DocBits exportiert die Menge und den Stückpreis in der Einheit der Rechnung.
* **On:** DocBits rechnet die Menge und den Stückpreis jeder zugeordneten Bestellzeile mit deren Umrechnungsfaktor in die Basismaßeinheit dieser Bestellzeile um und schreibt den Code der Basiseinheit statt des Codes der abgerechneten Einheit.

Eine Zeile ohne Umrechnungsfaktor wird unverändert exportiert; ein fehlender Faktor blockiert den Export also nicht.

{% hint style="info" %}
Die Umrechnung gilt nur für den Infor-LN-Export. Andere Exportziele behalten die abgerechnete Einheit.
{% endhint %}

## Wann Sie ihn einsetzen

Schalten Sie den Schalter ein, wenn die Infor-LN-Instanz Bestellmengen in der Basismaßeinheit erwartet. Die Umrechnung nutzt den Faktor, der an der Bestellzeile gespeichert ist, nicht einen Faktor, den DocBits aus dem Artikelstamm berechnet.

Einstellungen können Live-Dokumente betreffen. Prüfen Sie das Ergebnis mit einem Testdokument, bevor Sie die Änderung in der Produktion speichern. Der Schalter ändert die exportierten Werte; er ändert nicht, wie Rechnungs- und Bestellzeilen abgeglichen werden.

## Weiterführende Seiten

* [Bestellung](README.md)
* [Export nicht übereinstimmender PO-Zeilen](export-not-matched-po-lines.md)
* [Alternativer Export](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
