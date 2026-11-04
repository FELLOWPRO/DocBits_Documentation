# Wyślij e-mail do grup

***

Dodaj tę kartę do grupy **Wtedy** Kreatora przepływu pracy — akcje, które zostaną uruchomione po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

## 📌 Informacje o wersji

**Stan:** ✅ Pojedyncza wersja (bez istotnych zmian) **Najnowsza wersja:** v1 (aktywna) **Uwaga:** Ta karta wykorzystuje model pojedynczej wersji z obsługą wielu języków za pomocą kluczy tłumaczeniowych.

📖 [Kompletna baza danych kart](../../cards-overview/export-cards-guide.md)

***

## Cel

Ta karta automatycznie wysyła powiadomienia e-mail do grup użytkowników. Zamiast przydzielać pracę poszczególnym osobom, wysyłasz wiadomość do grupy i wszyscy członkowie tej grupy ją odbierają.

**Przykład z życia wziętego:** Gdy otrzymana zostanie faktura o dużej wartości, automatycznie wyślij powiadomienie e-mailem do wszystkich osób w grupie „Zespół finansowy”, aby wiedzieli, że faktura wymaga sprawdzenia.

***

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:

* Powiadom wiele osób jednocześnie
* Wysyłaj alerty do grup zespołów
* Przesyłaj aktualizacje do działów
* Powiadamiaj grupy o zmianach statusu dokumentu
* Wysyłaj przypomnienia członkom grupy

**Typowe scenariusze:**

* Powiadom zespół ds. zakupów o nowych dostawcach
* Powiadom zespół finansowy o fakturach o dużej wartości
* Powiadom zespół magazynowy o wysyłkach
* Zmiany statusu dokumentu rozgłaszanego

***

## Jak to działa

1. **Kontrola stanu**: Przebieg pracy sprawdza warunki „Kiedy” i „I”
2. **Przygotuj wiadomość e-mail**: System przygotowuje wiadomość e-mail przy użyciu szablonu
3. **Pobierz członków grupy**: System znajduje wszystkich członków określonej grupy
4. **Wyślij**: Wiadomość e-mail jest wysyłana do każdego członka grupy
5. **Log**: Wysyłanie wiadomości e-mail jest rejestrowane

***

## Parametry wyjaśnione

### Szablon e-maila

Wiadomość e-mail, która ma zostać wysłana

**Opcje:**

* Wybierz jeden z istniejących szablonów
* Każdy szablon ma predefiniowany temat, treść i formatowanie
* Szablony mogą zawierać elementy zastępcze, takie jak {document\_number}, {supplier\_name}

**Przykładowy szablon:**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Grupa

Grupa użytkowników, do której ma zostać wysłana wiadomość e-mail

**Przykładowe grupy:**

* Zespół Finansów
* Zespół ds. zakupów
* Zespół Magazynowy
* Komitet zatwierdzający
* Grupa Zarządzająca

***

## Kroki konfiguracji

### Krok 1: Wybierz szablon wiadomości e-mail

1. Kliknij „Wybierz szablon wiadomości e-mail”
2. Wybierz szablon z listy
3. Sprawdź temat i treść

### Krok 2: Wybierz Grupę

1. Kliknij „Wybierz grupę”
2. Wybierz grupę, którą chcesz powiadomić
3. Zweryfikuj członków grupy (zwykle pokazuje liczbę)

### Krok 3: Ustaw warunki

1. Dodaj warunek: „Kiedy \[warunek] jest prawdziwy”
2. Przykład: „Kiedy kwota faktury przekracza 5000 EUR”

### Krok 4: Przetestuj

1. Przetestuj na przykładowym dokumencie
2. Sprawdź, czy e-maile są wysyłane do grupy
3. Sprawdź renderowanie szablonu

***

## Przykłady szablonów e-maili

### Szablon 1: Powiadomienie o fakturze o wysokiej wartości

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Szablon 2: Zmiana statusu dostawcy

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Szablon 3: Dokument gotowy do eksportu

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## Typowe przypadki użycia

### Przypadek użycia 1: Alerty kontroli jakości

**Wyzwalacz:** W przypadku wykrycia rozbieżności między fakturą a zamówieniem

**Grupa e-mailowa:** Zespół ds. jakości

**Treść:**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Przypadek użycia 2: Powiadomienia o zatwierdzeniu

**Wyzwalacz:** Gdy dokument osiągnie określony status

**Grupa e-mailowa:** Komitet zatwierdzający

**Treść:**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Przypadek użycia 3: Powiadomienia o wyjątkach

**Wyzwalacz:** Gdy warunki nie są spełnione

**Grupa e-mailowa:** Menedżerowie

**Treść:**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Przypadek użycia 4: Aktualizacje statusu

**Wyzwalacz:** Kiedy zmienia się status dokumentu

**Grupa e-mailowa:** Zespół odpowiedzialny za następny krok

