# Leistungsmetriken

<figure><img src="../.gitbook/assets/performance-metrics-business-de-20261111.png" alt="Seite Leistungsmetriken in der deutschen Oberfläche mit dem Filter Zeiteinheit, den Schaltflächen Filter und Löschen, den Registerkarten Geschäftsansicht und IT-Ansicht sowie den Diagrammen Durchschnittliche Dauer, Durchschnittliche Dauer für andere Organisationen und Leistungsübersicht"><figcaption><p>Die Seite Leistungsmetriken öffnet sich auf der Registerkarte Geschäftsansicht. Die gezeigten Zahlen stammen aus einer synthetischen Beispielorganisation und weichen in Ihrer Organisation ab.</p></figcaption></figure>

**Leistungsmetriken** zeigt, wie lange Dokumente in den einzelnen Verarbeitungsschritten verweilen und wie oft jeder Dienst läuft. Nutzen Sie die Seite, um Fragen zu beantworten wie „Welcher Schritt ist nach der Validierung am langsamsten?“ oder „Wie hat sich unser Verarbeitungsvolumen in den letzten Wochen entwickelt?“

## Aufrufen

Leistungsmetriken hat keinen Eintrag in der Seitenleiste der Einstellungen. Öffnen Sie die Seite auf einem dieser Wege:

1. **Sitemap**: Klicken Sie unten in der linken Seitenleiste auf das Lupensymbol, geben Sie „Performance“ in das Suchfeld ein und klicken Sie in der Gruppe **Einstellungen — Erweitert** auf den Eintrag **Performance-Kennzahlen**. Siehe [Sitemap](../end-user-and-partner-section/end-user-section/sitemap.md).
2. **Globale Schnellsuche**: Drücken Sie an beliebiger Stelle in der App <kbd>Ctrl</kbd> + <kbd>K</kbd> (unter macOS <kbd>Cmd</kbd> + <kbd>K</kbd>), geben Sie „Performance“ ein und öffnen Sie den Eintrag mit <kbd>Enter</kbd>. Siehe [Globale Schnellsuche](../end-user-and-partner-section/end-user-section/global-quick-search.md).
3. Direkt über die Adresse `/settings/performance-metrics`. Die ältere Adresse `/performance_report` öffnet weiterhin dieselbe Seite.

Die Seite ist für Administratoren gedacht. Die gezeigten Zahlen stammen aus einer synthetischen Beispielorganisation und weichen in Ihrer Organisation ab.

## Filter

Die Filter über den Registerkarten legen den Zeitraum fest und — auf der Registerkarte IT-Ansicht — die Dienste, deren Zahlen Sie sehen möchten.

| Filter | Beschreibung |
|--------|-------------|
| **Zeiteinheit** | Wählen Sie den Zeitraum: **Letzte 7 Tage**, **Letzte 30 Tage** oder **Zeitbereich wählen** für einen eigenen Zeitraum. Klicken Sie für einen eigenen Zeitraum auf das Kalendersymbol, wählen Sie den ersten und den letzten Tag und bestätigen Sie mit **Ok**. |
| **Microservice** | Nur auf der Registerkarte **IT-Ansicht** sichtbar. Wählen Sie einen einzelnen Dienst (zum Beispiel OCR), um nur dessen Zahlen zu sehen. Lassen Sie das Feld leer, um alle Dienste zu sehen. |
| **Zeitgruppen (nur für Frequenz)** | Nur auf der Registerkarte **IT-Ansicht** sichtbar. Gruppiert das Diagramm Prozesshäufigkeit nach Stunde, Tag, Woche oder Monat. |
| **Filter** | Wendet die gewählten Filter an und zeichnet die Diagramme neu. |
| **Löschen** | Entfernt alle Filter und zeigt wieder die Standardansicht. |

Die Diagramme aktualisieren sich nicht von selbst, wenn Sie einen Filter ändern — klicken Sie danach auf **Filter**.

## Geschäftsansicht

