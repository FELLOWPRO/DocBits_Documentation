# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Karta przepływu pracy **"Create Task or Notification"** usprawnia zarządzanie zadaniami i powiadomieniami w ramach przepływów pracy. W zależności od wersji karta może tworzyć zadania, wysyłać powiadomienia i wykorzystywać dodatkową funkcjonalność, taką jak drzewa decyzyjne, do dynamicznego przetwarzania.

## **Komponenty karty**

1. **Title**
   * **Opis**: Definiuje tytuł tworzonego zadania lub powiadomienia.
   * **Szczegóły**: Tytuł zapewnia jasny i zwięzły identyfikator zadania lub powiadomienia.
2. **Description**
   * **Opis**: Dostarcza szczegółów o zadaniu lub powiadomieniu.
   * **Szczegóły**: Pomaga wyjaśnić cel lub kontekst zadania lub powiadomienia dla przypisanego użytkownika.
3. **Priority**
   * **Opis**: Ustawia poziom pilności zadania.
   * **Opcje**:
     * **High**: Wymaga natychmiastowej uwagi.
     * **Medium**: Ważne, ale nie pilne.
     * **Low**: Można obsłużyć później.
4. **Assigned User**
   1. **Opis**: Określa użytkownika, do którego przypisane jest zadanie.
   2. **Szczegóły**: Użytkownicy są wybierani z listy rozwijanej dostępnego personelu.
5. **Email Notification**
   * **Opis**: Określa, czy przypisany użytkownik otrzymuje powiadomienie e-mail.
   * **Opcje**:
     * **True**: Wysyła powiadomienie e-mail do użytkownika.
     * **False**: Nie jest wysyłane powiadomienie e-mail.

## Dodatkowe komponenty **w Version 3 i Version 4**

1. **Decision Tree (tylko Version 3)**
   * **Opis**: Umożliwia użycie drzewa decyzyjnego do dynamicznego tworzenia zadań.
   * **Opcje**:
     * **True**: Aktywuje przetwarzanie drzewa decyzyjnego.
     * **False**: Wyłącza przetwarzanie drzewa decyzyjnego.
2. **Task or Notification (tylko Version 4)**
   * **Opis**: Umożliwia wybór między utworzeniem zadania a powiadomienia.
   * **Opcje**:
     * **Task**: Tworzy zadanie.
     * **Notification**: Tworzy powiadomienie zamiast zadania.

## **Funkcjonalność:**

* **Ocena warunku**:\
  Karta jest wyzwalana tylko wtedy, gdy warunki w sekcjach **"Where"** i **"And Sections"** są spełnione.
* **Tworzenie zadania lub powiadomienia**:
  * Wersje 2 i 3: Tworzone jest zadanie z określonym tytułem, opisem, priorytetem i przypisanym użytkownikiem.
  * Version 4: Umożliwia utworzenie zadania lub powiadomienia.
* **Dynamiczne przypisanie**:
  * W Version 3 drzewo decyzyjne dynamicznie określa użytkownika, do którego ma zostać przypisane zadanie, na podstawie parametrów przepływu pracy.
* **Powiadomienie e-mail**:\
  Wysyła e-mail do przypisanego użytkownika, jeśli opcja powiadomienia jest włączona.

## **Konfiguracja:**

1. **Select Version**: Wybierz wersję karty na podstawie wymaganej funkcjonalności:
   * Version 2: Podstawowe tworzenie zadań z ręcznym przypisaniem użytkownika i powiadomieniami e-mail.
   * Version 3: Zawiera funkcjonalność drzewa decyzyjnego do dynamicznego przypisywania użytkownika.
   * Version 4: Dodaje możliwość utworzenia powiadomienia zamiast zadania.
2. **Enter Task Details**: Określ tytuł, opis i priorytet zadania lub powiadomienia.
3. **Assign User**:
   * Dla wersji 2 i 4 ręcznie wybierz użytkownika z listy rozwijanej.
   * Dla Version 3 włącz drzewo decyzyjne, aby dynamicznie określić przypisanego użytkownika.
4. **Enable Email Notification**: Określ, czy przypisany użytkownik powinien otrzymać powiadomienie e-mail.
5. (Dla Version 4) **Choose Task or Notification**: Wskaż, czy utworzyć zadanie, czy powiadomienie.

## **Podsumowanie:**

Karta przepływu pracy **"Create Task or Notification"** jest wszechstronnym narzędziem do zarządzania zadaniami i powiadomieniami. Wspierając dynamiczne przypisywanie użytkowników za pomocą drzew decyzyjnych i zapewniając opcje tworzenia zadań lub powiadomień, zwiększa elastyczność przepływu pracy i efektywność współpracy.
