# Rozwiązywanie problemów z kontrolą dostępu i uprawnieniami

Jeśli użytkownicy napotykają nieoczekiwane ograniczenia dostępu - takie jak brakujące dokumenty, niemożność edycji pól lub odmowy działań - skorzystaj z poniższej listy kontrolnej, aby zidentyfikować i rozwiązać problem na podstawie konfiguracji uprawnień w DocBits.

### 1. Sprawdź, czy kontrola dostępu jest włączona

Ustawienia kontroli dostępu mają zastosowanie tylko wtedy, gdy funkcja jest **włączona**.

* Przejdź do: `Ustawienia` > `Przetwarzanie dokumentów` > `Moduł`.
* Upewnij się, że przełącznik **Kontroli dostępu** jest włączony.
* Jeśli jest wyłączony, wszyscy użytkownicy zazwyczaj mają nieograniczony dostęp bez względu na uprawnienia grupy lub pola.

### 2. Sprawdź przypisania grup

Upewnij się, że użytkownik jest poprawnie przypisany do odpowiednich grup:

* Przejdź do: `Ustawienia` > `Ustawienia globalne` > `Grupy, Użytkownicy i Uprawnienia`.
* Wybierz **Grupy i Uprawnienia**.
* Potwierdź, że użytkownik jest wymieniony w oczekiwanej grupie.
* Jeśli grupa korzysta z określonej kontroli dostępu, brak przypisania do grupy zablokuje dostęp do dokumentów i działań.

### 3. Przejrzyj uprawnienia dostępu grupy

Dostęp jest udzielany na podstawie typu dokumentu i działania:

* Na ekranie **Kontroli dostępu** dla grupy sprawdź typ dokumentu (np. Faktura, Zamówienie zakupu).
* Zweryfikuj uprawnienia takie jak:
  * **Lista**, **Wyświetl**, **Edytuj**, **Usuń**, **Masowa aktualizacja**
  * **Poziomy zatwierdzenia** (1., 2.), **Odblokuj dokument**
* Upewnij się, że poziom dostępu nie jest ograniczony do **Właściciela** lub **Administratora**, chyba że jest to odpowiednie.

### 4. Potwierdź uprawnienia na poziomie pól

Dostęp może być również ograniczony na poziomie **pola**, co może blokować edycję lub widoczność:

* W konfiguracji Kontroli dostępu grupy przejdź do typu dokumentu i sprawdź ustawienia na poziomie pól.
* Zweryfikuj, czy pola są ustawione na:
  * **Odczyt/Zapis**, **Tylko odczyt**, **Zapis Właściciela**, **Brak**
* Dostosuj, jeśli konieczne, w zależności od roli użytkownika.

### 5. Sprawdź ustawienie "Tylko przypisane dokumenty"

To globalne ustawienie ogranicza widoczność dokumentów:

* Przejdź do: `Ustawienia` > `Ustawienia globalne` > `Grupy, Użytkownicy i Uprawnienia`.
* Jeśli **Tylko przypisane dokumenty** są **włączone**, użytkownicy mogą widzieć tylko dokumenty przypisane bezpośrednio do nich lub ich grupy.
* Jeśli użytkownicy nie widzą oczekiwanych dokumentów:
  * Sprawdź przypisanie dokumentów.
  * Tymczasowo wyłącz ustawienie, aby sprawdzić, czy jest to główna przyczyna.

### 6. Przetestuj z znanym użytkownikiem lub grupą, które działają poprawnie

Aby zlokalizować problem:

* Zaloguj się jako użytkownik z grupy, która ma potwierdzony dostęp.
* Porównaj widoczność dokumentów i dostępne działania.
* To pomoże określić, czy problem dotyczy konkretnego użytkownika, konkretnej grupy czy całego systemu.

### 7. Ponownie sprawdź przypisanie dokumentów

Jeśli "Tylko przypisane dokumenty" są **włączone**, upewnij się, że:

* Dokument jest **przypisany** do użytkownika lub jednej z ich grup.
* Użyj kontrolek przypisania w widoku szczegółów dokumentu, aby dokonać lub przejrzeć przypisania.

### 8. Zresetuj lub ponownie skonfiguruj uprawnienia

Jeśli uprawnienia zostały niedawno zmienione lub użytkownicy zostali przeniesieni między grupami:

* Ponownie potwierdź, że ustawienia Kontroli dostępu odzwierciedlają nowe konfiguracje grup.
* Dostosuj uprawnienia pól i dokumentów, jeśli jest to konieczne.
* W razie wątpliwości utwórz grupę testową z szerokimi uprawnieniami i przetestuj zachowanie dostępu przed zastosowaniem zmian w grupach produkcyjnych.
