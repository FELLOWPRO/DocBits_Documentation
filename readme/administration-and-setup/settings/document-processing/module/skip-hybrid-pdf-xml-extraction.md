# Hybride PDF-XML-Extraktion überspringen

### Überblick

Die Einstellung **Hybride PDF-XML-Extraktion überspringen** (Skip Hybrid PDF XML Extraction) steuert, wie DocBits **hybride PDFs** verarbeitet — PDF-Rechnungen mit eingebetteter strukturierter E-Rechnung (ZUGFeRD / Factur-X). Sie entscheidet, ob das **strukturierte XML im PDF** das führende Dokument für die automatische Verarbeitung ist oder ob das **PDF selbst** per OCR als primäres Dokument verarbeitet wird.

Diese Einstellung ist besonders für **US-Kunden** relevant. Anders als in der EU/DE gibt es in den USA keine allgemeine B2B-E-Rechnungspflicht. US-Organisationen möchten das PDF daher meist als primäre, menschenlesbare Rechnung behandeln — auch wenn ein Geschäftspartner eine ZUGFeRD/Factur-X-Datei mit eingebettetem XML sendet.

### Was bewirkt die Einstellung?

Eine ZUGFeRD/Factur-X-Datei ist ein einzelnes PDF, das zusätzlich eine maschinenlesbare XML-Rechnung enthält. Standardmäßig erkennt DocBits dieses eingebettete XML und nutzt es als führende Quelle für die Extraktion (strukturierter elektronischer Pfad).

* **Deaktiviert (Standard)** — DocBits erkennt das eingebettete E-Rechnungs-XML und verarbeitet das Dokument auf dem **strukturierten elektronischen Pfad**. Das XML ist die führende Rechnung. Dies ist das rechtlich korrekte Verhalten für EU/DE, wo die strukturierte E-Rechnung die maßgebliche Rechnung ist und das PDF nur eine Visualisierung / Lesekopie.
* **Aktiviert** — DocBits **ignoriert das eingebettete XML** und leitet das Dokument an den **PDF-Prozessor (OCR)**. Das PDF wird zum primären Verarbeitungsdokument. Dies ist die typische Wahl für **US-Organisationen**, die eine PDF-first-Verarbeitung wünschen.

{% hint style="info" %}
Diese Einstellung betrifft ausschließlich **hybride PDFs** (ZUGFeRD / Factur-X = eine `.pdf` mit eingebettetem XML). Eine reine XRechnung-/EDI-Datei, die als `.xml` hochgeladen wird, wird immer auf dem strukturierten elektronischen Pfad verarbeitet — es gibt kein PDF, das primär werden könnte.
{% endhint %}

### Audit & Compliance — das Original bleibt immer erhalten

Das Aktivieren dieser Einstellung **verwirft die E-Rechnung nicht**. Das Originalartefakt bleibt stets erhalten:

* Das ursprüngliche ZUGFeRD/Factur-X-**PDF — einschließlich des eingebetteten XML — bleibt gespeichert** und herunterladbar. Aus der gespeicherten Kopie des Dokuments wird nichts gelöscht.
* Die Verarbeitung ändert nur, **welcher Inhalt die Extraktion steuert** (PDF/OCR vs. eingebettetes XML), nicht das, was archiviert wird.

So kann eine US-Organisation das PDF primär verarbeiten, während die strukturierte E-Rechnung für Audits verfügbar bleibt.

{% hint style="warning" %}
Für EU/DE-Organisationen sollte diese Einstellung **deaktiviert** bleiben. Nach den E-Rechnungsregeln ab 2025 ist eine strukturierte E-Rechnung (ZUGFeRD/Factur-X, XRechnung) die rechtlich maßgebliche Rechnung; ein einfaches PDF ist nur eine Lesekopie. Das PDF anstelle der strukturierten Daten primär zu verarbeiten, ist nicht angemessen, wenn eine gültige E-Rechnung vorliegt.
{% endhint %}

### Verwendung

1. **Einstellung öffnen**:
   * Gehen Sie zu **Einstellungen**.
   * Wählen Sie **Dokumentverarbeitung**.
   * Wählen Sie **Modul**.
   * Öffnen Sie den Abschnitt **Dokumenttyp**.
   * Finden Sie **Hybride PDF-XML-Extraktion überspringen** und betätigen Sie den Schalter.
2. **Modus wählen**:
   * **US- / PDF-first-Organisationen** → Schalter aktivieren, damit ZUGFeRD/Factur-X-PDFs per OCR als primäres Dokument verarbeitet werden.
   * **EU/DE-Organisationen** → Schalter deaktiviert lassen, damit die strukturierte E-Rechnung das führende Dokument bleibt.
3. **Prüfen**:
   * Laden Sie ein ZUGFeRD/Factur-X-PDF hoch und prüfen Sie das Verarbeitungsergebnis — bei aktiviertem Schalter wird es als reguläres PDF (OCR) behandelt, bei deaktiviertem Schalter werden die eingebetteten E-Rechnungsdaten extrahiert.

### Wann diese Funktion nutzen

* **US-Kunden / keine E-Rechnungspflicht**: aktivieren, damit das vertraute PDF das primäre Verarbeitungsdokument ist, während die eingebettete E-Rechnung archiviert bleibt.
* **Gemischte/PDF-first-Workflows**: aktivieren, wenn nachgelagerte Prozesse, Validierung oder Prüfung auf dem PDF-Layout statt auf dem XML beruhen.
* **EU/DE-Compliance**: deaktiviert lassen, damit strukturierte E-Rechnungsdaten die Verarbeitung steuern, wie gefordert.
