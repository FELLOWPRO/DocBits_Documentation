# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Die Karte **"Run Workflow"** ermöglicht es Benutzern, dynamisch einen ausgewählten Workflow aus einer Liste verfügbarer Workflows auszuführen. Diese Karte ist nützlich, um Prozesse zu automatisieren, bei denen mehrere Workflows miteinander verbunden sind, und ermöglicht so optimierte Abläufe.

## Bestandteile der Karte:

1. **Workflow**
   * **Beschreibung:** Gibt den Workflow an, der ausgeführt wird, wenn die Bedingungen als erfüllt ausgewertet werden.
   * **Detail:** Zur Auswahl wird eine Dropdown-Liste aller verfügbaren Workflows bereitgestellt.

## Funktionalität:

* **Bedingungsauswertung:** Die Karte führt den ausgewählten Workflow nur aus, wenn sowohl der **"Where"**- als auch der **"And"**-Abschnitt als erfüllt ausgewertet werden.
  * Ist eine der Bedingungen nicht erfüllt, wird keine Aktion ausgeführt, und der Workflow bleibt nicht ausgelöst.
* **Workflow-Ausführung:**
  * Sind die Bedingungen erfüllt, wird der angegebene Workflow automatisch ausgelöst.
  * Sind die Bedingungen nicht erfüllt, wird kein Workflow ausgeführt.

## Einrichtung und Konfiguration:

1. **Workflow auswählen:** Wählen Sie den auszulösenden Workflow aus der **Dropdown-Liste** der verfügbaren Workflows.
2. **Bedingungen definieren:** Konfigurieren Sie die Abschnitte **"Where"** und **"And"**, um die Kriterien festzulegen, die erfüllt sein müssen, damit der Workflow ausgeführt wird.

## Fazit:

Die Karte **"Run Workflow"** bietet eine komfortable und effiziente Möglichkeit, Workflows zu verknüpfen und mehrstufige Prozesse mühelos zu automatisieren. Indem sichergestellt wird, dass die Bedingungen in den Abschnitten **"Where"** und **"And"** erfüllt sind, können Benutzer Workflows dynamisch ausführen und manuelle Eingriffe reduzieren.
