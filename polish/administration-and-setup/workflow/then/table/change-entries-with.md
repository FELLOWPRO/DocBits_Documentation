# Change Entries with

<figure><img src="../../../../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Change Entries in Table"** służy do aktualizacji wpisów w określonej tabeli bazy danych. Umożliwia wybór **tabeli** i **kolumny**, a następnie wykonanie operacji matematycznych (dodawanie, odejmowanie, mnożenie lub dzielenie) na wartościach w tej kolumnie, przy użyciu określonej wartości.

## **Komponenty karty:**

1. **Table Name**
   * **Opis:** Określa **tabelę**, w której wpisy zostaną zaktualizowane.
   * **Szczegóły:** Udostępniana jest lista rozwijana dostępnych **tabel**, umożliwiająca wybór docelowej tabeli do aktualizacji wpisów.
2. **Column Name**
   * **Opis:** Określa **kolumnę** w wybranej tabeli, która ma zostać zaktualizowana.
   * **Szczegóły:** Do wyboru udostępniana jest lista wszystkich dostępnych **kolumn**.
3. **Operation**
   * **Opis:** Definiuje operację matematyczną, która ma być wykonana na wartościach **kolumny**.
   * **Opcje:**
     * **Add (+):** Dodaje określoną **wartość** do bieżącej wartości w wybranej kolumnie.
     * **Subtract (-):** Odejmuje określoną **wartość** od bieżącej wartości w wybranej kolumnie.
     * **Multiply (\*):** Mnoży bieżącą wartość w wybranej kolumnie przez określoną **wartość**.
     * **Divide (/):** Dzieli bieżącą wartość w wybranej kolumnie przez określoną **wartość**.
4. **Value**
   * **Opis:** Określa **wartość**, która ma być użyta w wybranej operacji.
   * **Szczegóły:** Jest to liczba, która zostanie dodana, odjęta, pomnożona lub podzielona z wpisami w wybranej kolumnie.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Aktualizacja wpisu tabeli:**\
  Karta wykonuje wybraną operację (**+**, **-**, **\*** lub **/**) na wartościach w wybranej **kolumnie** wybranej **tabeli**, używając określonej **wartości**.

## **Konfiguracja:**

* **Select Table:**\
  Wybierz **tabelę**, w której zostaną zastosowane zmiany.
* **Choose Column:**\
  Wybierz **kolumnę** w tabeli, którą chcesz zaktualizować.
* **Select Operation:**\
  Wybierz operację matematyczną (**+**, **-**, **\***, **/**), która ma być zastosowana do wartości wybranej kolumny.
* **Enter Value:**\
  Podaj **wartość**, która ma być użyta w wybranej operacji.

## **Podsumowanie:**

Karta przepływu pracy **"Change Entries in Table"** umożliwia zautomatyzowane aktualizacje wpisów w bazie danych poprzez wybór **tabeli**, **kolumny** i żądanej **operacji matematycznej**. Karta ta jest niezbędna do wykonywania zbiorczych modyfikacji danych lub obliczeń w bazie danych.
