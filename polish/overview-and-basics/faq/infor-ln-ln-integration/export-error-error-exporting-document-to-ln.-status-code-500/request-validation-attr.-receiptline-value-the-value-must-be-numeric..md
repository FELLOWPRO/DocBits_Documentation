# wartość musi być numeryczna.

## **Krok 1: Zbadaj zamówienie zakupu**

**1. Sprawdź zamówienie zakupu z pulpitu nawigacyjnego**

* Jeśli status dokumentu to **Błąd eksportu**:
  1. Zlokalizuj dokument na pulpicie nawigacyjnym.
  2. Kliknij na niego, a następnie wybierz przycisk **Walidacja pól**, aby powrócić do ekranu walidacji pól.
* Jeśli status dokumentu to **Gotowy do walidacji**:
  1. Kliknij na dokument, aby przejść bezpośrednio do ekranu **Walidacji pól**.
* Jeśli dokument znajduje się w stanie **Oczekuje na zatwierdzenie**:
  1. Przejdź do **Ekranu zatwierdzania**.
  2. Obok **Pozycji faktury**, zlokalizuj **Tabelę zamówień zakupu**.
  3. Przejdź do 3. Sprawdź krok numeru dostawy.

**2. Zweryfikuj zamówienie zakupu**

1. Na ekranie **Walidacji pól**, upewnij się, że wybrano poprawne zamówienie zakupu.
2. Po potwierdzeniu poprawnego zamówienia zakupu, kliknij na zamówienie zakupu obok tabeli wydobytej, aby otworzyć widok **Tabeli zamówień zakupu**.

**3. Sprawdź numer dostawy**

* W tabeli zamówień zakupu, znajdź kolumnę **Numer dostawy**:
  * **Jeśli numer dostawy jest obecny**, przejdź do **Ekranu zatwierdzania** i ponownie sprawdź, czy jest obecny, gdy jest obecny przejdź do **Kroku 3**.
  * **Jeśli numer dostawy nie jest obecny**, wykonaj **Krok 2**, aby rozwiązać ten problem.

## Krok 2: Zweryfikuj zamówienie zakupu w LN

Przed wysłaniem zamówienia zakupu do DocBits, zweryfikuj, czy **Numer dostawy** jest poprawnie przypisany w **LN**. Sprawdź szczegóły **Zamówienia zakupu** w **LN**, aby upewnić się, że są one kompleksowe i dokładne. Jeśli **Numer dostawy** jest brakujący lub niepoprawny, może to być przyczyną błędu eksportu.

Jeśli **Zamówienie zakupu** wydaje się poprawne i zawiera niezbędne szczegóły, możesz przejść do następnego kroku.

## **Krok 3: Otwórz ustawienia DocBits**

1. Otwórz **DocBits** i przejdź do sekcji **Ustawienia**.
2. Przejdź do **Przetwarzania dokumentów**.
3. Wybierz **Eksport**.
4. W sekcji **Eksport**, kliknij na ikonę **trzech kropek** obok eksportu, który nie działa, i wybierz **Edytuj**.
5. W menu **Edycji ustawień eksportu**, kliknij **Pobierz plik mapowania LN**.

## **Krok 3: Edytuj plik mapowania LN**

1. Otwórz pobrany plik **mapowania LN**.
2. Wyszukaj pole **IRF\_ReceiptLine**.
   * Jeśli pole **IRF\_ReceiptLine** jest obecne i ustawione na **nic** (puste), zaktualizuj je na **TF\_delivery\_line**.
   * Jeśli pole **IRF\_ReceiptLine** **nie jest obecne**, dodaj je do pliku i ustaw jego wartość na **TF\_delivery\_line**.
3. Dla pola **InvoiceReceiptFields,** dodaj **ReceiptLine** do wartości.

Powinno to wyglądać następująco:

<figure><img src="../../../../.gitbook/assets/ReceiptLine.png" alt="" width="563"><figcaption></figcaption></figure>

## **Krok 4: Dodaj zaktualizowany plik z powrotem do DocBits**

1. Wróć do sekcji **Eksport** w DocBits, gdzie wcześniej pobrałeś plik **mapowania LN**.
2. Wgraj zaktualizowany plik **mapowania LN** z nowymi aktualizacjami.

## Krok 5: Spróbuj ponownie eksport

Po potwierdzeniu, że **Zamówienie zakupu** ma **Numer dostawy** i upewnieniu się, że **Plik eksportu jest poprawny**, postępuj zgodnie z poniższymi krokami, aby spróbować ponownie eksportować:

1. **Powrót do pulpitu nawigacyjnego:**
   * Wróć do pulpitu nawigacyjnego i znajdź dokument z błędem eksportu.
2. **Ponowna próba procesu eksportu:**
   * Kliknij na dokument z błędem eksportu.
   * Jeśli **Zamówienie zakupu** ma poprawny **Numer dostawy** i **Plik eksportu** jest poprawny, przejdź do ponownej próby eksportu.
3. **Sprawdź wynik eksportu:**
   * Po ponownej próbie, ponownie sprawdź proces eksportu, aby sprawdzić, czy problem został rozwiązany i dokument nie jest już oznaczony jako błąd eksportu.
   * Jeśli eksport zakończył się sukcesem, problem powinien być rozwiązany.
4. **Dalsze badania (jeśli problem nadal występuje):**
   * Jeśli problem nadal występuje po ponownej próbie eksportu, skontaktuj się z pomocą techniczną w celu dalszego zbadania możliwych problemów konfiguracyjnych lub systemowych.
