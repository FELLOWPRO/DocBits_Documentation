# Ekstrakcja tabeli dla elementu kosztowego

Elementy kosztowe to opłaty lub inne kwoty przedstawione jako pozycje w tabeli faktury. Jeśli ta funkcja jest włączona i dokument ma wyodrębnione pozycje, DocBits może klasyfikować te pozycje względem elementów kosztowych skonfigurowanych dla organizacji. Osoba weryfikująca może poprawić klasyfikację pozycji w tabeli dokumentu.

## Włączanie ustawienia

1. Otwórz **Ustawienia → Typy dokumentów** i wybierz **Klasyfikacja i ekstrakcja** pod pozycją **Typy dokumentów**.
2. Pozostań na karcie **Ogólny** i rozwiń sekcję **Ekstrakcja**.
3. Znajdź **Ekstrakcja tabeli dla elementu kosztowego** poniżej pól wymaganych do ekstrakcji tabeli. Administrator może włączyć ten przełącznik dla organizacji.

<figure><img src="../../../../.gitbook/assets/table-extraction-costing-setting-pl-20261111.png" alt="Sekcja Ekstrakcja w ustawieniach Klasyfikacja i ekstrakcja z przełącznikami Ekstrakcja tabeli, Ekstrakcja tabeli AI, Użyj wizji ekstrakcji tabeli (AI), Użyj ekstrakcji strukturalnej (AI), Ekstrakcja tabeli dla elementu kosztowego, Automatyczne wyodrębnianie kodu podatkowego, Zapisz zasady ekstrakcji (tylko administrator) i Wyodrębnij ukryte pola oraz selektorem modelu AI"><figcaption><p>Przełącznik <strong>Ekstrakcja tabeli dla elementu kosztowego</strong> znajduje się między opcjami <strong>Użyj ekstrakcji strukturalnej (AI)</strong> i <strong>Automatyczne wyodrębnianie kodu podatkowego</strong>. W organizacji używanej na potrzeby tego przewodnika jest wyłączony.</p></figcaption></figure>

{% hint style="info" %}
Sam przełącznik nie tworzy elementów kosztowych ani pozycji faktury. Najpierw skonfiguruj elementy i zaimportuj wymagane dane. Połączony [przewodnik konfiguracji elementów kosztowych](../../../../infor-integration-and-configuration/importing-customer-master-data/m3/table-extraction-for-costing-element.md) pokazuje przykład M3. Inne ustawienia ekstrakcji opisuje strona [Klasyfikacja i ekstrakcja](README.md).
{% endhint %}

## Sprawdzanie lub poprawianie pozycji

Otwórz dokument, którego tabela faktury zawiera wyodrębnione pozycje, i odszukaj ikonę elementu kosztowego obok odpowiedniej pozycji. Wybierz ikonę, aby otworzyć dostępne klasyfikacje. Wybierz właściwy skonfigurowany element kosztowy albo wybierz opcję **Niekategoryzowane**, jeśli pozycja jest zwykłym artykułem. Następnie sprawdź wynikową pozycję i sumy przed zapisaniem dokumentu.

Jeśli ikona lub klasyfikacja jest niedostępna, najpierw upewnij się, że dokument ma wyodrębnione pozycje, funkcja jest włączona, a dla organizacji skonfigurowano element kosztowy.
