# Barcode-Zuordnung

### Überblick

Die Einstellung **Barcode-Zuordnung** (Barcode Assignment) ermöglicht es DocBits, **Barcodes innerhalb einer Datei zu nutzen, um sie in einzelne Dokumente zu trennen**. Das ist nützlich, wenn mehrere Dokumente gemeinsam in eine große PDF gescannt werden und ein Barcode markiert, wo ein Dokument endet und das nächste beginnt.

Diese Einstellung ist **standardmäßig deaktiviert**.

### Was bewirkt die Einstellung?

Wenn diese Einstellung aktiviert ist, sucht DocBits in einer eingehenden mehrseitigen Datei nach Barcodes und teilt diese Datei an den markierten Stellen in separate Dokumente auf. Jedes entstandene Dokument wird anschließend einzeln verarbeitet.

* **Aktiviert** — DocBits erkennt Barcodes und trennt eine zusammengefasste Datei automatisch anhand dieser in einzelne Dokumente.
* **Deaktiviert** — Die Datei wird als ein einziges Dokument verarbeitet; Barcodes werden nicht zum Aufteilen verwendet.

{% hint style="info" %}
Hier geht es um das **Aufteilen und Zuordnen** von Seiten anhand von Barcodes. Das Auslesen der in einem Barcode kodierten Daten (z. B. bei Zahlungs-QR-Codes) erfolgt separat unter **Bar-Code / QR Code Extraction**.
{% endhint %}

### Vorteile

* **Schnelleres Stapel-Scannen**: Scannen Sie einen ganzen Stapel Dokumente in einem Durchgang, getrennt durch Barcode-Trennblätter, statt jedes Dokument einzeln zu scannen.
* **Weniger manuelles Sortieren**: DocBits erstellt die einzelnen Dokumente für Sie, sodass niemand die PDF von Hand aufteilen muss.
* **Weniger Fehler**: Dokumente werden jedes Mal exakt an den markierten Stellen getrennt.

### Verwendung

1. Gehen Sie zu **Einstellungen**.
2. Wählen Sie **Dokumentverarbeitung**.
3. Wählen Sie **Modul**.
4. Öffnen Sie den Abschnitt **Dokumenttyp**.
5. Finden Sie **Barcode-Zuordnung** und schalten Sie den Schalter ein.

### Wann diese Funktion nutzen

* **Hohes Scan-Volumen**: Wenn Sie viele Dokumente gemeinsam scannen und Barcode-Trennblätter dazwischen verwenden.
* **Gemischte Stapel**: Wenn eine einzelne eingehende Datei mehrere verschiedene Dokumente enthält, die separat verarbeitet werden müssen.
* **Ausgeschaltet lassen**, wenn Ihre Dokumente immer als separate Dateien ankommen — ein Aufteilen ist dann nicht nötig.
