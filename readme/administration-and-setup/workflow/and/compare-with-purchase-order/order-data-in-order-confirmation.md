# Dane zamówienia w potwierdzeniu zamówienia

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v1-pl-pl.png" alt="Dane zamówienia w potwierdzeniu zamówienia, Wersja 1" width="634"><figcaption><p>Wersja 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v2-pl-pl.png" alt="Dane zamówienia w potwierdzeniu zamówienia, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v3-pl-pl.png" alt="Dane zamówienia w potwierdzeniu zamówienia, Wersja 3" width="634"><figcaption><p>Wersja 3</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v4-pl-pl.png" alt="Dane zamówienia w potwierdzeniu zamówienia, Wersja 4" width="634"><figcaption><p>Wersja 4</p></figcaption></figure>

## **Cel**

Ta karta przepływu pracy służy do porównania określonych pól — **Cena jednostkowa**, **Rabat** lub **Ilość** — między potwierdzeniem zamówienia a zamówieniem zakupu. Zapewnia spójność i zgodność z uzgodnionymi warunkami. Na podstawie wyniku porównania karta umożliwia użytkownikom wpisanie określonego tekstu do wybranego pola, gdy warunek jest **true** lub **false**, usprawniając przetwarzanie dokumentów i redukując ręczną interwencję.

## **Komponenty karty**

1. **Dane zamówienia**
   * **Opis:** Określa pole do porównania między potwierdzeniem zamówienia a zamówieniem zakupu.
   * **Opcje:**
     * **Cena jednostkowa**: Porównuje cenę jednostkową w obu dokumentach.
     * **Rabat**: Porównuje procent lub wartość rabatu.
     * **Ilość**: Porównuje zamówioną ilość.
2. **Operatora**
   * **Opis:** Definiuje warunek stosowany podczas porównania.
   * **Opcje:**
     * **Równa się (=):** Sprawdza, czy wartość w wybranym polu jest zgodna między potwierdzeniem zamówienia a zamówieniem zakupu.
     * **Nie równa się (≠):** Zapewnia, że wartość w wybranym polu różni się między dwoma dokumentami.
3. **Tekst**
   * **Opis:** Określa tekst, który ma zostać wpisany do pola docelowego po ocenie warunku.
   * **Szczegóły:** Tekst ten może zawierać niestandardowe notatki, aktualizacje statusu lub predefiniowane wartości.
4. **Nazwa pola**
   * **Opis:** Określa pole, do którego zostanie wpisany tekst.
   * **Szczegóły:** Pole docelowe jest wybierane spośród dostępnych edytowalnych pól w systemie.
5. **Wynik warunku**
   * **Opis:** Określa, kiedy tekst powinien zostać wpisany, na podstawie wyniku porównania.
   * **Opcje:**
     * **True:** Wpisuje tekst, jeśli warunek porównania jest spełniony.
     * **False:** Wpisuje tekst, jeśli warunek porównania nie jest spełniony.

## **Funkcjonalność**

* **Ocena porównania:** System porównuje wybrane pole między potwierdzeniem zamówienia a zamówieniem zakupu za pomocą określonego operatora.
* **Wykonanie akcji:** Jeśli warunek jest **true** lub **false**, określony tekst jest wpisywany do wyznaczonego pola.

## **Konfiguracja**

* Aby skonfigurować tę kartę, użytkownicy najpierw wybierają pole do porównania — **Cena jednostkowa**, **Rabat** lub **Ilość**. Następnie wybierają operator definiujący warunek porównania, taki jak **equals** lub **nie jest równy**. Użytkownicy określają tekst, który ma zostać wpisany do pola docelowego, oraz wybierają, kiedy ta akcja ma nastąpić, na podstawie wyniku warunku (**true** lub **false**).

## **Przykładowy scenariusz**

* Potwierdzenie zamówienia wymienia cenę jednostkową 50 USD za produkt, podczas gdy zamówienie zakupu określa cenę 45 USD. Przy użyciu operatora **Nie równa się (≠)** karta identyfikuje rozbieżność i wpisuje tekst "Price Mismatch" do wyznaczonego pola, gdy warunek jest **true**.

## **Podsumowanie**

Karta przepływu pracy "\[Unit Price/Discount/Quantity] in Order Confirmation" zapewnia praktyczne rozwiązanie zapewniające spójność dokumentów. Automatycznie oznaczając rozbieżności i wpisując odpowiedni tekst do określonych pól, zwiększa efektywność i redukuje błędy w procesach zarządzania zamówieniami.
