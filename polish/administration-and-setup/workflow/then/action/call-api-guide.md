# Call External API

Te karty trafiają do grupy **Then** w Kreatorze przepływów — akcje uruchamiane po spełnieniu warunków When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dodaje się do grupy <strong>Then</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

## Cel
Ta karta umożliwia wysyłanie danych do zewnętrznej witryny lub usługi i odbieranie informacji zwrotnych. Pomyśl o tym jak o wysłaniu pytania do usługi zewnętrznej i otrzymaniu odpowiedzi, którą możesz wykorzystać w swoim przepływie pracy.

**Rzeczywisty przykład:** Twoja firma korzysta z systemu cenowego na innej witrynie. Ta karta może automatycznie zapytać ten system cenowy o aktualną cenę pozycji i wprowadzić tę cenę do Twojego dokumentu.

---

## Kiedy używać tej karty

Użyj tej karty, gdy musisz:
- Uzyskać informacje z usługi zewnętrznej (jak ceny, walidacja lub dane wyszukiwania)
- Wysłać informacje o dokumencie do innego systemu w celu przetworzenia
- Zintegrować się z usługami stron trzecich
- Automatycznie pobierać dane bez ręcznych wyszukiwań
- Połączyć ze sobą wiele systemów biznesowych

**Typowe scenariusze:**
- Wyszukiwanie informacji o dostawcy w bazie danych
- Uzyskiwanie cen w czasie rzeczywistym z usługi cenowej
- Walidacja danych względem systemu zewnętrznego
- Pobieranie informacji o wysyłce od dostawcy logistycznego

---

## Jak to działa

1. **Sprawdzenie warunku**: Przepływ pracy najpierw sprawdza, czy warunki w sekcjach "Where" i "And" są spełnione
2. **Przygotowanie danych**: Karta zbiera skonfigurowane parametry
3. **Wysłanie żądania**: Wysyła Twoje dane do zewnętrznego API/usługi
4. **Odbiór odpowiedzi**: Usługa zewnętrzna odpowiada danymi
5. **Kontynuacja**: Przepływ pracy wykorzystuje te dane w kolejnych kartach

---

## Wyjaśnienie parametrów

### API Endpoint URL
**Co to jest:** Adres usługi zewnętrznej, z którą chcesz się komunikować

**Przykład:** `https://api.supplier-system.com/product/pricing`

**Jak go znaleźć:** Zapytaj swój zespół IT lub dostawcę usługi o ich punkt końcowy API

---

### HTTP Method
**Co to jest:** Typ żądania do wysłania

**Opcje:**
- **GET**: Żądanie informacji (jak zadawanie pytania)
- **POST**: Wysłanie nowych danych
- **PUT**: Aktualizacja istniejących danych
- **DELETE**: Usunięcie danych

**Najczęstsze:** GET (do pobierania informacji)

---

### Headers
**Co to jest:** Dodatkowe instrukcje dla wywoływanej usługi

**Przykład:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Dlaczego jest potrzebne:** Usługi często wymagają uwierzytelniania lub konkretnych instrukcji dotyczących formatu

---

### Parameters (Query Parameters)
**Co to jest:** Dodatkowe informacje przekazywane w adresie URL

**Przykład:**
```
?supplier_id=12345&currency=USD
```

**Rzeczywisty przykład:** Jeśli pytasz o ceny, parametry mogą obejmować identyfikator dostawcy i walutę

---

### Request Data (Body)
**Co to jest:** Informacje, które wysyłasz do usługi

**Przykład:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Kiedy używane:** Podczas korzystania z metod POST lub PUT

---

## Przykład krok po kroku

### Scenariusz: Uzyskanie cen dostawcy w czasie rzeczywistym

**Konfiguracja:**
1. **Card Type:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Method:** POST
4. **Headers:** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Co się dzieje:**
1. Dokument przybywa z Product ID: ABC123, Quantity: 100
2. Karta wysyła żądanie do API dostawcy
3. API dostawcy odpowiada: `{"unit_price": 25.50, "total_price": 2550}`
4. Przepływ pracy kontynuuje z tymi informacjami cenowymi
5. Następna karta może użyć tych danych do walidacji ceny faktury

---

## Kroki konfiguracji

### 1. Uzyskaj informacje o API
Skontaktuj się z dostawcą usługi zewnętrznej i poproś o:
- [ ] URL punktu końcowego API
- [ ] Metodę uwierzytelniania (klucz API, nazwa użytkownika/hasło, OAuth)
- [ ] Wymagane parametry
- [ ] Oczekiwany format odpowiedzi
- [ ] Limity szybkości lub kwoty

### 2. Skonfiguruj kartę
1. Wprowadź URL punktu końcowego API
2. Wybierz metodę HTTP (zwykle GET lub POST)
3. Dodaj nagłówki uwierzytelniania, jeśli wymagane
4. Dodaj wszelkie wymagane parametry
5. Sformatuj dane żądania jako JSON, jeśli to konieczne

### 3. Przetestuj kartę
1. Użyj dokumentu testowego
2. Uruchom przepływ pracy
3. Sprawdź, czy odpowiedź jest poprawnie odbierana
4. Zweryfikuj, czy format danych odpowiada oczekiwaniom

---

## Typowe scenariusze odpowiedzi

### Pomyślna odpowiedź (kod statusu 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ Dane są dostępne do użycia przez kolejne karty

### Odpowiedź błędu (kod statusu 404)
```json
{
  "error": "Product not found"
}
```
⚠️ API nie mogło znaleźć tego, czego szukasz

### Timeout
Usługa zewnętrzna nie odpowiedziała w limicie czasu
⚠️ Sprawdź, czy usługa jest dostępna lub czy URL punktu końcowego jest poprawny

