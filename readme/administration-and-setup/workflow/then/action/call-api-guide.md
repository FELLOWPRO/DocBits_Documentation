# Wywołaj zewnętrzny interfejs API

***

Dodaj tę kartę do grupy **Wtedy** Kreatora przepływu pracy — akcje, które zostaną uruchomione po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

## 📌 Informacje o wersji

**Aktualna wersja:** v2 (najnowsza i zalecana) **Stan:** ✅Aktywny

**Historia wersji:**

* v1 → Podstawowe wywołanie API (nie jest już zalecane)
* **v2 → AKTUALNY** (dodano obsługę wielu języków)

**Co się zmieniło:** wersja 2 dodała obsługę internacjonalizacji (i18n) z kluczami tłumaczeniowymi. Funkcjonalność pozostaje identyczna.

📖 [Historia wersji i zmiany](../../release.md) | [Kompletna baza danych kart](../../cards-overview/export-cards-guide.md)

***

## Cel

Karta ta umożliwia przesyłanie danych do zewnętrznej strony internetowej lub usługi i otrzymywanie informacji zwrotnych. Pomyśl o tym jak o wysłaniu pytania do usługi zewnętrznej i uzyskaniu odpowiedzi, którą możesz wykorzystać w swoim przepływie pracy.

**Przykład z życia codziennego:** Twoja firma korzysta z systemu cenowego na innej stronie internetowej. Ta karta może automatycznie zapytać system cenowy o aktualną cenę przedmiotu i wprowadzić tę cenę do Twojego dokumentu.

***

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:

* Uzyskaj informacje z usługi zewnętrznej (takie jak dane dotyczące cen, weryfikacji lub wyszukiwania)
* Wyślij informacje o dokumencie do innego systemu w celu przetworzenia
* Integruj z usługami stron trzecich
* Automatycznie pobieraj dane bez ręcznego wyszukiwania
* Połącz ze sobą wiele systemów biznesowych

**Typowe scenariusze:**

* Wyszukaj informacje o dostawcach w bazie danych
* Otrzymuj ceny w czasie rzeczywistym za pomocą usługi wyceny
* Zweryfikuj dane w systemie zewnętrznym
* Pobierz informacje o wysyłce od dostawcy usług logistycznych

***

## Jak to działa

1. **Sprawdzanie warunku**: Przepływ pracy sprawdza najpierw, czy spełnione są warunki w sekcjach „Kiedy” i „I”
2. **Przygotuj dane**: Karta zbiera skonfigurowane parametry
3. **Wyślij żądanie**: Wysyła Twoje dane do zewnętrznego API/usługi
4. **Odbierz odpowiedź**: Usługa zewnętrzna odpowiada danymi
5. **Kontynuuj**: Przepływ pracy wykorzystuje te dane w kolejnych kartach

***

## Parametry wyjaśnione

### Adres URL punktu końcowego interfejsu API

**Co to jest:** Adres usługi zewnętrznej, z którą chcesz się komunikować

**Przykład:** `https://api.supplier-system.com/product/pricing`

**Jak to znaleźć:** Zapytaj swój zespół IT lub dostawcę usług o punkt końcowy API

***

### Metoda HTTP

**Co to jest:** Typ żądania do wysłania

**Opcje:**

* **GET**: Poproś o informacje (np. zadając pytanie)
* **POST**: Wyślij nowe dane
* **PUT**: Aktualizuj istniejące dane
* **DELETE**: Usuń dane

**Najczęstsze:** GET (do pobierania informacji)

***

### Nagłówki

**Co to jest:** Dodatkowe instrukcje dotyczące usługi, do której dzwonisz

**Przykład:**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Dlaczego jest to potrzebne:** Usługi często wymagają uwierzytelnienia lub instrukcji dotyczących określonego formatu

***

### Parametry (parametry zapytania)

**Co to jest:** Dodatkowe informacje przekazywane w adresie URL

**Przykład:**

```
?supplier_id=12345&currency=USD
```

**Prawdziwy przykład:** Jeśli pytasz o ceny, parametry mogą obejmować identyfikator dostawcy i walutę

***

### Dane żądania (treść)

**Co to jest:** Informacje, które wysyłasz do usługi

