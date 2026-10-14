# Compare two Fields with Tolerance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji poprzez porównanie wartości dwóch określonych pól dokumentu, z dodatkową możliwością zastosowania wartości tolerancji. Funkcja ta umożliwia systemowi uwzględnienie marginesu błędu (tolerancji) podczas porównywania wartości pól, pozwalając na bardziej elastyczne podejmowanie decyzji w przepływach pracy.

## **Komponenty karty:**

1. **Field Name (1)**
   * **Opis:** Określa pierwsze pole dokumentu do porównania.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pierwszego pola w dokumencie.
2. **Operator**
   * **Opis:** Definiuje typ porównania, który ma być wykonany między dwoma polami.
   * **Opcje:**
     * **Equals (=):** Sprawdza, czy wartości dwóch pól są równe.
     * **Not Equals (≠):** Zapewnia, że wartości dwóch pól są różne.
     * **Greater Than (>):** Potwierdza, że wartość pierwszego pola jest większa niż drugiego pola.
     * **Greater or Equals (≥):** Weryfikuje, że wartość pierwszego pola jest równa lub większa niż drugiego pola.
     * **Lesser Than (<):** Sprawdza, czy wartość pierwszego pola jest mniejsza niż drugiego pola.
     * **Less or Equals (≤):** Zapewnia, że wartość pierwszego pola jest mniejsza lub równa drugiemu polu.
3. **Field Name (2)**
   * **Opis:** Określa drugie pole dokumentu do porównania z pierwszym polem.
   * **Szczegóły:** Powinno to odpowiadać dokładnemu identyfikatorowi drugiego pola w dokumencie.&#x20;
4. **Tolerance Amount**
   * **Opis:** Definiuje akceptowalny margines błędu dla porównania.
   * **Szczegóły:** Kwota tolerancji jest wartością liczbową wskazującą maksymalną dopuszczalną różnicę między dwiema wartościami pól, aby porównanie zostało uznane za prawdziwe.
5. **Tolerance Type**
   * **Opis:** Określa jednostkę miary dla kwoty tolerancji.
   * **Opcje:**
     * **Value:** Tolerancja jest wartością bezwzględną, co oznacza, że dwa pola mogą różnić się o określoną kwotę tolerancji.
     * **Percent:** Tolerancja jest obliczana jako procent wartości drugiego pola, dopuszczając względny margines błędu.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia, czy wartości w dwóch określonych polach spełniają warunek porównania, z uwzględnieniem zdefiniowanej tolerancji. Jeśli bezwzględna lub względna różnica między dwoma polami mieści się w tolerancji, warunek jest uznawany za prawdziwy.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:**\
    Jeśli wartości dwóch pól, po uwzględnieniu tolerancji, odpowiadają warunkowi porównania, system wyzwala powiązane akcje. Akcje te mogą obejmować kontynuowanie przepływu pracy, aktualizację rekordów, wyzwalanie alertów lub włączanie określonych operacji.
  * **Warunek fałszywy:**\
    Jeśli wartości dwóch pól, po uwzględnieniu tolerancji, nie odpowiadają określonemu warunkowi, mogą zostać wykonane alternatywne akcje lub żadne, w zależności od konfiguracji przepływu pracy.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając dwa pola do porównania z listy dostępnych pól w systemie. Operator jest wybierany z listy rozwijanej dostępnych opcji porównania. Użytkownicy wprowadzają kwotę tolerancji i wybierają typ tolerancji (value lub percent).&#x20;

## **Podsumowanie:**

Karta przepływu pracy "Compare Two Fields with Tolerance" jest potężnym narzędziem do porównywania pól dokumentu z uwzględnieniem dopuszczalnych odchyleń w danych. Stosując tolerancję do porównań pól, karta ta dodaje elastyczność do przepływu pracy, umożliwiając obsługę rzeczywistych różnic danych. Poprawia podejmowanie decyzji, wspiera walidację danych i zwiększa ogólną automatyzację przepływu pracy.
