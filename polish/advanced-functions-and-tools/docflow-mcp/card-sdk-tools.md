# Narzędzia Card SDK

Narzędzia Card SDK pozwalają tworzyć, walidować, testować i zarządzać niestandardowymi kartami partnerskimi przez MCP. Karty partnerskie rozszerzają DocFlow o niestandardową logikę biznesową napisaną w Pythonie.

## Cykl życia karty

Karta partnerska przechodzi przez następujące stany zgłoszenia (`partner_status`):

| Stan | Znaczenie | Widoczność w przepływach pracy |
|-------|-----------|---------------------|
| `validating` | Zgłoszenie przyjęte; trwa potok walidacji. | Tylko organizacja zgłaszająca |
| `validated` | Wszystkie etapy walidacji zakończone powodzeniem. Oczekuje na zatwierdzenie przez administratora. | Tylko organizacja zgłaszająca |
| `rejected` | Walidacja nie powiodła się lub administrator odrzucił kartę. Kod źródłowy jest zachowany do wglądu. | Tylko organizacja zgłaszająca |
| `approved` | Administrator zatwierdził kartę; `enabled = true`. | **Wszystkie organizacje** |
| `disabled` | Wcześniej zatwierdzona karta, którą administrator dezaktywował. | Tylko organizacja zgłaszająca |
| `deleted` | Usunięta miękko; nie jest zwracana na listach zgłoszeń. | Ukryta |

{% hint style="warning" %}
**Widoczność w organizacjach:** Karta partnerska jest dostępna dla węzłów przepływów pracy w `list_cards` dopiero po **zatwierdzeniu**. Zatwierdzone karty partnerskie są widoczne dla każdej organizacji na platformie — zatwierdzenie to aktywacja globalna, a nie per organizacja. Karty niezatwierdzone (validating, validated, rejected, disabled) są widoczne tylko dla organizacji, która je zgłosiła.
{% endhint %}

Typowy przebieg:

1. **Utwórz** kartę za pomocą `sdk_create_card` lub `sdk_import_github` — uruchamia potok walidacji i zapisuje kartę z `partner_status = validated` (lub `rejected` w razie niepowodzenia).
2. **Zwaliduj** za pomocą `sdk_validate_card`, aby ponownie sprawdzić istniejącą kartę lub przeprowadzić próbną walidację nowego kodu źródłowego bez zapisywania.
3. **Przetestuj** za pomocą `sdk_test_card`, aby wykonać kartę w środowisku sandbox na symulowanym kontekście.
4. **Zatwierdź** za pomocą `sdk_approve_card` (tylko administrator organizacji) — ponownie uruchamia walidację AST i behawioralną, a następnie ustawia `partner_status = approved` i `enabled = true`.
5. Po zatwierdzeniu karta pojawia się w `list_cards` dla każdej organizacji i może być używana w węzłach przepływów pracy.

## Narzędzia deweloperskie

### sdk\_create\_card

