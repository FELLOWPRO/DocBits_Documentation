# Uruchamianie monitów za pomocą przepływu pracy

Ten przewodnik wyjaśnia, jak skonfigurować przepływ pracy DocBits, aby automatycznie uruchamiał zapisany monit. Pozwala to zintegrować monitory Operatora w przepływy przetwarzania dokumentów bez konieczności ręcznego wprowadzania.

## Krok 1: Utwórz monit

Przed połączeniem monitora z przepływem pracy:

* Upewnij się, że twój monitor jest już utworzony
* Dołącz wszystkie niezbędne **zmienne** do treści monitora.

Jeśli potrzebujesz pomocy przy pisaniu lub zapisywaniu monitorów, odwołaj się do [Przewodnika po pisaniu monitów](../prompt-writing-guide.md) i [Przeglądu interfejsu Operatora](../).

## Krok 2: Skonfiguruj przepływ pracy

Przed skonfigurowaniem karty Monitu Operatora upewnij się, że twój przepływ pracy jest właściwie utworzony.

1. Przejdź do **Kreatora przepływów pracy** w interfejsie DocBits.
2. Utwórz nowy przepływ pracy lub otwórz istniejący.
3. Zdefiniuj **warunki wyzwalające** - określają one, kiedy przepływ pracy zostanie uruchomiony (np. typ dokumentu, status, obecność pola itp.).
4. Dodaj niezbędne **kroki akcji** do swojego przepływu pracy, w miarę potrzeb.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Krok 3: Skonfiguruj kartę Monitu Operatora w przepływie pracy

W Kreatorze przepływów pracy użyj karty **Monit Operatora**, aby skonfigurować monit, który powinien zostać wykonany, gdy warunki przepływu pracy zostaną spełnione.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Kluczowe opcje konfiguracji

* **Skrypt:** Wybierz zapisany **Monit Organizacji**, który ma zostać wykonany.
* **Dane skryptu (Zmienne):** Jeśli wybrany monit zawiera zmienne, zdefiniuj ich wartości tutaj, używając par klucz-wartość.
  * Jeśli zmienna zostanie tutaj pozostawiona pusta, system spróbuje automatycznie wypełnić ją **z dokumentu**.
  * Aby to działało, nazwa zmiennej w monicie musi **dokładnie pasować** do **ID pola** atrybutu dokumentu.
* **Maksymalna liczba kroków:** Zdefiniuj maksymalną liczbę kroków, jakie operator może wykonać podczas tego monitu.
* **Maksymalna liczba ponownych prób:** Określ, ile razy system powinien ponowić próbę monitu w przypadku niepowodzenia.
* **Tryb wykonania:** Wybierz, czy monit powinien być uruchomiony:
  * **W chmurze**
  * **Lokalnie** (wymagane, jeśli twoje ERP lub system docelowy jest hostowany lokalnie)
