# Umgang mit Zusatzkosten bei Infor M3

## Übersicht

Dieses Dokument enthält detaillierte Informationen darüber, wie DocBits mit Infor M3 integriert wird, um Zusatzkosten (Charges) im Zusammenhang mit Rechnungen und Bestellungen (PO) zu behandeln. Es enthält Szenarien für externe Zusatzkosten und die jeweils erwarteten Lösungen.

## Szenarien für den Umgang mit Zusatzkosten

| Szenario-ID | Beschreibung                                                                                  | Geschäftsfall                                                                                                                                  | Erwartete Lösung                                                                                                                                                                                                                                                  |
| ----------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | Externe Zusatzkosten nicht auf der Bestellung, aber auf der Rechnung (akzeptiert)             | Externe Zusatzkosten erscheinen auf der Rechnung, sind aber nicht auf der Bestellung aufgeführt. Diese Zusatzkosten werden akzeptiert.        | Die Zusatzkosten werden auf Basis des von DocBits gesendeten Kostenelements auf die Accounting Rule PP20-228 gebucht.                                                                                                                                              |
| 2           | Externe Zusatzkosten nicht auf der Bestellung, aber auf der Rechnung (nicht akzeptiert)       | Externe Zusatzkosten erscheinen auf der Rechnung, sind aber nicht auf der Bestellung aufgeführt. Diese Zusatzkosten werden nicht akzeptiert oder genehmigt. | Der Gesamtrechnungswert wird mit einer Kopf-Zusatzkostenposition für die nicht genehmigten Zusatzkosten erfasst. Zusätzlich wird für diese Zusatzkosten eine Lastschriftanzeige erstellt.                                                                          |
| 3           | Externe Zusatzkosten auf der Rechnung höher oder niedriger als auf der Bestellung (innerhalb der Toleranz) | Die externen Zusatzkosten auf der Rechnung sind höher oder niedriger als die auf der Bestellung, liegen aber innerhalb der akzeptierten Toleranz. | Die zusätzlichen Kosten werden auf Basis des von DocBits gesendeten Kostenelements auf die Accounting Rule PP20-228 gebucht.                                                                                                                                       |
| 4           | Externe Zusatzkosten auf der Rechnung höher als auf der Bestellung (außerhalb der Toleranz, nicht genehmigt) | Die externen Zusatzkosten auf der Rechnung sind höher als die auf der Bestellung und liegen außerhalb der akzeptierten Toleranz; sie sind nicht genehmigt. | Die Rechnung wird mit dem Gesamtrechnungsbetrag erfasst. Eine zusätzliche nicht genehmigte Zusatzkostenposition wird als Kopf-Zusatzkosten hinzugefügt, und für diese zusätzlichen Kosten wird eine Lastschriftanzeige erstellt.                                   |
| 5           | Externe Zusatzkosten auf der Rechnung höher als auf der Bestellung (außerhalb der Toleranz, in DocBits genehmigt) | Die externen Zusatzkosten auf der Rechnung sind höher als die auf der Bestellung und liegen außerhalb der akzeptierten Toleranz; sie sind in DocBits genehmigt. | Die zusätzlichen Kosten werden auf PP20-228 gebucht. Zwei Optionen werden betrachtet:\<br>- Wenn die Toleranz in APS900 > DocBits ist, werden die zusätzlichen Kosten automatisch gebucht.\<br>- Wenn die Toleranz in APS900 = DocBits ist, werden die zusätzlichen Kosten mit neuen, nicht auf der Bestellung vorhandenen Kostenelementen gebucht. |
| 6           | Externe Zusatzkosten auf der Rechnung niedriger als auf der Bestellung (außerhalb der Toleranz, nicht genehmigt) | Die externen Zusatzkosten auf der Rechnung sind niedriger als die auf der Bestellung und liegen außerhalb der akzeptierten Toleranz; sie sind nicht genehmigt. | Die Rechnung wird in APS110 als nicht genehmigt gebucht. Das AP-Team passt die Zusatzkosten über die Option Invoice Control in APS110 an, die APS360 aufruft.                                                                                                       |
| 7           | Externe Zusatzkosten auf der Bestellung und keine Zusatzkosten auf der Rechnung               | Externe Zusatzkosten sind auf der Bestellung aufgeführt, aber auf der Rechnung gibt es keine Zusatzkosten.                                     | Die Rechnung wird in APS110 als nicht genehmigt gebucht. Das AP-Team passt die Zusatzkosten über die Option Invoice Control in APS110 an, die APS360 aufruft.                                                                                                       |

## Beispiel für Szenario 5

| Feld           | Wert auf der Bestellung | Wert auf der Lieferantenrechnung |
| -------------- | ----------------------- | -------------------------------- |
| Zeile 1        | 6.000 $                 | 6.000 $                          |
| Fracht (E001)  | 1.000 $                 | 3.000 $                          |
| **Summe**      | 7.000 $                 | 9.000 $                          |

**Toleranz für Fracht:** 100 $ werden in M3 (APS900) und DocBits automatisch genehmigt. Der Gesamtrechnungswert von 9.000 $ wird (mit Zusatzkosten) manuell genehmigt.

**APS451 (Rechnungszeile):**

* Zeilentyp 1 (Rechnungszeile): 9.000 $
* Zeilentyp 5 (Zeilen-Zusatzkosten): 1.000 $ (Element: E001 für Fracht auf der Bestellung 1.000 $)
* Zeilentyp 5 (Zeilen-Zusatzkosten): 2.000 $ (Element: E101 für Fracht auf der Bestellung 0 $)

### Wichtige Felder und Werte für den Umgang mit Zusatzkosten in DocBits

| Feld                        | Beschreibung                                                          |
| --------------------------- | --------------------------------------------------------------------- |
| Sequence Number             | Eindeutige Kennung für jedes Zusatzkosten-Szenario                    |
| Costing Element ID          | Kennung des Kostenelements                                            |
| Costing Element Description | Beschreibung des Kostenelements                                       |
| Charge Type                 | Typischerweise „External“                                             |
| Charge Invoicing            | Relevanz muss noch bestimmt werden                                    |
| Distribution Method         | Methode zur Verteilung der Zusatzkosten                               |
| Gross Weight                | Anwendbar, wenn das Bruttogewicht auf der Rechnung vorhanden ist      |
| Volume                      | Anwendungsfälle müssen noch definiert werden                          |
| Net Amount                  | Anwendungsfälle müssen noch definiert werden                          |
| 3rd Party Charge            | Vorhandensein auf der Rechnung und Verarbeitungsanforderungen         |
| Invoice Charge Quantity     | Klärungsbedarf                                                        |
| Markup                      | Wird als Differenz zwischen Zusatzkosten und Rabatt angenommen        |
| Charge Category             | Relevanz muss noch definiert werden                                   |
| Costing Operator            | Relevanz muss noch definiert werden                                   |

\

