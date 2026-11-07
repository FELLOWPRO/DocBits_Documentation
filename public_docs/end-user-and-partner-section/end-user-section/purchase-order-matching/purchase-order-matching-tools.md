# Narzędzia dopasowywania zamówień zakupu

Na ekranie dopasowywania zamówień zakupu wyszukiwanie zamówień i narzędzia znajdują się nad wierszami zamówienia zakupu. Podgląd faktury pozostaje po prawej stronie. Dostępne działania mogą się różnić w zależności od Twoich uprawnień, danych dokumentu oraz ustawień Twojej organizacji.

<figure><img src="../../../.gitbook/assets/dbdc-190-po-tools-overview-pl.png" alt="Polski ekran dopasowywania zamówień zakupu w sandboxie dokumentacyjnym DocBits: wyszukiwarka zamówień, pasek narzędzi akcji, wiersze zamówienia zakupu, sekcja faktury i podgląd dokumentu"><figcaption><p>Pole wyszukiwania i pasek narzędzi akcji znajdziesz nad wierszami zamówienia zakupu.</p></figcaption></figure>

## Znajdowanie właściwego zamówienia zakupu

Wpisz numer zamówienia zakupu w polu **Search purchase order number** i wybierz wynik. Ikona filtra obok pola otwiera opcje wyszukiwania na całym obszarze wierszy zamówienia zakupu: Słowo kluczowe, Dostawca, Status, Status zamówienia, Po dacie, Przed datą, Minimalna kwota zamówienia, Maksymalna kwota zamówienia, Sortuj według, Sortuj kierunek i Liczba rekordów do wyświetlenia. Wybierz **Apply**, aby użyć filtrów, albo **Clear**, aby je zresetować. Filtrowanie listy nie dopasowuje i nie eksportuje faktury.

<figure><img src="../../../.gitbook/assets/po-matching-tools-filter-pl-20261107.png" alt="Filtr wyszukiwania zamówień zakupu na całym obszarze wierszy zamówienia, z polami słowa kluczowego, dostawcy, statusu, dat, kwoty i sortowania"><figcaption><p>Kliknij ikonę filtra obok pola wyszukiwania zamówienia, aby otworzyć więcej opcji wyszukiwania.</p></figcaption></figure>

## Akcje na pasku narzędzi

Przed wybraniem ikony przeczytaj jej podpowiedź. Pasek narzędzi może pokazywać:

| Akcja | Co robi |
| --- | --- |
| **Matching history** (clock) | Otwiera wcześniejsze działania dopasowań dla tego dokumentu. Nie uruchamia nowego dopasowania. |
| **Help** (?) | Otwiera stronę pomocy o dopasowywaniu zamówień zakupu w nowej karcie przeglądarki. |
| **Keyboard shortcuts** (keyboard) | Pokazuje skróty dostępne na tym ekranie. Zobacz [Skróty klawiaturowe](keyboard-shortcuts.md). |
| **Training mode** (table) | Włącza lub wyłącza przeciąganie wierszy zamówienia zakupu do tabeli faktury. Przydatny tylko wtedy, gdy dokument ma wiersze faktury; przykładowy ekran poniżej ich nie ma. |
| **Tasks / Create task** | Otwiera zadania dokumentu lub tworzy zadanie, gdy te akcje są dostępne dla Twojego dokumentu i roli. Zobacz [Zadania](../tasks.md). |
| **Auto Accounting** | Otwiera rozliczanie dla tego dokumentu, gdy dane księgowe są dostępne. |
| **Auto PO match** (wand) | Uruchamia dopasowanie automatyczne. Jeśli organizacja włączyła eksport automatyczny, a wynik spełnia jego warunki, ta akcja może również wyeksportować dokument. Sprawdź dokument, zanim jej użyjesz. Zobacz [Automatyczne dopasowywanie danych zamówień zakupu](automatic-purchase-order-data-matching.md). |
| **Save** (disk) | Zapisuje zmiany dopasowania zamówienia zakupu w dokumencie. |
| **Sync Data** | Dostępne tylko dla odpowiedniego ustawienia ilości zamówienia zakupu; odświeża wybrane dane zamówienia z połączonego systemu. Użyj wyświetlonego numeru zamówienia i dostępnych opcji synchronizacji. |
| **Export** | Eksportuje dokument po dopasowaniu. Jeśli Twoja organizacja oferuje wiele celów eksportu, użyj strzałki obok **Export**, aby wybrać jeden. |

Zakładka zamówienia zakupu ma też ikonę odświeżenia do ponownego wczytania tego zamówienia. Ikona ustawień kolumn po prawej stronie nagłówka tabeli decyduje, które kolumny zamówienia zakupu są widoczne. Obie zmieniają widok tabeli zamówienia zakupu, a nie wartości wyodrębnione z faktury.

## Skróty klawiaturowe

Wybierz ikonę klawiatury, aby zobaczyć aktualną listę skrótów. Typowe przykłady to **Ctrl+F**, aby ustawić fokus na wyszukiwaniu zamówienia, **Ctrl+K**, aby ponownie otworzyć okno skrótów, **Ctrl+S**, aby zapisać, oraz **Ctrl+E**, aby wyeksportować. Pełną listę dla Twojego ekranu pokazuje samo okno.

<figure><img src="../../../.gitbook/assets/dbdc-190-po-tools-shortcuts-pl.png" alt="Okno skrótów klawiaturowych na polskim ekranie dopasowywania zamówień zakupu"><figcaption><p>Otwórz ikonę klawiatury, aby zobaczyć skróty obsługiwane na tym ekranie.</p></figcaption></figure>

{% hint style="info" %}
Ten przykład używa syntetycznej faktury i zamówienia zakupu w sandboxie dokumentacyjnym DocBits. Faktura nie ma wyodrębnionych wierszy, więc nie może pokazać udanego dopasowania. Akcje dopasowania, zapisu, synchronizacji i eksportu nie były uruchamiane podczas tworzenia tych obrazów.
{% endhint %}
