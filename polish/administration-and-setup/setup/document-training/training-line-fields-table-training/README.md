# Trenowanie pól pozycji i tabel

## Trenowanie tabel: kiedy i jak go używać

DocBits domyślnie korzysta z wyodrębniania tabel w oparciu o AI, co działa u wszystkich dostawców. Jeśli jednak potrzebujesz większej kontroli nad sposobem wyodrębniania pozycji dla konkretnego dostawcy, możesz użyć **Trenowanie tabel**, aby ręcznie zdefiniować strukturę.

#### &#x20;**Ważne: trenowanie specyficzne dla dostawcy**

Trenowanie tabel jest **specyficzne dla każdego dostawcy**. Jeśli szkolisz układ tabeli dla jednego dostawcy, zasady dotyczą tylko dokumentów tego dostawcy.\
Inni dostawcy będą nadal korzystać z ekstrakcji tabeli opartej na AI, chyba że zostaną przeszkoleni osobno.

#### Kiedy należy używać trenowania tabel?

Użyj treningu tabel **tylko wtedy, gdy układ dokumentu jest stabilny** i chcesz zapewnić spójną ekstrakcję wysokiej jakości. Najlepiej nadaje się dla dostawców, którzy:

* Z czasem używaj **stałego formatu faktury**.
* Wymagaj **precyzyjnego mapowania** elementów zamówienia do określonych pól.
* Są **dostawcami masowymi**, w przypadku których cenna jest konsekwentna automatyzacja.

#### Kiedy nie używać trenowania tabel

Unikaj korzystania z treningu przy stole, jeśli:

* Dostawca **często zmienia układ faktury** (np. co kilka miesięcy).
* Nie otrzymujesz regularnie dokumentów od tego dostawcy.
* Domyślna ekstrakcja AI działa **wystarczająco** bez ręcznego szkolenia.

W takich przypadkach wielokrotne przeszkolenie tabeli byłoby nieefektywne i czasochłonne.



## Sposób użycia:

**Tryb trenowania** służy do uczenia DocBits, jak prawidłowo wyodrębniać pozycje z układu dokumentu określonego dostawcy.

Kiedy jesteś w trybie treningowym, definiujesz:

* **Gdzie znajduje się tabela** w dokumencie.
* **Które obszary odpowiadają każdej kolumnie** (np. Ilość, Opis, Cena jednostkowa).

Ten tryb tworzy dla tego dostawcy **szablon wyodrębniania wielokrotnego użytku**, dzięki czemu przyszłe dokumenty o tym samym układzie będą przetwarzane automatycznie — bez konieczności ponownego trenowania.

**Key Characteristics:**

* **Zamapowane kolumny są tylko do odczytu** — nie można ręcznie zmienić tekstu.
* **Nie możesz dodawać ani usuwać wierszy**.
* Koncentrujemy się na **mapowaniu pozycji**, a nie na korygowaniu wartości.
* Po zakończeniu mapowania tabeli i jej kolumn kliknij **“Save Rules”**, aby DocBits nauczył się i zastosował to trenowanie do podobnych dokumentów od tego samego dostawcy.



**Tryb korekcji** umożliwia **naprawienie błędów ekstrakcji** w danych tabeli dla bieżącego dokumentu. Używa się go, gdy DocBits już próbował wyodrębnić tabelę, ale wyniki wymagają drobnych poprawek.

Użyj trybu korekcji, gdy:

* Brakuje niektórych wartości **lub są one źle wyrównane**.
* Wyodrębniono **pustą lub zduplikowaną linię** i należy ją usunąć.

**Co możesz zrobić w trybie korekcji:**

* **Ręcznie dostosuj wartości** w mapowanych kolumnach (np. napraw nieprawidłowe rozmieszczenie).
* **Usuń wiersze**, które nie powinny być częścią tabeli.
* **Dodaj wiersze**, które zostały całkowicie pominięte podczas wyodrębniania.
