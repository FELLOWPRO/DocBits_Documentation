# LN-Exportfehler: „ReceiptLine muss numerisch sein“

Die englische Fehlermeldung lautet: **Request validation; Attr. 'ReceiptLine', Value " " : the value must be numeric.** Prüfen Sie die Wareneingangsdaten und die Zuordnung von `ReceiptLine` in der LN-Exportkonfiguration.

## Schritt 1: Bestellung in DocBits prüfen

### Dokument öffnen

* **Status Export Error:** Öffnen Sie das Dokument im Dashboard und wechseln Sie über **Fields Validation** zurück zur Feldvalidierung.
* **Status Ready for Validation:** Öffnen Sie das Dokument direkt in der Feldvalidierung (**Field Validation**).
* **Status Pending Approval:** Öffnen Sie die Genehmigungsansicht (**Approval Screen**). Suchen Sie neben den Rechnungspositionen (**Invoice Line Items**) die Bestelltabelle (**Purchase Order Table**) und prüfen Sie dort die Liefernummer.

### Richtige Bestellung und Liefernummer prüfen

1. Prüfen Sie in der Feldvalidierung, ob die richtige Bestellung ausgewählt ist.
2. Öffnen Sie die Bestellung neben der extrahierten Tabelle, um die Bestelltabelle anzuzeigen.
3. Suchen Sie die Spalte **Delivery Number**.
4. Wenn eine Liefernummer vorhanden ist, prüfen Sie sie auch in der Genehmigungsansicht. Ist sie dort ebenfalls vorhanden, fahren Sie mit Schritt 3 fort.
5. Fehlt die Liefernummer, prüfen Sie zunächst die Bestelldaten in LN gemäß Schritt 2.

## Schritt 2: Bestellung in LN prüfen

Prüfen Sie vor der Übertragung nach DocBits, ob die **Delivery Number** in LN korrekt zugeordnet ist. Kontrollieren Sie die Bestelldetails auf Vollständigkeit und Richtigkeit. Eine fehlende oder falsche Liefernummer kann den Exportfehler verursachen.

Wenn die Bestellung korrekt ist und die erforderlichen Angaben enthält, fahren Sie mit dem nächsten Schritt fort.

## Schritt 3: LN-Zuordnungsdatei herunterladen

1. Öffnen Sie **Settings → Document Processing → Export** in DocBits.
2. Öffnen Sie das Drei-Punkte-Menü des betroffenen Exports und wählen Sie **Edit**.
3. Laden Sie im Dialog **Edit Export Settings** die Datei über **Download the LN-Mapping** herunter.

## Schritt 4: ReceiptLine-Zuordnung prüfen und bearbeiten

1. Öffnen Sie die heruntergeladene LN-Zuordnungsdatei.
2. Suchen Sie `IRF_ReceiptLine`.
   * Ist der Eintrag leer, setzen Sie ihn auf `TF_delivery_line`.
   * Fehlt der Eintrag, ergänzen Sie ihn mit dem Wert `TF_delivery_line`.
3. Stellen Sie sicher, dass `InvoiceReceiptFields` den Eintrag `ReceiptLine` enthält.

Die entscheidende Zuordnung ist `IRF_ReceiptLine = TF_delivery_line`. Die zuvor in dieser Seite beschriebene Zuordnung von `PackingSlip` betrifft ein anderes Feld und behebt diesen numerischen `ReceiptLine`-Fehler nicht.

## Schritt 5: Aktualisierte Datei hochladen

Öffnen Sie erneut den betroffenen Export in DocBits und laden Sie die bearbeitete LN-Zuordnungsdatei hoch.

## Schritt 6: Export erneut versuchen und Ergebnis prüfen

1. Kehren Sie zum Dashboard zurück und öffnen Sie das Dokument mit dem Exportfehler.
2. Prüfen Sie vor dem erneuten Export, ob die Bestellung eine gültige Liefernummer hat und die Exportzuordnung korrekt ist.
3. Starten Sie den Export erneut.
4. Prüfen Sie das Exportergebnis und den Dokumentstatus. Wenn der Export weiterhin fehlschlägt, wenden Sie sich mit den Fehlerdetails an den Support, um mögliche Konfigurations- oder Systemprobleme weiter untersuchen zu lassen.
