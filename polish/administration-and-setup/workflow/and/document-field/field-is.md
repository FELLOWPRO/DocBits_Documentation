# Sprawdzanie obecności i zawartości pola dokumentu

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-db30554e1eb1-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji na podstawie obecności lub stanu określonego pola w dokumencie. Oceniając, czy pole jest puste, brakujące, czy wypełnione, umożliwia przepływom pracy precyzyjną i dokładną obsługę dokumentów.

## **Komponenty karty:**

1. **Nazwa pola**
   * **Opis:** Określa nazwę pola, które ma być oceniane.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi używanemu w dokumencie, aby zapewnić dokładne wykrywanie pola.
2. **Operatorzy**
   * **Opis**: Definiuje warunek wyzwalający przepływ pracy, na podstawie obecności lub stanu pola.
   * **Opcje**:
     * **Pusty/brak w dokumencie:** Przepływ pracy jest wyzwalany, jeśli pole jest albo nieobecne w dokumencie, albo obecne, ale puste.
     * **W dokumencie/nie pusty:** Przepływ pracy jest wyzwalany, jeśli pole istnieje w dokumencie i zawiera wartość.

## **Funkcjonalność:**

* **Wykrywanie stanu:** Karta monitoruje określone pole, aby ocenić jego obecność i stan.
* **Ocena warunku:**
  * System ocenia, czy określone pole jest w stanie (Empty/Not in Document lub In Document/Not Empty) zdefiniowanym przez wybrany operator.
*

**Wykonanie akcji:**
* **Warunek Pusty/Nie w dokumencie:** Jeśli stan pola odpowiada temu warunkowi (tj. pole jest albo nieobecne w dokumencie, albo obecne, ale puste), system inicjuje powiązane akcje. Mogą one obejmować generowanie alertów, oznaczanie dokumentu do przeglądu lub zatrzymanie przepływu pracy.
* **Warunek W dokumencie/Nie pusty:** Jeśli stan pola odpowiada temu warunkowi (tj. pole istnieje w dokumencie i zawiera wartość), system wyzwala powiązane akcje. Mogą one obejmować włączanie kolejnych kroków przepływu pracy, aktualizację rekordów lub wyzwalanie powiadomień.
## **Konfiguracja:**

* Użytkownicy wybierają pole z listy dostępnych pól dokumentu. Operator jest wybierany za pomocą menu rozwijanego, oferującego jasne opcje "Empty/Not in Document" lub "In Document/Not Empty".

## **Podsumowanie:**

Karta przepływu pracy "Field Presence and State Validation" jest kluczowym narzędziem dla przepływów pracy przetwarzania dokumentów, zapewniając dokładną obsługę brakujących lub wypełnionych pól. Automatyzując akcje na podstawie stanów pól, karta ta zwiększa integralność danych, redukuje błędy i zapewnia płynne i wydajne działanie przepływów pracy.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Wykryj faktury, których numer faktury nadal wymaga sprawdzenia.

**Konfiguracja:** Wybierz pole `invoice_number` i Puste/Nie ma w dokumencie.

**Oczekiwany wynik i kontrprzykład:** Puste lub brakujące pole zostaje uznane. Wypełniona wartość, taka jak `DEMO-001`, nie spełnia tego warunku.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
