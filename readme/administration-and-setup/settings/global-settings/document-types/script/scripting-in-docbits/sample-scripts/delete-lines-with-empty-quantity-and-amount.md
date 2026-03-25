# Brisanje redova sa praznom kolicinom i iznosom

#### Deo 1: Brisanje redova sa praznom kolicinom i iznosom

Ovaj deo skripte obradjuje tabelu fakture kako bi uklonio sve redove u kojima su i kolicina i ukupni iznos jednaki nuli ili nisu navedeni.

* **Provera INVOICE\_TABLE:** Pocinje proverom da li kljuc `INVOICE_TABLE` postoji u recniku `tables_dict`.
* **Iteracija kroz redove:** Za svaki red u tabeli, skripta inicijalizuje indikatore i varijable da utvrdi da li kolone `TOTAL_AMOUNT` i `QUANTITY` postoje i da preuzme njihove vrednosti.
* **Provera naziva kolona:** Dok iterira kroz svaku kolonu u redu, trazi kolone po imenu `TOTAL_AMOUNT` i `QUANTITY`.
  * Ako se pronadje `TOTAL_AMOUNT`, preuzima vrednost. Ako je ova vrednost razlicita od nule, konvertuje je u decimalni broj.
  * Slicno za `QUANTITY`, preuzima i konvertuje vrednost ako je razlicita od nule.
* **Oznacavanje reda za brisanje:** Nakon provere obe kolone u redu, ako su i ukupni iznos i kolicina efektivno nula (ili su nula ili ne postoje), red se oznacava za brisanje postavljanjem `row['is_deleted']` na `True`.

#### Deo 2: Validacija ukupnog iznosa stavki naspram ukupnog iznosa fakture

Ovaj deo izracunava ukupni iznos iz svih stavki fakture i uporedjuje ga sa prijavljenim ukupnim iznosom fakture kako bi se validirala njihova konzistentnost.

* **Inicijalizacija ukupnog iznosa stavki:** Pocinje postavljanjem varijable `lines_total` na 0.0 za akumuliranje ukupnog iznosa iz svih stavki.
* **Sabiranje iznosa stavki:** Iterira kroz svaki red u `INVOICE_TABLE`, izdvajajuci `TOTAL_AMOUNT` iz svakog i dodajuci ga u `lines_total`.
* **Preuzimanje i konverzija ukupnog iznosa fakture:** Preuzima ukupni iznos fakture koriscenjem pomocne funkcije `get_field_value` i konvertuje ga u decimalni broj.
* **Poredjenje ukupnih iznosa:** Na kraju, proverava da li apsolutna razlika izmedju izracunatog ukupnog iznosa stavki (`lines_total`) i prijavljenog ukupnog iznosa fakture (`total_amount`) prelazi prag od 0.05. Ako je tako, oznacava polje ukupnog iznosa fakture kao nevazece koriscenjem pomocne funkcije `set_field_as_invalid`, navodeci neslaganje.

```python
##################################################
# Brisanje redova sa praznom kolicinom i iznosom
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
# Kraj: Brisanje redova sa praznom kolicinom i iznosom
##################################################

##################################################
# Validacija ukupnog iznosa stavki naspram ukupnog iznosa fakture
##################################################
lines_total = 0.0
# Preuzimanje ukupnog iznosa stavki
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

# Preuzimanje ukupnog iznosa fakture
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Poredjenje ukupnog iznosa stavki sa ukupnim iznosom fakture
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Kraj: Validacija ukupnog iznosa stavki naspram ukupnog iznosa fakture
##################################################





```

#### Rezime

Skripta efikasno osigurava integritet podataka kroz:

1. Uklanjanje redova podataka koji ne doprinose finansijskom ukupnom iznosu fakture zbog nedostatka kolicina ili iznosa.
2. Validaciju konzistentnosti izmedju zbira pojedinacnih iznosa stavki i ukupnog iznosa fakture, isticuci neslaganja za dalju akciju.

Ova automatizacija pomaze u odrzavanju tacnih finansijskih zapisa i moze biti kljucna za sisteme poput ERP-a koji zahtevaju precizne podatke za racunovodstvo i finansijsko izvestavanja.

