# Leere Zeilen löschen

#### Teil 1: Zeilen mit leerer Menge und Betrag löschen

Dieser Abschnitt des Skripts verarbeitet eine Rechnungstabelle, um alle Zeilen zu entfernen, in denen sowohl die Menge als auch der Gesamtbetrag null oder nicht angegeben sind.

* **Prüfung auf INVOICE\_TABLE:** Es beginnt mit der Prüfung, ob der Schlüssel `INVOICE_TABLE` im Dictionary `tables_dict` existiert.
* **Iteration über Zeilen:** Für jede Zeile in der Tabelle initialisiert das Skript Flags und Variablen, um festzustellen, ob die Spalten `TOTAL_AMOUNT` und `QUANTITY` existieren und deren Werte zu erfassen.
* **Prüfung der Spaltennamen:** Bei der Iteration durch jede Spalte einer Zeile sucht es nach Spalten mit den Namen `TOTAL_AMOUNT` und `QUANTITY`.
  * Wenn `TOTAL_AMOUNT` gefunden wird, erfasst es den Wert. Wenn dieser Wert ungleich null ist, wird er in eine Gleitkommazahl konvertiert.
  * Ebenso für `QUANTITY`, wobei der Wert erfasst und konvertiert wird, wenn er ungleich null ist.
* **Zeile zum Löschen markieren:** Nach der Prüfung beider Spalten in einer Zeile wird, wenn sowohl der Gesamtbetrag als auch die Menge effektiv null sind (entweder durch den Wert null oder durch Nichtexistenz), die Zeile zum Löschen markiert, indem `row['is_deleted']` auf `True` gesetzt wird.

#### Teil 2: Zeilensumme gegen Rechnungssumme validieren

Dieser Abschnitt berechnet den Gesamtbetrag aus allen Zeilen einer Rechnung und vergleicht ihn mit der gemeldeten Rechnungssumme, um deren Konsistenz zu überprüfen.

* **Initialisierung der Zeilensumme:** Beginnt mit dem Setzen einer Variable `lines_total` auf 0.0, um den Gesamtbetrag aus allen Zeilen zu akkumulieren.
* **Summierung der Zeilenbeträge:** Iteriert über jede Zeile in der `INVOICE_TABLE`, extrahiert den `TOTAL_AMOUNT` aus jeder und addiert ihn zu `lines_total`.
* **Abruf und Konvertierung der Rechnungssumme:** Ruft die Gesamtrechnungssumme mit der Hilfsfunktion `get_field_value` ab und konvertiert sie in eine Gleitkommazahl.
* **Vergleich der Summen:** Schließlich prüft es, ob die absolute Differenz zwischen der berechneten Zeilensumme (`lines_total`) und der gemeldeten Rechnungssumme (`total_amount`) einen Schwellenwert von 0,05 überschreitet. Falls ja, markiert es das Rechnungssummenfeld als ungültig mit der Hilfsfunktion `set_field_as_invalid` und gibt eine Abweichung an.

```python
##################################################
# Zeilen mit leerer Menge und Betrag löschen
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
# Ende: Zeilen mit leerer Menge und Betrag löschen
##################################################

##################################################
# Zeilensumme gegen Rechnungssumme validieren
##################################################
lines_total = 0.0
# Zeilensumme ermitteln
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

# Rechnungssumme abrufen
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Zeilensumme mit Rechnungssumme vergleichen
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Ende: Zeilensumme gegen Rechnungssumme validieren
##################################################
```

#### Zusammenfassung

Das Skript gewährleistet effektiv die Datenintegrität durch:

1. Entfernen von Datenzeilen, die aufgrund fehlender Mengen oder Beträge nicht zur finanziellen Summe der Rechnung beitragen.
2. Validierung der Konsistenz zwischen der Summe der einzelnen Zeilenbeträge und der Gesamtrechnungssumme, wobei Abweichungen für weitere Maßnahmen hervorgehoben werden.

Diese Automatisierung hilft, genaue Finanzaufzeichnungen zu führen und kann für Systeme wie ERP, die präzise Daten für Buchhaltung und Finanzberichterstattung benötigen, entscheidend sein.
