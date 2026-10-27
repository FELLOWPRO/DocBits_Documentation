---
description: "DocBits Academy: 3. Automatische Kontierung auf mehrere Kostenstellen"
---

# 3. Automatische Kontierung auf mehrere Kostenstellen

**Zielgruppe:** Buchhaltung und Controlling · **Schwierigkeit:** Mittel · **Übungsdauer:** 15 Minuten

**Lernziel:** Verteilen Sie eine Wartungsrechnung mit 3.000 EUR netto auf drei Kostenstellen und kontrollieren Sie die resultierenden Buchungszeilen.

## Problem

Verteilen Sie eine Wartungsrechnung mit 3.000 EUR netto auf drei Kostenstellen und kontrollieren Sie die resultierenden Buchungszeilen.

## Beispieldokument

{% file src="../.gitbook/assets/academy-de-v1/rechnung-kostenstellen.pdf" %}
ACADEMY-COST-3000: 3.000,00 EUR netto, 570,00 EUR Steuer, 3.570,00 EUR brutto.
{% endfile %}

| Kostenstelle | Anteil | Nettobetrag EUR |
| --- | ---: | ---: |
| IT | 50 % | 1.500,00 |
| Verwaltung | 30 % | 900,00 |
| Vertrieb | 20 % | 600,00 |
| **Gesamt** | **100 %** | **3.000,00** |

Die Namen sind fachliche Beispiele. Verwenden Sie die dafür vorbereiteten gültigen Kostenstellen-IDs Ihrer Testorganisation.

## Konfiguration

Administratoren prüfen unter **Einstellungen → Module → Bestellung & Finanzen → Auto Accounting** den Typ **LN** beziehungsweise **M3**, den Stammdatenimport und die verfügbaren Sachkonten und Dimensionen. Aktivieren Sie die Funktion erst nach dieser Prüfung.

Eine automatische Kontierung benötigt passende Stammdaten beziehungsweise eine eingerichtete Kontierungslogik. Die folgende manuelle Aufteilung zeigt, wie Sie das Ergebnis kontrollieren und bei Bedarf ergänzen. Sie richtet durch Eingabe von Prozenten allein keine wiederkehrende automatische Kontierungsregel ein. Prüfen Sie getrennt, ob Ihr Prozess nach Netto oder Gesamtbetrag aufteilt und wie Steuerzeilen exportiert werden. [LN-Einrichtung](../infor-integration-and-configuration/importing-customer-master-data/ln/auto-accounting.md) · [M3-Einrichtung](../infor-integration-and-configuration/importing-customer-master-data/m3/auto-accounting.md)

## Ausführung

1. Importieren Sie die Kostenrechnung und prüfen Sie Netto 3.000,00, Steuer 570,00 und Brutto 3.570,00 EUR.
2. Öffnen Sie die eingerichtete Kontierung. Prüfen Sie zuerst automatisch vorbelegte Sachkonten und Dimensionen. Ein leerer Bereich ist kein automatisch kontiertes Ergebnis.
3. Wählen Sie das vorbereitete Sachkonto und legen Sie drei Aufteilungszeilen an. Wählen Sie je Zeile die gültige Kostenstelle und ergänzen Sie einen Buchungstext.
4. Bestätigen Sie nacheinander 50 %, 30 % und 20 %. Warten Sie jeweils auf die Neuberechnung. Bei Nettoaufteilung müssen 1.500,00, 900,00 und 600,00 EUR erscheinen.
5. Falls die Oberfläche auf Brutto aufteilt, sind die Beträge 1.785,00, 1.071,00 und 714,00 EUR. Prüfen Sie die Steueraufteilung, bevor Sie diese Werte mit den Nettobuchungszeilen vergleichen.
6. Prüfen Sie Summe 100 %, vollständig erfassten Betrag und offenen Restbetrag 0. Speichern und öffnen Sie das Dokument erneut.
7. Führen Sie den vorgesehenen Freigabeprozess aus und exportieren Sie zum Testziel. Prüfen Sie dort alle drei Kostenstellen, Konto, Nettobeträge und Steuerbehandlung.
8. Prüfen Sie für den Automatiknachweis an einem zweiten, eindeutig neu nummerierten Testbeleg mit derselben fachlichen Zuordnung, ob die drei Kostenstellen bereits ohne manuelle Ergänzung vorbelegt werden. Halten Sie automatische und manuelle Schritte getrennt fest.

## Ergebnis

Die drei Nettobuchungszeilen ergeben 3.000,00 EUR. Die Steuer von 570,00 EUR wird nach der Integration gesondert korrekt behandelt. Das Test-ERP enthält die drei Kostenstellen und genau einen Beleg. Der zusätzliche Automatiknachweis ist erst bestanden, wenn ein Folgebeleg ohne manuelle Aufteilung korrekt vorbelegt wird.

## Fehlerbehebung

Ändern Sie im Trainingsdokument 20 % auf 15 %. Dann ergeben sich nur 95 % und 2.850 EUR netto; 150 EUR bleiben offen. Bei Bruttobasis fehlen 178,50 EUR. Beobachten und dokumentieren Sie die tatsächliche Validierung. Bleibt die Weiterverarbeitung möglich, ist die gewünschte Sperre noch nicht nachgewiesen. Stellen Sie anschließend 20 % wieder her.

Fehlende Kostenstellen: Stammdaten, Gesellschaft und Berechtigungen prüfen. Falsche Summe: Betragsbasis und Neuberechnung kontrollieren. Fehlende Automatik: gültige Einrichtung und Auswahlbedingungen des importierten Kontierungssatzes prüfen.

## Screenshots und Video

<figure><img src="../.gitbook/assets/customer-totals-de-accounting-email-v2.png" alt="Vorhandene Aufteilung einer Kostenrechnung auf zwei Kostenstellen"><figcaption><p>Bestehender Schulungsfall: 1.000 EUR ohne Steuer, aufgeteilt mit 60/40. Für diese Übung gelten drei Kostenstellen und 50/30/20.</p></figcaption></figure>

Der vorhandene Film erklärt das Anlegen, Prüfen und Speichern von Aufteilungszeilen mit einem anderen Zahlenbeispiel. Er belegt keine automatische Kontierung des neuen 3.000-EUR-Falls.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/cost-invoice-accounting-customer/v3/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/cost-invoice-accounting-customer/v3/de.html)

## Weiterführende Anleitung

[Kontierungsoberfläche](../end-user-and-partner-section/end-user-section/accounting-for-cost-invoice-and-indirect-sales.md) · [Auto Accounting LN](../infor-integration-and-configuration/importing-customer-master-data/ln/auto-accounting.md) · [Auto Accounting M3](../infor-integration-and-configuration/importing-customer-master-data/m3/auto-accounting.md)

**Stand:** 27.10.2026 · **Übungsversion:** 1.0. Die Medien zeigen die jeweils beschriebenen bestehenden Schulungsfälle. Die neuen Übungsbelege sind synthetisch. Ein erfolgreicher Lauf mit diesen Belegen und Ihrer ERP-Konfiguration muss anhand der Prüfkriterien bestätigt werden. [Voraussetzungen und Übungspaket](vorbereitung.md) · [Abnahme](qualitaet-und-abnahme.md) · [Academy](README.md)
