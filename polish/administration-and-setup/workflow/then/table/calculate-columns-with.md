# Oblicz kolumny za pomocą

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-aafc18d42905-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Karta przepływu pracy **„Oblicz kolumny w tabeli”** służy do wykonywania obliczeń między kolumnami w wybranej tabeli. Umożliwia użytkownikom wybór kolumn, zastosowanie operacji matematycznej i zapisanie wyniku w określonej kolumnie wynikowej.

## **Komponenty karty:**

1. **Nazwa tabeli**
   * **Opis:** Określa **tabelę**, w której kolumny będą obliczane.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych **tabel**.
2. **Nazwa kolumny (pierwsza kolumna)**
   * **Opis:** Określa **pierwszą kolumnę**, która ma być uwzględniona w obliczeniach.
   * **Szczegóły:** Do wyboru udostępniana jest lista wszystkich dostępnych **kolumna**.
3. **Działanie**
   * **Opis:** Definiuje operację matematyczną, która ma być zastosowana między wybranymi kolumnami.
   * **Opcje:**
     * **Add (+):** Dodaje wartość drugiej kolumny do wartości pierwszej kolumny.
     * **Odejmij (-):** Odejmuje wartość drugiej kolumny od wartości pierwszej kolumny.
     * **Multiply (\*):** Mnoży wartość w pierwszej kolumnie przez wartość w drugiej kolumnie.
     * **Podziel (/):** Dzieli wartość w pierwszej kolumnie przez wartość w drugiej kolumnie.
4. **Nazwa kolumny (druga kolumna)**
   * **Opis:** Określa **drugą kolumnę**, która ma być uwzględniona w obliczeniach.
   * **Szczegóły:** Do wyboru udostępniana jest lista dostępnych **kolumna**.
5. **Kolumna wyników**
   * **Opis:** Określa **kolumnę**, w której zostanie zapisany wynik obliczeń.
   * **Szczegóły:** Udostępniana jest lista dostępnych **kolumna**, w których zostanie zapisana obliczona wartość.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Obliczanie kolumn:**\
  Karta wykonuje wybraną operację matematyczną między dwiema wybranymi kolumnami.
* **Przechowywanie wyniku:**\
  Wynik obliczeń jest przechowywany w wybranej **kolumnie wynikowej**.

## **Konfiguracja:**

* **Wybierz tabelę:**\
  Wybierz **tabelę**, w której kolumny będą obliczane.
* **Wybierz kolumny:**\
  Wybierz **pierwszą kolumnę** i **drugą kolumnę**, które zostaną użyte w obliczeniach.
* **Wybierz operację:**\
  Wybierz operację matematyczną (**Add (+)**, **Odejmij (-)**, **Multiply (\*)**, **Divide (/)**), która ma być zastosowana między kolumnami.
* **Wybierz kolumnę wyników:**\
  Wybierz **kolumnę wynikową**, w której zostanie zapisane obliczenie.

## **Podsumowanie:**

Karta przepływu pracy **„Oblicz kolumny w tabeli”** umożliwia użytkownikom wykonywanie dynamicznych obliczeń między kolumnami w tabeli i przechowywanie wyników w wyznaczonej kolumnie. Karta oferuje elastyczność stosowania różnych operacji matematycznych i zapewnia zapisanie wyniku w określonej kolumnie.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Oblicz sumę wierszy na podstawie ilości i ceny jednostkowej.

**Konfiguracja:** Wybierz tabelę `lines`, kolumny `quantity` i `unit_price`, mnożenie i kolumnę wynikową `line_total`.

**Oczekiwany wynik i kontrprzykład:** Wiersz zawierający `2` i `10` daje `20`. Przetestuj niezależnie inny wiersz i zdiagnozuj brakujące lub nienumeryczne dane wejściowe, zamiast traktować je jako prawidłową sumę.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
