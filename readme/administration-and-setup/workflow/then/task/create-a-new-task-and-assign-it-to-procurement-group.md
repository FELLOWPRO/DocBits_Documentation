# Create a New Task and assign it to Procurement Group

<figure><img src="../../../../.gitbook/assets/image (292).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Create Task for Procurement Group"** tworzy nowe zadanie dynamicznie przypisane do grupy zakupowej określonej w konfiguracji. Zadanie to może być przypisane z różnymi poziomami priorytetu, a opcjonalne powiadomienie e-mail może zostać wysłane w celu poinformowania grupy o zadaniu. Karta ta zapewnia, że właściwy zespół jest powiadamiany na podstawie warunków przepływu pracy.

## **Komponenty karty:**

1. **Title**
   * **Opis:** Określa tytuł zadania.
   * **Szczegóły:** To pole identyfikuje tworzone zadanie, zapewniając zwięzły tytuł ułatwiający identyfikację.
2. **Description**
   * **Opis:** Dostarcza dalszych szczegółów o zadaniu.
   * **Szczegóły:** To pole służy do opisania celu zadania oraz wszelkiego niezbędnego kontekstu lub instrukcji.
3. **Priority**
   * **Opis:** Definiuje pilność zadania.
   * **Opcje:**
     * **High:** Zadanie wymaga natychmiastowej uwagi.
     * **Medium:** Zadanie jest ważne, ale nie pilne.
     * **Low:** Zadaniem można się zająć później.
4. **Group Name**
   * **Opis:** Określa grupę zakupową, do której zostanie przypisane zadanie.
   * **Szczegóły:** To pole wyznacza grupę zakupową odpowiedzialną za zadanie. Zapewnia, że zadanie jest kierowane do właściwego zespołu.
5. **Email Notification**
   * **Opis:** Konfiguruje, czy powiadomienie e-mail powinno zostać wysłane do przypisanej grupy zakupowej.
   * **Opcje:**
     * **True:** Wysyła powiadomienie e-mail do grupy zakupowej.
     * **False:** Nie jest wysyłane powiadomienie e-mail.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Tworzenie zadania:**\
  Karta tworzy nowe zadanie, przypisując je do grupy zakupowej zdefiniowanej w polu "Group Name". Zadanie to będzie zawierać określony tytuł, opis i poziom priorytetu.
* **Powiadomienie e-mail:**\
  Jeśli opcja powiadomienia e-mail jest ustawiona na true, do grupy zakupowej wysyłany jest e-mail informujący ją o zadaniu.

## **Konfiguracja:**

* **Define Task Details:**\
  Wprowadź tytuł zadania, opis i poziom priorytetu.
* **Select Procurement Group:**\
  Wybierz grupę zakupową, która będzie odpowiedzialna za zadanie.
* **Enable Email Notification:**\
  Określ, czy powiadomienie e-mail powinno zostać wysłane do grupy po utworzeniu zadania.

## **Podsumowanie:**

Karta przepływu pracy "Create Task for Procurement Group" zapewnia, że zadania są automatycznie przypisywane do odpowiedniej grupy zakupowej ze zdefiniowanymi priorytetami. Karta ta może również powiadamiać grupę za pośrednictwem e-maila, aby zapewnić szybką obsługę zadań, poprawiając efektywność przepływu pracy i zarządzanie zadaniami.
