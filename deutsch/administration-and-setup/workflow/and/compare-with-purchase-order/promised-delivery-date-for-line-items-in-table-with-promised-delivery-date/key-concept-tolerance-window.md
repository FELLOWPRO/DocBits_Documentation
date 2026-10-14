# Schlüsselkonzept: Toleranzfenster

Bevor wir uns die Operatoren ansehen, ist es wichtig zu verstehen, wie das Toleranzfenster berechnet wird.

## Was ist ein Toleranzfenster?

Das Toleranzfenster definiert einen Bereich akzeptabler Daten rund um das zugesagte Lieferdatum der Bestellung.

**Beispiel:**

* Bestelldatum: **9. Januar**
* Toleranztage: **3**
* Toleranzfenster: **6. Januar → 12. Januar**

> <mark style="color:red;">Nur die ausgewählten</mark> <mark style="color:red;"></mark><mark style="color:red;">**Zulässigen Toleranztage**</mark> <mark style="color:red;"></mark><mark style="color:red;">(Wochentage) werden bei der Berechnung dieses Fensters gezählt.</mark>

### Visuelles Zeitachsen-Beispiel

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Operatorverhalten anhand von Beispielen erklärt

* **Gleich (=)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss _innerhalb_ des Toleranzfensters liegen.
  * **Gültige Daten:**
    * Jedes Datum zwischen dem **6. Jan und 12. Jan** (einschließlich)
  * **Ungültige Daten:**
    * Jedes Datum **vor dem 6. Jan**
    * Jedes Datum **nach dem 12. Jan**
* **Ungleich (≠)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss _außerhalb_ des Toleranzfensters liegen.
  * **Gültige Daten:**
    * Jedes Datum **vor dem 6. Jan**
    * Jedes Datum **nach dem 12. Jan**
  * **Ungültige Daten:**
    * Daten zwischen dem **6. Jan und 12. Jan**
* **Größer oder gleich (≥)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss am oder nach dem **Beginn des Toleranzfensters** liegen.
  * **Gültige Daten:**
    * **6. Jan → jedes zukünftige Datum**
  * **Ungültige Daten:**
    * Jedes Datum **vor dem 6. Jan**
  * <mark style="color:red;">**Wichtig:**</mark>\
    Dieser Operator lässt Daten _innerhalb_ des Toleranzfensters **und darüber hinaus** zu.
* **Kleiner oder gleich (≤)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss am oder vor dem **Ende des Toleranzfensters** liegen.
  * **Gültige Daten:**
    * Jedes vergangene Datum bis zum **12. Jan**
  * **Ungültige Daten:**
    * Jedes Datum **nach dem 12. Jan**
* **Größer als (>)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss _strikt nach_ dem Toleranzfenster liegen.
  * **Gültige Daten:**
    * **13. Jan → jedes zukünftige Datum**
  * **Ungültige Daten:**
    * Jedes Datum **am oder vor dem 12. Jan**
* **Kleiner als (<)**
  * **Bedeutung:**\
    Das Lieferdatum der Position muss _strikt vor_ dem Toleranzfenster liegen.
  * **Gültige Daten:**
    * Jedes Datum **vor dem 6. Jan**
  * **Ungültige Daten:**
    * Jedes Datum **am oder nach dem 6. Jan**

## Wie sich „Zulässige Toleranztage“ auf das Toleranzfenster auswirken

Bei der Berechnung des Toleranzfensters werden **nur die ausgewählten Wochentage gezählt**.\
Tage, die nicht ausgewählt sind (etwa Wochenenden oder ausgeschlossene Wochentage), werden **vollständig übersprungen**.

#### Beispiel: Wochentagsbasierte Toleranzberechnung

**Konfiguration:**

* Bestelldatum: **Mittwoch, 9. Januar**
* Toleranztage: **3**
* Zulässige Toleranztage: **Montag, Dienstag, Mittwoch, Donnerstag, Freitag**
* Wochenenden (Samstag, Sonntag): **Nicht ausgewählt**

#### Schritt-für-Schritt-Berechnung

Ausgehend vom Bestelldatum (**9. Jan**):

**Rückwärtszählung (3 Toleranztage):**

* Dienstag, 8. Jan → **Tag 1**
* Montag, 7. Jan → **Tag 2**
* Sonntag, 6. Jan → _Übersprungen (nicht zulässig)_
* Samstag, 5. Jan → _Übersprungen (nicht zulässig)_
* Freitag, 4. Jan → **Tag 3**

➡ **Toleranz-Startdatum: Freitag, 4. Januar**

**Vorwärtszählung (3 Toleranztage):**

* Donnerstag, 10. Jan → **Tag 1**
* Freitag, 11. Jan → **Tag 2**
* Samstag, 12. Jan → _Übersprungen_
* Sonntag, 13. Jan → _Übersprungen_
* Montag, 14. Jan → **Tag 3**

➡ **Toleranz-Enddatum: Montag, 14. Januar**

#### Resultierendes Toleranzfenster

```
4 January  →  14 January
```

#### Warum das wichtig ist

Wenn die Zulässigen Toleranztage falsch konfiguriert sind:

* können Lieferdaten **unerwartet gültig oder ungültig** erscheinen
* werden frühe oder verspätete Lieferungen möglicherweise nicht korrekt erkannt
