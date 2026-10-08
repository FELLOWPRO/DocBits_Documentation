# Dokument-Flow

**Dokument-Flow** zeigt die Verarbeitungsschritte eines Dokuments. Damit sehen Sie, welche Schritte abgeschlossen sind, welcher wartet und wie lange die Verarbeitung gedauert hat. Das Beispiel unten verwendet eine synthetische Rechnung im Deutschen Sandbox.

## Öffnen über das Dashboard

Suchen Sie im [Dashboard](../dashboard/) das Dokument. Wählen Sie in der Spalte **Aktionen** die drei Punkte und dann **Dokumentenfluss**. Die Option öffnet den Flow dieses Dokuments; sie ändert das Dokument nicht.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-de-20261008.png" alt="Deutsches Dashboard mit geöffnetem Aktionen-Menü einer synthetischen Rechnung; Dokumentenfluss steht unterhalb von Zuweisen an."><figcaption>Wählen Sie Dokumentenfluss im Aktionen-Menü des Dokuments.</figcaption></figure>

## Öffnen über die Feldvalidierung

Öffnen Sie das Dokument. Wählen Sie im [Validierungsbildschirm](../validation-screen/) die drei Punkte in der rechten Aktionsleiste und dann unter **Mehr Optionen** **Dokumentenfluss**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-de-20261008.png" alt="Deutscher Feldvalidierung-Bildschirm mit dem Menü Mehr Optionen und dem Eintrag Dokumentenfluss neben einer synthetischen Rechnung."><figcaption>Derselbe Flow ist über die Dokumentenansicht erreichbar.</figcaption></figure>

## Den Flow lesen

Die **Prozessstatistik** links fasst die Anzahl der Schritte, abgeschlossene und wartende Schritte, Neustarts, die Gesamtdauer, den aktuellen Status und den Gesamtfortschritt zusammen. Jede nummerierte Karte zeigt einen Verarbeitungsschritt und seinen aktuellen Zustand. Scrollen Sie nach unten, um spätere Schritte zu sehen.

<figure><img src="../../../.gitbook/assets/document-flow-overview-de-20261008.png" alt="Deutscher Dokument-Flow mit Prozessstatistik links und den ersten nummerierten Schritt-Karten: Importiert und OCR."><figcaption>Die ersten Schritte im Flow einer synthetischen Rechnung.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-de-20261008.png" alt="Deutscher Dokument-Flow nach dem Scrollen; weitere Karten sind Klassifiziert, Fields Extracted, Tables Extracted, Transformed, Metadata Populated, Lookup Completed und Waiting for Validation."><figcaption>Scrollen Sie, um der Reihenfolge bis zu den späteren Schritten zu folgen.</figcaption></figure>

Wählen Sie eine Schritt-Karte aus, um die **Step Details** links zu öffnen. Sie zeigen das Modul und seinen Status. Rechts kann sich zusätzlich ein **Task Logs**-Bereich öffnen; die Logdetails hängen davon ab, was für diesen Task verfügbar ist. Wählen Sie in Step Details das **×**, um den Bereich zu schließen.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-de-20261008.png" alt="Deutscher Dokument-Flow mit ausgewählter OCR-Karte; Step Details unter der Prozessstatistik zeigt Modul OCR_COMPLETED und Status Completed."><figcaption>Step Details erklärt den Status des ausgewählten Moduls.</figcaption></figure>
