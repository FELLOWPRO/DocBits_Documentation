# Automatischer Bestelldaten-Abgleich

Docbits ist ein fortschrittliches System, das entwickelt wurde, um den Abgleich von Bestelldaten (POs) mit eingehenden Rechnungsdokumenten zu automatisieren. Dieses Tool wurde speziell für die effiziente Verwaltung und Verarbeitung von Rechnungsdaten innerhalb von ERP-Systemen entwickelt. Diese Dokumentation erläutert die Grundlagen des automatischen Abgleichs durch Docbits und definiert die spezifischen Regeln, die für einen erfolgreichen Abgleich erforderlich sind.

<figure><img src="../../../.gitbook/assets/Automatic Purchase Order Data Matching.svg" alt=""><figcaption></figcaption></figure>

## **Grundprinzipien des automatischen Abgleichs in Docbits**

**Datenextraktion:** Docbits beginnt den Prozess mit der Extraktion relevanter Daten aus digitalisierten Rechnungsdokumenten. Typischerweise umfassen diese Daten Artikelnummern, Mengen und Stückpreise jeder Rechnungsposition. Die Präzision dieser Extraktion ist entscheidend, da sie die Grundlage für den nachfolgenden Abgleichsprozess bildet.

**Vergleich mit PO-Daten:** Die extrahierten Daten werden mit den entsprechenden Informationen in den hinterlegten Bestellungen verglichen. Docbits prüft, ob die Artikelnummern, Mengen und Preise mit denen in den Bestellungen übereinstimmen. Für einen erfolgreichen Abgleich müssen die Daten in den Rechnungen unter Berücksichtigung definierter Toleranzschwellen den Daten in den Bestellungen entsprechen.

**Automatischer Abgleich:** Auf Grundlage der Vergleichsergebnisse führt Docbits den Abgleich durch. Das System überprüft, ob die Abgleichskriterien innerhalb der festgelegten Toleranzgrenzen liegen. Sind diese Kriterien erfüllt, gilt der Abgleich als erfolgreich.

**Berichterstattung:** Nach Abschluss des Abgleichsprozesses erstellt Docbits Berichte, die den Status der Abgleiche anzeigen. Diese Berichte informieren über erfolgreich abgeglichene Rechnungen und identifizieren solche mit Abweichungen.

## **Definition der Abgleichsregeln**

**Artikelnummer:** Die Artikelnummer auf der Rechnung muss exakt mit der Artikelnummer in der Bestellung übereinstimmen. Für Abweichungen bei Artikelnummern gibt es keine Toleranz.

**Mengen:** Die auf der Rechnung gelieferte Warenmenge darf innerhalb eines vordefinierten Toleranzbereichs variieren. Typischerweise könnte eine Toleranz von ±5 % akzeptabel sein, um geringfügige Unterschiede bei den Liefermengen zu berücksichtigen.

**Preise:** Preisabweichungen sind bis zu einem festgelegten Schwellenwert tolerierbar. Eine gängige Toleranz könnte ±2 % des Preises betragen, um geringfügige Unterschiede bei den Preisangaben zu akzeptieren, die durch Rundungsdifferenzen oder Währungsschwankungen entstehen.

## **Abgleichsstatus:**

* **Vollständige Übereinstimmung (Full Match):** Alle Datenpunkte (Artikelnummer, Menge und Preis) liegen innerhalb der festgelegten Toleranzgrenzen.
* **Teilweise Übereinstimmung (Partial Match):** Ein oder mehrere Datenpunkte weichen außerhalb der Toleranzgrenzen ab, die Abweichungen sind jedoch minimal und erfordern eine manuelle Prüfung.
* **Keine Übereinstimmung (No Match):** Erhebliche Abweichungen bei einem oder mehreren Datenpunkten, die eine sofortige Korrektur oder weitere Untersuchung erfordern.

Die präzise Definition dieser Regeln und die Festlegung der Toleranzgrenzen sind entscheidend für die Effizienz des automatischen Abgleichs und die Reduzierung manueller Eingriffe. Docbits ermöglicht eine flexible Konfiguration dieser Parameter, um den Anforderungen verschiedener Unternehmen und Branchen gerecht zu werden.
