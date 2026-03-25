# Auto-Eksport na Podstawie Warunków

## Co robi ten skrypt?

Automatycznie ustawia status dokumentu na "gotowy do eksportu" gdy spełnione są określone warunki: dostawca jest znanym/zaufanym dostawcą ORAZ kwota faktury jest poniżej progu. Pomija to ręczną walidację dla faktur niskiego ryzyka.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj odpowiednie pola
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Zdefiniuj zaufanych dostawców do auto-eksportu
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-eksport dla znanych dostawców z małymi kwotami
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-eksport (mała kwota, znany dostawca)"
    )
```

## Wyjaśnienie krok po kroku

1. **Odczytaj kwotę netto i nazwę dostawcy** z dokumentu (dostawca z `is_clean=True` do porównania)
2. **Zdefiniuj zaufanych dostawców** — lista znanych nazw dostawców (oczyszczone/wielkie litery)
3. **Sprawdź warunki** — dostawca musi być na liście zaufanych ORAZ kwota musi być poniżej 500
4. **Zmień status** na `"ready_for_export"` z opisowym komunikatem

{% hint style="warning" %}
**Uwaga:** Zmiany statusu wyzwalają dalsze przepływy pracy (DocFlow, hooki eksportu). Upewnij się, że warunki są wystarczająco restrykcyjne, aby uniknąć niezamierzonych eksportów.
{% endhint %}

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt wartości pól
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Zmiana statusu dokumentu
