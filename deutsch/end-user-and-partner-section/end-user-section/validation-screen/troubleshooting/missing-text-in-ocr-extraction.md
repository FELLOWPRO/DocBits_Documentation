# Fehlender Text in der OCR-Extraktion

## **Problem**

In einigen Fällen kann es vorkommen, dass Text in der **OCR-Ansicht** zu fehlen scheint, was die Extraktion mit der Extraktionsfunktion verhindert.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_5.png)

Um dies zu überprüfen, klicken Sie auf die Schaltfläche **OCR-Ansicht** in der Symbolleiste auf der rechten Seite. Wenn der Text dort nicht angezeigt wird, bedeutet dies, dass er nicht für die Extraktion verfügbar ist.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_6.png)

## **Ursache**

Die wahrscheinlichste Ursache ist, dass der Text, den Sie extrahieren möchten, Teil eines Bildes (z. B. eines Logos oder eines gescannten Abschnitts) innerhalb des Dokuments ist.\
Wenn die E-Text-Funktion aktiviert ist, wird Text, der auf Bildern oder Logos erscheint, nicht in die extrahierte Textebene aufgenommen. Daher kann dieser Text nicht über die standardmäßige Extraktionslogik zugegriffen oder extrahiert werden.

## **Lösung**

Um dieses Problem zu beheben, deaktivieren Sie die E-Text-Funktion—entweder für den [spezifischen Anbieter](missing-text-in-ocr-extraction.md#e-text-fur-einen-bestimmten-anbieter-deaktivieren) oder für die [gesamte Organisation](missing-text-in-ocr-extraction.md#e-text-fur-die-gesamte-organisation-deaktivieren). Sobald E-Text deaktiviert ist, wird DocBits ausschließlich auf OCR angewiesen sein, das in der Lage ist, Text aus Bildern und Logos innerhalb des Dokuments zu extrahieren.

### **E-Text für einen bestimmten Anbieter deaktivieren**

1. Öffnen Sie ein Dokument vom spezifischen Anbieter in der **Feldvalidierung**.
2.  Klicken Sie auf das Drei-Punkte-Menü in der Symbolleiste auf der rechten Seite.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_2.png)
3.  Deaktivieren Sie die Option **E-Text verwenden, falls verfügbar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_3.png)
4.  Klicken Sie auf **Bestätigen**, um die Verarbeitung für das Dokument neu zu starten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_4.png)

### E-Text für die gesamte Organisation deaktivieren

1.  Gehen Sie zu **Einstellungen → Verarbeitung von Dokumenten → OCR-Einstellungen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)
2.  Deaktivieren Sie unter **Allgemeine OCR-Einstellungen** die Option **E-Text verwenden, falls verfügbar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_1.png)
