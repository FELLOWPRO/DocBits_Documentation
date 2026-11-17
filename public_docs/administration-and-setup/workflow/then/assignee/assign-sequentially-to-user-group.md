# Nacheinander Benutzer/Gruppe zuweisen

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_decision_table_sequential_v2-de-de.png" alt="Nacheinander Benutzer/Gruppe zuweisen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_decision_table_sequential_no_variables_v2-de-de.png" alt="Ordnen Sie das Dokument auf der Grundlage der Entscheidungstabelle nacheinander einem Benutzer/einer Gruppe zu. — Version 2" width="634"><figcaption><p>Ordnen Sie das Dokument auf der Grundlage der Entscheidungstabelle nacheinander einem Benutzer/einer Gruppe zu. — Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/de.mp4" %}

**Video:** Karte: Nacheinander per Entscheidungstabelle zuweisen · 0:45 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Nacheinander per Entscheidungstabelle zuweisen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/de.mp4#t=0.25)

Die Karte Nacheinander per Entscheidungstabelle zuweisen gibt das Dokument nacheinander an die Benutzer und Gruppen, die eine Entscheidungstabelle zurückgegeben hat. Die Karte hat keine Einstellungen: Alles kommt aus der Tabelle.

**Was die Karte braucht** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/de.mp4#t=14.85)

Sie braucht davor eine Entscheidungstabellen-Karte, die ihre Rückgabe speichert. Sie nimmt alle Benutzer und Gruppen, die die Tabelle zurückgegeben hat, und die niedrigste Priorität bekommt das Dokument zuerst. Zeilen ohne Priorität zählen als Priorität eins. Hat die Tabelle niemanden zurückgegeben, nimmt die Karte ihren Fehlerpfad.

**Beispiel: zwei Freigebende nacheinander** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/de.mp4#t=33.85)

Zum Beispiel gibt die Tabelle Example approvers zwei Freigebende mit Priorität eins und zwei zurück. Die Rechnung geht an den ersten und nach der Freigabe an den zweiten.

</details>

## **Zweck**

Die Workflow-Karte "**Ordnen Sie das Dokument basierend auf der Entscheidungstabelle der Reihe nach einem Benutzer/einer Gruppe zu**" weist Dokumente dynamisch entweder einem Benutzer oder einer Gruppe zu, abhängig von der Auswertung der Entscheidungstabelle. Dadurch wird sichergestellt, dass Dokumente auf Basis vordefinierter Regeln angemessen weitergeleitet werden.

## **Bestandteile der Karte**

1. **Priorität (Wert)**
   * **Beschreibung**: Gibt die Prioritätsstufe für Zuweisungen an, wobei niedrigere Zahlen eine höhere Priorität darstellen.
   * **Detailliert**: Ein numerisches Eingabefeld, in dem der Prioritätswert festgelegt werden kann, um die Reihenfolge der Zuweisung zu steuern.

## **Funktionalität**

* **Auswertung der Entscheidungstabelle**:\
  Die Entscheidungstabelle wertet vordefinierte Bedingungen aus, um zu entscheiden, ob das Dokument einem Benutzer oder einer Gruppe zugewiesen wird.
* **Dokumentzuweisung**:
  * Gibt die Entscheidungstabelle einen Benutzer zurück, wird das Dokument direkt diesem Benutzer zugewiesen.
  * Gibt die Entscheidungstabelle eine Gruppe zurück, wird das Dokument der Gruppe sequenziell zugewiesen, wobei der angegebene Prioritätswert berücksichtigt wird.

## **Einrichtung und Konfiguration**

1. Fügen Sie die Karte **Ordnen Sie das Dokument der Reihe nach zu** zu Ihrem Workflow hinzu.
2. Konfigurieren Sie das Feld **Priorität (Wert)**:
   * Geben Sie einen numerischen Wert ein, um die Zuweisungspriorität festzulegen.
3. Speichern und aktivieren Sie den Workflow, um die Konfiguration anzuwenden.

## **Fazit**

Die Workflow-Karte "**Ordnen Sie das Dokument basierend auf der Entscheidungstabelle der Reihe nach einem Benutzer/einer Gruppe zu**" sorgt für eine effiziente und dynamische Weiterleitung von Dokumenten. Durch die Nutzung der Logik der Entscheidungstabelle und der Prioritätswerte ermöglicht die Karte eine präzise Zuweisung an entweder einen Benutzer oder eine Gruppe und optimiert so Dokument-Workflows.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Verwenden Sie eine Entscheidungstabelle, um einen priorisierten Dokumentzuständigen auszuwählen.

**Konfiguration:** Konfigurieren Sie eine passende Demo-Entscheidungstabellenregel, die den gewünschten Benutzer oder die gewünschte Gruppe zurückgibt, und wählen Sie dann diese Tabelle auf der Karte aus.

**Erwartetes Ergebnis und Gegenbeispiel:** Der zurückgegebene Beauftragte wird für die sequentielle Dokumentenzuweisung verwendet. Wenn keine passende Rückgabe vorliegt, gehen Sie nicht von einem Standardempfänger aus; Überprüfen Sie das Ergebnis und das konfigurierte Fallback-Verhalten dieser Version.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
