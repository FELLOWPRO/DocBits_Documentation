# Run DocOperator Prompt (Automation Script)

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

## Cel
Ta karta uruchamia zautomatyzowaną akcję przeglądarki lub skrypt przy użyciu DocOperator. Pomyśl o tym jak o robocie, który może wchodzić w interakcje z witrynami lub systemami dokładnie tak, jak zrobiłby to człowiek - klikając przyciski, wypełniając formularze, ekstrahując dane itp.

**Rzeczywisty przykład:** Twoja firma korzysta z internetowego systemu zakupowego. Ta karta może automatycznie zalogować się, wyszukać produkt, sprawdzić dostępność i uzyskać aktualną cenę - a wszystko to bez ręcznego wykonywania tych czynności.

---

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:
- Automatyzować zadania na witrynach, które nie mają API
- Ekstrahować dane ze stron internetowych
- Automatycznie wypełniać formularze
- Logować się do systemów i pobierać informacje
- Automatyzować powtarzalne zadania ręczne
- Wchodzić w interakcje ze starszymi systemami, które nie są zintegrowane

**Typowe scenariusze:**
- Logowanie do witryn dostawców i uzyskiwanie stanów magazynowych w czasie rzeczywistym
- Automatyczne wypełnianie formularzy w systemach zewnętrznych
- Ekstrakcja danych ze stron internetowych, które nie oferują API
- Sprawdzanie statusu dostawy na witrynach kurierskich
- Uzyskiwanie cen z systemów bez dostępu do API

---

## Jak to działa

1. **Wyzwolenie karty**: Przepływ pracy osiąga tę kartę i warunki są spełnione
2. **Uruchomienie skryptu**: Bot DocOperator rozpoczyna uruchamianie Twojego skryptu automatyzacji
3. **Akcje bota**: Bot wykonuje akcje takie jak klikanie, pisanie, przewijanie, ekstrahowanie
4. **Ekstrakcja danych**: Bot zbiera informacje ze stron internetowych
5. **Zwrot danych**: Dane wracają do DocFlow w celu wykorzystania w kolejnych kartach
6. **Obsługa limitu czasu**: Jeśli skrypt trwa zbyt długo, zatrzymuje się i zwraca to, co ma

---

## Wyjaśnienie parametrów

### DocOperator Prompt/Script
Skrypt automatyzacji, który dokładnie mówi DocOperatorowi, co ma robić

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

### Variables
Dane, które chcesz przekazać DO skryptu

**Przykład:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Tych zmiennych można używać w skrypcie w następujący sposób:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
Ile akcji bot może wykonać

**Typowe wartości:**
- Proste zadanie (jak uzyskanie jednej ceny): 10-20 kroków
- Średnia złożoność (wypełnij formularz + ekstrahuj): 20-50 kroków
- Złożony przepływ pracy (logowanie + wyszukiwanie + walidacja): 50-100 kroków

**Dlaczego to ważne:** Zapobiega nieskończonym pętlom i bardzo długo działającym skryptom

### Maximum Retries
Jeśli bot nie wykona akcji, ile razy powinien spróbować ponownie?

**Przykłady:**
- 1: Spróbuj raz, jeśli się nie powiedzie, przejdź dalej
- 3: Spróbuj 3 razy przed rezygnacją
- 5: Bardzo wytrwały - spróbuj 5 razy

---

## Przykład krok po kroku

### Scenariusz: Uzyskanie cen dostawcy z witryny

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

---

## Typy akcji, które może wykonać DocOperator

### Nawigacja
- Przejdź do URL
- Kliknij łącza
- Naciśnij przyciski
- Przewiń stronę

### Wypełnianie formularzy
- Wpisz tekst w pola
- Wybierz opcje listy rozwijanej
- Zaznacz/odznacz pola wyboru
- Kliknij przyciski

### Ekstrakcja danych
- Odczytaj tekst ze strony
- Wyekstrahuj liczby
- Pobierz dane tabeli
- Skopiuj informacje

### Oczekiwanie
- Czekaj na załadowanie strony
- Czekaj na pojawienie się elementów
- Czekaj na treść dynamiczną

### Logika warunkowa
- Jeśli coś istnieje, zrób to
- Jeśli tekst pasuje, to...
- Policz wyniki i działaj odpowiednio

---

## Typowe przypadki użycia

### 1. Uzyskanie cen w czasie rzeczywistym
**Scenariusz:** Dostawca nie ma API, ale witryna pokazuje ceny

**Skrypt:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Sprawdzenie dostępności w magazynie
**Scenariusz:** Trzeba wiedzieć, czy dostawca ma towar

**Skrypt:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatyczne przesyłanie formularza
**Scenariusz:** Trzeba wypełnić formularz na zewnętrznej witrynie

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
**Scenariusz:** Weryfikacja, czy dane są zgodne w dwóch różnych systemach

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

---

## Kroki konfiguracji

### Krok 1: Utwórz skrypt
1. Zdefiniuj, co chcesz osiągnąć
2. Podziel to na małe kroki
3. Napisz każdy krok jasno
4. Najpierw przetestuj ręcznie (otwórz witrynę, zrób to samodzielnie)
5. Udokumentuj dokładnie, co klikasz, gdzie piszesz, co ekstrahujesz

### Krok 2: Zidentyfikuj zmienne
1. Jakie dane będą się zmieniać między dokumentami?
2. Co powinno być przekazane do skryptu?
3. Zdefiniuj nazwy zmiennych
4. Określ, gdzie zmienne są używane w skrypcie

