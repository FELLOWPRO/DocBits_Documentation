# Bearbeiten und Speichern von Regex-Mustern

## Anleitung zum Ändern bestehender Muster und die Bedeutung des Testens dieser Änderungen, um sicherzustellen, dass sie wie erwartet funktionieren, ohne bestehende Funktionen zu beeinträchtigen.

**Um bestehende Regex-Muster zu bearbeiten und sicherzustellen, dass die Änderungen wie erwartet funktionieren, ohne bestehende Funktionen zu beeinträchtigen, können Sie sich an der folgenden Anleitung orientieren:**

<figure><img src="../../../../../.gitbook/assets/docbits_regex_edit_settings.png" alt="Docbits Regex Edit Settings"><figcaption><p>Einstellungen: Belegtyp</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_regex_pattern_analysis.png" alt="Docbits Regex Pattern Analysis"><figcaption></figcaption></figure>

**Bestehendes Muster analysieren:**

* Untersuchen Sie das bestehende Regex-Muster, um zu verstehen, welche Daten es erfasst und wie es funktioniert.
* Identifizieren Sie die Teile des Musters, die geändert werden müssen, und die Auswirkungen dieser Änderungen auf die erfassten Daten.

**Zum Beispiel: Der Rechnungsbetrag soll ausgelesen werden:**

*   (?<=Rechnungsbetrag:)[\s]*((((\d+)[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Den Betrag mit 1000er Punkt lesen, aber den Punkt NICHT mit übergeben

    [\d.]_[\,\d]_

    Erlaubte Zeichen: 0123456789,
*   Der Wert "P32180" soll ausgelesen werden. Ankerwort ist hier "Invoice Date".

    (?<=InvoiceDate )[\s]*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/docbits_import_start_process.png" alt="Docbits Import Start Process"><figcaption></figcaption></figure>

**Änderungen dokumentieren:**

* Notieren Sie sich die Änderungen, die Sie am Regex-Muster vornehmen möchten.
* Notieren Sie, welche neuen Muster Sie hinzufügen möchten und welche Teile des bestehenden Musters möglicherweise geändert oder entfernt werden müssen.

**Testdaten vorbereiten:**

* Sammeln Sie Testdaten, die repräsentativ für die verschiedenen Datentypen sind, die das Regex-Muster normalerweise erfasst.
* Stellen Sie sicher, dass Ihre Testdaten sowohl typische Fälle als auch Randfälle abdecken, um die Robustheit Ihrer Änderungen zu überprüfen.

**Änderungen am Regex-Muster vornehmen:**

* Nehmen Sie die geplanten Änderungen am Regex-Muster vor.
* Dies kann das Hinzufügen neuer Muster, das Entfernen oder Anpassen bestehender Teile oder die Optimierung des Musters für eine bessere Leistung beinhalten.

**Änderungen testen:**

* Wenden Sie das aktualisierte Regex-Muster auf Ihre Testdaten an und überprüfen Sie die Ergebnisse sorgfältig.
* Vergewissern Sie sich, dass das Muster die gewünschten Daten immer noch korrekt erfasst und dass keine unerwarteten Auswirkungen auf andere Teile der Daten oder des Systems auftreten.

**Debugging und Anpassung:**

* Wenn die Testergebnisse nicht wie erwartet ausfallen oder unerwartete Probleme auftreten, überprüfen Sie Ihre Änderungen sorgfältig und nehmen Sie nach Bedarf weitere Anpassungen vor.
* Dies kann das Rückgängigmachen bestimmter Änderungen oder das Hinzufügen weiterer Anpassungen zur Behebung des Problems beinhalten.

**Änderungen dokumentieren:**

* Aktualisieren Sie die Dokumentation Ihres Regex-Musters, um die vorgenommenen Änderungen widerzuspiegeln.
* Beschreiben Sie die aktualisierten Muster und die Gründe für die vorgenommenen Änderungen, um anderen Entwicklern zu helfen, das Muster zu verstehen und zu verwenden.

**Änderungen speichern:**

* Sobald Sie sicher sind, dass die Änderungen erfolgreich sind und wie erwartet funktionieren, speichern Sie das aktualisierte Regex-Muster in Ihrer Codebasis oder Ihren Konfigurationsdateien, um sicherzustellen, dass sie für die zukünftige Verwendung verfügbar sind.

<figure><img src="../../../../../.gitbook/assets/docbits_model_training_continuous.png" alt="Docbits Model Training Continuous"><figcaption><p>Änderungen speichern</p></figcaption></figure>

Durch Befolgen dieser Schritte und sorgfältiges Testen von Änderungen an Regex-Mustern können Sie sicherstellen, dass Ihr Regex-Muster weiterhin korrekt funktioniert, während es neue Anforderungen erfüllt.
