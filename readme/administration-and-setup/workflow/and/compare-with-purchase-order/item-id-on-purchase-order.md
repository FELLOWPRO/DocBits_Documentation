# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania identyfikatorów pozycji (item ID) między zamówieniem zakupu a powiązanym dokumentem, aby zapewnić uwzględnienie właściwych pozycji. Karta ocenia, czy identyfikator pozycji w zamówieniu zakupu odpowiada identyfikatorowi pozycji w dokumencie. Porównanie to może wyzwalać akcje w przypadku wykrycia rozbieżności, zapewniając, że pozycje w dokumencie są zgodne z zamówieniem zakupu.

## **Komponenty karty:**

1. **Any / All:**
   * **Opis**: Definiuje, czy warunek dotyczy dowolnych, czy wszystkich przypadków porównań identyfikatorów pozycji.
   * **Opcje**:
     * **Any**: Warunek jest spełniony, jeśli dowolny identyfikator pozycji w zamówieniu zakupu odpowiada identyfikatorowi pozycji w dokumencie.
     * **All**: Warunek jest spełniony tylko wtedy, gdy wszystkie identyfikatory pozycji w zamówieniu zakupu odpowiadają identyfikatorom pozycji w dokumencie.
2. **Operator:**
   * **Opis**: Definiuje warunek porównania identyfikatora pozycji w zamówieniu zakupu z identyfikatorem pozycji w dokumencie.
   * **Opcje**:
     * **Equals (=)**: Weryfikuje, czy identyfikator pozycji w zamówieniu zakupu dokładnie odpowiada identyfikatorowi pozycji w dokumencie.
     * **Not Equals (≠)**: Zapewnia, że identyfikator pozycji w zamówieniu zakupu nie odpowiada identyfikatorowi pozycji w dokumencie.

## **Funkcjonalność:**

* **Ocena warunku:** System porównuje identyfikator pozycji w zamówieniu zakupu z identyfikatorem pozycji w dokumencie na podstawie wybranego operatora. Jeśli warunek porównania jest prawdziwy (np. identyfikatory pozycji są zgodne lub niezgodne), przepływ pracy będzie kontynuowany odpowiednio.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli warunek jest prawdziwy (np. identyfikator pozycji w zamówieniu zakupu jest równy identyfikatorowi pozycji w dokumencie), przepływ pracy będzie kontynuowany z akcją prawdziwą (np. zatwierdzenie lub dalsze przetwarzanie).
  * **Warunek fałszywy**: Jeśli warunek jest fałszywy (np. identyfikator pozycji w zamówieniu zakupu nie odpowiada identyfikatorowi pozycji w dokumencie), przepływ pracy nie będzie kontynuowany.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając identyfikator pozycji zarówno w zamówieniu zakupu, jak i w dokumencie. Następnie wybierają odpowiedni operator (Equals lub Not Equals), aby zdefiniować sposób porównania identyfikatorów pozycji. Na koniec użytkownicy wybierają, czy warunek dotyczy dowolnych, czy wszystkich identyfikatorów pozycji w porównaniu.

## **Przykładowy scenariusz:**

* Faktura wymienia pozycję o ID "ABC123", a powiązane zamówienie zakupu również zawiera pozycję o ID "ABC123". Przy użyciu operatora "Equals" karta porównuje identyfikator pozycji w dokumencie z identyfikatorem pozycji w zamówieniu zakupu. Ponieważ identyfikatory pozycji są zgodne, przepływ pracy jest kontynuowany bez problemu.

## **Podsumowanie:**

Karta przepływu pracy "Item ID Comparison" zapewnia, że identyfikatory pozycji w dokumentach są zgodne z tymi w zamówieniach zakupu. Pomaga to zapobiegać rozbieżnościom w wykazach pozycji i zapewnia, że właściwe pozycje są przetwarzane zgodnie z zamówieniem zakupu. Możliwość porównywania na podstawie dowolnych lub wszystkich przypadków zapewnia elastyczność w różnych przypadkach użycia, poprawiając dokładność i efektywność przepływów pracy zakupowych.
