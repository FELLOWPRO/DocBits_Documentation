# Verwijder regels met lege hoeveelheid en bedrag

#### Deel 1: Verwijder Regels met Lege Hoeveelheid en Bedrag

Dit gedeelte van het script verwerkt een factuurtabel om alle regels te verwijderen waar zowel de hoeveelheid als het totaalbedrag nul of niet opgegeven zijn.

* **Controleer INVOICE\_TABLE:** Het begint met controleren of de sleutel `INVOICE_TABLE` bestaat in het woordenboek `tables_dict`.
* **Itereer over Rijen:** Voor elke rij in de tabel initialiseert het script vlaggen en variabelen om te bepalen of de kolommen `TOTAL_AMOUNT` en `QUANTITY` bestaan en om hun waarden vast te leggen.
* **Controleer Kolomnamen:** Tijdens het itereren door elke kolom in een rij zoekt het naar kolommen met de naam `TOTAL_AMOUNT` en `QUANTITY`.
  * Als `TOTAL_AMOUNT` wordt gevonden, legt het de waarde vast. Als deze waarde niet nul is, wordt deze geconverteerd naar een drijvende-kommagetal.
  * Hetzelfde geldt voor `QUANTITY`, waarbij de waarde wordt vastgelegd en geconverteerd als deze niet nul is.
* **Markeer Rij voor Verwijdering:** Na het controleren van beide kolommen in een rij, als zowel het totaalbedrag als de hoeveelheid effectief nul zijn (hetzij door nul te zijn of door niet te bestaan), wordt de rij gemarkeerd voor verwijdering door `row['is_deleted']` op `True` te zetten.

#### Deel 2: Valideer Regeltotaal tegen Factuurtotaal

Dit gedeelte berekent het totaalbedrag van alle regels in een factuur en vergelijkt dit met het gerapporteerde factuurtotaal om hun consistentie te valideren.

* **Initialiseer Regeltotaal:** Begint met het instellen van een variabele `lines_total` op 0.0 om het totaalbedrag van alle regels te accumuleren.
* **Som Regelbedragen:** Itereert over elke rij in de `INVOICE_TABLE`, haalt het `TOTAL_AMOUNT` uit elke rij en voegt dit toe aan `lines_total`.
* **Haal Factuurtotaal Op en Converteer:** Haalt het totale factuurbedrag op met behulp van een hulpfunctie `get_field_value` en converteert het naar een drijvende-kommagetal.
* **Vergelijk Totalen:** Ten slotte controleert het of het absolute verschil tussen het berekende regeltotaal (`lines_total`) en het gerapporteerde factuurtotaal (`total_amount`) een drempel van 0,05 overschrijdt. Als dat zo is, markeert het het veld factuurtotaal als ongeldig met behulp van een andere hulpfunctie `set_field_as_invalid`, met vermelding van een afwijking.

```python
##################################################
# Regels met lege hoeveelheid en bedrag verwijderen
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
# Einde: Regels met lege hoeveelheid en bedrag verwijderen
##################################################

##################################################
# Regeltotaal valideren tegen factuurtotaal
##################################################
lines_total = 0.0
# Regeltotalen ophalen
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

# Factuurtotaal ophalen
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Regeltotalen vergelijken met factuurtotaal
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Einde: Regeltotaal valideren tegen factuurtotaal
##################################################





```

#### Samenvatting

Het script zorgt effectief voor gegevensintegriteit door:

1. Gegevensrijen te verwijderen die niet bijdragen aan het financiële totaal van de factuur vanwege ontbrekende hoeveelheden of bedragen.
2. De consistentie te valideren tussen de som van individuele regelbedragen en het totale factuurtotaal, waarbij afwijkingen worden gemarkeerd voor verdere actie.

Deze automatisering helpt bij het onderhouden van nauwkeurige financiële gegevens en kan cruciaal zijn voor systemen zoals ERP die nauwkeurige gegevens vereisen voor boekhouding en financiële rapportage.


