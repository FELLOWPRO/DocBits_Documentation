# Validierungs-Setup und akzeptierte Versionen

Diese Seite erklärt den Setup-Assistenten, die akzeptierten XRechnung-Versionen und die akzeptierten Profile der Seite [E-Rechnungs-Prüfung](./). Nur Organisationsadministratoren können diese Einstellungen ändern.

## Validierungs-Setup

<figure><img src="../../../../../.gitbook/assets/einvoice-setup-versions-de-20261104.png" alt="Akzeptierte XRechnung-Versionen in der Dev-Beispielorganisation. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche."><figcaption><p>Akzeptierte XRechnung-Versionen in der Dev-Beispielorganisation. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche.</p></figcaption></figure>

Die Karte **Validation Setup** zeigt Ihr aktuelles Validierungsprofil (zum Beispiel *B2G – Public Sector Receiver*). Klicken Sie auf **Edit answers**, um den Setup-Assistenten erneut auszuführen und den Standard zu ändern, gegen den validiert wird.

## Akzeptierte XRechnung-Versionen

Das Gate **Accepted XRechnung versions** listet jede XRechnung-Version auf. Markieren Sie die Versionen, die Sie akzeptieren – Dokumente, deren CustomizationID außerhalb dieser Liste liegt, werden bereits vor jeder weiteren Prüfung mit `VAL-VERSION-NOT-ALLOWED` abgelehnt. Eine leere Liste bedeutet „alles akzeptieren". Jede Version ist mit **current**, **deprecated** oder **EOL** sowie ihrem Veröffentlichungsdatum gekennzeichnet.

## Akzeptierte Profile und Schweregrad-Modell

<figure><img src="../../../../../.gitbook/assets/einvoice-profiles-severity-de-20261104.png" alt="Akzeptierte ZUGFeRD- und Factur-X-Profile. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche."><figcaption><p>Akzeptierte ZUGFeRD- und Factur-X-Profile. Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche.</p></figcaption></figure>

Wählen Sie über **Accept all** / **Clear** und anschließend **Save**, welche **Profile** Sie akzeptieren (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)).

Jede Validierungsregel hat einen **Severity**, der bestimmt, was beim Auslösen geschieht:

| Schweregrad | Auswirkung |
|-------------|------------|
| **FATAL** | Beendet den aktuellen Prüfschritt, wenn der Fehler weitere Prüfungen verhindert. Ob die Prüfung die Dokumentverarbeitung blockiert, hängt zusätzlich von **Blocking** am Dokumenttyp ab. |
| **ERROR** | Ein Validierungsfehler. Bei eingeschaltetem **Blocking** erhält das Dokument den Status **Error**. Das ist getrennt von der manuellen Aktion **Reject document**. |
| **WARNING** | Erscheint im Validierungsbericht, das Dokument durchläuft die Pipeline jedoch normal. |
| **INFO** | Ein Hinweis im Prüfbericht. Er blockiert das Dokument nicht. |

### Was der Assistent ändert

Die Karte **Validation Setup** weiter unten auf der Seite öffnet mit **Edit answers** einen Assistenten. Der Assistent ersetzt alle Regel-Überschreibungen Ihrer Organisation. DocBits warnt Sie vor dem Speichern. Prüfen Sie den Schritt **Review and apply** sorgfältig.

Weiter: [Regel-Schweregrade](validation-rule-severities.md) und [Prüfung je Dokumenttyp](validation-per-document-type.md).
