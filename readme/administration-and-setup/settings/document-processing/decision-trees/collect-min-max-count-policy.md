# Collect-(min/max/count)-Policy

Diese Policy sammelt alle zutreffenden Regeln und wählt entweder das **Minimum**, das **Maximum** oder **zählt** die Vorkommen. Sie funktioniert nur für **Return Type Value**.

**Beispiel:**

| Regel | Bedingung            | Rückgabewert |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Wenn die Option **Collect (min)** ausgewählt ist, gibt das Ergebnis das **Minimum** der **Rückgabewerte** der zutreffenden Regeln zurück.
   * Für den Eingabewert **Total Amount = 2500** würde die Auswertung der Regeln wie folgt aussehen:
     * **Regel 1**: Total Amount <= 1000 (trifft nicht zu)
     * **Regel 2**: Total Amount <= 2000 (trifft nicht zu)
     * **Regel 3**: Total Amount <= 3000 (trifft zu, Rückgabewert = 3)
     * **Regel 4**: Total Amount <= 4000 (trifft zu, Rückgabewert = 4)
     * **Regel 5**: Total Amount <= 5000 (trifft zu, Rückgabewert = 5)
   * Die **zutreffenden Regeln** sind Regel 3, Regel 4 und Regel 5 mit **Rückgabewerten** von **3, 4 und 5**.
   * Da die **Collect-(min)**-Policy angewendet wird, ist das Ergebnis der **Minimalwert**, also **3**.
   * **Ergebnis**: **3**
2. Wenn die Option **Collect (max)** ausgewählt ist, gibt das Ergebnis das **Maximum** der **Rückgabewerte** der zutreffenden Regeln zurück.
   * Bei derselben Auswertung wie oben lautet das Ergebnis:
   * **Ergebnis**: **5**
3. Wenn die Option **Collect (count)** ausgewählt ist, zählt das Ergebnis die **Anzahl der zutreffenden Regeln**.
   * Bei derselben Auswertung wie oben lautet das Ergebnis:
   * **Ergebnis**: **3** (da 3 Regeln zutreffen).
