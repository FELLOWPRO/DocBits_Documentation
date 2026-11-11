---
description: >-
  Nutzen Sie die Karte Status auf … ändern so, dass ein Statuswechsel nicht
  denselben Workflow erneut startet.
---

# Status ändern, ohne den Workflow neu zu starten

Wenn ein Dokument einen neuen Status erhält, startet DocBits die Workflows, die für diesen Status vorgesehen sind. Dazu kann auch der Workflow gehören, der den Status gerade geändert hat. Passen seine Bedingungen weiterhin, läuft er erneut und erzeugt eine zweite Aufgabe oder einen zweiten Export.

Diese Seite zeigt, wie Sie Ihren Workflow so einrichten, dass jedes Dokument ihn nur einmal durchläuft.

## Die entscheidende Einstellung

Die Karte [Status auf … ändern](../then/status/change-status-to.md) setzt den neuen Status. Ihre Einstellung **Workflows auslösen** legt fest, ob dieser Statuswechsel Workflows starten darf:

* **Falsch:** Es wird kein Workflow gestartet. Verwenden Sie diesen Wert, außer ein anderer Workflow soll mit dem Dokument weiterarbeiten.
* **Wahr:** DocBits startet die Workflows, deren Bedingungen auf das Dokument mit seinem neuen Status passen. Dazu kann auch der Workflow gehören, der die Änderung vorgenommen hat.

Die Kartenseite beschreibt alle Status und die Kartenversionen.

## Welche Workflows nach einem Statuswechsel starten

Ist **Workflows auslösen** auf **Wahr** gesetzt, prüft DocBits jeden aktiven Workflow auf seine Bedingungen zu Dokumenttyp und Status, zum Beispiel eine Karte **Dokumentstatus**. Ein Workflow startet, wenn das Dokument mit seinem neuen Status dazu passt.

Ein Workflow, der den Status nicht prüft, passt auf **jeden** Status. Ändert er den Status selbst, startet ihn der neue Status also erneut.

Setzen Sie ein Dokument auf den Status, den es bereits hat, passiert nichts: Der Status bleibt, und kein Workflow startet.

## Beispiel: ein Lauf oder zwei Läufe

Die Regel: Sobald Ihr Workflow seine Aufgabe erledigt hat, dürfen seine eigenen Bedingungen nicht mehr passen.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-de.png" alt="Zwei Workflows, beide mit Workflows auslösen auf Wahr. Links: Die Bedingung prüft Dokumenttyp ist Rechnung und Status Bereit zur Validierung. Nach dem Wechsel auf Genehmigung ausstehend passt die Bedingung nicht mehr, der Workflow startet nicht erneut, Ergebnis 1 Aufgabe. Rechts: Die Bedingung prüft nur Dokumenttyp ist Rechnung. Der neue Status startet den Workflow ein zweites Mal, er erzeugt eine zweite Aufgabe und setzt erneut Genehmigung ausstehend, was nichts ändert. Ergebnis 2 Aufgaben." width="800"><figcaption><p>Derselbe Workflow mit und ohne Statusbedingung</p></figcaption></figure>

Rechts läuft der Workflow ein zweites Mal und erzeugt eine doppelte Aufgabe. Er stoppt dort nur, weil der zweite Statuswechsel einen Status setzt, den das Dokument bereits hat.

**Zwei Workflows können sich gegenseitig starten.** Setzt ein Workflow **Genehmigung ausstehend** und ein anderer das Dokument zurück auf **Bereit zur Validierung**, beide mit **Wahr**, starten sie sich immer wieder gegenseitig. Geben Sie jedem Workflow eine Bedingung auf den Status, von dem er ausgeht, und verwenden Sie **Wahr** nur dort, wo es nötig ist.

## Schritt für Schritt einrichten

1. **Verwenden Sie Version 3 von Status auf … ändern.** Ältere Versionen haben keine Einstellung **Workflows auslösen** (siehe [Kartenversionen](../then/status/change-status-to.md#kartenversionen)).
2. **Prüfen Sie den Ausgangsstatus.** Fügen Sie die **Und**-Karte **Dokumentstatus** hinzu (unter **Und → Status**) und stellen Sie sie auf **Ist** **Bereit zur Validierung**. Siehe [Statusbedingung für ein einzelnes Dokument](../and/status/single-document-status-condition.md). Wenn der Status allein nicht zeigt, ob der Schritt erledigt ist, prüfen Sie zusätzlich ein Feld, das Ihr Workflow nach getaner Arbeit füllt.
3. **Fügen Sie die Aktion hinzu**, zum Beispiel das Erstellen einer Aufgabe oder den Export des Dokuments.
4. **Fügen Sie Status auf … ändern hinzu** und wählen Sie den nächsten Status, zum Beispiel **Genehmigung ausstehend**.
5. **Wählen Sie Workflows auslösen.** Beginnen Sie mit **Falsch**. Wählen Sie **Wahr** nur, wenn ein anderer Workflow mit dem neuen Status weiterarbeiten soll.
6. **Testen Sie mit einem echten Dokument.** Prüfen Sie, dass genau eine Aufgabe oder ein Export entstanden ist und das Dokument den neuen Status hat.

{% hint style="info" %}
Tests im Workflow-Designer simulieren den Statuswechsel nur. Der Status wird nicht gespeichert, und kein anderer Workflow startet. Um das tatsächliche Verhalten zu sehen, verwenden Sie ein echtes Dokument.
{% endhint %}

## Eingebauter Schutz

DocBits begrenzt den Schaden, wenn sich Workflows immer wieder gegenseitig starten:

* **Pro Dokument läuft immer nur ein Workflow-Lauf.** Läufe für dasselbe Dokument warten aufeinander, und jeder Lauf sieht das Dokument so, wie der vorherige es hinterlassen hat.
* **Laufgrenze.** Standardmäßig läuft derselbe Workflow höchstens 50-mal für ein Dokument. Danach startet DocBits ihn für dieses Dokument nicht mehr.

Diese Grenzen beenden die Wiederholung irgendwann, aber bis dahin können bereits viele Aufgaben oder Exporte entstanden sein. Verhindert wird sie durch eine Bedingung auf den Status. Wenn ein Duplikat ein echtes Problem wäre, prüfen Sie zusätzlich vor der Aktion darauf, zum Beispiel ob für das Dokument bereits eine offene Aufgabe existiert.

## Verwandte Seiten

* [Status auf … ändern](../then/status/change-status-to.md): die Karte, ihre Status und Versionen
* [Statusbedingung für ein einzelnes Dokument](../and/status/single-document-status-condition.md): den Dokumentstatus in einer Bedingung prüfen
* [Wann läuft mein Workflow?](../workflow-execution-model.md)
* [Übersicht über den Lernweg](../workflow-learning-path.md)
