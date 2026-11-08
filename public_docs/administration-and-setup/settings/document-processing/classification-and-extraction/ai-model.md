# AI Model

## Przegląd

Ustawienie **AI Model** pozwala zdefiniować, który model AI jest domyślnie używany do **ekstrakcji pól** i **ekstrakcji tabel** podczas przetwarzania dokumentów.\
Użyj bieżącego selektora modelu i tabeli preferencji szablonu, aby przejrzeć ustawienie organizacji i nadpisania. W kwestii kosztów zapoznaj się z informacjami dostępnymi w Twoim środowisku i warunkami subskrypcji.

## Jak uzyskać dostęp

1.  Przejdź do **Settings** → **Document Types** → **Classification and Extraction** → **General**

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/site-complete-global-ai-model-options-en.png" alt="Bieżące ustawienia ekstrakcji i menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto i Auto Nexus. Prywatne wartości tabeli są ukryte; nie wybrano modelu ani nie usunięto preferencji."><figcaption><p>Bieżące ustawienia ekstrakcji i menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto i Auto Nexus. Prywatne wartości tabeli są ukryte; nie wybrano modelu ani nie usunięto preferencji.</p></figcaption></figure>
2.  Rozwiń **Extraction** i znajdź ustawienie **AI Model**.



## Opcje modelu AI

Bieżące menu oferuje **Full**, **Fast**, **Nexus**, **Nexus Flash**, **Auto** i **Auto Nexus**. To nazwy poziomów produktu. Dostępne opcje, modele bazowe i koszty tokenów mogą się zmieniać; sprawdzaj informacje w bieżącym środowisku i warunki subskrypcji, zamiast opierać się na historycznej nazwie modelu dostawcy lub stałej cenie.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-3-six-model-options-en-20261031.png" alt="Bieżące menu rozwijane AI Model z opcjami Full, Fast, Nexus, Nexus Flash, Auto i Auto Nexus"><figcaption><p>Szczegół sześciu poziomów ekstrakcji w bieżącym menu środowiska deweloperskiego. Otwarcie i zamknięcie menu pozostawiło istniejący wybór bez zmian.</p></figcaption></figure>

| Opcja | Co sprawdzić na reprezentatywnych dokumentach |
| --- | --- |
| **Full** | Wyniki ekstrakcji dla złożonych układów, czas przetwarzania i koszt. |
| **Fast** | Wyniki i czas przetwarzania dla codziennych dokumentów; nazwa nie jest gwarancją dla każdego dokumentu. |
| **Nexus** | Porównaj tę alternatywną opcję na tej samej próbce dokumentów. |
| **Nexus Flash** | Sprawdź zarówno jakość, jak i opóźnienie na rzeczywistych układach. |
| **Auto** | Sprawdź wyniki i koszty automatycznego wyboru. |
| **Auto Nexus** | Sprawdź wyniki i koszty opcji automatycznego wyboru Nexus. |

Gdy bieżący szablon ekstrakcji nie ma nadpisania, jego ustawienie modelu przechodzi na konfigurację organizacji. Nieustawiona wartość specyficzna dla dostawcy nie oznacza powszechnie Fast. Porównaj stałą próbkę przed zmianą modelu; sama zmiana modelu nie gwarantuje walidacji pól, uzgodnienia z zamówieniem, zatwierdzenia ani udanego eksportu.



## Tabela przypisań modeli AI

**Ekran walidacji** udostępnia punkt wejścia dla modelu specyficznego dla dostawcy. Jego nadpisanie jest zapisywane dla organizacji i bieżącego szablonu ekstrakcji (`tfidf_id`); nie aktualizuje bezwarunkowo każdego szablonu ani dokumentu historycznego należącego do tego samego dostawcy.\
\
Więcej informacji znajdziesz w odpowiedniej dokumentacji [tutaj](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

Tabela przypisań podsumowuje preferencje ekstrakcji związane z szablonem. Kolumny różnią się w zależności od wersji produktu; używaj bieżących nagłówków, aby sprawdzić powiązanie z dostawcą, model, opcje ekstrakcji i informacje audytowe:

* **Supplier ID** – Unikalny identyfikator dostawcy
* **AI Model** – Poziom skonfigurowany dla tego wpisu szablonu
* **Use Structured Extraction (AI)**, jeśli występuje – Preferencja ekstrakcji strukturalnej tego wpisu
* **E-Text** – Wskazuje, czy funkcja E-Text jest włączona
* **Created By / Modified By / Created On / Modified On** – Kto ustawił wpis i kiedy
* **Action** – Zawiera opcję usunięcia wpisu



### Usuwanie wpisu — usuwanie nadpisań szablonu

Zanim administrator usunie wpis, musi ustalić jego szablon ekstrakcji i wszystkie zawarte w nim preferencje. Usunięcie może usunąć kilka nadpisań szablonu, nie tylko ustawienie modelu:

1.  Kliknij trzy kropki w kolumnie **Action** obok wpisu dostawcy i wybierz **Delete**.


2.  Pojawi się okno potwierdzenia — potwierdź, że chcesz usunąć wpis.



Po usunięciu dalsze przetwarzanie odczytuje obowiązującą konfigurację organizacji i wartości zapasowe dla tego szablonu. Inne szablony powiązane z tym samym dostawcą mogą zachować własne nadpisania. Usunięcie nie przetwarza automatycznie dokumentów historycznych. W tym przewodniku nie usunięto żadnego wpisu ani nie wykonano wynikającej z tego ekstrakcji.

## Ustawienia i nadpisania

Structured Output ma osobne ustawienie organizacji/szablonu, niezależne od poziomu modelu. Zmień je w More options na dokumencie; potwierdzenie zapisuje nadpisanie i ponownie uruchamia ten dokument. Wskaźniki na liście ustawień są tylko do odczytu. Usunięcie wpisu preferencji może usunąć kilka nadpisań jednocześnie. [Structured Output dla tabel](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
