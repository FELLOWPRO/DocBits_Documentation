# Strukturyzacja i Poprawa Ekstrakcji Tabel w DocBits

Po wyekstrahowaniu tabeli i zakończeniu początkowego mapowania kolumn, możesz poprawić jakość i strukturę danych za pomocą kilku wbudowanych narzędzi. Ten przewodnik prowadzi Cię przez:

* Grupowanie wierszy
* Ręczny wybór wierszy
* Mapowanie kolumn
* Udoskonalanie nagłówków za pomocą regex

Te narzędzia są szczególnie pomocne przy pracy z złożonymi lub niekonsekwentnymi układami dokumentów.

## 1. Grupowanie Wierszy

Dokumenty takie jak faktury czy potwierdzenia zamówień często zawierają wpisy tabeli, w których jedna kolumna (np. opis) obejmuje kilka wierszy, podczas gdy inne kolumny (np. ilość lub cena) zajmują tylko jeden wiersz.

Weźmy jako przykład niemiecką fakturę — kolumna "Bezeichnung" (opis) obejmuje kilka wierszy:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-multiline-doc-pl-20261009.png" alt="Tabela niemieckiej faktury, w której opis (Bezeichnung) każdej pozycji zajmuje kilka wierszy."><figcaption><p>Kolumna opisu rozciągająca się na kilka wierszy.</p></figcaption></figure>

Początkowo DocBits wyodrębnia każdy wiersz osobno:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-initial-extraction-pl-20261009.png" alt="Wyekstrahowana tabela, w której każdy wiersz tekstu opisu stał się osobnym wierszem."><figcaption><p>DocBits najpierw wyodrębnia każdy wiersz osobno.</p></figcaption></figure>

Następnie możesz **grupować wiersze na podstawie kolumny**, takiej jak "Pozycja". To połączy powiązane linie w jedno, uporządkowane wpisy:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-grouped-result-pl-20261009.png" alt="Wyekstrahowana tabela, w której powiązane wiersze opisu zostały połączone w jeden wpis na pozycję."><figcaption><p>Po grupowaniu według Pozycji powiązane wiersze tworzą jeden wpis.</p></figcaption></figure>

Ile podwierszy zostanie połączonych w jeden wpis i jak zachowuje się grupowanie, ustawisz w [Ustawieniach zaawansowanych](advanced-settings.md) pod **Minimalna liczba zgrupowanych wierszy** oraz **Grupowanie odwrócone**.

## 2. Ręczny Wybór Wierszy

W niektórych przypadkach tekst na dokumencie jest rozłożony na kilka kolumn w jednym wierszu, co sprawia, że trudno jest przypisać go automatycznie.

Oto przykład, gdzie linia "PRAEF" nakłada się na **Bezeichnung**, **Menge**, **ME** i **Preis in EUR**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-misalignment-pl-20261009.png" alt="Tabela faktury z wierszem PRAEF, którego tekst rozciąga się na kilka kolumn."><figcaption><p>Wiersz PRAEF, który nie pasuje do struktury kolumn.</p></figcaption></figure>

### Jak Ręcznie Przypisać Wartości:

1.  **Włącz Tryb szkoleniowy**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-training-mode-pl-20261009.png" alt="Widok ekstrakcji tabeli z włączonym trybem szkoleniowym."><figcaption><p>Tryb szkoleniowy włączony.</p></figcaption></figure>
2.  **Aktywuj Tryb edycji danych wiersza**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-edit-mode-pl-20261009.png" alt="Widok ekstrakcji tabeli z włączonym trybem edycji danych wiersza i widoczną podpowiedzią."><figcaption><p>Tryb edycji danych wiersza włączony.</p></figcaption></figure>
3.  **Wybierz i Mapuj Tekst**\
    Kliknij odpowiedni fragment tekstu i przypisz go do **niebieskiego** nagłówka kolumny.

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-editable-columns-pl-20261009.png" alt="Wyekstrahowana tabela w trybie edycji danych wiersza z niebieskimi, jeszcze niewypełnionymi nagłówkami kolumn, które można przypisać ręcznie."><figcaption><p>Niebieskie nagłówki kolumn można wypełnić ręcznie.</p></figcaption></figure>

> Uwaga: Kolumny o fiolecie są już zmapowane przez system i nie mogą być edytowane ręcznie.

Ta praca odbywa się w **Trybie edycji danych wiersza**. Co można w nim zrobić i kiedy używać go zamiast trybu szkoleniowego, opisano w [Szkolenie pól pozycji / Szkolenie tabeli](README.md).

## 3. Mapowanie Kolumn

Mapowanie kolumn łączy wyekstrahowane dane z oczekiwanymi nagłówkami kolumn, zapewniając spójność i możliwość eksportu.

Aby zmapować lub ponownie zmapować kolumnę:

