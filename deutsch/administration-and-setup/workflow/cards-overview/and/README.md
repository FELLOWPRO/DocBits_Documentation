# And

Verwenden Sie eine **And**-Karte, um zu entscheiden, ob ein Workflow nach seinem **When**-Auslöser fortgesetzt werden soll. Fügen Sie die benötigten Prüfungen vor der **Then**-Aktion hinzu. Jede Karte zeigt Felder zum Ausfüllen, etwa **Operator**, **Field Name** oder **Value**; die Screenshots zeigen die verfügbaren Kartenvorlagen, keine fertig ausgefüllten Regeln.

Wählen Sie im **Workflow Builder** unter **And...** die Option **Add Card**. Wählen Sie links eine Kategorie aus oder geben Sie in **Search Card** den Namen einer Karte ein. Wählen Sie eine Kartenvorschau aus, um sie dem Workflow hinzuzufügen. Sie können in der Vorschauliste scrollen, um weitere Karten zu sehen. Mit **×** schließen Sie die Auswahl, ohne eine weitere Karte zu wählen. Speichern Sie den Workflow, nachdem Sie die Karten konfiguriert haben. Die umgebenden Schritte **When**, **And** und **Then** finden Sie unter [Workflow](../../).

## Compare with Purchase Order

Mit diesen Karten vergleichen Sie Bestell- oder Rechnungsdaten mit einer Bestellung, etwa Stückpreis, zugesagtes Lieferdatum, Gebühren oder Menge. Wählen Sie die Felder, den Operator und gegebenenfalls die Toleranz, nach der die gewählte Karte fragt. Die einzelnen Karten finden Sie unter [Compare with Purchase Order](compare-with-purchase-order/).

<figure><img src="../../../../.gitbook/assets/and-category-po-comparison-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Compare with Purchase Order; sichtbare Vorschauen umfassen Vergleiche von Stückpreis, Lieferdatum, Gebühren und Menge."><figcaption><p>Kategorie Compare with Purchase Order in der englischen Sandbox.</p></figcaption></figure>

## Document Field

