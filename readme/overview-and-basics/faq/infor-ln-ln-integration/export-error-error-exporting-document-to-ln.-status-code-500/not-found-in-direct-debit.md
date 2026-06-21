# Nicht gefunden in Lastschrift

## **Schritt 1: LN-Konfiguration prüfen**

1. Melden Sie sich bei **LN CE** an.
2. Navigieren Sie zum Menü **Options** und wählen Sie **Run Program**.
3. Geben Sie im Eingabefeld **ACP Parameters** ein und drücken Sie die Eingabetaste, um das Programm zu öffnen.
4. Klicken Sie auf den Pfeil neben dem Feld **Actual Set**, um die Einstellungen aufzuklappen.
5. Wechseln Sie zum Abschnitt **Matching**.
   * **Prüfen Sie die Einstellung „Automatic Matching“:**
     * Wenn das **Automatic Matching** auf **Match to Purchase Receipt** eingestellt ist, fahren Sie mit dem nächsten Schritt fort.
     * Wenn es **nicht** auf **Match to Purchase Receipt** eingestellt ist, Sie diesen Fehler aber dennoch erhalten haben, wenden Sie sich bitte an uns.

## **Schritt 2: DocBits-Einstellungen öffnen**

Wenn das **Automatic Matching** auf **Match to Purchase Receipt** eingestellt ist, fahren Sie mit den folgenden Schritten in DocBits fort:

1. Öffnen Sie **DocBits** und gehen Sie zum Bereich **Einstellungen**.
2. Navigieren Sie zu **Dokumentverarbeitung**.
3. Wählen Sie **Export**.
4. Klicken Sie im Bereich **Export** auf das Symbol mit den **drei Punkten** neben dem nicht funktionierenden Export und wählen Sie **Bearbeiten**.
5. Klicken Sie im Menü **Exporteinstellungen bearbeiten** auf **LN-Mapping-Datei herunterladen**.

## **Schritt 3: LN-Mapping-Datei bearbeiten**

1. Öffnen Sie die heruntergeladene **LN-Mapping**-Datei.
2.  Suchen Sie nach dem Feld **IRF\_PackingSlip**.

    * Wenn das Feld **IRF\_PackingSlip** vorhanden und auf **nichts** (leer) gesetzt ist, aktualisieren Sie es auf **TF\_packing\_slip**.
    * Wenn das Feld **IRF\_PackingSlip** **nicht vorhanden** ist, fügen Sie es der Datei hinzu und setzen Sie seinen Wert auf **TF\_packing\_slip**.&#x20;


3. Fügen Sie für das Feld **InvoiceReceiptFields** den Wert **PackingSlip** zu den Werten hinzu.

Es sollte wie folgt aussehen:

<figure><img src="../../../../.gitbook/assets/image (328).png" alt=""><figcaption></figcaption></figure>



## **Schritt 4: Die aktualisierte Datei wieder in DocBits hinzufügen**

1. Gehen Sie zurück zum Bereich **Export** in DocBits, wo Sie zuvor die **LN-Mapping**-Datei heruntergeladen haben.
2. Laden Sie die bearbeitete **LN-Mapping**-Datei mit den neuen Aktualisierungen hoch.

## Falls weiterhin der Fehler **Error exporting document to LN** mit dem Statuscode **500** auftritt, wenden Sie sich bitte an uns
