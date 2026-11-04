# Formatowanie skryptu numerów referencyjnych certyfikatu eksportowego dla Docbits

Ten dokument opisuje skrypt "Formatowanie numerów referencyjnych certyfikatu eksportowego", którego celem jest standaryzacja numerów referencyjnych we wszystkich certyfikatach eksportowych w Docbits. Poprawne formatowanie zapewnia, że numery referencyjne spełniają wymagania zewnętrznych systemów lub regulacji.

### Cel

Głównym celem skryptu jest formatowanie numerów referencyjnych na certyfikatach eksportowych, zapewniając, że spełniają one określone wymagania dotyczące długości poprzez wypełnienie ich wiodącymi zerami. Ta spójność pomaga w utrzymaniu standaryzowanego formatu dla wszystkich dokumentów eksportowych przetwarzanych za pomocą Docbits.

### Przegląd skryptu

Skrypt identyfikuje pole `reference_number` w certyfikacie eksportowym, sprawdza jego długość i jeśli jest to konieczne, wypełnia numer wiodącymi zerami, aby zapewnić, że spełnia on minimalne wymagania dotyczące długości.

#### Fragment kodu
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

