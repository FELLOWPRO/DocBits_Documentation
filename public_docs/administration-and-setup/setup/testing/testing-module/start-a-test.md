# Test starten

Ein Test ist ein Template plus eine Eingabe. Das Testing-Modul führt ihn aus und steuert ihn; Sie wählen, wie er startet.
Die drei Wege sind gleichwertig, und jeder Lauf landet in den [Protokollen](logs.md).

| Weg | Wann | In den Protokollen als |
|---|---|---|
| **Im Browser** | Sie wollen eine Prüfung jetzt ausführen und zusehen. | **Seite** |
| **KI-Assistent (MCP)** | Sie arbeiten mit einem an DocBits angebundenen KI-Assistenten, der Prüfungen starten und auswerten soll. | **MCP-Agent** |
| **Von außen (Playwright oder REST)** | Ihre Testautomatisierung oder CI-Pipeline startet Prüfungen, etwa nach einem Deployment. | **Playwright** |

In jedem Fall wird in einem **DocBits-Browser-Tab eines Organisations-Admins** geklickt, mit dessen Rechten. Der Tab muss
offen bleiben; Neuladen oder Schließen beendet den Lauf. Einzige Ausnahme ist ein Schritt **Seite neu laden** des Tests selbst
(siehe [Neu laden und fortsetzen](reload-and-resume.md)).

## Im Browser starten

1. Öffnen Sie **Einstellungen → Testing**, Reiter **Eingaben**.
2. Wählen Sie **Start** bei der Eingabe (oder öffnen Sie die Eingabe und wählen Sie **Start**).
3. Ändert das Template Daten, fragt DocBits: *Dieses Template schreibt Daten. Start bestätigen.* Wählen Sie **Start**, um fortzufahren.
4. Der Test läuft in diesem Tab. Auf der Seite Testing zeigt der Bereich **Laufender Test** Status, **Aktuelle Aktion**,
   Fortschritt sowie **Pausieren**, **Fortsetzen** und **Stoppen**. Öffnet der Test eine andere Seite, zeigt dort eine kleine
   Anzeige unten rechts den Fortschritt. Ist der Test fertig, zeigt die Anzeige das Ergebnis mit **Protokoll öffnen**
   und **Ausblenden**.
5. Ist der Test fertig, lesen Sie das Ergebnis im Reiter **Protokolle**.

<figure><img src="../../../../.gitbook/assets/testing-12-confirm-writes-de.png" alt="Rückfrage vor einem Test, der Daten schreibt"><figcaption><p>Rückfrage vor einem Test, der Daten schreibt.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/testing-13-live-run-de.png" alt="Bereich Laufender Test nach einem bestandenen Lauf"><figcaption><p>Bereich Laufender Test nach einem bestandenen Lauf.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/testing-14-run-indicator-de.png" alt="Laufanzeige unten rechts auf einer anderen Seite"><figcaption><p>Laufanzeige unten rechts auf einer anderen Seite.</p></figcaption></figure>

{% hint style="info" %}
**Uploads während eines Tests:** Hat Ihre Organisation Unterorganisationen und zeigt das Dashboard alle an, fragt der Upload-Dialog
normalerweise, zu welcher Unterorganisation das Dokument gehört. Während ein Test läuft, geht der Upload ohne Rückfrage an die **erste
Unterorganisation, die der Dialog anbietet**. Um in eine bestimmte Unterorganisation hochzuladen, starten Sie den Test aus der Ansicht
dieser Unterorganisation.
{% endhint %}

## Start von außen erlauben

Ein KI-Assistent oder ein Playwright-Skript kann nicht selbst klicken; es bittet DocBits, einen Test **in einem von Ihnen
registrierten Browser-Tab** auszuführen:

1. Öffnen Sie **Einstellungen → Testing**, Reiter **Eingaben**, in dem Browser-Tab, der die Tests ausführen soll.
2. Schalten Sie **Start von außen erlauben** ein. Der Tab nimmt jetzt Starts an und zeigt seine Sitzungs-ID.
3. Lassen Sie den Tab offen. Die Registrierung endet, wenn der Tab neu geladen oder geschlossen wird.

<figure><img src="../../../../.gitbook/assets/testing-15-remote-start-de.png" alt="Start von außen erlauben eingeschaltet, mit Sitzungs-ID"><figcaption><p>Start von außen erlauben eingeschaltet, mit Sitzungs-ID.</p></figcaption></figure>

Der Eingabe-Editor erinnert unter **Von außen starten:** an die drei Wege **Diese Seite**, **MCP-Agent** und **Playwright oder REST**.

<figure><img src="../../../../.gitbook/assets/testing-16-start-from-outside-de.png" alt="Zeile Von außen starten im Eingabe-Editor"><figcaption><p>Zeile Von außen starten im Eingabe-Editor.</p></figcaption></figure>

