# Skrypt Formatowania Numerów Referencyjnych Certyfikatów Eksportowych dla DocBits

Ten dokument opisuje skrypt „Formatting Export Certificate Reference Numbers", przeznaczony do standaryzacji numerów referencyjnych w certyfikatach eksportowych w DocBits. Właściwe formatowanie zapewnia, że numery referencyjne są zgodne z wymaganiami systemów zewnętrznych lub przepisów.

### Cel

Głównym celem skryptu jest formatowanie numerów referencyjnych w certyfikatach eksportowych, zapewniając, że spełniają one wymagania dotyczące predefiniowanej długości poprzez uzupełnianie ich zerami na początku. Ta spójność pomaga utrzymać ustandaryzowany format dla wszystkich dokumentów eksportowych przetwarzanych przez DocBits.

### Przegląd Skryptu

Skrypt identyfikuje pole `reference_number` w certyfikacie eksportowym, sprawdza jego długość i w razie potrzeby uzupełnia numer zerami na początku, aby zapewnić spełnienie wymagania minimalnej długości.

#### Fragment Kodu

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
