# Send HTTPS Request

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

## Cel
Ta karta wysyła bezpieczną wiadomość do witryny lub usługi i może otrzymać odpowiedź zwrotną. Jest prostsza niż karta "Call API" i jest przydatna do szybkich integracji.

**Rzeczywisty przykład:** Wyślij dane faktury do swojego systemu księgowego lub zapytaj system zewnętrzny, czy pracownik jest upoważniony do przetworzenia tego zakupu.

---

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:
- Wysyłać powiadomienia webhook do usług zewnętrznych
- Wyzwalać akcje w innych systemach
- Odpytywać prostą usługę internetową
- Wysyłać aktualizacje statusu do innych aplikacji
- Wykonywać proste integracje bez złożonych wymagań API

---

## Jak to działa

1. **Sprawdzenie wyzwalacza**: System sprawdza, czy warunki "Where" i "And" są spełnione
2. **Budowanie żądania**: System przygotowuje żądanie HTTPS z Twoimi parametrami
3. **Bezpieczne wysłanie**: Dane są wysyłane przy użyciu bezpiecznego połączenia HTTPS
4. **Odbiór odpowiedzi**: Usługa zewnętrzna odpowiada
5. **Kontynuacja**: Przepływ pracy postępuje z danymi odpowiedzi

---

## Parametry

### URL
Adres witryny, do której zostanie wysłane żądanie

**Przykład:** `https://webhook.company.com/process`

### Headers
Specjalne instrukcje dla odbiorcy

**Przykład:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Method
- **GET**: Żądanie informacji
- **POST**: Wysłanie danych
- **PUT**: Aktualizacja danych

### Parameters (Query String)
Dane dodane do adresu URL

**Przykład:** `?action=approve&user_id=123`

### Request Data
Faktyczne wysyłane informacje (w formacie JSON)

**Przykład:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Przykład krok po kroku

### Scenariusz: Wysłanie faktury do systemu księgowego

**Konfiguracja karty:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Method:** POST
- **Headers:** `Authorization: Bearer YOUR-TOKEN`
- **Request Data:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Oczekiwana odpowiedź:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Typowe przypadki użycia

### 1. Powiadomienia webhook
Wysyłaj powiadomienia w czasie rzeczywistym do innych systemów za każdym razem, gdy coś dzieje się w DocFlow

**Przykład:**
- Dokument zatwierdzony → Wyślij powiadomienie do systemu realizacji
- Dostawca zmieniony → Powiadom zespół zakupowy przez webhook Slack/Teams

### 2. Integracja z systemem zewnętrznym
Połącz DocFlow z innymi systemami biznesowymi w celu automatycznej wymiany danych

**Przykład:**
- Po przetworzeniu dokumentu → Synchronizuj z systemem ERP
- Dodano nowego dostawcę → Utwórz rekord dostawcy w systemie danych podstawowych

### 3. Przepływy zatwierdzania
Wyślij dokument do zewnętrznego systemu zatwierdzania i otrzymaj decyzję

**Przykład:**
- Faktura o wysokiej wartości → Wyślij do działu finansów do zatwierdzenia
- Zwróć dokument do systemu zewnętrznego z decyzją

---

## Przewodnik konfiguracji

### Krok 1: Uzyskaj informacje o punkcie końcowym
Zapytaj system odbierający o:
- [ ] URL HTTPS
- [ ] Wymagane nagłówki
- [ ] Metoda uwierzytelniania
- [ ] Oczekiwany format żądania
- [ ] Oczekiwany format odpowiedzi

### Krok 2: Skonfiguruj kartę
1. Wprowadź URL HTTPS
2. Ustaw metodę HTTP (zwykle POST)
3. Dodaj uwierzytelnianie, jeśli wymagane
4. Sformatuj dane żądania jako JSON
5. Dodaj wszelkie niestandardowe nagłówki

### Krok 3: Przetestuj
Wyślij żądanie testowe i zweryfikuj odpowiedź

---

## Obsługa odpowiedzi

Twoje żądanie HTTPS otrzyma odpowiedź. Typowe odpowiedzi:

### Sukces (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Błędne żądanie (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Nieautoryzowane (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Błąd serwera (500)
System odbierający ma wewnętrzny problem

---

## Rozwiązywanie problemów

### "Certificate Error"
**Przyczyna:** Problem z certyfikatem bezpieczeństwa HTTPS

**Rozwiązanie:**
- Zweryfikuj, czy adres URL jest poprawny
- Sprawdź, czy certyfikat witryny jest ważny
- Upewnij się, że używasz HTTPS (nie HTTP)

### "Connection Refused"
**Przyczyna:** Nie można połączyć się z serwerem

**Rozwiązanie:**
- Zweryfikuj, czy adres URL/IP jest poprawny
- Sprawdź, czy usługa jest uruchomiona
- Sprawdź reguły zapory
- Zweryfikuj łączność internetową

### "No Response / Timeout"
**Przyczyna:** Serwer nie odpowiada w limicie czasu

**Rozwiązanie:**
- Sprawdź, czy usługa jest dostępna
- Zweryfikuj URL punktu końcowego
- Sprawdź, czy istnieją limity szybkości
- Skontaktuj się z administratorem systemu

### "Invalid JSON"
**Przyczyna:** Dane żądania są nieprawidłowo sformatowane

**Rozwiązanie:**
- Sprawdź brakujące przecinki w JSON
- Zweryfikuj, czy wszystkie cudzysłowy są poprawne
- Zwaliduj format JSON (użyj internetowego walidatora JSON)
- Sprawdź znaki specjalne

---

## Przykłady

### Przykład 1: Wysłanie do usługi webhook
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Przykład 2: Aktualizacja systemu zewnętrznego
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Przykład 3: Odpytanie usługi zewnętrznej
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Różnica względem karty "Call API"

| Funkcja | HTTPS Request | Call API |
|---------|---------------|----------|
| Prostota | Prosta | Bardziej złożona |
| Parametry | Podstawowe | Zaawansowane |
| Obsługa błędów | Podstawowa | Szczegółowa |
| Użyj do | Szybkich integracji | Złożonych API |
| Najlepsza do | Webhooków | Profesjonalnych API |

---

## Kwestie bezpieczeństwa

✅ **Zawsze używaj HTTPS** (bezpieczne połączenie)

⚠️ **Nigdy:**
- Nie umieszczaj haseł w adresie URL
- Nie ujawniaj kluczy API w dziennikach
- Nie dołączaj danych osobowych w parametrach
- Nie używaj HTTP dla danych wrażliwych

---

## Najlepsze praktyki

✅ **Rób:**
- Najpierw testuj z małymi ilościami danych
- Uwzględnij obsługę błędów
- Rejestruj ważne żądania
- Dokumentuj integrację
- Monitoruj awarie

❌ **Nie rób:**
- Nie wywołuj wielokrotnie tego samego punktu końcowego, jeśli nie jest to potrzebne
- Nie ignoruj błędów odpowiedzi
- Nie dołączaj danych wrażliwych w postaci zwykłego tekstu
- Nie przekraczaj limitów szybkości usługi

---

## Powiązane karty

- **CALL_API** - Bardziej zaawansowana integracja API
- **CONDITION_HTTPS_REQUEST_STATUS** - Sprawdź, czy żądanie się powiodło
- **ACTION_SEND_EMAIL** - Wyślij zamiast tego za pośrednictwem wiadomości e-mail
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Zautomatyzowane skrypty
