# Activity Logging

<figure><img src="../../../.gitbook/assets/activity_logging.png" alt="Activity Logging"><figcaption><p>Strona Activity Logging</p></figcaption></figure>

Activity Logging zapewnia podgląd zdarzeń systemowych we wszystkich usługach DocBits w czasie rzeczywistym. Używaj go do monitorowania przetwarzania, diagnozowania błędów i audytu zachowania systemu.

## Analytics Banner

U góry strony baner prowadzi do **Analytics Dashboard** z wykresami, metrykami i monitorowaniem w czasie rzeczywistym.

## Filtry

| Filtr | Opis |
|--------|-------------|
| **Time Range** | Wybierz okno czasowe (np. Today, Last 7 Days, Last 30 Days). |
| **Severity** | Włączaj lub wyłączaj poziomy ważności: **Debug**, **Info**, **Warning**, **Error**. Każdy znacznik pokazuje bieżącą liczbę. |
| **Service** | Filtruj logi według usługi (np. api, auth, api-service). |
| **Search logs** | Wyszukiwanie pełnotekstowe w komunikatach logów. |

## Tabela logów

| Kolumna | Opis |
|--------|-------------|
| **Timestamp** | Data i godzina wystąpienia zdarzenia. Z możliwością sortowania. |
| **Severity** | Kolorowa plakietka: Info (niebieska), Warning (żółta), Error (czerwona), Debug (szara). |
| **Component** | Usługa lub moduł, który wygenerował log (np. api, auth, api-service). |
| **Message** | Pełny komunikat logu ze szczegółami zdarzenia. |

Wyniki są podzielone na strony — użyj elementów sterujących na dole, aby przechodzić między stronami.

## Akcje w stopce

| Akcja | Opis |
|--------|-------------|
| **Auto-refresh** | Przełącznik automatycznego odświeżania widoku logów w regularnych odstępach. |
| **Refresh Now** | Ręczne odświeżenie danych logów. |
| **Export JSON** | Eksportuje bieżące przefiltrowane logi jako plik JSON. |
| **Download Logs** | Pobiera kompletne dane logów. |
