# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Ta karta przepływu pracy służy do porównania określonych pól — **Unit Price**, **Discount** lub **Quantity** — między potwierdzeniem zamówienia a zamówieniem zakupu. Zapewnia spójność i zgodność z uzgodnionymi warunkami. Na podstawie wyniku porównania karta umożliwia użytkownikom wpisanie określonego tekstu do wybranego pola, gdy warunek jest **true** lub **false**, usprawniając przetwarzanie dokumentów i redukując ręczną interwencję.

## **Komponenty karty**

1. **Order Data**
   * **Opis:** Określa pole do porównania między potwierdzeniem zamówienia a zamówieniem zakupu.
   * **Opcje:**
     * **Unit Price**: Porównuje cenę jednostkową w obu dokumentach.
     * **Discount**: Porównuje procent lub wartość rabatu.
     * **Quantity**: Porównuje zamówioną ilość.
2. **Operator**
   * **Opis:** Definiuje warunek stosowany podczas porównania.
   * **Opcje:**
     * **Equals (=):** Sprawdza, czy wartość w wybranym polu jest zgodna między potwierdzeniem zamówienia a zamówieniem zakupu.
     * **Not Equals (≠):** Zapewnia, że wartość w wybranym polu różni się między dwoma dokumentami.
3. **Text**
   * **Opis:** Określa tekst, który ma zostać wpisany do pola docelowego po ocenie warunku.
   * **Szczegóły:** Tekst ten może zawierać niestandardowe notatki, aktualizacje statusu lub predefiniowane wartości.
4. **Field Name**
   * **Opis:** Określa pole, do którego zostanie wpisany tekst.
   * **Szczegóły:** Pole docelowe jest wybierane spośród dostępnych edytowalnych pól w systemie.
5. **Condition Result**
   * **Opis:** Określa, kiedy tekst powinien zostać wpisany, na podstawie wyniku porównania.
   * **Opcje:**
     * **True:** Wpisuje tekst, jeśli warunek porównania jest spełniony.
     * **False:** Wpisuje tekst, jeśli warunek porównania nie jest spełniony.

## **Funkcjonalność**

* **Ocena porównania:** System porównuje wybrane pole między potwierdzeniem zamówienia a zamówieniem zakupu za pomocą określonego operatora.
* **Wykonanie akcji:** Jeśli warunek jest **true** lub **false**, określony tekst jest wpisywany do wyznaczonego pola.

## **Konfiguracja**

* Aby skonfigurować tę kartę, użytkownicy najpierw wybierają pole do porównania — **Unit Price**, **Discount** lub **Quantity**. Następnie wybierają operator definiujący warunek porównania, taki jak **equals** lub **not equals**. Użytkownicy określają tekst, który ma zostać wpisany do pola docelowego, oraz wybierają, kiedy ta akcja ma nastąpić, na podstawie wyniku warunku (**true** lub **false**).

## **Przykładowy scenariusz**

* Potwierdzenie zamówienia wymienia cenę jednostkową 50 USD za produkt, podczas gdy zamówienie zakupu określa cenę 45 USD. Przy użyciu operatora **Not Equals (≠)** karta identyfikuje rozbieżność i wpisuje tekst "Price Mismatch" do wyznaczonego pola, gdy warunek jest **true**.

## **Podsumowanie**

Karta przepływu pracy "\[Unit Price/Discount/Quantity] in Order Confirmation" zapewnia praktyczne rozwiązanie zapewniające spójność dokumentów. Automatycznie oznaczając rozbieżności i wpisując odpowiedni tekst do określonych pól, zwiększa efektywność i redukuje błędy w procesach zarządzania zamówieniami.
