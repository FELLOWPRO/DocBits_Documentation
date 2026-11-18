# Entscheidungstabelle liefert Ergebnisse

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v2-de-de.png" alt="Entscheidungstabelle liefert Ergebnisse, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v3-de-de.png" alt="Entscheidungstabelle liefert Ergebnisse, Version 3" width="634"><figcaption><p>Version 3</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/de.mp4" %}

**Video:** Karte: Entscheidungstabelle hat Rückgabewerte · 0:47 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Entscheidungstabelle hat Rückgabewerte** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/de.mp4#t=0.25)

Die Karte Entscheidungstabelle hat Rückgabewerte führt eine Entscheidungstabelle für das Dokument aus. Wählen Sie die Tabelle, zum Beispiel Example approvers, und ob ihre Rückgabedaten für die nächsten Karten gespeichert werden.

**Eine passende Zeile heißt wahr** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/de.mp4#t=17.516)

Passt eine Zeile der Tabelle zum Dokument, ist die Karte wahr. Passt keine Zeile, ist sie falsch. Gespeicherte Daten nutzen spätere Karten, etwa die Zuweisungskarten. Ein Workflow behält nur das zuletzt gespeicherte Ergebnis.

**Beispiel: Genehmiger aus einer Tabelle** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/de.mp4#t=34.283)

Zum Beispiel findet die Tabelle die Genehmiger für den Rechnungsbetrag und speichert sie, und die nächste Karte weist ihnen die Rechnung zu. Findet die Tabelle niemanden, ist die Karte falsch und die Zuweisung läuft nicht.

</details>

## **Zweck:**

Diese DocBits-Karte prüft, ob eine angegebene Entscheidungstabelle für ein bestimmtes Dokument Rückgabewerte enthält, und bestimmt, ob die zurückgegebenen Daten in nachfolgenden Workflow-Schritten verwendet werden sollen. Sie stellt sicher, dass sich Workflows dynamisch an die Ergebnisse der Entscheidungstabelle anpassen können.

## **Funktionalität:**

* **Validierung der Entscheidungstabelle:** Diese Karte überprüft, ob die ausgewählte Entscheidungstabelle Rückgabewerte für das verarbeitete Dokument liefert.
* **Auswahl der Entscheidungstabelle:** Benutzer geben den Namen der zu prüfenden Entscheidungstabelle an.
* **Rückgabedaten verwenden:** Benutzer können mit einer **Boolescher Wert**-Einstellung festlegen, ob die Rückgabedaten in späteren Karten verwendet werden sollen:
  * **True:** Die Rückgabedaten sind verfügbar und werden in nachfolgenden Workflow-Schritten verwendet.
  * **False:** Die Rückgabedaten werden nicht verwendet, und der Workflow wird ohne sie fortgesetzt.

## **Verwendung:**

Diese Karte eignet sich ideal für Workflows mit bedingter Logik oder Entscheidungsfindung auf Basis vordefinierter Regeln in einer Entscheidungstabelle. Sie sorgt für eine nahtlose Integration der Ausgaben der Entscheidungstabelle in Workflow-Prozesse.

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie die Entscheidungstabelle **„Regeln zur Rechnungsbearbeitung“** auf Rückgabewerte prüft. Der **Boolescher Wert** ist auf **True** gesetzt, was angibt, dass die Rückgabedaten (z. B. Freigabeanforderungen) in späteren Karten genutzt werden, um Workflow-Entscheidungen zu steuern.

Durch die Verwendung der Karte "Decision Table Check" können Organisationen die Flexibilität von Workflows erhöhen, die regelbasierte Verarbeitung optimieren und Konsistenz bei der Entscheidungsfindung über automatisierte Workflows hinweg sicherstellen.
