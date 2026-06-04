# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji na podstawie obecności lub braku określonego tekstu w określonym polu dokumentu. Zapewnia, że przepływy pracy mogą dynamicznie dostosowywać się do treści dokumentów, wspierając efektywne przetwarzanie i dokładne podejmowanie decyzji.

## **Komponenty karty:**

1. **Text**
   * **Opis:** Określa ciąg tekstowy do sprawdzenia w polu.
   * **Szczegóły:** Może to być słowo, fraza lub sekwencja znaków istotna dla przepływu pracy.
2. **Operator**
   * **Opis:** Definiuje warunek obecności tekstu w polu.
   * **Opcje:**
     * **Is:** Wyzwala przepływ pracy, jeśli określony tekst jest obecny w polu.
     * **Is Not:** Wyzwala przepływ pracy, jeśli określony tekst nie jest obecny w polu.
3. **Field Name**
   * **Opis:** Określa nazwę pola dokumentu, które ma być oceniane.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pola w dokumencie.

## **Funkcjonalność:**

1. **Ocena warunku:** System sprawdza, czy określony tekst istnieje w polu, na podstawie wybranego operatora (Is lub Is Not).
2. **Wykonanie akcji:**
   * **Warunek prawdziwy:**\
     Jeśli obecność tekstu w polu odpowiada określonemu warunkowi, system inicjuje powiązane akcje. Mogą one obejmować wyzwalanie alertów, kontynuowanie przepływów pracy lub aktualizację rekordów.
   * **Warunek fałszywy:**\
     Jeśli obecność tekstu w polu nie odpowiada warunkowi, mogą zostać podjęte alternatywne akcje lub żadne, w zależności od konfiguracji przepływu pracy.

## **Konfiguracja:**&#x20;

* Użytkownik wprowadza tekst do sprawdzenia. Następnie wybiera nazwę pola odpowiedniego dokumentu.

## **Podsumowanie:**

Karta przepływu pracy "Text Presence in Field" jest prostym, ale potężnym narzędziem do analizy treści dokumentów. Automatyzując akcje na podstawie wykrywania tekstu, karta ta wspiera bardziej inteligentne przepływy pracy, poprawia dokładność obsługi dokumentów i redukuje ręczny wysiłek.
