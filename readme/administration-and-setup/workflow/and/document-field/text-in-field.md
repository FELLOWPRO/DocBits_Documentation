# Tekst w polu

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61d692604341-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatyzacji akcji na podstawie obecności lub braku określonego tekstu w określonym polu dokumentu. Zapewnia, że przepływy pracy mogą dynamicznie dostosowywać się do treści dokumentów, wspierając efektywne przetwarzanie i dokładne podejmowanie decyzji.

## **Komponenty karty:**

1. **Tekst**
   * **Opis:** Określa ciąg tekstowy do sprawdzenia w polu.
   * **Szczegóły:** Może to być słowo, fraza lub sekwencja znaków istotna dla przepływu pracy.
2. **Operatora**
   * **Opis:** Definiuje warunek obecności tekstu w polu.
   * **Opcje:**
     * **Is:** Wyzwala przepływ pracy, jeśli określony tekst jest obecny w polu.
     * **Nie jest:** Wyzwala przepływ pracy, jeśli określony tekst nie jest obecny w polu.
3. **Nazwa pola**
   * **Opis:** Określa nazwę pola dokumentu, które ma być oceniane.
   * **Szczegóły:** Musi to odpowiadać dokładnemu identyfikatorowi pola w dokumencie.

## **Funkcjonalność:**

1. **Ocena warunku:** System sprawdza, czy określony tekst istnieje w polu, na podstawie wybranego operatora (Is lub Is Not).
2. **Wykonanie akcji:**
   * **Warunek prawdziwy:**\
     Jeśli obecność tekstu w polu odpowiada określonemu warunkowi, system inicjuje powiązane akcje. Mogą one obejmować wyzwalanie alertów, kontynuowanie przepływów pracy lub aktualizację rekordów.
   * **Warunek fałszywy:**\
     Jeśli obecność tekstu w polu nie odpowiada warunkowi, mogą zostać podjęte alternatywne akcje lub żadne, w zależności od konfiguracji przepływu pracy.

## **Konfiguracja:**

* Użytkownik wprowadza tekst do sprawdzenia. Następnie wybiera nazwę pola odpowiedniego dokumentu.

## **Podsumowanie:**

Karta przepływu pracy "Text Presence in Field" jest prostym, ale potężnym narzędziem do analizy treści dokumentów. Automatyzując akcje na podstawie wykrywania tekstu, karta ta wspiera bardziej inteligentne przepływy pracy, poprawia dokładność obsługi dokumentów i redukuje ręczny wysiłek.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Znajdź dokumenty oznaczone znacznikiem recenzji.

**Konfiguracja:** Wybierz pole tekstowe `review_note`, zawierające operator i tekst `manual review`.

**Oczekiwany wynik i kontrprzykład:** `Please start manual review` zalicza. `Ready for export` nie zawiera wybranego tekstu i kończy się niepowodzeniem.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
