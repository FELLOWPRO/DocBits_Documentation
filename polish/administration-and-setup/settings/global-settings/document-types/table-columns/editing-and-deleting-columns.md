# Edytowanie i usuwanie kolumn

Wszystko oprócz tytułu zmienia się bezpośrednio na liście; nie ma okna edycji.

**Gdzie:** Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli

## Przełączanie flagi

Zaznacz lub odznacz pole wyboru w wierszu. Zmiana jest zapisywana natychmiast (*Successfully saved*).

| Flaga | Włączona | Wyłączona |
|---|---|---|
| **Is Required** | Zatwierdzenie jest blokowane, dopóki kolumna jest pusta w którymkolwiek wierszu; ekran walidacji oznacza komórkę. | Puste komórki są dozwolone. |
| **Read Only** | Wartość jest wyświetlana, ale nie można jej nadpisać. Używaj dla wartości pochodzących z wyszukiwania lub ze skryptu. | Użytkownicy mogą edytować komórkę. |
| **Hidden** | Kolumna znika z ekranu walidacji i z eksportu. Jej dane są zachowane. | Kolumna jest wyświetlana i eksportowana. |
| **Use AI** | Kolumnę wypełnia ekstrakcja tabel przez AI, również dla dostawców z wytrenowanymi regułami. | Kolumnę wypełniają wytrenowane reguły albo AI, gdy reguł nie ma. |

{% hint style="info" %}
Flagi obowiązują dla dokumentów przesłanych lub uruchomionych ponownie **po** zmianie. Otwarte dokumenty zachowują bieżącą tabelę, dopóki nie zostaną uruchomione ponownie.
{% endhint %}

## Zmiana tytułu

Kliknij ikonę tłumaczenia w kolumnie *Actions* (*Update translation key*), wpisz nową etykietę i potwierdź. Ikona informacji obok pokazuje, która etykieta obowiązuje obecnie i skąd pochodzi. Zmienia się tylko etykieta; techniczna *Column name* pozostaje taka sama, więc skrypty, mapowania eksportu i wytrenowane reguły nadal działają.

## Zmiana typu lub tabeli

Nie jest to możliwe. Ukryj kolumnę (lub usuń ją, jeśli jest Twoja własna) i dodaj nową z właściwym typem.

## Usuwanie kolumny

Akcja usuwania jest dostępna tylko dla kolumn utworzonych przez Twoją organizację. Kolumn domyślnych nie można usunąć, ukryj je.

1. Otwórz menu z trzema kropkami w kolumnie *Actions* i wybierz **Delete**. Dla kolumn domyślnych ta pozycja nie jest dostępna.
2. Potwierdź.

Co się dzieje:

* Kolumna zostaje usunięta z konfiguracji. Dokumenty przetwarzane **od tej chwili** jej nie mają.
* Dokumenty, które zostały już wyodrębnione, zachowują kolumnę i jej wartości, dopóki nie zostaną uruchomione ponownie.
* Wytrenowane reguły, które mapowały tę kolumnę, nadal działają dla pozostałych kolumn; mapowanie usuniętej kolumny jest ignorowane.
* Jeśli kolumna jest przywołana w mapowaniu eksportu lub w skrypcie, usuń to odwołanie; w przeciwnym razie eksport lub skrypt zakończy się błędem brakującej kolumny.

## Cofnięcie usunięcia

Usuniętej kolumny nie można przywrócić z listy. Dodaj ją ponownie z tym samym tytułem: nazwa techniczna jest tworzona na podstawie tytułu, więc kolumna utworzona z tym samym tytułem otrzymuje tę samą *Column name* i istniejące mapowania znów do niej pasują.
