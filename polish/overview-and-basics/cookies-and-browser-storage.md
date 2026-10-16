# Pliki cookie i pamięć przeglądarki

Zweryfikowano **16 października 2026 r.** dla pytania **4.15**. Publiczna witryna, aplikacja DocBits i ta dokumentacja korzystają z różnych plików cookie i usług.

## Polityka i cele

[Polityka prywatności DocBits](https://docbits.com/en/privacy-policy/) zawiera sekcje **Cookies** i **Consent with Borlabs Cookie**. Opisuje zgody, niezbędne funkcje, ochronę przed botami, Google Analytics, reklamy i Leadfeeder. Analizy mogą tworzyć raporty o wizytach, stronach, interakcjach i wydajności; zbieranie danych nie ogranicza się do anonimowych danych zbiorczych. Polityka witryny sama nie określa listy plików cookie aplikacji.

## Lista plików cookie

**Zaobserwowano** oznacza nową wizytę bez logowania i bez wyboru opcjonalnych zgód. **Kod** oznacza sprawdzony kod lub ustawienia infrastruktury; nie potwierdza atrybutów każdej odpowiedzi produkcyjnej.

| Cookie / zakres | Cel i czas przechowywania | Dowód i atrybuty bezpieczeństwa |
| --- | --- | --- |
| `__cf_bm` / witryna i aplikacja | Ochrona Cloudflare przed botami; 30 minut bezczynności | Zaobserwowano: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) szyfruje informacje o botach z wyjątkiem danych czasowych. |
| `pll_language` / witryna | Preferowany język; około roku | Zaobserwowano: `Secure`, dostępny dla JavaScript, `SameSite=Lax`. |
| `_lfa` / witryna | Analizy odwiedzających i firm w Leadfeeder; około roku | Zaobserwowano: dostępny dla JavaScript, `SameSite=Lax`, **bez atrybutu `Secure`** podczas tej wizyty. |
| Cookie zgody Borlabs / witryna | Zapisuje zgody i ich wycofanie | Wskazany w polityce; nazwa, wdrożone atrybuty i czas nie zostały potwierdzone podczas wizyty. |
| `session` / uwierzytelnianie | Stan sesji w procesach uwierzytelniania | Domyślne wartości kodu: `Secure`, `HttpOnly`, `SameSite=None`; podpisane dane sesji Flask, bez szyfrowania. Ustawienia wdrożenia mogą je zmienić. |
| `dbx_td` / uwierzytelnianie | Zapamiętuje zaufane urządzenie, jeśli wybrano po poprawnej MFA; 30 dni | Kod: `Secure`, `HttpOnly`, `SameSite=None`; losowy token, którego skrót jest przechowywany na serwerze. |
| `prod-sticky` / produkcyjne równoważenie obciążenia | Kieruje żądania do tego samego backendu; ustawiony czas 300 sekund | Ustawienie infrastruktury potwierdzone; atrybuty przeglądarki niesprawdzone. |
| `dontAsk` / aplikacja | Zapamiętuje preferencję dotyczącą monitu; brak jawnego terminu w sprawdzonym wywołaniu | Kod: dostępny dla JavaScript; brak jawnych opcji `Secure` lub `SameSite` w tym wywołaniu. |

Podczas nowej wizyty w dokumentacji nie zaobserwowano plików cookie. To obserwacja z określonego dnia, nie pełna lista dla zalogowanych użytkowników, funkcji opcjonalnych lub treści zewnętrznych. Polityka wymienia dalsze usługi analityczne i reklamowe, których plików cookie ta wizyta nie potwierdziła. Pełna lista oraz kontrola stosowania zgód wymagają osobnego sprawdzenia tych procesów.

## Bezpieczeństwo i analityka

`Secure` ogranicza wysyłanie do HTTPS. `HttpOnly` uniemożliwia odczyt przez JavaScript. `SameSite` steruje wysyłaniem między witrynami. Atrybuty te nie szyfrują zawartości. Ogólne stwierdzenie, że wszystkie pliki cookie są szyfrowane lub jednakowo zabezpieczone, byłoby nieprawidłowe. Publiczne endpointy obsługują TLS 1.2 i 1.3; zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).

Pamięć przeglądarki jest wykorzystywana także niezależnie od cookie. Konfiguracja Grafana Faro obsługuje trwałe śledzenie sesji, błędy, pomiary wydajności i ślady, z identyfikatorami użytkownika i organizacji, jeśli są dostępne. Zbieranie zależy od wdrożonego kolektora. Nie należy opisywać go jako wyłącznie anonimowej, zbiorczej analityki cookie. Preferencje języka również korzystają z pamięci lokalnej.

Cookie i pamięć można usunąć w przeglądarce. Może to usunąć preferencje i zapamiętane zaufane urządzenia. Aktualna lista i pytania o prywatność: **compliance@fellowpro.com**.
