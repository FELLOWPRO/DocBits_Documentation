# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy "Assign Task / Notification from Decision Table" służy do dynamicznego przypisywania zadań lub powiadomień na podstawie wyników tabeli decyzyjnej. Karta ta zapewnia, że zadania lub powiadomienia są przypisywane do właściwego użytkownika lub grupy zgodnie z logiką zdefiniowaną w tabeli decyzyjnej, z opcjonalnym powiadomieniem e-mail wysyłanym do odbiorcy.

## **Komponenty karty:**

1. **Title**
   * **Opis**: Określa tytuł tworzonego zadania lub powiadomienia.
   * **Szczegóły**: Tytuł powinien zapewniać kontekst i opisywać cel zadania lub powiadomienia.
2. **Description**
   * **Opis**: Definiuje treść lub cel zadania lub powiadomienia.
   * **Szczegóły**: Dostarcza dodatkowych informacji o zadaniu lub powiadomieniu, wyjaśniając kontekst lub wymaganą akcję.
3. **Priority**
   * **Opis**: Definiuje poziom pilności zadania lub powiadomienia.
   * **Opcje**:
     * **High**: Zadania lub powiadomienia wymagające natychmiastowej uwagi.
     * **Medium**: Ważne zadania, które powinny zostać szybko obsłużone.
     * **Low**: Zadania, którymi można się zająć później.
4. **Assignee Type**
   * **Opis**: Określa użytkownika lub grupę przypisaną do zadania lub powiadomienia na podstawie wyniku tabeli decyzyjnej.
   * **Szczegóły**: Tabela decyzyjna dynamicznie ocenia warunki i zwraca odpowiedniego użytkownika lub grupę do przypisania.
5. **Email Notification**
   * **Opis**: Konfiguruje, czy powiadomienie e-mail zostanie wysłane do przypisanego użytkownika lub grupy.
   * **Opcje**:
     * **True**: Wysyła powiadomienie e-mail do odbiorcy.
     * **False**: Nie jest wysyłane powiadomienie e-mail.

#### **Dodatkowe komponenty w Version 3**

1. **Notification Type**
   * **Opis**: Określa, czy karta tworzy zadanie, czy powiadomienie.
   * **Opcje**:
     * **Task**: Tworzy zadanie przypisane do użytkownika lub grupy z tabeli decyzyjnej.
     * **Notification**: Wysyła powiadomienie do użytkownika lub grupy z tabeli decyzyjnej.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Przypisanie zadania / powiadomienia**\
  Karta przypisuje zadanie lub powiadomienie do użytkownika lub grupy zidentyfikowanej przez tabelę decyzyjną. Tabela decyzyjna dynamicznie ocenia predefiniowane warunki i zwraca odpowiedniego odbiorcę.
* **Powiadomienie e-mail**\
  Jeśli tak skonfigurowano, powiadomienie e-mail jest wysyłane do przypisanego użytkownika lub grupy.
* **Funkcjonalność Version 3**\
  W Version 3 karta umożliwia utworzenie zadania (Task) lub powiadomienia (Notification), zapewniając większą elastyczność w zarządzaniu zadaniami i komunikacji.

## **Konfiguracja:**

1. **Define Task or Notification Details**:\
   Wprowadź tytuł, opis i priorytet zadania lub powiadomienia.
2. **Configure Decision Table**:\
   Skonfiguruj tabelę decyzyjną, aby dynamicznie określać, który użytkownik lub grupa powinni zostać przypisani do zadania lub powiadomienia.
3. **Enable Email Notification**:\
   Określ, czy powiadomienie e-mail powinno zostać wysłane do przypisanego użytkownika lub grupy.
4. **Specify Notification Type (Version 3)**:\
   Wybierz, czy karta utworzy zadanie, czy wyśle powiadomienie.

## **Podsumowanie:**

Karta przepływu pracy **"Assign Task / Notification from Decision Table"** automatyzuje przypisywanie zadań lub powiadomień na podstawie dynamicznych warunków zdefiniowanych w tabeli decyzyjnej. Version 3 zwiększa jej funkcjonalność, umożliwiając użytkownikom wybór między utworzeniem zadania a powiadomienia, oraz zapewnia, że zawsze przypisywany jest właściwy odbiorca. Funkcja powiadomień e-mail informuje użytkowników na bieżąco, usprawniając komunikację i zarządzanie zadaniami.
