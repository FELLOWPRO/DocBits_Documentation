# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Die Workflow-Karte **"AI Calculation for Cost Increase Surcharges"** nutzt KI, um Zuschlagsbeträge auf Basis von Kostensteigerungen automatisch zu berechnen. Sie sorgt für konsistente und präzise Zuschlagsberechnungen, optimiert Workflows und reduziert den manuellen Aufwand.

## Bestandteile der Karte:

* **Kostensteigerungsfaktor**
  * **Beschreibung:** Der Multiplikator oder Prozentsatz, der auf die Basiskosten angewendet wird, um den Zuschlag zu berechnen.
  * **Detail:** Bestimmt den Zuschlagsbetrag auf Basis der Kostensteigerung (z. B. ein Faktor von 1,10 für eine Steigerung um 10 %).
* **Basiskostenfeld**
  * **Beschreibung:** Das Feld, das den ursprünglichen Kostenwert enthält, der als Grundlage für die Zuschlagsberechnung dient.
  * **Detail:** Wird automatisch ausgewählt oder innerhalb des Workflows definiert, um während der Berechnung als Referenz zu dienen.
* **Zuschlagsfeld**
  * **Beschreibung:** Das Feld, in dem der per KI berechnete Zuschlagswert gespeichert wird.
  * **Detail:** Dieses Feld spiegelt den berechneten Zuschlag wider und macht ihn für die weitere Verarbeitung oder Berichterstattung verfügbar.

## Funktionalität:

**Bedingungsauswertung:**

* Die Karte wird nur aktiviert, wenn sowohl die Bedingungen im **"Where"**- als auch im **"And"**-Abschnitt als erfüllt ausgewertet werden.
* Wird eine der beiden Bedingungen als nicht erfüllt ausgewertet, wird keine Zuschlagsberechnung durchgeführt.

**KI-gestützte Berechnung:**

* Das System wendet den **Kostensteigerungsfaktor** auf das **Basiskostenfeld** an, um den Zuschlag zu berechnen.
* Das Ergebnis wird im **Zuschlagsfeld** gespeichert und stellt so die Verfügbarkeit für nachfolgende Workflow-Schritte sicher.

## Fazit:

Die Workflow-Karte **"AI Calculation for Cost Increase Surcharges"** automatisiert die Anwendung von Zuschlägen auf Basis von Kostensteigerungen. Indem sie KI für Präzision und Konsistenz nutzt, eliminiert diese Karte manuelle Berechnungen, steigert die Effizienz und unterstützt ein präzises Kostenmanagement in automatisierten Workflows.
