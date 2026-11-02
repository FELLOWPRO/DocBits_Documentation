# Narzedzia Card SDK

Narzedzia Card SDK pozwalaja tworzyc, walidowac, testowac i zarzadzac niestandardowymi kartami partnerskimi przez MCP. Karty partnerskie rozszerzaja DocFlow o niestandardowa logike biznesowa napisana w Pythonie.

## Cykl zycia karty

Karta partnerska przechodzi przez nastepujace stany zgloszenia (`partner_status`):

| Stan | Znaczenie | Widocznosc w przepływach pracy |
|-------|---------|---------------------|
| `validating` | Zgloszenie zaakceptowane; pipeline walidacji jest uruchomiony. | Tylko organizacja zglaszajaca |
| `validated` | Wszystkie etapy walidacji zakonczone sukcesem. Oczekuje na zatwierdzenie admina. | Tylko organizacja zglaszajaca |
| `rejected` | Walidacja nie powiodla sie lub admin odrzucil karte. Kod zrodlowy jest zachowywany do wgladu. | Tylko organizacja zglaszajaca |
| `approved` | Admin zatwierdzil karte; `enabled = true`. | **Wszystkie organizacje** |
| `disabled` | Wczesniej zatwierdzona karta, ktora admin dezaktywowal. | Tylko organizacja zglaszajaca |
| `deleted` | Miekko usunieta; nie zwracana w listach zgloszen. | Ukryta |

{% hint style="warning" %}
**Widocznosc miedzy organizacjami:** Karta partnerska jest dostepna dla wezlow przepływu pracy w `list_cards` dopiero po jej **zatwierdzeniu**. Zatwierdzone karty partnerskie sa widoczne dla kazdej organizacji na platformie — zatwierdzenie to globalna aktywacja, a nie aktywacja na poziomie organizacji. Karty niezatwierdzone (validating, validated, rejected, disabled) sa widoczne tylko dla organizacji, ktora je zglosila.
{% endhint %}

Typowy przepływ:

1. **Utworz** karte za pomoca `sdk_create_card` lub `sdk_import_github` — uruchamia pipeline walidacji i zapisuje karte z `partner_status = validated` (lub `rejected` w przypadku bledu).
2. **Zwaliduj** za pomoca `sdk_validate_card`, aby ponownie sprawdzic istniejaca karte lub przetestowac nowy kod zrodlowy na sucho bez zapisywania.
3. **Przetestuj** za pomoca `sdk_test_card`, aby wykonac karte w srodowisku sandbox wzgledem mock-kontekstu.
4. **Zatwierdz** za pomoca `sdk_approve_card` (tylko admin organizacji) — ponownie uruchamia walidacje AST i behawioralna, nastepnie ustawia `partner_status = approved` i `enabled = true`.
5. Po zatwierdzeniu karta pojawia sie w `list_cards` dla kazdej organizacji i mozna sie do niej odwolywac z wezlow przepływu pracy.

## Narzedzia deweloperskie

### sdk\_create\_card

