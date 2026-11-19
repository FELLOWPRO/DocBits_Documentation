# Dokumentenverarbeitung

Die **Dokumentenverarbeitung** steuert, wie DocBits Dokumente liest, mit weiteren Daten anreichert und exportiert. Öffnen Sie die **Einstellungen** und wählen Sie unter **Dokumentenverarbeitung** den passenden Bereich.

* [OCR-Einstellungen](ocr-settings.md): wie Text aus Dokumenten gelesen wird.
* [Stammdaten-Lookup](master-data-lookup.md): wie extrahierte Werte mit Ihren Stammdaten abgeglichen werden.
* [Fälligkeitsberechnung](due-date-calculation.md): wie Fälligkeiten ermittelt werden.
* [Export](export.md): wohin und wie verarbeitete Dokumente exportiert werden.

Öffnen Sie zum Beispiel **OCR-Einstellungen**, um die **Allgemeinen OCR-Einstellungen** zu prüfen. **E-Text verwenden, falls verfügbar** nutzt eingebetteten elektronischen Text. **DESKEW verwenden, wenn verfügbar** richtet gescannte Seiten gerade aus. **AI OCR Version** wählt die Version der Texterkennung aus. Einzelheiten zu den Steuerelementen finden Sie unter [OCR-Einstellungen](ocr-settings.md#allgemeine-ocr-einstellungen).

<figure><img src="../../../.gitbook/assets/dbdc-233-general-ocr-settings-de-20261031.png" alt="Allgemeine OCR-Einstellungen in der deutschen DocBits-Oberfläche mit E-Text-, DESKEW- und AI-OCR-Version-Steuerelementen"><figcaption><p>Die allgemeinen OCR-Einstellungen sind ein Bereich der Dokumentenverarbeitung. Die gewählten Werte hängen von Ihrer Organisation ab.</p></figcaption></figure>

Weitere Bereiche sind [Importieren](import/README.md), [Klassifizierung und Extraktion](classification-and-extraction/README.md), [Regelverwaltung](rule-manager/README.md), [Wertelisten](list-of-values.md) und [Modul](module/README.md).

Wenn Sie ein Problem beheben möchten, beginnen Sie bei dem Schritt, an dem Sie das Problem sehen, statt mehrere Einstellungen auf einmal zu ändern:

| Was Sie prüfen möchten | Anleitung |
| --- | --- |
| Text fehlt oder wird falsch gelesen | [OCR-Einstellungen](ocr-settings.md) |
| Ein Wert soll mit Referenzdaten verglichen werden | [Stammdaten-Lookup](master-data-lookup.md) oder [Wertelisten](list-of-values.md) |
| Eine Fälligkeit ist unerwartet | [Fälligkeitsberechnung](due-date-calculation.md) |
| Ein Dokument soll DocBits verlassen | [Export](export.md) |
| Eine Regel soll ein Dokument weiterleiten oder ändern | [Entscheidungsbäume](decision-trees.md) |

Wenn sich eine Einstellung nicht wie erwartet verhält, prüfen Sie sie zuerst mit einem Testdokument. Eine Änderung kann jedes neue Dokument der Organisation betreffen.
