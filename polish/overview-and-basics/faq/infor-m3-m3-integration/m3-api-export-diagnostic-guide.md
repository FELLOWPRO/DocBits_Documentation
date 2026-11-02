# Przewodnik Diagnostyczny Eksportu M3 API

### 1. Konfiguracja Początkowa

Zanim rozpoczniesz rozwiązywanie problemów, upewnij się, że znasz oczekiwane dane wejściowe dla punktu końcowego M3, z którym pracujesz.

#### 1.1 Dostęp do Dokumentacji API M3

* Zaloguj się do **M3**.
* Przejdź do **Sekcji API → Dokumentacja API**.
* Zlokalizuj i wybierz odpowiedni punkt końcowy (np. `APS450MI` dla eksportów związanych z fakturami).
* Wybierz odpowiednią funkcję (np. `Add`).

#### 1.2 Zrozumienie Wymagań API

* Zapoznaj się z wszystkimi **pola wymagane** w dokumentacji API.
* Zwróć uwagę na ważne pola, takie jak:
  * `DIVI`
  * `ACDT` (data księgowania)
  * `CUCD` (kod waluty)
  * `SINO` (numer faktury dostawcy)
* Potwierdź typy danych pól, wielkość liter oraz reguły formatowania (np. `RRRR-MM-DD` dla dat).

### 2. Testowanie Wywołań API Bezpośrednio w M3

Ten krok sprawdza, czy API M3 zachowuje się zgodnie z oczekiwaniami przy użyciu danych testowych.

#### 2.1 Generowanie Testowego Żądania w M3

* W narzędziu Dokumentacji API M3:
  * Wypełnij dane testowe dla pól wymaganych.
  * Kliknij **Uruchom**, aby wykonać żądanie.
  * Skopiuj wynikowy **cURL** oraz **treść JSON**.

#### 2.2 Debugowanie Za Pomocą Postman

* Otwórz **Postman** i utwórz nowe żądanie typu **POST**.
* Wklej treść JSON lub cURL.
* Dodaj niezbędne nagłówki (np. autoryzacja).
* Kliknij **Wyślij** i obserwuj wynik:
  * `200 OK`: Żądanie zostało pomyślnie zrealizowane.
  * Błąd: Sprawdź komunikat w celu uzyskania szczegółów dotyczących problemu.

### 3. Porównywanie API M3 z Mapowaniem DocBits

Po potwierdzeniu, że API działa z danymi testowymi, porównaj go z tym, co DocBits faktycznie wysyła.

#### 3.1 Eksportowanie Próbki Danych z DocBits

*   Otwórz **Dokumentację API DocBits**:

    Użyj punktu końcowego **/export/get\_infor\_export\_api\_json**.
* Wprowadź **ID Dokumentu** problematycznego.
* Uruchom eksport, aby zobaczyć **ładunek JSON**, który DocBits wyśle do M3.

#### 3.2 Porównywanie Ładunków API

* Umieść **testowy JSON M3** obok **eksportowego JSON DocBits**.
* Sprawdź:
  * **Nazwy Pól**: Upewnij się, że nazwy są identyczne, włączając wielkość liter (`DIVI` ≠ `divi`).
  * **Typy Danych**: Zweryfikuj, czy ciągi znaków, liczby i daty są poprawnie sformatowane.
  * **Brakujące Pola**: Zidentyfikuj pola obecne w żądaniu M3, ale brakujące w DocBits.

### 4. Rozwiązywanie Powszechnych Problemów

| Problem                                     | Prawdopodobna Przyczyna                    | Naprawa                                                          |
| ------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| Błąd brakującego pola                       | Wymagane pole nie jest zmapowane w DocBits | Dodaj brakujące pole w konfiguracji eksportu DocBits.            |
| Niezgodność wielkości liter w polu (`DIVI`) | M3 rozróżnia wielkość liter                | Użyj poprawnej wielkości liter w mapowaniu pola.                 |
| Nieprawidłowy format `accountingDate`       | Zły lub brakujący format daty              | Dostosuj do oczekiwanego formatu przez M3 (np. `RRRR-MM-DD`).    |
| Nieoczekiwany błąd API                      | Dodatkowe lub nierozpoznane pola           | Porównaj z znanymi działającymi ładunkami i wyczyść zbędne dane. |

### 5. Jeśli Problemy Nadal Istnieją

Jeśli problem nie został rozwiązany po wykonaniu powyższych kroków:

1. **Zdokumentuj** problem:
   * Komunikat błędu i kod stanu
   * Przykładowe żądanie M3 i eksport JSON DocBits
2. **Podsumuj** swoje działania:
   * Co próbowałeś
   * Główne różnice zauważone między testowymi a nieudanymi ładunkami
3. **Eskaluj** do programisty:
   * Dołącz wszystkie dane i wyniki
   * Zwróć uwagę na obszary podejrzane o problemy
