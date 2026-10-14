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

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

Początkowo DocBits wyodrębnia każdy wiersz osobno:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Następnie możesz **grupować wiersze na podstawie kolumny**, takiej jak "Pozycja". To połączy powiązane linie w jedno, uporządkowane wpisy:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Ręczny Wybór Wierszy

W niektórych przypadkach tekst na dokumencie jest rozłożony na kilka kolumn w jednym wierszu, co sprawia, że trudno jest przypisać go automatycznie.

Oto przykład, gdzie linia "PRAEF" nakłada się na **Bezeichnung**, **Menge**, **ME** i **Preis in EUR**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

### Jak Ręcznie Przypisać Wartości:

1.  **Włącz Tryb Szkoleniowy**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)
2.  **Aktywuj Tryb Edycji Wiersza**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)
3.  **Wybierz i Mapuj Tekst** Kliknij odpowiedni fragment tekstu i przypisz go do **niebieskiego** nagłówka kolumny.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Uwaga: Kolumny o fiolecie są już zmapowane przez system i nie mogą być edytowane ręcznie.

## 3. Mapowanie Kolumn

Mapowanie kolumn łączy wyekstrahowane dane z oczekiwanymi nagłówkami kolumn, zapewniając spójność i możliwość eksportu.

Aby zmapować lub ponownie zmapować kolumnę:

1. Kliknij nagłówek kolumny w widoku ekstrakcji.
2. Wybierz właściwą kolumnę docelową z rozwijanego menu.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

Możesz dostosować mapowanie tak często, jak jest to potrzebne.

## 4. Wyodrębnianie Z Góry / Z Dole

Niektóre dokumenty są zorganizowane w taki sposób, że istotne wartości tabeli nie pojawiają się w tym samym wierszu co inne dane. W takich przypadkach DocBits pozwala kontrolować **skąd dane powinny być wyodrębnione**:

* **Wyodrębnij Z Góry**: Użyj tej opcji, gdy wartość dla bieżącego wiersza pojawia się **w linii powyżej**.
* **Wyodrębnij Z Dole**: Użyj tej opcji, gdy wartość pojawia się **w linii poniżej** bieżącego wiersza.

**Gdzie To Znaleźć**

1. Wejdź w **Tryb Szkoleniowy**.
2. Kliknij trzy kropki (⋯) na nagłówku kolumny.
3. W opcji **"Wyodrębnij Z"** wybierz `Z Góry` lub `Z Dole`, w zależności od układu dokumentu.

## 5. Format Kwoty

Niektóre kolumny, takie jak **Ilość** lub **Cena Jednostkowa**, zawierają wartości numeryczne lub daty, które mogą być formatowane zgodnie z różnymi konwencjami w zależności od pochodzenia dokumentu lub lokalizacji. DocBits pozwala określić format, jaki powinny przyjąć te wartości, aby zapewnić dokładną ekstrakcję i interpretację.

**Opcje Formatu Kwoty:**

* Zdefiniuj oczekiwany format liczbowy lub daty dla kolumny, takie jak USA (MM/DD/RRRR, dziesiętny z kropką), Polska (DD.MM.RRRR, dziesiętny z przecinkiem), Niemcy i inne.
* Pomaga to DocBits poprawnie analizować i standaryzować wartości nawet jeśli dokument używa innego regionalnego formatu.

**Gdzie To Znaleźć**

1. Wejdź w **Tryb Szkoleniowy**.
2. Kliknij trzy kropki (⋯) na nagłówku obsługiwanej kolumny (np. Ilość, Cena Jednostkowa).
3. W opcji **Format Kwoty** wybierz pożądany format odpowiadający lokalizacji Twojego dokumentu.

## 6. Udoskonalanie Ekstrakcji Tabeli za pomocą Regex

## **Co To Oznacza**

Ta funkcja pozwala zdefiniować regex dla każdego nagłówka tabeli, poprawiając dokładność ekstrakcji i zapewniając poprawne wyniki.

## **Jak To Używać**

1. Otwórz dokument od dostawcy, dla którego chcesz zdefiniować regex.
2.  Przejdź do widoku **Ekstrakcji Tabeli**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Włącz **Tryb Szkoleniowy**.
4.  Wybierz nagłówek tabeli, który chcesz ulepszyć, a następnie wybierz **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Pojawi się okno, w którym możesz wprowadzić i zdefiniować swój regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Kliknij **Sprawdź poprawność**, aby zweryfikować regex, a następnie **Zapisz zmiany**, aby je zastosować.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Zapisz regułę i potwierdź**, aby zastosować zmiany.

## Kiedy Korzystać z Każdej Funkcji

Użyj tych narzędzi, aby zwiększyć dokładność ekstrakcji i zmniejszyć pracę manualną:

* **Grupowanie**: Gdy opis lub dowolna kolumna obejmuje kilka wierszy i musi być połączona dla jasności.
* **Ręczny Wybór Wierszy**: Gdy wiersze nie są czysto zorganizowane, a części treści trafiają do niewłaściwych kolumn.
* **Mapowanie Kolumn**: Gdy automatycznie wykryte nazwy kolumn nie pasują do Twojej struktury lub wymagają ulepszenia.
* **Reguły Regex**: Gdy nagłówki tabel różnią się nieznacznie w dokumentach od tego samego dostawcy lub OCR wprowadza niekonsekwencje.