**Przykład:**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**W przypadku użycia:** W przypadku stosowania metod POST lub PUT

***

## Przykład krok po kroku

### Scenariusz: Uzyskaj ceny dostawców w czasie rzeczywistym

**Konfiguracja:**

1. **Typ karty:** Wywołaj API
2. **Punkt końcowy interfejsu API:** `https://api.suppliers.com/v1/prices`
3. **Metoda:** POST
4. **Nagłówki:** `Authorization: Bearer YOUR-API-KEY`
5.  **Zażądaj danych:**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**Co się dzieje:**

1. Przychodzi dokument z identyfikatorem produktu: ABC123, ilość: 100
2. Karta wysyła żądanie do API dostawcy
3. API dostawcy odpowiada: `{"unit_price": 25.50, "total_price": 2550}`
4. Przepływ pracy jest kontynuowany z tymi informacjami o cenach
5. Następna karta może wykorzystać te dane do sprawdzenia ceny na fakturze

***

## Kroki konfiguracji

### 1. Uzyskaj informacje API

Skontaktuj się z zewnętrznym usługodawcą i poproś:

* [ ] Adres URL punktu końcowego interfejsu API
* [ ] Metoda uwierzytelnienia (klucz API, nazwa użytkownika/hasło, OAuth)
* [ ] Wymagane parametry
* [ ] Oczekiwany format odpowiedzi
* [ ] Limity stawek lub kwoty

### 2. Skonfiguruj kartę

1. Wprowadź adres URL punktu końcowego interfejsu API
2. Wybierz metodę HTTP (zwykle GET lub POST)
3. W razie potrzeby dodaj nagłówki uwierzytelniające
4. Dodaj wszelkie wymagane parametry
5. W razie potrzeby sformatuj dane żądania jako JSON

### 3. Przetestuj kartę

1. Użyj dokumentu testowego
2. Uruchom przepływ pracy
3. Sprawdź, czy odpowiedź została otrzymana prawidłowo
4. Sprawdź, czy format danych odpowiada oczekiwaniom

***

## Typowe scenariusze reakcji

### Pomyślna odpowiedź (kod stanu 200)

```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```

✅ Dane są dostępne do wykorzystania przez kolejne karty

### Odpowiedź na błąd (kod stanu 404)

```json
{
  "error": "Product not found"
}
```

⚠️ Interfejs API nie mógł znaleźć tego, czego szukasz

### Limit czasu

Usługa zewnętrzna nie odpowiedziała w terminie ⚠️ Sprawdź, czy usługa jest dostępna lub czy adres URL punktu końcowego jest poprawny

***

## Przykładowe przepływy pracy

### Przykład 1: Automatyczna weryfikacja ceny

**Scenariusz:** Zweryfikuj ceny na fakturze w porównaniu z bieżącymi cenami dostawcy

**Przepływ:**

1. Dokument dociera z pozycją faktury (Produkt: A123, Cena: 50 €)
2. **Zadzwoń do karty API** → Zapytaj dostawcę API: „Jaka jest aktualna cena za A123?”
3. Dostawca odpowiada: „48 €”
4. **Karta stanu** → Sprawdza, czy cena na fakturze (50€) mieści się w granicach 5% aktualnej ceny (48€)
5. **Karta zatwierdzenia** → Zatwierdza, jeśli mieści się w tolerancji

### Przykład 2: Automatyczne wyszukiwanie dostawców

**Scenariusz:** Uzyskaj podstawowe dane dostawcy z centralnej bazy danych

**Przepływ:**

1. Dochodzi faktura z kodem dostawcy: SUPP-789
2. **Zadzwoń do karty API** → System pyta: „Podaj mi dane dostawcy SUPP-789”
3. System odpowiada: Imię, Kontakt, Warunki itp.
4. **Ustaw karty pól** → Wypełnij pola dokumentu tymi danymi
5. **Karta eksportowa** → Eksportuj z pełnymi informacjami

### Przykład 3: Koszty wysyłki w czasie rzeczywistym

**Scenariusz:** Uzyskaj automatyczny koszt wysyłki na podstawie miejsca docelowego

**Przepływ:**

