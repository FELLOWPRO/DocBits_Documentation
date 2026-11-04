# Wzorzec transformacji danych

**Typ wzorca:** Przetwarzanie i manipulacja danymi
**Złożoność:** Średnia
**Szacowany czas konfiguracji:** 30-45 minut
**Typowe przypadki użycia:** Obliczenia pól, formatowanie danych, konwersja walut, konwersja jednostek, wzbogacanie danych

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak transformować, obliczać, formatować i wzbogacać dane dokumentów w przepływach pracy DocBits. Transformacja danych jest niezbędna do przygotowania danych do eksportu, wykonywania obliczeń, standaryzacji formatów i wzbogacania dokumentów o dodatkowe informacje.

**Co robi ten wzorzec:**
1. Wyodrębnia dane z pól dokumentu
2. Wykonuje obliczenia i transformacje
3. Formatuje dane zgodnie z wymaganymi standardami
4. Konwertuje jednostki, waluty, daty
5. Wzbogaca dokumenty o dane wyliczone lub pobrane
6. Waliduje i oczyszcza dane

---

## Kiedy używać tego wzorca

Użyj tego wzorca, gdy musisz:
- ✅ Obliczać sumy, sumy częściowe, podatki
- ✅ Konwertować waluty lub jednostki
- ✅ Formatować daty, liczby, tekst
- ✅ Wyliczać wartości z istniejących pól
- ✅ Wzbogacać dane z zewnętrznych źródeł
- ✅ Standaryzować formaty danych
- ✅ Czyścić i walidować dane
- ✅ Przygotować dane do eksportu

---

## Typy transformacji danych

### 1. Obliczenia

**Operacje matematyczne:**
```
- Dodawanie: Ilość + Ilość_Bonusowa = Ilość_Całkowita
- Odejmowanie: Suma_Faktury - Kwota_Podatku = Kwota_Netto
- Mnożenie: Ilość × Cena_Jednostkowa = Suma_Linii
- Dzielenie: Kwota_Całkowita / Ilość = Cena_Jednostkowa
```

### 2. Operacje na ciągach znaków (String)

**Manipulacja tekstem:**
```
- Łączenie: Imię + " " + Nazwisko = Pełne_Imię
- Wielkie litery: "faktura" → "FAKTURA"
- Wycinanie: "INV-2025-001" → "2025"
```

---

## Przykładowe wdrożenie krok po kroku

### Krok 1: Obliczenia pozycji linii

**Oblicz sumy linii:**

**Karta:** ACTION_CALCULATE_FIELD

**Dla każdej pozycji:**
```
Pole: Suma_Linii
Formuła: {{TABLE_FIELD:Ilosc}} * {{TABLE_FIELD:Cena_Jednostkowa}}
Typ wyniku: Liczba
Miejsca dziesiętne: 2
```

---

### Krok 2: Oblicz sumę częściową dokumentu

**Karta:** ACTION_CALCULATE_FIELD

**Konfiguracja:**
```
Pole: Obliczona_Suma_Czesciowa
Formuła: SUM({{TABLE_COLUMN:Suma_Linii}})
Typ wyniku: Liczba
```

---

### Krok 3: Konwersja walut (jeśli potrzebna)

**Karta:** CALL_API

**Pobierz kurs:**
```
Punkt końcowy: https://api.exchangerate-api.com/v4/latest/{{Waluta_Faktury}}
Ścieżka odpowiedzi: rates.PLN
Zapisz w: Kurs_Wymiany_PLN
```

---

## Lista kontrolna testów

- [ ] Wszystkie obliczenia dają poprawne wyniki
- [ ] Zachowana precyzja dziesiętna
- [ ] Konwersje walut są dokładne
- [ ] Obliczenia dat są poprawne
- [ ] Transformacje tekstu działają
- [ ] Obsługa wartości pustych (null)
- [ ] Zabezpieczenie przed dzieleniem przez zero
- [ ] Walidacja formatów liczb
- [ ] Prawidłowo zastosowane zasady zaokrąglania
- [ ] Wszystkie przetransformowane pola są wypełnione
- [ ] Walidacja wyłapuje błędy
- [ ] Format eksportu jest prawidłowy

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.
**Trudność:** Średnia
