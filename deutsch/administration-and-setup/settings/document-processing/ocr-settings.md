# OCR-Einstellungen

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR & E-Text Explained: Settings, Quality & Header Extraction
{% endembed %}

## Übersicht

In den **OCR (Optische Zeichenerkennung)**-Einstellungen können Sie konfigurieren, wie OCR während der Verarbeitung von Dokumenten angewendet wird. Dazu gehört die Festlegung der erforderlichen Mindestqualität, die Auswahl, ob eingebetteter Text (E-Text) verwendet werden soll, die Auswahl der OCR-Version und mehr. Diese Seite bietet eine detaillierte Erklärung aller verfügbaren Einstellungen.

## So greifen Sie auf die OCR-Einstellungen zu

Um auf die OCR-Einstellungen zuzugreifen:

*   Navigieren Sie zu: **Einstellungen** → **Verarbeitung von Dokumenten** → **OCR-Einstellungen**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)

## OCR-Qualität

In diesem Abschnitt können Sie die Mindestqualität des Dokuments festlegen, die für die OCR-Verarbeitung erforderlich ist, indem Sie den Qualitätsregler anpassen. Bewegen Sie den Regler nach links oder rechts, um die Qualitätsgrenze zu verringern oder zu erhöhen.

Wenn ein Dokument das definierte Qualitätsniveau nicht erfüllt, bietet DocBits drei Optionen für den Umgang damit:

* **Lauf trotzdem**\
  Das Dokument wird unabhängig von seiner Qualität verarbeitet.
* **Nach Bestätigung erneut ausführen**\
  **DocBits** pausiert und fordert Sie auf, zu bestätigen, ob die Verarbeitung fortgesetzt werden soll.
* **Fehler auslösen**\
  Die Verarbeitung des Dokuments wird vollständig gestoppt, und eine Fehlermeldung wird angezeigt, die darauf hinweist, dass das Dokument das erforderliche Qualitätsniveau nicht erfüllt hat.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_1.png)

## Allgemeine OCR-Einstellungen

* **E-Text verwenden, falls verfügbar**\
  Wenn aktiviert, verwendet **DocBits** eingebetteten elektronischen Text (z. B. aus PDFs) anstelle der Durchführung von OCR. Dies verbessert sowohl die Geschwindigkeit als auch die Genauigkeit, da der Text direkt extrahiert wird, ohne dass eine OCR-Verarbeitung erforderlich ist.
* **DESKEW verwenden, wenn verfügbar**\
  Diese Option korrigiert automatisch die Ausrichtung von gescannten Dokumenten. Das Begradigen schiefer Bilder hilft, die OCR-Genauigkeit zu verbessern.
*   **AI OCR Version**\
    Ermöglicht Ihnen die Auswahl einer bestimmten Version der KI-basierten OCR-Engine.\
    Dies kann nützlich sein, wenn:

    * Sie mit der derzeit ausgewählten Version nicht die gewünschten Ergebnisse erzielen.
    * Sie Probleme im Zusammenhang mit der OCR-Leistung oder -Genauigkeit beheben.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ocr_settings_2.png)

## OCR-Einstellungen für Tabellen

* **Verwenden Sie AI-Daten für Tabellen, falls verfügbar**\
  Wenn aktiviert, verwendet DocBits OCR-Daten für Tabellen anstelle von eingebettetem elektronischen Text (E-Text) – selbst wenn die Einstellung **E-Text verwenden, falls verfügbar** aktiviert ist.

## OCR-Einstellungen für Headerfelder

* **Extraktion von Regeln verwenden**\
  DocBits wendet Ihre vordefinierten Extraktionsregeln zur Identifizierung von Headerfeldern an.
* **KI-Extraktion verwenden**\
  DocBits verwendet KI, um Headerfelder automatisch zu erkennen und zu extrahieren.

**Ausführungsreihenfolge:**\
Wenn beide Optionen aktiviert sind, führt **DocBits** die Extraktion in folgender Reihenfolge durch:\
**Extraktion von Regeln → KI-Extraktion**\
\
<mark style="color:red;">**Hinweis**</mark>: Für die besten Ergebnisse und ein konsistentes Verhalten aktivieren Sie beide Optionen. Dies ermöglicht **DocBits**, sowohl regelbasierte als auch KI-basierte Methoden in Kombination während der Header-Extraktion zu verwenden.
