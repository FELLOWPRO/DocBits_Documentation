# Barcode-Zuordnung

### Überblick

Die Einstellung **Barcode-Zuordnung** (Barcode Assignment) fügt dem **Validierungs-Bildschirm** ein Barcode-Werkzeug hinzu. Es liest die in einem Dokument gefundenen Barcodes und QR-Codes aus und ermöglicht Ihnen, **deren Werte den Feldern des Dokuments zuzuordnen** — zum Beispiel eine Bestell-, Referenz- oder Lieferscheinnummer aus einem Barcode zu übernehmen, statt sie abzutippen.

Diese Einstellung ist **standardmäßig deaktiviert**.

### Was Sie nach dem Aktivieren erhalten

Sobald die Einstellung aktiviert ist, erscheint ein neuer **Barcode-Button** (ein QR-Code-Symbol) in der Werkzeugleiste am rechten Rand des **Validierungs-Bildschirms** (`/field_validation_v1/…`). Dieser Button ist der Einstieg in die gesamte Funktion — ohne die Einstellung ist das Symbol ausgeblendet.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="Das Barcode-Symbol (QR-Code) in der Validierungs-Werkzeugleiste"><figcaption><p>Bei aktivierter Einstellung erscheint das Barcode-Symbol in der Validierungs-Werkzeugleiste.</p></figcaption></figure>

Hier sehen Sie das Symbol im Kontext des Validierungs-Bildschirms, neben dem zu prüfenden Dokument:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Validierungs-Bildschirm mit verfügbarem Barcode-Symbol"><figcaption><p>Der Validierungs-Bildschirm — das Barcode-Symbol (hervorgehoben, rechte Werkzeugleiste) wird nur angezeigt, wenn die Barcode-Zuordnung aktiviert ist.</p></figcaption></figure>

### Wie Barcodes ausgelesen werden

DocBits erkennt die Barcodes während der Dokumentverarbeitung und bietet ihre dekodierten Werte zur Zuordnung an. Ein einzelnes Dokument kann mehrere Barcode-Typen tragen — zum Beispiel einen **QR-Code**, einen **Code 128** und einen **EAN-13** — die jeweils einen anderen Wert kodieren, etwa eine Bestellnummer, eine Rechnungsnummer oder eine Lieferanten-GLN.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Demo-Rechnung mit mehreren Barcode-Typen"><figcaption><p>Beispielhafte DocBits-Demo-Rechnung mit drei Barcode-Typen (QR-Code → Bestellnummer, Code 128 → Rechnungsnummer, EAN-13 → Lieferanten-GLN), die jeweils einen einem Feld zuordenbaren Wert kodieren.</p></figcaption></figure>

{% hint style="info" %}
Welche Barcode-Typen erkannt werden, steuert die Einstellung **Bar-Code / QR-Code-Extraktion** (`Barcode Extraction Types`). Zeigt der Dialog *„no barcodes extracted found“*, stellen Sie sicher, dass die Barcode-Extraktion aktiviert ist und die erwarteten Typen (z. B. `QRCODE`, `CODE128`, `EAN13`) ausgewählt sind. Siehe [Bar-Code / QR-Code-Extraktion](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Den Barcode-Zuordnungs-Dialog verwenden

1. Öffnen Sie ein Dokument im **Validierungs-Bildschirm**.
2. Klicken Sie auf das **Barcode-Symbol** in der rechten Werkzeugleiste.
3. Der Dialog **Barcode-Zuordnung** listet jeden von DocBits im Dokument erkannten Barcode auf, dargestellt als `Barcode <n> : <Wert>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Barcode-Zuordnungs-Dialog mit den erkannten Barcodes"><figcaption><p>Der Barcode-Zuordnungs-Dialog listet jeden erkannten Barcode mit einer Auswahlliste zur Wahl des Zielfelds auf.</p></figcaption></figure>

4. Öffnen Sie für jeden Barcode die Auswahlliste und wählen Sie das Feld, in das der Wert übernommen werden soll.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Auswahl des Zielfelds für einen Barcode"><figcaption><p>Jeder Barcode kann einem beliebigen Dokumentfeld zugeordnet werden — z. B. Bestellnummer, Rechnungsnummer, Lieferanten-ID.</p></figcaption></figure>

5. Sobald Sie ein Feld auswählen, wird dieses Feld mit dem Wert des Barcodes befüllt.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Barcode dem Feld Bestellnummer zugeordnet"><figcaption><p>Nach Auswahl eines Felds (hier Bestellnummer) wird das Feld mit dem Barcode-Wert befüllt.</p></figcaption></figure>

### Aktivieren

1. Gehen Sie zu **Einstellungen**.
2. Wählen Sie **Dokumentverarbeitung**.
3. Wählen Sie **Modul**.
4. Öffnen Sie den Abschnitt **Dokumenttyp**.
5. Finden Sie **Barcode-Zuordnung** und schalten Sie den Schalter ein.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Schalter Barcode-Zuordnung"><figcaption><p>Der Schalter Barcode-Zuordnung unter Einstellungen → Dokumentverarbeitung → Modul.</p></figcaption></figure>

### Vorteile

* **Schnellere, fehlerfreie Erfassung**: Übernehmen Sie Werte direkt aus einem Barcode, statt sie abzulesen und abzutippen.
* **Weniger Tippfehler**: Ein gescannter Wert entspricht genau dem, was im Barcode kodiert ist.
* **Volle Kontrolle**: Sie entscheiden bei der Validierung, welcher Barcode in welches Feld kommt.

### Wann diese Funktion nutzen

* **Dokumente mit Barcodes**: Wenn Ihre Dokumente Barcodes/QR-Codes enthalten, deren Werte in bestimmte Felder gehören (z. B. Bestell- oder Referenznummern).
* **Manuelle Validierungs-Workflows**: Wenn eine Person Dokumente prüft und Felder schnell aus Barcodes befüllen möchte.
* **Ausgeschaltet lassen**, wenn Ihre Dokumente keine nutzbaren Barcodes haben oder Sie nur die automatische Barcode-/QR-**Extraktion** benötigen — siehe [Bar-Code / QR-Code-Extraktion](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**Hier geht es darum, einen Barcode-/QR-Wert auszulesen und ihn bei der Validierung einem Feld zuzuordnen.** Das automatische Extrahieren strukturierter Daten aus Zahlungscodes (z. B. Swiss QR Bill oder GiroCode) — sowie das Aufteilen einer mehrseitigen Datei an Barcode-Trennseiten — übernimmt eine **andere** Einstellung: [Bar-Code / QR-Code-Extraktion](bar-code-qr-code-extraction/README.md).
{% endhint %}
