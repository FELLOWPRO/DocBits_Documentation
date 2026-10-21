# Uruchom monit DocOperator (skrypt automatyzacji)

***

Dodaj tę kartę do grupy **Wtedy** Kreatora przepływu pracy — akcje, które zostaną uruchomione po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

## 📌 Informacje o wersji

**Aktualna wersja:** v3 (najnowsza i zalecana) **Stan:** ✅Aktywny

**Historia wersji:**

* v2 → Oryginalna implementacja DocOperatora
* **v3 → BIEŻĄCY** (dodano parametr kontroli wykonania)
* v4 → Przestarzałe (przywrócono funkcje)

**Co się zmieniło:** w wersji 3 dodano opcjonalny parametr „Wykonaj monit”, aby zapewnić większą kontrolę. wersja 4 próbowała to przywrócić, ale została przestarzała.

📖 [Historia wersji i zmiany](../../release.md) | [Kompletna baza danych kart](../../cards-overview/export-cards-guide.md)

***

## Cel

Ta karta uruchamia zautomatyzowaną akcję lub skrypt przeglądarki za pomocą DocOperator. Pomyśl o tym jak o robocie, który może wchodzić w interakcję ze stronami internetowymi lub systemami dokładnie tak, jak zrobiłby to człowiek – klikając przyciski, wypełniając formularze, wyodrębniając dane itp.

**Przykład z życia codziennego:** Twoja firma korzysta z internetowego systemu zakupów. Dzięki tej karcie możesz automatycznie zalogować się, wyszukać produkt, sprawdzić dostępność i uzyskać aktualną cenę - a wszystko to bez konieczności robienia tego ręcznie.

***

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:

* Automatyzuj zadania na stronach internetowych, które nie mają interfejsów API
* Wyodrębniaj dane ze stron internetowych
* Wypełniaj formularze automatycznie
* Zaloguj się do systemów i pobierz informacje
* Automatyzuj powtarzalne zadania ręczne
* Interakcja ze starszymi systemami, które nie są zintegrowane

**Typowe scenariusze:**

* Zaloguj się na stronach internetowych dostawców i otrzymuj informacje o zapasach w czasie rzeczywistym
* Automatycznie wypełniaj formularze w systemach zewnętrznych
* Wyodrębnij dane ze stron internetowych, które nie oferują interfejsów API
* Sprawdź status przesyłki na stronach firm kurierskich
* Uzyskaj ceny z systemów bez dostępu do API

***

## Jak to działa

1. **Karta została uruchomiona**: Przepływ pracy dociera do tej karty i warunki są spełnione
2. **Uruchamia się skrypt**: Bot DocOperator rozpoczyna uruchamianie skryptu automatyzacji
3. **Działania bota**: Bot wykonuje czynności takie jak klikanie, pisanie, przewijanie, wyodrębnianie
4. **Wydobywanie danych**: Bot zbiera informacje ze stron internetowych
5. **Return Data**: Dane wracają do DocFlow w celu wykorzystania ich w kolejnych kartach
6. **Obsługa przekroczenia limitu czasu**: Jeśli skrypt trwa zbyt długo, zatrzymuje się i zwraca to, co zrobił

***

## Parametry wyjaśnione

### Podpowiedź/skrypt DocOperatora

Skrypt automatyzacji, który mówi DocOperatorowi dokładnie, co ma robić

**Przykład (zwykły angielski):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Zmienne

Dane, które chcesz przekazać DO skryptu

**Przykład:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Zmienne te mogą być użyte w skrypcie, np.:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maksymalne kroki

Ile akcji może wykonać bot

**Typowe wartości:**

* Proste zadanie (np. uzyskanie jednej ceny): 10-20 kroków
* Średnia złożoność (formularz wypełnienia + wyciąg): 20-50 kroków
* Złożony przepływ pracy (logowanie + wyszukiwanie + sprawdzanie): 50-100 kroków

**Dlaczego to ma znaczenie:** Zapobiega nieskończonym pętlom i bardzo długo działającym skryptom

### Maksymalna liczba ponownych prób

Jeśli bot nie wykona żadnej akcji, ile razy powinien próbować ponownie?

**Przykłady:**

