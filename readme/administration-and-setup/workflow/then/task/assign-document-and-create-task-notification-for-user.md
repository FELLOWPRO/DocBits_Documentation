# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Karta przepływu pracy "**Assign Document and Create Task/Notification for User**" przypisuje dokument do określonego użytkownika, tworzy zadanie lub powiadomienie z konfigurowalnymi szczegółami i opcjonalnie wysyła powiadomienie e-mail do użytkownika. Karta ta umożliwia również ustawienie numerycznej wartości priorytetu w celu określenia kolejności wykonywania.

## **Komponenty karty**

1. **User**
   * **Opis:** Określa użytkownika, który otrzyma zadanie lub powiadomienie.
   * **Szczegóły:** Menu rozwijane do wyboru użytkownika, do którego zostanie przypisany dokument i zadanie/powiadomienie.
2. **Task/Notification**
   * **Opis:** Określa typ akcji do utworzenia dla użytkownika.
   * **Szczegóły:** Lista rozwijana do wyboru "Task" lub "Notification" w zależności od zamierzonej akcji.
3. **Title**
   * **Opis:** Tytuł zadania lub powiadomienia.
   * **Szczegóły:** Pole do podania zwięzłego, opisowego tytułu zadania lub powiadomienia.
4. **Description**
   * **Opis:** Dodatkowe szczegóły o zadaniu lub powiadomieniu.
   * **Szczegóły:** Pole do opisania celu zadania lub podania kontekstu powiadomienia.
5. **Priority**
   * **Opis:** Definiuje poziom pilności zadania lub powiadomienia.
   * **Opcje:**
     * **High:** Wymaga natychmiastowej uwagi.
     * **Medium:** Ważne, ale nie pilne.
     * **Low:** Można obsłużyć później.
6. **Send Mail**
   * **Opis:** Konfiguruje, czy powiadomienie e-mail jest wysyłane do użytkownika.
   * **Opcje:**
     * **True:** Wysyła powiadomienie e-mail do użytkownika.
     * **False:** Nie jest wysyłane powiadomienie e-mail.
7. **Value**
   * **Opis:** Ustawia numeryczny priorytet dla przypisania dokumentu.
   * **Szczegóły:** Pole do wprowadzenia wartości liczbowej, gdzie niższe liczby oznaczają wyższy priorytet.

## **Funkcjonalność**

* **Ocena warunku:**\
  Karta wykonuje swoje akcje tylko wtedy, gdy skonfigurowane warunki przepływu pracy są spełnione.
* **Przypisanie dokumentu i utworzenie zadania/powiadomienia:**\
  Dokument jest przypisywany do użytkownika określonego w polu "User". Tworzone jest zadanie lub powiadomienie z podanym tytułem, opisem i poziomem priorytetu.
* **Powiadomienie e-mail:**\
  Jeśli "Send Mail" jest ustawione na True, do użytkownika wysyłany jest e-mail informujący go o zadaniu lub powiadomieniu.

## **Konfiguracja**

1. **Select User:**
   * Wybierz użytkownika z menu rozwijanego User.
2. **Configure Task/Notification Details:**
   * Wybierz "Task" lub "Notification" z listy rozwijanej Task/Notification.
   * Wprowadź Title i Description dla zadania lub powiadomienia.
   * Ustaw Priority, wybierając High, Medium lub Low z listy rozwijanej.
3. **Enable Email Notification:**
   * Skonfiguruj opcję Send Mail na True lub False, w zależności od tego, czy powiadomienie e-mail powinno zostać wysłane.
4. **Set Numeric Priority:**
   * Wprowadź wartość liczbową w polu Value, aby określić priorytet przypisania, gdzie niższe wartości są przetwarzane jako pierwsze.
5. Zapisz konfigurację karty i aktywuj przepływ pracy.

## **Podsumowanie**

Karta przepływu pracy "Assign Document and Create Task/Notification for User" zapewnia, że dokumenty są przypisywane do odpowiedniego użytkownika, jednocześnie tworząc zadania lub powiadomienia ze zdefiniowanymi priorytetami i opcjonalnymi powiadomieniami e-mail. Karta ta pomaga usprawnić delegowanie zadań i zwiększa efektywność przepływu pracy.
