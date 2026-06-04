# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania wartości pola z określoną wartością referencyjną, dopuszczając tolerancje. Umożliwia precyzyjne przetwarzanie warunkowe w przepływach pracy, w których akceptowalne są niewielkie odchylenia, co czyni ją idealną dla scenariuszy takich jak zapewnienie jakości, analiza finansowa lub akcje oparte na progach.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Pole, które ma być oceniane w porównaniu.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pierwszego pola w dokumencie.
2. **Comparison Operator**
   * **Opis:** Określa, w jaki sposób wartość wybranego pola zostanie porównana z wartością referencyjną.
   * **Opcje:**
     * **Equals (=):** Weryfikuje, czy wartość pola dokładnie odpowiada wartości referencyjnej.
     * **Not Equals (≠):** Weryfikuje, czy wartość pola nie odpowiada wartości referencyjnej.
     * **Greater Than (>):** Sprawdza, czy wartość pola jest większa niż wartość referencyjna.
     * **Greater or Equals (≥):** Sprawdza, czy wartość pola jest większa lub równa wartości referencyjnej.
     * **Lesser Than (<):** Sprawdza, czy wartość pola jest mniejsza niż wartość referencyjna.
     * **Lesser or Equals (≤):** Sprawdza, czy wartość pola jest mniejsza lub równa wartości referencyjnej.
3. **Reference Value**
   * **Opis:** Wartość, z którą porównywane jest pole.
   * **Szczegóły:** Wartość ta może być liczbowa, tekstowa lub oparta na dacie, w zależności od kontekstu porównania.
4. **Tolerance Amount**
   * **Opis:** Definiuje akceptowalny margines błędu dla porównania.
   * **Szczegóły:** Kwota tolerancji jest wartością liczbową wskazującą maksymalną dopuszczalną różnicę między dwiema wartościami pól, aby porównanie zostało uznane za prawdziwe.
5. **Tolerance Type**
   * **Opis:** Określa jednostkę miary dla kwoty tolerancji.
   * **Opcje:**
     * **Value:** Tolerancja jest wartością bezwzględną, co oznacza, że dwa pola mogą różnić się o określoną kwotę tolerancji.
     * **Percent:** Tolerancja jest obliczana jako procent wartości drugiego pola, dopuszczając względny margines błędu.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia wartość pola względem wartości referencyjnej za pomocą wybranego operatora porównania. Jeśli skonfigurowana jest tolerancja, system uznaje porównanie za pomyślne, jeśli wartość pola mieści się w zdefiniowanym zakresie tolerancji.
* **Wykonanie akcji:**
  * **W zakresie tolerancji:** Jeśli wartość pola spełnia warunek w ramach określonej tolerancji, przepływ pracy jest kontynuowany, wyzwalając powiązane akcje.
  * **Poza tolerancją:** Jeśli wartość pola nie spełnia warunku lub znajduje się poza zakresem tolerancji, mogą zostać wykonane alternatywne akcje, takie jak rejestrowanie, wysyłanie alertów lub zatrzymanie przepływu pracy.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając pole do oceny z listy dostępnych pól i wybierając operator porównania (np. równe, większe niż) z listy rozwijanej. Następnie określają wartość referencyjną do porównania i definiują kwotę tolerancji, a potem wybierają typ tolerancji (np. procent lub wartość).&#x20;

## **Podsumowanie:**

Karta "Field Comparison with Tolerances" jest wszechstronnym narzędziem dla przepływów pracy wymagających elastycznych ocen. Umożliwiając porównania z tolerancjami, zapewnia, że przepływy pracy pozostają wydajne i elastyczne, uwzględniając rzeczywiste różnice bez utraty dokładności.
