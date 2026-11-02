# Weryfikacja ustawienia spółki logistycznej w przypadku rozbieżności przyjęć towaru

W dużych procesach zakupowych nierzadko zdarza się, że niektóre dane nie zgadzają się zgodnie z oczekiwaniami. Można na przykład zobaczyć komunikat o błędzie, taki jak:

**„Dowód dostawy L1234, Typ zamówienia: Zakup, Zamówienie 100000211, Pozycja 10, Kolejny numer 1, Firma logistyczna**<mark style="color:red;">**XXXX**</mark>**, Towary W poleceniu zapłaty nie znaleziono paragonu WE0000293 i pozycji wpisu 10.”**

Ten typ komunikatu często wskazuje na niezgodność lub brakujące informacje związane z konfiguracją spółki logistycznej. Spółka logistyczna jest kluczowym elementem systemów planowania zasobów przedsiębiorstwa (ERP), zwłaszcza w złożonych łańcuchach dostaw obejmujących wiele podmiotów prawnych lub logistycznych.

**Dlaczego tak się dzieje?**

W środowiskach wielopodmiotowych każda transakcja - zakup, przyjęcie towaru czy inicjowanie płatności - musi być prawidłowo przypisana do właściwej spółki logistycznej. „Spółka logistyczna” to coś więcej niż identyfikator; określa, który magazyn, centrum dystrybucyjne lub węzeł sieci dostaw odpowiada za zamówienie i zadania realizacyjne. Jeśli numer spółki nie zgadza się z oczekiwanym podmiotem, procesy następcze, takie jak weryfikacja przyjęcia towaru lub rozliczenia polecenia zapłaty, mogą się nie powieść.

## **Kluczowe kontrole do wykonania:**

### 1. Zweryfikuj przypisaną spółkę logistyczną:

Sprawdź rekordy danych podstawowych, aby upewnić się, że wskazana spółka logistyczna (w tym przypadku <mark style="color:red;">XXXX</mark>) jest właściwym podmiotem dla danego zamówienia. Czy <mark style="color:red;">XXXX</mark> jest właściwym kodem spółki do obsługi zakupów od tego dostawcy lub dla tej konkretnej linii produktów?

### 2. Przejrzyj konfigurację zamówienia zakupu (PO):

Potwierdź, że spółka logistyczna zamówienia zakupu odpowiada zamierzonemu miejscu odbioru. Czasami zamówienie jest tworzone w jednej spółce logistycznej, a towar jest przyjmowany w innej, jeśli konfiguracja nie jest spójna.

### 3. Porównaj przyjęcie towaru z zapisami magazynowymi:

Sprawdź przyjęcie towaru (WE0000293) i upewnij się, że zostało zaksięgowane w magazynie właściwej spółki. Jeśli magazyn należy do innej spółki logistycznej, może być konieczne poprawienie konfiguracji lub wykonanie przeniesienia do właściwego podmiotu.

### 4. Sprawdź spójność integracji i danych podstawowych:

Punkty integracji między różnymi modułami (Zakupy, Magazyn, Finanse) opierają się na spójnych kodach. Upewnij się, że spółka logistyczna jest zdefiniowana jednolicie we wszystkich istotnych modułach.

### 5. Skorzystaj z dokumentacji i wsparcia:

Jeśli wewnętrzne kontrole nie rozwiążą problemu, skorzystaj z dokumentacji systemu lub skontaktuj się z zespołem wsparcia ERP. Może on pomóc sprawdzić, czy kod spółki logistycznej jest poprawnie skonfigurowany lub czy potrzebne są dodatkowe kroki konfiguracyjne.
