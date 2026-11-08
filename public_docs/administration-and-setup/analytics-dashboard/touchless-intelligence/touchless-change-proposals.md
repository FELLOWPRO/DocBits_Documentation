# Änderungsvorschläge und Berichte

<!-- touchless-admin-video-v2-20261104:start -->
**Video-Kapitel (Prüffassung):** [Vorschläge und Verlauf](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/de.html#chapter=10).
<!-- touchless-admin-video-v2-20261104:end -->

Eine Empfehlung kann mit einem **Änderungsvorschlag** kommen, einer einzelnen Einstellungsänderung, die helfen soll. Administratoren arbeiten in vier Schritten damit:

1. **Preview**: zeigt die Änderung (aktueller und vorgeschlagener Wert) und was DocBits erwartet. Nichts wird gespeichert. **Apply** ist erst möglich, nachdem Sie eine Vorschau angesehen haben.
2. **Apply**: speichert genau die in der Vorschau gezeigte Änderung. Sie wird protokolliert.
3. **Measure**: DocBits vergleicht die Touchless-Quote desselben Dokumenttyps **vorher und nachher** über gleich lange Zeiträume. In jedem Zeitraum sind mindestens **20 Dokumente** nötig, sonst heißt es _not measurable_.
4. **Undo**: nimmt die Änderung zurück, wenn dieser Vorschlag eine Rücknahme unterstützt. Prüfen Sie die Verfügbarkeit und kontrollieren Sie die wiederhergestellte Einstellung.

{% hint style="warning" %}
Ein Vorher/Nachher-Unterschied ist eine **Beobachtung**, kein Beweis für die Ursache. Gleichzeitig können sich andere Dinge ändern (ein neuer Lieferant, eine saisonale Spitze).
{% endhint %}

**Beispiel (zur Veranschaulichung).** Sie wenden _Switch on automatic PO match and export_ für Rechnungen an. Zwei Wochen später zeigt die **Change history** eine AP-Touchless-Quote von vorher 52 % (210 Dokumente) und nachher 61 % (198 Dokumente). Das sind +9 pp, mit genügend Dokumenten für eine Messung. Die gemessene Quote umfasst Pure- und reine Freigabedokumente; sie misst keine Auslesegenauigkeit. Eine Quelldatenkorrektur in Infor prüfen Sie zusätzlich am importierten Datenbestand und an späteren Rechnungen; gehen Sie nicht davon aus, dass sie eine DocBits-Einstellungsänderung ist oder automatisch in dieser Historie erscheint.

Administratoren sehen außerdem zwei Abschnitte zwischen den Kennzahlen und den Diagrammen:

* **Improvement requests**: Vorschläge, die Benutzer aus dem Validierungsassistenten gesendet haben, in zwei Tabs **Open** und **History**.
* **Learned rule proposals**: Regeln, die DocBits aus den Korrekturen Ihres Teams gelernt hat, zum Beispiel „für Lieferant X den Wert in Feld Y ersetzen“. Prüfen Sie vor dem Anlegen die Dokumente, in denen die Regel einen Wert ersetzen würde, den Ihr Team akzeptiert hatte. Der Abschnitt **After activation** zeigt die manuellen Korrekturen des Zielfelds vor und nach dem Aktivieren einer Regel.

<figure><img src="../../../.gitbook/assets/touchless-consulting-report-de.png" alt="Der Consulting report mit den drei wichtigsten Vorschlägen, einer Rangliste und den Problemen nach Bereich"><figcaption><p>Der Consulting report: die wichtigsten Vorschläge, eine Rangliste aller Blocker mit Dokumenten und geschätzter Wirkung pro Monat sowie die Probleme nach Bereich. Beispielorganisation mit Demodaten; die Lieferantennamen sind frei erfunden.</p></figcaption></figure>

Administratoren finden den **Consulting report** unten im Tab. Klicken Sie auf **Create report**, um ihn zu laden. Er fasst für Ihre Organisation zusammen:

* die **Änderungen mit der größten Wirkung**, als Rangliste, jeweils mit Bereich, Problem, empfohlener Maßnahme, Anzahl der Dokumente und der **geschätzten** Wirkung pro Monat,
* **den Bereich jedes Problems** (Extraktion, Stammdaten, Bestellabgleich, Auto Accounting, Einstellungen, Prozess),
* **Prüfungen der Tabellenkonfiguration**, zum Beispiel _structured table output not used_ oder _table column type mismatch_ je Dokumenttyp und Spalte.

Die Wirkungswerte sind **Schätzungen**. Antwortet der Bericht mit _forbidden_, erlaubt Ihre Rolle ihn nicht.

Die zugehörigen Werkzeugaufrufe und die Einordnung menschlicher Aktionen sind unter [Touchless mit MCP](touchless-mcp.md) beschrieben.

## Weiterführende Seiten

* [Touchless Intelligence](./)
* [Lieferantendiagnose und Fehlermuster](../../touchless-supplier-diagnosis.md)
* [Bestellabgleich-Diagnose](../../touchless-po-matching-diagnosis.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
