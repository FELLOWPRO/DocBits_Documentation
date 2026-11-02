# DocBits Release-Lebenszyklus-Strategie

Mit dem Rollout des kommenden Minor-Releases R1.1 führt DocBits eine neue Release-Lebenszyklus-Strategie auf Basis von zwei Release-Kanälen ein: VESTA und NOVA.

**NOVA** ist der Kanal für die Einführung neuer Major- und Minor-Releases, wie **Rx** und **Rx.y**. **VESTA** stellt weiterhin das bestehende Produktions-Release bereit.

{% hint style="success" %}
**Wichtig: Eine URL für VESTA und NOVA**

Verwenden Sie weiterhin Ihre gewohnte DocBits-Anwendungs-URL. VESTA und NOVA haben keine separaten Zugriffs-URLs: Beide Release-Kanäle sind über dieselbe Standard-URL erreichbar, die Sie bereits für die jeweilige Umgebung nutzen.

Um den Kanal zu wechseln, gehen Sie zu **Settings > Company Information > Release Channel** und wählen Sie **VESTA** oder **NOVA**. Sie müssen sich nicht ab- und wieder anmelden. Ihr nächster Klick in der Anwendung führt Sie automatisch zum Release des ausgewählten Kanals.

Prüfen Sie vor dem Wechsel, ob beide Kanäle in Ihrer Umgebung bereit und verfügbar sind, wie unter [Umgebungsverfügbarkeit vor dem Wechsel prüfen](#wichtig-umgebungsverfügbarkeit-vor-dem-wechsel-prüfen) erläutert.
{% endhint %}

## Release-Kanäle

| Kanal | Rolle im Lebenszyklus |
| --- | --- |
| **VESTA** | Stellt das aktuelle Produktions-Release bereit. |
| **NOVA** | Stellt das nächste Release bereit, während es Entwicklung, Tests und Produktionsverfügbarkeit durchläuft. Während der parallelen Produktion bieten NOVA und VESTA beide produktive Live-Releases an. |

## Überblick über den Lebenszyklus

![Dreiphasiger Release-Lebenszyklus von DocBits VESTA und NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Jeder Zyklus besteht aus drei Phasen. Ein von FELLOWPRO gesteuerter Rollover überführt anschließend das NOVA-Produktions-Release in VESTA und startet den nächsten Zyklus.

| Phase | VESTA | NOVA | Was dies für Ihre Organisation bedeutet |
| --- | --- | --- | --- |
| **1. Entwicklung** | R1.0.x in Produktion | R1.1 in Entwicklung | Nutzen Sie weiterhin VESTA, während das nächste Release vorbereitet wird. |
| **2. QA und Abnahmetests** | R1.0.x in Produktion | R1.1 in QA und UAT | Evaluieren Sie das kommende Release in der NOVA-Sandbox, während die produktive Arbeit auf VESTA weiterläuft. |
| **3. Parallele Produktion** | R1.0.x in Produktion | R1.1.x in Produktion | Bleiben Sie auf VESTA oder wechseln Sie eigenständig zu NOVA, sobald Sie bereit sind. |

Nach dem Rollover nutzen alle Kunden VESTA R1.1.x, und NOVA wird für die Entwicklung von R1.2 neu aufgesetzt. Phase 1 beginnt mit diesen aktualisierten Versionen erneut.

### Phase 1 — Entwicklung

VESTA stellt das aktuelle Produktions-Release R1.0.x bereit, während das nächste Release, R1.1, in NOVA entwickelt wird. Ihre Organisation setzt ihre tägliche Arbeit während dieser gesamten Phase auf VESTA fort.

### Phase 2 — QA und Abnahmetests

Das kommende NOVA-Release durchläuft die Qualitätssicherung (QA) und die Benutzerabnahmetests (UAT). Sie können es in der NOVA-Sandbox evaluieren, um zu beurteilen, wie sich die Änderungen in die Arbeitsabläufe Ihrer Organisation einfügen, und die Einführung vorzubereiten.

VESTA R1.0.x bleibt in dieser Phase das Produktions-Release. Sie können für den produktiven Einsatz zu NOVA wechseln, sobald es in Phase 3 verfügbar ist.

### Phase 3 — Parallele Produktion

VESTA R1.0.x und NOVA R1.1.x sind beide produktive Live-Releases. Ihre Organisation entscheidet auf Grundlage Ihrer Anforderungen und der Ergebnisse Ihrer Sandbox-Evaluierung, ob und wann sie zu NOVA wechselt.

So führen Sie NOVA in dieser Phase ein:

1. Evaluieren Sie das Release in der NOVA-Sandbox.
2. Prüfen Sie die Release-Ankündigung oder bestätigen Sie mit dem FELLOWPRO Support, dass beide Produktionsumgebungen bereit und für einen Wechsel verfügbar sind.
3. Entscheiden Sie, wann Ihre Organisation bereit ist, das neue Release produktiv zu nutzen.
4. Gehen Sie in DocBits zu **Settings > Company Information > Release Channel** und wählen Sie **NOVA**.

Während der parallelen Produktion können Sie auch wieder zu VESTA zurückwechseln, indem Sie zu **Settings > Company Information > Release Channel** gehen und **VESTA** auswählen.

Der Kanalwechsel erfolgt per Self-Service. FELLOWPRO legt nicht fest, welche Kunden zu NOVA wechseln sollen. Sie können VESTA während der gesamten parallelen Produktion weiter nutzen und das neue Release mit dem darauffolgenden Rollover übernehmen.

## Release-Rollover und der nächste Zyklus

FELLOWPRO führt den Rollover durch, sobald das NOVA-Release bereit ist, zum gemeinsamen Produktions-Release zu werden, und die Zustimmung aller Kunden zum geplanten Übergang vorliegt:

**NOVA R1.1.x → VESTA R1.1.x**

### Vorankündigung und Zustimmung der Kunden

FELLOWPRO kündigt den geplanten Rollover allen Kunden vorab per E-Mail an und holt deren Zustimmung zum Übergang ein. Sie sind eingeladen, sich mit etwaigen Bedenken oder Einwänden an FELLOWPRO zu wenden, damit diese vor dem Rollover besprochen werden können. Der Rollover und das Neuaufsetzen von NOVA erfolgen erst, wenn das Release bereit ist und alle Kunden dem geplanten Übergang zugestimmt haben.

### Was sich beim Rollover ändert

| Änderung | Ergebnis |
| --- | --- |
| **Das NOVA-Release wird zum VESTA-Release** | R1.1.x wird zum gemeinsamen Produktions-Release in VESTA für alle Kunden. |
| **Das vorherige Release wird abgekündigt** | R1.0.x wird außer Betrieb genommen und ist weder über einen der beiden Kanäle noch auf anderem Wege weiterhin verfügbar. |
| **NOVA wird für das nächste Release neu aufgesetzt** | Die Entwicklung von R1.2 beginnt in NOVA und startet damit Phase 1 des nächsten Zyklus. |

Anschließend wiederholen sich dieselben drei Phasen mit den neuen Versionsnummern.

Das folgende Diagramm veranschaulicht den oben beschriebenen Release-Zyklus im Detail.

![Detaillierter Release-Zyklus von DocBits VESTA und NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Release-Rhythmus

Der geplante Rhythmus unterscheidet sich zwischen Major- und Minor-Releases, die über NOVA eingeführt werden, und Hotfixes, die auf die Produktions-Releases in VESTA und NOVA angewendet werden.

#### Major- und Minor-Releases über NOVA

FELLOWPRO plant derzeit mit einem Zyklus von etwa **3–4 Monaten für Major- und Minor-Releases**, die über den Release-Kanal NOVA eingeführt werden, wie **Rx** und **Rx.y**. Diese Schätzung gilt für den oben beschriebenen Release-Lebenszyklus, einschließlich des anschließenden Rollovers in VESTA und des Neuaufsetzens von NOVA für das nächste Release. Sie beschreibt nicht die Häufigkeit von Hotfixes.

Dieser Zeitraum spiegelt unsere aktuelle Planungsschätzung wider; er ist weder ein fester Zeitplan noch eine maximale Zyklusdauer noch eine Garantie für einen Release- oder Rollover-Termin. Der Zeitpunkt jedes Rollovers und des Neuaufsetzens von NOVA hängt sowohl von der **Release-Reife als auch von der Zustimmung aller Kunden zum geplanten Übergang** ab. Wird zusätzliche Zeit benötigt, um die Release-Reife zu erreichen, Bedenken von Kunden zu klären oder die Zustimmung jedes einzelnen Kunden einzuholen, verlängert sich der Zyklus und kann länger als vier Monate dauern.

FELLOWPRO kündigt jeden geplanten Rollover vorab an. Jede indikative Zeitangabe steht unter dem Vorbehalt, dass diese Bedingungen erfüllt sind.

#### Hotfixes in der VESTA-Produktion

Hotfixes für das VESTA-Produktions-Release werden voraussichtlich etwa **einmal im Monat oder in etwas längeren Abständen** bereitgestellt. Dies ist ein indikativer Rhythmus und kein fester Zeitplan und keine garantierte Liefertermin-Zusage.

#### Stabilisierungs-Hotfixes in der NOVA-Produktion

Für Stabilisierungs-Hotfixes in der NOVA-Produktion lässt sich kein allgemeiner Rhythmus angeben. NOVA führt völlig neue Releases ein, daher hängen Zeitpunkt und Häufigkeit dieser Hotfixes vom Stabilisierungsbedarf des jeweiligen Releases ab. Sie folgen daher weder dem indikativen monatlichen Rhythmus für VESTA noch dem 3–4-Monats-Zyklus für Major- und Minor-Releases.

## Verantwortlichkeiten und Wahlmöglichkeiten der Kunden

| Übergang | Verantwortlich | Was Sie erwartet |
| --- | --- | --- |
| **Wechsel zwischen VESTA und NOVA während Phase 3** | Ihre Organisation | Evaluieren Sie NOVA in der Sandbox und entscheiden Sie, ob und wann Sie wechseln. Verwenden Sie **Settings > Company Information > Release Channel**, um während der parallelen Produktion NOVA auszuwählen oder zu VESTA zurückzukehren. |
| **Rollover von NOVA R1.1.x in VESTA R1.1.x** | FELLOWPRO | Prüfen Sie die Vorankündigung per E-Mail, äußern Sie etwaige Bedenken oder Einwände und bestätigen Sie Ihre Zustimmung zum geplanten Übergang. FELLOWPRO führt den Rollover durch, sobald das Release bereit ist und alle Kunden zugestimmt haben. |

## Wichtig: Umgebungsverfügbarkeit vor dem Wechsel prüfen

Wechseln Sie nur dann über **Settings > Company Information > Release Channel** zwischen VESTA und NOVA, wenn die Releases parallel verfügbar und in der **entsprechenden Umgebung auf beiden Kanälen** einsatzbereit sind. Die Verfügbarkeit in Sandbox und Produktion muss separat beurteilt werden:

- **Sandbox:** Sie können von VESTA Sandbox zu NOVA Sandbox wechseln, sobald das neue Release in NOVA Sandbox bereit und verfügbar ist und VESTA Sandbox weiterhin verfügbar bleibt. Dieselbe Voraussetzung gilt für den Wechsel zurück.
- **Produktion:** Sie können nur dann zwischen VESTA Production und NOVA Production wechseln, solange beide Produktions-Releases parallel bereit und verfügbar sind. Die Verfügbarkeit in NOVA Sandbox bedeutet nicht, dass NOVA Production einsatzbereit ist.

Ein Wechsel, wenn die entsprechende Umgebung nicht bereit oder verfügbar ist, kann Ihren Betrieb beeinträchtigen. FELLOWPRO versendet Release-Ankündigungs-E-Mails einige Tage, bevor Releases in der Sandbox oder in der Produktion verfügbar werden. Prüfen Sie diese Ankündigungen vor dem Wechsel. Wenn Sie unsicher sind, ob ein Wechsel für Ihre Organisation verfügbar oder angemessen ist, wenden Sie sich zur Bestätigung an den FELLOWPRO Support.

**Geplante Verfügbarkeitssteuerung:** FELLOWPRO arbeitet an einer Ja/Nein-Steuerung, mit der der Support die Einstellung Release Channel schreibgeschützt setzen oder den Kanalwechsel unabhängig von einem Software-Deployment aktivieren kann. Sobald diese Steuerung verfügbar ist, nutzt der Support sie, um den Wechsel zu aktivieren, wenn die entsprechenden Umgebungen bereit sind, und die Einstellung andernfalls schreibgeschützt zu halten. Dadurch sollen Kunden sicher zwischen VESTA und NOVA wechseln können, wenn die Einstellung aktiviert ist. Bis diese Steuerung eingeführt ist, sollte eine bearbeitbare Einstellung allein nicht als Bestätigung dafür gewertet werden, dass ein Wechsel angemessen ist; folgen Sie den Release-Ankündigungen oder holen Sie eine Bestätigung beim Support ein.

## Häufig gestellte Fragen

### Woher wissen wir, ob ein Wechsel zwischen VESTA und NOVA sicher ist?

Prüfen Sie die Release-Ankündigung für die Umgebung, die Sie nutzen möchten, oder bitten Sie den FELLOWPRO Support zu bestätigen, dass ein Wechsel angemessen ist. Beide entsprechenden Umgebungen müssen parallel bereit und verfügbar sein; die Sandbox-Reife bestätigt nicht die Produktionsreife. Die vollständigen Hinweise, einschließlich der geplanten Steuerung zum Aktivieren oder Deaktivieren des Kanalwechsels, finden Sie oben unter [Wichtig: Umgebungsverfügbarkeit vor dem Wechsel prüfen](#wichtig-umgebungsverfügbarkeit-vor-dem-wechsel-prüfen).

### Können wir auf VESTA bleiben, während NOVA produktiv verfügbar ist?

Ja. Während Phase 3 können Sie auf VESTA bleiben oder zu NOVA wechseln, sobald Ihre Organisation bereit ist. Beim darauffolgenden Rollover wird das neue Release zu VESTA, und das vorherige Release wird abgekündigt.

### Wie wechseln wir zu NOVA oder zurück zu VESTA?

Prüfen Sie zunächst, ob die entsprechende Umgebung auf beiden Kanälen bereit und verfügbar ist, wie unter [Umgebungsverfügbarkeit vor dem Wechsel prüfen](#wichtig-umgebungsverfügbarkeit-vor-dem-wechsel-prüfen) erläutert. Die Verfügbarkeit in Sandbox und Produktion ist getrennt zu betrachten.

Gehen Sie während Phase 3 in DocBits zu **Settings > Company Information > Release Channel** und wählen Sie **NOVA**, um das neue Produktions-Release zu übernehmen, oder **VESTA**, um zum aktuellen VESTA-Produktions-Release zurückzukehren. Ihre Organisation trifft diese Entscheidung eigenständig, basierend auf ihren Anforderungen und der Evaluierung von NOVA in der Sandbox. Diese Wahl gilt, solange beide Releases parallel verfügbar sind; das vorherige VESTA-Release wird beim Rollover abgekündigt.

### Wann ist NOVA für den produktiven Einsatz verfügbar?

NOVA wird in Phase 3, nach Entwicklung und QA/UAT, zu einem produktiven Live-Release. In dieser Phase laufen VESTA und NOVA mit unterschiedlichen Softwareversionen parallel in Produktion.

### Wie erfahren wir vom Rollover, und können wir Einwände erheben?

FELLOWPRO informiert alle Kunden vorab per E-Mail und holt deren Zustimmung zum geplanten Übergang ein. Sie sind eingeladen, etwaige Bedenken oder Einwände gegenüber FELLOWPRO zu äußern. Der Rollover und das Neuaufsetzen von NOVA erfolgen erst, wenn das Release bereit ist und die Zustimmung aller Kunden vorliegt.

### Können wir R1.0.x nach dem Rollover weiter nutzen?

Nein. R1.0.x wird beim Rollover außer Betrieb genommen und ist weder über einen der beiden Kanäle noch auf anderem Wege weiterhin verfügbar. R1.1.x wird zum gemeinsamen VESTA-Produktions-Release für alle Kunden.

### Worin unterscheidet sich der Rollover von unserem Wechsel zu NOVA?

Ihr Wechsel zu NOVA während Phase 3 ist eine Self-Service-Entscheidung darüber, wann Sie das neue Produktions-Release übernehmen. Der Rollover ist der darauffolgende, von FELLOWPRO gesteuerte Übergang: NOVA R1.1.x wird zu VESTA R1.1.x, das vorherige Release wird abgekündigt, und der nächste Zyklus beginnt.

### Was passiert mit NOVA nach dem Rollover?

NOVA wird für die Entwicklung des nächsten Release neu aufgesetzt, in diesem Beispiel R1.2. VESTA stellt R1.1.x bereit, während NOVA erneut Entwicklung, QA/UAT und parallele Produktion durchläuft.

### Ist alle drei bis vier Monate ein Major- oder Minor-Release garantiert?

Nein. Der Rhythmus von etwa 3–4 Monaten für Major- und Minor-Releases, die über NOVA eingeführt werden, ist eine aktuelle Planungsschätzung, kein garantierter Zeitplan und keine maximale Dauer. Rollover und Neuaufsetzen von NOVA setzen sowohl die Release-Reife als auch die Zustimmung aller Kunden voraus. Erfordert eine dieser Bedingungen mehr Zeit, verlängert sich der Zyklus und kann vier Monate überschreiten. FELLOWPRO kündigt jeden geplanten Rollover vorab an.
