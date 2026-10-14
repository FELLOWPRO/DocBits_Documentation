# Send Email to Groups

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

## Cel
Ta karta automatycznie wysyła powiadomienia e-mail do grup użytkowników. Zamiast przypisywać pracę pojedynczym osobom, wysyłasz wiadomość do grupy, a wszyscy członkowie tej grupy ją otrzymują.

**Rzeczywisty przykład:** Gdy przybywa faktura o wysokiej wartości, automatycznie wyślij powiadomienie e-mail do wszystkich w grupie "Finance Team", aby byli świadomi, że wymaga ona przeglądu.

---

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:
- Powiadomić wiele osób jednocześnie
- Wysyłać alerty do grup zespołów
- Rozsyłać aktualizacje do działów
- Powiadamiać grupy o zmianach statusu dokumentu
- Wysyłać przypomnienia członkom grupy

**Typowe scenariusze:**
- Powiadamianie zespołu zakupowego o nowych dostawcach
- Alarmowanie zespołu finansowego o fakturach o wysokiej wartości
- Powiadamianie zespołu magazynowego o wysyłkach
- Rozsyłanie zmian statusu dokumentu

---

## Jak to działa

1. **Sprawdzenie warunku**: Przepływ pracy sprawdza warunki "Where" i "And"
2. **Przygotowanie e-maila**: System przygotowuje wiadomość e-mail przy użyciu szablonu
3. **Pobranie członków grupy**: System znajduje wszystkich członków określonej grupy
4. **Wysłanie**: Wiadomość e-mail jest wysyłana do każdego członka grupy
5. **Rejestracja**: Wysłanie wiadomości e-mail jest rejestrowane

---

## Wyjaśnienie parametrów

### Email Template
Wiadomość e-mail do wysłania

**Opcje:**
- Wybierz spośród istniejących szablonów
- Każdy szablon ma wstępnie zdefiniowany temat, treść i formatowanie
- Szablony mogą zawierać symbole zastępcze takie jak {document_number}, {supplier_name}

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

### Group
Grupa użytkowników, do której zostanie wysłana wiadomość e-mail

**Przykładowe grupy:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Kroki konfiguracji

### Krok 1: Wybierz szablon e-mail
1. Kliknij "Select Email Template"
2. Wybierz szablon z listy
3. Zweryfikuj temat i treść

### Krok 2: Wybierz grupę
1. Kliknij "Select Group"
2. Wybierz grupę, którą chcesz powiadomić
3. Zweryfikuj członków grupy (zwykle pokazuje liczbę)

### Krok 3: Ustaw warunki
1. Dodaj warunek: "When [condition] is true"
2. Przykład: "When invoice amount is greater than €5000"

### Krok 4: Przetestuj
1. Przetestuj z przykładowym dokumentem
2. Zweryfikuj, czy wiadomość e-mail jest wysyłana do grupy
3. Sprawdź renderowanie szablonu

---

## Przykłady szablonów e-mail

### Szablon 1: Alert o fakturze o wysokiej wartości
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

---

## Typowe przypadki użycia

### Przypadek użycia 1: Alerty kontroli jakości
**Wyzwalacz:** Gdy znaleziono rozbieżność między fakturą a PO

**Grupa e-mail:** Quality Team

**Treść:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Przypadek użycia 2: Powiadomienia o zatwierdzeniu
**Wyzwalacz:** Gdy dokument osiąga określony status

**Grupa e-mail:** Approval Committee

**Treść:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Przypadek użycia 3: Powiadomienia o wyjątkach
**Wyzwalacz:** Gdy warunki nie są spełnione

**Grupa e-mail:** Managers

**Treść:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Przypadek użycia 4: Aktualizacje statusu
**Wyzwalacz:** Gdy zmienia się status dokumentu

**Grupa e-mail:** Zespół odpowiedzialny za następny krok

**Treść:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Rozwiązywanie problemów

### "Email not received"

**Możliwe przyczyny:**
- [ ] Użytkownicy w grupie nie mają adresów e-mail
- [ ] Wiadomość e-mail zablokowana przez filtr spamu
- [ ] Adres e-mail jest nieprawidłowy w grupie
- [ ] Grupa nie ma członków

