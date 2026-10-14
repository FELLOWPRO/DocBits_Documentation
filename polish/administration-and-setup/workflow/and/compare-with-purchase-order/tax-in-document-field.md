# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do oceny, czy wartość podatku w polu dokumentu odpowiada wartości podatku w zamówieniu zakupu, z uwzględnieniem tolerancji opartych na charge ID. Karta porównuje te dwie wartości podatku (jedną z pola dokumentu i jedną z zamówienia zakupu) i sprawdza, czy spełniają określony warunek (np. równe, większe niż, mniejsze niż itp.). Pomaga to zapewnić spójność wartości podatku i oznaczać rozbieżności do dalszego przeglądu lub zatwierdzenia w przepływach pracy zakupowych.

## **Komponenty karty:**

1. **Field Name**
   * **Opis**: Określa pole dokumentu zawierające wartość podatku do porównania z wartością podatku w zamówieniu zakupu.
   * **Szczegóły**: To pole musi odpowiadać dokładnemu identyfikatorowi wartości podatku w dokumencie.
2. **Operator**
   * **Opis**: Definiuje warunek, który ma być zastosowany do porównania między wartością podatku w dokumencie a wartością podatku w zamówieniu zakupu.
   * **Opcje**:
     * **Equals (=)**: Sprawdza, czy podatek w polu dokumentu odpowiada podatkowi w zamówieniu zakupu.
     * **Not Equals (≠)**: Zapewnia, że podatek w polu dokumentu nie odpowiada podatkowi w zamówieniu zakupu.
     * **Greater Than (>)**: Weryfikuje, czy podatek w polu dokumentu jest większy niż podatek w zamówieniu zakupu.
     * **Greater or Equals (≥)**: Sprawdza, czy podatek w polu dokumentu jest większy lub równy podatkowi w zamówieniu zakupu.
     * **Lesser Than (<)**: Weryfikuje, czy podatek w polu dokumentu jest mniejszy niż podatek w zamówieniu zakupu.
     * **Lesser or Equals (≤)**: Sprawdza, czy podatek w polu dokumentu jest mniejszy lub równy podatkowi w zamówieniu zakupu.
3. **Master Data Table**
   * **Opis**: Tabela zawierająca szczegóły zamówienia zakupu, w tym charge ID i wartości podatku.
   * **Szczegóły**: Ta tabela musi mieć odniesienie do charge ID powiązanego z wartością podatku zamówienia zakupu.
4. **Tolerance Amount**
   * **Opis**: Próg kwoty, w ramach którego wartości podatku mogą się różnić. Służy to uwzględnieniu drobnych rozbieżności w obliczeniach podatku.
   * **Szczegóły**: Kwota tolerancji powinna być wartością liczbową, definiującą maksymalną dozwoloną różnicę między wartościami podatku.
5. **Tolerance Type**
   * **Opis**: Określa typ stosowanej tolerancji, bezwzględnej lub procentowej.
   * **Opcje**:
     * **Value**: Tolerancja jest stałą wartością liczbową.
     * **Percentage**: Tolerancja jest obliczana jako procent wartości podatku.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia, czy wartość podatku w polu dokumentu spełnia określony warunek w porównaniu z wartością podatku w zamówieniu zakupu (z odniesieniem do charge ID z tabeli danych podstawowych). Kwota i typ tolerancji są uwzględniane w tej ocenie, aby umożliwić drobne różnice w obliczeniach podatku.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli podatek w polu dokumentu spełnia warunek w porównaniu z podatkiem zamówienia zakupu (w ramach kwoty i typu tolerancji), przepływ pracy jest kontynuowany.
  * **Warunek fałszywy**: Jeśli podatek w polu dokumentu nie spełnia warunku (albo nie mieści się w zakresie tolerancji, albo porównanie się nie powiedzie), przepływ pracy zostanie zatrzymany.

## **Konfiguracja:**

* Użytkownicy muszą wybrać pole dokumentu zawierające wartość podatku do porównania. Następnie wybierają operator określający sposób przeprowadzenia porównania (np. równe, większe niż). Po tym użytkownicy muszą określić odniesienie do tabeli danych podstawowych oraz ustawić kwotę i typ tolerancji, aby uwzględnić drobne rozbieżności podatkowe.

## **Przykładowy scenariusz:**

* Faktura wymienia kwotę podatku 100 USD. Odpowiadające zamówienie zakupu, znajdujące się w tabeli danych podstawowych, określa wartość podatku 95 USD. Przy użyciu operatora "Greater Than" system porównuje wartość podatku dokumentu (100 USD) z wartością podatku zamówienia zakupu (95 USD) z tolerancją 10 USD (typ tolerancji bezwzględny). Ponieważ różnica 5 USD mieści się w zakresie tolerancji, przepływ pracy jest kontynuowany bez wyzwalania alertów.

## **Podsumowanie:**

Karta przepływu pracy "Tax in Document Field Comparison" zapewnia, że wartości podatku w dokumentach są zgodne ze szczegółami zamówienia zakupu, dopuszczając drobne rozbieżności na podstawie określonych tolerancji. Automatyzując tę kontrolę, organizacje mogą zminimalizować błędy w obliczeniach podatku i usprawnić procesy zakupowe, redukując potrzebę ręcznej interwencji lub zatwierdzeń.
