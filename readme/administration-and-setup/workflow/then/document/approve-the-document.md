# Approve the Document



<figure><img src="../../../../.gitbook/assets/image (281).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Approve the Document"** wird verwendet, um ein Dokument als freigegeben zu markieren. Sie ermöglicht es dem Dokument, in die nächste Phase des Workflows überzugehen, und erlaubt die Ausführung automatisierter Verarbeitungs- oder Freigabe-Workflows. Diese Karte hilft, Dokumentenmanagementprozesse zu optimieren, und stellt sicher, dass nur freigegebene Dokumente für weitere Aktionen weitergeleitet werden.

## **Bestandteile der Karte:**

1. **Freigabestatus**
   * **Beschreibung**: Diese Komponente markiert das Dokument als freigegeben.
   * **Detail**: Wird diese Karte ausgelöst, wird der Freigabestatus des Dokuments aktualisiert, um die Freigabe anzuzeigen. Diese Aktion kann auf Basis der in den Abschnitten **"Where"** und **"And"** definierten Bedingungen festgelegt werden.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** festgelegten Bedingungen aus.
  * Sind **beide Bedingungen erfüllt**, wird das Dokument als freigegeben markiert.
  * Ist **eine der Bedingungen nicht erfüllt**, wird die Karte nicht ausgeführt, und der Freigabestatus des Dokuments bleibt unverändert.
* **Ausführung der Aktion**: Sind die Bedingungen erfüllt, wird das Dokument freigegeben. Diese Änderung spiegelt sich im Dokumentstatus wider und ermöglicht es, im Workflow weiter fortzufahren.

## **Fazit:**

Die Workflow-Karte **"Approve the Document"** ist eine zentrale Komponente für die Automatisierung der Dokumentfreigabe in Geschäftsworkflows. Indem sie sicherstellt, dass nur Dokumente freigegeben werden, die bestimmte Kriterien erfüllen, hilft sie, Konsistenz zu wahren, manuelle Kontrolle zu reduzieren und eine reibungslosere Dokumentverarbeitung zu ermöglichen.
