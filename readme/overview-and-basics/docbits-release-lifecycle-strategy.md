# DocBits Release-Lebenszyklus-Strategie

DocBits verwendet zwei Release-Kanäle, **VESTA** und **NOVA**, um neue Releases einzuführen und Ihrer Organisation Zeit zu geben, diese vor der Einführung zu evaluieren. Während der parallelen Produktion entscheiden Sie, ob und wann Sie auf das neue Release wechseln. FELLOWPRO steuert anschließend den Rollover, durch den es zum gemeinsamen Produktions-Release für alle Kunden wird.

Die Versionsnummern in diesem Leitfaden – R1.0.x, R1.1.x und R1.2 – dienen nur zur Veranschaulichung. Derselbe Lebenszyklus wiederholt sich mit jedem weiteren Release; `x` steht für Updates innerhalb einer Release-Serie.

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
2. Entscheiden Sie, wann Ihre Organisation bereit ist, es produktiv zu nutzen.
3. Wechseln Sie über die Einstellung **Release Channel** in der DocBits-Anwendung von VESTA zu NOVA.

Dieser Wechsel erfolgt per Self-Service. FELLOWPRO legt nicht fest, welche Kunden zu NOVA wechseln sollen. Sie können VESTA während der gesamten parallelen Produktion weiter nutzen und das neue Release mit dem darauffolgenden Rollover übernehmen.

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

FELLOWPRO plant derzeit mit einem Release-Zyklus von etwa **3–4 Monaten**. Dieser Zeitraum spiegelt unsere aktuelle Planungsschätzung wider; er ist weder ein fester Zeitplan noch eine maximale Zyklusdauer noch eine Garantie für einen Release- oder Rollover-Termin.

Der Zeitpunkt jedes Rollovers und des Neuaufsetzens von NOVA hängt sowohl von der **Release-Reife als auch von der Zustimmung aller Kunden zum geplanten Übergang** ab. Wird zusätzliche Zeit benötigt, um die Release-Reife zu erreichen, Bedenken von Kunden zu klären oder die Zustimmung jedes einzelnen Kunden einzuholen, verlängert sich der Zyklus und kann länger als vier Monate dauern.

FELLOWPRO kündigt jeden geplanten Rollover vorab an. Jede indikative Zeitangabe steht unter dem Vorbehalt, dass diese Bedingungen erfüllt sind.

## Verantwortlichkeiten und Wahlmöglichkeiten der Kunden

| Übergang | Verantwortlich | Was Sie erwartet |
| --- | --- | --- |
| **Wechsel von VESTA zu NOVA während Phase 3** | Ihre Organisation | Evaluieren Sie NOVA in der Sandbox und entscheiden Sie über die Einstellung Release Channel der Anwendung, ob und wann Sie wechseln. |
| **Rollover von NOVA R1.1.x in VESTA R1.1.x** | FELLOWPRO | Prüfen Sie die Vorankündigung per E-Mail, äußern Sie etwaige Bedenken oder Einwände und bestätigen Sie Ihre Zustimmung zum geplanten Übergang. FELLOWPRO führt den Rollover durch, sobald das Release bereit ist und alle Kunden zugestimmt haben. |

## Häufig gestellte Fragen

### Können wir auf VESTA bleiben, während NOVA produktiv verfügbar ist?

Ja. Während Phase 3 können Sie auf VESTA bleiben oder zu NOVA wechseln, sobald Ihre Organisation bereit ist. Beim darauffolgenden Rollover wird das neue Release zu VESTA, und das vorherige Release wird abgekündigt.

### Wie wechseln wir zu NOVA?

Sobald NOVA produktiv verfügbar ist, verwenden Sie die Einstellung **Release Channel** in der DocBits-Anwendung. Ihre Organisation trifft diese Entscheidung eigenständig, basierend auf ihren Anforderungen und der Evaluierung des Release in der NOVA-Sandbox.

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

### Ist alle drei bis vier Monate ein neues Release garantiert?

Nein. Der Rhythmus von etwa 3–4 Monaten ist eine aktuelle Planungsschätzung, kein garantierter Zeitplan und keine maximale Dauer. Rollover und Neuaufsetzen von NOVA setzen sowohl die Release-Reife als auch die Zustimmung aller Kunden voraus. Erfordert eine dieser Bedingungen mehr Zeit, verlängert sich der Zyklus und kann vier Monate überschreiten. FELLOWPRO kündigt jeden geplanten Rollover vorab an.