Die Registerkarte **Geschäftsansicht** beantwortet die fachliche Frage: Wie lange wartet ein Dokument an jedem Verarbeitungsschritt? Sie zeigt drei Diagramme:

| Diagramm | Beschreibung |
|----------|-------------|
| **Durchschnittliche Dauer** | Durchschnittliche Zeit pro Schritt in Ihrer Organisation, von **Validierung bis bereit** über **Bereit zur Validierung**, **Von validiert bis genehmigt** und **Zweite Genehmigung bis zur Genehmigung** bis **Genehmigt bis Fertig**. |
| **Durchschnittliche Dauer für andere Organisationen** | Dieselben Schritte für andere Organisationen, damit Sie Ihre Zeiten mit deren vergleichen können. |
| **Leistungsübersicht** | Kürzeste (**Minimum**) und längste (**Maximum**) Zeit pro Schritt — hilfreich, um Ausreißer zu erkennen. |

Zeiten werden in Stunden, Minuten und Sekunden angezeigt. Es sind Durchschnittswerte — ein einzelnes Dokument kann schneller oder langsamer sein.

## IT-Ansicht

<figure><img src="../.gitbook/assets/performance-metrics-it-de-20261111.png" alt="Seite Leistungsmetriken, Registerkarte IT-Ansicht in der deutschen Oberfläche mit den Filtern Microservice und Zeitgruppen, dem Diagramm Durchschnittliche Dauer pro Dienst, dem Diagramm Prozesshäufigkeit über die Zeit und der Leistungsübersicht mit Minimum und Maximum"><figcaption><p>Die IT-Ansicht schlüsselt dieselben Daten nach Diensten auf. Mit dem Filter Microservice können Sie sich auf einen Dienst konzentrieren.</p></figcaption></figure>

Die Registerkarte **IT-Ansicht** beantwortet die technische Frage: Welcher Dienst benötigt wie viel Zeit und wie oft läuft er? Sie zeigt drei Diagramme:

| Diagramm | Beschreibung |
|----------|-------------|
| **Durchschnittliche Dauer** | Durchschnittliche Verarbeitungszeit pro Dienst: **OCR**, **Klassifizierung**, **Extraktion** und **Exportieren**. |
| **Prozesshäufigkeit** | Wie viele Dokumente jeder Dienst im gewählten Zeitraum verarbeitet hat, gruppiert nach der Einstellung **Zeitgruppen**. |
| **Leistungsübersicht** | Kürzeste (**Minimum**) und längste (**Maximum**) Verarbeitungszeit pro Dienst — hilfreich, um Ausreißer zu erkennen. |

Jedes Diagramm hat oben rechts ein Download-Menü (Download SVG, Download PNG, Download CSV), sodass Sie ein Diagramm für einen Bericht oder einen Supportfall exportieren können.

## Tipps

* Beginnen Sie mit der **Geschäftsansicht**, um zu sehen, wo Dokumente am längsten warten; wechseln Sie zur **IT-Ansicht**, um zu erkennen, welcher Dienst dafür verantwortlich ist.
* Eine lange Zeit bei **Validierung bis bereit** oder **Von validiert bis genehmigt** deutet meist auf manuelle Arbeit hin (Dokumente warten auf die Prüfung), während lange OCR- oder Extraktionszeiten auf systemseitige Verarbeitung hindeuten.
* Wenn ein Diagramm keine Daten zeigt, erweitern Sie den Zeitraum unter **Zeiteinheit** oder klicken Sie auf **Löschen** und versuchen Sie es erneut.

## Verwandte Seiten

* [Analyse-Dashboard](analytics-dashboard.md) — detaillierte Verarbeitungszeiten pro Dokument, Lieferant und Dokumenttyp.
* [Aktivitätsprotokollierung](settings/log-settings/README.md) — das zugrunde liegende Ereignisprotokoll mit Filtern und Export.
* [Berichtsseite](report-page.md) — Dokumentanzahlen, geänderte Felder und Exportstatistiken.
