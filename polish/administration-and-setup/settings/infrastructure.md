# Infrastruktura

Strona **Infrastruktura** zapewnia administratorom bieżący wgląd w to, gdzie działa każdy element DocBits (UE lub USA), jak dokument przepływa przez system oraz czy przetwarzanie w tle jest sprawne. Strona jest tylko do odczytu — niczego się tu nie konfiguruje; odpowiada na pytanie: *„czy wszystko działa i czy moje dane pozostają w mojym regionie?"*

> **Dostęp:** Infrastruktura to strona wyłącznie dla administratorów. Otwórz **Ustawienia → Organizacja i Dostęp → Infrastruktura**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Strona Infrastruktura z otwartą kartą Topologia"><figcaption><p>Strona Infrastruktura, karta Topologia</p></figcaption></figure>

Strona jest podzielona na trzy karty:

| Karta | Odpowiada na |
|-------|--------------|
| **Topologia** | Gdzie działa każdy komponent i czy wszystko jest w moim regionie? |
| **Przetwarzanie** | Czy etapy przetwarzania (OCR, ekstrakcja, dopasowanie PO …) działają i są aktualne? |
| **Zaplanowane zadania** | Czy cykliczne zadania w tle są wykonywane zgodnie z harmonogramem? |

## Topologia

Karta Topologia przedstawia całą platformę DocBits w postaci diagramu, pogrupowanego w warstwy — **Edge / Web**, **Core API**, **Import**, **Usługi w tle**, **Magazyny danych** oraz **Uwierzytelnianie**. Każde pole to jeden komponent (aplikacja webowa/CDN, brama API, worker OCR, baza danych itd.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Diagram topologii z odznakami regionu"><figcaption><p>Każdy komponent jest oznaczony regionem, w którym działa</p></figcaption></figure>

### Przejrzystość regionu

Każdy komponent ma odznakę regionu, dzięki czemu możesz jednym rzutem oka potwierdzić miejsce przechowywania danych:

| Odznaka | Znaczenie |
|---------|-----------|
| **UE ✓** / **US ✓** | Komponent działa w regionie Twojej organizacji. |
| **SHARED** | Komponent globalny (np. CDN) bez jednego regionu — jest to oczekiwane i nie stanowi problemu. |
| **Niezgodność regionu** | Komponent działa w *innym* regionie niż Twoja organizacja. Jest podświetlony, abyś mógł zgłosić to do wsparcia. |

Baner u góry podsumowuje wynik: **„Wszystkie komponenty działają w Twoim regionie (UE)"**, gdy wszystko się zgadza, lub ostrzeżenie, jeśli któryś krytyczny komponent znajduje się w innym regionie.

### Architektura vs. Odtwórz proces

Użyj przełącznika nad diagramem, aby zmienić widok:

- **Architektura** — statyczna mapa wszystkich komponentów i ich połączeń.
- **Odtwórz proces** — animuje drogę dokumentu przez system, krok po kroku, dzięki czemu widzisz kolejność, w jakiej komponenty są zaangażowane.

Wskaźnik **● live** pokazuje, że informacje o stanie na diagramie odzwierciedlają bieżący stan systemu.

### Moduły opcjonalne

Komponenty należące do modułu opcjonalnego (Wyszukiwanie pełnotekstowe, DocFlow, Auto-Accounting, DocNet, Dopasowanie PO) wyświetlają odznakę **aktywny** lub **nieaktywny**. Kliknięcie nieaktywnego modułu przenosi Cię bezpośrednio na stronę, na której możesz go włączyć — **Ustawienia → Moduł** dla większości modułów lub **Typy dokumentów** dla Dopasowania PO (które jest włączane dla każdego typu dokumentu).

## Przetwarzanie

Karta Przetwarzanie pokazuje potok przetwarzania dokumentów dla **Twojej organizacji** — kiedy każdy etap był ostatnio uruchomiony i czy praca przebiega płynnie, czy się piętrzy.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tabela przetwarzania z odznakami stanu"><figcaption><p>Stan przetwarzania według etapu dla Twojej organizacji</p></figcaption></figure>

| Kolumna | Opis |
|---------|------|
| **Proces** | Etap przetwarzania — Przetwarzanie dokumentów, OCR, TR-OCR, Podział po kodzie kreskowym, Ekstrakcja kodu kreskowego, Ekstrakcja, Dopasowanie PO. |
| **Ostatnie uruchomienie** | Jak dawno temu etap był uruchomiony. Najedź kursorem, aby zobaczyć dokładny znacznik czasu. *„Nigdy nie uruchomiono"* oznacza, że żaden dokument nie dotarł jeszcze do tego etapu. |
| **Stan** | Odznaka typu sygnalizacja świetlna (patrz niżej). |

Odznaki stanu:

| Odznaka | Znaczenie |
|---------|-----------|
| **OK** (zielony) | Brak ostatnich błędów i nic nie oczekuje — etap jest sprawny. |
| **W toku (N)** (bursztynowy) | `N` dokumentów jest obecnie przetwarzanych na tym etapie. |
| **Błąd (N)** (czerwony) | `N` dokumentów ostatnio nie powiodło się na tym etapie. |

Błędy i *w toku* to niezależne sygnały, więc etap może pokazywać obie odznaki naraz — dzięki temu widzisz błąd nawet wtedy, gdy inna praca wciąż trwa. Użyj **Odśwież** (u góry po prawej), aby pobrać najnowsze wartości.

## Zaplanowane zadania

Karta Zaplanowane zadania zawiera listę cyklicznych zadań w tle, które utrzymują działanie DocBits (odświeżanie pamięci podręcznej, alerty stanu, limity czasu dokumentów, synchronizacje wychodzące i inne) oraz potwierdza, że każde z nich uruchamia się o czasie.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabela zaplanowanych zadań"><figcaption><p>Cykliczne zadania w tle i ich stan harmonogramu</p></figcaption></figure>

| Kolumna | Opis |
|---------|------|
| **Zadanie** | Nazwa zaplanowanego zadania. |
| **Ostatnie uruchomienie** | Jak dawno temu było uruchomione. Najedź kursorem, aby zobaczyć dokładny znacznik czasu; *„Nigdy nie uruchomiono"* oznacza, że jeszcze się nie uruchomiło. |
| **Stan** | Stan harmonogramu (patrz niżej). |

Wartości stanu:

| Odznaka | Znaczenie |
|---------|-----------|
| **Zgodnie z harmonogramem** (zielony) | Zadanie działa w oczekiwanym interwale. |
| **Opóźnione** (czerwony) | Zadanie nie zostało uruchomione zgodnie z oczekiwaniami — warto to zbadać lub zgłosić do wsparcia. |
| **Nieznany** (szary) | Nie udało się ustalić stanu harmonogramu. |

Użyj **Odśwież**, aby ponownie sprawdzić stan harmonogramu na żądanie.
