---
description: "DocBits Academy: 30 Positionen: zwei Mengenfehler und einen Preisfehler erkennen"
---

# 30 Positionen: zwei Mengenfehler und einen Preisfehler erkennen

**Zielgruppe:** Einkauf und Kreditorenbuchhaltung · **Schwierigkeit:** Mittel · **Übungsdauer:** 20–30 Minuten

**Lernziel:** Verhindern Sie, dass eine dreiseitige Rechnung mit zwei Mengenabweichungen und einer Preisabweichung ungeprüft ins ERP gelangt.

## Problem

Verhindern Sie, dass eine dreiseitige Rechnung mit zwei Mengenabweichungen und einer Preisabweichung ungeprüft ins ERP gelangt.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-30-positionen.pdf" %}
Die Rechnung ACADEMY-INV-030 mit 30 Positionen.
{% endfile %}

{% file src="../.gitbook/assets/academy-de-v1/bestellreferenzen.json" %}
ACADEMY-PO-030 als Sollreferenz. Alle Positionen: Menge 10, Preis 10,00 EUR, Preiseinheit 1.
{% endfile %}

| Position | Rechnung | Bestellung | Abweichung |
| --- | --- | --- | --- |
| 7 / ACA-007 | Menge 12 | Menge 10 | +2 / +20 % |
| 18 / ACA-018 | Menge 8 | Menge 10 | −2 / −20 % |
| 26 / ACA-026 | Preis 10,50 EUR | Preis 10,00 EUR | +0,50 EUR / +5 % |

Alle übrigen Positionen stimmen überein. Bestellung netto: 3.000,00 EUR; Rechnung netto: 3.005,00 EUR. Die beiden Mengenabweichungen heben sich im Gesamtbetrag auf. Deshalb genügt ein Vergleich der Gesamtsummen nicht.

## Konfiguration

Voraussetzung ist die vollständig geprüfte Tabelle aus Tutorial 6. Ein Administrator importiert die Bestellreferenz über die konfigurierte Stammdatenschnittstelle und prüft Lieferant, Gesellschaft, Artikel, Währung und Einheiten. Zum Sichtbarmachen aller drei Abweichungen zunächst Menge **0 %** und Einzelpreis **2 %** verwenden. Die Vergleichsregeln müssen Menge und Einzelpreis prüfen; artikelbezogene Übersteuerungen gesondert kontrollieren. Der Exportprozess muss ungeklärte Abweichungen entsprechend der Geschäftsregel anhalten.

## Ausführung

1. Importieren Sie die Rechnung und bestätigen Sie alle 30 extrahierten Positionen anhand von Tutorial 6.
2. Prüfen Sie Artikelnummer, Beschreibung, Menge, Einheit, Einzelpreis und Nettobetrag. Ordnen Sie diese konfigurierten Spalten zu. Lassen Sie das ERP-Positionsmapping durch den Administrator anhand der aktiven LN-/M3-Konfiguration prüfen.
3. Prüfen Sie ACADEMY-PO-030 und starten Sie den PO-Abgleich. Kontrollieren Sie die vorhandenen Zuordnungen, bevor Sie Auto Match erneut verwenden.
4. Öffnen Sie die Details von ACA-007, ACA-018 und ACA-026. Vergleichen Sie die Werte mit der Solltabelle oben und notieren Sie Regel und Abweichung.
5. Prüfen Sie die Toleranzen: ±2 % von 10,00 EUR ergeben 9,80 bis 10,20 EUR. 10,50 EUR liegt außerhalb. Eine Mengentoleranz von 0 % akzeptiert weder 12 noch 8 statt 10.
6. Erhöhen Sie nur in einer gesonderten Testkonfiguration den Einzelpreis auf 6 %. Der Preis liegt dann innerhalb; die beiden Mengenabweichungen bleiben. Dokumentieren Sie beide Durchläufe und stellen Sie die Ausgangskonfiguration wieder her.
7. Bei falsch gelesenen Werten korrigieren Sie anhand des Originals. Bei echten Abweichungen zum Auftrag behalten Sie die Rechnungswerte und lassen die zuständige Rolle entscheiden beziehungsweise einen korrigierten Beleg anfordern. Begründen Sie die Entscheidung.
8. Prüfen Sie nach Speichern und Freigabe die weiterhin offenen Beträge, Mengen und Entscheidungen. Exportieren Sie erst zum Testziel, wenn der konfigurierte Prozess das erlaubt.
9. Vergleichen Sie im Zielsystem alle 30 Positionen, nicht nur die Belegsumme. Prüfen Sie die beiden Mengenfälle, Preisabweichung, Gebühren und Steuerbehandlung sowie genau einen Zielbeleg.

## Ergebnis

Im ersten Durchlauf werden genau die drei festgelegten fachlichen Abweichungen sichtbar. Im 6-%-Preistest bleibt die Mengenprüfung wirksam. Für einen abgeschlossenen Geschäftsfall sind alle Entscheidungen und die 30 korrekten ERP-Zeilen nachgewiesen. Die Referenzdatei enthält Sollwerte, keine aufgezeichnete erfolgreiche Produktverarbeitung.

## Fehlerbehebung

Wird nur der Gesamtbetrag verglichen, können sich die Mengenfehler gegenseitig verdecken. Prüfen Sie deshalb die numerischen Vergleichsspalten der aktiven Regel. Fehlt eine Position, zuerst Extraktion korrigieren. Fehlt die Bestellung, Stammdatenimport prüfen. Ein akzeptierter Preis legitimiert keine abweichende Menge. Eine grüne Zuordnung ersetzt keine erforderliche Freigabe.

## Screenshots und Video

<figure><img src="../.gitbook/assets/po-matching-mismatch-de.png" alt="Bestehende Detailanzeige eines unpassenden Abgleichs"><figcaption><p>Die vorhandene Abbildung erklärt die Detailanzeige anhand eines anderen Falls. Sie ist kein Nachweis der drei Abweichungen der 30-Positionen-Übung.</p></figcaption></figure>

Vorhandene Bedienungsanleitung zum Abgleich. Für die Freigabe dieses neuen End-to-End-Falls sind eigene Aufnahmen der 30 Positionen und des kontrollierten Ergebnisses erforderlich.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/de.html)

## Weiterführende Anleitung

[Tutorial 6](mehrseitige-ki-tabellen.md) · [PO-Regeln](../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) · [ERP-Exportkonfiguration](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
