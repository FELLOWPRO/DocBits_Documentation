# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, den aktuellen Zustand eines Kontrollkästchenfelds umzukehren. Ist das Kontrollkästchen aktiviert (true), wird es deaktiviert (false), und umgekehrt. Die Umkehrung erfolgt auf Basis der in den Abschnitten **"Where"** und **"And"** festgelegten Bedingungen. Diese Karte hilft, Workflows zu automatisieren, bei denen eine Bedingung das Umschalten eines Kontrollkästchens auf Basis bestimmter Kriterien erfordert.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung**: Gibt das umzukehrende Kontrollkästchenfeld an.&#x20;
   * **Detail**: Der Zustand des ausgewählten Kontrollkästchenfelds wird je nach aktuellem Zustand von true auf false oder von false auf true umgeschaltet.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** definierten Bedingungen aus:
  * Sind **beide Bedingungen erfüllt**, wird die Aktion im **"Then"-Abschnitt** ausgeführt, was in diesem Fall bedeutet, dass das Kontrollkästchenfeld umgeschaltet wird.
  * Ist **eine der beiden Bedingungen nicht erfüllt**, wird die Karte nicht ausgeführt, und es erfolgt keine Änderung am Kontrollkästchenfeld.
* **Ausführung der Aktion**: Werden die Bedingungen in den Abschnitten **"Where"** und **"And"** als erfüllt ausgewertet, wird der Zustand des Kontrollkästchenfelds umgekehrt:
  * Ist das Kontrollkästchen aktiviert (true), wird es deaktiviert (false).
  * Ist das Kontrollkästchen deaktiviert (false), wird es aktiviert (true).

## **Einrichtung und Konfiguration:**

Um diese Karte zu konfigurieren, müssen Benutzer:

1. **Das umzukehrende Kontrollkästchenfeld auswählen** (Feldname). Die verfügbaren Kontrollkästchenfelder im Dokument werden zur Auswahl aufgelistet.
2. Das Kontrollkästchenfeld wird nur umgekehrt, wenn die Bedingungen in beiden Abschnitten **"Where"** und **"And"** erfüllt sind.

## **Fazit:**

Die Workflow-Karte **"Invert checkbox \[Field Name]"** bietet ein einfaches, aber leistungsstarkes Automatisierungswerkzeug, um Kontrollkästchenwerte auf Basis bestimmter Bedingungen umzuschalten. Indem sie den Bedarf an manuellen Anpassungen von Kontrollkästchen reduziert, steigert diese Karte die Effizienz bei der Dokumentverarbeitung und sorgt für Konsistenz über Workflows hinweg.
