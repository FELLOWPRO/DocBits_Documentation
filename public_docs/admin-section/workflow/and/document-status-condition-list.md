# Lista warunków statusu dokumentu

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta została zaprojektowana w celu kontrolowania działań w toku pracy na podstawie bieżącego statusu dokumentu, używając logiki warunkowej do wyzwalania lub ograniczania określonych procesów. Zapewnia, że dokumenty przechodzą przez przepływy pracy tylko wtedy, gdy spełniają określone kryteria statusu.

**Składniki karty**

1. **Operator**
* **Opis**: Określa, w jaki sposób status dokumentu będzie oceniany w porównaniu do określonego warunku.
* **Opcje**:
* **jest**: Wywołuje powiązane działania, jeśli bieżący status dokumentu pasuje do jednego z określonych statusów.
* **nie jest**: Wywołuje działania, jeśli status dokumentu nie pasuje do żadnego z określonych statusów.
2. **Status ( Lista )**&#x20;
* **Opis**: Wyświetla konkretne statusy, do których bieżący status dokumentu będzie porównywany.
* **Przykłady**: "Błąd", "Błąd eksportu", "Gotowy do walidacji", "Gotowy do przeglądu", "Oczekujący na zatwierdzenie", "Oczekujący na drugie zatwierdzenie". Oznaczają one różne etapy lub warunki, w jakich dokument może znajdować się w procesie przepływu pracy.

**Funkcjonalność**

* **Identyfikacja statusu**: Automatycznie identyfikuje bieżący status dokumentu w miarę jego przemieszczania się przez system ERP.
* **Ocena warunku**: Stosuje wybrany operator (jest lub nie jest) do statusu dokumentu w porównaniu do wymienionych statusów:
* Jeśli **jest**, sprawdza, czy status dokumentu pasuje do któregokolwiek z statusów na liście.
* Jeśli **nie jest**, sprawdza, czy status dokumentu nie występuje na liście.
* **Wykonanie działania**: W zależności od wyniku oceny warunku:
* **Prawda**: Wykonuje zdefiniowane wcześniej działania lub przepływy pracy, jeśli warunek jest spełniony.
* **Fałsz**: Pomija lub wywołuje alternatywne przepływy pracy, jeśli warunek nie jest spełniony.
* **Integracja z przepływem pracy**: Łączy się bezproblemowo z innymi składnikami przepływu pracy, zapewniając koordynację obsługi dokumentów w całym systemie.

**Interakcje użytkownika**

* **Konfiguracja i ustawienia**: Użytkownicy konfigurują kartę, wybierając operatora i określając odpowiednie statusy. Konfiguracja ta może obejmować proste menu rozwijane lub pola wyboru do wybierania statusów i operatorów.
* **Monitorowanie i zarządzanie**: Użytkownicy mogą śledzić aktywność karty za pomocą pulpitu, który dostarcza informacji na temat monitorowanych warunków statusu i podejmowanych działań na ich podstawie.
* **Obsługa błędów i alertów**: Obsługuje ustawianie alertów dla awarii procesu lub niezgodności oczekiwanych statusów dokumentów, umożliwiając szybką reakcję na problemy operacyjne.

#### Podsumowanie

Karta przepływu pracy "Warunek statusu dokumentu" jest kluczowa dla zapewnienia poprawnej obróbki dokumentów zgodnie z ich bieżącym statusem, zwiększając kontrolę i efektywność w systemie ERP. Dokumentowanie tej karty w podręczniku systemowym pomoże użytkownikom skutecznie ją wdrożyć i zarządzać, wykorzystując jej funkcjonalność do utrzymania płynnych i zgodnych przepływów dokumentów. Ta karta jest szczególnie przydatna w zarządzaniu cyklami życia dokumentów i zapewnianiu, że tylko dokumenty spełniające określone kryteria przechodzą do kolejnych etapów procesów biznesowych.
