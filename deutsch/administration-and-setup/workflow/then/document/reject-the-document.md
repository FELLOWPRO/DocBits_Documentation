# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Reject the Document"** wird verwendet, um ein Dokument innerhalb eines Workflows als abgelehnt zu markieren. Diese Aktion stoppt den Fortschritt des Dokuments und verhindert, dass es in die nächste Phase des Workflows übergeht. Sie stellt sicher, dass Dokumente, die die erforderlichen Bedingungen oder Kriterien nicht erfüllen, markiert und von der weiteren Verarbeitung ausgeschlossen werden.

## **Bestandteile der Karte:**

1. **Ablehnungsstatus**
   * **Beschreibung**: Diese Komponente markiert das Dokument als abgelehnt und signalisiert, dass es die für die Freigabe erforderlichen Bedingungen nicht erfüllt hat.
   * **Detail**: Wird diese Karte ausgelöst, aktualisiert sie den Status des Dokuments auf "abgelehnt". Diese Entscheidung wird auf Basis der in den Abschnitten **"Where"** und **"And"** festgelegten Bedingungen getroffen.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** festgelegten Bedingungen aus.
  * Sind **beide Bedingungen erfüllt**, wird das Dokument abgelehnt.
  * Ist **eine der Bedingungen nicht erfüllt**, wird die Karte nicht ausgeführt, und der Status des Dokuments bleibt unverändert.
* **Ausführung der Aktion**: Sind die Bedingungen erfüllt, wird das Dokument als abgelehnt markiert. Diese Aktion stellt sicher, dass nur Dokumente, die bestimmte Kriterien erfüllen, weiter fortfahren, während andere markiert und zur Prüfung oder Korrektur angehalten werden.

## **Fazit:**

Die Workflow-Karte **"Reject the Document"** ist ein unverzichtbares Werkzeug, um den Dokumentfluss in automatisierten Prozessen zu steuern. Indem sie die Ablehnung nicht konformer Dokumente ermöglicht, stellt sie sicher, dass nur gültige und korrekte Dokumente den Workflow durchlaufen, und verbessert so die Effizienz und Genauigkeit im Dokumentenmanagement.
