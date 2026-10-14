# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do porównania typu zamówienia w zamówieniu zakupu z określoną wartością. Karta sprawdza, czy typ zamówienia w zamówieniu zakupu spełnia określony warunek (np. czy jest równy, nierówny, większy niż lub spełnia inny warunek), aby zapewnić, że zamówienie zakupu jest prawidłowo sklasyfikowane. Porównanie to może wyzwalać akcje na podstawie określonych warunków, takie jak przekierowanie zamówienia do dalszego przeglądu lub zatwierdzenia w przypadku wykrycia rozbieżności.

## **Komponenty karty:**

1. **Any/All:**
   * **Opis**: Definiuje, czy warunek dotyczy dowolnych, czy wszystkich zamówień zakupu ocenianych w przepływie pracy.
   * **Opcje**:
     * **Any**: Warunek jest spełniony, jeśli którekolwiek z zamówień zakupu odpowiada określonemu warunkowi.
     * **All**: Warunek jest spełniony tylko wtedy, gdy wszystkie zamówienia zakupu spełniają określony warunek.
2. **Operator:**
   * **Opis**: Definiuje warunek, który zostanie zastosowany do porównania typu zamówienia z określoną wartością.
   * **Opcje**:
     * **Equals (=)**: Sprawdza, czy typ zamówienia odpowiada określonej wartości.
     * **Not Equals (≠)**: Zapewnia, że typ zamówienia różni się od określonej wartości.
3. **Order Type:**
   * **Opis**: Określa wartość, z którą porównywany będzie typ zamówienia w zamówieniu zakupu.
   * **Szczegóły**: Wartość musi odpowiadać typowi zamówienia lub klasyfikacji w systemie.

## **Funkcjonalność:**

* **Ocena warunku:** System ocenia typ zamówienia w zamówieniu zakupu względem określonego warunku za pomocą wybranego operatora. Jeśli typ zamówienia odpowiada (lub nie odpowiada) określonej wartości, przepływ pracy jest kontynuowany odpowiednio.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli warunek jest prawdziwy (np. typ zamówienia odpowiada określonej wartości), przepływ pracy będzie kontynuowany, możliwie wyzwalając dodatkowe akcje lub kroki przetwarzania.
  * **Warunek fałszywy**: Jeśli warunek jest fałszywy (np. typ zamówienia nie odpowiada określonej wartości), przepływ pracy nie będzie kontynuowany.

## **Konfiguracja:**

* Użytkownicy konfigurują kartę, wybierając pole typu zamówienia w zamówieniu zakupu i wybierając operator definiujący sposób porównania typu zamówienia. Następnie ustawiają określoną wartość i decydują, czy zastosować warunek do dowolnych, czy wszystkich wierszy zamówienia zakupu.

## **Przykładowy scenariusz:**

* Zamówienie zakupu ma typ zamówienia "Standard". Przepływ pracy jest skonfigurowany tak, aby sprawdzać, czy typ zamówienia to "Urgent". Przy użyciu operatora "Equals" karta porównuje typ zamówienia i stwierdza, że nie odpowiada on określonej wartości, wyzwalając przepływ pracy do wysłania zamówienia do przeglądu z powodu niezgodności.

## **Podsumowanie:**

Karta przepływu pracy "Order Type of Purchase Order" zapewnia, że zamówienia zakupu są prawidłowo sklasyfikowane zgodnie z określonym typem zamówienia. Automatyzując porównanie typów zamówień, organizacje mogą zapewnić, że zamówienia zakupu są przetwarzane zgodnie z oczekiwanymi klasyfikacjami, pomagając egzekwować zgodność i usprawnić przepływy pracy zakupowe.
