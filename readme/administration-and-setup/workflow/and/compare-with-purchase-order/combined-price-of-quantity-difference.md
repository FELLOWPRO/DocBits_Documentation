# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**:

Ta karta przepływu pracy ocenia łączną cenę różnicy ilości, porównując ją z określoną wartością. Pomaga zautomatyzować akcje na podstawie rozbieżności cenowych i ilościowych w powiązanych dokumentach, usprawniając przepływy pracy zakupów i przyjęć. **Version 4** rozszerza tę funkcjonalność, umożliwiając porównania między różnymi encjami, takimi jak zamówienie zakupu, ilości otrzymane oraz sam dokument, dodając więcej elastyczności i kontroli do przepływu pracy.

## **Komponenty karty**:

1. **Operator**:&#x20;
   * **Opis:** Warunek porównania łącznej ceny z określoną wartością.
   * **Opcje:**
     * **Equals (=)**: Sprawdza, czy łączna cena odpowiada określonej wartości.
     * **Not Equals (≠)**: Zapewnia, że łączna cena różni się od określonej wartości.
     * **Greater Than (>)**: Weryfikuje, czy łączna cena jest większa niż określona wartość.
     * **Greater or Equals (≥)**: Sprawdza, czy łączna cena jest większa lub równa określonej wartości.
     * **Lesser Than (<)**: Weryfikuje, czy łączna cena jest mniejsza niż określona wartość.
     * **Lesser or Equals (≤)**: Sprawdza, czy łączna cena jest mniejsza lub równa określonej wartości.
2. **Value**:&#x20;
   * **Opis:** Określa wartość, z którą porównywana będzie łączna cena różnicy ilości.
   * **Szczegóły:** Wartość musi być wartością liczbową.

## **Dodatkowe komponenty w Version 4**:

* **Comparison Type**: Wybiera encje do porównania. Opcje obejmują:
  * **Purchase Order to Document**: Porównuje ilości i ceny między zamówieniem zakupu a powiązanym dokumentem.
  * **Received to Document**: Porównuje ilości otrzymane z ilościami w dokumencie.
  * **Purchase Order to Received**: Porównuje ilości w zamówieniu zakupu z ilościami otrzymanymi.

## **Funkcjonalność**:

* **Ocena warunku**: Oblicza łączną cenę, mnożąc różnicę ilości przez cenę jednostkową, i porównuje ją z określoną wartością za pomocą wybranego operatora.\
  **Version 4** dodaje opcję porównania dodatkowych encji na podstawie konfiguracji użytkownika, takich jak zamówienie zakupu do otrzymanych lub zamówienie zakupu do dokumentu.
* **Wykonanie akcji**: W zależności od tego, czy łączna cena spełnia określony warunek, przepływ pracy będzie kontynuowany z warunkami prawdziwymi lub fałszywymi w celu wyzwolenia akcji lub zatrzymania przepływu pracy. **Version 4** umożliwia również bardziej dynamiczne wykonywanie akcji, gdzie typ warunku (np. zamówienie zakupu do otrzymanych) wpływa na kolejny krok.

## **Konfiguracja**:

* **Version 3**: Użytkownicy konfigurują kartę, wybierając pola dokumentu dla różnicy ilości i ceny jednostkowej. Następnie wybierany jest operator definiujący, w jaki sposób łączna cena zostanie porównana z określoną wartością. Na koniec użytkownicy ustawiają warunek kontynuacji (true lub false), który dyktuje kolejny krok w przepływie pracy.
* **Version 4**: Oprócz konfiguracji w **Version 3** użytkownicy mają dodatkową opcję skonfigurowania **Comparison Type**. Definiuje to, jakie encje będą porównywane, takie jak **Purchase Order to Document**, **Received to Document** lub **Purchase Order to Received**.

## **Przykładowy scenariusz**:

* Faktura pokazuje 50 jednostek produktu po 100 USD każda, co daje łącznie 5000 USD. Powiązane zamówienie zakupu autoryzowało zakup na kwotę 4500 USD za 45 jednostek. Różnica ilości wynosi 5 jednostek, a łączna cena różnicy to 500 USD. Karta porównuje ilość w zamówieniu zakupu (45 jednostek) z ilością otrzymaną (50 jednostek) i sprawdza, czy łączna cena jest większa niż 400 USD (określona wartość). Przy użyciu operatora **Greater Than (>)** karta identyfikuje rozbieżność i oznacza ją do przeglądu przez zespół finansowy.

## **Podsumowanie**:

**Version 3** karty przepływu pracy "Combined Price of Quantity Difference" oferuje proste podejście do porównywania rozbieżności ilościowych i wyzwalania akcji na podstawie progów cenowych.\
**Version 4** rozszerza tę funkcjonalność, umożliwiając porównania między różnymi encjami (zamówienie zakupu, otrzymane, dokument), zapewniając większą elastyczność i kontrolę nad przepływem pracy. Organizacje mogą teraz automatyzować bardziej złożone scenariusze i egzekwować ściślejszą kontrolę nad procesami zakupów i przyjęć.
