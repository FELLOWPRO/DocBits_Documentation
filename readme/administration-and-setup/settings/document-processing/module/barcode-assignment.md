# Barcode-Zuordnung

### Überblick

Die Einstellung **Barcode-Zuordnung** (Barcode Assignment) fügt dem **Validierungs-Bildschirm** ein Barcode-Werkzeug hinzu. Es liest die in einem Dokument gefundenen Barcodes und QR-Codes aus und ermöglicht Ihnen, **deren Werte den Feldern des Dokuments zuzuordnen** — zum Beispiel eine Referenz-, Bestell- oder Lieferscheinnummer aus einem Barcode zu übernehmen, statt sie abzutippen.

Diese Einstellung ist **standardmäßig deaktiviert**.

### Was bewirkt die Einstellung?

Wenn diese Einstellung aktiviert ist, erscheint beim Validieren eines Dokuments ein kleiner **Barcode-Button** (ein QR-Code-Symbol) in der Werkzeugleiste. Ein Klick darauf zeigt die Barcodes, die DocBits im Dokument gefunden hat, und Sie können jeden davon einem Feld zuordnen. Das Feld wird dann mit dem aus dem Barcode ausgelesenen Wert befüllt.

* **Aktiviert** — Der Barcode-Button wird im Validierungs-Bildschirm angezeigt. Sie können die Barcodes im Dokument auslesen und ihre Werte den Feldern zuordnen.
* **Deaktiviert** — Der Button ist ausgeblendet, und Barcode-Werte werden bei der Validierung nicht zur Zuordnung angeboten.

{% hint style="info" %}
**Hier geht es darum, einen Barcode-/QR-Wert auszulesen und ihn bei der Validierung einem Feld zuzuordnen.** Das automatische Extrahieren strukturierter Daten aus Zahlungscodes (z. B. Swiss QR Bill oder GiroCode) — sowie das Aufteilen einer mehrseitigen Datei an Barcode-Trennseiten — übernimmt eine **andere** Einstellung: [Bar-Code / QR-Code-Extraktion](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Vorteile

* **Schnellere, fehlerfreie Erfassung**: Übernehmen Sie Werte direkt aus einem Barcode, statt sie abzulesen und abzutippen.
* **Weniger Tippfehler**: Ein gescannter Wert entspricht genau dem, was im Barcode kodiert ist.
* **Volle Kontrolle**: Sie entscheiden bei der Validierung, welcher Barcode in welches Feld kommt.

### Verwendung

1. Gehen Sie zu **Einstellungen**.
2. Wählen Sie **Dokumentverarbeitung**.
3. Wählen Sie **Modul**.
4. Öffnen Sie den Abschnitt **Dokumenttyp**.
5. Finden Sie **Barcode-Zuordnung** und schalten Sie den Schalter ein.
6. Klicken Sie anschließend beim Validieren eines Dokuments auf den **Barcode-Button** in der Werkzeugleiste und ordnen Sie die erkannten Barcode-Werte den passenden Feldern zu.

### Wann diese Funktion nutzen

* **Dokumente mit Barcodes**: Wenn Ihre Dokumente Barcodes/QR-Codes enthalten, deren Werte in bestimmte Felder gehören (z. B. Bestell- oder Referenznummern).
* **Manuelle Validierungs-Workflows**: Wenn eine Person Dokumente prüft und Felder schnell aus Barcodes befüllen möchte.
* **Ausgeschaltet lassen**, wenn Ihre Dokumente keine nutzbaren Barcodes haben oder Sie nur die automatische Barcode-/QR-**Extraktion** benötigen — siehe [Bar-Code / QR-Code-Extraktion](bar-code-qr-code-extraction/README.md).
