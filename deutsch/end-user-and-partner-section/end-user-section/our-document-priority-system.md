# Unser Dokumenten-Prioritätssystem

In unserem Dokumentenverarbeitungssystem bearbeiten wir täglich ein großes Volumen an Dokumenten von mehreren Kunden. Um sicherzustellen, dass die Dokumente jedes Kunden zeitnah verarbeitet werden, haben wir ein ausgeklügeltes Prioritätssystem implementiert. Dieses System passt die Prioritäten dynamisch an die Anzahl der ausstehenden Dokumente eines Kunden an und gewährleistet so **Fairness** und **Effizienz**. Schauen wir uns an, wie dieses Prioritätssystem funktioniert und wann der Aufgabenzähler zurückgesetzt wird.

**Schlüsselkonzepte des Prioritätssystems**

Unser Prioritätssystem basiert auf einigen Schlüsselkonzepten:

1. **Ausstehende Dokumente**: Dies ist die Anzahl der Dokumente, die ein Kunde übermittelt hat, die jedoch noch nicht verarbeitet wurden.
2. **Reset-Intervall**: Das System setzt die Anzahl der ausstehenden Dokumente in regelmäßigen Abständen auf null zurück, um sicherzustellen, dass kein Kunde die Verarbeitungsressourcen auf unbegrenzte Zeit für sich beanspruchen kann.

**So wird die Priorität bestimmt**

Hier finden Sie eine Schritt-für-Schritt-Erläuterung, wie die Priorität für die Verarbeitung von Dokumenten bestimmt wird:

1. **Erfassung ausstehender Dokumente**: Jeder Kunde verfügt über eine Anzahl ausstehender Dokumente. Diese Anzahl hilft uns zu erkennen, wie viele Dokumente jedes Kunden auf ihre Verarbeitung warten.
2. **Zurücksetzen der Anzahl**: Um Fairness zu wahren, setzen wir die Anzahl der ausstehenden Dokumente auf null zurück, wenn seit der letzten Aktualisierung eine bestimmte Zeit (das Reset-Intervall) vergangen ist. Dieses Intervall ist standardmäßig auf 1500 Sekunden (bzw. 25 Minuten) eingestellt.
3. **Aktualisieren der Anzahl**: Wenn das Reset-Intervall noch nicht abgelaufen ist, verringern wir die Anzahl der ausstehenden Dokumente bei jeder Prüfung um eins und simulieren so die Verarbeitung eines Dokuments.
4. **Festlegen der Prioritäten**: Die Priorität für die Verarbeitung von Aufgaben richtet sich nach der Anzahl der ausstehenden Dokumente. Je weniger ausstehende Dokumente vorhanden sind, desto höher ist die Priorität, was bedeutet, dass diese Aufgaben früher verarbeitet werden. Wir haben spezifische Schwellenwerte, um Prioritätsstufen von 1 (höchste Priorität) bis 9 (niedrigste Priorität) zuzuweisen.

**Prioritätsstufen**

Die Prioritätsstufen werden anhand der Anzahl der ausstehenden Dokumente wie folgt zugewiesen:

* **Priorität 9**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -20 ist
* **Priorität 8**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -14 ist
* **Priorität 7**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -12 ist
* **Priorität 6**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -10 ist
* **Priorität 5**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -8 ist
* **Priorität 4**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -6 ist
* **Priorität 3**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -4 ist
* **Priorität 2**: Wenn die Anzahl der ausstehenden Dokumente kleiner als -2 ist
* **Priorität 1**: Wenn die Anzahl der ausstehenden Dokumente größer oder gleich -2 ist

{% hint style="info" %}
Vereinfacht ausgedrückt: Je höher die Anzahl der ausstehenden Dokumente, desto niedriger die Prioritätsstufe, was bedeutet, dass diese Dokumente im Vergleich zu anderen mit höherer Priorität später verarbeitet werden.
{% endhint %}

**Wann der Zähler zurückgesetzt wird**

Der Zähler für ausstehende Dokumente wird auf null zurückgesetzt, wenn seit der letzten Aktualisierung mehr als das Reset-Intervall (**1500** Sekunden) vergangen ist. Dieser Mechanismus stellt sicher, dass kein Kunde endlos ausstehende Dokumente ansammeln und die Systemressourcen monopolisieren kann. Durch das regelmäßige Zurücksetzen des Zählers garantieren wir, dass jeder Kunde einen fairen Anteil an Verarbeitungszeit erhält.
