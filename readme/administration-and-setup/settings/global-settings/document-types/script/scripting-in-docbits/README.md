# Skriptovanje u DocBits-u

## Vodic za skriptovanje u DocBits-u

Dobrodosli u vodic za skriptovanje u DocBits-u! Ovde cete nauciti kako da koristite skripte za automatizaciju i unapredjenje obrade dokumenata u okviru DocBits-a. Skripte omogucavaju prilagodenu manipulaciju poljima, transformaciju podataka i implementaciju logike na razlicitim tipovima dokumenata.

### Pocetni koraci

Skripte u DocBits-u su napisane u Python-u. One komuniciraju sa poljima dokumenta i metapodacima za obavljanje sirokog spektra operacija, od jednostavnog formatiranja podataka do slozene logike.

#### Kljucne funkcije

* `get_field_value(fields_dict, field_name, default=None)`: Preuzima vrednost navedenog polja.
* `set_field_value(fields_dict, field_name, value)`: Postavlja vrednost navedenog polja.
* `create_new_field(field_name, value)`: Kreira novo polje sa navedenim imenom i vrednoscu.
* `format_decimal_to_locale(value, locale)`: Formatira decimalnu vrednost prema navedenom lokalitetu.

### Primeri skripti

U nastavku je nekoliko primera koji demonstriraju uobicajene zadatke skriptovanja.

#### Primer 1: Mapiranje valuta za fakture

Standardizovanje simbola valuta ili teksta u ISO kodove valuta.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```

