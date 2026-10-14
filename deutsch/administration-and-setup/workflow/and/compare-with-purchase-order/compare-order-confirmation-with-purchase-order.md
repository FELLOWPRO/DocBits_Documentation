# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Diese DocBits-Karte ist darauf ausgelegt, ein bestimmtes Auftragsdatenfeld – etwa Menge, Rabatt oder Stückpreis – zwischen einer Auftragsbestätigung und einer Bestellung zu vergleichen. Indem sie jeweils einen gezielten Vergleich eines einzelnen Feldes ermöglicht, sorgt sie für Präzision bei der Validierung wichtiger Datenpunkte und erhält die Auftragsgenauigkeit. **Version 4** erweitert diese Funktionalität, indem sie Vergleiche zwischen verschiedenen Entitäten wie der Bestellung, den erhaltenen Mengen und dem Dokument selbst ermöglicht und so mehr Flexibilität und Kontrolle in den Workflow bringt.

## Bestandteile der Karte:

1. **Any/All**&#x20;
   * **Beschreibung:** Bestimmt, ob die Bedingung für irgendeine oder alle Zeilen der Auftragsbestätigung gilt.\
     **Optionen:**
     * **Any**: Der Vergleich wird ausgelöst, wenn der ausgewählte Feldwert in irgendeiner Zeile der Auftragsbestätigung mit dem entsprechenden Wert in der Bestellung übereinstimmt.
     * **All**: Der Vergleich wird nur ausgelöst, wenn der ausgewählte Feldwert in allen Zeilen der Auftragsbestätigung mit dem entsprechenden Wert in der Bestellung übereinstimmt.
2. **Auftragsdatenfeld**
   * **Beschreibung**: Gibt das Datenfeld an, das zwischen der Auftragsbestätigung und der Bestellung verglichen wird.
   * **Detail**: Benutzer können eines der folgenden Felder für den Vergleich auswählen:
     * **Menge**: Vergleicht die bestellte Menge mit der bestätigten Menge.
     * **Rabatt**: Überprüft, ob der Rabatt in der Bestätigung mit der Bestellung übereinstimmt.
     * **Stückpreis**: Stellt sicher, dass der Stückpreis in der Bestätigung mit der Bestellung übereinstimmt.
3. **Operator**
   * **Beschreibung**: Legt die Bedingung fest, die auf den Vergleich des ausgewählten Datenfeldes angewendet wird.
   * **Optionen**:
     * **Gleich (=)**: Bestätigt, dass der Wert mit der Bestellung übereinstimmt.
     * **Ungleich (≠)**: Stellt sicher, dass sich der Wert von der Bestellung unterscheidet.
     * **Größer als (>)**: Überprüft, ob der Wert den Wert der Bestellung übersteigt.
     * **Größer oder gleich (≥)**: Bestätigt, dass der Wert dem Wert der Bestellung entspricht oder ihn übersteigt.
     * **Kleiner als (<)**: Prüft, ob der Wert unter dem Wert der Bestellung liegt.
     * **Kleiner oder gleich (≤)**: Bestätigt, dass der Wert unter dem Wert der Bestellung liegt oder ihm entspricht.

## **Zusätzliche Komponenten in Version 4**:

* **Vergleichstyp**: Wählt die zu vergleichenden Entitäten aus. Die Optionen umfassen:
  * **Purchase Order to Document**: Vergleicht die Bestelldaten mit dem zugehörigen Dokument.
  * **Received to Document**: Vergleicht die erhaltenen Daten (z. B. erhaltene Mengen) mit dem Dokument.
  * **Purchase Order to Received**: Vergleicht die Bestelldaten mit den erhaltenen Mengen.

## Funktionalität:

* **Feldvergleich**: Das System vergleicht das ausgewählte Auftragsdatenfeld (Stückpreis, Rabatt oder Menge) aus der Auftragsbestätigung mit dem entsprechenden Wert in der Bestellung.
* **Ausführung der Aktion**: Basierend auf dem Vergleichsergebnis und der Operatorbedingung kann die Karte Folgeaktionen auslösen, etwa Benachrichtigungen oder Warnungen.

## Beispiel-Szenario:

* Eine Auftragsbestätigung gibt einen **Stückpreis** von 50 $ an, während die Bestellung 45 $ ausweist. Mit dem Operator "Größer als" markiert die Karte die Abweichung und ermöglicht es dem Beschaffungsteam, sie vor der Verarbeitung zu klären.

## Fazit:

Diese Karte vereinfacht die Validierung einzelner Auftragsdatenfelder und stellt die Einhaltung der Bestellkonditionen sicher. Indem sie für den Vergleich jeweils ein einzelnes Feld isoliert, unterstützt sie gezielte Prüfungen und die Fehlervermeidung bei der Auftragsverarbeitung.