Tworzy nowa karte partnerska z kodu zrodlowego i manifestow. Uruchamia pelny pipeline walidacji (zobacz [Etapy walidacji](#sdk_validate_card) ponizej) i zapisuje karte w bazie danych. Karta laduje w stanie `validated` i wymaga zatwierdzenia admina przed uzyciem w przepływach pracy.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `app_manifest` | object | Tak | Manifest aplikacji z id, name, version, informacjami o partnerze |
| `card_manifest` | object | Tak | Manifest karty z id, title, entry\_point, class\_name, args |
| `card_type` | string | Tak | `action` lub `condition` |
| `source_code` | string | Tak | Kod zrodlowy Python (musi rozszerzac `PartnerCard`) |
| `test_code` | string | Tak | Kod testow Pytest dla karty |
| `locales` | object | Nie | Tlumaczenia lokalizacji, np. `{"en": {...}, "de": {...}}` |

**Przyklad manifestu aplikacji:**

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

**Przyklad manifestu karty:**

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

**Przyklad kodu zrodlowego:**

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
`CardStatus` ma trzy wartosci, ktore odwzorowuja sie bezposrednio na krawedzie przepływu pracy:

| Status | Wybierana krawedz | Do uzycia dla |
|--------|------------|------------|
| `SUCCESS` | `success` | Karta zakonczona sukcesem — dotyczy zarowno warunkow, jak i akcji. |
| `FAILED` | `failed_condition` | **Tylko karty warunkow.** Warunek zostal oceniony jako false — przepływ pracy podaza galezia "else". Karty akcji nie maja uchwytu `failed_condition`, wiec zwrocenie `FAILED` z akcji pozostawia wykonanie bez wyjscia. |
| `ERROR` | `error` | Nieoczekiwany blad w czasie wykonania (wyjatek). Dotyczy zarowno warunkow, jak i akcji. |

W skrocie: akcje zwracaja `SUCCESS` lub `ERROR`; warunki moga dodatkowo zwracac `FAILED`.
{% endhint %}

### sdk\_validate\_card

Uruchamia pipeline walidacji na karcie partnerskiej bez jej zapisywania. Dwa tryby:

- **Tryb A** — Walidacja istniejacej karty po ID
- **Tryb B** — Walidacja nowego kodu zrodlowego inline

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Nie | UUID istniejacej karty (Tryb A) |
| `app_manifest` | object | Nie | Manifest aplikacji (Tryb B) |
| `card_manifest` | object | Nie | Manifest karty (Tryb B) |
| `card_type` | string | Nie | `action` lub `condition` (Tryb B) |
| `source_code` | string | Nie | Kod zrodlowy Python (Tryb B) |
| `test_code` | string | Nie | Kod testow (Tryb B) |

{% hint style="info" %}
Podaj sam `card_id` (Tryb A) lub `app_manifest` + `card_manifest` + `source_code` razem (Tryb B).
{% endhint %}

**Etapy walidacji:**

1. **Structure** — Weryfikuje uklad plikow, schemat manifestu (`app.json`, `.docflowcompose/flow/...`) oraz to, czy zadeklarowane entry pointy istnieja.
2. **Locales** — Uzgadnia klucze tlumaczen uzywane w karcie z plikami `locales/<lang>.json`; nie powiedzie sie, jesli klucz brakuje w zadeklarowanym jezyku.
3. **AST Analysis** — Przechodzi przez kazdy plik `.py` pod `src/` i sprawdza zabronione importy, niebezpieczne wywolania oraz wymagania dotyczace hierarchii klas / sygnatur metod.
4. **Dependencies** — Waliduje, ze wszystkie importy rozwiazuja sie do dozwolonych modulow z allowlisty SDK.
5. **Tests** — Uruchamia zestaw testow pytest karty pod zredukowanymi rlimitami.
6. **Behavioral** — Wykonuje karte w produkcyjnym sandboxie wobec minimalnego mock-kontekstu, aby potwierdzic zachowanie w czasie wykonania.

Etapy uruchamiane sa kolejno; pierwszy nieudany etap przerywa pozostale. Etap 6 (Behavioral) jest rowniez ponownie uruchamiany w momencie zatwierdzania jako kontrola defense-in-depth, zanim karta zostanie aktywowana.

### sdk\_test\_card

Wykonuje karte partnerska w srodowisku sandbox z mock-kontekstem. Sandbox wymusza ograniczone builtins, kuratowana allowliste importow, limit czasu wykonania oraz zredukowane limity zasobow procesu — te same ograniczenia, pod ktorymi dziala karta po zatwierdzeniu.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Nie | UUID istniejacej karty (Tryb A) |
| `source_code` | string | Nie | Kod zrodlowy do testow inline (Tryb B) |
| `class_name` | string | Nie | Nazwa klasy do testow inline (Tryb B) |
| `variables` | object | Nie | Zmienne przekazywane do konstruktora karty |
| `mock_context` | object | Nie | Mock-kontekst wykonania |

**Pola mock-kontekstu:**

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

Narzedzie zwraca `execution_success` (wskazuje, czy sandbox uruchomil karte do konca — limit czasu, naruszenie importu lub rzucony wyjatek ustawiaja go na `false`), `card_status` (`CardStatus` zwrocony przez sama `execute()`), `message` i `data` karty, przechwycone `logs` oraz `execution_time_ms`.

### sdk\_import\_github

Importuje aplikacje partnera z repozytorium GitHub. Klonuje repo, czyta `app.json` i importuje wszystkie karty znalezione w katalogu `.docflowcompose`.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `github_url` | string | Tak | URL HTTPS GitHub (np. `https://github.com/org/repo`) |
| `branch` | string | Nie | Galaz do sklonowania (domyslnie: `main`) |
| `token` | string | Nie | Token GitHub do prywatnych repozytoriow |

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

## Narzedzia zarzadzania

### sdk\_list\_submissions

Wyswietla wszystkie zgloszenia kart partnerskich dla biezacej organizacji.

**Parametry:** Brak

### sdk\_get\_submission\_status

Pobiera status walidacji i raport dla konkretnego zgloszenia karty partnerskiej.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Tak | UUID karty partnerskiej |

### sdk\_approve\_card

Zatwierdza zwalidowana karte partnerska i ja aktywuje. Zatwierdzenie ponownie uruchamia walidacje AST i behawioralna jako kontrole defense-in-depth, ustawia `partner_status = approved` i `enabled = true` oraz rejestruje karte w rejestrze uruchomieniowym. Po zatwierdzeniu karta pojawia sie w `list_cards` dla **kazdej organizacji**, a nie tylko dla zglaszajacej.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Tak | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnien admina organizacji. Karta musi byc w stanie `validated`. Odrzucone karty musza zostac ponownie przeslane i ponownie zwalidowane, zanim beda mogly zostac zatwierdzone.
{% endhint %}

### sdk\_reject\_card

Odrzuca zgloszenie karty partnerskiej i je dezaktywuje.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Tak | UUID karty partnerskiej |
| `reason` | string | Nie | Powod odrzucenia |

{% hint style="warning" %}
Wymaga uprawnien admina organizacji.
{% endhint %}

### sdk\_delete\_submission

Miekko usuwa zgloszenie karty partnerskiej, niezaleznie od jej aktualnego stanu. Ustawia `partner_status = deleted`, `enabled = false` i `deprecated = true`. Wiersz jest zachowywany do celow audytu, ale jest ukryty z list zgloszen i `list_cards`.

**Parametry:**

| Parametr | Typ | Wymagany | Opis |
|----------|-----|----------|------|
| `card_id` | string | Tak | UUID karty partnerskiej |

{% hint style="warning" %}
Wymaga uprawnien admina organizacji.
{% endhint %}

### sdk\_list\_cards\_picker

Wyswietla wszystkie wlaczone, nieprzedawnione karty z flagami rol. Przydatne do okreslania, ktore karty mozna uzywac w ktorych typach wezlow przy budowaniu przepływow pracy.

**Parametry:** Brak

## Obecne mozliwosci i roadmapa

Partner Card SDK jest wdrazany przyrostowo. Oto, na co moze polegac twoja karta dzis i co jest dopiero podlaczane:

| Mozliwosc | Status |
|------------|--------|
| **Warunki na polach** — odczyt pol dokumentu z `context.document_fields` i rozgalezianie wedlug ich wartosci w kartach warunkow | ✅ Zaimplementowane |
| **Wychodzace zadania HTTP** — wywolywanie zewnetrznych uslug z wnetrza karty | 🚧 Aktualnie dodawane |
| **Rozszerzone informacje o dokumencie** — dodatkowe metadane dokumentu (poza `document_id`, `document_type` i `document_fields`) udostepnione na `ExecutionContext` | 🚧 Aktualnie dodawane |
| **Pomocnicy do wyszukiwania w tabelach bazy danych** — wbudowani pomocnicy do odczytu z tabel master-data / lookup DocBits z wnetrza karty | 📅 Planowane na 1.1 |
| **Przegladarka kodu karty partnerskiej** — widok tylko do odczytu zgloszonego kodu karty partnerskiej w interfejsie DocBits, aby adminowie mogli sprawdzic, co zatwierdzaja | 📅 Planowane na 1.1 |

{% hint style="info" %}
Jesli twoja karta wymaga mozliwosci, ktora jest jeszcze w trakcie tworzenia, walidacja nie powiedzie sie (zabroniony import, brakujacy atrybut kontekstu lub ograniczenie sandboxa), dopoki odpowiednia czesc nie zostanie wdrozona. Ta strona bedzie aktualizowana w miare wdrazania kazdej mozliwosci.
{% endhint %}

{% hint style="danger" %}
**Karty partnerskie uruchamiaja kod firm trzecich — uzywanie na wlasne ryzyko.**

Karty przeslane przez Partner Card SDK sa tylko **czesciowo walidowane przez DocBits**. Pipeline walidacji sprawdza strukture, locales, importy, wzorce AST, zaleznosci, wlasne testy karty oraz behawioralne uruchomienie smoke w sandboxie — **nie** stanowi to pelnego audytu bezpieczenstwa ani funkcjonalnej gwarancji logiki biznesowej karty.

Gdy admin organizacji zatwierdzi karte partnerska, staje sie ona dostepna dla kazdej organizacji na platformie i dziala w produkcyjnym sandboxie wobec rzeczywistych dokumentow. Zatwierdzenie i wlaczenie karty partnerskiej jest zatem jawna decyzja zaufania ze strony zatwierdzajacego admina. DocBits nie ponosi odpowiedzialnosci za utrate danych, niewlasciwy routing, wyciek informacji lub jakiekolwiek inne skutki spowodowane przez karte partnerska, ktora zdecydujesz sie zainstalowac lub zatwierdzic.

Jesli nie jestes pierwotnym autorem karty, sprawdz kod zrodlowy (a po wydaniu 1.1 uzyj przegladarki kodu karty partnerskiej) przed jej zatwierdzeniem.
{% endhint %}
