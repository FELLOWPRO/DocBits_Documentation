# Jeśli kraj w polu jest jednym z

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-364a45ddb67d-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel**

Ta karta przepływu pracy służy do oceny, czy określony kraj, znajdujący się w wyznaczonym polu, należy do predefiniowanej listy krajów. Na podstawie tej oceny przepływ pracy może być kontynuowany z warunkiem prawdziwym lub fałszywym. Pomaga zautomatyzować procesy, w których akcje zależą od tego, czy kraj znajduje się na liście dozwolonych lub ograniczonych krajów.

## **Komponenty karty:**

1. **Nazwa pola**
   * **Opis:** Określa pole dokumentu, w którym przechowywana jest nazwa lub kod kraju.
   * **Szczegóły:** Powinno to odpowiadać dokładnemu identyfikatorowi pola danych kraju w dokumencie.
2. **Operatora**
   * **Opis:** Definiuje, czy kraj w polu musi należeć do predefiniowanej listy krajów.
   * **Opcje:**
     * **Is:** Kraj musi być uwzględniony na liście określonych krajów, aby warunek był prawdziwy.
     * **Nie jest:** Kraj nie może być uwzględniony na liście określonych krajów, aby warunek był prawdziwy.
3. **Kraje**
   * **Opis:** Określa listę krajów, z którymi porównywany będzie wybrany kraj.
   * **Szczegóły:** Jest to lista krajów oddzielonych przecinkami. Porównanie sprawdza, czy kraj w polu jest uwzględniony na tej liście.
4. **Kontynuuj warunek**
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

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Kieruj faktury z dwóch określonych krajów.

**Konfiguracja:** Wybierz pole kraju, jest-jednym z, kody krajów `DE` i `FR` oraz kontynuację `true`.

**Oczekiwany wynik i kontrprzykład:** `DE` zalicza; `US` nie spełnia wymagań wybranej listy krajów.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
