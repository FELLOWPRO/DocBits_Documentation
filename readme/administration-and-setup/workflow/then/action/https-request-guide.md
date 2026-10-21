# Wyślij żądanie HTTPS

***

Dodaj tę kartę do grupy **Wtedy** Kreatora przepływu pracy — akcje, które zostaną uruchomione po spełnieniu warunków Kiedy/I:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pl.png" alt="Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Niezapisany przykład z kartami Kiedy, I oraz Wtedy. Uzupełnij wszystkie pola przed uruchomieniem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

***

## 📌 Informacje o wersji

**Aktualna wersja:** v2 (najnowsza i zalecana) **Stan:** ✅Aktywny

**Historia wersji:**

* v1 → Proste żądanie HTTP (nie jest już zalecane)
* **v2 → AKTUALNY** (dodano obsługę wielu języków)

**Co się zmieniło:** wersja 2 dodała obsługę internacjonalizacji (i18n). Podstawowa funkcjonalność webhooka/żądania pozostaje niezmieniona.

📖 [Historia wersji i zmiany](../../release.md) | [Kompletna baza danych kart](../../cards-overview/export-cards-guide.md)

***

## Cel

Ta karta wysyła bezpieczną wiadomość do witryny internetowej lub usługi i może otrzymać odpowiedź zwrotną. Jest prostsza niż karta „Call API” i przydatna przy szybkich integracjach.

**Przykład z życia codziennego:** Wyślij dane z faktury do swojego systemu księgowego lub zapytaj system zewnętrzny, czy pracownik jest zatwierdzony do przetwarzania tego zakupu.

***

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:

* Wysyłaj powiadomienia webhooka do usług zewnętrznych
* Wyzwalaj akcje w innych systemach
* Zapytanie o prostą usługę internetową
* Wysyłaj aktualizacje statusu do innych aplikacji
* Wykonuj proste integracje bez skomplikowanych wymagań API

***

## Jak to działa

1. **Sprawdzanie wyzwalacza**: System sprawdza, czy spełnione są warunki „Kiedy” i „I”
2. **Żądanie kompilacji**: System przygotowuje żądanie HTTPS z Twoimi parametrami
3. **Wyślij bezpiecznie**: Dane są wysyłane przy użyciu bezpiecznego połączenia HTTPS
4. **Odbierz odpowiedź**: Usługa zewnętrzna odpowiada
5. **Kontynuuj**: Przepływ pracy jest kontynuowany z danymi odpowiedzi

***

## Parametry

### Adres URL

Adres strony internetowej, na którą należy wysłać żądanie

**Przykład:** `https://webhook.company.com/process`

### Nagłówki

Specjalne instrukcje dla odbiorcy

**Przykład:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Metoda

* **GET**: Poproś o informacje
* **POST**: Wyślij dane
* **PUT**: Aktualizuj dane

### Parametry (ciąg zapytania)

Dane dodane do adresu URL

**Przykład:** `?action=approve&user_id=123`

### Poproś o dane

Rzeczywiste wysyłane informacje (w formacie JSON)

**Przykład:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Przykład krok po kroku

### Scenariusz: Wyślij fakturę do systemu księgowego

**Konfiguracja karty:**

* **Adres URL:** `https://accounting.company.com/invoices/create`
* **Metoda:** POST
* **Nagłówki:** `Authorization: Bearer YOUR-TOKEN`
* **Zażądaj danych:**

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

***

## Typowe przypadki użycia

### 1. Powiadomienia webhooka

Wysyłaj powiadomienia w czasie rzeczywistym do innych systemów, gdy coś dzieje się w DocFlow

**Przykład:**

* Dokument zatwierdzony → Wyślij powiadomienie do systemu realizacji
* Zmiana dostawcy → Powiadom zespół zakupowy za pośrednictwem webhooka Slack/Teams

### 2. Integracja z systemem zewnętrznym

Połącz DocFlow z innymi systemami biznesowymi w celu automatycznej wymiany danych

**Przykład:**

* Po przetworzeniu dokumentu → Synchronizuj z systemem ERP
* Dodano nowego dostawcę → Utwórz rekord dostawcy w systemie danych podstawowych

### 3. Procesy zatwierdzania

Wyślij dokument do zewnętrznego systemu zatwierdzającego i otrzymaj decyzję

**Przykład:**

* Faktura o dużej wartości → Wyślij do Finance do zatwierdzenia
* Zwróć dokument do systemu zewnętrznego wraz z decyzją

***

## Przewodnik konfiguracji

### Krok 1: Uzyskaj informacje o punkcie końcowym

Zapytaj system odbiorczy o:

* [ ] Adres URL HTTPS
* [ ] Wymagane nagłówki
* [ ] Metoda uwierzytelniania
* [ ] Oczekiwany format żądania
* [ ] Oczekiwany format odpowiedzi

### Krok 2: Skonfiguruj kartę

