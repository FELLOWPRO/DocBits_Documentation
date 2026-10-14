# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, Artikel-IDs zwischen einer Bestellung und einem zugehörigen Dokument zu vergleichen, um sicherzustellen, dass die richtigen Artikel enthalten sind. Die Karte wertet aus, ob die Artikel-ID in der Bestellung mit der Artikel-ID im Dokument übereinstimmt. Dieser Vergleich kann Aktionen auslösen, wenn Abweichungen festgestellt werden, und stellt so sicher, dass die Artikel im Dokument mit der Bestellung übereinstimmen.

## **Bestandteile der Karte:**

1. **Any / All:**
   * **Beschreibung**: Legt fest, ob die Bedingung für irgendeinen oder alle Fälle des Artikel-ID-Vergleichs gilt.
   * **Optionen**:
     * **Any**: Die Bedingung ist erfüllt, wenn irgendeine Artikel-ID in der Bestellung mit der Artikel-ID im Dokument übereinstimmt.
     * **All**: Die Bedingung ist nur erfüllt, wenn alle Artikel-IDs in der Bestellung mit den Artikel-IDs im Dokument übereinstimmen.
2. **Operator:**
   * **Beschreibung**: Legt die Bedingung für den Vergleich der Artikel-ID auf der Bestellung mit der Artikel-ID auf dem Dokument fest.
   * **Optionen**:
     * **Gleich (=)**: Überprüft, ob die Artikel-ID in der Bestellung exakt mit der Artikel-ID im Dokument übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass die Artikel-ID in der Bestellung nicht mit der Artikel-ID im Dokument übereinstimmt.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System vergleicht die Artikel-ID in der Bestellung mit der Artikel-ID im Dokument auf Basis des ausgewählten Operators. Ist die Vergleichsbedingung erfüllt (z. B. stimmen die Artikel-IDs überein oder nicht überein), wird der Workflow entsprechend fortgesetzt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True)**: Ergibt die Bedingung „wahr“ (z. B. ist die Artikel-ID in der Bestellung gleich der Artikel-ID im Dokument), wird der Workflow mit der True-Aktion fortgesetzt (z. B. Freigabe oder weitere Verarbeitung).
  * **Bedingung nicht erfüllt (False)**: Ergibt die Bedingung „falsch“ (z. B. stimmt die Artikel-ID in der Bestellung nicht mit der Artikel-ID im Dokument überein), wird der Workflow nicht fortgesetzt.

## **Einrichtung und Konfiguration:**

* Benutzer konfigurieren die Karte, indem sie die Artikel-ID sowohl in der Bestellung als auch im Dokument auswählen. Anschließend wählen sie den passenden Operator (Gleich oder Ungleich), um festzulegen, wie die Artikel-IDs verglichen werden. Zuletzt wählen die Benutzer aus, ob die Bedingung für irgendeine oder alle Artikel-IDs im Vergleich gilt.

## **Beispiel-Szenario:**

* Eine Rechnung führt einen Artikel mit der ID "ABC123" auf, und die zugehörige Bestellung enthält ebenfalls einen Artikel mit der ID "ABC123". Mit dem Operator "Gleich" vergleicht die Karte die Artikel-ID im Dokument mit der Artikel-ID in der Bestellung. Da die Artikel-IDs übereinstimmen, wird der Workflow ohne Probleme fortgesetzt.

## **Fazit:**

Die Workflow-Karte "Item ID Comparison" stellt sicher, dass die Artikel-IDs in Dokumenten mit denen in Bestellungen übereinstimmen. Dies hilft, Abweichungen in den Artikelaufstellungen zu vermeiden, und stellt sicher, dass die richtigen Artikel gemäß der Bestellung verarbeitet werden. Die Möglichkeit, auf Basis von irgendeinem oder allen Fällen zu vergleichen, bietet Flexibilität für unterschiedliche Anwendungsfälle und verbessert die Genauigkeit und Effizienz von Beschaffungs-Workflows.
