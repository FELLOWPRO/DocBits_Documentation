# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Create Task with Fallback"** zapewnia efektywne delegowanie zadań poprzez przypisywanie zadań do określonych ról — dyspozytora lub purchasera — przy jednoczesnym zastosowaniu mechanizmu zapasowego, aby zapobiec niepowodzeniom przypisywania zadań. Karta ta poprawia niezawodność i elastyczność przepływu pracy w dynamicznych scenariuszach.

## **Komponenty karty:**

1. **Title**
   * **Opis**: Określa tytuł tworzonego zadania.
   * **Szczegóły**: Zapewnia zwięzły identyfikator zadania.
2. **Description**
   * **Opis**: Opisuje cel lub kontekst zadania.
   * **Szczegóły**: Wyjaśnia szczegóły zadania.
3. **Priority**
   * **Opis**: Ustawia poziom pilności zadania.
   * **Opcje**:
     * **High**: Wymaga natychmiastowej uwagi.
     * **Medium**: Ważne, ale nie pilne.
     * **Low**: Można obsłużyć później.
4. **Assigned Role**
   * **Opis**: Określa podstawową rolę, do której przypisywane jest zadanie.
   * **Opcje**:
     * **Disponent**: Przypisuje zadanie do disponenta.
     * **Purchaser**: Przypisuje zadanie do purchasera.
5. **Email Notification**
   * **Opis**: Umożliwia powiadomienie przypisanego użytkownika za pośrednictwem e-maila.
   * **Opcje**:
     * **True**: Wysyła powiadomienie e-mail do użytkownika.
     * **False**: Nie jest wysyłane powiadomienie e-mail.
6. **Fallback User**
   * **Opis**: Zapewnia opcję zapasową dla przypisania zadania, jeśli rola odbiorcy nie zostanie znaleziona.
   * **Szczegóły**: Umożliwia wybór użytkownika z listy rozwijanej w celu zapewnienia delegowania zadania.

## **Funkcjonalność:**

* **Ocena warunku**:\
  Karta wykonuje się tylko wtedy, gdy warunki w sekcjach **"Where"** i **"And Sections"** są spełnione.
* **Przypisanie zadania**:
  * Zadanie jest przypisywane do wybranej roli (disponent lub purchaser).
  * Jeśli określona rola nie zostanie znaleziona, zadanie jest przypisywane do użytkownika z zapasowej listy rozwijanej.
* **Powiadomienie e-mail**:\
  Wysyła e-mail do przypisanego użytkownika, jeśli powiadomienie e-mail jest włączone.

## **Konfiguracja:**

1. **Specify Task Details**: Wprowadź tytuł, opis i priorytet zadania.
2. **Select Primary Role**: Wybierz rolę, do której zostanie przypisane zadanie (disponent lub purchaser).
3. **Configure Fallback User**: Wybierz użytkownika zapasowego z listy rozwijanej, aby zapewnić przypisanie zadania, jeśli podstawowa rola nie zostanie znaleziona.
4. **Enable Email Notification**: Wskaż, czy przypisany użytkownik powinien otrzymać powiadomienie e-mail.

## **Podsumowanie:**

Karta przepływu pracy **"Create Task with Fallback"** zapewnia bezproblemowe delegowanie zadań poprzez zintegrowanie mechanizmu zapasowego. Przypisując zadania na podstawie ról i zapewniając alternatywną opcję użytkownika, zwiększa niezawodność i elastyczność w procesach zarządzania zadaniami.
