# Następnie

## Przegląd kart akcji "Następnie..."

### **1. Akcje pola dokumentu:**

* **Odwróć pole wyboru:** Ta akcja przełącza stan pola wyboru w dokumencie.
* **Ustaw pole wyboru:** Ustawia stan pola wyboru na true (zaznaczone) lub false (niezaznaczone).
* **Ustaw pole na tekst:** Ta akcja ustawia określone pole dokumentu na określoną wartość tekstową.

<figure><img src="../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Akcje dokumentu:**

* **Zatwierdź dokument:** Oznacza dokument jako zatwierdzony w systemie.
* **Rozpocznij eksport:** Rozpoczyna proces eksportu dokumentu.
* **Odrzuć dokument:** Oznacza dokument jako odrzucony.

<figure><img src="../../.gitbook/assets/then2.png" alt=""><figcaption></figcaption></figure>

### **3. Akcje statusu:**

* **Zmień status:** Zmienia status dokumentu lub zadania na określony nowy status.

<figure><img src="../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **4. Akcje zadania:**

* Przypisania i powiadomienia:
* **Przypisz zadanie:** Tworzy i przypisuje zadanie z określonymi szczegółami osobie lub grupie, z opcjami powiadomienia ich za pomocą e-maila.
* **Utwórz nowe zadanie:** Podobne do przypisania, ale skupione na utworzeniu całkowicie nowego zadania w systemie.

<figure><img src="../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **5. Akcje tabeli:**

* **Oblicz w tabeli:** Wykonuje obliczenia na danych tabeli na podstawie określonych warunków i przechowuje wyniki w wyznaczonej kolumnie.
* **Zmień wpisy:** Aktualizuje wpisy w tabeli na podstawie określonych warunków.

<figure><img src="../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **6. Akcje przypisania:**

* **Przypisz użytkownika z pola:** Przypisuje użytkownika do zadania lub dokumentu na podstawie danych użytkownika przechowywanych w określonym polu, z opcją wyboru użytkownika zastępczego, jeśli podstawowy jest niedostępny.
* **Przypisz dokument do użytkownika lub grupy:** Bezpośrednio przypisuje dokument do użytkownika lub grupy, zapewniając odpowiednie przypisanie odpowiedzialności.

<figure><img src="../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **7. Akcje interakcji zewnętrznej:**

* **Wywołaj API:** Wysyła żądanie do zewnętrznego interfejsu API, który może być dostosowany za pomocą określonych metod, parametrów i danych.
* **Wyślij żądanie HTTPS:** Podobne do wywołań API, ale specjalnie sformatowane dla protokołów HTTPS.

<figure><img src="../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **8. Zaawansowane przetwarzanie:**

* **Uruchom proces:** Wywołuje inny proces w systemie, umożliwiając złożone łańcuchy procesów.

#### Zastosowanie praktyczne

Te karty akcji służą do automatyzacji odpowiedzi na podstawie określonych wyzwalaczy zidentyfikowanych we wcześniejszych częściach konfiguracji procesu. Na przykład:

* Jeśli dokument wymaga przeglądu, akcja "Zatwierdź dokument" może zostać automatycznie uruchomiona, gdy spełni wszystkie określone warunki.
* W zadaniach związanych z zarządzaniem danymi akcje "Ustaw pole wyboru" lub "Ustaw pole na tekst" zapewniają automatyczne aktualizowanie pól dokumentu, zmniejszając ręczne wprowadzanie danych i potencjalne błędy.
* Zadania złożone, takie jak interakcje z API lub zmiany statusu, usprawniają interakcje nie tylko w systemie ERP, ale także z zewnętrznymi usługami i narzędziami, zwiększając integrację i funkcjonalność.

### Podsumowanie

Sekcja "Następnie..." w systemie workflow dostarcza solidnych narzędzi do definiowania precyzyjnych działań, które powinny wystąpić w wyniku spełnienia warunków w procesie. Poprzez efektywne wykorzystanie tych działań firmy mogą automatyzować rutynowe procesy, zapewnić dokładność danych i dynamicznie reagować na zmieniające się informacje i stany systemu. Zrozumienie konfiguracji i wykorzystania tych działań jest kluczem do maksymalizacji efektywności i skuteczności możliwości workflow systemu ERP.
