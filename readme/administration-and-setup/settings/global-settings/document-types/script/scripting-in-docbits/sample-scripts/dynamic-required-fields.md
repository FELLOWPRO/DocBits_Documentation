# Dinamicka obavezna polja

## Sta ova skripta radi?

Dinamicki postavlja zahteve za polja na osnovu sadrzaja dokumenta. U ovom primeru: kada valuta fakture nije EUR, polje za kurs postaje obavezno i vidljivo. Za EUR fakture, polje za kurs je skriveno i opciono.

## Okidac

`ON_FIELD_CHANGE` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje trenutne valute
currency = get_field_value(document_data, "currency", "EUR")

# Strana valuta: kurs je obavezan i vidljiv
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: kurs je opcion i skriven
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Varijacija: Nabavna faktura naspram troskovne fakture

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Nabavna faktura: broj narudzbenice je obavezan
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Troskovna faktura: broj narudzbenice nije potreban, sakrij tabelu
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Objasnjenje korak po korak

1. **Citanje kontrolnog polja** (valuta u ovom slucaju)
2. **Primena poslovnih pravila** -- razliciti zahtevi za polja na osnovu vrednosti
3. **Postavljanje vidljivosti** -- sakrivanje irelevantnih polja za cist korisnicki interfejs
4. **Postavljanje zahteva** -- polja koja su relevantna postaju obavezna

{% hint style="info" %}
**Izbor okidaca:** `ON_FIELD_CHANGE` se pokrece svaki put kada korisnik izmeni polje, tako da se zahtevi azuriraju u realnom vremenu. `AFTER_FORMATTING` se pokrece samo jednom posle inicijalne ekstrakcije.
{% endhint %}

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje kontrolnog polja
- [set\_is\_required()](../field-functions.md#set\_is\_required) -- Postavljanje polja kao obaveznog/opcionog
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) -- Prikazivanje/sakrivanje polja
- [set\_field\_value()](../field-functions.md#set\_field\_value) -- Postavljanje polja kategorije
- [delete\_tables()](../table-functions.md#delete\_tables) -- Uklanjanje tabela za troskovne fakture
