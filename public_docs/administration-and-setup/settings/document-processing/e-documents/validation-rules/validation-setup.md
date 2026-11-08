# Validierungs-Setup und akzeptierte Versionen

Diese Seite erklärt den Setup-Assistenten, die akzeptierten XRechnung-Versionen und die akzeptierten Profile der Seite [E-Rechnungs-Prüfung](README.md). Nur Organisationsadministratoren können diese Einstellungen ändern.

## Validierungs-Setup

<figure><img src="../../../../../.gitbook/assets/einvoice-setup-versions-de-20261104.png" alt="Akzeptierte XRechnung-Versionen in der Dev-Beispielorganisation. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche."><figcaption><p>Akzeptierte XRechnung-Versionen in der Dev-Beispielorganisation. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche.</p></figcaption></figure>

Die Karte **Validierungs-Setup** zeigt Ihr aktuelles Validierungsprofil (zum Beispiel *B2G – Public Sector Receiver*). Klicken Sie auf **Antworten bearbeiten**, um den Setup-Assistenten erneut auszuführen und den Standard zu ändern, gegen den validiert wird.

## Akzeptierte XRechnung-Versionen

Das Gate **Akzeptierte XRechnung-Versionen** listet jede XRechnung-Version auf. Markieren Sie die Versionen, die Sie akzeptieren – Dokumente, deren CustomizationID außerhalb dieser Liste liegt, werden bereits vor jeder weiteren Prüfung mit `VAL-VERSION-NOT-ALLOWED` abgelehnt. Eine leere Liste bedeutet „alles akzeptieren". Jede Version ist mit **current**, **deprecated** oder **EOL** sowie ihrem Veröffentlichungsdatum gekennzeichnet.

## Akzeptierte Profile und Schweregrad-Modell

<figure><img src="../../../../../.gitbook/assets/einvoice-profiles-severity-de-20261104.png" alt="Akzeptierte ZUGFeRD- und Factur-X-Profile. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche."><figcaption><p>Akzeptierte ZUGFeRD- und Factur-X-Profile. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche.</p></figcaption></figure>

Wählen Sie über **Alle akzeptieren** / **Leeren** und anschließend **Speichern**, welche **Profile** Sie akzeptieren (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)).

Jede Validierungsregel hat einen **Schweregrad**, der bestimmt, was beim Auslösen geschieht:

| Schweregrad | Auswirkung |
|-------------|------------|
| **FATAL** | Beendet den aktuellen Prüfschritt, wenn der Fehler weitere Prüfungen verhindert. Ob die Prüfung die Dokumentverarbeitung blockiert, hängt zusätzlich von **Blockierend** am Dokumenttyp ab. |
| **ERROR** | Ein Validierungsfehler. Bei eingeschaltetem **Blockierend** erhält das Dokument den Status **Fehler**. Das ist getrennt von der manuellen Aktion **Dokument ablehnen**. |
| **WARNING** | Erscheint im Validierungsbericht, das Dokument durchläuft die Pipeline jedoch normal. |
| **INFO** | Ein Hinweis im Prüfbericht. Er blockiert das Dokument nicht. |

### Was der Assistent ändert

Die Karte **Validierungs-Setup** weiter unten auf der Seite öffnet mit **Antworten bearbeiten** einen Assistenten. Der Assistent ersetzt alle Regel-Überschreibungen Ihrer Organisation. DocBits warnt Sie vor dem Speichern. Prüfen Sie den Schritt **Überprüfen und anwenden** sorgfältig.

Weiter: [Regel-Schweregrade](validation-rule-severities.md) und [Prüfung je Dokumenttyp](validation-per-document-type.md).
