---
description: "DocBits Academy: Extrahierte Positionen für den ERP-Export vorbereiten"
---

# Extrahierte Positionen für den ERP-Export vorbereiten

**Zielgruppe:** Buchhaltung und Key User · **Schwierigkeit:** Mittel · **Übungsdauer:** 10–20 Minuten

**Lernziel:** Die Tabelle ist korrekt, aber ihre Felder müssen den richtigen ERP-Positionen entsprechen.

## Problem

Die Tabelle ist korrekt, aber ihre Felder müssen den richtigen ERP-Positionen entsprechen.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-30-positionen.pdf" %}
Synthetischer Übungsbeleg. Weitere Formate und Sollwerte im Übungspaket.
{% endfile %}

## Konfiguration

Administratoren prüfen das aktive LN- oder M3-Exportmapping, die tatsächliche Transaktion, Pflichtfelder, Gesellschaft und Einheiten. Es gibt keine für jedes ERP universelle Liste von Zielfeldnamen.

## Ausführung

1. Bestätigen Sie die 30 Rechnungspositionen und die fachlichen Spalten im Validierungsbildschirm.
2. Dokumentieren Sie pro Feld: DocBits-Spaltenschlüssel, fachliche Bedeutung, tatsächliches ERP-Zielfeld, Typ und Konvertierung.
3. Prüfen Sie Artikelnummer, Beschreibung, Menge, Einheit, Einzelpreis, Preiseinheit, Nettobetrag und PO-/Wareneingangsbezug, soweit für den Zielprozess erforderlich.
4. Prüfen Sie die erzeugte Export-Payload vor dem Testexport. Kontrollieren Sie nach Freigabe im Test-ERP alle 30 Zeilen und genau einen Beleg.

## Ergebnis

Die gespeicherte Tabelle, Exportdaten und ERP-Zeilen sind anhand stabiler Artikel-/Positionsschlüssel vergleichbar. 3.005 EUR netto und 570,95 EUR Steuer stimmen über alle Stufen überein.

## Fehlerbehebung

Wenn Felder leer ankommen, zuerst Mapping und tatsächliche Payload prüfen. Bei vertauschten Positionen nicht nur Zeilennummern, sondern Artikel- und Bestellbezug vergleichen. Vor jedem erneuten Export eine mögliche Teilübernahme klären.

## Screenshots und Video

<figure><img src="../.gitbook/assets/ai-table-map-column-de.png" alt="Vorhandene echte KI-Tabellenoberfläche zur Spaltenzuordnung"><figcaption><p>Bestehende deutsche Schulungsansicht zur Bedienung. Die neuen Übungsbelege werden bei ihrer Abnahme separat geprüft.</p></figcaption></figure>

Vorhandene Kurzanleitung zur Korrektur und Prüfung einer Spalte. Sie zeigt einen anderen Schulungsbeleg.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.mp4" %}

[Deutsche Untertitel herunterladen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/de.vtt)

## Weiterführende Anleitung

[KI-Tabelle](../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Validierungsregeln](../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) · [Exportmodul](../infor-integration-and-configuration/exporting-in-docbits/export-module.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
