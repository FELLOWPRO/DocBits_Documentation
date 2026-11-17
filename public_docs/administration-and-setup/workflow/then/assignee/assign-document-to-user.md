# Dokument dem Benutzer zuweisen

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v1-de-de.png" alt="Dokument dem Benutzer zuweisen, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v2-de-de.png" alt="Dokument dem Benutzer zuweisen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_user_assign_v3-de-de.png" alt="Dokument dem Benutzer zuweisen, Version 3" width="634"><figcaption><p>Version 3</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-user/v1/de.mp4" %}

**Video:** Karte: Dokument einem Benutzer zuweisen · 0:53 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-user/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Dokument einem Benutzer zuweisen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-user/v1/de.mp4#t=0.25)

Die Karte Dokument dem Benutzer zuweisen gibt das Dokument einem Benutzer: Wählen Sie den Benutzer. Version drei, gewählt über das Versionslabel, bringt eine zweite Einstellung: ob stattdessen eine Entscheidungstabelle den Benutzer wählen darf.

**Entscheidungsbaum verwenden: zuerst der Benutzer der Tabelle** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-user/v1/de.mp4#t=21.75)

Ist Entscheidungsbaum verwenden eingeschaltet, nimmt die Karte den ersten Benutzer, den eine Entscheidungstabellen-Karte früher im Workflow zurückgegeben hat. Hat die Tabelle keinen Benutzer zurückgegeben, bekommt der Benutzer auf der Karte das Dokument. Version zwei weist immer den Benutzer auf der Karte zu.

**Beispiel: Genehmiger aus der Tabelle, Ersatz auf der Karte** · [0:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-user/v1/de.mp4#t=40.916)

Zum Beispiel gibt eine Entscheidungstabelle den Genehmiger für den Rechnungsbetrag zurück, und die Zuweisungskarte nutzt ihn. Findet die Tabelle niemanden, bekommt Alex Example die Rechnung.

</details>

## **Zweck:**

Die Workflow-Karte **"Assign Document to User"** ermöglicht es Benutzern, ein Dokument einem bestimmten Benutzer zuzuweisen, und sorgt so für ein reibungsloses Workflow-Management, indem Dokumente an die passende Person weitergeleitet werden. Version 3 fügt die Möglichkeit hinzu, einen Entscheidungsbaum zu verwenden, um die Benutzerzuweisung dynamisch auf Basis verfügbarer Bedingungen zu bestimmen.

## **Bestandteile der Karte:**

1. **Benutzer**
   * **Beschreibung:** Gibt den Benutzer an, dem das Dokument zugewiesen wird.
   * **Detail:** Zur Auswahl wird eine Dropdown-Liste aller verfügbaren Benutzer bereitgestellt. Dem ausgewählten Benutzer wird das Dokument zur weiteren Bearbeitung zugewiesen.

## **Zusätzliche Komponenten in Version 3:**

1. **Entscheidungsbaum verwenden**
   * **Beschreibung:** Ist diese Option aktiviert, verwendet die Karte einen Entscheidungsbaum, um die Benutzerzuweisung dynamisch zu bestimmen.
   * **Optionen:**
     * **True:** Verwendet den Entscheidungsbaum für die dynamische Benutzerzuweisung.
     * **False:** Weist das Dokument dem ausgewählten Benutzer ohne Verwendung des Entscheidungsbaums zu.

## **Funktionalität:**

* **Bedingungsauswertung:**\
  Die Karte führt ihre Aktion nur aus, wenn sowohl der **„Wenn“**- als auch der **„Und“**-Abschnitt als erfüllt ausgewertet werden.
* **Dokumentzuweisung:**\
  Die Karte weist das Dokument dem ausgewählten Benutzer zu und stellt so sicher, dass die Aufgabe an die passende Person zur Bearbeitung weitergeleitet wird. Dies unterstützt die Nachvollziehbarkeit und ein effektives Dokumentenmanagement.
* **Entscheidungsbaum (Version 3):**\
  Ist der Entscheidungsbaum aktiviert, wertet die Karte die innerhalb des Baums definierten Bedingungen aus, um den Benutzer für die Dokumentzuweisung dynamisch auszuwählen.

## **Einrichtung und Konfiguration:**

* **Benutzer auswählen:**\
  Wählen Sie aus der Dropdown-Liste den **Benutzer**, dem das Dokument zugewiesen wird.
* **Entscheidungsbaum verwenden (Version 3):**\
  Aktivieren oder deaktivieren Sie die Verwendung des Entscheidungsbaums zur dynamischen Auswahl des Benutzers.

## **Fazit:**

Die Workflow-Karte **"Assign Document to User"** ermöglicht eine effiziente Weiterleitung von Dokumenten, indem sie sie dem ausgewählten Benutzer zuweist, mit der zusätzlichen Flexibilität in Version 3, den Benutzer mithilfe eines Entscheidungsbaums dynamisch zu bestimmen. Dies sorgt für einen anpassungsfähigeren und effizienteren Workflow-Prozess.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Verwendungszweck:** Senden Sie Rechnungen, die eine manuelle Prüfung erfordern, an eine verantwortliche Person.

**Konfiguration:** Wählen Sie den konfigurierten Benutzer `Demo Reviewer A`.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Dokument ist diesem Benutzer zugewiesen. Bestätigen Sie die resultierende Dokumentenzuordnung; Diese Karte allein erstellt keine separate Überprüfungsaufgabe.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.
