# Zadanie dla Wysokiej Kwoty Faktury

## Co robi ten skrypt?

Tworzy zadanie zatwierdzenia gdy suma faktury przekracza próg (np. 100 000). Zadanie jest przypisywane do grupy "Finance Approval" i wyzwala powiadomienie e-mail w celu zapewnienia terminowego przeglądu.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj kwotę całkowitą z dokumentu
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Znajdź grupę Finance Approval po nazwie
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Utwórz zadanie zatwierdzenia
        create_document_task(
            user,
            document_data,
            title="Kwota > 100 000 - Wymagane zatwierdzenie",
            description=f"Kwota całkowita: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Wyjaśnienie krok po kroku

1. **Odczytaj kwotę całkowitą** z dokumentu
2. **Sprawdź próg** — kontynuuj tylko jeśli kwota przekracza 100 000
3. **Znajdź grupę** po nazwie za pomocą `get_group_by_name()` aby dynamicznie uzyskać ID grupy
4. **Utwórz zadanie** przypisane do grupy finansowej z wysokim priorytetem i powiadomieniem e-mail

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt wartości pola
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Wyszukanie grupy po nazwie
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Tworzenie zadania zatwierdzenia
