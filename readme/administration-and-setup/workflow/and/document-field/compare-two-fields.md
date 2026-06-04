# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji poprzez porównanie wartości dwóch określonych pól dokumentu. Umożliwia dynamiczne podejmowanie decyzji na podstawie danych pól i zapewnia, że przepływy pracy są wykonywane na podstawie porównań między różnymi wartościami dokumentu.

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
   * **Szczegóły:** Powinno to odpowiadać dokładnemu identyfikatorowi drugiego pola w dokumencie.

## **Funkcjonalność:**

**Ocena warunku:** System ocenia, czy wartości w dwóch określonych polach spełniają warunek porównania zdefiniowany przez operator.

**Wykonanie akcji:**

* **Warunek prawdziwy:**\
  Jeśli wartości dwóch pól odpowiadają warunkowi porównania, system wyzwala powiązane akcje. Akcje te mogą obejmować aktualizację rekordów lub wyzwalanie alertów.
* **Warunek fałszywy:**\
  Jeśli wartości dwóch pól nie odpowiadają określonemu warunkowi, mogą zostać wykonane alternatywne akcje lub żadne, w zależności od konfiguracji przepływów pracy.

## **Konfiguracja:**&#x20;

* Użytkownicy konfigurują kartę, wybierając dwa pola do porównania z listy dostępnych pól w systemie. Operator jest wybierany z listy rozwijanej dostępnych opcji porównania.

## **Podsumowanie:**

Karta przepływu pracy "Compare Two Fields" jest niezbędnym narzędziem do porównywania danych między polami w dokumentach. Automatyzując akcje na podstawie porównań pól, karta ta pomaga zoptymalizować podejmowanie decyzji, wspiera walidację danych i zwiększa automatyzację przepływu pracy.
