# Wzorzec logiki decyzyjnej

**Typ wzorca:** Warunkowy routing i logika
**Złożoność:** Średnia
**Szacowany czas konfiguracji:** 30-45 minut
**Typowe przypadki użycia:** Routing wielościeżkowy, przetwarzanie warunkowe, drzewa decyzyjne, wdrażanie zasad biznesowych

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak wdrażać złożoną logikę decyzyjną w przepływach pracy DocBits przy użyciu kart warunków do kierowania dokumentów przez różne ścieżki przetwarzania w oparciu o atrybuty dokumentu, wartości pól i zasady biznesowe.

**Co robi ten wzorzec:**
1. Ocenia wiele warunków sekwencyjnie lub równolegle
2. Kieruje dokumenty na różne ścieżki w zależności od warunków
3. Wdraża reguły i polityki biznesowe
4. Obsługuje złożone drzewa decyzyjne
5. Łączy wiele kryteriów dla decyzji o routingu

---

## Kiedy używać tego wzorca

Użyj tego wzorca, gdy musisz:
- ✅ Kierować dokumenty według progów kwotowych
- ✅ Stosować różne zasady dla różnych typów dokumentów
- ✅ Wdrażać wielopoziomową logikę zatwierdzania
- ✅ Obsługiwać złożone polityki biznesowe
- ✅ Tworzyć dynamiczny routing oparty na wielu kryteriach
- ✅ Wdrażać macierze zatwierdzania

---

## Typy logiki decyzyjnej

### 1. Prosta logika IF-THEN

```
JEŚLI warunek:
  → Akcja A
W PRZECIWNYM RAZIE:
  → Akcja B
```

### 2. Wiele kryteriów (Logika AND)

```
JEŚLI warunek1 ORAZ warunek2 ORAZ warunek3:
  → Akcja A
```

### 3. Kryteria alternatywne (Logika OR)

```
JEŚLI warunek1 LUB warunek2 LUB warunek3:
  → Akcja A
```

---

## Przykładowe wdrożenie krok po kroku

### Krok 1: Zdefiniuj karty warunków

**Warunek 1: Próg kwotowy**
```
Karta: CONDITION_DOC_FIELD_AMOUNT
Pole: Kwota_Calkowita
Operator: JEST MNIEJSZA NIŻ
Wartość: 1000
Waluta: PLN
```

**Warunek 2: Sprawdzenie typu dokumentu**
```
Karta: CONDITION_DOC_TYPE_IS_ISNOT
Typ dokumentu: JEST
Typ: Faktura
```

---

### Krok 2: Zbuduj drzewo decyzyjne

**Poziom 1: Typ dokumentu**
```
JEŚLI Typ_Dokumentu = „Faktura”:
  → Kontynuuj do Poziomu 2

W PRZECIWNYM RAZIE JEŚLI Typ_Dokumentu = „Nota Kredytowa”:
  → Przejdź do przepływu „Noty Kredytowe”
```

**Poziom 2: Progi kwotowe (dla faktur)**
```
JEŚLI Kwota < 1 000 PLN:
  → Ścieżka „Automatyczne zatwierdzenie”

W PRZECIWNYM RAZIE JEŚLI Kwota < 10 000 PLN:
  → Ścieżka „Zatwierdzenie Menedżera”

W PRZECIWNYM RAZIE:
  → Ścieżka „Zatwierdzenie Dyrektora”
```

---

## Najlepsze praktyki konfiguracji

### 1. Utrzymuj logikę przejrzystą i łatwą w utrzymaniu

✅ **Dobrze:**
```
JEŚLI Kwota > 10000:
  → Ścieżka wysokiej wartości
W PRZECIWNYM RAZIE:
  → Ścieżka standardowa
```

### 2. Testuj wszystkie ścieżki

**Macierz testowa:**

| Przypadek | Kwota | Typ | Dostawca | Oczekiwana ścieżka |
|-----------|--------|------|----------|--------------------|
| TC1 | 500 PLN | Faktura | Istniejący | Autozatwierdzenie |
| TC2 | 5 000 PLN | Faktura | Istniejący | Menedżer |
| TC3 | 15 000 PLN | Faktura | Nowy | Dyrektor+CFO |

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.
**Trudność:** Średnia
