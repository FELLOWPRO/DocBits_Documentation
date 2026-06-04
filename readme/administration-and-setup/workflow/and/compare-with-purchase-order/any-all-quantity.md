# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania ilości w dokumencie z tolerancją zdefiniowaną w zamówieniu zakupu. Umożliwia użytkownikom ocenę, czy ilość spełnia określone warunki, takie jak równość lub przekroczenie określonej tolerancji. W Version 4 karta rozszerza funkcjonalność, dodając możliwość porównywania wielu encji, w tym zamówienia zakupu, ilości otrzymanych i ilości w dokumencie, oferując większą elastyczność w obsłudze różnych scenariuszy.

## **Komponenty karty:**

1. **Any / All:**
   * **Opis**: Określa, w jaki sposób porównanie powinno być stosowane do wielu pozycji lub warunków.
   * **Opcje**:
     * **Any**: Przynajmniej jeden z warunków musi być spełniony, aby akcja została wyzwolona.
     * **All**: Wszystkie warunki muszą być spełnione, aby akcja mogła być kontynuowana.
2. **Operator:**
   * **Opis**: Definiuje warunek, który zostanie zastosowany do porównania ilości w dokumencie z określoną tolerancją.
   * **Opcje**:
     * **Equals (=)**: Sprawdza, czy ilość odpowiada określonej wartości tolerancji.
     * **Not Equals (≠)**: Zapewnia, że ilość różni się od określonej wartości tolerancji.
     * **Greater Than (>)**: Weryfikuje, czy ilość jest większa niż określona tolerancja.
     * **Greater or Equals (≥)**: Sprawdza, czy ilość jest większa lub równa określonej tolerancji.
     * **Lesser Than (<)**: Weryfikuje, czy ilość jest mniejsza niż określona tolerancja.
     * **Lesser or Equals (≤)**: Sprawdza, czy ilość jest mniejsza lub równa określonej tolerancji.
3. **Tolerance Amount:**
   * **Opis**: Określa wartość tolerancji, z którą porównywana będzie ilość w dokumencie.
   * **Szczegóły**: Wartość ta jest liczbowa i reprezentuje próg dozwolonej zmienności ilości.
4. **Tolerance Type:**
   * **Opis**: Definiuje typ tolerancji, który zostanie zastosowany.
   * **Opcje**:
     * **Percentage**: Tolerancja jest obliczana jako procent ilości w zamówieniu zakupu.
     * **Value**: Tolerancja jest określana jako stała wartość liczbowa.

## **Dodatkowe komponenty w Version 4:**

* **Comparison Type**: Wybiera encje do porównania, zapewniając większą elastyczność w sposobie oceny ilości w Version 4.
  * **Purchase Order to Document**: Porównuje ilość w zamówieniu zakupu z ilością w powiązanym dokumencie.
  * **Received to Document**: Porównuje ilość otrzymaną z ilością w dokumencie.
  * **Purchase Order to Received**: Porównuje ilość w zamówieniu zakupu z ilością otrzymaną.

## **Funkcjonalność:**

* **Ocena warunku:** System porównuje ilość w dokumencie z tolerancją w zamówieniu zakupu na podstawie wybranego operatora oraz kwoty/typu tolerancji. W Version 4 **Comparison Type** umożliwia porównywanie różnych ilości, takich jak zamówienie zakupu do otrzymanych lub zamówienie zakupu do dokumentu, zapewniając bardziej dynamiczne porównanie.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli porównanie daje wynik prawdziwy (np. ilość w dokumencie mieści się w akceptowalnym zakresie tolerancji), przepływ pracy będzie kontynuowany.
  * **Warunek fałszywy**: Jeśli porównanie daje wynik fałszywy (np. ilość nie spełnia tolerancji), przepływ pracy nie będzie kontynuowany.

## **Konfiguracja:**

**Version 3:**

* Użytkownicy konfigurują kartę, wybierając ilość w dokumencie, definiując kwotę tolerancji i typ tolerancji oraz wybierając odpowiedni operator do porównania ilości z tolerancją. Karta ocenia, czy ilość mieści się w progu tolerancji, i kontynuuje akcją "True" lub "False" w zależności od wyniku.

**Version 4:**

* Oprócz konfiguracji z Version 3 użytkownicy mogą wybrać **Comparison Type**, umożliwiając porównania między różnymi encjami, takimi jak:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Przykładowy scenariusz:**

Faktura pokazuje, że dostarczono 100 jednostek, ale zamówienie zakupu autoryzowało tylko 90 jednostek. Kwota tolerancji jest ustawiona na 10 jednostek, a typ tolerancji jest bezwzględny.

* **Version 3**: Karta porównuje 100 jednostek w dokumencie z tolerancją zamówienia zakupu wynoszącą 90 jednostek. Jeśli ilość przekracza tolerancję, karta oznacza rozbieżność do dalszego przeglądu.
* **Version 4**: Karta może porównać **ilość w zamówieniu zakupu** (90 jednostek) z **ilością otrzymaną** (100 jednostek) lub **ilością w dokumencie** (100 jednostek). W zależności od wybranego **Comparison Type** sprawdza, czy różnica między dwiema encjami przekracza tolerancję, i wyzwala odpowiednią akcję.

## **Podsumowanie:**

* **Version 3**: Ta karta przepływu pracy porównuje ilość w dokumencie z tolerancją zamówienia zakupu, pomagając zapewnić, że rozbieżności w ilości są oznaczane i odpowiednio obsługiwane.
* **Version 4**: Rozszerza tę funkcjonalność, umożliwiając użytkownikom porównywanie różnych encji, takich jak zamówienie zakupu do otrzymanych lub zamówienie zakupu do dokumentu, zapewniając większą elastyczność w obsłudze bardziej złożonych scenariuszy. Version 4 zapewnia ściślejszą kontrolę nad przepływami pracy zakupów i przyjęć, oferując bardziej dynamiczne porównania i akcje oparte na wybranym typie porównania.
