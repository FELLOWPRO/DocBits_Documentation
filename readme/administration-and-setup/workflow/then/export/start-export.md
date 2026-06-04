# Start Export

<figure><img src="../../../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Die Workflow-Karte **"Start Export"** ist darauf ausgelegt, den Exportprozess für ein Dokument einzuleiten. Diese Karte fungiert als Auslöser innerhalb des Workflows, um den Exportvorgang nahtlos zu starten, sobald die Bedingungen in den vorangehenden Abschnitten erfüllt sind.

## **Bestandteile der Karte:**

1. **Aktion**
   1. **Beschreibung**: Leitet den Exportprozess für das Dokument ein.
   2. **Detail**: Die Karte verwendet die im System konfigurierten Exporteinstellungen, um das Dokument zu verarbeiten und zu exportieren.

## **Funktionalität:**

* **Bedingungsauswertung**: Das System wertet die in den Abschnitten **"Where"** und **"And"** des Workflows festgelegten Bedingungen aus. Sind alle Bedingungen erfüllt, beginnt der Exportprozess.
* **Dokumentexport**: Das Dokument wird mithilfe der Standard- oder zuvor definierten Exportkonfiguration verarbeitet und exportiert.

## **Einrichtung und Konfiguration:**

Diese Karte erfordert keine spezielle Konfiguration, da sie die bereits im System definierten Exporteinstellungen verwendet. Benutzer müssen sicherstellen, dass:

1. Die Bedingungen in den Abschnitten **"Where"** und **"And"** korrekt konfiguriert sind, da die Karte nur ausgeführt wird, wenn diese Bedingungen als erfüllt ausgewertet werden.
2. Dem Dokument im System eine gültige Exportkonfiguration zugeordnet ist.

## **Fazit:**

Die Workflow-Karte **"Start Export"** bietet eine optimierte und automatisierte Möglichkeit, den Exportprozess auszulösen. Indem sie sich auf vorkonfigurierte Einstellungen und bedingte Auswertungen stützt, gewährleistet sie eine effiziente und präzise Dokumentverarbeitung.
