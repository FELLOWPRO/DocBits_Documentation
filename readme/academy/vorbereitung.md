# Vorbereitung und Übungspaket

**Stand:** 27.10.2026 · **Paketversion:** 1.0 · Sprache: Deutsch

## Ihre Testumgebung vorbereiten

Verwenden Sie eine getrennte Testorganisation mit einem fiktiven Lieferanten und einem isolierten ERP-Testziel. Ein Administrator muss die verfügbaren Funktionen, Rollen und Stammdaten prüfen. Die Unterlagen enthalten keine Zugangsdaten und legen keine produktiven Konten oder Bestellungen an.

| Bereich | Benötigt |
| --- | --- |
| Bearbeitung | Import, Validierung, Kontierung und PO-Abgleich nach Rolle |
| Tabellen | Aktive KI-Extraktion; passende Spalten; geprüftes Lieferantenmodell und etwaige klassische Regeln |
| Bestellung | ACADEMY-PO-003 beziehungsweise ACADEMY-PO-030 in derselben Gesellschaft und Organisation wie die Rechnung |
| Kostenstellen | Drei gültige Test-IDs für IT, Verwaltung und Vertrieb sowie passende Sachkonten und Steuerkennzeichen |
| Freigabe | Zwei unterschiedliche berechtigte Testrollen, eindeutige Routingbedingungen und geprüfte Exportsperre |
| Export | Getrenntes LN- oder M3-Testziel und Zugriff zur Prüfung des tatsächlichen Zielbelegs |

Die Musterbelege verwenden **Muster IT Services GmbH** ausschließlich als fiktiven Schulungslieferanten. Ordnen Sie ihn dem dafür vorbereiteten Testlieferanten zu. Lieferant, Währung, Gesellschaft, Einheiten und Preiseinheit müssen bei Rechnung und Bestellung zueinander passen. Eine vorhandene fremde Bestellung mit ähnlichen Beträgen ist kein Ersatz.

## Alle Unterlagen herunterladen

{% file src="../.gitbook/assets/academy-de-v1/academy-uebungspaket-de-v1.zip" %}
Alle PDFs, Excel-Datei, Bestellreferenzen und Sollwerte einschließlich Dateiprüfsummen.
{% endfile %}

| Datei | Zweck |
| --- | --- |
| rechnung-ohne-bestellung.pdf | Tutorial 1 und Exportdiagnose: 1.000 EUR netto, 1.190 EUR brutto |
| rechnung-preisabweichung.pdf | Tutorial 2: 1.325 EUR netto, Preisabweichung bei ART-B |
| rechnung-kostenstellen.pdf | Tutorial 3: 3.000 EUR netto für 50/30/20-Aufteilung |
| rechnung-freigabe.pdf | Tutorial 4: exakt 12.000 EUR brutto als Freigabebasis |
| rechnung-30-positionen.pdf | Tutorial 6 und kompletter PO-Fall mit 30 Positionen auf drei Seiten |
| rechnung-ohne-linien.pdf | Gleiche drei Artikel wie Tutorial 2, ohne Rahmenlinien |
| rechnung-spaltenreihenfolge.pdf | Einzelpreis und Menge in anderer Reihenfolge |
| rechnung-rabatt-zuschlag.pdf | 25 EUR Rabatt und 20 EUR Fracht, 1.320 EUR netto |
| rechnung-30-positionen-scan.pdf | Bildbasierte PDF mit denselben drei Seiten |
| rechnung-30-positionen.xlsx | 30 Positionen mit Formeln und Summen zum Formatvergleich |
| bestellreferenzen.json | Lesbare Bestell-Sollwerte für Administratoren |
| belege-und-sollwerte.json | Originaldaten und erwartete Werte, keine aufgezeichneten Verarbeitungsergebnisse |
| konfigurationsreferenz.json | Toleranz-Testwerte, Kostenstellenaufteilung, Freigabegrenzen und Vorlage zur Feldmapping-Prüfung |
| pruefsummen.json | SHA-256 der enthaltenen Übungsdateien |

{% file src="../.gitbook/assets/academy-de-v1/konfigurationsreferenz.json" %}
Konfigurationsreferenz für die vorbereitende Prüfung durch Ihren Administrator.
{% endfile %}

Die Konfigurationsreferenz ist kein importierbares DocBits-Regelwerk. Sie hält die fachlichen Testvorgaben fest. Tragen Sie beim Mapping-Vergleich die tatsächlichen DocBits-Schlüssel und ERP-Zielfelder Ihrer Integration ein. Die mit `null` markierten Angaben müssen vor einem Export geklärt werden.

## Bestellungen bereitstellen

`bestellreferenzen.json` ist **kein direkt importierbares DocBits-API-Schema**. Ein Administrator überführt die enthaltenen Werte in den eingerichteten Stammdatenimport und prüft danach die verfügbaren Bestellpositionen in DocBits. Die Lieferung von Referenzwerten allein belegt keinen erfolgreichen Import.

## Ergebnisse festhalten

Notieren Sie pro Übung Umgebung, angezeigte Produktversion, Rolle, Dokument-ID, Originalwerte, gespeicherte Werte nach erneutem Öffnen und das tatsächliche Ergebnis. Ergänzen Sie bei PO-Fällen aktive Regelversion und Toleranzen, bei Freigaben beide Entscheidungen und bei Exporten die fachliche Antwort und den Zielbeleg.

Bei einer nicht verfügbaren Funktion endet der Nachweis vor diesem Schritt. Kennzeichnen Sie ihn als offen. Nach dem Test stellen Sie geänderte Testkonfigurationen wieder her und behandeln Sie Testbelege nach Ihrem vereinbarten Aufbewahrungsprozess.

[Abnahmekriterien](qualitaet-und-abnahme.md) · [Academy](README.md)
