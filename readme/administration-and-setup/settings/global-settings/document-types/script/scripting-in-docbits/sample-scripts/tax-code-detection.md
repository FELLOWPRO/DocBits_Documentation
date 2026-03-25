# Wykrywanie Kodu Podatkowego

## Co robi ten skrypt?

Automatycznie określa prawidłowy kod podatkowy na podstawie pełnego tekstu dokumentu oraz kwot podatku/netto. Wykrywa scenariusze odwrotnego obciążenia, faktury wolne od podatku i oblicza stawkę podatkową w celu przypisania odpowiedniego kodu (np. S1 dla 19%, S2 dla 7%).

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Pobierz pełny tekst dokumentu i kwoty
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Reguła 1: Wykrywanie odwrotnego obciążenia przez pełny tekst
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Reguła 2: Zerowy podatek = wolny od podatku
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Reguła 3: Oblicz stawkę podatkową z kwot
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Stawka standardowa
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Stawka obniżona
    else:
        set_field_value(document_data, "tax_code", "S3")    # Inna stawka
```

## Wyjaśnienie krok po kroku

1. **Odczytaj pełny tekst** za pomocą `get_document_content()` do wykrywania słów kluczowych
2. **Odczytaj kwoty podatku i netto** do obliczenia stawki podatkowej
3. **Sprawdź odwrotne obciążenie** — szukaj słów kluczowych w tekście dokumentu (po niemiecku i angielsku)
4. **Sprawdź zerowy podatek** — jeśli kwota podatku wynosi 0, przypisz kod wolny od podatku
5. **Oblicz stawkę podatkową** ze stosunku podatek/netto i przypisz odpowiedni kod

## Użyte funkcje

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Odczyt pełnego tekstu OCR
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt wartości pól
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Ustawienie kodu podatkowego