Tworzy nową kartę partnerską z kodu źródłowego i manifestów. Uruchamia pełny potok walidacji (zobacz [Etapy walidacji](#sdk_validate_card) poniżej) i zapisuje kartę w bazie danych. Karta trafia do stanu `validated` i wymaga zatwierdzenia przez administratora, zanim będzie mogła być używana w przepływach pracy.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `app_manifest` | object | Tak | Manifest aplikacji z id, name, version, informacjami o partnerze |
| `card_manifest` | object | Tak | Manifest karty z id, title, entry\_point, class\_name, args |
| `card_type` | string | Tak | `action` lub `condition` |
| `source_code` | string | Tak | Kod źródłowy Python (musi rozszerzać `PartnerCard`) |
| `test_code` | string | Tak | Kod testów Pytest dla karty |
| `locales` | object | Nie | Tłumaczenia lokalizacji, np. `{"en": {...}, "de": {...}}` |

**Przykład manifestu aplikacji:**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Przykład manifestu karty:**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Przykład kodu źródłowego:**

```python
from api.sdk.base import PartnerCard
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` ma trzy wartości, które odpowiadają bezpośrednio krawędziom przepływu pracy:

| Status | Wybrana krawędź | Do czego służy |
|--------|------------|------------|
| `SUCCESS` | `success` | Karta zakończyła się powodzeniem — dotyczy zarówno warunków, jak i akcji. |
| `FAILED` | `failed_condition` | **Tylko karty warunków.** Warunek został oceniony jako fałszywy — przepływ pracy przechodzi gałęzią „else". Karty akcji nie mają uchwytu `failed_condition`, więc zwrócenie `FAILED` z akcji pozostawia uruchomienie bez dalszej drogi. |
| `ERROR` | `error` | Nieoczekiwany błąd w czasie wykonania (wyjątek). Dotyczy zarówno warunków, jak i akcji. |

Krótko: akcje zwracają `SUCCESS` lub `ERROR`; warunki mogą dodatkowo zwracać `FAILED`.
{% endhint %}

### sdk\_validate\_card

Uruchamia potok walidacji karty partnerskiej bez zapisywania. Dwa tryby:

- **Tryb A** — Walidacja istniejącej karty według ID
- **Tryb B** — Walidacja nowego kodu źródłowego inline

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Nie | UUID istniejącej karty (Tryb A) |
| `app_manifest` | object | Nie | Manifest aplikacji (Tryb B) |
| `card_manifest` | object | Nie | Manifest karty (Tryb B) |
| `card_type` | string | Nie | `action` lub `condition` (Tryb B) |
| `source_code` | string | Nie | Kod źródłowy Python (Tryb B) |
| `test_code` | string | Nie | Kod testów (Tryb B) |

{% hint style="info" %}
Podaj albo sam `card_id` (Tryb A), albo `app_manifest` + `card_manifest` + `source_code` razem (Tryb B).
{% endhint %}

**Etapy walidacji:**

1. **Struktura** — Weryfikuje układ plików, schemat manifestu (`app.json`, `.docflowcompose/flow/...`) oraz istnienie zadeklarowanych punktów wejścia.
2. **Lokalizacje** — Uzgadnia klucze tłumaczeń użyte w karcie z plikami `locales/<lang>.json`; kończy się błędem, jeśli klucza brakuje w zadeklarowanym języku.
3. **Analiza AST** — Przechodzi przez każdy plik `.py` w `src/` i sprawdza zabronione importy, niebezpieczne wywołania oraz wymagania dotyczące hierarchii klas i sygnatur metod.
4. **Zależności** — Waliduje, czy wszystkie importy odnoszą się do dozwolonych modułów z białej listy SDK.
5. **Testy** — Uruchamia zestaw testów pytest karty przy obniżonych limitach zasobów (rlimits).
6. **Behawioralna** — Wykonuje kartę w produkcyjnym środowisku sandbox na minimalnym symulowanym kontekście, aby potwierdzić zachowanie w czasie wykonania.

Etapy są uruchamiane po kolei; pierwszy etap zakończony niepowodzeniem pomija pozostałe. Etap 6 (Behawioralna) jest ponownie uruchamiany podczas zatwierdzania jako dodatkowe zabezpieczenie przed aktywacją karty.

### sdk\_test\_card

Wykonuje kartę partnerską w środowisku sandbox z symulowanym kontekstem. Sandbox wymusza ograniczone funkcje wbudowane, wyselekcjonowaną białą listę importów, limit czasu wykonania oraz obniżone limity zasobów procesu — te same ograniczenia, w jakich karta działa po zatwierdzeniu.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Nie | UUID istniejącej karty (Tryb A) |
| `source_code` | string | Nie | Kod źródłowy do testowania inline (Tryb B) |
| `class_name` | string | Nie | Nazwa klasy do testowania inline (Tryb B) |
| `variables` | object | Nie | Zmienne przekazywane do konstruktora karty |
| `mock_context` | object | Nie | Symulowany kontekst wykonania |

**Pola symulowanego kontekstu:**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

Narzędzie zwraca `execution_success` (czy sandbox wykonał kartę do końca — przekroczenie limitu czasu, naruszenie zasad importu lub zgłoszony wyjątek ustawia wartość `false`), `card_status` (`CardStatus` zwrócony przez samo `execute()`), `message` i `data` karty, przechwycone `logs` oraz `execution_time_ms`.

### sdk\_import\_github

Importuje aplikację partnerską z repozytorium GitHub. Klonuje repozytorium, odczytuje `app.json` i importuje wszystkie karty znalezione w katalogu `.docflowcompose`.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `github_url` | string | Tak | URL HTTPS GitHub (np. `https://github.com/org/repo`) |
| `branch` | string | Nie | Gałąź do sklonowania (domyślnie: `main`) |
| `token` | string | Nie | Token GitHub dla prywatnych repozytoriów |

**Oczekiwana struktura repozytorium:**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

## Narzędzia zarządzania

### sdk\_list\_submissions

Wyświetla wszystkie zgłoszenia kart partnerskich bieżącej organizacji.

**Parametry:** Brak

### sdk\_get\_submission\_status

Pobiera status walidacji i raport dla konkretnego zgłoszenia karty partnerskiej.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Tak | UUID karty partnerskiej |

### sdk\_approve\_card

Zatwierdza zwalidowaną kartę partnerską i aktywuje ją. Zatwierdzenie ponownie uruchamia walidację AST i behawioralną jako dodatkowe zabezpieczenie, ustawia `partner_status = approved` i `enabled = true` oraz rejestruje kartę w rejestrze runtime. Po zatwierdzeniu karta pojawia się w `list_cards` dla **każdej organizacji**, nie tylko dla zgłaszającej.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Tak | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnień administratora organizacji. Karta musi być w stanie `validated`. Odrzucone karty trzeba ponownie przesłać i zwalidować, zanim będzie można je zatwierdzić.
{% endhint %}

### sdk\_reject\_card

Odrzuca zgłoszenie karty partnerskiej i dezaktywuje je.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Tak | UUID karty partnerskiej |
| `reason` | string | Nie | Powód odrzucenia |

{% hint style="warning" %}
Wymaga uprawnień administratora organizacji.
{% endhint %}

### sdk\_delete\_submission

Usuwa miękko zgłoszenie karty partnerskiej, niezależnie od jego bieżącego stanu. Ustawia `partner_status = deleted`, `enabled = false` i `deprecated = true`. Wiersz jest zachowany do celów audytu, ale ukryty na listach zgłoszeń i w `list_cards`.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|-----------|------|----------|-------------|
| `card_id` | string | Tak | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnień administratora organizacji.
{% endhint %}

### sdk\_list\_cards\_picker

Wyświetla wszystkie włączone, nieoznaczone jako przestarzałe karty wraz z flagami ról. Przydatne do ustalenia, które karty mogą być używane w jakich typach węzłów podczas budowania przepływów pracy.

**Parametry:** Brak

## Obecne możliwości i plan rozwoju

Partner Card SDK jest wdrażany stopniowo. Oto na czym karta może polegać już dziś, a co jest jeszcze w trakcie realizacji:

| Możliwość | Status |
|------------|--------|
| **Warunki na polach** — odczyt pól dokumentu z `context.document_fields` i rozgałęzianie na podstawie ich wartości w kartach warunków | ✅ Zaimplementowane |
| **Wychodzące żądania HTTP** — wywoływanie usług zewnętrznych z wnętrza karty | 🚧 W trakcie dodawania |
| **Rozszerzone informacje o dokumencie** — dodatkowe metadane dokumentu (poza `document_id`, `document_type` i `document_fields`) udostępnione w `ExecutionContext` | 🚧 W trakcie dodawania |
| **Pomocniki wyszukiwania w tabelach bazy danych** — wbudowane pomocniki do odczytu z danych podstawowych / tabel wyszukiwania DocBits wewnątrz karty | 📅 Planowane na 1.1 |
| **Podgląd kodu źródłowego karty partnerskiej** — widok tylko do odczytu przesłanego kodu karty partnerskiej w interfejsie DocBits, aby administratorzy mogli sprawdzić, co zatwierdzają | 📅 Planowane na 1.1 |

{% hint style="info" %}
Jeśli Twoja karta potrzebuje możliwości, która jest jeszcze w realizacji, nie przejdzie walidacji (zabroniony import, brakujący atrybut kontekstu lub ograniczenie sandboxa) do czasu, aż odpowiedni element zostanie wdrożony. Ta strona będzie aktualizowana wraz z udostępnieniem kolejnych możliwości.
{% endhint %}

{% hint style="danger" %}
**Karty partnerskie uruchamiają kod stron trzecich — używasz ich na własne ryzyko.**

Karty przesłane przez Partner Card SDK są przez DocBits walidowane tylko **częściowo**. Potok walidacji sprawdza strukturę, lokalizacje, importy, wzorce AST, zależności, własne testy karty oraz behawioralny test uruchomieniowy w sandboxie — **nie** stanowi pełnego audytu bezpieczeństwa ani gwarancji funkcjonalnej logiki biznesowej karty.

Gdy administrator organizacji zatwierdzi kartę partnerską, staje się ona dostępna dla każdej organizacji na platformie i działa w produkcyjnym sandboxie na prawdziwych dokumentach. Zatwierdzenie i włączenie karty partnerskiej jest zatem wyraźną decyzją zaufania po stronie zatwierdzającego administratora. DocBits nie ponosi odpowiedzialności za utratę danych, nieprawidłowe kierowanie, wyciek informacji ani żadne inne skutki spowodowane kartą partnerską, którą zdecydujesz się zainstalować lub zatwierdzić.

Jeśli nie jesteś pierwotnym autorem karty, przejrzyj jej kod źródłowy (a po wydaniu 1.1 skorzystaj z podglądu kodu źródłowego karty partnerskiej) przed jej zatwierdzeniem.
{% endhint %}
