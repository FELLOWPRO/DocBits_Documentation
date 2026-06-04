# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, die Lieferanteninformationen auf einer Rechnung mit den Lieferanteninformationen auf der zugehörigen Bestellung zu vergleichen. Die Karte stellt sicher, dass der Lieferant auf der Rechnung mit dem Lieferanten auf der Bestellung übereinstimmt. Dieser Vergleich hilft zu überprüfen, ob der richtige Lieferant für die Bestellung in Rechnung stellt, und kann auf Basis etwaiger Abweichungen Aktionen auslösen.

## **Bestandteile der Karte:**

1. **Operator:**
   * **Beschreibung**: Legt die Bedingung für den Vergleich des Lieferanten auf der Rechnung mit dem Lieferanten auf der Bestellung fest.
   * **Optionen**:
     * **Is**: Prüft, ob der Lieferant auf der Rechnung mit dem Lieferanten auf der Bestellung übereinstimmt.
     * **Is Not**: Stellt sicher, dass der Lieferant auf der Rechnung nicht mit dem Lieferanten auf der Bestellung übereinstimmt.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System vergleicht den Lieferanten auf der Rechnung mit dem Lieferanten auf der Bestellung auf Basis des ausgewählten Operators. Ist die Vergleichsbedingung erfüllt (z. B. ist der Lieferant wie erforderlich gleich oder unterschiedlich), wird der Workflow entsprechend fortgesetzt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt die Bedingung „wahr“ (z. B. stimmt der Lieferant auf der Rechnung mit dem Lieferanten auf der Bestellung überein), wird der Workflow fortgesetzt, ohne Fehler auszulösen.
  * **Bedingung nicht erfüllt (False)**: Ergibt die Bedingung „falsch“ (z. B. stimmt der Lieferant auf der Rechnung nicht mit dem Lieferanten auf der Bestellung überein), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* Benutzer wählen den passenden Operator ("Is" oder "Is Not"), um festzulegen, wie die Lieferanten verglichen werden.

## **Beispiel-Szenario:**

* Eine Rechnung führt einen Lieferanten mit der ID "SUP123" auf, und die zugehörige Bestellung führt ebenfalls "SUP123" als Lieferanten auf. Mit dem Operator "Is" vergleicht die Karte die Lieferanten und stellt fest, dass sie identisch sind, sodass der Workflow ohne Probleme fortgesetzt wird.

## **Fazit:**

Die Workflow-Karte "Supplier Comparison" stellt sicher, dass der richtige Lieferant für die Bestellung in Rechnung stellt, und hilft so, Abweichungen und Fehler im Beschaffungsprozess zu vermeiden. Durch die automatische Überprüfung der Lieferanteninformationen können Organisationen ihren Rechnungsfreigabeprozess optimieren und das Risiko von Betrug oder Fehlern bei der Lieferantenabrechnung reduzieren.
