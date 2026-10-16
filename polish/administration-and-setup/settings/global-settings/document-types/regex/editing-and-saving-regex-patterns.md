# Edytowanie i zapisywanie wzorców wyrażeń regularnych

## Przewodnik po modyfikowaniu istniejących wzorców oraz znaczeniu testowania tych zmian, aby upewnić się, że działają zgodnie z oczekiwaniami bez naruszania istniejącej funkcjonalności.

**Aby edytować istniejące wzorce wyrażeń regularnych i upewnić się, że zmiany działają zgodnie z oczekiwaniami bez naruszania istniejącej funkcjonalności, możesz skorzystać z poniższego przewodnika:**

<figure><img src="../../../../../.gitbook/assets/image (94).png" alt=""><figcaption><p>Settings: Document Type</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 14.18.25.png" alt=""><figcaption></figcaption></figure>

**Przeanalizuj istniejący wzorzec:**

* Zbadaj istniejący wzorzec wyrażenia regularnego, aby zrozumieć, jakie dane przechwytuje i jak działa.
* Zidentyfikuj części wzorca, które wymagają zmiany, oraz wpływ tych zmian na przechwytywane dane.

**Na przykład: ma zostać odczytana kwota faktury:**

*   (?<=Rechnungsbetrag:)\[\s]\*((((\d+)\[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Odczytaj kwotę z kropką jako separatorem tysięcy, ale NIE przepuszczaj kropki

    \[\d.]_\[,\d]_

    Dozwolone znaki: 0123456789,
*   Ma zostać odczytana wartość "P32180". Słowem kotwiczącym jest tutaj "Invoice Date".

    (?<=InvoiceDate )\[\s]\*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

**Udokumentuj zmiany:**

* Zapisz notatki o zmianach, które planujesz wprowadzić we wzorcu wyrażenia regularnego.
* Zanotuj, jakie nowe wzorce planujesz dodać oraz które części istniejącego wzorca mogą wymagać zmiany lub usunięcia.

**Przygotuj dane testowe:**

* Zbierz dane testowe reprezentatywne dla różnych typów danych, które wzorzec wyrażenia regularnego zazwyczaj przechwytuje.
* Upewnij się, że dane testowe obejmują zarówno typowe przypadki, jak i przypadki brzegowe, aby sprawdzić odporność wprowadzonych zmian.

**Wprowadź zmiany we wzorcu wyrażenia regularnego:**

* Wprowadź zaplanowane zmiany we wzorcu wyrażenia regularnego.
* Może to obejmować dodanie nowych wzorców, usunięcie lub dostosowanie istniejących części albo optymalizację wzorca w celu lepszej wydajności.

**Przetestuj zmiany:**

* Zastosuj zaktualizowany wzorzec wyrażenia regularnego do swoich danych testowych i uważnie sprawdź wyniki.
* Sprawdź, czy wzorzec nadal poprawnie przechwytuje pożądane dane i czy nie ma nieoczekiwanego wpływu na inne części danych lub systemu.

**Debugowanie i dostosowywanie:**

* Jeśli wyniki testów nie są zgodne z oczekiwaniami lub pojawiają się nieoczekiwane problemy, uważnie przejrzyj wprowadzone zmiany i w razie potrzeby wprowadź dalsze poprawki.
* Może to obejmować cofnięcie niektórych zmian lub dodanie dodatkowych korekt w celu rozwiązania problemu.

**Udokumentuj zmiany:**

* Zaktualizuj dokumentację swojego wzorca wyrażenia regularnego, aby odzwierciedlała wprowadzone zmiany.
* Opisz zaktualizowane wzorce i powody wprowadzonych zmian, aby pomóc innym programistom zrozumieć wzorzec i z niego korzystać.

**Zapisz zmiany:**

* Gdy upewnisz się, że zmiany zakończyły się powodzeniem i działają zgodnie z oczekiwaniami, zapisz zaktualizowany wzorzec wyrażenia regularnego w swojej bazie kodu lub plikach konfiguracyjnych, aby był dostępny do przyszłego użytku.

<figure><img src="../../../../../.gitbook/assets/image (109).png" alt=""><figcaption><p>Save Changes</p></figcaption></figure>

Postępując zgodnie z tymi krokami i starannie testując zmiany we wzorcach wyrażeń regularnych, możesz zapewnić, że Twój wzorzec nadal będzie działał poprawnie, spełniając jednocześnie nowe wymagania.
