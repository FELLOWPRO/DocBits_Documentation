# Debug Collector

Debug Collector wykonuje pełną migawkę twojej sesji DocBits — aktywność sieci, błędy, środowisko przeglądarki i metryki wydajności — pakuje ją jako raport JSON i opcjonalnie otwiera zgłoszenie wsparcia bezpośrednio z tego samego okna.

## Jak otworzyć

Naciśnij <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> w Windows i Linux lub <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> w macOS. Okno Performance Report otwiera się natychmiast.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Okno Debug Collector"><figcaption><p>Okno Performance Report pokazuje zarejestrowaną migawkę i wbudowany formularz tworzenia zgłoszenia.</p></figcaption></figure>

## Co jest rejestrowane

* **Wywołania API** — ostatnie 60 wywołań REST i WebSocket, z czasami, kodami stanu i odwiedzonymi adresami URL. Wywołania trwające ponad dwie sekundy są oznaczane osobno.
* **Błędy** — niedawne błędy JavaScript i niewychwycone odrzucenia obietnic z konsoli przeglądarki.
* **Logi konsoli** — najnowsze komunikaty logów aplikacji.
* **Środowisko** — wersja przeglądarki, system operacyjny, rozmiar ekranu i aktywne flagi funkcji.
* **Kontekst użytkownika** — twoja rola, organizacja i strona, na której byłeś podczas tworzenia migawki.
* **Metryki wydajności** — czasy ładowania strony (LCP, FCP), użycie pamięci i rozmiar DOM.
* **Trace ID** — identyfikatory korelacji łączące migawkę z logami backendu.

## Tworzenie zgłoszenia wsparcia z okna

Nie musisz niczego ręcznie pobierać ani załączać — okno zawiera wbudowany formularz **Create Support Ticket**.

1. Wpisz swój email, zostaw sugerowany temat lub go zmień, wybierz priorytet i dodaj notatki opisujące, co robiłeś, gdy wystąpił problem.
2. Kliknij **Send Report**. Migawka JSON jest dołączana, a zgłoszenie tworzone w jednym kroku.

Gotowe — wsparcie otrzymuje zgłoszenie ze wszystkimi danymi potrzebnymi do odtworzenia sytuacji.

Jeśli chcesz mieć lokalną kopię migawki, użyj **Copy Debug Data**, aby skopiować JSON do schowka, lub funkcji Zapisz jako przeglądarki, aby zachować raport jako plik `.json`.

## Prywatność i obsługa danych

* Tokeny uwierzytelniania i wrażliwe nagłówki są usuwane z zarejestrowanych wywołań API przed zbudowaniem migawki.
* Nic nie opuszcza przeglądarki, dopóki nie klikniesz **Send Report** — skrót jedynie otwiera okno.

<mark>Przejrzyj migawkę przed wysłaniem, jeśli pracowałeś z dokumentami zawierającymi dane klientów. Identyfikatory dokumentów widoczne w adresach URL pojawią się w raporcie.</mark>
