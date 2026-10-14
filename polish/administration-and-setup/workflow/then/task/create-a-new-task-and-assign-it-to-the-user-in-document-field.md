# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Create Field-Based Task or Notification"** służy do tworzenia zadań lub powiadomień dynamicznie przypisanych do użytkowników zidentyfikowanych w określonych polach dokumentu. Karta ta zapewnia opcjonalny mechanizm zapasowy, aby zapewnić płynne wykonywanie przepływu pracy nawet wtedy, gdy pole dokumentu nie określa prawidłowego użytkownika.

## **Komponenty karty:**&#x20;

1. **Title**
   * **Opis**: Określa tytuł zadania lub powiadomienia.
   * **Szczegóły**: Służy do nazwania i identyfikacji tworzonego zadania lub powiadomienia.
2. **Description**
   * **Opis**: Dostarcza dodatkowych szczegółów o zadaniu lub powiadomieniu.
   * **Szczegóły**: Zapewnia, że odbiorca rozumie cel i kontekst zadania lub powiadomienia.
3. **Priority**
   * **Opis**: Definiuje pilność zadania lub powiadomienia.
   * **Opcje**:
     * **High**: Wymaga natychmiastowej uwagi.
     * **Medium**: Ważne, ale mniej pilne.
     * **Low**: Można obsłużyć później.
4. **Field Name**
   * **Opis**: Określa pole dokumentu, które zostanie użyte do przypisania zadania lub powiadomienia.
   * **Szczegóły**: Wybrane pole dynamicznie określi użytkownika, do którego zostanie przypisane zadanie lub powiadomienie. Jeśli pole jest puste lub nieprawidłowe, zadanie lub powiadomienie zostanie przypisane do użytkownika zapasowego wybranego z listy rozwijanej.
5. **Email Notification**
   * **Opis**: Konfiguruje, czy przypisany użytkownik jest powiadamiany za pośrednictwem e-maila.
   * **Opcje**:
     * **True**: Wysyła powiadomienie e-mail do przypisanego użytkownika.
     * **False**: Nie jest wysyłane powiadomienie e-mail.
6. **Fallback User**
   * **Opis**: Umożliwia wybór użytkownika z listy rozwijanej w celu przypisania zadania lub powiadomienia, gdy w polu dokumentu nie zostanie znaleziony prawidłowy użytkownik.
   * **Szczegóły**: Zapewnia przypisanie zadania lub powiadomienia, nawet jeśli pole dokumentu jest puste lub nieprawidłowe.

## **Dodatkowe komponenty w Version 3:**

1. **Notification Type**&#x20;
   * **Opis**: Określa, czy karta tworzy zadanie, czy powiadomienie.
   * **Opcje**:
     * **Task**: Tworzy zadanie przypisane do określonego użytkownika.
     * **Notification**: Wysyła powiadomienie zamiast tworzenia zadania.

## **Funkcjonalność:**

* **Ocena warunku**:\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Tworzenie zadania lub powiadomienia**:
  * Przypisuje zadanie lub powiadomienie do użytkownika zidentyfikowanego w polu dokumentu.
  * W Version 3 umożliwia utworzenie zadania lub powiadomienia.
* **Mechanizm zapasowy**:\
  Jeśli pole dokumentu nie identyfikuje prawidłowego użytkownika, karta przypisuje zadanie lub powiadomienie do użytkownika zapasowego wybranego z listy rozwijanej.
* **Powiadomienie e-mail**:\
  Wysyła powiadomienie e-mail do przypisanego użytkownika, jeśli tak skonfigurowano.

## **Konfiguracja:**

1. **Define Task or Notification Details**: Wprowadź tytuł, opis i priorytet.
2. **Select the Document Field**: Wybierz pole, które określa użytkownika do przypisania zadania lub powiadomienia.
3. **Enable Email Notification**: Określ, czy powiadomienie e-mail powinno zostać wysłane do przypisanego użytkownika.
4. **Select Fallback User**: Wybierz użytkownika zapasowego z listy rozwijanej do przypisania, jeśli pole dokumentu nie identyfikuje prawidłowego użytkownika.
5. **Specify Notification Type (Version 3)**: Wskaż, czy karta tworzy zadanie, czy powiadomienie.

## **Podsumowanie:**

Karta przepływu pracy **"Create Field-Based Task or Notification"** usprawnia zarządzanie zadaniami i powiadomieniami poprzez dynamiczne przypisywanie obowiązków na podstawie pól dokumentu. Jej mechanizm użytkownika zapasowego i rozszerzone opcje w Version 3 zapewniają elastyczność, gwarantując, że zadania lub powiadomienia są zawsze przypisywane, nawet gdy dane dokumentu są niekompletne.
