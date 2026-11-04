---
description: "P1: sprawdzanie wywołań API i użycia odpowiedzi"
---

# P1: sprawdzanie wywołań API i użycia odpowiedzi

**Call API** v2 dołącza skonfigurowaną ścieżkę do bazy API DocBits i używa kontekstu bieżącej organizacji. **Send HTTPS Request** v2 używa zewnętrznego URL i własnych nagłówków. Pełny obcy URL nie zastępuje ścieżki Call API. Obie karty symulują wysyłanie w Advanced Test.

Sprawdzona akcja HTTPS zapisuje status i tekst odpowiedzi w logu, ale nie udostępnia kolejnym kartom dowolnie nazwanego magazynu odpowiedzi JSON. Call API konwertuje tekst odpowiedzi na wartość logiczną. HTTP 200, prawidłowy JSON i udane dalsze przetwarzanie wymagają osobnych dowodów. Nie wymyślaj składni takiej jak `api.response.cost_center`.

Dla zewnętrznego `{"cost_center":"4711"}` uzgodnij jawnie wspierany zapis lub callback do pola dokumentu. Zweryfikuj zapisane pole i odczytaj je w przeznaczonym do tego kolejnym wykonaniu. Bezpośredni transfer wymaga karty lub rozszerzenia z udokumentowanym kontraktem wyjścia. JSON w konfiguracji nie dowodzi też rzeczywistych wysłanych bajtów JSON.

Użyj własnego celu testowego i sprawdź metodę, nagłówki, rzeczywiste body, status i schemat. Uwzględnij 4xx, 5xx, timeout, błędny JSON i podwójne wyzwolenie. Ponawiaj zapisy dopiero po sprawdzeniu pierwszego odbioru. Przykładowy URL jest zarezerwowanym symbolem i nie był testowany jako osiągalna usługa.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `call_api` · v2

Identyfikacja: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identyfikacja: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| API-01 | Advanced Test | symulowane; brak dowodu dostarczenia |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | sprawdź odbiór przed ponowieniem |
| API-04 | {"cost_center":"4711"} | brak automatycznego api.response.cost_center |
| API-05 | POST × 2 | sprawdź duplikaty u odbiorcy |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
