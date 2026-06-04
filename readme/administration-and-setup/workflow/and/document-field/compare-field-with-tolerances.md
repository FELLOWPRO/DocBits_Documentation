# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, den Wert eines Feldes mit einem angegebenen Referenzwert zu vergleichen und dabei Toleranzen zuzulassen. Sie ermöglicht eine präzise bedingte Verarbeitung in Workflows, in denen kleine Abweichungen akzeptabel sind, und eignet sich damit ideal für Szenarien wie Qualitätssicherung, Finanzanalyse oder schwellenwertbasierte Aktionen.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Das im Vergleich auszuwertende Feld.
   * **Detail:** Dieser muss exakt mit dem Bezeichner des ersten Feldes innerhalb des Dokuments übereinstimmen.
2. **Vergleichsoperator**
   * **Beschreibung:** Gibt an, wie der ausgewählte Feldwert mit dem Referenzwert verglichen wird.
   * **Optionen:**
     * **Gleich (=):** Überprüft, ob der Feldwert exakt mit dem Referenzwert übereinstimmt.
     * **Ungleich (≠):** Überprüft, ob der Feldwert nicht mit dem Referenzwert übereinstimmt.
     * **Größer als (>):** Prüft, ob der Feldwert größer als der Referenzwert ist.
     * **Größer oder gleich (≥):** Prüft, ob der Feldwert größer oder gleich dem Referenzwert ist.
     * **Kleiner als (<):** Prüft, ob der Feldwert kleiner als der Referenzwert ist.
     * **Kleiner oder gleich (≤):** Prüft, ob der Feldwert kleiner oder gleich dem Referenzwert ist.
3. **Referenzwert**
   * **Beschreibung:** Der Wert, mit dem das Feld verglichen wird.
   * **Detail:** Dieser Wert kann je nach Kontext des Vergleichs numerisch, textbasiert oder datumsbasiert sein.
4. **Toleranzbetrag**
   * **Beschreibung:** Legt die zulässige Fehlertoleranz für den Vergleich fest.
   * **Detail:** Der Toleranzbetrag ist ein numerischer Wert, der die maximal zulässige Differenz zwischen den beiden Feldwerten angibt, damit der Vergleich als erfüllt gilt.
5. **Toleranztyp**
   * **Beschreibung:** Gibt die Maßeinheit für den Toleranzbetrag an.
   * **Optionen:**
     * **Wert:** Die Toleranz ist ein absoluter Wert, das heißt, die beiden Felder dürfen sich um den angegebenen Toleranzbetrag unterscheiden.
     * **Prozent:** Die Toleranz wird als Prozentsatz des zweiten Feldwerts berechnet und lässt so eine relative Fehlertoleranz zu.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System wertet den Wert des Feldes anhand des Referenzwerts mithilfe des ausgewählten Vergleichsoperators aus. Ist eine Toleranz konfiguriert, betrachtet das System den Vergleich als erfolgreich, wenn der Feldwert innerhalb des definierten Toleranzbereichs liegt.
* **Ausführung der Aktion:**
  * **Innerhalb der Toleranz:** Erfüllt der Feldwert die Bedingung innerhalb der angegebenen Toleranz, wird der Workflow fortgesetzt und löst die zugehörigen Aktionen aus.
  * **Außerhalb der Toleranz:** Erfüllt der Feldwert die Bedingung nicht oder liegt er außerhalb des Toleranzbereichs, können alternative Aktionen ausgeführt werden, etwa Protokollierung, das Senden von Warnungen oder das Anhalten des Workflows.

## **Einrichtung und Konfiguration:**

* Benutzer konfigurieren die Karte, indem sie das auszuwertende Feld aus einer Liste verfügbarer Felder auswählen und den Vergleichsoperator (z. B. gleich, größer als) aus einer Dropdown-Liste wählen. Anschließend geben sie den Referenzwert an, mit dem verglichen wird, und legen den Toleranzbetrag fest; danach wählen sie den Toleranztyp (z. B. Prozent oder Wert).&#x20;

## **Fazit:**

Die Karte "Field Comparison with Tolerances" ist ein vielseitiges Werkzeug für Workflows, die flexible Auswertungen erfordern. Indem sie Vergleiche mit Toleranzen ermöglicht, sorgt sie dafür, dass Workflows effizient und anpassungsfähig bleiben und reale Abweichungen berücksichtigen, ohne Kompromisse bei der Genauigkeit einzugehen.