Wählen Sie diese Kategorie, um ein Kontrollkästchen oder einen Feldstatus zu prüfen, ein Feld mit einem Wert zu vergleichen oder zwei Felder miteinander zu vergleichen. Füllen Sie auf der gewählten Karte die Platzhalter **Field Name** und **Operator** aus. Einige Vergleiche fragen zusätzlich nach einer Toleranz. Siehe [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/and-category-document-field-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Document Field; sichtbare Vorschauen prüfen ein Kontrollkästchen, einen Feldstatus, Feldwerte und Vergleiche zweier Felder."><figcaption><p>Document-Field-Prüfungen verwenden Werte aus dem aktuellen Dokument.</p></figcaption></figure>

## Date & Time

Verwenden Sie **Date & Time**, um ein Datum oder eine Uhrzeit mit einem Bereich zu vergleichen oder **Today** mit einem gewählten Datum zu vergleichen. Wählen Sie in der Karte den **Operator** und die Datumswerte aus. Siehe [Date & Time](date-and-time/).

<figure><img src="../../../../.gitbook/assets/and-category-date-time-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Date &#x26; Time; zwei Vorschauen vergleichen ein Datum oder eine Uhrzeit mit einem Bereich und vergleichen Today mit einem Date."><figcaption><p>Date &#x26; Time bietet eine Bereichsprüfung und eine Prüfung gegen das heutige Datum.</p></figcaption></figure>

## Document

Verwenden Sie diese Karten, wenn ein Workflow vom **Dokumenttyp** oder von der **Unterorganisation** abhängen soll. Wählen Sie den Typ oder die Organisation, die in der Karte genannt wird. Siehe [Document](document/).

<figure><img src="../../../../.gitbook/assets/and-category-document-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Document; Vorschauen prüfen den Dokumenttyp und die Zugehörigkeit zu einer Unterorganisation."><figcaption><p>Document-Bedingungen prüfen Typ oder Unterorganisation.</p></figcaption></figure>

## Logic

Diese Kategorie enthält Prüfungen mit einer Entscheidungstabelle, einer HTTPS-Antwort, der Verfügbarkeit eines Moduls, einem angebotenen Artikelpreis, einem Zufallswert oder zwei Werten. Öffnen Sie die jeweilige Karte und füllen Sie die benannten Platzhalter aus; die HTTPS-Karte fragt zum Beispiel nach einer URL, einer Methode und einem akzeptierten Statuscode. Siehe [Logic](logic/).

<figure><img src="../../../../.gitbook/assets/and-category-logic-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Logic; Vorschauen umfassen Karten für Entscheidungstabelle, HTTPS-Anfrage, Modul aktiv, angebotenen Preis, Zufallswert und Wertevergleich."><figcaption><p>Logic bietet mehrere unterschiedliche Bedingungstypen; wählen Sie den, der zu Ihrer Regel passt.</p></figcaption></figure>

## Status

Verwenden Sie **Status**, um zu prüfen, ob ein Dokument einen gewählten Status hat oder ob sein Status in einer ausgewählten Menge enthalten ist. Wählen Sie in der Karte den **Operator** und den **Status**. Siehe [Status](status/).

<figure><img src="../../../../.gitbook/assets/and-category-status-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Status; zwei Vorschauen vergleichen den Document status mit einem Status oder einer Menge von Status."><figcaption><p>Status-Bedingungen prüfen den aktuellen Dokumentzustand.</p></figcaption></figure>

## Table

Diese Karten untersuchen die Zeilen von Dokumenttabellen. Die sichtbaren Optionen umfassen Datumsprüfungen, Textmuster, Haltbarkeit und Vergleiche zwischen Spalten. Wählen Sie den **Table name** und den **Column Name**, bevor Sie einen Operator oder ein Muster auswählen. Siehe [Table](table/).

<figure><img src="../../../../.gitbook/assets/and-category-table-en.png" alt="Englische And-Kartenauswahl mit ausgewählter Table; sichtbare Vorschauen umfassen Datum, Regex-Muster, Haltbarkeit und Vergleiche von Tabellenspalten."><figcaption><p>Table-Bedingungen verwenden Zeilen und Spalten aus einer Dokumenttabelle.</p></figcaption></figure>

## Compare with Quote Price

Mit diesen Karten vergleichen Sie einen Artikel mit angebotenen Preisdaten. Die sichtbaren Auswahlmöglichkeiten umfassen Artikel-ID, Lieferantentyp, Lieferanten-Artikel-ID, Stückpreis und Mengeneinheit. Der **Operator** und die Datenplatzhalter hängen von der gewählten Karte ab.

<figure><img src="../../../../.gitbook/assets/and-category-quote-price-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Compare with Quote Price; fünf Vorschauen decken Artikel-ID, Lieferantentyp, Lieferanten-Artikel-ID, Stückpreis und Mengeneinheit ab."><figcaption><p>Compare with Quote Price ist in der aktuellen Kartenauswahl eine eigene Kategorie.</p></figcaption></figure>

## Assignee

Verwenden Sie **Assignee**, wenn die Bedingung vom zugewiesenen Benutzer oder der zugewiesenen Gruppe abhängt. Wählen Sie, ob mit einem einzelnen Benutzer oder einer einzelnen Gruppe oder mit einer ausgewählten Menge verglichen werden soll. Siehe [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/and-category-assignee-en.png" alt="Englische And-Kartenauswahl mit ausgewähltem Assignee; Vorschauen vergleichen den zugewiesenen Benutzer oder die zugewiesene Gruppe mit einer oder mehreren Auswahlmöglichkeiten."><figcaption><p>Assignee-Bedingungen prüfen den Benutzer oder die Gruppe, dem bzw. der das Dokument zugewiesen ist.</p></figcaption></figure>