## Einen Start-Link teilen

Ein Start-Link öffnet den bereits ausgefüllten Startdialog eines Templates. Andere Personen oder eine CI-Pipeline müssen das Template und seine Werte so nicht erneut auswählen:

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

| Teil | Was er bewirkt |
|---|---|
| **run** | Schlüssel des Templates, das geöffnet wird (die Zeile unter dem Template-Namen im Dialog, zum Beispiel `default-smoke-analytics`). Erforderlich. |
| **version** | Öffnet diese gespeicherte Version. Ohne diese Angabe wird die neueste Version geöffnet. |
| **input** | Füllt eine gespeicherte Eingabe anhand ihres Namens oder ihrer ID aus. Als vertraulich gekennzeichnete Parameter werden niemals ausgefüllt. |
| **autostart=1** | Startet den Test, sobald die Seite geöffnet ist, aber nur, wenn das Template ausschließlich Daten liest. Ein Template, das Daten schreibt, wartet weiterhin auf die Bestätigung. |

Um den Link zu erhalten, öffnen Sie den Startdialog eines Templates und wechseln Sie zu **Von außen starten**. Der Bereich **Start-Link** enthält den Link dieses Templates. Unter **Playwright mit Start-Link** finden Sie ein Codebeispiel, das den Link öffnet und auf das Ergebnis wartet.

<figure><img src="../../../../.gitbook/assets/testing-start-link-dialog-de.png" alt="Startdialog in der Ansicht Von außen starten mit kopierbarem Start-Link und einem Playwright-Beispiel"><figcaption><p>Der Startdialog in der Ansicht <strong>Von außen starten</strong>: der kopierbare Start-Link und ein Playwright-Beispiel, das ihn öffnet. Sobald ein Tab Starts von außen annimmt, erscheint eine Sitzung unter <strong>Sitzung, die den Test ausführt</strong>.</p></figcaption></figure>

Beim Öffnen des Links gilt Folgendes:

* DocBits öffnet **Einstellungen → Testing**, Reiter **Templates**, mit dem Startdialog des Templates. Der Link funktioniert nur für
  Personen, die Einstellungen → Testing öffnen können, da der Test in ihrem Browser-Tab und mit ihren Berechtigungen läuft.
* Bei unbekanntem Template, unbekannter Version oder unbekannter Eingabe erscheint unter den Reitern eine Fehlermeldung; es wird nichts gestartet.
* Mit `autostart=1` startet ein Template, das ausschließlich Daten liest, sofort. In allen anderen Fällen wartet der Test auf **Starten**.
  Bei einem Template, das Daten schreibt, ist weiterhin eine Bestätigung erforderlich.
* Nach dem Auslesen werden die Parameter aus der Adressleiste entfernt, sodass ein erneutes Laden der Seite den Test nicht ein zweites
  Mal startet.

Das **?** neben den Reitern und im Startdialog öffnet die passende Seite dieser Dokumentation in Ihrer Oberflächensprache.

## Über einen KI-Assistenten starten (MCP)

Wenn Ihr KI-Assistent mit DocBits verbunden ist (siehe die Seite [DocBits MCP](../../../../advanced-functions-and-tools/docbits-mcp/README.md)):

1. Erlauben Sie in einem Browser-Tab den Start von außen (siehe oben).
2. Bitten Sie den Assistenten zum Beispiel: *„Zeig mir meine DocBits-Testeingaben und starte ‚Rechnung LT-2026-0001 bereit zur
   Validierung' in meinem registrierten Browser-Tab. Sag mir danach das Ergebnis."*
3. Sind mehrere Tabs registriert, fragt der Assistent, welcher genutzt werden soll; vor einem Test, der Daten ändert, fragt er
   Sie um Erlaubnis. Danach liest er das Protokoll und meldet das Ergebnis.

## Mit Playwright oder einem anderen Werkzeug starten (REST)

Ihre Testautomatisierung startet eine Eingabe mit einem API-Aufruf und liest danach ihr Protokoll. Sie braucht:

* ein Token eines Organisations-Admins der Organisation;
* die ID der Eingabe;
* die Sitzungs-ID eines Browser-Tabs mit eingeschaltetem **Start von außen erlauben**.

Aufruf und Beispiel stehen auf der Seite [Für Entwickler](for-developers.md).

## Kundenumgebungen

In Sandbox und Produktion ist die Anzeige **Umgebung** rot. Tests, die Daten ändern, brauchen bei jedem Start eine
ausdrückliche Bestätigung, und Export-, Lösch- oder Freigabeschritte sind gesperrt, solange das Template nicht erklärt, dass
es Daten schreibt. Führen Sie schreibende Tests möglichst in einer Testumgebung aus.
