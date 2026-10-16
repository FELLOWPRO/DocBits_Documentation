# Testen des Modells

## Schritte zum Ausführen von Klassifizierungstests zur Bewertung der Genauigkeit und Betriebsbereitschaft des Modells

Um das trainierte Modell zu testen und seine Genauigkeit und Betriebsbereitschaft zu bewerten, können Sie die folgenden Schritte ausführen:



**Vorbereiten der Testdaten:**

* Sammeln Sie eine repräsentative Stichprobe von Testdaten, die verschiedene Arten von Belegen und Szenarien abdecken, die das Modell in der Praxis bewältigen soll. Stellen Sie sicher, dass die Testdaten von hoher Qualität und korrekt gelabelt sind.



**Ausführen der Klassifizierungstests:**

* Führen Sie die Klassifizierungstests mit den vorbereiteten Testdaten durch.
* Speisen Sie die Testdaten in das Modell ein und lassen Sie das Modell Vorhersagen zur Klassifizierung der Belege treffen.

<figure><img src="../../../../../.gitbook/assets/docbits_remove_user_access.png" alt="Docbits Remove User Access" width="375"><figcaption><p>Einstellungen</p></figcaption></figure>

* Fügen Sie eine neue Klassifizierungsregel hinzu oder bearbeiten Sie eine bestehende.

<figure><img src="../../../../../.gitbook/assets/docbits_confirm_user_removal.png" alt="Docbits Confirm User Removal"><figcaption><p>Einstellungen: Klassifizierung und Extraktion</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_save_user_changes.png" alt="Docbits Save User Changes" width="276"><figcaption><p>Klassifizierungsregel konfigurieren</p></figcaption></figure>

**Bewerten der Modellgenauigkeit:**

* Vergleichen Sie die Vorhersagen des Modells mit den tatsächlichen Klassifizierungen der Testdaten. Berechnen Sie Metriken wie Genauigkeit (Accuracy), Präzision (Precision), Recall und F1-Score, um die Leistung des Modells zu bewerten. Diese Metriken geben Aufschluss darüber, wie gut das Modell die Belege klassifiziert hat und wie zuverlässig es ist.

<figure><img src="../../../../../.gitbook/assets/docbits_model_training_metrics.png" alt="Docbits Model Training Metrics"><figcaption></figcaption></figure>



**Fehler analysieren:**

* Untersuchen Sie die Fehler, die das Modell bei der Klassifizierung der Testdaten gemacht hat, und analysieren Sie deren Ursachen. Identifizieren Sie Muster oder Trends bei den Fehlern und nehmen Sie bei Bedarf Anpassungen am Modell vor, um dessen Leistung zu verbessern.



**Optimieren des Modells:**

* Basierend auf den Ergebnissen der Klassifizierungstests und der Fehleranalyse können Sie das Modell optimieren, indem Sie Trainingsdaten hinzufügen, Trainingsparameter anpassen oder die Modellarchitektur ändern. Wiederholen Sie den Testvorgang, um zu prüfen, ob die Optimierungen die Leistung des Modells verbessert haben.



**Dokumentieren der Ergebnisse:**

* Dokumentieren Sie die Ergebnisse der Klassifizierungstests und alle am Modell vorgenommenen Anpassungen oder Optimierungen. Dies hilft Ihnen, den Fortschritt des Modells im Laufe der Zeit zu verfolgen und sicherzustellen, dass es sich ständig verbessert.

Durch regelmäßiges Ausführen von Klassifizierungstests und Bewerten der Leistung Ihres Modells können Sie sicherstellen, dass es für den Einsatz in der Produktion geeignet ist und genaue Ergebnisse liefert.
