# Any / All Charges

<figure><img src="../../../../.gitbook/assets/workflow_cards_and_po_compare_any_all_charges.png" alt="Karta w bibliotece kart, wersja 2 i wersja 3"><figcaption><p>Karta w bibliotece kart. Wersja 2 powyżej, wersja 3 poniżej.</p></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy porównuje opłaty dodatkowe dokumentu z opłatami dodatkowymi dopasowanego zamówienia zakupu, w ramach określonej tolerancji. Odpowiada na jedno pytanie: czy dokument i zamówienie zakupu są zgodne co do opłat dodatkowych? Porównywana jest każda opłata, którą dopasowanie zamówienia zakupu sparowało, dlatego na karcie nie trzeba podawać żadnej nazwy pola.

Ta karta różni się od **Compare Total Charges**, która porównuje jedno wskazane pole dokumentu z pojedynczą opłatą określoną przez Charge ID. Użyj tej karty, gdy wszystkie sparowane opłaty dokumentu mają zostać sprawdzone naraz.

Dopasowanie zamówienia zakupu musi zostać wykonane przed tą kartą. Jeśli dokument nie ma dopasowanego zamówienia zakupu, karta zatrzymuje przepływ pracy i zgłasza brakujące dane.

## **Elementy karty:**

1. **Dowolny/Wszystkie:**
   * **Opis**: Jak poszczególne porównania opłat są łączone w jeden wynik karty.
   * **Opcje**:
     * **Każdy**: co najmniej jedna opłata musi spełnić porównanie.
     * **Wszystko**: każda opłata musi spełnić porównanie.
2. **Operator:**
   * **Opis**: Jak kwota opłaty z dokumentu jest porównywana z kwotą zamówienia zakupu dla tej samej opłaty.
   * **Opcje**:
     * **w**: obie kwoty muszą być zgodne, z uwzględnieniem tolerancji.
     * **Poza**: obie kwoty muszą różnić się o więcej niż tolerancja.
3. **Ilość tolerancji:**
   * **Opis**: Dopuszczalne odchylenie między opłatą dokumentu a opłatą zamówienia zakupu.
4. **Typ tolerancji:**
   * **Opis**: Jak interpretowana jest ilość tolerancji.
   * **Opcje**:
     * **Procent**: procent opłaty zamówienia zakupu.
     * **Wartość**: kwota stała.
5. **Zachowanie przy brakujących danych (tylko wersja 3):**
   * **Opis**: Co zrobić, gdy opłata istnieje tylko z jednej strony, w dokumencie albo w zamówieniu zakupu, tak że nie ma odpowiednika do porównania. Opcja znajduje się na końcu zdania wersji 3.
   * **Opcje**:
     * **traktować jako niedopasowanie**: przepływ pracy zostaje zatrzymany. To ustawienie domyślne.
     * **zignoruj to i traktuj jako dopasowanie**: przepływ pracy jest kontynuowany, jak gdyby opłata była zgodna.

## **Funkcjonalność:**

Karta przechodzi przez następujące kroki.

1. **Wymaga dopasowanego zamówienia zakupu.** Bez dopasowanego zamówienia zakupu karta zatrzymuje się natychmiast i zgłasza brakujące dane.
2. **Odczytuje tolerancję** z **Ilość tolerancji** i **Typ tolerancji** na karcie.
3. **Wersja 3 przypisuje każdą dopasowaną pozycję zamówienia zakupu** do jednej z czterech sytuacji, pytając wyłącznie, czy dana strona ma jakiekolwiek opłaty: opłaty po obu stronach, brak opłat po obu stronach, opłaty tylko w dokumencie albo opłaty tylko w zamówieniu zakupu. Pozycja, której nie da się powiązać z danymi zamówienia zakupu w dokumencie, jest błędem danych i karta zatrzymuje się.
4. **Opłata obecna tylko po jednej stronie decyduje o całej karcie.** Gdy jedna dopasowana pozycja ma opłaty po jednej stronie i żadnych po drugiej, **Zachowanie przy brakujących danych** decyduje o wyniku i żadna opłata nie jest porównywana, również opłaty pozycji poprawnie sparowanych. Operator i tolerancja nie są brane pod uwagę.
5. **Jeśli żadna pozycja nie ma opłat po żadnej ze stron**, obie strony są zgodne, że nie ma opłat dodatkowych. Operator **Poza** nie jest wtedy spełniony, ponieważ nic nie odbiega poza tolerancję, i przepływ pracy zostaje zatrzymany. Każdy inny operator uznaje zgodność za spełnioną i przepływ pracy jest kontynuowany. **Zachowanie przy brakujących danych** nie ma tu żadnego wpływu.
6. **W przeciwnym razie każda opłata jest porównywana**, kwota dokumentu z kwotą zamówienia zakupu, przy użyciu operatora i tolerancji. Kwota opłaty, która nie jest liczbą, zatrzymuje kartę z brakującymi danymi.
7. **Porównania są zbierane i łączone jednorazowo.** Każda opłata każdej dopasowanej pozycji wchodzi do jednego zbioru wyników, który ustawienie **Dowolny/Wszystkie** redukuje do jednego wyniku karty. Zbieranie odbywa się w skali dokumentu, nie na pozycję, dlatego **Każdy** oznacza dowolną opłatę w dowolnym miejscu dokumentu. Jeśli połączony wynik jest prawdziwy, przepływ pracy jest kontynuowany, w przeciwnym razie zatrzymuje się na niespełnionym warunku.

