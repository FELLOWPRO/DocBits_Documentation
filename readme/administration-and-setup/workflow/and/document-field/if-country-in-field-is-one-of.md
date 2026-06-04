# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Ta karta przepływu pracy służy do oceny, czy określony kraj, znajdujący się w wyznaczonym polu, należy do predefiniowanej listy krajów. Na podstawie tej oceny przepływ pracy może być kontynuowany z warunkiem prawdziwym lub fałszywym. Pomaga zautomatyzować procesy, w których akcje zależą od tego, czy kraj znajduje się na liście dozwolonych lub ograniczonych krajów.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa pole dokumentu, w którym przechowywana jest nazwa lub kod kraju.
   * **Szczegóły:** Powinno to odpowiadać dokładnemu identyfikatorowi pola danych kraju w dokumencie.&#x20;
2. **Operator**
   * **Opis:** Definiuje, czy kraj w polu musi należeć do predefiniowanej listy krajów.
   * **Opcje:**
     * **Is:** Kraj musi być uwzględniony na liście określonych krajów, aby warunek był prawdziwy.
     * **Is Not:** Kraj nie może być uwzględniony na liście określonych krajów, aby warunek był prawdziwy.
3. **Countries**
   * **Opis:** Określa listę krajów, z którymi porównywany będzie wybrany kraj.
   * **Szczegóły:** Jest to lista krajów oddzielonych przecinkami. Porównanie sprawdza, czy kraj w polu jest uwzględniony na tej liście.
4. **Continue Condition**
   * **Opis:** Definiuje wynik porównania. Jeśli kraj spełnia warunek, przepływ pracy jest kontynuowany z określoną wartością Boolean.
   * **Opcje:**
     * **True:** Przepływ pracy jest kontynuowany, jeśli warunek jest spełniony.
     * **False:** Przepływ pracy jest kontynuowany, jeśli warunek nie jest spełniony.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia, czy kraj określony w polu należy do listy predefiniowanych krajów. Ocena ta sprawdza nazwę lub kod kraju względem podanej listy.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:**\
    Jeśli kraj w polu należy do określonej listy krajów, przepływ pracy jest kontynuowany z warunkiem prawdziwym. Może to wyzwolić dalsze akcje, takie jak przekierowanie dokumentów do odpowiedniego działu, zastosowanie określonych reguł przetwarzania lub włączenie funkcji specyficznych dla regionu.
  * **Warunek fałszywy:**\
    Jeśli kraj nie odpowiada liście, przepływ pracy jest kontynuowany z warunkiem fałszywym. Umożliwia to wykonanie alternatywnych akcji lub zatrzymanie przepływu pracy na podstawie konfiguracji systemu.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając pole dokumentu zawierające kraj i określając listę krajów do sprawdzenia. Następnie operator jest wybierany z listy rozwijanej, aby zdefiniować, czy kraj musi być częścią określonej listy krajów, czy nie. Na koniec użytkownicy ustawiają warunek kontynuacji (true lub false), który dyktuje kolejny krok w przepływie pracy.

## **Podsumowanie:**

Karta przepływu pracy "Country in Field Comparison with List" jest cennym narzędziem do automatyzacji akcji na podstawie tego, czy kraj należy do predefiniowanej grupy. Porównując dane kraju z listą dozwolonych lub ograniczonych krajów, karta ta zwiększa efektywność przepływu pracy i zapewnia, że procesy systemowe przestrzegają właściwych reguł geograficznych.
