# Tabellenauszug Fehlerbehebung

## **Schritt 1: OCR-Ansicht für schlechte Extraktionsergebnisse öffnen**

Wenn die Ergebnisse des Tabellenauszugs-Trainings nicht gut sind:

1. Öffnen Sie die **OCR-Ansicht**, indem Sie auf das Lupensymbol mit **OCR** klicken.
2. Überprüfen Sie die Extraktionsergebnisse und sehen Sie, ob der OCR-Prozess die Datenerfassung verbessern kann.
3. Wenn die Ergebnisse immer noch schlecht aussehen, versuchen Sie ein anderes Dokument, um zu überprüfen, ob das Problem dokumentenspezifisch ist.
4. Wenn das Problem dokumentenspezifisch ist, verwenden Sie ein anderes Dokument für die Extraktion.
   * Wenn das Problem weiterhin besteht, befolgen Sie die nächsten Schritte.

## **Schritt 2: Überprüfen Sie die Verfügbarkeit von E-Text**

1. Überprüfen Sie, ob das Dokument über **E-Text** verfügt.
   * Sie können dies mit einem Tool wie **Adobe Acrobat** überprüfen.
   * Wenn das Dokument E-Text enthält, folgen Sie **Schritt 3.**
   * Wenn das Dokument keinen E-Text enthält, folgen Sie **Schritt 4.**

## **Schritt 3: E-Text-Extraktion aktivieren**

Wenn das Dokument E-Text enthält, haben Sie zwei Optionen:

1. **Aktivieren Sie die E-Text-Extraktion nur für diesen Lieferanten**:
   * Gehen Sie zurück zur **Dokumentenfeldvalidierung**.
   * Klicken Sie auf das Quadrat mit den drei Punkten in der linken Symbolleiste.
   * Aktivieren Sie hier die Option **E-Text verwenden, wenn verfügbar**, um sie nur für diesen Lieferanten zu aktivieren.
2. **Aktivieren Sie die E-Text-Extraktion für alle Lieferanten**:
   * Gehen Sie zu **Einstellungen** > **Dokumentenverarbeitung** > **OCR-Einstellungen**.
   * In diesem Abschnitt finden Sie die Option **E-Text verwenden, wenn verfügbar** und können sie für alle Lieferanten aktivieren.
3. Nach Aktivierung der E-Text-Extraktion versuchen Sie das **Tabellenauszugs-Training** erneut.
   * Wenn sich die Ergebnisse verbessern, ist das Problem behoben.
   * Wenn die Ergebnisse immer noch nicht gut sind, fahren Sie mit **Schritt 4** fort.

## **Schritt 4: Kein E-Text verfügbar - Ändern Sie die AI OCR-Version**

Wenn das Dokument keinen E-Text enthält:

1. Gehen Sie zu **Einstellungen** > **Dokumentenverarbeitung** > **OCR-Einstellungen**.
2. Ändern Sie die **AI OCR-Version** in eine andere Version.
3. Gehen Sie zurück zum **Tabellenauszugs-Training** und versuchen Sie es erneut.
4. Wenn das Ergebnis besser ist:
   * Überprüfen Sie andere Dokumente von verschiedenen Lieferanten, um sicherzustellen, dass die Extraktionsergebnisse für diese Lieferanten nicht von dieser Änderung beeinflusst werden.
   * **Seien Sie vorsichtig, da diese Änderung die Extraktionsergebnisse anderer Lieferanten beeinflussen kann.**
   * Diese Änderung kann sich auf andere Lieferanten auswirken, daher überprüfen Sie die Ergebnisse sorgfältig, um sicherzustellen, dass sie die Dokumentextraktionen anderer Lieferanten nicht negativ beeinflusst.
5. Wenn sich das Ergebnis nach Änderung der AI OCR-Version nicht verbessert hat, wenden Sie sich bitte an uns für weitere Unterstützung.

## Meldungen an der Tabelle

Die Extraktion kann richtig aussehen, und das Dokument lässt sich trotzdem nicht freigeben. Dies sind die Meldungen, die DocBits an oder unter der Positionstabelle anzeigt, was sie auslöst und wie Sie sie beheben.

