---
description: "DocBits Academy: Tabellen aus Excel, PDF und Scans vergleichen"
---

# Tabellen aus Excel, PDF und Scans vergleichen

**Zielgruppe:** Buchhaltung und Key User · **Schwierigkeit:** Mittel · **Übungsdauer:** 10–20 Minuten

**Lernziel:** Die gleiche Tabelle kommt als digitale PDF, Excel-Datei oder bildbasierter Scan an.

## Problem

Die gleiche Tabelle kommt als digitale PDF, Excel-Datei oder bildbasierter Scan an.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-30-positionen-scan.pdf" %}
Synthetischer Übungsbeleg. Weitere Formate und Sollwerte im Übungspaket.
{% endfile %}

## Konfiguration

Das Paket enthält digitale PDF, bildbasierte PDF und XLSX mit denselben 30 Positionen. Prüfen Sie vor dem Import, ob der konkrete DocBits-Importweg XLSX direkt unterstützt. Eine generelle Unterstützung wird aus dem Vorhandensein der Datei nicht abgeleitet.

## Ausführung

1. Importieren Sie digitale PDF und Scan als getrennte Trainingsbelege und notieren Sie ihre Dokument-IDs.
2. Vergleichen Sie jeweils 30 Artikelnummern und die Summen. Kontrollieren Sie beim Scan besonders Dezimalzeichen und Seitenübergänge.
3. Öffnen Sie rechnung-30-positionen.xlsx zum Sollvergleich. Falls der konfigurierte Import XLSX akzeptiert, prüfen Sie auch dieses Ergebnis. Andernfalls erzeugen Sie im freigegebenen Vorprozess eine PDF und prüfen Sie deren Seiten und Summen erneut.
4. Notieren Sie die tatsächlich verwendeten Formate und Konvertierungen. Verwenden Sie neue Belegnummern, falls Ihre Dublettenprüfung den Vergleich sonst blockiert.

## Ergebnis

Jeder tatsächlich unterstützte und geprüfte Eingang ergibt dieselben 30 Positionen, 3.005 EUR netto und 3.575,95 EUR brutto. Scan-Verarbeitung und direkter Excel-Import werden getrennt nachgewiesen.

## Fehlerbehebung

Bei schlechter Scanerkennung zuerst Lesbarkeit, Auflösung, Rotation und vollständige Seiten prüfen. Eine XLSX-Ablehnung nicht durch Umbenennen der Dateiendung umgehen.

## Screenshots und Video

<figure><img src="../.gitbook/assets/ai-table-map-column-de.png" alt="Vorhandene echte KI-Tabellenoberfläche zur Spaltenzuordnung"><figcaption><p>Bestehende deutsche Schulungsansicht zur Bedienung. Die neuen Übungsbelege werden bei ihrer Abnahme separat geprüft.</p></figcaption></figure>

Vorhandene Kurzanleitung zur Korrektur und Prüfung einer Spalte. Sie zeigt einen anderen Schulungsbeleg.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.mp4" %}

[Deutsche Untertitel herunterladen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.vtt)

## Weiterführende Anleitung

[KI-Tabelle](../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Validierungsregeln](../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) · [Exportmodul](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
