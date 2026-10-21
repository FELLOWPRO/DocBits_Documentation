# Zmień wpisy za pomocą

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-2186644bde72-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Change Entries in Table"** służy do aktualizacji wpisów w określonej tabeli bazy danych. Umożliwia wybór **tabeli** i **kolumny**, a następnie wykonanie operacji matematycznych (dodawanie, odejmowanie, mnożenie lub dzielenie) na wartościach w tej kolumnie, przy użyciu określonej wartości.

## **Komponenty karty:**

1. **Nazwa tabeli**
   * **Opis:** Określa **tabelę**, w której wpisy zostaną zaktualizowane.
   * **Szczegóły:** Udostępniana jest lista rozwijana dostępnych **tabel**, umożliwiająca wybór docelowej tabeli do aktualizacji wpisów.
2. **Nazwa kolumny**
   * **Opis:** Określa **kolumnę** w wybranej tabeli, która ma zostać zaktualizowana.
   * **Szczegóły:** Do wyboru udostępniana jest lista wszystkich dostępnych **kolumna**.
3. **Działanie**
   * **Opis:** Definiuje operację matematyczną, która ma być wykonana na wartościach **kolumny**.
   * **Opcje:**
     * **Add (+):** Dodaje określoną **wartość** do bieżącej wartości w wybranej kolumnie.
     * **Odejmij (-):** Odejmuje określoną **wartość** od bieżącej wartości w wybranej kolumnie.
     * **Multiply (\*):** Mnoży bieżącą wartość w wybranej kolumnie przez określoną **wartość**.
     * **Podziel (/):** Dzieli bieżącą wartość w wybranej kolumnie przez określoną **wartość**.
4. **Wartość**
   * **Opis:** Określa **wartość**, która ma być użyta w wybranej operacji.
   * **Szczegóły:** Jest to liczba, która zostanie dodana, odjęta, pomnożona lub podzielona z wpisami w wybranej kolumnie.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Aktualizacja wpisu tabeli:**\
  Karta wykonuje wybraną operację (**+**, **-**, **\*** lub **/**) na wartościach w wybranej **kolumnie** wybranej **tabeli**, używając określonej **wartości**.

## **Konfiguracja:**

* **Wybierz tabelę:**\
  Wybierz **tabelę**, w której zostaną zastosowane zmiany.
* **Wybierz kolumnę:**\
  Wybierz **kolumnę** w tabeli, którą chcesz zaktualizować.
* **Wybierz operację:**\
  Wybierz operację matematyczną (**+**, **-**, **\***, **/**), która ma być zastosowana do wartości wybranej kolumny.
* **Wprowadź wartość:**\
  Podaj **wartość**, która ma być użyta w wybranej operacji.

## **Podsumowanie:**

Karta przepływu pracy **"Change Entries in Table"** umożliwia zautomatyzowane aktualizacje wpisów w bazie danych poprzez wybór **tabeli**, **kolumny** i żądanej **operacji matematycznej**. Karta ta jest niezbędna do wykonywania zbiorczych modyfikacji danych lub obliczeń w bazie danych.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Zastosuj korektę numeryczną do istniejącej kolumny tabeli.

**Konfiguracja:** Wybierz tabelę demonstracyjną `lines`, kolumnę numeryczną `quantity`, dodatek i wartość `1`.

**Oczekiwany wynik i kontrprzykład:** Istniejąca ilość `2` staje się `3`. Powtarzanie tej czynności daje `4`, więc używaj jej tylko wtedy, gdy planowane jest wielokrotne dodawanie.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