1. Kliknij nagłówek kolumny w widoku ekstrakcji.
2. Wybierz właściwą kolumnę docelową z rozwijanego menu.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-mapping-dropdown-pl-20261009.png" alt="Wyekstrahowana tabela z otwartą listą rozwijaną nagłówka kolumny, wyświetlającą kolumny docelowe Opis, Numer Przedmiotu, Kwota Netto, Pozycja, Ilość, Całkowita Kwota, Jednostka i Cena Jednostkowa."><figcaption><p>Wybierz kolumnę docelową z listy rozwijanej nagłówka.</p></figcaption></figure>

Możesz dostosować mapowanie tak często, jak jest to potrzebne.

Aby dowiedzieć się, jak tworzyć tabele i kolumny, zobacz [Definiowanie Tabel i Kolumn](defining-tables-and-columns.md).

## 4. Wyodrębnianie Z Góry / Z Dole

Niektóre dokumenty są zorganizowane w taki sposób, że istotne wartości tabeli nie pojawiają się w tym samym wierszu co inne dane. W takich przypadkach DocBits pozwala kontrolować **skąd dane powinny być wyodrębnione**:

* **Wyodrębnij Z Góry**: Użyj tej opcji, gdy wartość dla bieżącego wiersza pojawia się **w linii powyżej**.
* **Wyodrębnij Z Dole**: Użyj tej opcji, gdy wartość pojawia się **w linii poniżej** bieżącego wiersza.

**Gdzie To Znaleźć**

1. Wejdź w **Tryb szkoleniowy**.
2. Kliknij trzy kropki (⋯) na nagłówku kolumny.
3. W opcji **"Wyodrębnij Z"** wybierz `Z Góry` lub `Z Dole`, w zależności od układu dokumentu.

## 5. Format Kwoty

Niektóre kolumny, takie jak **Ilość** lub **Cena Jednostkowa**, zawierają wartości numeryczne lub daty, które mogą być formatowane zgodnie z różnymi konwencjami w zależności od pochodzenia dokumentu lub lokalizacji. DocBits pozwala określić format, jaki powinny przyjąć te wartości, aby zapewnić dokładną ekstrakcję i interpretację.

**Opcje Formatu Kwoty:**

* Zdefiniuj oczekiwany format liczbowy lub daty dla kolumny, takie jak USA (MM/DD/RRRR, dziesiętny z kropką), Polska (DD.MM.RRRR, dziesiętny z przecinkiem), Niemcy i inne.
* Pomaga to DocBits poprawnie analizować i standaryzować wartości nawet jeśli dokument używa innego regionalnego formatu.

**Gdzie To Znaleźć**

1. Wejdź w **Tryb szkoleniowy**.
2. Kliknij trzy kropki (⋯) na nagłówku obsługiwanej kolumny (np. Ilość, Cena Jednostkowa).
3. W opcji **Format Kwoty** wybierz pożądany format odpowiadający lokalizacji Twojego dokumentu.

## 6. Udoskonalanie Ekstrakcji Tabeli za pomocą Regex

## **Co To Oznacza**

Ta funkcja pozwala zdefiniować regex dla każdego nagłówka tabeli, poprawiając dokładność ekstrakcji i zapewniając poprawne wyniki.

## **Jak To Używać**

1. Otwórz dokument od dostawcy, dla którego chcesz zdefiniować regex.
2.  Przejdź do widoku **Ekstrakcji Tabeli**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Włącz **Tryb szkoleniowy**.
4.  Wybierz nagłówek tabeli, który chcesz ulepszyć, a następnie wybierz **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Pojawi się okno, w którym możesz wprowadzić i zdefiniować swój regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Kliknij **Sprawdź poprawność**, aby zweryfikować regex, a następnie **Zapisz zmiany**, aby je zastosować.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Zapisz regułę i potwierdź**, aby zastosować zmiany.

Aby dowiedzieć się, jak trwale zapisać lub usunąć wyszkolone reguły, zobacz [Zapisywanie i Usuwanie Reguł](save-and-delete-rules.md).

## Kiedy Korzystać z Każdej Funkcji

Użyj tych narzędzi, aby zwiększyć dokładność ekstrakcji i zmniejszyć pracę manualną:

* **Grupowanie**: Gdy opis lub dowolna kolumna obejmuje kilka wierszy i musi być połączona dla jasności.
* **Ręczny Wybór Wierszy**: Gdy wiersze nie są czysto zorganizowane, a części treści trafiają do niewłaściwych kolumn.
* **Mapowanie Kolumn**: Gdy automatycznie wykryte nazwy kolumn nie pasują do Twojej struktury lub wymagają ulepszenia.
* **Reguły Regex**: Gdy nagłówki tabel różnią się nieznacznie w dokumentach od tego samego dostawcy lub OCR wprowadza niekonsekwencje.

## Powiązane przewodniki w tym obszarze

* [Ustawienia zaawansowane](advanced-settings.md) – grupowanie, nagłówki i obsługa dodatkowych wierszy.
* [Definiowanie Tabel i Kolumn](defining-tables-and-columns.md) – tworzenie tabel i kolumn do szkolenia.
* [Zapisywanie i Usuwanie Reguł](save-and-delete-rules.md) – trwałe zastosowanie lub odrzucenie wyszkolonego układu.