**Rozwiązania:**
1. Zweryfikuj, czy wszyscy członkowie grupy mają adresy e-mail
2. Sprawdź folder spamu/wiadomości-śmieci
3. Zweryfikuj, czy członkostwo w grupie jest poprawne
4. Dodaj użytkowników do grupy, jeśli ich brakuje
5. Sprawdź z działem IT, czy usługa e-mail działa

### "Template not rendering correctly"

**Przyczyna:** Nie znaleziono zmiennych symboli zastępczych

**Rozwiązanie:**
- [ ] Zweryfikuj, czy nazwy pól są dokładnie zgodne
- [ ] Sprawdź, czy pole ma wartość w dokumencie
- [ ] Użyj poprawnego formatu symbolu zastępczego: {field_name}
- [ ] Przetestuj z przykładowym dokumentem zawierającym wszystkie pola

### "Some people getting email, others not"

**Przyczyna:** Niekompletne członkostwo w grupie lub nieprawidłowe adresy e-mail

**Rozwiązania:**
- [ ] Zweryfikuj, czy wszyscy członkowie mają prawidłowy e-mail
- [ ] Sprawdź, czy niektórzy użytkownicy zrezygnowali
- [ ] Zweryfikuj, czy członkostwo w grupie jest aktualne
- [ ] Skontaktuj się z działem IT w celu walidacji adresów e-mail

### "Want to add/remove people from group"

**Rozwiązanie:**
- Skontaktuj się ze swoim administratorem
- Grupy są zarządzane w ustawieniach systemu
- Nie można ich zmienić z tej karty
- Poproś o zmiany w członkostwie grupy w dziale IT

---

## Dostosowywanie szablonu e-mail

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
Jeśli potrzebujesz dodatkowych danych w wiadomościach e-mail:
1. Skontaktuj się ze swoim administratorem
2. Poproś o nowy symbol zastępczy
3. Dodaj niezbędne pole do dokumentu
4. Zaktualizuj szablon e-mail

---

## Najlepsze praktyki

✅ **Rób:**
- Utrzymuj treść wiadomości e-mail zwięzłą i jasną
- Uwzględnij elementy do działania (co powinni zrobić odbiorcy?)
- Dołącz łącze lub instrukcje dostępu do dokumentu
- Przetestuj szablon z przykładowymi danymi
- Wysyłaj do właściwej grupy (nie powiadamiaj nadmiernie)
- Używaj szablonów dla spójności

❌ **Nie rób:**
- Nie wysyłaj zbyt wielu wiadomości e-mail (zmęczenie powiadomieniami)
- Nie dołączaj danych wrażliwych w wiadomościach e-mail
- Nie wysyłaj do grup, które nie potrzebują informacji
- Nie używaj niejasnych tematów
- Nie zapominaj dołączyć informacji, jak podjąć działanie
- Nie wysyłaj wiadomości e-mail do osób indywidualnych (zamiast tego użyj grupy)

---

## Uwagi dotyczące wydajności

- Każda wiadomość e-mail trwa ~1 sekundę na wysłanie
- Duże grupy mogą zająć czas (100 osób = ~100 sekund)
- Nie twórz pętli wysyłających tysiące wiadomości e-mail
- Monitoruj pojemność usługi e-mail
- Rozważ grupowanie w razie wielu dokumentów

---

## Powiązane karty

- **ACTION_SEND_EMAIL** - Wyślij do osoby indywidualnej
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Przypisz zadanie zamiast tylko powiadamiać
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Utwórz zadanie i powiadom
- **STAUS_CHANGE** - Zmień status i powiadom

---

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

---

## Często zadawane pytania

**P: Czy mogę wysyłać do wielu grup?**
O: Utwórz oddzielne karty dla każdej grupy

**P: Co się stanie, jeśli czyjaś wiadomość e-mail zostanie odbita?**
O: Wiadomość e-mail jest rejestrowana jako nieudana, dział IT może rozwiązać problem

**P: Czy mogę zmienić szablon e-mail?**
O: Skontaktuj się ze swoim administratorem, aby zmodyfikować szablony

**P: Czy mogę wysyłać na podstawie warunków?**
O: Tak! Użyj warunków "Where" i "And", aby kontrolować, kiedy wysyłane są wiadomości e-mail

**P: Skąd mam wiedzieć, czy wiadomość e-mail została odebrana?**
O: Sprawdź dzienniki e-mail w DocBits, aby uzyskać status wysyłania
