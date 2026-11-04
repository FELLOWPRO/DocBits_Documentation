# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits-Anleitung für E-Rechnungen: XRechnung und ZUGFeRD (Factur-X) verarbeiten, Daten validieren und Workflows automatisieren
{% endembed %}

## Überblick

Im Verwaltungsbereich für XRechnung stehen die folgenden Hauptbestandteile zur Verfügung:

## 1. Transformation

### Zweck

Die Transformation überführt Rohdaten, meist im XML-Format, in eine strukturierte Ausgabe für einen bestimmten Zweck, beispielsweise eine Rechnung. Bei XRechnung wird dafür vor allem XSLT (Extensible Stylesheet Language Transformations) verwendet. Mit dieser Sprache lassen sich XML-Dokumente in andere Formate wie XML, HTML oder einfachen Text umwandeln.

### Funktionsweise

• XSLT-Vorlage: Die XSLT-Datei legt fest, wie XML-Daten verarbeitet werden und wie die Ausgabe aussehen soll. Regeln und Vorlagen extrahieren, bearbeiten und exportieren Daten aus dem XML-Dokument.

• Elemente und Attribute: Bestimmte Elemente und Attribute in der XSLT-Datei steuern die Transformation. Beispielsweise extrahiert \<xsl:value-of> den Wert eines bestimmten Knotens aus dem XML-Dokument.

### Möglichkeiten für Administratoren

• XSLT anpassen:

• Bestehende Vorlagen bearbeiten: Administratoren können XSLT-Vorlagen ändern, um die Transformation der XML-Eingangsdaten anzupassen. Um zusätzliche Informationen zu extrahieren, lassen sich beispielsweise neue Regeln ergänzen.

• Neue Versionen erstellen: Bei Änderungen können Administratoren eine neue Version der XSLT-Vorlage anlegen. Frühere Versionen bleiben damit als Referenz oder zur Wiederherstellung erhalten.

### Beispiel:

Angenommen, die XSLT-Vorlage extrahiert die Rechnungsnummer mit folgendem Ausdruck:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Soll ein weiteres Feld wie die Kundenreferenznummer extrahiert werden, kann ein Administrator Folgendes ergänzen:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Vorschau

### Zweck

Mit der Vorschau können Administratoren das Ergebnis einer XSLT-Transformation vor dem Abschluss prüfen. So lässt sich kontrollieren, ob die Regeln korrekt funktionieren und die Ausgabe den Anforderungen entspricht.

### Funktionsweise

• Darstellung in Echtzeit: Die Vorschau zeigt, wie die transformierten Daten in einem Dokument, beispielsweise einer Rechnung, aussehen. Dadurch lassen sich Fehler und Formatierungsprobleme früh erkennen.

• Anpassungen: Zeigt die Vorschau Abweichungen oder Fehler, können diese direkt in der Transformationsdatei (XSLT) korrigiert werden.

### Möglichkeiten für Administratoren

• Vorschau anpassen:

• Vorschauumfang ändern: Administratoren können festlegen, welche Teile der Transformation angezeigt werden, beispielsweise bestimmte Dokumentabschnitte oder neu ergänzte Regeln.

• Speichern und erneut prüfen: Nach einer Anpassung aktualisieren Sie die Vorschau und kontrollieren das Ergebnis. Wiederholen Sie diesen Ablauf, bis die gewünschte Ausgabe erreicht ist.

### Beispiel:

Wenn das Datum in der Vorschau beispielsweise als YYYY-MM-DD statt als DD-MM-YYYY erscheint, kann ein Administrator die XSLT-Formatierung ändern und das Ergebnis sofort in der Vorschau prüfen.

## 3. Extraktionspfade

### Zweck

Extraktionspfade bestimmen, an welchen Stellen einer XML- oder JSON-Struktur Daten entnommen werden. Sie grenzen die Informationen ein, die für die Transformation oder weitere Verarbeitungsschritte benötigt werden.

### Funktionsweise

• XPath und JSONPath: Extraktionspfade verwenden XPath für XML oder JSONPath für JSON, um die Position der Daten im Dokument zu beschreiben. Sie geben dem System vor, wo es die erforderlichen Informationen findet und wie es sie extrahiert.

### Möglichkeiten für Administratoren

• Pfade definieren und ändern:

• Bestehende Pfade ändern: Administratoren können Extraktionspfade anpassen, wenn sich die Datenstruktur ändert oder zusätzliche Daten benötigt werden. Dazu ändern sie die jeweiligen XPath- oder JSONPath-Ausdrücke.

• Neue Pfade ergänzen: Für zusätzliche Felder oder Datenpunkte können Administratoren neue Extraktionspfade mit den passenden Positionen im XML- oder JSON-Dokument definieren.

### Beispiel:

Wenn in einer XML-Rechnung der Pfad zur Rechnungsnummer wie folgt definiert ist:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

und ein neues Feld wie die Lieferadresse benötigt wird, kann ein Administrator Folgendes ergänzen:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Verwendete Regeln und Aktivierung

Organisationsspezifische Regeln haben Vorrang vor den Standardregeln für das erkannte eDoc-Format. Prüfen Sie die aktive TRANSFORMATION und prüfen Sie, welcher Knoten im transformierten XML invoice_type liefert; der Pfad hängt vom Format ab. Speichern sichert einen Entwurf; aktivieren Sie ihn nach dem Testen über das Häkchen. Eine gerenderte Preview belegt nicht den gespeicherten Dokumenttyp. Die [Anleitung zur Fehlerbehebung bei der Klassifizierung](../credit-note-recognized-as-invoice.md) erläutert die Codes 381/261, spätere Skripte und Vorsichtsmaßnahmen bei der erneuten Verarbeitung.