**Treść:**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## Rozwiązywanie problemów

### „Nie otrzymano e-maila”

**Możliwe przyczyny:**

* [ ] Użytkownicy w grupie nie mają adresów e-mail
* [ ] E-mail zablokowany przez filtr spamu
* [ ] Adres e-mail w grupie jest nieprawidłowy
* [ ] Grupa nie ma członków

**Rozwiązania:**

1. Sprawdź, czy wszyscy członkowie grupy mają adresy e-mail
2. Sprawdź folder spam/śmieci
3. Sprawdź, czy członkostwo w grupie jest prawidłowe
4. Dodaj użytkowników do grupy, jeśli ich brakuje
5. Sprawdź w dziale IT, czy usługa e-mail działa

### „Szablon nie renderuje się poprawnie”

**Przyczyna:** Nie znaleziono zmiennych zastępczych

**Rozwiązanie:**

* [ ] Sprawdź, czy nazwy pól są dokładnie zgodne
* [ ] Sprawdź, czy pole ma wartość w dokumencie
* [ ] Użyj prawidłowego formatu symbolu zastępczego: {field\_name}
* [ ] Przetestuj na przykładowym dokumencie zawierającym wszystkie pola

### „Niektórzy ludzie otrzymują e-maile, inni nie”

**Przyczyna:** Niekompletne członkostwo w grupie lub nieprawidłowe adresy e-mail

**Rozwiązania:**

* [ ] Sprawdź, czy wszyscy członkowie mają ważny adres e-mail
* [ ] Sprawdź, czy niektórzy użytkownicy zrezygnowali
* [ ] Sprawdź, czy członkostwo w grupie jest aktualne
* [ ] Skontaktuj się z działem IT, aby zweryfikować adresy e-mail

### „Chcę dodać/usunąć osoby z grupy”

**Rozwiązanie:**

* Skontaktuj się ze swoim administratorem
* Zarządzanie grupami odbywa się w ustawieniach systemu
* Nie można zmienić tej karty
* Poproś o zmiany w członkostwie grupy w IT

***

## Dostosowywanie szablonu wiadomości e-mail

### Dostępne symbole zastępcze

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Tworzenie niestandardowych symboli zastępczych

Jeżeli potrzebujesz dodatkowych danych w mailach:

1. Skontaktuj się ze swoim administratorem
2. Poproś o nowy symbol zastępczy
3. Dodaj niezbędne pole do dokumentu
4. Zaktualizuj szablon wiadomości e-mail

***

## Najlepsze praktyki

✅ **Wykonaj:**

* Treść wiadomości e-mail powinna być krótka i jasna
* Uwzględnij elementy działania (co powinni zrobić odbiorcy?)
* Dołącz link lub instrukcje umożliwiające dostęp do dokumentu
* Szablon testowy z przykładowymi danymi
* Wyślij do właściwej grupy (nie powiadamiaj nadmiernie)
* Aby zachować spójność, użyj szablonów

❌ **Nie:**

* Wysyłaj zbyt wiele e-maili (zmęczenie powiadomieniami)
* Dołącz wrażliwe dane do wiadomości e-mail
* Wyślij do grup, które nie potrzebują informacji
* Używaj niejasnych tematów
* Zapomnij o podaniu sposobu podjęcia działań
* Wysyłaj e-maile do poszczególnych osób (zamiast tego użyj grupy)

***

## Uwagi dotyczące wydajności

* Wysłanie każdego e-maila trwa \~ 1 sekundę
* Duże grupy mogą zająć trochę czasu (100 osób = \~100 sekund)
* Nie twórz pętli, które wysyłają tysiące e-maili
* Monitoruj wydajność usług e-mail
* W przypadku wielu dokumentów należy rozważyć połączenie wsadowe

***

## Powiązane karty

* **ACTION\_SEND\_EMAIL** - Wyślij do konkretnej osoby
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** – Przypisz zadanie zamiast po prostu powiadamiać
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - Utwórz zadanie i powiadom
* **STAUS\_CHANGE** – Zmień status i powiadom

***

## Typowy przykład przepływu pracy

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## Często zadawane pytania

**P: Czy mogę wysyłać do wielu grup?** O: Utwórz osobne karty dla każdej grupy

**Q: Co się stanie, jeśli czyjś e-mail zostanie odesłany?** O: E-mail zostanie zarejestrowany jako nieudany, dział IT może rozwiązać problem

**Q: Czy mogę zmienić szablon wiadomości e-mail?** O: Skontaktuj się z administratorem, aby zmodyfikować szablony

**Q: Czy mogę wysłać na określonych warunkach?** O: Tak! Użyj warunków „Kiedy” i „I”, aby kontrolować, kiedy wysyłane są e-maile

**Q: Skąd mam wiedzieć, czy e-mail został odebrany?** O: Sprawdź dzienniki e-maili w DocBits pod kątem statusu wysyłania
