# Beispiele

End-to-End-Beispiele, die zeigen, wie Sie die eDocs-MCP-Tools gemeinsam verwenden.

## Beispiel 1: Eine benutzerdefinierte Vorschau für XRechnung erstellen

Dieses Beispiel führt durch den gesamten Lebenszyklus einer benutzerdefinierten PREVIEW-Regel:
1. Prüfen, welche Regeln bereits existieren
2. Das XSLT in der Vorschau testen, ohne es zu aktivieren
3. Die benutzerdefinierte Regel erstellen
4. Sie auf eine neue Version aktualisieren
5. Zum Standard zurückkehren

### Schritt 1: Vorhandene Anpassungen prüfen

Rufen Sie `list_edoc_custom_attributes` auf:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

Die Antwort enthält zwei Listen. Ist `custom` für das Attribut `PREVIEW` leer, verwendet Ihre Organisation derzeit das integrierte Standard-Vorschau-Stylesheet.

### Schritt 2: Ihr XSLT testen, bevor Sie es erstellen

Rufen Sie `preview_edoc_custom_xslt` mit einer vorhandenen Attribut-ID (verwenden Sie eine Standard-ID aus der `list`-Antwort) und einer als Base64 kodierten XML-Beispieldatei auf:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Prüfen Sie die gerenderte Ausgabe, um sicherzustellen, dass Ihr XSLT das erwartete Ergebnis liefert, bevor Sie es übernehmen.

### Schritt 3: Die benutzerdefinierte Regel erstellen

Rufen Sie `create_edoc_custom_attribute` auf:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Speichern Sie die `attribute_id` aus der Antwort. Ab diesem Zeitpunkt verwendet jede von Ihrer Organisation verarbeitete XRechnung-2.1-CII-Rechnung Ihre benutzerdefinierte Vorschau.

### Schritt 4: Die Regel mit einer neuen Version aktualisieren

Wenn Sie das XSLT später verfeinern möchten, rufen Sie `update_edoc_custom_attribute` auf:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Mit `activate: true` wechseln Sie sofort zur neuen Version. Die vorherige Version bleibt im Verlauf erhalten. Setzen Sie `activate: false`, um sie als Entwurf zu speichern und separat zu aktivieren.

### Schritt 5: Zum integrierten Standard zurückkehren

Wenn Sie zur Standardvorschau zurückkehren möchten, rufen Sie `delete_edoc_custom_attribute` auf:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

Die benutzerdefinierte Regel wird entfernt, und das System greift automatisch wieder auf das gemeinsame Standard-Stylesheet zurück. Andere Kunden sind nicht betroffen.

---

## Beispiel 2: Extraktionspfade für EDI anpassen

Ihre Organisation erhält EDI-Rechnungen mit einem nicht standardmäßigen Feldlayout. Dieses Beispiel zeigt, wie Sie die Extraktionspfade für Ihre Organisation überschreiben.

### Schritt 1: Die aktuellen Regeln prüfen

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Wenn Sie in `default` einen Eintrag `EXTRACTION_PATHS` sehen, in `custom` jedoch nicht, übernimmt Ihre Organisation die gemeinsamen XPath-Regeln.

### Schritt 2: Ihre benutzerdefinierten Extraktionspfade erstellen

Rufen Sie `create_edoc_custom_attribute` mit Ihrem angepassten XPath-JSON auf:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Schritt 3: Mit einem Testlauf überprüfen

Rufen Sie `test_electronic_document` mit einer EDI-Beispieldatei auf, um zu bestätigen, dass die benutzerdefinierten Extraktionspfade die richtigen Werte erfassen:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

Die Antwort enthält `extracted_fields` und ein PNG unter `preview.image_base64`. Prüfen Sie beides auf Richtigkeit, bevor Sie live gehen.

---

## Beispiel 3: Eine vollständige eDoc-Verifizierung durchführen

Bevor Sie eine Änderung ausliefern, prüfen Sie, ob alle unterstützten eDoc-Fixtures weiterhin bestehen:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

Das Tool führt jede XRechnung-Fixture durch die Pipeline und meldet pro Fixture bestanden/fehlgeschlagen/Warnung. Ein fehlerfreier Lauf bestätigt, dass Ihre Anpassungen andere Dokumenttypen nicht beeinträchtigt haben.

Um nur einen einzelnen Typ schnell zu testen:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Dadurch werden bis zu 3 ZUGFeRD-Fixtures hochgeladen, die Verarbeitung abgewartet und Klassifizierung, Extraktion und Vorschauerzeugung durchgängig überprüft.
