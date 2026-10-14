# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Change Status"** służy do zmiany statusu dokumentu na jeden z predefiniowanych stanów — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — i opcjonalnie wyzwala powiązane przepływy pracy na podstawie zmiany statusu. Karta ta automatyzuje proces aktualizacji statusów i wyzwalania przepływów pracy, zapewniając efektywne zarządzanie dokumentami i obsługę błędów.

## **Komponenty karty:**

1. **Status**
   * **Opis**: Określa nowy status, który ma zostać zastosowany do dokumentu.
   * **Opcje**:
     * **Error**: Oznacza dokument jako taki, który napotkał błąd.
     * **Rejected**: Wskazuje, że dokument został odrzucony i nie będzie dalej procesowany.
     * **Ready for Validation**: Ustawia dokument do przeglądu i walidacji przez następnego użytkownika lub proces systemowy.
     * **Pending Approval**: Umieszcza dokument w stanie oczekiwania na zatwierdzenie.
     * **Pending Second Approval**: Wstrzymuje dokument do drugiego poziomu zatwierdzenia, jeśli dotyczy.
2. **Trigger Workflows**
   * **Opis**: Określa, czy po zmianie statusu powinny zostać wyzwolone jakiekolwiek kolejne przepływy pracy.
   * **Opcje**:
     * **True**: Inicjuje wszelkie istotne przepływy pracy na podstawie zmiany statusu.
     * **False**: Zapobiega wykonaniu przepływu pracy po zmianie statusu.

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki ustawione w sekcjach **"Where"** i **"And Sections."** Jeśli te warunki są prawdziwe, karta przystępuje do zmiany statusu dokumentu na wybraną wartość.
* **Aktualizacja statusu**: Gdy warunki są spełnione, status dokumentu jest aktualizowany na jedną z predefiniowanych opcji (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), w zależności od wyboru użytkownika.
* **Akcja wyzwalania przepływu pracy**: Jeśli **Trigger Workflows** jest ustawione na **True**, system automatycznie inicjuje wszelkie powiązane przepływy pracy po aktualizacji statusu. Jeśli ustawione na **False**, nie są wyzwalane żadne dodatkowe przepływy pracy, a proces kończy się zmianą statusu.

## **Konfiguracja:**

Aby skonfigurować tę kartę, użytkownicy muszą:

1. Określić żądany **Status**, na który dokument zostanie ustawiony po ocenie warunku (Error, Rejected, Ready for Validation, Pending Approval lub Pending Second Approval).
2. Wybrać, czy **Trigger Workflows** po zmianie statusu, wybierając **True** lub **False**.
3. Karta wykonuje swoją akcję tylko wtedy, gdy oba warunki w sekcjach **"Where"** i **"And Sections"** są prawdziwe.

## **Podsumowanie:**

Karta przepływu pracy **"Change Status"** oferuje usprawnione podejście do zarządzania statusami dokumentów i wyzwalania powiązanych przepływów pracy. Zapewnia, że dokumenty są automatycznie kierowane do właściwego statusu i że podejmowane są niezbędne akcje, w zależności od zmiany statusu. Ustawiając jasne warunki wykonania, redukuje ręczny wysiłek i zwiększa efektywność przepływu pracy.
