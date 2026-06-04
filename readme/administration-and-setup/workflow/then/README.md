# Then

## Przegląd kart akcji "Then..."

### **1. Akcje Document Field:**

* **Invert Checkbox:** Ta akcja przełącza stan pola wyboru w dokumencie.
* **Set Checkbox:** Ustawia stan pola wyboru na true (zaznaczone) lub false (niezaznaczone).
* **Set Field to Text:** Ta akcja ustawia określone pole dokumentu na podaną wartość tekstową.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Akcje Document:**

* **Approve the Document:** Oznacza dokument jako zatwierdzony w systemie.
* **Reject the Document:** Oznacza dokument jako odrzucony.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Akcje Export:**

* **Export document with export configuration:** Uruchamia proces eksportu z określoną konfiguracją eksportu.
* **Start Export:** Uruchamia proces eksportu.



<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Akcje Status:**



* **Change Status:** Zmienia status dokumentu lub zadania na określony nowy status.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Akcje Task:**

* Przypisania i powiadomienia:
  * **Assign Task:** Tworzy i przypisuje zadanie z określonymi szczegółami do osoby lub grupy, z opcjami powiadomienia ich za pośrednictwem wiadomości e-mail.
  * **Create a New Task:** Podobne do przypisywania, ale skupione na utworzeniu całkowicie nowego zadania w systemie.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Akcje Table:**

* **Calculate in Table:** Wykonuje obliczenia na danych tabelarycznych na podstawie określonych warunków i zapisuje wyniki w wyznaczonej kolumnie.
* **Change Entries:** Aktualizuje wpisy w tabeli na podstawie określonych warunków.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Akcje Assignee:**

* **Assign User from Field:** Przypisuje użytkownika do zadania lub dokumentu na podstawie danych użytkownika zapisanych w określonym polu, z opcją użytkownika zapasowego, jeśli podstawowy jest niedostępny.
* **Assign Document to User or Group:** Bezpośrednio przypisuje dokument do użytkownika lub grupy, zapewniając właściwe przypisanie odpowiedzialności.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Akcje interakcji zewnętrznych:**

* **Call API:** Wysyła żądanie do zewnętrznego API, które można dostosować za pomocą określonych metod, parametrów i danych.
* **Send HTTPS Request:** Podobne do wywołań API, ale specjalnie sformatowane dla protokołów HTTPS.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Przetwarzanie zaawansowane:**

* **Run Workflow:** Wyzwala inny przepływ pracy w systemie, umożliwiając łączenie złożonych procesów.

#### Praktyczne zastosowanie

Te karty akcji służą do automatyzacji reakcji na podstawie określonych wyzwalaczy zidentyfikowanych we wcześniejszych częściach konfiguracji przepływu pracy. Na przykład:

* Jeśli dokument zostanie zidentyfikowany jako wymagający przeglądu, akcja "Approve the Document" może zostać automatycznie wyzwolona po spełnieniu wszystkich określonych warunków.
* W przypadku zadań zarządzania danymi akcje "Set Checkbox" lub "Set Field to Text" zapewniają automatyczną aktualizację pól dokumentu, redukując ręczne wprowadzanie danych i ryzyko błędów.
* Złożone zadania, takie jak interakcje z API czy zmiany statusu, usprawniają interakcje nie tylko w ramach systemu ERP, ale także z usługami i narzędziami zewnętrznymi, zwiększając integrację i funkcjonalność.

### Podsumowanie

Sekcja "Then..." w systemie przepływu pracy zapewnia rozbudowane narzędzia do definiowania precyzyjnych akcji, które powinny nastąpić w wyniku spełnienia warunków w przepływie pracy. Dzięki skutecznemu wykorzystaniu tych akcji firmy mogą automatyzować rutynowe procesy, zapewniać dokładność danych i dynamicznie reagować na zmieniające się informacje oraz stany systemu. Zrozumienie, jak konfigurować i wykorzystywać te akcje, jest kluczem do maksymalizacji wydajności i skuteczności możliwości przepływu pracy systemu ERP.
