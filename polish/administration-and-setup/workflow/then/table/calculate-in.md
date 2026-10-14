# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Calculate with Regex Dependency"** umożliwia użytkownikom wykonywanie obliczeń między kolumnami w wybranej tabeli, z dodatkowym warunkiem opartym na wzorcu wyrażenia regularnego (regex) zastosowanym do kolumny zależności. Jeśli wzorzec pasuje, obliczenie jest wykonywane, a wynik jest przechowywany w określonej kolumnie wynikowej.

## **Komponenty karty:**

1. **Table Name**
   * **Opis:** Określa **tabelę**, w której kolumny będą obliczane.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych **tabel**.
2. **Column Name (1st Column)**
   * **Opis:** Określa **pierwszą kolumnę** uwzględnioną w obliczeniach.
   * **Szczegóły:** Do wyboru udostępniana jest lista wszystkich dostępnych **kolumn**.
3. **Operation**
   * **Opis:** Definiuje operację matematyczną, która ma być zastosowana między wybranymi kolumnami.
   * **Opcje:**
     * **Add (+):** Dodaje wartość drugiej kolumny do wartości pierwszej kolumny.
     * **Subtract (-):** Odejmuje wartość drugiej kolumny od pierwszej kolumny.
     * **Multiply (\*):** Mnoży wartość pierwszej kolumny przez wartość w drugiej kolumnie.
     * **Divide (/):** Dzieli wartość pierwszej kolumny przez drugą kolumnę.
4. **Column Name (2nd Column)**
   * **Opis:** Określa **drugą kolumnę** uwzględnioną w obliczeniach.
   * **Szczegóły:** Do wyboru udostępniana jest lista wszystkich dostępnych **kolumn**.
5. **Column Name (Dependency)**
   * **Opis:** Określa **kolumnę zależności**, do której zostanie zastosowany wzorzec regex.
   * **Szczegóły:** Do dopasowania wzorca udostępniana jest lista wszystkich dostępnych **kolumn**.
6. **Regex Pattern**
   * **Opis:** Definiuje **wzorzec regex**, który zostanie użyty do dopasowania względem kolumny zależności.
   * **Szczegóły:** Jeśli wartość w kolumnie zależności odpowiada wzorcowi regex, obliczenie zostanie wykonane.
7. **Result Column**
   * **Opis:** Określa **kolumnę wynikową**, w której zostanie zapisany wynik obliczeń.
   * **Szczegóły:** Może to być nowa lub istniejąca kolumna, w której zostanie zapisana obliczona wartość.

## **Funkcjonalność:**

* **Ocena warunku:**
  * Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
  * Karta wykonuje swoją akcję tylko wtedy, gdy wartość w kolumnie zależności odpowiada podanemu **wzorcowi regex**.
* **Obliczanie kolumn:**\
  Jeśli wzorzec regex pasuje, karta wykonuje wybraną operację matematyczną między dwiema wybranymi kolumnami.
* **Przechowywanie wyniku:**\
  Wynik obliczeń jest przechowywany w wybranej **kolumnie wynikowej**.

## **Konfiguracja:**

* **Select Table:**\
  Wybierz **tabelę**, w której kolumny będą obliczane.
* **Choose Columns:**\
  Wybierz **pierwszą kolumnę** i **drugą kolumnę**, które zostaną użyte w obliczeniach.
* **Select Operation:**\
  Wybierz operację matematyczną (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**), która ma być zastosowana między kolumnami.
* **Select Dependency Column:**\
  Wybierz **kolumnę zależności**, do której zostanie zastosowany wzorzec regex.
* **Define Regex Pattern:**\
  Wprowadź **wzorzec regex**, któremu powinna odpowiadać kolumna zależności.
* **Select Result Column:**\
  Wybierz **kolumnę wynikową**, w której zostanie zapisana obliczona wartość.

## **Podsumowanie:**

Karta przepływu pracy **"Calculate with Regex Dependency"** zapewnia potężny sposób wykonywania obliczeń z logiką warunkową opartą na wzorcu regex. Zapewnia to, że tylko wiersze, w których kolumna zależności odpowiada określonemu wzorcowi, zostaną poddane określonemu obliczeniu, a wynik jest przechowywany w wybranej kolumnie wynikowej.
