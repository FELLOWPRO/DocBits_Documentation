# Barcode-Extraktion

## Übersicht

Diese Funktion ermöglicht die automatische Erkennung von Barcodes auf Dokumenten. Wenn sie aktiviert ist, werden bei der Verarbeitung alle unterstützten Barcode-Typen gescannt und extrahiert.

## So aktivieren Sie die Barcode-Extraktion

Um die Funktion Bar-Code Extraction zu aktivieren, gehen Sie wie folgt vor:

1. **Zu den Einstellungen navigieren**:
   * Gehen Sie im Dashboard zu **Settings**.
   * Wählen Sie **Document Processing** und anschließend **Module**.
2. **Die Funktion aktivieren**:
   * Scrollen Sie nach unten bis zur Option **Bar-Code Extraction**.
   * Schalten Sie den Schieberegler ein, um die Barcode-Extraktion zu aktivieren.\\

## **Zusätzliche Einstellungen**

### **Barcode-Zuweisung**

#### **Zweck:** Ermöglicht Prüfern, einen extrahierten Barcode-Wert während der Feldvalidierung manuell einem bestimmten Dokumentfeld zuzuweisen.

#### So aktivieren Sie die **Barcode Assignment**

Um die Funktion **Barcode Assignment** zu aktivieren, gehen Sie wie folgt vor:

1. **Zu den Einstellungen navigieren**:
   * Gehen Sie im Dashboard zu **Settings**.
   * Wählen Sie **Document Processing** und anschließend **Module**.
2. **Die Funktion aktivieren**:
   * Scrollen Sie nach unten bis zur Option **Barcode Assignment**.
   * Schalten Sie den Schieberegler ein, um **Barcode Assignment** zu aktivieren.\\

#### **So funktioniert es:**

* Aktiviert im Validierungsbildschirm für Felder die Option „Assign Barcode“.\\
* Benutzer können einen erkannten Barcode-Wert auswählen und einem Dokumentfeld wie PO Number oder Invoice Number zuordnen.\\

### Aufteilung von Dokumenten per Barcode / QR-Code

**Zweck:** Teilt mehrseitige Dokumente automatisch in separate Dokumente auf, wenn bestimmte Barcodes oder QR-Codes vorhanden sind.

#### So aktivieren Sie die Aufteilung von Dokumenten per Barcode / QR-Code

Um die Funktion **Split of Document by Barcode / QR Code** zu aktivieren, gehen Sie wie folgt vor:

1. **Zu den Einstellungen navigieren**:
   * Gehen Sie im Dashboard zu **Settings**.
   * Wählen Sie **Document Processing** und anschließend **Classification and Extraction**.
2. **Die Funktion aktivieren**:
   * Suchen Sie die Option **Document Splitting**.
   * Wählen Sie bei **Split** den Eintrag **Split by Barcode / QR Code**.
   * Wählen Sie bei **Barcode Type** einen oder mehrere unterstützte Barcode-Typen aus der Liste.
   * Definieren Sie bei **Barcode Pattern** das Muster, das eine Aufteilung auslösen soll. Sie können einen **regulären Ausdruck** (Regex) verwenden, um dynamische Barcode-Werte zu erfassen.

**So funktioniert es:**

* Sie wählen die Barcode-Typen aus, die eine Aufteilung auslösen sollen.
* Sie definieren ein Muster, dem der Barcode entsprechen muss – das kann eine feste Zeichenfolge oder ein Regex sein (z. B. `^INV\d{6}$`, um Barcodes wie `INV123456` zu erfassen).
* Bei der Dokumentenverarbeitung wird jedes Mal, wenn eine Seite einen passenden Barcode enthält, ein **neues Dokument erstellt**, das ab dieser Seite beginnt.

### Unterstützte Codetypen

Die vollständige Liste der unterstützten Barcode- und QR-Code-Formate finden Sie auf der [Übersichtsseite](./).
