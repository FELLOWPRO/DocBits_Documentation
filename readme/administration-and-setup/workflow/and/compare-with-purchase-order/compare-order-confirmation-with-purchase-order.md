# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Cel:

Ta karta DocBits służy do porównania określonego pola danych zamówienia — takiego jak ilość, rabat lub cena jednostkowa — między potwierdzeniem zamówienia a zamówieniem zakupu. Umożliwiając ukierunkowane porównanie jednego pola naraz, zapewnia precyzję walidacji kluczowych punktów danych, utrzymując dokładność zamówienia. **Version 4** rozszerza tę funkcjonalność, umożliwiając porównania między różnymi encjami, takimi jak zamówienie zakupu, ilości otrzymane oraz sam dokument, dodając więcej elastyczności i kontroli do przepływu pracy.

## Komponenty karty:

1. **Any/All**&#x20;
   * **Opis:** Określa, czy warunek dotyczy dowolnych, czy wszystkich wierszy w potwierdzeniu zamówienia.\
     **Opcje:**
     * **Any**: Porównanie zostanie wyzwolone, jeśli wartość wybranego pola w dowolnym wierszu potwierdzenia zamówienia odpowiada odpowiadającej jej wartości w zamówieniu zakupu.
     * **All**: Porównanie zostanie wyzwolone tylko wtedy, gdy wartość wybranego pola we wszystkich wierszach potwierdzenia zamówienia odpowiada odpowiadającej jej wartości w zamówieniu zakupu.
2. **Order Data Field**
   * **Opis**: Określa pole danych do porównania między potwierdzeniem zamówienia a zamówieniem zakupu.
   * **Szczegóły**: Użytkownicy mogą wybrać jedno z następujących pól do porównania:
     * **Quantity**: Porównuje zamówioną ilość z potwierdzoną ilością.
     * **Discount**: Weryfikuje, czy rabat w potwierdzeniu odpowiada zamówieniu zakupu.
     * **Unit Price**: Zapewnia, że cena jednostkowa w potwierdzeniu jest zgodna z zamówieniem zakupu.
3. **Operator**
   * **Opis**: Definiuje warunek stosowany do porównania wybranego pola danych.
   * **Opcje**:
     * **Equals (=)**: Potwierdza, że wartość odpowiada zamówieniu zakupu.
     * **Not Equals (≠)**: Zapewnia, że wartość różni się od zamówienia zakupu.
     * **Greater Than (>)**: Weryfikuje, czy wartość przekracza wartość zamówienia zakupu.
     * **Greater or Equals (≥)**: Potwierdza, że wartość jest równa lub przekracza wartość zamówienia zakupu.
     * **Less Than (<)**: Sprawdza, czy wartość jest niższa niż wartość zamówienia zakupu.
     * **Less or Equals (≤)**: Potwierdza, że wartość jest niższa lub równa wartości zamówienia zakupu.

## **Dodatkowe komponenty w Version 4**:

* **Comparison Type**: Wybiera encje do porównania. Opcje obejmują:
  * **Purchase Order to Document**: Porównuje dane zamówienia zakupu z powiązanym dokumentem.
  * **Received to Document**: Porównuje dane otrzymane (np. ilości otrzymane) z dokumentem.
  * **Purchase Order to Received**: Porównuje dane zamówienia zakupu z ilościami otrzymanymi.

## Funkcjonalność:

* **Porównanie pola**: System porównuje wybrane pole danych zamówienia (Unit Price, Discount lub Quantity) z potwierdzenia zamówienia z odpowiadającą wartością w zamówieniu zakupu.
* **Wykonanie akcji**: Na podstawie wyniku porównania i warunku operatora karta może wyzwalać kolejne akcje, takie jak powiadomienia lub alerty.

## Przykładowy scenariusz:

* Potwierdzenie zamówienia określa **cenę jednostkową** 50 USD, podczas gdy zamówienie zakupu podaje 45 USD. Przy użyciu operatora "Greater Than" karta oznacza rozbieżność, umożliwiając zespołowi zakupów rozwiązanie jej przed przetwarzaniem.

## Podsumowanie:

Ta karta upraszcza walidację poszczególnych pól danych zamówienia, zapewniając zgodność z warunkami zamówienia zakupu. Izolując jedno pole naraz do porównania, wspiera ukierunkowane przeglądy i zapobieganie błędom w przetwarzaniu zamówień.
