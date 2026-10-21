# Porównaj pole z tolerancjami

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-4ee291b0848d-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania wartości pola z określoną wartością referencyjną, dopuszczając tolerancje. Umożliwia precyzyjne przetwarzanie warunkowe w przepływach pracy, w których akceptowalne są niewielkie odchylenia, co czyni ją idealną dla scenariuszy takich jak zapewnienie jakości, analiza finansowa lub akcje oparte na progach.

## **Komponenty karty:**

1. **Nazwa pola**
   * **Opis:** Pole, które ma być oceniane w porównaniu.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pierwszego pola w dokumencie.
2. **Operator porównania**
   * **Opis:** Określa, w jaki sposób wartość wybranego pola zostanie porównana z wartością referencyjną.
   * **Opcje:**
     * **Równa się (=):** Weryfikuje, czy wartość pola dokładnie odpowiada wartości referencyjnej.
     * **Nie równa się (≠):** Weryfikuje, czy wartość pola nie odpowiada wartości referencyjnej.
     * **Większy niż (>):** Sprawdza, czy wartość pola jest większa niż wartość referencyjna.
     * **Większe lub równe (≥):** Sprawdza, czy wartość pola jest większa lub równa wartości referencyjnej.
     * **Mniejszy niż (<):** Sprawdza, czy wartość pola jest mniejsza niż wartość referencyjna.
     * **Mniejszy lub równy (≤):** Sprawdza, czy wartość pola jest mniejsza lub równa wartości referencyjnej.
3. **Wartość referencyjna**
   * **Opis:** Wartość, z którą porównywane jest pole.
   * **Szczegóły:** Wartość ta może być liczbowa, tekstowa lub oparta na dacie, w zależności od kontekstu porównania.
4. **Kwota tolerancji**
   * **Opis:** Definiuje akceptowalny margines błędu dla porównania.
   * **Szczegóły:** Kwota tolerancji jest wartością liczbową wskazującą maksymalną dopuszczalną różnicę między dwiema wartościami pól, aby porównanie zostało uznane za prawdziwe.
5. **Typ tolerancji**
   * **Opis:** Określa jednostkę miary dla kwoty tolerancji.
   * **Opcje:**
     * **Wartość:** Tolerancja jest wartością bezwzględną, co oznacza, że dwa pola mogą różnić się o określoną kwotę tolerancji.
     * **Percent:** Tolerancja jest obliczana jako procent wartości drugiego pola, dopuszczając względny margines błędu.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia wartość pola względem wartości referencyjnej za pomocą wybranego operatora porównania. Jeśli skonfigurowana jest tolerancja, system uznaje porównanie za pomyślne, jeśli wartość pola mieści się w zdefiniowanym zakresie tolerancji.
* **Wykonanie akcji:**
  * **W zakresie tolerancji:** Jeśli wartość pola spełnia warunek w ramach określonej tolerancji, przepływ pracy jest kontynuowany, wyzwalając powiązane akcje.
  * **Poza tolerancją:** Jeśli wartość pola nie spełnia warunku lub znajduje się poza zakresem tolerancji, mogą zostać wykonane alternatywne akcje, takie jak rejestrowanie, wysyłanie alertów lub zatrzymanie przepływu pracy.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając pole do oceny z listy dostępnych pól i wybierając operator porównania (np. równe, większe niż) z listy rozwijanej. Następnie określają wartość referencyjną do porównania i definiują kwotę tolerancji, a potem wybierają typ tolerancji (np. procent lub wartość).

## **Podsumowanie:**

Karta "Field Comparison with Tolerances" jest wszechstronnym narzędziem dla przepływów pracy wymagających elastycznych ocen. Umożliwiając porównania z tolerancjami, zapewnia, że przepływy pracy pozostają wydajne i elastyczne, uwzględniając rzeczywiste różnice bez utraty dokładności.

<!-- workflow-card-complete-example-20261021 condition_docfield_operator_value_tolerances -->

### Przykład tolerancji wartości odniesienia

**Konfiguracja:** Wybierz numeryczne pole dokumentu `total_amount`, równość, wartość odniesienia `100`, tolerancję absolutną `5` i typ tolerancji Wartość.

**Oczekiwany wynik i kontrprzykład:** Przy wartości `103` warunek jest prawdziwy, ponieważ różnica mieści się w dopuszczalnej tolerancji. W przypadku wartości `110` warunek jest fałszywy, ponieważ różnica przekracza tę tolerancję. Ta karta porównuje jedno pole ze skonfigurowaną wartością referencyjną. Użyj osobnej karty dwupolowej, gdy obie strony muszą pochodzić z pól dokumentu. Brakujące lub nieliczbowe dane wymagają zbadania, a nie zakładanego dopasowania.

To jest ilustracyjna konfiguracja testu i oczekiwany wynik; nie zostało ono wykonane. Skorzystaj z danych i odbiorców skonfigurowanych w Twojej organizacji testowej.
