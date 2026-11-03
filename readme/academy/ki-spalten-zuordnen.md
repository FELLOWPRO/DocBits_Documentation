---
description: "DocBits Academy: Spalten bei unterschiedlicher Reihenfolge zuordnen"
---

# Spalten bei unterschiedlicher Reihenfolge zuordnen

**Zielgruppe:** Buchhaltung und Key User · **Schwierigkeit:** Mittel · **Übungsdauer:** 10–20 Minuten

**Lernziel:** Einzelpreis und Menge stehen in anderer Reihenfolge oder tragen abweichende Überschriften.

## Problem

Einzelpreis und Menge stehen in anderer Reihenfolge oder tragen abweichende Überschriften.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-spaltenreihenfolge.pdf" %}
Synthetischer Übungsbeleg. Weitere Formate und Sollwerte im Übungspaket.
{% endfile %}

## Konfiguration

Prüfen Sie die konfigurierten Tabellenspalten und ihre fachliche Bedeutung. Anzeigename, interner Spaltenschlüssel und ERP-Zielfeld sind unterschiedliche Angaben.

## Ausführung

1. Öffnen Sie den Beleg und vergleichen Sie die Spaltenüberschriften mit dem PDF.
2. Wählen Sie den Spaltennamen in der Tabelle und ordnen Sie die konfigurierte Spalte für Artikelnummer, Beschreibung, Menge und Einzelpreis zu.
3. Prüfen Sie einen möglichen Konfliktdialog: Eine bereits belegte Zuordnung kann eine andere Spalte unzugeordnet lassen.
4. Prüfen Sie danach jede Zeile. ART-B muss Menge 5, Einzelpreis 105 EUR und Netto 525 EUR zeigen.

## Ergebnis

Die Spaltenreihenfolge verändert die Werte und ihre Bedeutung nicht. Alle drei Positionen ergeben 1.325 EUR netto.

## Fehlerbehebung

Sind Werte vertauscht, ändern Sie die Zuordnung statt die Zahlen zu überschreiben. Prüfen Sie nach jeder Neuzuordnung auch vorher bereits korrekt zugeordnete Spalten.

## Screenshots und Video

<figure><img src="../.gitbook/assets/ai-table-map-column-de.png" alt="Vorhandene echte KI-Tabellenoberfläche zur Spaltenzuordnung"><figcaption><p>Bestehende deutsche Schulungsansicht zur Bedienung. Die neuen Übungsbelege werden bei ihrer Abnahme separat geprüft.</p></figcaption></figure>

Vorhandene Kurzanleitung zur Korrektur und Prüfung einer Spalte. Sie zeigt einen anderen Schulungsbeleg.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.mp4" %}

[Deutsche Untertitel herunterladen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.vtt)

## Weiterführende Anleitung

[KI-Tabelle](../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Validierungsregeln](../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) · [Exportmodul](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