1. Dokument zawiera adres dostawy
2. **Karta API** → Zapytaj dostawcę usług spedycyjnych: „Jaki jest koszt dotarcia do \[adres]?”
3. Dostawca odpowiada kosztem wysyłki
4. **Oblicz kartę** → Dodaj wysyłkę do całkowitej kwoty faktury
5. **Karta eksportu** → Wyślij ze zaktualizowaną sumą

***

## Rozwiązywanie problemów

### Błąd „Przekroczono limit czasu połączenia”.

**Przyczyna:** Usługa API nie odpowiada

**Rozwiązania:**

* [ ] Sprawdź dostępność usługi (odwiedź stronę)
* [ ] Sprawdź, czy adres URL punktu końcowego jest poprawny (bez literówek)
* [ ] Sprawdź połączenie internetowe
* [ ] Skontaktuj się z usługodawcą
* [ ] Sprawdź, czy usługa ma limity stawek (wysyłasz za dużo żądań)

### Błąd „Nieautoryzowany” lub „403 zabroniony”.

**Przyczyna:** Uwierzytelnienie nie powiodło się

**Rozwiązania:**

* [ ] Sprawdź, czy Twój klucz API jest poprawny
* [ ] Sprawdź, czy Twój klucz API nie wygasł
* [ ] Upewnij się, że nagłówek uwierzytelniania jest poprawnie sformatowany
* [ ] Sprawdź, czy masz uprawnienia do tego punktu końcowego

### „Złe żądanie” lub „Błąd 400”

**Przyczyna:** Format danych żądania jest nieprawidłowy

**Rozwiązania:**

* [ ] Sprawdź składnię JSON (brakujące przecinki, cudzysłowy itp.)
* [ ] Sprawdź, czy wszystkie wymagane pola zostały uwzględnione
* [ ] Sprawdź, czy nazwy parametrów odpowiadają oczekiwaniom usługi
* [ ] Zapoznaj się z dokumentacją API

### „Odpowiedź nie działa zgodnie z oczekiwaniami”

**Rozwiązania:**

* [ ] Przetestuj interfejs API za pomocą narzędzia takiego jak Postman
* [ ] Porównaj aktualny format odpowiedzi z oczekiwanym formatem
* [ ] Sprawdź, czy dokumentacja API uległa zmianie
* [ ] Sprawdź, czy wysyłane dane są prawidłowe

***

## Wykorzystanie danych odpowiedzi

Gdy już odzyskasz dane z API, będą mogły z nich korzystać kolejne karty:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

***

## Uwagi dotyczące bezpieczeństwa

⚠️ **Ważne:** Nigdy nie umieszczaj w konfiguracji karty poufnych informacji, które mogą być widoczne dla innych użytkowników

* Nie szyfruj haseł na stałe
* Bezpiecznie korzystaj z kluczy API
* Nie wpisuj danych osobowych w logach
* Użyj punktów końcowych HTTPS (nie HTTP)

***

## Wskazówki i najlepsze praktyki

✅ **Wykonaj:**

* Najpierw przetestuj na małej próbce dokumentów
* Staraj się, aby wywołania API były proste i skoncentrowane
* Dodaj obsługę błędów za pomocą kart warunków
* Monitoruj wykorzystanie/koszty API
* Udokumentuj wymagania API dla swojego zespołu

❌ **Nie:**

* Wywołuj interfejsy API dla każdego pojedynczego żądania, jeśli możesz buforować dane
* Ignoruj kody błędów odpowiedzi
* Używaj testowych interfejsów API w środowisku produkcyjnym
* Zapomnij o dodaniu nagłówków uwierzytelniających
* Załóżmy, że interfejs API będzie zawsze dostępny

***

## Powiązane karty

* **ACTION\_HTTPS\_REQUEST** — podobne, ale prostsze żądania HTTPS
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Sprawdź, czy wywołanie API powiodło się
* **ACTION\_SEND\_EMAIL** – Wysyłaj dane e-mailem zamiast API
* **CALL\_API** (inna wersja) - Alternatywna metoda wywołania API

***

## Potrzebujesz pomocy?

* Poproś swój zespół IT/integratorów o dokumentację API
* Użyj narzędzia Postman, aby najpierw przetestować punkty końcowe API
* Sprawdź portal wsparcia usługodawcy
* Przejrzyj dokumentację interfejsu API pod kątem wymaganych formatów
