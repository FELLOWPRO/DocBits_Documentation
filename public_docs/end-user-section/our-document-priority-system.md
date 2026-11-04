# Unser Dokumenten-Prioritätssystem

In unserem Dokumentenverarbeitungssystem bearbeiten wir täglich ein großes Volumen an Dokumenten von mehreren Kunden. Um sicherzustellen, dass die Dokumente jedes Kunden zeitnah bearbeitet werden, haben wir ein ausgeklügeltes Prioritätssystem implementiert. Dieses System passt die Prioritäten dynamisch basierend auf der Anzahl der ausstehenden Dokumente eines Kunden an und gewährleistet **Fairness** und **Effizienz**. Lassen Sie uns näher darauf eingehen, wie dieses Prioritätssystem funktioniert und wann der Aufgaben-Zähler zurückgesetzt wird.

**Schlüsselkonzepte des Prioritätssystems**

Unser Prioritätssystem dreht sich um einige Schlüsselkonzepte:

1. **Ausstehende Dokumente**: Dies ist eine Zählung der Dokumente, die ein Kunde eingereicht hat, die jedoch noch bearbeitet werden müssen.
2. **Zurücksetzintervall**: Das System setzt die Zählung der ausstehenden Dokumente regelmäßig auf null zurück, um sicherzustellen, dass kein Kunde die Verarbeitungsressourcen unbegrenzt monopolisiert.

**Wie die Priorität bestimmt wird**

Hier ist eine schrittweise Erklärung, wie die Priorität für die Verarbeitung von Dokumenten bestimmt wird:

1. **Verfolgung ausstehender Dokumente**: Jeder Kunde hat eine Zählung der ausstehenden Dokumente. Diese Zählung hilft uns zu wissen, wie viele Dokumente auf die Verarbeitung für jeden Kunden warten.
2. **Zurücksetzen der Zählung**: Um Fairness zu gewährleisten, setzen wir die Zählung der ausstehenden Dokumente auf null zurück, wenn eine festgelegte Zeitspanne (das Zurücksetzintervall) seit dem letzten Update vergangen ist. Dieses Intervall ist standardmäßig auf 1500 Sekunden (oder 25 Minuten) eingestellt.
3. **Aktualisierung der Zählung**: Wenn das Zurücksetzintervall nicht vergangen ist, reduzieren wir die Zählung der ausstehenden Dokumente jedes Mal um eins, wenn wir überprüfen, was die Verarbeitung eines Dokuments simuliert.
4. **Festlegung der Prioritäten**: Die Priorität für die Verarbeitung von Aufgaben basiert auf der Anzahl der ausstehenden Dokumente. Je weniger ausstehende Dokumente, desto höher die Priorität, was bedeutet, dass diese Aufgaben früher bearbeitet werden. Wir haben spezifische Schwellenwerte, um Prioritätsstufen von 1 (höchste Priorität) bis 9 (niedrigste Priorität) zuzuweisen.

**Prioritätsstufen**

Die Prioritätsstufen werden basierend auf der Zählung der ausstehenden Dokumente wie folgt zugewiesen:

* **Priorität 9**: Wenn die Zählung der ausstehenden Dokumente weniger als -20 beträgt
* **Priorität 8**: Wenn die Zählung der ausstehenden Dokumente weniger als -14 beträgt
* **Priorität 7**: Wenn die Zählung der ausstehenden Dokumente weniger als -12 beträgt
* **Priorität 6**: Wenn die Zählung der ausstehenden Dokumente weniger als -10 beträgt
* **Priorität 5**: Wenn die Zählung der ausstehenden Dokumente weniger als -8 beträgt
* **Priorität 4**: Wenn die Zählung der ausstehenden Dokumente weniger als -6 beträgt
* **Priorität 3**: Wenn die Zählung der ausstehenden Dokumente weniger als -4 beträgt
* **Priorität 2**: Wenn die Zählung der ausstehenden Dokumente weniger als -2 beträgt
* **Priorität 1**: Wenn die Zählung der ausstehenden Dokumente größer oder gleich -2 ist

{% hint style="info" %}
Einfacher ausgedrückt, wenn die Anzahl der ausstehenden Dokumente steigt, sinkt die Prioritätsstufe, was bedeutet, dass diese Dokumente später im Vergleich zu anderen mit höheren Prioritäten bearbeitet werden.
{% endhint %}

**Wann der Zähler zurückgesetzt wird**

Der Zähler der ausstehenden Dokumente wird auf null zurückgesetzt, wenn mehr als das Zurücksetzintervall (**1500** Sekunden) seit dem letzten Update vergangen ist. Dieser Mechanismus stellt sicher, dass kein Kunde endlos ausstehende Dokumente anhäuft und die Systemressourcen blockiert. Durch das regelmäßige Zurücksetzen des Zählers garantieren wir, dass jeder Kunde einen fairen Anteil an Verarbeitungszeit erhält.
