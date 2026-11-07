# Edytowanie i usuwanie kolumn

Pola wyboru sterują wymaganymi wartościami, edycją i widocznością. Use AI konfiguruje się osobno na opisanej poniżej liście trzech stanów.

Wszystko oprócz tytułu zmienia się bezpośrednio na liście; nie ma okna edycji.

**Gdzie:** Settings → Document Processing → Document Types → Table Columns

## Przełączanie flagi

Zaznacz lub odznacz pole wyboru w wierszu. Zmiana jest zapisywana natychmiast (*Successfully saved*).

| Flaga | Włączona | Wyłączona |
|---|---|---|
| **Is Required** | Zatwierdzenie jest blokowane, dopóki kolumna jest pusta w którymkolwiek wierszu; ekran walidacji oznacza komórkę. | Puste komórki są dozwolone. |
| **Read Only** | Wartość jest wyświetlana, ale nie można jej nadpisać. Używaj dla wartości pochodzących z wyszukiwania lub ze skryptu. | Użytkownicy mogą edytować komórkę. |
| **Hidden** | Kolumna znika z ekranu walidacji i z eksportu. Jej dane są zachowane. | Kolumna jest wyświetlana i eksportowana. |


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

## Use AI: Domyślne, Tak lub Nie

Otwórz [Kolumny tabeli](README.md) dla właściwego typu dokumentu i tabeli. **Użyj sztucznej inteligencji (Use AI)** jest listą trzech stanów, a nie polem wyboru. Zmiana zapisuje się natychmiast.

| Aktualna opcja | Wpływ na schemat bazowy |
| --- | --- |
| **Default · żądane** lub **Default · nie zażądano** | Przyjmuje ustawienie DocBits dla tego typu i nazwy kolumny. Domyślne nie oznacza zawsze włączone ani zawsze wyłączone. |
| **Yes · poproszono** | Jawnie żąda skonfigurowanej kolumny od AI. |
| **Nie · nie poproszono** | Wyklucza ją ze schematu bazowego, nawet jeśli normalnie jest żądana. |

Powrót do **Default** usuwa jawny wybór. Nowa własna kolumna zwykle nie należy do domyślnego zestawu AI: wybierz **Yes**, aby AI ją zwracała. Domyślny zestaw AI nie oznacza wszystkich kolumn dostarczonych z DocBits. Sprawdź wskazany efekt i podgląd.

**Required**, **Read Only** i **Hidden** sterują kompletnością, edycją i widocznością; nie zastępują wyboru AI. **Nie** nie usuwa kolumny ani jej wartości i nie blokuje reguł, skryptów lub innych źródeł danych. Trening dostawcy i dodatkowe tagi AI mogą rozszerzyć faktyczne żądanie: rozwiąż sprzeczności także tam. Przełącznik nie zastępuje automatycznie wyniku pochodzącego wyłącznie z reguł.

[Structured Output dla tabel](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
