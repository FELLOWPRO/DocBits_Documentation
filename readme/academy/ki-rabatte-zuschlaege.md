---
description: "DocBits Academy: Rabatte, Zuschläge und Zwischensummen behandeln"
---

# Rabatte, Zuschläge und Zwischensummen behandeln

**Zielgruppe:** Buchhaltung und Key User · **Schwierigkeit:** Mittel · **Übungsdauer:** 10–20 Minuten

**Lernziel:** Rabatte oder Überträge werden als zusätzliche Artikel erkannt oder zweimal abgezogen.

## Problem

Rabatte oder Überträge werden als zusätzliche Artikel erkannt oder zweimal abgezogen.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-rabatt-zuschlag.pdf" %}
Synthetischer Übungsbeleg. Weitere Formate und Sollwerte im Übungspaket.
{% endfile %}

## Konfiguration

Prüfen Sie, ob Rabatte auf Zeilen- oder Kopfebene gelten und wie Ihre Integration Fracht und Zusatzkosten behandelt. Ein ausgewiesener Nettopreis kann den Rabatt bereits enthalten.

## Ausführung

1. Prüfen Sie die drei Artikelpositionen mit 1.325 EUR Zwischensumme.
2. Vergleichen Sie den Kopfrabatt von 25 EUR und die Fracht von 20 EUR mit der konfigurierten Verarbeitung.
3. Prüfen Sie, dass keine zusätzliche Artikelposition nur aus der Zwischen- oder Endsumme entstanden ist.
4. Kontrollieren Sie 1.325 − 25 + 20 = 1.320 EUR netto, 250,80 EUR Steuer und 1.570,80 EUR brutto.

## Ergebnis

Drei echte Artikelpositionen bleiben erhalten. Rabatt und Fracht werden genau einmal nach der Integration berücksichtigt.

## Fehlerbehebung

Ist der Nettobetrag 1.295 EUR, prüfen Sie einen doppelt abgezogenen Rabatt. Fehlen 20 EUR, prüfen Sie die Frachtzuordnung. Entfernen Sie eine echte Gebührenzeile nicht nur, um die Zeilenzahl zu reduzieren.

## Screenshots und Video

<figure><img src="../.gitbook/assets/ai-table-map-column-de.png" alt="Vorhandene echte KI-Tabellenoberfläche zur Spaltenzuordnung"><figcaption><p>Bestehende deutsche Schulungsansicht zur Bedienung. Die neuen Übungsbelege werden bei ihrer Abnahme separat geprüft.</p></figcaption></figure>

Vorhandene Kurzanleitung zur Korrektur und Prüfung einer Spalte. Sie zeigt einen anderen Schulungsbeleg.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.mp4" %}

[Deutsche Untertitel herunterladen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.vtt)

## Weiterführende Anleitung

[KI-Tabelle](../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Validierungsregeln](../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) · [Exportmodul](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
