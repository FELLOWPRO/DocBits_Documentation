---
description: "DocBits Academy: Menge × Einzelpreis und Summen validieren"
---

# Menge × Einzelpreis und Summen validieren

**Zielgruppe:** Buchhaltung und Key User · **Schwierigkeit:** Mittel · **Übungsdauer:** 10–20 Minuten

**Lernziel:** Rechnerisch falsche Positionswerte sollen vor der Weiterverarbeitung auffallen.

## Problem

Rechnerisch falsche Positionswerte sollen vor der Weiterverarbeitung auffallen.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-preisabweichung.pdf" %}
Synthetischer Übungsbeleg. Weitere Formate und Sollwerte im Übungspaket.
{% endfile %}

## Konfiguration

Administratoren öffnen beim Dokumenttyp Benutzerdefinierte Validierungsregeln. Achtung: Beim Aktivieren ersetzen diese bestimmte eingebaute Betragsprüfungen. Bilden Sie benötigte Kopf-, Zeilen-, Rabatt- und Summenprüfungen nach. Die gezeigte einfache Formel gilt nur für Preiseinheit 1 ohne Positionsrabatt.

## Ausführung

1. Prüfen Sie die tatsächlichen Schlüssel Ihrer Tabelle. Im Standardbeispiel: INVOICE_TABLE, NET_AMOUNT, QUANTITY, UNIT_PRICE.
2. Erstellen Sie eine Tabellenzeilenregel am Nettobetrag mit Formel row.NET_AMOUNT == row.QUANTITY * row.UNIT_PRICE und Toleranz 0.01. Starten Sie mit Warnung im Test.
3. Testen Sie ART-B mit Menge 5, Preis 105 und Netto 525: bestanden. Ändern Sie im Trainingsdatensatz den Nettowert auf 520: fehlgeschlagen.
4. Prüfen Sie zusätzlich Pflichtwerte, Preiseinheit, Rabatte und die Tabellensumme. Eine Preisabweichung zur Bestellung ist ein eigener PO-Vergleich: 5 × 105 = 525 ist rechnerisch korrekt.

## Ergebnis

Der korrekte Rechenfall besteht; 520 statt 525 wird beanstandet. Eine Warnung blockiert keine Validierung. Für eine gewünschte Sperre muss die geprüfte Regel als Fehler eingerichtet sein.

## Fehlerbehebung

Leere oder nicht numerische Beträge können als 0 eingehen; ergänzen Sie passende Pflichtfeld-/Formatprüfungen. Bei Division durch null kann eine Regel übersprungen werden. Prüfen Sie bestanden, fehlgeschlagen und übersprungen getrennt.

## Screenshots und Video

<figure><img src="../.gitbook/assets/ai-table-map-column-de.png" alt="Vorhandene echte KI-Tabellenoberfläche zur Spaltenzuordnung"><figcaption><p>Bestehende deutsche Schulungsansicht zur Bedienung. Die neuen Übungsbelege werden bei ihrer Abnahme separat geprüft.</p></figcaption></figure>

Vorhandene Kurzanleitung zur Korrektur und Prüfung einer Spalte. Sie zeigt einen anderen Schulungsbeleg.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.mp4" %}

[Deutsche Untertitel herunterladen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.vtt)

## Weiterführende Anleitung

[KI-Tabelle](../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Validierungsregeln](../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) · [Exportmodul](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