Przed skonfigurowaniem karty warto znać trzy konsekwencje.

* **w z tolerancją 0 wymaga dokładnej równości.** Obie kwoty muszą być zgodne co do groszy.
* **Opłata obecna tylko po jednej stronie ma pierwszeństwo nad wszystkim innym.** Ponieważ krok 4 wykonuje się przed jakimkolwiek porównaniem, **zignoruj to i traktuj jako dopasowanie** pomija także sprawdzenie kwot każdej poprawnie sparowanej opłaty w dokumencie. Zachowaj **traktować jako niedopasowanie**, jeśli kwoty mają być weryfikowane.
* **traktować jako niedopasowanie zatrzymuje przepływ pracy jako błąd, a nie jako niespełniony warunek.** Wbrew brzmieniu karta zgłasza brakujące dane, co dziennik przepływu pracy i test karty pokazują na czerwono, a nie na pomarańczowo jak niespełniony warunek. Przepływ pracy zatrzymuje się w obu przypadkach.

## **Instalacja i konfiguracja:**

Dodaj kartę jako warunek And po dopasowaniu zamówienia zakupu. Wybierz, czy każda opłata czy dowolna opłata musi spełnić porównanie, wybierz operator **w** albo **Poza** i wprowadź ilość oraz typ tolerancji. W wersji 3 wybierz, co ma się stać, gdy opłaty występują tylko po jednej stronie.

Aby wypróbować konfigurację bez czekania na dokument, otwórz menu karty w Workflow Builder, wybierz **Karta testowa**, wybierz dokument, a następnie **Test na dokumencie**. Dziennik karty wymienia każdą porównaną opłatę z obiema kwotami, operatorem i użytą tolerancją, a także zapisuje, która wartość **Zachowanie przy brakujących danych** zdecydowała o wyniku, gdy opłata była obecna tylko po jednej stronie.

## **Przykładowy scenariusz:**

Potwierdzenie zamówienia zawiera opłatę transportową 100,00, a dopasowana pozycja zamówienia zakupu zawiera tę samą opłatę transportową 100,00. Przy **Wszystko**, operatorze **w** i tolerancji 0 jako wartości kwoty są równe, karta jest spełniona i przepływ pracy jest kontynuowany.

Przy 120,00 na potwierdzeniu zamówienia wobec 100,00 w zamówieniu zakupu ta sama konfiguracja nie jest spełniona i przepływ pracy zatrzymuje się na niespełnionym warunku.

Jeśli ani potwierdzenie zamówienia, ani zamówienie zakupu nie zawiera żadnej opłaty, operator **w** uznaje to za zgodność i przepływ pracy jest kontynuowany, natomiast **Poza** go zatrzymuje.

Jeśli potwierdzenie zamówienia zawiera opłatę transportową, a zamówienie zakupu żadnej, operator przestaje mieć zastosowanie. Przy **traktować jako niedopasowanie** przepływ pracy zatrzymuje się, aby ktoś mógł sprawdzić, dlaczego opłata występuje tylko po jednej stronie.

## **Różnice między wersjami:**

Wersję 3 stosują nowe karty. Wersja 2 pozostaje wspierana w istniejących przepływach pracy. Obie wersje porównują opłatę po opłacie i łączą wyniki w skali dokumentu ustawieniem **Dowolny/Wszystkie**, ale wersja 2 nie ma klasyfikacji przypadków, co zmienia to, co się dzieje, gdy opłaty nie są obecne po obu stronach:

* Wersja 2 nie ma opcji **Zachowanie przy brakujących danych**. Jej zdanie kończy się po typie tolerancji.
* Wersja 2 nie klasyfikuje dopasowanych pozycji i dlatego nie rozpoznaje opłaty istniejącej tylko po jednej stronie. Porównuje obecną kwotę z 0,00 przyjętym dla brakującej strony, a decyduje operator: **w** nie jest spełniony i przepływ pracy zatrzymuje się, **Poza** jest spełniony i przepływ pracy jest kontynuowany. Dziennik karty pokazuje porównanie z 0,00.
* Jeśli żadna ze stron nie zawiera opłat, wersja 2 nie ma czego porównywać i zgłasza brakujące dane, zamiast uznać brak po obu stronach za zgodność.

## **Wnioski:**

Karta "Any / All Charges" automatyzuje sprawdzenie, że zafakturowane lub potwierdzone opłaty dodatkowe odpowiadają zamówionym opłatom dodatkowym. Ponieważ brak opłat po obu stronach liczy się w wersji 3 jako zgodność, dokumenty bez opłat dodatkowych przechodzą bez ręcznej interwencji, natomiast opłaty występujące tylko po jednej stronie są wstrzymywane do weryfikacji, o ile nie zostanie to celowo dopuszczone.
