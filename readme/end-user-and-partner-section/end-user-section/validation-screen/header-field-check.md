---
description: >-
  Woher der Wert eines Kopffelds kommt und wie er entsteht — die Erklärung
  hinter dem Kopffeld-Check im Validierungsbildschirm.
---

# Kopffeld-Check: Woher die Daten kommen

Der Button **Kopffeld-Check** sitzt im Validierungsbildschirm neben **Speichern**. Er öffnet den Bericht *Woher kommt jeder Wert?*: Für jedes Kopffeld zeigt er, was auf dem Dokument stand, was den Wert unterwegs verändert hat, was DocBits jetzt anzeigt und warum.

Diese Seite erklärt, wie ein Wert entsteht und was die einzelnen Quellen bedeuten. Es ist kein Expertenwissen nötig.

{% hint style="info" %}
Der Kopffeld-Check gehört zum Modul **Analytics**. Ist der Button ausgegraut, kann ein Administrator ihn Ihrer Rolle unter **Einstellungen › Rollen** freigeben.
{% endhint %}

## Ein Wert entsteht immer in dieser Reihenfolge

| Schritt | Was passiert |
| --- | --- |
| **1. Lesen** | Der Wert wird aus dem Dokument gelesen — durch eine trainierte Regel, durch die KI oder direkt aus einer E-Rechnung. |
| **2. Umformen** | Skripte und Transformationsregeln des Kunden verändern den gelesenen Wert: kürzen, ergänzen, das Format anpassen. |
| **3. Nachschlagen** | Der Wert wird in den Stammdaten gesucht. Wird etwas gefunden, ersetzt der Stammdatensatz den gelesenen Wert. |
| **4. Anzeigen** | Der Benutzer sieht nur das Ergebnis. Was unterwegs passiert ist, zeigt der Kopffeld-Check. |

Schritt 2 und 3 laufen nicht immer — aber wenn sie laufen, verändern sie den Wert. Genau daher kommen die meisten gemeldeten Fälle.

## Die Quellen — was jede bedeutet

Die Symbole sind dieselben, die der Bericht in der Spalte **Aktion** und in der Filterleiste oben zeigt.

### Trainierte Regel

DocBits merkt sich, wo ein Feld auf diesem Dokumenttyp steht, weil es dort einmal jemand markiert hat.

* **Beispiel:** Lieferant „Bornemann“ — immer an derselben Stelle oben links.
* **Wenn es falsch ist:** die richtige Stelle auf dem Dokument markieren und speichern — die Regel lernt daraus.

### KI

Kein festes Muster. Die KI liest das Dokument wie ein Mensch und entscheidet selbst, welcher Text zu welchem Feld gehört.

* **Beispiel:** Rechnungsdatum, Beträge, Zahlungsbedingungen.
* **Wenn es falsch ist:** korrigieren. Ein- und ausschalten lässt sie sich unter **Einstellungen › OCR-Kopffelder**.

### E-Rechnung

Bei XRechnung oder ZUGFeRD wird nichts erkannt: Der Wert ist im Dokument bereits ein Datenfeld und wird direkt übernommen.

* **Beispiel:** Rechnungsnummer aus dem XML-Feld des Absenders.
* **Wenn es falsch ist:** Der Fehler liegt beim Absender. DocBits zeigt genau, aus welchem XML-Feld der Wert stammt.

### Skript / Transformationsregel

Nach dem Lesen greift die Logik des Kunden ein und formt den Wert um. Das Dokument bleibt gleich — der Wert nicht.

* **Beispiel:** `1001 / LS 206776` wird zu `1001`.
* **Wenn es falsch ist:** nicht auf dem Dokument suchen. **Einstellungen › Skripte** bzw. **Transformationsregeln** prüfen.

### Stammdaten

Der gelesene Wert wird in Ihren eigenen Daten gesucht — Bestellungen, Lieferanten. Ein Treffer ersetzt den Wert und zieht weitere Felder mit.

* **Beispiel:** `1001` findet die Bestellung `06O051001` — und Lieferant und Käufer kommen dann ebenfalls von dort.
* **Wenn es falsch ist:** **Einstellungen › Lookup-Konfiguration** prüfen. Dort steht, ob die Suche exakt ist oder auch Teiltreffer akzeptiert.

### Berechnet

Nicht gelesen, sondern aus anderen Feldern berechnet.

* **Beispiel:** Fälligkeitsdatum aus Rechnungsdatum plus Zahlungsbedingungen.
* **Wenn es falsch ist:** meist ist eines der Felder falsch, aus denen berechnet wird.

### Barcode

Aus einem Barcode oder QR-Code auf dem Dokument gelesen.

* **Beispiel:** Die Rechnungsnummer steckt im QR-Code.
* **Wenn es falsch ist:** die Barcode-Einstellungen des Dokumenttyps prüfen.

## Was am häufigsten missverstanden wird

{% hint style="warning" %}
Steht in einem Feld plötzlich ein Wert, der so nicht auf dem Dokument steht, war es fast nie die KI — sondern Schritt 2 oder Schritt 3. Am häufigsten der Stammdaten-Treffer, der auch Teiltreffer akzeptiert: `1001` trifft `06O051001`, und mit der gefundenen Bestellung ändert sich auch der Lieferant.
{% endhint %}

Im Bericht ist ein solches Feld rot markiert. Die Spalte **Aktion** zeigt den Stammdatensatz zusammen mit einem roten Chip *nur Teiltreffer*, und der übereinstimmende Teil des Werts ist hervorgehoben.

## Den Bericht lesen

* **Status-Chips** oben zählen die Felder, die unverändert aus dem Dokument kamen, unterwegs verändert wurden oder so nicht auf dem Dokument stehen. Ein Klick auf einen Chip zeigt nur diese Felder; ein weiterer Klick zeigt wieder alle.
* **Quellenfilter:** Die Symbolreihe zeigt jede Extraktionsmethode. Ein Klick zeigt nur die Felder, die durch sie gelaufen sind.
* **Aktion:** jeder Schritt, den der Wert durchlaufen hat, mit dem Symbol seiner Quelle. Der Schritt, aus dem der aktuelle Wert stammt, ist hervorgehoben. Beim Darüberfahren sehen Sie, was jeder Schritt getan hat, von welchem Wert zu welchem.
* **Grund:** der Status des Feldes. Das (i)-Symbol erklärt, warum der Wert so ist, wie er ist. Steht dort *Feld gab es nicht*, war das Feld auf dem Dokument nicht vorhanden.
* Lange Werte werden mit … gekürzt — beim Darüberfahren erscheint der volle Wert.
