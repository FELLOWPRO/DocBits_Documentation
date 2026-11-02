# Fehlender Text in der OCR-Extraktion

Die Abbildungen zeigen den Prüfablauf an einer fiktiven Rechnung mit vorhandenem OCR-Text. Sie stellen keinen reproduzierten Fall mit fehlendem Text dar.

## **Problem**

In einigen Fällen kann es vorkommen, dass Text in der **OCR-Ansicht** zu fehlen scheint, was die Extraktion mit der Extraktionsfunktion verhindert.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_5-de.png" alt="Validierungsansicht zur Kontrolle erkannter Felder an einer fiktiven deutschen Rechnung."><figcaption><p>Validierungsansicht zur Kontrolle erkannter Felder an einer fiktiven deutschen Rechnung.</p></figcaption></figure>

Um dies zu überprüfen, klicken Sie auf die Schaltfläche **OCR-Ansicht** in der Symbolleiste auf der rechten Seite. Wenn der Text dort nicht angezeigt wird, bedeutet dies, dass er nicht für die Extraktion verfügbar ist.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_6-de.png" alt="OCR-Ansicht mit erkanntem Text der fiktiven deutschen Rechnung."><figcaption><p>OCR-Ansicht mit erkanntem Text der fiktiven deutschen Rechnung.</p></figcaption></figure>

## **Ursache**

Eine mögliche Ursache ist, dass der Text, den Sie extrahieren möchten, Teil eines Bildes (z. B. eines Logos oder eines gescannten Abschnitts) innerhalb des Dokuments ist.\
Wenn die E-Text-Funktion aktiviert ist, wird Text, der auf Bildern oder Logos erscheint, nicht in die extrahierte Textebene aufgenommen. Daher kann dieser Text nicht über die standardmäßige Extraktionslogik zugegriffen oder extrahiert werden.

## **Lösung**

Um dieses Problem zu beheben, deaktivieren Sie die E-Text-Funktion—entweder für den [spezifischen Anbieter](missing-text-in-ocr-extraction.md#e-text-fur-einen-bestimmten-anbieter-deaktivieren) oder für die [gesamte Organisation](missing-text-in-ocr-extraction.md#e-text-fur-die-gesamte-organisation-deaktivieren). Nach der Umstellung und erneuten Verarbeitung prüfen Sie die OCR-Ansicht nochmals. Ob Bildtext erkannt wird, hängt auch von Qualität und Aufbau des Dokuments ab.

### **E-Text für einen bestimmten Anbieter deaktivieren**

1. Öffnen Sie ein Dokument vom spezifischen Anbieter in der **Feldvalidierung**.
2.  Klicken Sie auf das Drei-Punkte-Menü in der Symbolleiste auf der rechten Seite.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_2-de.png" alt="Weitere Optionen der Feldvalidierung öffnen."><figcaption><p>Weitere Optionen der Feldvalidierung öffnen.</p></figcaption></figure>

3.  Deaktivieren Sie die Option **E-Text verwenden, falls verfügbar**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_3-de.png" alt="Option E-Text verwenden, falls verfügbar im Dokumentmenü."><figcaption><p>Option E-Text verwenden, falls verfügbar im Dokumentmenü.</p></figcaption></figure>

4.  Klicken Sie auf **Bestätigen**, um die Verarbeitung für das Dokument neu zu starten.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_4-de.png" alt="Bestätigungsdialog vor einer Änderung der E-Text-Verwendung."><figcaption><p>Bestätigungsdialog vor einer Änderung der E-Text-Verwendung.</p></figcaption></figure>

### E-Text für die gesamte Organisation deaktivieren

1.  Gehen Sie zu **Einstellungen → Verarbeitung von Dokumenten → OCR-Einstellungen**.

<figure><img src="../../../../.gitbook/assets/s150-settings_ocr-de.png" alt="OCR-Einstellungen in der deutschen Oberfläche."><figcaption><p>OCR-Einstellungen in der deutschen Oberfläche.</p></figcaption></figure>

2.  Deaktivieren Sie unter **Allgemeine OCR-Einstellungen** die Option **E-Text verwenden, falls verfügbar**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_1-de.png" alt="Allgemeine OCR-Einstellungen mit der Option zur Verwendung von E-Text."><figcaption><p>Allgemeine OCR-Einstellungen mit der Option zur Verwendung von E-Text.</p></figcaption></figure>
