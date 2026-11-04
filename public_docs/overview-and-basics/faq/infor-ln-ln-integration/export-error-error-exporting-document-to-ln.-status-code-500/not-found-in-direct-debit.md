# nie znaleziono w bezpośrednim obciążeniu bezpośrednim

## **Krok 1: Sprawdź konfigurację LN**

1. Zaloguj się do **LN CE**.
2. Przejdź do menu **Opcje** i wybierz **Uruchom program**.
3. W polu wprowadź **Parametry ACP** i naciśnij Enter, aby otworzyć program.
4. Kliknij strzałkę obok pola **Aktualny zestaw**, aby rozwinąć ustawienia.
5. Przejdź do sekcji **Dopasowanie**.
   * **Sprawdź ustawienie automatycznego dopasowania:**
     * Jeśli **Automatyczne dopasowanie** jest ustawione na **Dopasuj do potwierdzenia zakupu**, przejdź do następnego kroku.
     * Jeśli nie jest ustawione na **Dopasuj do potwierdzenia zakupu**, a mimo to otrzymujesz ten błąd, skontaktuj się z nami.

## **Krok 2: Otwórz ustawienia DocBits**

Jeśli **Automatyczne dopasowanie** jest ustawione na **Dopasuj do potwierdzenia zakupu**, przejdź do następujących kroków w DocBits:

1. Otwórz **DocBits** i przejdź do sekcji **Ustawienia**.
2. Przejdź do **Przetwarzanie dokumentów**.
3. Wybierz **Eksport**.
4. W sekcji **Eksport**, kliknij ikonę **trzech kropek** obok eksportu, który nie działa, i wybierz **Edytuj**.
5. W menu **Edytuj ustawienia eksportu**, kliknij **Pobierz plik mapowania LN**.

## **Krok 3: Edytuj plik mapowania LN**

1. Otwórz pobrany plik **mapowania LN**.
2. Wyszukaj pole **IRF\_PackingSlip**.
   * Jeśli pole **IRF\_PackingSlip** istnieje i jest ustawione na **nic** (puste), zaktualizuj je na **TF\_packing\_slip**.
   * Jeśli pole **IRF\_PackingSlip** **nie istnieje**, dodaj je do pliku i ustaw jego wartość na **TF\_packing\_slip**.
3. Dla pola **InvoiceReceiptFields** dodaj **PackingSlip** do wartości.

Powinno to wyglądać następująco:

<figure><img src="../../../../.gitbook/assets/PackingSlip.png" alt=""><figcaption></figcaption></figure>

## **Krok 4: Dodaj zaktualizowany plik z powrotem do DocBits**

1. Wróć do sekcji **Eksport** w DocBits, gdzie wcześniej pobrałeś plik **mapowania LN**.
2. Prześlij zedytowany plik **mapowania LN** z nowymi aktualizacjami.

## Jeśli nadal napotykasz **Błąd eksportu dokumentu do LN** ze statusem kodu **500**, skontaktuj się z nami
