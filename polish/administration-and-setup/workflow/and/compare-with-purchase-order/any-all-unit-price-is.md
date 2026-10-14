# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania ceny jednostkowej w dokumencie z ceną jednostkową w zamówieniu zakupu, zapewniając, że ceny mieszczą się w określonych poziomach tolerancji. Porównanie może wyzwalać akcje, jeśli cena jednostkowa nie spełnia oczekiwań. **Version 4** dodaje większą elastyczność, umożliwiając użytkownikom wybór różnych encji do porównania, zapewniając głębszy poziom kontroli nad procesami cenowymi i zakupowymi.

## **Komponenty karty:**

1. **Any / All:**
   * **Opis**: Definiuje, czy warunek dotyczy dowolnego, czy wszystkich przypadków porównywania ceny jednostkowej.
   * **Opcje**:
     * **Any**: Warunek jest spełniony, jeśli dowolna cena jednostkowa spełnia określony warunek porównania.
     * **All**: Warunek jest spełniony tylko wtedy, gdy wszystkie ceny jednostkowe spełniają określony warunek porównania.
2. **Operator:**
   * **Opis**: Definiuje warunek porównania ceny jednostkowej z określoną wartością.
   * **Opcje**:
     * **Equals (=)**: Weryfikuje, czy cena jednostkowa odpowiada określonej wartości.
     * **Not Equals (≠)**: Zapewnia, że cena jednostkowa różni się od określonej wartości.
     * **Greater Than (>)**: Weryfikuje, czy cena jednostkowa jest większa niż określona wartość.
     * **Greater or Equals (≥)**: Weryfikuje, czy cena jednostkowa jest większa lub równa określonej wartości.
     * **Lesser Than (<)**: Weryfikuje, czy cena jednostkowa jest mniejsza niż określona wartość.
     * **Lesser or Equals (≤)**: Weryfikuje, czy cena jednostkowa jest mniejsza lub równa określonej wartości.

## **Dodatkowe komponenty w Version 4:**

**Comparison Type:**

* **Opis**: Umożliwia użytkownikom wybór, jakie encje będą porównywane oprócz ceny jednostkowej.
* **Opcje**:
  * **Purchase Order to Document**: Porównuje cenę jednostkową w zamówieniu zakupu z ceną jednostkową w dokumencie.
  * **Received to Document**: Porównuje ilość otrzymaną z ceną jednostkową w dokumencie.
  * **Purchase Order to Received**: Porównuje cenę jednostkową w zamówieniu zakupu z ilością otrzymaną.

## **Funkcjonalność:**

* **Ocena warunku:** System porównuje cenę jednostkową w dokumencie z ceną jednostkową w zamówieniu zakupu (lub inną wybraną encją, w Version 4) na podstawie wybranego operatora. Jeśli porównanie jest prawdziwe, przepływ pracy jest kontynuowany zgodnie z kolejnymi krokami, wyzwalając zatwierdzenie lub zatrzymując proces.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli warunek jest prawdziwy (np. cena jednostkowa w dokumencie jest większa niż określona wartość), przepływ pracy będzie kontynuowany z akcją prawdziwą (np. zatwierdzenie, przetwarzanie dokumentu).
  * **Warunek fałszywy**: Jeśli warunek jest fałszywy (np. cena jednostkowa w dokumencie nie spełnia porównania), przepływ pracy nie będzie kontynuowany.

## **Konfiguracja:**

* **Konfiguracja Version 3:** Użytkownicy konfigurują kartę, wybierając cenę jednostkową w dokumencie, wybierając odpowiedni operator definiujący sposób porównania ceny jednostkowej z określoną wartością oraz ustawiając wartość do porównania. Dodatkowo użytkownicy wybierają, czy warunek dotyczy dowolnych, czy wszystkich przypadków porównania ceny jednostkowej.
* **Konfiguracja Version 4:** W Version 4 użytkownicy mają dodatkową opcję wyboru Comparison Type. Umożliwia to zdefiniowanie encji do porównania, takich jak Purchase Order to Document, Received to Document lub Purchase Order to Received. Zwiększa to elastyczność karty w porównywaniu cen jednostkowych w bardziej złożonych scenariuszach.

## **Przykładowy scenariusz:**

*   **Przykład Version 3:**&#x20;

    Faktura pokazuje cenę jednostkową 50 USD. Powiązane zamówienie zakupu ma cenę jednostkową 45 USD. Karta porównuje obie ceny jednostkowe za pomocą operatora "Greater Than". Ponieważ cena jednostkowa w dokumencie (50 USD) jest większa niż cena jednostkowa w zamówieniu zakupu (45 USD), przepływ pracy wyzwoli warunek prawdziwy (np. wyślij dokument do przeglądu).
* **Przykład Version 4:**\
  Faktura pokazuje cenę jednostkową 50 USD, a powiązane zamówienie zakupu autoryzowało cenę jednostkową 45 USD. Dodatkowo ilość otrzymana wynosi 60 jednostek. Karta porównuje ilość otrzymaną z ceną jednostkową w dokumencie za pomocą operatora "Greater Than". Ponieważ ilość otrzymana (60) jest większa niż cena jednostkowa (50 USD), przepływ pracy wyzwala warunek prawdziwy, a dokument zostaje oznaczony do dalszego przeglądu.

## **Podsumowanie:**

Version 3 karty przepływu pracy "Unit Price Comparison" służy do zapewnienia, że ceny jednostkowe w dokumentach są zgodne z cenami w zamówieniach zakupu, wyzwalając akcje na podstawie zdefiniowanych warunków. Version 4 rozszerza tę funkcjonalność, wprowadzając bardziej złożone opcje porównania, takie jak porównywanie zamówień zakupu z dokumentami, ilości otrzymanych z dokumentami oraz zamówień zakupu z ilościami otrzymanymi. Ta dodatkowa elastyczność umożliwia organizacjom obsługę bardziej zaawansowanych scenariuszy cenowych i zakupowych, poprawiając kontrolę i dokładność w przepływach pracy.