| Meldung | Ursache | Lösung |
|---|---|---|
| **Erforderliche Spalte leer** (Zelle rot markiert, Spaltenname im Tooltip) | Eine Spalte, die in den Tabellenspalten-Einstellungen mit *Erforderlich* markiert ist, hat in dieser Zeile keinen Wert. | Füllen Sie die Zelle. Existiert der Wert für diesen Dokumenttyp nie, entfernt ein Administrator *Erforderlich* unter Einstellungen → Dokumenttypen → Tabellenspalten, und Sie starten das Dokument neu. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits prüft jede Zeile: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, minus `DISCOUNT`, oder × (100 − `DISCOUNT_PERCENT`) / 100, oder minus `DISCOUNT_PER_UNIT × QUANTITY`, je nachdem, welche Rabattspalte gefüllt ist. Eine Abweichung über 0,02 löst die Meldung aus. Die Prüfung läuft nur, wenn Menge, Einzelpreis und Summe alle gefüllt sind. | Vergleichen Sie die vier Werte mit dem Dokument. Meist wurde einer davon in die falsche Spalte gelesen; ein Zuschlags- oder Rabattwert in der falschen Zelle ist der häufigste Fall. Korrigieren Sie die Zelle; die Meldung verschwindet beim Speichern. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Dieselbe Prüfung, mit der Rabattspalte, die gefüllt ist. | Wie oben; prüfen Sie zuerst die Rabattzelle. |
| **Line items add up to … but the net total is …** (Warnung) | Die Summe aller `TOTAL_AMOUNT`-Zellen weicht vom Nettobetrag im Kopf ab. | Suchen Sie nach einer fehlenden Zeile, einer doppelten Zeile oder einem falsch gelesenen Nettobetrag im Kopf. Eine Warnung blockiert die Freigabe nicht. |
| **Total does not add up: expected …, got …** (Kopf) | Netto + Steuer (+ Versand in US-Layouts) weicht vom Gesamtbetrag im Kopf ab. | Kopfprüfung, kein Tabellenproblem: Korrigieren Sie die Kopfbeträge. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** (In der Positionstabelle fehlt eine obligatorische Spalte für die Bestellung) | Der Bestellabgleich benötigt diese vier Standardspalten, und eine davon ist versteckt oder durch eine eigene Spalte ersetzt. | Administrator: Verstecken der Standardspalte unter Tabellenspalten aufheben, oder den Wert im Tabellentraining dieser Spalte zuordnen. |
| **Table is already extracted by AI. Do you want to train manually?** (Die Tabelle wurde bereits von der KI extrahiert. Möchten Sie manuell trainieren?) | Sie haben das Tabellentraining für einen Lieferanten geöffnet, dessen Tabelle von der KI stammt. | Bestätigen Sie, um zu trainieren; die gespeicherten Regeln ersetzen dann die KI-Tabelle für diesen Lieferanten. Abbrechen, um die KI-Tabelle zu behalten. |
| **AI Table will display here. Enable in …** (Hier wird die KI-Tabelle angezeigt. Aktivieren in …) | Die KI-Tabellenextraktion ist für die Organisation ausgeschaltet. | Administrator: Einstellungen → Dokumentenverarbeitung → Klassifizierung und Extraktion → *AI-Tabellen-Extraktion*. |
| **No line items yet** (Noch keine Einzelposten) | Nichts wurde extrahiert: keine Regeln für diesen Lieferanten und die KI hat keine Tabelle gefunden, oder das Dokument hat keinen lesbaren Text. | Folgen Sie den Schritten 1 bis 4 oben (OCR-Ansicht, E-Text). Trainieren Sie dann die Tabelle einmal, oder fügen Sie Zeilen manuell mit *Neue Tabellenzeile hinzufügen* hinzu. |

### Die KI füllt eine Spalte immer wieder mit dem falschen Wert

Ein Beispiel aus der Praxis: Die KI schreibt die Positionssumme in `CHARGES`. Jede Zeile fällt dann bei der Positionssummenprüfung durch, weil Zuschläge zu Menge × Einzelpreis addiert werden.

1. Hat der Lieferant gespeicherte Regeln, entfernen Sie *KI nutzen* bei dieser Spalte (Einstellungen → Dokumenttypen → Tabellenspalten), damit die Regeln sie füllen.
2. Hat der Lieferant keine Regeln, trainieren Sie die Tabelle einmal, damit die Spalte an ihre Position auf der Seite gebunden ist, oder verstecken Sie die Spalte, wenn der Lieferant diesen Wert nie druckt.
3. Fügen Sie ein [KI-Tabellen-Tag](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) hinzu wie *„die Zuschlagsspalte ist bei diesem Lieferanten leer“*; Tags werden pro Lieferant gespeichert.

### Die Tabellenprüfungen abschalten

Einstellungen → Dokumenttypen → *Ihr Typ* → Weitere Einstellungen → **Tabellenvalidierung überspringen** markiert die Tabelle jedes Dokuments dieses Typs als gültig: Positionssummenabweichungen und leere erforderliche Spalten werden nicht mehr gemeldet. Die Kopfprüfungen (Gesamt = Netto + Steuer) bleiben. Verwenden Sie die Option nur für Dokumenttypen, deren Tabellen informativ sind und nicht an das ERP exportiert werden.
