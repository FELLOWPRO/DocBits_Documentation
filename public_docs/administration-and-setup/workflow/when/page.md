# Operacja typu dokumentu

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-pl-pl.png" alt="Operacja typu dokumentu, Wersja 1" width="634"><figcaption><p>Wersja 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-pl-pl.png" alt="Operacja typu dokumentu, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pl.mp4" %}

**Film:** Karta: Typ dokumentu jest / nie jest · 0:34 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Typ dokumentu jest / nie jest** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pl.mp4#t=0.25)

Karta Typ dokumentu sprawdza typ dokumentu. Wybierz Jest albo Nie jest, a potem typ, na przykład Faktura. Nie jest pasuje do każdego typu poza wybranym.

**Przykład: tylko faktury** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pl.mp4#t=17.183)

Na przykład Workflow tylko dla faktur: Typ dokumentu jest Faktura jako karta Kiedy, potem karta przypisania. Dla korekt, ofert lub zamówień ten Workflow się nie uruchamia.

</details>

## **Cel:**

Ta karta przepływu pracy jest specjalnie zaprojektowana do wykonywania predefiniowanych operacji na dokumentach kategoryzowanych według typu. Usprawnia obsługę różnych form dokumentów w systemie ERP, zapewniając, że każdy typ jest przetwarzany zgodnie ze swoimi unikalnymi wymaganiami i politykami organizacyjnymi.

## **Funkcjonalność:**

* **Walidacja typu dokumentu**: Karta sprawdza, czy dokument odpowiada określonemu typowi, co pozwala użytkownikom potwierdzić jego kategoryzację.
* **Operatora**: Użytkownicy mogą ustawić warunki określające typ dokumentu. Dostępne operatory:
  * **Is**: Potwierdza, że dokument odpowiada wskazanemu typowi dokumentu.
  * **Nie jest**: Zapewnia, że dokument nie odpowiada wskazanemu typowi dokumentu.
* **Typy dokumentów**: Obsługiwane typy dokumentów:
  * **Faktura**
  * **Nota debetowa**
  * **Nota kredytowa**
  * **Zamówienie**
  * **Potwierdzenie zamówienia**
  * **Powiadomienie o wysyłce z wyprzedzeniem**

## **Zastosowanie**:

Ta karta jest przydatna dla menedżerów dokumentów i administratorów, którzy muszą zadbać o prawidłową klasyfikację dokumentów w celu usprawnienia ich przetwarzania. Walidacja typów dokumentów zwiększa automatyzację przepływów pracy, umożliwia akcje specyficzne dla dokumentu i utrzymuje porządek w rekordach.

## **Przykładowy scenariusz**:

* Użytkownik przesyła dokument oznaczony jako „Debit Note”. Za pomocą operatora „Is” karta potwierdza, że typ dokumentu rzeczywiście jest „Debit Note”, co pozwala systemowi zastosować odpowiednie reguły przetwarzania i właściwie go skategoryzować.

Dzięki zastosowaniu karty „Document Type” organizacje mogą zautomatyzować klasyfikację dokumentów, zapewnić spójność w obsłudze dokumentów i zwiększyć wydajność przepływów pracy związanych z zarządzaniem dokumentami.
