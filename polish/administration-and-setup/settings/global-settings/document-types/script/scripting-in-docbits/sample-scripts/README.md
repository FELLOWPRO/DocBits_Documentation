# Przykładowe Skrypty

Gotowe do użycia przykłady skryptów dla typowych przypadków automatyzacji w DocBits. Każdy przykład zawiera pełny skrypt, wyjaśnienie krok po kroku oraz odnośniki do użytych funkcji.

## Przykłady według zastosowania

### Walidacja danych
- [Walidacja Dostawcy przez Lookup](lookup-supplier-validation.md) — Walidacja dostawcy względem danych podstawowych
- [Walidacja Sumy Tabeli](table-sum-validation.md) — Weryfikacja zgodności sum pozycji z kwotą netto

### Automatyzacja
- [Automatyczne Dopasowanie ZZ](auto-po-matching.md) — Uruchomienie automatycznego dopasowania zamówień zakupu
- [Auto-Eksport na Podstawie Warunków](status-auto-export.md) — Pomijanie walidacji dla faktur niskiego ryzyka
- [Obliczanie Terminu Płatności](due-date-calculation.md) — Obliczanie warunków płatności z pomijaniem weekendów

### Reguły biznesowe
- [Wykrywanie Kodu Podatkowego](tax-code-detection.md) — Określanie kodu podatkowego na podstawie pełnego tekstu i kwot
- [Zadanie dla Wysokiej Kwoty](task-high-amount.md) — Tworzenie zadania zatwierdzenia dla dużych faktur
- [Dynamiczne Pola Wymagane](dynamic-required-fields.md) — Dostosowywanie wymaganych pól na podstawie waluty

### Wyszukiwanie Fulltext i Wektorowe
- [Wykrywanie Duplikatow Faktur](duplicate-invoice-detection.md) — Znajdowanie zduplikowanych faktur za pomoca wyszukiwania fulltext
- [Wykrywanie Podobnych Dokumentow](similar-document-detection.md) — Oznaczanie podobnych dokumentow za pomoca wyszukiwania wektorowego
- [Wyszukiwanie Tekstu Zgodnosci](compliance-text-search.md) — Wyszukiwanie slow kluczowych zgodnosci (np. Reverse Charge)
- [Walidacja Dostawcy ERP](erp-vendor-validation.md) — Walidacja dostawcy wzgledem danych bazowych ERP
- [Uzupelnianie Brakujacych Pol z Historii](fill-missing-fields-from-history.md) — Automatyczne uzupelnianie pol z podobnych wczesniejszych dokumentow

### Starsze przykłady
- [Obliczanie Łącznych Opłat](calculating-total-charges-script-for-docbits-1.md) — Sumowanie kwot frachtu i pakowania
- [Usuwanie Pustych Wierszy](delete-lines-with-empty-quantity-and-amount.md) — Usuwanie wierszy z zerową ilością/kwotą
- [Numery Certyfikatów Eksportowych](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Dopełnianie numerów referencyjnych zerami wiodącymi
- [Rozszerzone Numery Faktur](generating-extended-invoice-numbers-script-for-docbits-1.md) — Łączenie ID faktury i numeru ZZ
- [USD jako Domyślna Waluta](usd-as-default-currency.md) — Ustawienie USD jako domyślnej waluty
