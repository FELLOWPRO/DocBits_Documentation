# Dashboard

Das **Workflow-Dashboard** ist die Startseite des Workflow-Bereichs. Es zeigt, wie Ihre Workflows laufen – Ausführungssummen, Erfolgs- und Ausfallrate, ein Diagramm der Ausführungen im Zeitverlauf und die letzte Aktivität – und bietet Zugriff auf die Workflow-Liste, den Testmanager und das Card SDK.

Die folgenden Teilansichten zeigen die Mengenkennzahlen, die Laufergebnisse und das Diagramm der Ausführungen. Letzte Aktivität und Bedienelemente liegen außerhalb dieser Ausschnitte.

<figure><img src="../../.gitbook/assets/workflow-kpi-volume-de-20261112.png" alt="Mengenkennzahlen: heute ausgeführte Workflows, erstellte Workflows und Gesamtläufe"><figcaption><p>Mengenkennzahlen: <strong>Heute ausgeführter Workflow</strong>, <strong>Erstellte Workflows</strong> und <strong>Gesamtläufe</strong>, hier für die letzten 31 Tage.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/workflow-kpi-outcomes-de-20261112.png" alt="Laufergebnisse: erfolgreiche Läufe, Erfolgsquote und Ausfallrate"><figcaption><p>Laufergebnisse: <strong>Erfolgreiche Läufe</strong>, <strong>Erfolgsquote</strong> und <strong>Ausfallrate</strong>, jeweils mit Bezug auf die Gesamtläufe. Über der Quote steht eine farbige Marke, im Beispiel <strong>KRITISCH</strong> beziehungsweise <strong>GESUND</strong>.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/workflow-chart-de-20261112.png" alt="Workflow-Ausführungen über die angezeigten sieben Monate"><figcaption><p><strong>Workflow-Ausführungen</strong> über die angezeigten Monate Mai bis November, mit den Reihen <strong>Erfolg</strong> und <strong>Fehlgeschlagen</strong>.</p></figcaption></figure>

## Reiter

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.mp4" %}

**Video:** Suchen und Filtern im Workflow-Dashboard · 0:52 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Nach Namen suchen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.mp4#t=0.25)

In der Workflow-Liste findet das Suchfeld Workflows nach ihrem Namen. Tippen Sie einen Teil des Namens ein, und nur die passenden Workflows bleiben in der Liste.

**Suche leeren** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.mp4#t=10.383)

Leeren Sie die Suche, um wieder alle Workflows zu sehen. Die Suche steht auch in der Seitenadresse, sodass sie beim Zurückgehen zur Liste erhalten bleibt.

**Zeitraum und Workflow** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.mp4#t=20.75)

Auf dem Tab Dashboard bestimmen die Filter oben, was die Zahlen und das Diagramm zählen: ein Start- und ein Enddatum, standardmäßig der letzte Monat, und alle Workflows oder ein einzelner.

**Zwei Zeiträume vergleichen** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/de.mp4#t=33.516)

Vergleichen fügt einen zweiten Zeitraum hinzu: Geben Sie dessen Start- und Enddatum ein. Jede Zahl zeigt dann auch den Wert dieses Zeitraums und die Differenz. Die Filter merkt sich dieser Browser für Ihren nächsten Besuch.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4" %}

**Video:** Einen Workflow als JSON herunterladen und hochladen · 0:55 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Als JSON herunterladen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4#t=0.25)

Um eine Kopie eines Workflows zu behalten, öffnen Sie seine Aktionen in der Liste und wählen Herunterladen. Sie erhalten eine JSON-Datei mit seinem Namen, seinem Typ und allen Karten und Verbindungen.

**Sichern oder übertragen** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4#t=13.416)

Nutzen Sie sie als Sicherung, oder um einen Workflow zu übertragen, den Sie in einer Testumgebung gebaut und getestet haben.

**Workflow importieren** · [0:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4#t=22.35)

Um ihn zurückzuholen, klicken Sie auf Workflow importieren und wählen die JSON-Dateien, bis zu zehn auf einmal.

**Kommt ausgeschaltet an** · [0:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4#t=31.35)

Ein hochgeladener Workflow kommt ausgeschaltet an, damit nichts läuft, bevor Sie ihn angesehen haben.

**Benutzer, Gruppen und Tabellen prüfen** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/de.mp4#t=38.35)

Karten mit Benutzern, Gruppen, Unterorganisationen oder Entscheidungstabellen verweisen über eine interne ID darauf. Öffnen Sie nach einem Upload aus einer anderen Umgebung die Karten und prüfen Sie, ob sie noch so eingestellt sind, wie Sie es möchten. Testen Sie ihn dann und schalten Sie ihn ein.

</details>

- **Dashboard** — Kennzahlen zu den Ausführungen und letzte Aktivität (oben dargestellt).
- **Workflow-Liste** — jeder Workflow mit Typ, Workflow-Ausführungsreihenfolge und Auslöser. Einen neuen Workflow legen Sie mit **Neuer Workflow** an.
- **Testmanagerliste** — Testszenarien, die Ihre Workflows validieren; führen Sie sie mit **Alle Tests ausführen** aus.
- **Lizenz** — Informationen zur Workflow-Lizenzierung.
- **Card SDK** — eigene Workflow-Karten erstellen und hochladen (siehe [Card SDK](card-sdk.md)).

Die Symbolleiste bietet außerdem **Vorlagen**, das die Bibliothek [Workflow-Vorlagen](standard-workflow-builder.md#workflow-vorlagen) öffnet, und **Workflow importieren**, das einen Workflow aus einer JSON-Datei importiert.

Mit dem **Testmanager** können Sie Testszenarien pro Workflow speichern und gemeinsam ausführen, um zu bestätigen, dass Ihre Workflows sich nach Änderungen weiterhin korrekt verhalten:

<figure><img src="../../.gitbook/assets/s50-workflow_test_manager-de.png" alt="Deutsche Testmanagerliste mit Alle Tests ausführen und Testszenario hinzufügen. Szenariodaten sind ausgeblendet; Actions bleibt ein Produktbegriff."><figcaption><p>Deutsche Testmanagerliste mit Alle Tests ausführen und Testszenario hinzufügen. Szenariodaten sind ausgeblendet; Actions bleibt ein Produktbegriff.</p></figcaption></figure>

## Nächste Schritte

- Erstellen Sie mit dem Builder **Standard-Workflow** eine lineare Automatisierung.
- Erstellen Sie mit dem Builder **Erweiterter Workflow** einen verzweigten Ablauf.