1. Wprowadź adres URL HTTPS
2. Ustaw metodę HTTP (zwykle POST)
3. W razie potrzeby dodaj uwierzytelnianie
4. Sformatuj dane żądania jako JSON
5. Dodaj dowolne niestandardowe nagłówki

### Krok 3: Przetestuj

Wyślij żądanie testowe i sprawdź odpowiedź

***

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

### Złe żądanie (400)

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

W systemie odbierającym wystąpił problem wewnętrzny

***

## Rozwiązywanie problemów

### „Błąd certyfikatu”

**Przyczyna:** Problem z certyfikatem bezpieczeństwa HTTPS

**Rozwiązanie:**

* Sprawdź, czy adres URL jest poprawny
* Sprawdź, czy certyfikat witryny jest ważny
* Upewnij się, że używasz protokołu HTTPS (nie HTTP)

### „Połączenie odrzucone”

**Przyczyna:** Nie można połączyć się z serwerem

**Rozwiązanie:**

* Sprawdź, czy adres URL/IP jest poprawny
* Sprawdź, czy usługa jest uruchomiona
* Sprawdź reguły zapory sieciowej
* Sprawdź łączność z Internetem

### „Brak odpowiedzi / przekroczenie limitu czasu”

**Przyczyna:** Serwer nie odpowiada w określonym czasie

**Rozwiązanie:**

* Sprawdź, czy usługa jest dostępna
* Sprawdź adres URL punktu końcowego
* Sprawdź, czy istnieją limity stawek
* Skontaktuj się z administratorem systemu

### „Nieprawidłowy JSON”

**Przyczyna:** Dane żądania są zniekształcone

**Rozwiązanie:**

* Sprawdź brakujące przecinki w formacie JSON
* Sprawdź, czy wszystkie cytaty są poprawne
* Sprawdź poprawność formatu JSON (użyj internetowego walidatora JSON)
* Sprawdź znaki specjalne

***

## Przykłady

### Przykład 1: Wyślij do usługi webhook

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

### Przykład 2: Zaktualizuj system zewnętrzny

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

### Przykład 3: Zapytanie o usługę zewnętrzną

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Różnica w stosunku do karty „Call API”.

| Funkcja        | Żądanie HTTPS      | Zadzwoń do API          |
| -------------- | ------------------ | ----------------- |
| Prostota     | Proste             | Bardziej złożone      |
| Parametry     | Podstawowe              | Zaawansowane          |
| Obsługa błędów | Podstawowe              | Szczegółowe          |
| Użyj dla        | Szybkie integracje | Złożone interfejsy API      |
| Najlepsze dla       | Haki internetowe           | Profesjonalne API |

***

## Względy bezpieczeństwa

✅ **Zawsze używaj HTTPS** (bezpieczne połączenie)

⚠️ **Nigdy:**

* Umieść hasła w adresie URL
* Ujawnij klucze API w dziennikach
* Uwzględnij dane osobowe w parametrach
* W przypadku wrażliwych danych używaj protokołu HTTP

***

## Najlepsze praktyki

✅ **Wykonaj:**

* Najpierw przetestuj na małych ilościach danych
* Uwzględnij obsługę błędów
* Rejestruj ważne żądania
* Udokumentuj integrację
* Monitoruj awarie

❌ **Nie:**

* Jeśli nie jest to potrzebne, wielokrotnie wywoływaj ten sam punkt końcowy
* Ignoruj błędy odpowiedzi
* Uwzględnij wrażliwe dane w postaci zwykłego tekstu
* Przekrocz limity stawek za usługę

***

## Powiązane karty

* **CALL\_API** - Bardziej zaawansowana integracja API
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Sprawdź, czy żądanie się powiodło
* **ACTION\_SEND\_EMAIL** — zamiast tego wyślij e-mailem
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Zautomatyzowane skrypty

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Przykład akcji HTTPS

**Konfiguracja:** Wybierz metodę `POST`, zamień `DEMO_WEBHOOK_URL` na autoryzowany testowy punkt końcowy, dodaj nagłówek `Content-Type: application/json` i treść `{"document_number":"DEMO-001"}`. Skonfiguruj uwierzytelnianie tylko zgodnie z wymaganiami tego punktu końcowego; nigdy nie kopiuj prawdziwego sekretu do dokumentacji.

**Oczekiwany wynik i kontrprzykład:** Akcja wysyła skonfigurowane żądanie, gdy wykonywana jest jej trasa przepływu pracy. Sprawdź odpowiedź HTTP i odbierającą usługę testową. Przekroczenie limitu czasu nie jest dowodem na to, że usługa nic nie zrobiła, a ta akcja Następnie jest oddzielna od karty And, która sprawdza stan HTTP. Ta przykładowa prośba nie została wysłana.

To jest ilustracyjna konfiguracja testu i oczekiwany wynik; nie zostało ono wykonane. Skorzystaj z danych i odbiorców skonfigurowanych w Twojej organizacji testowej.
