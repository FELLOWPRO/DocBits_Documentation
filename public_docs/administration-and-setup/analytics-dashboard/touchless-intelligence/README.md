# Touchless Intelligence

Touchless Intelligence odpowiada na dwa odrębne pytania: **Czy DocBits poprawnie odczytał fakturę?** Oraz: **Czy cały proces zakończył się bez ingerencji w przetwarzanie?** Poprawny odczyt może mimo to wymagać poprawki, gdy dane w Infor się różnią. AP oznacza ludzki zespół Accounts Payable.

## Film: funkcje raportu Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pl.mp4" %}

Ta wersja przeglądowa 3:57 pokazuje raport z danymi: filtry, KPI i obliczenia, trendy, pierwsze blokady, zarejestrowane dowody, historię dokumentu, porównanie uruchomień, wyuczone reguły, ulepszenia i historię, raporty doradcze oraz rzeczywiste wyniki MCP.

[Otwórz film z polskimi napisami i 16 rozdziałami](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pl.html). Ludzki przegląd odsłuchowy tej nowej wersji jest nadal w toku.

Te przypadki szkoleniowe wyjaśniają funkcje raportu. Rekomendacja ani podgląd nie dowodzą ani zastosowanego ustawienia, ani zmierzonej poprawy. Wyświetlana propozycja zmiany MCP nadal wymaga konkretnej konfiguracji docelowej; podgląd i zastosowanie są dla tej propozycji niedostępne. Niektóre natywne teksty produktu mogą zachować swój oryginalny język.

<figure><img src="../../../.gitbook/assets/anatomy-touchless-pl.svg" alt="Izometryczna linia sortująca: przenośnik z 14 bramkami, popychacz przekierowujący jeden dokument do tacy do sprawdzenia, pojemnik eksportowy ze stosem dokumentów i tarcza pokazująca 78,9 procent"><figcaption><p>Touchless jako linia sortująca, z liczbami z przykładowego obliczenia: 14 bramek to etapy Pipeline Path, arkusze wciąż na taśmie są w toku i nie są liczone, dokument, który zatrzymuje się przy bramce, jest spychany na tacę do sprawdzenia razem z dokumentami AP Assisted (30) i wyjątku procesu (10), a dokumenty czyste (120) i wymagające tylko zatwierdzenia (30) w pojemniku eksportowym dają 150 z 190, czyli 78,9 %, na tarczy powyżej znacznika celu 70 %.</p></figcaption></figure>

## Znajdź odpowiedni przewodnik

| Przewodnik | Co obejmuje |
| --- | --- |
| [Wskaźniki i obliczenia](touchless-metrics.md) | Kategorie wyników, licznik i mianownik, działania AP i obliczenia |
| [Korzystanie z panelu](touchless-dashboard.md) | Filtry, karty KPI, trendy, pierwsze blokady i elementy sterowania |
| [Przykłady: cena i ilość](touchless-examples.md) | Fikcyjne faktury i rzeczywiste widoki PO z Dev z różnicami ceny i ilości |
| [Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md) | Priorytetyzacja dostawców i powtarzających się przyczyn |
| [Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md) | Zrozumienie aktywnych reguł, tolerancji i przepływu decyzji |
| [Ślad dokumentu](touchless-document-trace.md) | Sprawdzanie oryginalnych wartości, uruchomień, blokad i interwencji |
| [Propozycje zmian i raporty](touchless-change-proposals.md) | Rozróżnianie podglądu, zastosowania, pomiaru efektu i wycofania |
| [Wyjaśnianie i poprawa Touchless przez MCP](touchless-mcp.md) | Wyjaśnianie, diagnozowanie i kontrolowane ulepszenia przez MCP |

<figure><img src="../../../.gitbook/assets/touchless-overview-pl.png" alt="Karta Touchless Intelligence z pięcioma kluczowymi wskaźnikami, sugestiami ulepszeń i wykresem wskaźnika touchless"><figcaption><p>Karta Touchless Intelligence: kluczowe wskaźniki, ulepszenia, wskaźnik w czasie i wykres pierwszej utraty. Przykładowa organizacja z danymi demonstracyjnymi; nazwy dostawców są fikcyjne.</p></figcaption></figure>

## Ustawienia raportu

Raport odczytuje cztery ustawienia organizacji, które administrator prowadzi w **Settings → Module → Dashboards &amp; Analytics**. Określają one cel i widok kosztów; puste pole oznacza, że DocBits używa wartości domyślnej.

| Ustawienie | Wartość domyślna | Co kontroluje |
| --- | --- | --- |
| Touchless target | 70 % | Udział dokumentów, które powinny przejść bez ingerencji w przetwarzanie. Raport używa go jako znacznika celu na wykresie wskaźnika. |
| Minutes per AP intervention | 6 min | Czas, którego pracownik AP potrzebuje na poprawienie i zwolnienie jednego dokumentu. |
| Hourly cost | 40 | Koszt jednej godziny pracy AP w walucie podanej poniżej. |
| Currency | EUR | Waluta widoku kosztów, jako trzyliterowy kod ISO 4217, na przykład `EUR`, `CHF` lub `USD`. DocBits przechowuje kod wielkimi literami i odrzuca wartość, która nie jest kodem waluty, więc literówka nie trafi do raportu. |

API sprawdza zapisane wartości ponownie i używa wartości domyślnej dla wartości, z którą nie może pracować.

## Dostęp

Ten obszar należy do [Analytics Dashboard](..). Administratorzy mają dostęp; inni użytkownicy potrzebują odpowiedniego nadania dla swojej roli. Analiza AI, obsługiwane zmiany i raporty doradcze mogą wymagać uprawnień administratora.

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
