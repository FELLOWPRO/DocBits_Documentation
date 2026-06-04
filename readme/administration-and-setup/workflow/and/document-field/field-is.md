# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji na podstawie obecności lub stanu określonego pola w dokumencie. Oceniając, czy pole jest puste, brakujące, czy wypełnione, umożliwia przepływom pracy precyzyjną i dokładną obsługę dokumentów.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa nazwę pola, które ma być oceniane.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi używanemu w dokumencie, aby zapewnić dokładne wykrywanie pola.
2. **Operators**
   * **Opis**: Definiuje warunek wyzwalający przepływ pracy, na podstawie obecności lub stanu pola.
   * **Opcje**:
     * **Empty/Not in Document:** Przepływ pracy jest wyzwalany, jeśli pole jest albo nieobecne w dokumencie, albo obecne, ale puste.
     * **In Document/Not Empty:** Przepływ pracy jest wyzwalany, jeśli pole istnieje w dokumencie i zawiera wartość.

## **Funkcjonalność:**

* **Wykrywanie stanu:** Karta monitoruje określone pole, aby ocenić jego obecność i stan.
* **Ocena warunku:**
  * System ocenia, czy określone pole jest w stanie (Empty/Not in Document lub In Document/Not Empty) zdefiniowanym przez wybrany operator.
*

    **Wykonanie akcji:**

    * **Warunek Empty/Not in Document:** Jeśli stan pola odpowiada temu warunkowi (tj. pole jest albo nieobecne w dokumencie, albo obecne, ale puste), system inicjuje powiązane akcje. Mogą one obejmować generowanie alertów, oznaczanie dokumentu do przeglądu lub zatrzymanie przepływu pracy.
    * **Warunek In Document/Not Empty:** Jeśli stan pola odpowiada temu warunkowi (tj. pole istnieje w dokumencie i zawiera wartość), system wyzwala powiązane akcje. Mogą one obejmować włączanie kolejnych kroków przepływu pracy, aktualizację rekordów lub wyzwalanie powiadomień.

## **Konfiguracja:**&#x20;

* Użytkownicy wybierają pole z listy dostępnych pól dokumentu. Operator jest wybierany za pomocą menu rozwijanego, oferującego jasne opcje "Empty/Not in Document" lub "In Document/Not Empty".

## **Podsumowanie:**

Karta przepływu pracy "Field Presence and State Validation" jest kluczowym narzędziem dla przepływów pracy przetwarzania dokumentów, zapewniając dokładną obsługę brakujących lub wypełnionych pól. Automatyzując akcje na podstawie stanów pól, karta ta zwiększa integralność danych, redukuje błędy i zapewnia płynne i wydajne działanie przepływów pracy.
