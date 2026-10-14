# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Karta przepływu pracy "**Assign Document and Create Task/Notification Based on Decision Table**" przypisuje dokument i tworzy zadanie lub powiadomienie z konfigurowalnymi szczegółami. Osoba przypisana jest określana na podstawie zwrotu tabeli decyzyjnej, a karta umożliwia ustawianie priorytetów i wysyłanie powiadomień e-mail.

## **Komponenty karty**

1. **Assignee Type**
   * **Opis:** Określa, czy zwrot tabeli decyzyjnej przypisuje dokument i zadanie/powiadomienie do użytkownika, czy grupy.
   * **Szczegóły:** Pole do skonfigurowania typu osoby przypisanej jako "User" lub "Group" na podstawie wyniku tabeli decyzyjnej.
2. **Task/Notification**
   * **Opis:** Określa typ akcji do utworzenia dla osoby przypisanej.
   * **Szczegóły:** Lista rozwijana do wyboru "Task" lub "Notification" na podstawie potrzeb przepływu pracy.
3. **Title**
   * **Opis:** Tytuł zadania lub powiadomienia.
   * **Szczegóły:** Pole do podania zwięzłego tytułu identyfikującego zadanie lub powiadomienie.
4. **Description**
   * **Opis:** Dodatkowe szczegóły o zadaniu lub powiadomieniu.
   * **Szczegóły:** Pole do opisania celu i kontekstu zadania lub powiadomienia.
5. **Priority**
   * **Opis:** Definiuje poziom pilności zadania lub powiadomienia.
   * **Opcje:**
     * **High:** Wymaga natychmiastowej uwagi.
     * **Medium:** Ważne, ale nie pilne.
     * **Low:** Można obsłużyć później.
6. **Assignee Type**
   * **Opis:** To pole określa typ osoby przypisanej (User lub Group), do której przypisywany jest dokument i zadanie/powiadomienie.
   * **Szczegóły:** Menu rozwijane do wyboru, czy zadanie/powiadomienie jest przypisane do użytkownika, czy grupy na podstawie wyniku tabeli decyzyjnej.
7. **Send Mail**
   * **Opis:** Konfiguruje, czy powiadomienie e-mail jest wysyłane do osoby przypisanej.
   * **Opcje:**
     * **True:** Wysyła powiadomienie e-mail.
     * **False:** Nie jest wysyłane powiadomienie e-mail.
8. **Value**
   * **Opis:** Ustawia numeryczny priorytet dla przypisania dokumentu.
   * **Szczegóły:** Pole do wprowadzenia wartości liczbowej, gdzie niższe liczby oznaczają wyższy priorytet.

## **Funkcjonalność**

* **Ocena warunku:**\
  Karta wykonuje swoje akcje tylko wtedy, gdy warunki przepływu pracy są spełnione.
* **Ocena tabeli decyzyjnej:**\
  Tabela decyzyjna określa, czy dokument i zadanie/powiadomienie są przypisane do użytkownika, czy grupy.
* **Przypisanie dokumentu i utworzenie zadania/powiadomienia:**\
  Dokument jest przypisywany do wyniku tabeli decyzyjnej. Tworzone jest zadanie lub powiadomienie z określonym tytułem, opisem i poziomem priorytetu.
* **Powiadomienie e-mail:**\
  Jeśli "Send Mail" jest ustawione na True, powiadomienie e-mail jest wysyłane do osoby przypisanej.

## **Konfiguracja**

1. **Define Assignee Type:**
   * Skonfiguruj pole Assignee Type jako "User" lub "Group" na podstawie wyniku tabeli decyzyjnej.
2. **Select Task/Notification:**
   * Wybierz "Task" lub "Notification" z listy rozwijanej Task/Notification.
3. **Set Task/Notification Details:**
   * Wprowadź Title i Description dla zadania lub powiadomienia.
   * Wybierz Priority (High, Medium lub Low) z listy rozwijanej.
4. **Enable Email Notification:**
   * Ustaw opcję Send Mail na True lub False, w zależności od tego, czy powiadomienie e-mail powinno zostać wysłane.
5. **Set Numeric Priority:**
   * Wprowadź wartość liczbową w polu Value, aby określić priorytet przypisania, gdzie niższe liczby są przetwarzane jako pierwsze.
6. Zapisz konfigurację karty i aktywuj przepływ pracy.

## **Podsumowanie**

Karta przepływu pracy "Assign Document and Create Task/Notification Based on Decision Table" zapewnia, że zadania lub powiadomienia są dynamicznie przypisywane do odpowiedniego użytkownika lub grupy na podstawie wyników tabeli decyzyjnej. Karta ta ułatwia efektywne delegowanie zadań, konfigurowalne priorytety i opcjonalne powiadomienia e-mail w celu zwiększenia responsywności przepływu pracy.
