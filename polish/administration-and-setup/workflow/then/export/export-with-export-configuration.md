# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Export Document with Export Configuration"** służy do eksportu dokumentu przy użyciu określonej konfiguracji eksportu. Zapewnia elastyczność ignorowania wszelkich oczekujących zadań powiązanych z dokumentem, zapewniając płynny proces eksportu niezależnie od jego bieżącego stanu.

## **Komponenty karty:**

1. **Export Configuration**
   * **Opis**: Określa konfigurację eksportu, która ma być użyta do przetworzenia dokumentu.
   * **Szczegóły**: Konfiguracja ta określa format, strukturę i miejsce docelowe eksportowanego dokumentu.
2. **Ignore Pending Tasks**
   * **Opis**: Określa, czy oczekujące zadania powiązane z dokumentem powinny zostać pominięte podczas procesu eksportu.
   * **Opcje**:
     * **True**: Eksportuje dokument niezależnie od oczekujących zadań.
     * **False**: Zapewnia ukończenie oczekujących zadań przed eksportem.

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki ustawione w sekcjach **"Where"** i **"And Sections"** przepływu pracy. Jeśli oba warunki są prawdziwe, proces eksportu jest inicjowany.
* **Eksport dokumentu**: Przy użyciu określonej **Export Configuration** dokument jest przetwarzany i eksportowany w zdefiniowanym formacie i miejscu docelowym.
* **Obsługa oczekujących zadań**: Jeśli **Ignore Pending Tasks** jest ustawione na **True**, proces eksportu pomija wszelkie zaległe zadania powiązane z dokumentem. Jeśli ustawione na **False**, eksport jest odroczony do czasu rozwiązania wszystkich zadań.

## **Konfiguracja:**

Aby skonfigurować tę kartę, użytkownicy muszą:

1. Wybrać żądaną **Export Configuration**, aby zdefiniować, jak dokument zostanie wyeksportowany.
2. Wybrać, czy **Ignore Pending Tasks**, ustawiając wartość na **True** lub **False.**
3. Upewnić się, że warunki w sekcjach **"Where"** i **"And Sections"** są prawidłowo ustawione, ponieważ karta wykonuje swoją akcję tylko wtedy, gdy te warunki są prawdziwe.

## **Podsumowanie:**

Karta przepływu pracy **"Export Document with Export Configuration"** zapewnia, że dokumenty są eksportowane efektywnie i zgodnie z predefiniowanymi konfiguracjami. Dzięki możliwości ignorowania oczekujących zadań karta ta oferuje elastyczność w obsłudze dokumentów na różnych etapach, redukując opóźnienia i usprawniając proces eksportu.
