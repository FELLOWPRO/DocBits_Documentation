# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck**

Diese Workflow-Karte ist darauf ausgelegt, bestimmte Felder – **Stückpreis**, **Rabatt** oder **Menge** – zwischen einer Auftragsbestätigung und einer Bestellung zu vergleichen. Sie gewährleistet Konsistenz und die Einhaltung der vereinbarten Konditionen. Basierend auf dem Vergleichsergebnis ermöglicht die Karte es Benutzern, einen festgelegten Text in ein ausgewähltes Feld zu schreiben, wenn die Bedingung als **wahr** oder **falsch** ausgewertet wird, und optimiert so die Dokumentverarbeitung und reduziert manuelle Eingriffe.

## **Bestandteile der Karte**

1. **Auftragsdaten**
   * **Beschreibung:** Gibt das Feld an, das zwischen der Auftragsbestätigung und der Bestellung verglichen wird.
   * **Optionen:**
     * **Stückpreis**: Vergleicht den Stückpreis in beiden Dokumenten.
     * **Rabatt**: Vergleicht den Rabattprozentsatz oder -wert.
     * **Menge**: Vergleicht die bestellte Menge.
2. **Operator**
   * **Beschreibung:** Legt die während des Vergleichs angewendete Bedingung fest.
   * **Optionen:**
     * **Gleich (=):** Prüft, ob der Wert im ausgewählten Feld zwischen der Auftragsbestätigung und der Bestellung übereinstimmt.
     * **Ungleich (≠):** Stellt sicher, dass sich der Wert im ausgewählten Feld zwischen den beiden Dokumenten unterscheidet.
3. **Text**
   * **Beschreibung:** Gibt den Text an, der bei der Bedingungsauswertung in das Zielfeld geschrieben wird.
   * **Detail:** Dieser Text kann benutzerdefinierte Notizen, Statusaktualisierungen oder vordefinierte Werte enthalten.
4. **Feldname**
   * **Beschreibung:** Gibt das Feld an, in das der Text geschrieben wird.
   * **Detail:** Das Zielfeld wird aus den verfügbaren bearbeitbaren Feldern innerhalb des Systems ausgewählt.
5. **Bedingungsergebnis**
   * **Beschreibung:** Bestimmt anhand des Vergleichsergebnisses, wann der Text geschrieben werden soll.
   * **Optionen:**
     * **True:** Schreibt den Text, wenn die Vergleichsbedingung erfüllt ist.
     * **False:** Schreibt den Text, wenn die Vergleichsbedingung nicht erfüllt ist.

## **Funktionalität**

* **Vergleichsauswertung:** Das System vergleicht das ausgewählte Feld zwischen der Auftragsbestätigung und der Bestellung mithilfe des angegebenen Operators.
* **Ausführung der Aktion:** Wird die Bedingung als **wahr** oder **falsch** ausgewertet, wird der angegebene Text in das festgelegte Feld geschrieben.

## **Einrichtung und Konfiguration**

* Um diese Karte einzurichten, wählen Benutzer zunächst das zu vergleichende Feld aus – **Stückpreis**, **Rabatt** oder **Menge**. Anschließend wählen sie einen Operator, um die Vergleichsbedingung festzulegen, etwa **gleich** oder **ungleich**. Benutzer geben den Text an, der in ein Zielfeld geschrieben werden soll, und wählen anhand des Bedingungsergebnisses (**wahr** oder **falsch**) aus, wann diese Aktion erfolgen soll.

## **Beispiel-Szenario**

* Eine Auftragsbestätigung weist für ein Produkt einen Stückpreis von 50 $ aus, während die Bestellung einen Preis von 45 $ angibt. Mit dem Operator **Ungleich (≠)** erkennt die Karte die Abweichung und schreibt den Text "Price Mismatch" in ein festgelegtes Feld, wenn die Bedingung als **wahr** ausgewertet wird.

## **Fazit**

Die Workflow-Karte "\[Unit Price/Discount/Quantity] in Order Confirmation" bietet eine praktische Lösung, um die Konsistenz von Dokumenten sicherzustellen. Indem sie Abweichungen automatisch markiert und relevanten Text in festgelegte Felder schreibt, steigert sie die Effizienz und reduziert Fehler in den Prozessen des Auftragsmanagements.
