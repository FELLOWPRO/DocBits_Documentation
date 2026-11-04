# Löschen von Zeilen mit leerer Menge und Betrag

#### Teil 1: Löschen von Zeilen mit leerer Menge und Betrag

Dieser Abschnitt des Skripts verarbeitet eine Rechnungstabelle, um alle Zeilen zu entfernen, bei denen sowohl die Menge als auch der Gesamtbetrag null oder nicht angegeben sind.

* **Überprüfen von INVOICE\_TABLE:** Es beginnt mit der Überprüfung, ob der Schlüssel `INVOICE_TABLE` im Wörterbuch `tables_dict` existiert.
* **Iteration über Zeilen:** Für jede Zeile in der Tabelle initialisiert das Skript Flags und Variablen, um festzustellen, ob die Spalten `TOTAL_AMOUNT` und `QUANTITY` existieren und erfasst ihre Werte.
* **Überprüfen der Spaltennamen:** Während es jede Spalte in einer Zeile durchläuft, sucht es nach den Spalten mit den Namen `TOTAL_AMOUNT` und `QUANTITY`.
* Wenn `TOTAL_AMOUNT` gefunden wird, erfasst es den Wert. Wenn dieser Wert ungleich null ist, wird er in eine Gleitkommazahl konvertiert.
* Ähnlich für `QUANTITY`, Erfassung und Konvertierung des Werts, wenn er ungleich null ist.
* **Zeile für Löschung markieren:** Nach Überprüfung beider Spalten in einer Zeile, wenn sowohl der Gesamtbetrag als auch die Menge effektiv null sind (entweder durch null oder nicht vorhanden), wird die Zeile für die Löschung markiert, indem `row['is_deleted']` auf `True` gesetzt wird.

#### Teil 2: Überprüfen der Gesamtzeile gegen die Gesamtrechnung

Dieser Abschnitt berechnet den Gesamtbetrag aus allen Zeilen einer Rechnung und vergleicht ihn mit dem gemeldeten Gesamtbetrag der Rechnung, um deren Konsistenz zu überprüfen.

* **Initialisieren des Gesamtzeilenbetrags:** Beginnt mit dem Setzen einer Variablen `lines_total` auf 0.0, um den Gesamtbetrag aus allen Zeilen zu akkumulieren.
* **Summe der Zeilenbeträge:** Iteriert über jede Zeile in der `INVOICE_TABLE`, extrahiert den `TOTAL_AMOUNT` aus jeder Zeile und fügt ihn zu `lines_total` hinzu.
* **Abrufen und Konvertieren des Rechnungsgesamtbetrags:** Holt den Gesamtbetrag der Rechnung mithilfe einer Hilfsfunktion `get_field_value` und konvertiert ihn in eine Gleitkommazahl.
* **Vergleichen der Beträge:** Schließlich wird überprüft, ob der absolute Unterschied zwischen dem berechneten Gesamtzeilenbetrag (`lines_total`) und dem gemeldeten Rechnungsgesamtbetrag (`total_amount`) einen Schwellenwert von 0,05 überschreitet. Wenn ja, markiert es das Feld des Rechnungsgesamtbetrags als ungültig mithilfe einer anderen Hilfsfunktion `set_field_as_invalid`, unter Angabe eines Missverhältnisses.
```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
amount_col_found = False
quantity_col_found = False
line_amount = 0.0
line_quantity = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
amount_col_found = True
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
if col['name'] == 'QUANTITY':
quantity_col_found = True
line_quantity = col.get('value', 0)
if line_quantity:
line_quantity = float(line_quantity)
if amount_col_found and quantity_col_found:
break
if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
line_amount = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
break
lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################







```
#### Zusammenfassung

Das Skript gewährleistet die Datenintegrität effektiv, indem es:

1. Datensätze entfernt, die nicht zum finanziellen Gesamtbetrag der Rechnung beitragen, da sie keine Mengen oder Beträge enthalten.
2. Die Konsistenz zwischen der Summe der einzelnen Positions­beträge und dem Gesamtbetrag der Rechnung validiert und Abweichungen für weitere Maßnahmen hervorhebt.

Diese Automatisierung hilft dabei, genaue Finanzdatensätze zu pflegen und kann für Systeme wie ERP entscheidend sein, die präzise Daten für Buchhaltung und Finanzberichterstattung erfordern.
