# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do oceny, czy określony kraj, znajdujący się w wyznaczonym polu, należy do określonego obszaru handlowego lub politycznego (Unia Europejska, strefa Schengen lub NAFTA). Na podstawie tej oceny przepływ pracy może być kontynuowany z warunkiem prawdziwym lub fałszywym, umożliwiając dalsze akcje w systemie. Jest szczególnie przydatna do automatyzacji reguł biznesowych specyficznych dla regionu, zapewnienia zgodności lub wyzwalania określonych przepływów pracy na podstawie powiązań geograficznych.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa pole dokumentu, w którym przechowywana jest nazwa lub kod kraju.
   * **Szczegóły:** Powinno to odpowiadać dokładnemu identyfikatorowi pola danych kraju w dokumencie.&#x20;
2. **Operator**
   * **Opis:** Określa, czy kraj w wybranym polu powinien odpowiadać, czy nie odpowiadać wybranemu regionowi lub porozumieniu.
   * **Opcje:**
     * **Is:** Kraj musi należeć do wybranego porozumienia (EU, Schengen lub NAFTA), aby warunek był prawdziwy.
     * **Is Not:** Kraj nie może należeć do wybranego porozumienia, aby warunek był prawdziwy.
3. **Country Comparison**
   * **Opis:** Definiuje, czy kraj w polu jest sprawdzany względem określonego porozumienia politycznego lub handlowego.
   * **Opcje:**
     * **European Union:** Karta sprawdza, czy kraj jest członkiem Unii Europejskiej.
     * **Schengen Area:** Karta sprawdza, czy kraj należy do strefy Schengen.
     * **NAFTA:** Karta sprawdza, czy kraj jest członkiem porozumienia NAFTA.
4. **Boolean**
   * **Opis:** Definiuje wynik porównania. Jeśli kraj spełnia warunek, przepływ pracy jest kontynuowany z określoną wartością Boolean.
   * **Opcje:**
     * **True:** Przepływ pracy jest kontynuowany, jeśli warunek jest spełniony.
     * **False:** Przepływ pracy jest kontynuowany, jeśli warunek nie jest spełniony.

## **Funkcjonalność:**

* **Ocena warunku:**
  * System ocenia, czy kraj określony w polu należy do wybranego regionu lub porozumienia (EU, strefa Schengen lub NAFTA) na podstawie wybranego operatora. Ocena ta sprawdza nazwę lub kod kraju względem predefiniowanej listy krajów należących do każdej z grup.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:** Jeśli kraj w polu odpowiada wybranemu regionowi (zgodnie z operatorem), przepływ pracy jest kontynuowany z określonym warunkiem prawdziwym. Może to wyzwolić dalsze akcje, takie jak routing dokumentów, zastosowanie specjalnych reguł przetwarzania lub włączenie funkcji specyficznych dla regionu.
  * **Warunek fałszywy:** Jeśli kraj nie odpowiada wybranemu regionowi (zgodnie z operatorem), przepływ pracy jest kontynuowany z określonym warunkiem fałszywym, umożliwiając wykonanie alternatywnych akcji lub zakończenie przepływu pracy na podstawie konfiguracji systemu.

## **Konfiguracja:**&#x20;

* Użytkownicy konfigurują kartę, wybierając pole dokumentu zawierające kraj i określając region (Unia Europejska, strefa Schengen lub NAFTA). Następnie operator jest wybierany z listy rozwijanej, aby zdefiniować, czy kraj musi należeć do wybranego regionu, czy nie. Na koniec użytkownicy ustawiają warunek kontynuacji (true lub false), który dyktuje kolejny krok w przepływie pracy.

## **Podsumowanie:**

Karta przepływu pracy "Country in Field Comparison" jest niezbędnym narzędziem do automatyzacji procesów zależnych od reguł geograficznych, takich jak zgodność z porozumieniami handlowymi lub powiązaniami politycznymi. Porównując dane kraju z określonymi regionami, takimi jak Unia Europejska, strefa Schengen lub NAFTA, karta ta zapewnia, że system stosuje właściwą logikę przetwarzania, poprawiając efektywność i zapewniając dokładne wykonanie przepływu pracy na podstawie warunków geograficznych.