* 1: Spróbuj raz, jeśli się nie uda, przejdź dalej
* 3: Spróbuj 3 razy, zanim się poddasz
* 5: Bardzo wytrwały – spróbuj 5 razy

***

## Przykład krok po kroku

### Scenariusz: pobierz ceny dostawcy ze strony internetowej

**Definicja skryptu:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Przekazane zmienne:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Skrypt wykorzystujący zmienne:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Oczekiwany wynik:**

```
price: 45.50
quantity_available: 500
```

***

## Rodzaje działań, które może wykonać DocOperator

### Nawigacja

* Przejdź do adresu URL
* Kliknij linki
* Naciśnij przyciski
* Przewiń stronę

### Wypełnienie formularza

* Wpisz tekst w polach
* Wybierz opcje rozwijane
* Zaznacz/odznacz pola
* Kliknij przyciski

### Ekstrakcja danych

* Przeczytaj tekst ze strony
* Wyodrębnij liczby
* Pobierz dane tabeli
* Skopiuj informacje

### Czekam

* Poczekaj na załadowanie strony
* Poczekaj, aż pojawią się elementy
* Poczekaj na dynamiczną zawartość

### Logika warunkowa

* Jeśli coś istnieje, zrób to
* Jeśli tekst pasuje, to...
* Licz wyniki i postępuj zgodnie z nimi

***

## Typowe przypadki użycia

### 1. Uzyskaj ceny w czasie rzeczywistym

**Scenariusz:** Dostawca nie ma API, ale strona internetowa pokazuje ceny

**Skrypt:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Sprawdź dostępność zapasów

**Scenariusz:** Trzeba wiedzieć, czy dostawca ma zapasy

**Skrypt:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatyczne przesłanie formularza

**Scenariusz:** Konieczność wypełnienia formularza na stronie zewnętrznej

**Skrypt:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Weryfikacja wprowadzania danych

**Scenariusz:** Sprawdź dopasowanie danych w dwóch różnych systemach

**Skrypt:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Kroki konfiguracji

### Krok 1: Utwórz skrypt

1. Zdefiniuj, co chcesz osiągnąć
2. Podziel to na małe kroki
3. Zapisz każdy krok wyraźnie
4. Najpierw przetestuj ręcznie (otwórz stronę, zrób to sam)
5. Dokumentuj dokładnie to, co klikasz, gdzie piszesz i co wyodrębniasz

### Krok 2: Zidentyfikuj zmienne

1. Jakie dane będą się zmieniać pomiędzy dokumentami?
2. Co należy przekazać do skryptu?
3. Zdefiniuj nazwy zmiennych
4. Określ, gdzie w skrypcie używane są zmienne

### Krok 3: Ustaw parametry

* **Maksymalna liczba kroków**: Na podstawie złożoności skryptu
* **Maksymalna liczba ponownych prób**: Jak trwały powinien być bot?
* **Limit czasu**: Jak długo powinien czekać na strony?

### Krok 4: Przetestuj

1. Przetestuj na przykładowych danych
2. Sprawdź, czy bot może uzyskać dostęp do witryny
3. Sprawdź, czy ekstrakcja jest prawidłowa
4. Sprawdź, czy zmienne działają poprawnie

***

## Wskazówki dotyczące pisania skryptów

### Wyczyść język

✅ **Wykonaj:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Nie:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Konkretne selektory

✅ **Wykonaj:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Nie:**

```
Click somewhere
Type in a field
```

### Obsługa błędów

✅ **Wykonaj:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Nie:**

```
Click "Next" (assumes it's always there)
```

***

## Rozwiązywanie problemów

### „Upłynął limit czasu skryptu”

**Przyczyna:** Ukończenie skryptu trwało zbyt długo

**Rozwiązania:**

* [ ] Zmniejsz liczbę działań
* [ ] Zwiększ wartość „Maksymalna liczba kroków”.
* [ ] Zoptymalizuj skrypt, aby przyspieszyć jego wykonanie
* [ ] Uprość to, co próbujesz wyodrębnić

### „Nie znaleziono elementu”

**Przyczyna:** DocOperator nie mógł znaleźć określonego przycisku/pola

**Rozwiązania:**

