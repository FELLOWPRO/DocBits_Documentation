# Przewodnik po pisaniu poleceń

Ten przewodnik wyjaśnia, jak pisać skuteczne polecenia dla operatora DocBits. Polecenia to instrukcje krok po kroku, które kierują operatorem do wykonania konkretnych zadań, takich jak nawigacja po stronach internetowych, interakcja z elementami interfejsu użytkownika i wprowadzanie danych.

## Co to jest polecenie?

Polecenie to sekwencja instrukcji zapisanych w tekście, która kieruje operatorem do wykonania określonego zadania. Polecenia mogą zawierać polecenia takie jak klikanie przycisków, wypełnianie formularzy, oczekiwanie na załadowanie stron lub elementów i wiele więcej.

## Składnia i struktura polecenia

* Każda instrukcja powinna być zapisana jako numerowany krok.
* Używaj jasnego, zwięzłego języka, aby opisać każdą akcję.
* Określ elementy interfejsu użytkownika według nazwy, etykiety lub numeru indeksu, aby zapewnić precyzję.
* Używaj spójnego formatowania, aby poprawić czytelność.

## Korzystanie z zmiennych w poleceniach

Zmienne pozwalają na dynamiczne tworzenie poleceń poprzez wstawianie różnych wartości podczas działania. Zamiast wpisywać wartości na stałe, takie jak daty czy numery dokumentów, użyj zmiennych wewnątrz nawiasów klamrowych - na przykład: `{invoice_number}`, `{url}`, lub `{purchase_order}`.

Dzięki temu polecenia stają się wielokrotnego użytku i dostosowalne do różnych przepływów pracy lub zbiorów danych.

### Jak używać zmiennych

* Umieść zmienne wewnątrz nawiasów klamrowych w tekście polecenia:
  * Wprowadź numer faktury: {invoice\_number} w polu 'Numer faktury HP'.
* Każda zmienna musi mieć unikalną nazwę (np. `invoice_number`, `url`, `document_type`).
* Nazwy zmiennych nie mogą zawierać spacji ani znaków specjalnych (podkreślenia są dozwolone).
* W przypadku przepływów pracy nazwy zmiennych muszą dokładnie pasować do identyfikatorów pól dokumentu, aby umożliwić automatyczne mapowanie danych.

## Okno dialogowe zmiennych polecenia

Aby otworzyć okno dialogowe zmiennych polecenia, kliknij ikonę **koła zębatego** znajdującą się obok pola wprowadzania polecenia.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Układ i kontrolki okna dialogowego

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Pole wprowadzania klucza:** Wprowadź nazwę zmiennej tutaj (bez nawiasów klamrowych).
* **Pole wprowadzania wartości:** Wprowadź wartość, która ma być użyta dla tej zmiennej podczas uruchamiania polecenia.
* **Zapisz jako poufne (pole wyboru):** Po zaznaczeniu oznacza to wartość zmiennej jako poufną. Wartości poufne są szyfrowane i ukrywane w przepływach pracy, aby chronić poufne informacje przed nieautoryzowanymi użytkownikami.
* **Przycisk Dodaj (+):** Kliknij, aby dodać kolejny wiersz wejścia pary klucz-wartość.
* **Ikona usuwania (Kosz):** Gdy istnieje wiele par klucz-wartość, wszystkie pary oprócz pierwszej pokazują małą ikonę kosza, aby usunąć tę konkretną parę.
* **Przycisk Wyczyść:** Resetuje okno dialogowe, czyściąc wszystkie pary klucz-wartość i wprowadzone wartości.
* **Przycisk Zapisz:** Zapisuje wszystkie zdefiniowane zmienne i ich wartości dla bieżącego polecenia.