---

## Przykładowe przepływy pracy

### Przykład 1: Automatyczna walidacja cen
**Scenariusz:** Walidacja cen faktury względem aktualnych cen dostawcy

**Przepływ:**
1. Dokument przybywa z pozycją faktury (Product: A123, Price: €50)
2. **Call API Card** → Pyta API dostawcy: "What's the current price for A123?"
3. Dostawca odpowiada: "€48"
4. **Condition Card** → Sprawdza, czy cena faktury (€50) mieści się w 5% aktualnej ceny (€48)
5. **Approval Card** → Zatwierdza, jeśli mieści się w tolerancji

### Przykład 2: Automatyczne wyszukiwanie dostawcy
**Scenariusz:** Uzyskanie danych podstawowych dostawcy z centralnej bazy danych

**Przepływ:**
1. Faktura przybywa z Supplier Code: SUPP-789
2. **Call API Card** → Pyta system: "Give me details for supplier SUPP-789"
3. System odpowiada: Name, Contact, Terms itp.
4. **Set Field Cards** → Wypełnij pola dokumentu tymi danymi
5. **Export Card** → Eksport z kompletnymi informacjami

### Przykład 3: Koszty wysyłki w czasie rzeczywistym
**Scenariusz:** Uzyskanie automatycznego kosztu wysyłki na podstawie miejsca docelowego

**Przepływ:**
1. Dokument ma adres dostawy
2. **Call API Card** → Zapytaj dostawcę wysyłki: "What's the cost to [address]?"
3. Dostawca odpowiada kosztem wysyłki
4. **Calculate Card** → Dodaj wysyłkę do łącznej kwoty faktury
5. **Export Card** → Wyślij ze zaktualizowaną sumą

---

## Rozwiązywanie problemów

### Błąd "Connection Timeout"
**Przyczyna:** Usługa API nie odpowiada

**Rozwiązania:**
- [ ] Sprawdź, czy usługa jest dostępna (odwiedź witrynę)
- [ ] Zweryfikuj, czy URL punktu końcowego jest poprawny (brak literówek)
- [ ] Sprawdź połączenie internetowe
- [ ] Skontaktuj się z dostawcą usługi
- [ ] Sprawdź, czy usługa ma limity szybkości (wysyłasz zbyt wiele żądań)

### Błąd "Unauthorized" lub "403 Forbidden"
**Przyczyna:** Uwierzytelnianie nie powiodło się

**Rozwiązania:**
- [ ] Zweryfikuj, czy Twój klucz API jest poprawny
- [ ] Sprawdź, czy Twój klucz API nie wygasł
- [ ] Upewnij się, że nagłówek uwierzytelniania jest poprawnie sformatowany
- [ ] Zweryfikuj, czy masz uprawnienia do tego punktu końcowego

### "Bad Request" lub błąd "400"
**Przyczyna:** Format danych żądania jest nieprawidłowy

**Rozwiązania:**
- [ ] Sprawdź składnię JSON (brakujące przecinki, cudzysłowy itp.)
- [ ] Zweryfikuj, czy wszystkie wymagane pola są uwzględnione
- [ ] Sprawdź, czy nazwy parametrów odpowiadają oczekiwaniom usługi
- [ ] Skonsultuj się z dokumentacją API

### "Odpowiedź nie działa zgodnie z oczekiwaniami"
**Rozwiązania:**
- [ ] Przetestuj API za pomocą narzędzia takiego jak Postman
- [ ] Porównaj rzeczywisty format odpowiedzi z oczekiwanym formatem
- [ ] Sprawdź, czy dokumentacja API uległa zmianie
- [ ] Zweryfikuj, czy wysyłane dane są poprawne

---

## Wykorzystanie danych odpowiedzi

Gdy otrzymasz dane z API, kolejne karty mogą je wykorzystać:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Uwagi dotyczące bezpieczeństwa

⚠️ **Ważne:** Nigdy nie umieszczaj w konfiguracji karty informacji wrażliwych, które mogą być widoczne dla innych użytkowników

- Nie umieszczaj haseł na stałe w kodzie
- Używaj kluczy API w bezpieczny sposób
- Nie dołączaj danych osobowych w dziennikach
- Używaj punktów końcowych HTTPS (nie HTTP)

---

## Wskazówki i najlepsze praktyki

✅ **Rób:**
- Najpierw testuj na małej próbce dokumentów
- Utrzymuj wywołania API proste i ukierunkowane
- Dodaj obsługę błędów za pomocą kart Condition
- Monitoruj użycie/koszty API
- Udokumentuj wymagania API dla swojego zespołu

❌ **Nie rób:**
- Nie wywołuj API dla każdego pojedynczego żądania, jeśli możesz buforować dane
- Nie ignoruj kodów błędów odpowiedzi
- Nie używaj testowych API w produkcji
- Nie zapominaj o dodaniu nagłówków uwierzytelniania
- Nie zakładaj, że API zawsze będzie dostępne

---

## Powiązane karty

- **ACTION_HTTPS_REQUEST** - Podobne, ale prostsze żądania HTTPS
- **CONDITION_HTTPS_REQUEST_STATUS** - Sprawdź, czy wywołanie API się powiodło
- **ACTION_SEND_EMAIL** - Wyślij dane za pośrednictwem wiadomości e-mail zamiast API
- **CALL_API** (inna wersja) - Alternatywna metoda wywołania API

---

## Potrzebujesz pomocy?

- Poproś swój zespół IT/integracji o dokumentację API
- Najpierw użyj narzędzia Postman do testowania punktów końcowych API
- Sprawdź portal wsparcia dostawcy usługi
- Przejrzyj dokumentację API pod kątem wymaganych formatów