### Krok 3: Ustaw parametry
- **Maximum Steps**: Na podstawie złożoności skryptu
- **Maximum Retries**: Jak wytrwały powinien być bot?
- **Timeout**: Jak długo powinien czekać na strony?

### Krok 4: Przetestuj
1. Przetestuj z przykładowymi danymi
2. Zweryfikuj, czy bot ma dostęp do witryny
3. Zweryfikuj, czy ekstrakcja jest poprawna
4. Sprawdź, czy zmienne działają poprawnie

---

## Wskazówki dotyczące pisania skryptów

### Jasny język
✅ **Rób:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Nie rób:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Konkretne selektory
✅ **Rób:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Nie rób:**
```
Click somewhere
Type in a field
```

### Obsługa błędów
✅ **Rób:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Nie rób:**
```
Click "Next" (assumes it's always there)
```

---

## Rozwiązywanie problemów

### "Script Timed Out"
**Przyczyna:** Skrypt potrzebował zbyt dużo czasu na ukończenie

**Rozwiązania:**
- [ ] Zmniejsz liczbę akcji
- [ ] Zwiększ wartość "Maximum Steps"
- [ ] Zoptymalizuj skrypt pod kątem szybszego wykonania
- [ ] Uprość to, co próbujesz wyekstrahować

### "Element Not Found"
**Przyczyna:** DocOperator nie mógł znaleźć określonego przez Ciebie przycisku/pola

**Rozwiązania:**
- [ ] Zweryfikuj, czy nazwa przycisku/pola jest dokładnie poprawna
- [ ] Sprawdź, czy układ witryny się zmienił
- [ ] Dodaj czas oczekiwania przed kliknięciem
- [ ] Sprawdź, czy przycisk pojawia się tylko w określonych warunkach

### "Login Failed"
**Przyczyna:** Uwierzytelnianie nie powiodło się

**Rozwiązania:**
- [ ] Zweryfikuj, czy nazwa użytkownika/hasło są poprawne
- [ ] Sprawdź, czy hasło zawiera znaki specjalne
- [ ] Zweryfikuj, czy konto nie jest zablokowane
- [ ] Sprawdź, czy proces logowania się zmienił

### "Data Not Extracted Correctly"
**Przyczyna:** Skrypt uruchomił się, ale wyekstrahował nieprawidłowe informacje

**Rozwiązania:**
- [ ] Zweryfikuj, czy wybrano poprawne pole
- [ ] Sprawdź, czy dane są w oczekiwanej lokalizacji
- [ ] Przetestuj logikę ekstrakcji ręcznie
- [ ] Dodaj kroki debugowania, aby zweryfikować, co jest na stronie

### "Script Runs Slowly"
**Przyczyna:** Zbyt wiele kroków lub wolna witryna

**Rozwiązania:**
- [ ] Usuń niepotrzebne kroki
- [ ] Zoptymalizuj czasy oczekiwania
- [ ] Sprawdź połączenie internetowe
- [ ] Rozważ, czy istnieje alternatywa w postaci API

---

## Najlepsze praktyki

✅ **Rób:**
- Dokładnie testuj skrypty przed wdrożeniem
- Utrzymuj skrypty proste i ukierunkowane
- Dodawaj komentarze wyjaśniające każdy krok
- Używaj znaczących nazw zmiennych
- Monitoruj wydajność skryptu
- Miej rozwiązanie zapasowe na wypadek awarii skryptów

❌ **Nie rób:**
- Nie twórz wyjątkowo długich skryptów (>100 kroków)
- Nie umieszczaj wrażliwych haseł w dziennikach
- Nie polegaj na dokładnych współrzędnych (witryny się zmieniają)
- Nie twórz pętli bez warunków wyjścia
- Nie ignoruj komunikatów o błędach

---

## Wskazówki dotyczące wydajności

- **Usuń nieużywane kroki** - Każdy krok zajmuje czas
- **Połącz podobne akcje** - Grupuj powiązane kliknięcia
- **Zoptymalizuj oczekiwania** - Używaj tylko niezbędnych opóźnień
- **Buforuj dane** - Nie ekstrahuj tych samych danych dwukrotnie
- **Przetwarzanie równoległe** - Uruchamiaj wiele skryptów, jeśli to możliwe

---

## Kwestie bezpieczeństwa

⚠️ **Ważne:**
- Nie przechowuj haseł w DocFlow
- Używaj bezpiecznych metod przekazywania poświadczeń
- Nie rejestruj danych wrażliwych
- Monitoruj, co jest ekstrahowane
- Zapewnij, że aktywność bota jest rejestrowana i możliwa do audytu

---

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

---

## Porównanie: Kiedy używać DocOperator vs API

| Sytuacja | Użyj DocOperator | Użyj API |
|-----------|-----------------|---------|
| Witryna ma API | ❌ Nie | ✅ Tak |
| Witryna jest interaktywna | ✅ Tak | ❌ Nie |
| Wymaga logowania | ✅ Tak | Zależy |
| Wymagana bardzo duża szybkość | ❌ Nie | ✅ Tak |
| Złożony przepływ pracy | ✅ Tak | ❌ Może nie |
| Dane zmieniają się codziennie | ✅ Tak | ✅ Tak |

---

## Powiązane karty

- **CALL_API** - Użyj, gdy zamiast tego dostępne jest API
- **ACTION_HTTPS_REQUEST** - Prostsze żądania
- **ACTION_SET_FIELD_TO_TEXT** - Użyj wyekstrahowanych danych
- **CONDITION_HTTPS_REQUEST_STATUS** - Sprawdź status żądania