* [ ] Sprawdź, czy nazwa przycisku/pola jest poprawna
* [ ] Sprawdź, czy zmienił się układ strony
* [ ] Dodaj czas oczekiwania przed kliknięciem
* [ ] Sprawdź, czy przycisk pojawia się tylko w określonych warunkach

### „Logowanie nie powiodło się”

**Przyczyna:** Uwierzytelnienie nie powiodło się

**Rozwiązania:**

* [ ] Sprawdź, czy nazwa użytkownika i hasło są prawidłowe
* [ ] Sprawdź, czy hasło zawiera znaki specjalne
* [ ] Sprawdź, czy konto nie jest zablokowane
* [ ] Sprawdź, czy proces logowania się zmienił

### „Dane nie zostały poprawnie wyodrębnione”

**Przyczyna:** Skrypt został uruchomiony, ale wyodrębnił błędne informacje

**Rozwiązania:**

* [ ] Sprawdź, czy wybrano właściwe pole
* [ ] Sprawdź, czy dane znajdują się w oczekiwanej lokalizacji
* [ ] Przetestuj logikę ekstrakcji ręcznie
* [ ] Dodaj kroki debugowania, aby sprawdzić, co jest na stronie

### „Skrypt działa powoli”

**Przyczyna:** Zbyt wiele kroków lub powolna witryna

**Rozwiązania:**

* [ ] Usuń niepotrzebne kroki
* [ ] Zoptymalizuj czas oczekiwania
* [ ] Sprawdź połączenie internetowe
* [ ] Rozważ, czy istnieje alternatywa API

***

## Najlepsze praktyki

✅ **Wykonaj:**

* Dokładnie przetestuj skrypty przed wdrożeniem
* Staraj się, aby skrypty były proste i skoncentrowane
* Dodaj komentarze wyjaśniające każdy krok
* Używaj znaczących nazw zmiennych
* Monitoruj wydajność skryptu
* Mają rezerwę na wypadek niepowodzenia skryptów

❌ **Nie:**

* Twórz wyjątkowo długie skrypty (>100 kroków)
* Umieść poufne hasła w dziennikach
* Polegaj na dokładnych współrzędnych (zmiany stron internetowych)
* Twórz pętle bez warunków wyjścia
* Ignoruj komunikaty o błędach

***

## Wskazówki dotyczące wydajności

* **Usuń nieużywane kroki** - Każdy krok wymaga czasu
* **Połącz podobne działania** - Grupuj powiązane kliknięcia
* **Optymalizuj oczekiwania** — Używaj tylko niezbędnych opóźnień
* **Dane pamięci podręcznej** — Nie wyodrębniaj dwukrotnie tych samych danych
* **Przetwarzanie równoległe** — Jeśli to możliwe, uruchamiaj wiele skryptów

***

## Względy bezpieczeństwa

⚠️ **Ważne:**

* Nie przechowuj haseł w DocFlow
* Użyj bezpiecznych metod przekazywania poświadczeń
* Nie rejestruj wrażliwych danych
* Monitoruj to, co jest wyodrębniane
* Upewnij się, że aktywność bota jest rejestrowana i możliwa do kontrolowania

***

## Przykład zmiennych

### Dostępne zmienne, których możesz użyć:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Skrypt wykorzystujący zmienne:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Porównanie: kiedy używać DocOperatora i API

| Sytuacja              | Użyj DocOperatora | Skorzystaj z API     |
| ---------------------- | --------------- | ----------- |
| Strona posiada API        | ❌ Nie            | ✅ Tak       |
| Strona internetowa jest interaktywna | ✅ Tak           | ❌ Nie        |
| Wymaga logowania         | ✅ Tak           | Zależy     |
| Potrzebne bardzo szybko       | ❌ Nie            | ✅ Tak       |
| Złożony przepływ pracy       | ✅ Tak           | ❌ Może nie |
| Dane zmieniają się codziennie     | ✅ Tak           | ✅ Tak       |

***

## Powiązane karty

* **CALL\_API** — użyj, gdy zamiast tego dostępne jest API
* **ACTION\_HTTPS\_REQUEST** - Prostsze żądania
* **ACTION\_SET\_FIELD\_TO\_TEXT** — Użyj wyodrębnionych danych
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Sprawdź status żądania
