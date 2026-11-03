---
description: "DocBits Academy: 2. Rechnung mit Bestellung und Preisabweichung"
---

# 2. Rechnung mit Bestellung und Preisabweichung

**Zielgruppe:** Einkauf und Kreditorenbuchhaltung · **Schwierigkeit:** Mittel · **Übungsdauer:** 15–20 Minuten

**Lernziel:** Erkennen und entscheiden Sie eine Preisabweichung, ohne die Originalwerte der Rechnung für einen erfolgreichen Abgleich zu verändern.

## Problem

Erkennen und entscheiden Sie eine Preisabweichung, ohne die Originalwerte der Rechnung für einen erfolgreichen Abgleich zu verändern.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-preisabweichung.pdf" %}
ACADEMY-INV-003: drei Rechnungspositionen.
{% endfile %}

{% file src="../.gitbook/assets/academy-de-v1/bestellreferenzen.json" %}
Sollwerte für ACADEMY-PO-003 und ACADEMY-PO-030. Referenzdaten, kein direkt importierbares API-Format.
{% endfile %}

| Artikel | Menge | PO-Einzelpreis EUR | Rechnungspreis EUR | Rechnungsnetto EUR |
| --- | ---: | ---: | ---: | ---: |
| ART-A | 10 | 50,00 | 50,00 | 500,00 |
| ART-B | 5 | 100,00 | 105,00 | 525,00 |
| ART-C | 20 | 15,00 | 15,00 | 300,00 |

Bestellung: **1.300,00 EUR netto**. Rechnung: **1.325,00 EUR netto**, 251,75 EUR Steuer, 1.576,75 EUR brutto. Artikel B liegt **5 %** über dem Bestellpreis. Die 25,00 EUR Differenz entsprechen nicht 5 % der gesamten Bestellung.

## Konfiguration

Der Administrator muss ACADEMY-PO-003 mit diesen Artikel-, Mengen- und Preiswerten über den für Ihre Organisation konfigurierten Stammdatenimport bereitstellen. Die JSON-Datei ist eine lesbare Bestellreferenz; sie legt in DocBits keine Bestellung an. Prüfen Sie Lieferant, Gesellschaft, EUR, Preiseinheit 1 und Mengeneinheit.

Für die erweiterte Übung öffnen Administratoren **Einstellungen → Dokumenttypen → Rechnung → Weitere Einstellungen → Bestellung → PO-Toleranzeinstellung**. Wählen Sie beim Einzelpreis **%** und zunächst **2**. Stellen Sie die Menge auf **0** mit der vorgesehenen Einheit. Im numerischen Spaltenvergleich der passenden PO-Abgleichregel muss **Toleranz zulassen** gesetzt sein. Artikelbezogene Übersteuerungen müssen geprüft werden. Die Steuerungen können unmittelbar speichern.

Der **Rule Manager** steuert zusätzliche Konflikt- und Exportentscheidungen. Er ersetzt die PO-Toleranzeinstellung und die Vergleichsregel nicht. Dokumentieren Sie das aktive Konfliktregelwerk getrennt. [Toleranzen konfigurieren](../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) · [Konfliktregeln](../administration-and-setup/settings/document-processing/rule-manager/README.md)

## Ausführung

1. Importieren Sie die PDF und öffnen Sie die Positionstabelle. Vergleichen Sie alle drei Artikel, Mengen, Einzelpreise und Nettobeträge mit dem Original.
2. Ordnen Sie die Tabelle den konfigurierten Rechnungsfeldern zu. Eine Spaltenzuordnung ist noch keine ERP-Exportzuordnung.
3. Prüfen Sie das Bestellfeld und die zugehörige Bestellung. Fehlt sie, suchen Sie nach ACADEMY-PO-003. Ein Suchtreffer muss zum Lieferanten und zur Gesellschaft passen.
4. Öffnen Sie den **PO-Abgleich**. Prüfen Sie vorhandene Verbindungen und starten Sie bei Bedarf **Auto Match**. Klappen Sie die Abgleichdetails auf und lesen Sie die Mengen- und Preisabweichung.
5. Dokumentieren Sie ART-B: Menge 5 gegen 5, Preis 105 gegen 100, Differenz 5 EUR je Stück und 25 EUR insgesamt.
6. Testen Sie mit 2 % Preistoleranz. Der erlaubte Preisbereich ist 98 bis 102 EUR; 105 EUR liegt außerhalb. Prüfen Sie auch, ob eine Konfliktregel eine weitere Entscheidung verlangt.
7. Lassen Sie den Administrator nur im isolierten Test den Wert auf 6 % ändern. Wiederholen Sie den Abgleich nach dem vorgesehenen Aktualisierungsverfahren: 94 bis 106 EUR schließt 105 EUR ein. Halten Sie beide Ergebnisse fest und stellen Sie die Ausgangskonfiguration anschließend wieder her.
8. Treffen Sie die nach den aktiven Regeln zulässige Entscheidung: fachlich akzeptieren, mit Begründung weiterleiten oder ablehnen. Lassen Sie die echte Rechnungsabweichung im Beleg bestehen.
9. Speichern und laden Sie erneut. Kontrollieren Sie Zuordnungen, Abgleichergebnis und Entscheidungsbegründung.
10. Exportieren Sie erst nach allen erforderlichen Prüfungen und Freigaben in das Test-ERP. Prüfen Sie die übernommenen Positionen und die Verarbeitung der Differenz anhand der aktiven Konfliktregeln.

## Ergebnis

A und C passen in Menge und Preis. B zeigt eine Preisabweichung von 5 %. Bei 2 % bleibt diese außerhalb der Toleranz, bei 6 % liegt sie innerhalb. Ein Full Match allein belegt weder Freigabe noch Export. Abgenommen ist der Ablauf erst nach dokumentierter Entscheidung und genau einer fachlich korrekten ERP-Übernahme.

## Fehlerbehebung

| Problem | Prüfung |
| --- | --- |
| Keine Bestellung gefunden | Import, Zielorganisation und Bestellnummer kontrollieren. |
| 105 EUR wird trotz 2 % akzeptiert | Artikelübersteuerung, aktive Regelversion und Vergleichsspalte prüfen. |
| 6 % hat keine Wirkung | Prozent statt fester Wert, Toleranz zulassen und erneuten Abgleich prüfen. |
| Keine Menge/kein Preis | Feldzuordnung und Preiseinheit prüfen, bevor der Abgleich wiederholt wird. |

## Screenshots und Video

<figure><img src="../.gitbook/assets/po-matching-mismatch-de.png" alt="Vorhandener PO-Schulungsfall mit Mengen- und Preisabweichung"><figcaption><p>Echte Oberfläche eines bestehenden Schulungsfalls mit absichtlich falscher Verbindung. Das Bild erklärt die Abweichungsanzeige und zeigt nicht die neue Drei-Artikel-Rechnung.</p></figcaption></figure>

Kurzanleitung zum PO-Abgleich anhand des bestehenden Schulungsfalls. Die Werte unterscheiden sich von ART-A bis ART-C.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/de.html)

## Weiterführende Anleitung

[PO-Abgleich](../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) · [PO-Regeln](../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) · [Toleranzen](../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) · [30 Positionen und drei Abweichungen](dreissig-positionen-abgleichen.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
