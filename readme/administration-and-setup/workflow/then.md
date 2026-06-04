---
description: Konfiguracja akcji Wtedy w przepływach pracy DocBits
---

# Then

## Przegląd kart akcji "Then..."

**1. Akcje Document Field:**

* **Invert Checkbox:** Ta akcja przełącza stan pola wyboru w dokumencie.
* **Set Checkbox:** Ustawia stan pola wyboru na true (zaznaczone) lub false (niezaznaczone).
* **Set Field to Text:** Ta akcja ustawia określone pole dokumentu na podaną wartość tekstową.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

**2. Akcje Document:**

* **Approve the Document:** Oznacza dokument jako zatwierdzony w systemie.
* **Start Export:** Inicjuje proces eksportu dokumentu.
* **Reject the Document:** Oznacza dokument jako odrzucony.

<figure><img src="../../../.gitbook/assets/then2.png" alt=""><figcaption></figcaption></figure>

**3. Akcje Status:**

* **Change Status:** Zmienia status dokumentu lub zadania na określony nowy status.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

**4. Akcje Task:**

* Przypisania i powiadomienia:
  * **Assign Task:** Tworzy i przypisuje zadanie z określonymi szczegółami do osoby lub grupy, z opcjami powiadomienia ich za pośrednictwem wiadomości e-mail.
  * **Create a New Task:** Podobne do przypisania, ale skupione na utworzeniu całkowicie nowego zadania w systemie.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

**5. Akcje Table:**

* **Calculate in Table:** Wykonuje obliczenia na danych tabeli na podstawie określonych warunków i zapisuje wyniki w wyznaczonej kolumnie.
* **Change Entries:** Aktualizuje wpisy w tabeli na podstawie określonych warunków.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

**6. Akcje Assignee:**

* **Assign User from Field:** Przypisuje użytkownika do zadania lub dokumentu na podstawie danych użytkownika przechowywanych w określonym polu, z opcją użytkownika zapasowego, jeśli podstawowy jest niedostępny.
* **Assign Document to User or Group:** Bezpośrednio przypisuje dokument do użytkownika lub grupy, zapewniając właściwe wyznaczenie odpowiedzialności.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

**7. Akcje interakcji zewnętrznych:**

* **Call API:** Wysyła żądanie do zewnętrznego API, które można dostosować za pomocą określonych metod, parametrów i danych.
* **Send HTTPS Request:** Podobne do wywołań API, ale specjalnie sformatowane dla protokołów HTTPS.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

**8. Zaawansowane przetwarzanie:**

* **Run Workflow:** Uruchamia inny przepływ pracy w systemie, umożliwiając łączenie złożonych procesów.

#### Zastosowanie praktyczne

Te karty akcji służą do automatyzacji reakcji na podstawie określonych wyzwalaczy zidentyfikowanych we wcześniejszych częściach konfiguracji przepływu pracy. Na przykład:

* Jeśli dokument zostanie zidentyfikowany jako wymagający przeglądu, akcja "Approve the Document" może zostać automatycznie wyzwolona, gdy przejdzie wszystkie określone warunki.
* W przypadku zadań zarządzania danymi akcje "Set Checkbox" lub "Set Field to Text" zapewniają automatyczną aktualizację pól dokumentu, redukując ręczne wprowadzanie danych i potencjalne błędy.
* Złożone zadania, takie jak interakcje z API lub zmiany statusu, usprawniają interakcje nie tylko w systemie ERP, ale także z usługami i narzędziami zewnętrznymi, zwiększając integrację i funkcjonalność.

#### Podsumowanie

Sekcja "Then..." w Twoim systemie przepływu pracy zapewnia solidne narzędzia do definiowania precyzyjnych akcji, które powinny nastąpić w wyniku spełnienia warunków w przepływie pracy. Dzięki efektywnemu wykorzystaniu tych akcji firmy mogą automatyzować rutynowe procesy, zapewniać dokładność danych i dynamicznie reagować na zmieniające się informacje i stany systemu. Zrozumienie, jak konfigurować i wykorzystywać te akcje, jest kluczem do maksymalizacji wydajności i skuteczności możliwości przepływu pracy Twojego systemu ERP.
