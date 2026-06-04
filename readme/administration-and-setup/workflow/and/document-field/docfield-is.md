# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji poprzez porównanie wartości określonego pola dokumentu z wartością referencyjną lub warunkiem. Zapewnia dynamiczne i dokładne podejmowanie decyzji w przepływach pracy na podstawie walidacji danych dokumentu.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa nazwę pola dokumentu, które ma być oceniane.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pola w dokumencie.
2. **Operators**
   * **Opis:** Definiuje typ porównania, który ma być wykonany między wartością pola a wartością referencyjną.
   * **Opcje:**
     * **Equals (=):** Sprawdza, czy wartość pola odpowiada wartości referencyjnej.
     * **Not Equals (≠):** Zapewnia, że wartość pola różni się od wartości referencyjnej.
     * **Greater Than (>):** Potwierdza, że wartość pola jest większa niż wartość referencyjna.
     * **Greater or Equals (≥):** Weryfikuje, że wartość pola jest równa lub większa niż wartość referencyjna.
     * **Lesser Than (<):** Sprawdza, czy wartość pola jest mniejsza niż wartość referencyjna.
     * **Less or Equals (≤):** Zapewnia, że wartość pola jest mniejsza lub równa wartości referencyjnej.

## **Funkcjonalność:**

* **Ocena warunku:** System sprawdza, czy wartość pola dokumentu, w odniesieniu do powiązanej z nim kolumny, spełnia warunek porównania określony przez operator i wartość referencyjną.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:**\
    Jeśli wartość pola dokumentu spełnia określony warunek (np. równa się wartości referencyjnej), system wyzwala powiązane akcje. Mogą one obejmować aktualizację rekordów, kontynuowanie przepływu pracy lub generowanie powiadomień.
  * **Warunek fałszywy:**\
    Jeśli wartość pola dokumentu nie spełnia określonego warunku, wykonywane są alternatywne akcje lub żadne, na podstawie konfiguracji przepływu pracy.

## **Konfiguracja:**

* Użytkownik wybiera nazwę pola odpowiedniego dokumentu i wybiera operator z menu rozwijanego. Następnie użytkownik określa wartość pola referencyjnego, aby zakończyć konfigurację.

## **Podsumowanie:**

Karta przepływu pracy "DocField Comparison Validation" jest niezawodnym narzędziem do dynamicznego przetwarzania dokumentów. Automatyzując akcje na podstawie porównań pól, karta ta usprawnia przepływy pracy, zwiększa dokładność i wspiera podejmowanie decyzji opartych na danych.
