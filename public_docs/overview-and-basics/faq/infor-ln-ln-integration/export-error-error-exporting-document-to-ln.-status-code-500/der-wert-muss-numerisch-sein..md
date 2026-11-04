# der Wert muss numerisch sein.

## **Schritt 1: Untersuchen des Kaufauftrags**

**1. Überprüfen Sie den Kaufauftrag vom Dashboard aus**

* Wenn der Dokumentenstatus **Exportfehler** ist:
  1. Suchen Sie das Dokument im Dashboard.
  2. Klicken Sie darauf und wählen Sie dann die Schaltfläche **Feldvalidierung**, um zur Feldvalidierung zurückzukehren.
* Wenn der Dokumentenstatus **Bereit zur Validierung** ist:
  1. Klicken Sie auf das Dokument, um direkt zum Bildschirm **Feldvalidierung** zu gelangen.
* Wenn das Dokument den Status **Ausstehende Genehmigung** hat:
  1. Navigieren Sie zum **Genehmigungsbildschirm**.
  2. Suchen Sie neben den **Rechnungszeilen** die **Kaufauftrags-Tabelle**.
  3. Gehen Sie zum Schritt 3. Überprüfen Sie die Liefernummer.

**2. Überprüfen des Kaufauftrags**

1. Stellen Sie auf dem Bildschirm **Feldvalidierung** sicher, dass der richtige Kaufauftrag ausgewählt ist.
2. Sobald der richtige Kaufauftrag bestätigt ist, klicken Sie auf den Kaufauftrag neben der extrahierten Tabelle, um die Ansicht der **Kaufauftrags-Tabelle** zu öffnen.

**3. Überprüfen der Liefernummer**

* In der Kaufauftrags-Tabelle suchen Sie die Spalte **Liefernummer**:
  * **Wenn eine Liefernummer vorhanden ist**, gehen Sie zum **Genehmigungsbildschirm** und überprüfen Sie erneut, ob sie vorhanden ist. Wenn sie vorhanden ist, gehen Sie zu **Schritt 3**.
  * **Wenn keine Liefernummer vorhanden ist**, folgen Sie **Schritt 2**, um dieses Problem zu beheben.

## Schritt 2: Überprüfen des Kaufauftrags in LN

Bevor Sie den Kaufauftrag an DocBits senden, überprüfen Sie, ob die **Liefernummer** in **LN** korrekt zugewiesen ist. Überprüfen Sie die **Kaufauftrags**-Details in **LN**, um sicherzustellen, dass sie vollständig und korrekt sind. Wenn die **Liefernummer** fehlt oder inkorrekt ist, könnte dies die Ursache für den Exportfehler sein.

Wenn der **Kaufauftrag** korrekt aussieht und die notwendigen Details enthält, können Sie mit dem nächsten Schritt fortfahren.

## **Schritt 3: Öffnen der DocBits-Einstellungen**

1. Öffnen Sie **DocBits** und gehen Sie zum Abschnitt **Einstellungen**.
2. Navigieren Sie zu **Dokumentenverarbeitung**.
3. Wählen Sie **Export**.
4. Klicken Sie im **Export**-Abschnitt auf das **Drei-Punkte**-Symbol neben dem Export, der nicht funktioniert, und wählen Sie **Bearbeiten**.
5. Im Menü **Exporteinstellungen bearbeiten** klicken Sie auf **LN-Mapping-Datei herunterladen**.

## **Schritt 3: LN-Mapping-Datei bearbeiten**

1. Öffnen Sie die heruntergeladene **LN-Mapping**-Datei.
2. Suchen Sie nach dem Feld **IRF\_ReceiptLine**.
   * Wenn das Feld **IRF\_ReceiptLine** vorhanden ist und auf **nichts** (leer) gesetzt ist, aktualisieren Sie es auf **TF\_delivery\_line**.
   * Wenn das Feld **IRF\_ReceiptLine** **nicht vorhanden** ist, fügen Sie es zur Datei hinzu und setzen Sie seinen Wert auf **TF\_delivery\_line**.
3. Fügen Sie für das Feld **InvoiceReceiptFields** **ReceiptLine** zu den Werten hinzu.

Es sollte wie folgt aussehen:

<figure><img src="../../../../.gitbook/assets/ReceiptLine.png" alt="" width="563"><figcaption></figcaption></figure>

## **Schritt 4: Die aktualisierte Datei zurück zu DocBits hinzufügen**

1. Gehen Sie zurück zum **Export**-Abschnitt in DocBits, wo Sie die **LN-Mapping**-Datei zuvor heruntergeladen haben.
2. Laden Sie die bearbeitete **LN-Mapping**-Datei mit den neuen Updates hoch.

## Schritt 5: Export erneut versuchen

Nach Bestätigung, dass der **Kaufauftrag** eine **Liefernummer** hat und das **Exportfile korrekt** ist, befolgen Sie diese Schritte, um den Export erneut zu versuchen:

1. **Zurück zum Dashboard:**
   * Gehen Sie zurück zum Dashboard und suchen Sie das Dokument mit dem Exportfehler.
2. **Exportvorgang erneut versuchen:**
   * Klicken Sie auf das Dokument mit dem Exportfehler.
   * Wenn der **Kaufauftrag** eine gültige **Liefernummer** hat und das **Exportfile** korrekt ist, fahren Sie mit dem erneuten Versuch des Exports fort.
3. **Exportergebnis überprüfen:**
   * Nach dem erneuten Versuch überprüfen Sie den Exportvorgang erneut, um zu sehen, ob das Problem behoben wurde und das Dokument nicht mehr als Exportfehler angezeigt wird.
   * Wenn der Export erfolgreich ist, sollte das Problem behoben sein.
4. **Weitere Untersuchung (falls das Problem weiterhin besteht):**
   * Wenn das Problem nach dem erneuten Versuch des Exports weiterhin besteht, wenden Sie sich an den Support für weitere Untersuchungen möglicher Konfigurations- oder Systemprobleme.
