# Wzorzec dopasowania zamówienia zakupu (PO)

**Typ wzorca:** Walidacja i porównanie
**Złożoność:** Średnia-Wysoka
**Szacowany czas konfiguracji:** 60-90 minut
**Typowe przypadki użycia:** Dopasowanie trójdrożne, walidacja faktur, sprawdzanie odchyleń, zarządzanie tolerancją

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak wdrażać kompleksowe przepływy pracy dopasowywania zamówień zakupu (PO) w DocBits. Dopasowanie PO jest krytycznym procesem kontrolnym, który porównuje dane faktury z danymi zamówienia zakupu w celu wykrycia rozbieżności przed zatwierdzeniem płatności.

**Co robi ten wzorzec:**
1. Pobiera dane PO na podstawie numeru PO z faktury
2. Porównuje pozycje linii faktury z pozycjami linii PO
3. Oblicza odchylenia (cena, ilość, sumy)
4. Stosuje zasady tolerancji
5. Kieruje do zatwierdzenia lub eskalacji na podstawie wyników dopasowania
6. Śledzi historię dopasowań i wyjątki

---

## Kiedy używać tego wzorca

Użyj tego wzorca, gdy musisz:
- ✅ Walidować faktury względem zamówień zakupu
- ✅ Wykrywać błędy cenowe przed płatnością
- ✅ Identyfikować rozbieżności w ilościach
- ✅ Egzekwować kontrole zakupowe
- ✅ Zapobiegać powielaniu płatności
- ✅ Zautomatyzować trójdrożne dopasowanie
- ✅ Zmniejszyć nakład pracy przy ręcznym przeglądzie faktur

---

## Formuły obliczania odchyleń

### Odchylenie ceny jednostkowej

**Formuła:**
```
Odchylenie % = |(Cena jednostkowa faktury - Cena jednostkowa PO)| / Cena jednostkowa PO × 100
```

**Przykład:**
```
Cena PO: 100,00 PLN
Cena faktury: 103,00 PLN
Odchylenie = 3%
Tolerancja: 5%
Wynik: 3% ≤ 5% → SUKCES ✅
```

---

## Wdrażanie krok po kroku

### Krok 1: Sprawdź referencję PO

**Karta:** CONDITION_DOC_FIELD_EXISTS

**Konfiguracja:**
```
Pole: Numer_PO
Operator: NIE JEST PUSTE
```

---

### Krok 2: Pobierz dane PO

**Automatycznie w DocBits:**
- System wyszukuje PO według numeru w polu Numer_PO
- Pobiera pozycje linii PO
- Udostępnia dane do porównania

---

### Krok 3: Sprawdzenie pełnego dopasowania PO

**Karta:** PURCHASE_ORDER_FULL_MATCH

**Cel:** Szybkie sprawdzenie, czy wszystko zgadza się idealnie

---

### Krok 4: Sprawdź odchylenie ceny jednostkowej

**Karta:** CONDITION_DOC_TO_PO_UNIT_PRICE

**Konfiguracja:**
```
Tryb porównania: Odchylenie procentowe
Tolerancja: 5%
```

---

## Lista kontrolna testów

- [ ] Scenariusz idealnego dopasowania (pełne dopasowanie)
- [ ] Scenariusz w granicach tolerancji (małe odchylenie)
- [ ] Scenariusz poza granicami tolerancji (duże odchylenie)
- [ ] Scenariusz brakującego zamówienia PO
- [ ] Scenariusz błędnego numeru PO
- [ ] Scenariusz dostawy częściowej
- [ ] Scenariusz nadwyżki dostawy
- [ ] Powiadomienia e-mail
- [ ] Aktualizacje pól

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.
**Trudność:** Średnia-Wysoka
