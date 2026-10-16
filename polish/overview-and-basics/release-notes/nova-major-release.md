# NOVA – Wydanie główne 4 listopada 2026 r.

**Dostępność NOVA R1.1:** Wersja jest dostępna w środowisku testowym od **16 października 2026 r.** Wydanie produkcyjne jest planowane na **4 listopada 2026 r.**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/pl.mp4" %}

**DocBits to produkt. NOVA to nazwa cyklu wydań.** [Obejrzyj film o nowym wydaniu DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/pl.mp4) · [Napisy](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/pl.vtt).

**Wersje usług w środowisku testowym: stan na 16 października 2026 r.**

NOVA obejmuje wszystkie funkcje wcześniej dostępne w VESTA w wersji beta jako funkcje standardowe, a także prowadzoną walidację dokumentów, więcej sposobów na usprawnienie automatyzacji, czytelniejsze kontrole faktur elektronicznych oraz lepszą kontrolę nad importem i przetwarzaniem dokumentów. Niniejsze notatki opisują zmiany widoczne dla klienta w wymienionych poniżej wersjach usługi w porównaniu z ostatnim opublikowanym [hotfixem VESTA, R1.0.15 z 14 października 2026 r.](incremental-updates-14-october-2026.md), w tym wcześniejszymi hotfixami VESTA.

Zrzut wskazuje kompilacje objęte niniejszymi notatkami. Informacje dotyczące dostępności w środowisku testowym lub produkcyjnym oraz przełączania między kanałami znajdują się w dokumencie [Cykl życia wydań DocBits](../docbits-release-lifecycle-strategy.md). Funkcje wymagające włączania na poziomie organizacji lub typu dokumentu muszą zostać aktywowane przez administratora.

## Wcześniejsze funkcje beta VESTA: włączone do NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Wszystkie funkcje dostępne wcześniej w wersji beta VESTA są zawarte jako funkcje standardowe w środowisku testowym NOVA.** Dla klientów, którzy nie korzystali z bety VESTA, oznacza to poszerzenie funkcjonalności dostępnych dla ich zespołu, w tym **Zarządzanie układami**, [**Niestandardowe reguły walidacji**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) oraz [**Zasady transformacji**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Ustawienia organizacji, przełączniki typów dokumentów oraz uprawnienia dostępu pozostają bez zmian.

Te same wcześniejsze funkcje beta staną się standardowymi funkcjami VESTA wraz z **następnym hotfixem VESTA, planowanym na [11 listopada 2026 r.](vesta-hotfix-11-november-2026.md)**. Niniejsze ogłoszenie dotyczy wcześniejszych funkcji beta VESTA; sekcje poniżej opisują również dodatkowe nowości i ulepszenia w NOVA.

## Co NOVA oferuje klientom <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

Poniższe porównanie obejmuje nowo dostępne wcześniejsze funkcje beta, nowe możliwości oraz rozszerzenia istniejących funkcji. Wersja bazowa VESTA zawiera funkcjonalność dostępną wyłącznie w wersji beta; jej włączenie do standardowego zestawu funkcji NOVA stanowi zmianę w wydaniu widoczną dla klienta.

| Możliwość | Wersja bazowa VESTA (w tym beta) | Co zyskują klienci dzięki NOVA |
| --- | --- | --- |
| **Korzystanie z wcześniejszych funkcji beta** | Funkcje dostępne przez betę VESTA | **Standardowe funkcje NOVA:** wszystkie wcześniejsze funkcje beta VESTA są włączone. Ich wdrożenie jako standardowych funkcji VESTA planowane jest w hotfixie z 11 listopada 2026 r. |
| **Pomoc podczas walidacji dokumentu** | Asystent ustawień i Kontrola pól nagłówka | **Nowy Asystent walidacji:** identyfikuj blokujące pola, przechodź do odpowiedniej wartości, przeglądaj sugerowane poprawki i utrzymuj czat w osobnym oknie. |
| **Usprawnianie automatyzacji na podstawie codziennych korekt** | Panel Touchless Intelligence, diagnostyka dostawców i propozycje zmian | **Nowy proces przeglądu i pomiaru:** przesyłaj wnioski o usprawnienia, przeglądaj propozycje wyuczonych reguł, sprawdzaj dowody na dokumentach, ranguj możliwości i mierz wyniki po aktywacji. |
| **Rozumienie i rozwiązywanie błędów faktur elektronicznych** | Kontrole dokumentów elektronicznych, katalog reguł i przeglądarka XML | **Rozszerzona Walidacja faktur elektronicznych:** raporty pogrupowane według poziomu walidacji, kontrola polityk i historia zmian, odrzucanie z poziomu raportu oraz inspekcja XML w obsługiwanych fakturach PDF. |
| **Kontrola importów FTP/SFTP** | Połączenia importowe oraz retencja lub archiwizacja plików źródłowych | **Nowa konfigurowana instalacja i kontrola:** kreator połączeń, logi krok po kroku, konfigurowalne ponowne próby i powiadomienia o błędach oraz usuwanie plików źródłowych po pomyślnym imporcie. |
| **Praca z regułami i układami** | Silniki reguł, logi wykonania i transformacje po wyszukiwaniu danych głównych; panele zarządzania wymagały linku beta | **Szerszy dostęp i lepsze narzędzia:** otwieraj panele zarządzania bezpośrednio, szukaj i podglądaj docelowe układy, otwieraj edytor układu dokumentu i rejestruj wykonanie wyboru układu. |
| **Działanie z poziomu Asystenta ustawień** | Czat ustawień, podgląd/potwierdzenie/cofnięcie i proaktywne ostrzeżenia o stanie importu | **Dodatkowe akcje:** zarządzaj błędnymi połączeniami, przeglądaj historię dezaktywacji, zmieniaj wybrane elementy konfiguracji, twórz nieaktywną regułę walidacji z katalogu i oglądaj wyjaśnienia na stronie. |
| **Kontrola przetwarzania dokumentów** | Limity stron organizacji i ponowne uruchamianie dokumentu | **Nowe opcje na poziomie dokumentu:** ponowne uruchomienie z wybraną liczbą stron, widok przetworzonych versus całkowitych stron oraz wybór, czy pola ukryte mają być ekstrahowane. |
| **Dopasowywanie złożonych dostaw** | Dopasowywanie zamówień i ręczne łączenie pozycji | **Elastyczniejsze dopasowywanie:** wybieraj pozycje w obu kierunkach, opcjonalnie zachowuj każdą dopasowaną podpozycję dokumentu i grupuj żądania eksportu według skonfigurowanych kolumn pozycji. |
| **Oddziel eksport od zakończonej pracy** | Istniejące przepływy pracy eksportu i Finished | **Nowe elementy sterujące stanem:** użyj Exported do dalszego przetwarzania, opcjonalnie zablokuj dokumenty Finished i znajdź dokumenty zatrzymane przez limit wykonania przepływu pracy. |

### Włącz funkcje wymagające konfiguracji

* **Asystent walidacji:** administrator organizacji włącza go w sekcji **Ustawienia → Informacje o firmie → Asystenci**. Jest on oddzielony od Asystenta ustawień i pozostaje wyłączony do momentu aktywacji.
* **Raporty przeglądu ulepszeń i konsultingowe:** wymagają uprawnień administratora organizacji oraz dostępu do Analytics. Wyuczone propozycje wymagają historii korekt; zmierzony wynik wymaga wystarczającej ilości danych oraz zakończenia okresu obserwacji.
* **Elementy sterujące regułami i układami:** przełączniki włączania dla poszczególnych typów dokumentów nadal obowiązują. NOVA udostępnia panele zarządzania bez konieczności korzystania z linku beta.
* **Opcjonalne zachowania przetwarzania:** skonfiguruj czyszczenie FTP i ponowne próby dla każdego połączenia. Rozszerzanie linii podrzędnych w relacji jeden-do-wielu oraz blokada gotowego dokumentu to ustawienia wymagające aktywacji (opt-in).

Aby uzyskać informacje dotyczące dostępności w Twoim środowisku oraz przełączania kanałów wydania, zapoznaj się z [cyklem życia wydania](../docbits-release-lifecycle-strategy.md).

## Obejrzyj filmy dotyczące funkcji <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Korzystaj z tych przewodników równolegle z notami wydania, aby zrozumieć powiązane funkcje i ich konfigurację. Filmy dostępne w języku polskim są podlinkowane poniżej; pozostałe filmy są wyraźnie oznaczone jako angielskie.

* [Wybór odpowiedniej automatyzacji — w tym miejsce Reguł dopasowywania zamówień](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/pl.mp4)
* [Zasady transformacji](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/pl.mp4)
* [Niestandardowe reguły walidacji (Film po angielsku)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4)
* [Układy i reguły selekcji (Film po angielsku)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4)
* [Touchless Intelligence](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/pl.mp4)
* [Walidacja e-faktur](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/pl.mp4)
* [Użytkownicy i dostęp administratora](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/pl.mp4)
* [Podorganizacje](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/pl.mp4)

### AI Table: sześć krótkich filmów

Te filmy są w języku angielskim. Obejrzyj całą serię lub wybierz interesujący Cię temat.

1. [Odczyt tabeli AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Popraw kolumnę i naucz DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Trzy typowe problemy](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Linie rabatowe, podatkowe i z zerową ilością](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Co AI już odczytuje poprawnie](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [Asystent i zakres możliwości zmian](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Aby zobaczyć zrzuty ekranu i szczegółowe instrukcje, zapoznaj się z [przewodnikiem po AI Table](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Asystent walidacji: pomoc przy bieżącym dokumencie

* **Znajdź przyczynę blokady postępu.** Zapytaj, dlaczego dokument nie może być dalej przetwarzany. Asystent identyfikuje dotknięte pola, wyjaśnia problem i oferuje przejście do konkretnego pola lub komórki tabeli. Wykorzystuje bieżący dokument oraz uprawnienia dostępu użytkownika.
* **Przejrzyj sugerowane korekty w kontekście.** Tam, gdzie jest to wspierane, recenzenci mogą zastosować proponowaną wartość pola lub tabeli, użyć kandydata z danych podstawowych, powtórzyć wyszukiwanie lub otworzyć odpowiedni ekran dopasowywania. Zmiany formularza podlegają zwykłemu procesowi przeglądu i zapisu dokumentu. Dokumenty tylko do odczytu oraz użytkownicy bez uprawnień do edycji nie otrzymują akcji edycji.
* **Zapytaj o dopasowywanie i księgowość.** Asystent może wyjaśnić kontekst zamówienia zakupu lub księgowości, gdy zostanie otwarty na tych ekranach. Zmiany w formularzu walidacji są wprowadzane na ekranie walidacji.
* **Zrozum ulepszenie przed jego zastosowaniem.** Wyjaśnienia łączą proponowaną regułę lub ustawienie z rzeczywistymi wartościami w dokumencie. Mogą zawierać diagram oraz narracyjne wyjaśnienie w języku użytkownika, jeśli jest dostępne. Sugestie są skupione wyłącznie na bieżącym dokumencie.
* **Pracuj z czatem w osobnym oknie.** Otwórz konwersację w nowym oknie podczas przeglądania dokumentu. Akcje zmieniające formularz pozostają w oknie dokumentu.
* **Zobacz więcej szczegółów dotyczących wyodrębnionych wartości.** Widok pochodzenia wartości dodaje szczegóły, takie jak rozróżnienie między OCR a warstwą tekstową PDF, dopasowanie reguł ekstrakcji oraz wyszukiwanie, które dostarczyło wartość. Wyjaśnienie tabeli AI dodaje bardziej praktyczne wskazówki dotyczące konfiguracji i czytelniejsze liczniki.

Administrator organizacji włącza Asystenta walidacji niezależnie od Asystenta ustawień w sekcji **Ustawienia → Informacje o firmie → Asystenci**.

## Przekształć powtarzalne korekty w ulepszenia automatyzacji

Istniejący pulpit [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) zyskuje proces przeglądu i monitorowania:

* **Propozycje wyuczonych reguł.** Powtarzające się ręczne korekty mogą sugerować [zasadę transformacji](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Administratorzy widzą, co reguła zapisze, przykłady ją wspierające oraz dokumenty, w których zastąpiłaby wartość zaakceptowaną przez zespół. Propozycja jest weryfikowana przed aktywacją reguły.
* **Zgłoszenia ulepszeń od recenzentów.** Użytkownicy mogą zgłaszać ulepszenia z poziomu asystenta dokumentu do przeglądu przez administratora w Touchless Intelligence. Zgłoszenie zachowuje swoje wyjaśnienie i decyzję w jednym miejscu.
* **Mierz efekty po aktywacji.** Dla obsługiwanych reguł transformacji DocBits porównuje ręczne korekty przed i po aktywacji oraz wyświetla wskaźnik bezobsługowości obok nich. Pomiar wykorzystuje 14-dniowe okresy i wskazuje niewystarczające dane zamiast wymyślać ulepszenie. Zmiana reguły rozpoczyna nowy pomiar dla tej rewizji.
* **Raport konsultingowy.** Administratorzy mogą generować uszeregowany widok możliwości ulepszeń w zakresie ekstrakcji, danych podstawowych, dopasowywania zamówień, księgowości, ustawień i przepływu przetwarzania. Szacowany wpływ jest oznaczony jako szacunek, dopóki nie zostanie zmierzony.
* **Doradztwo dotyczące dopasowania specyficznego dla dostawcy.** Powtarzające się problemy z dopasowaniem dostawców i pozycji mogą stanowić podstawę propozycji dotyczących tolerancji lub [reguł dopasowywania zamówień](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md). Doradztwo rozróżnia brakujące zamówienie od problemu z regułą lub tolerancją.
* **Podsumowania monitorowania.** Cotygodniowe podsumowanie dla administratora agreguje otwarte zgłoszenia ulepszeń, wiodące możliwości i zakończone pomiary, gdy jest coś do zgłoszenia. Zgłaszający mogą być powiadamiani, gdy dostępne są zmierzone wyniki.

## Asystent ustawień: dodatkowe akcje i wyjaśnienia stron

[Asystent ustawień](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), w tym proaktywne ostrzeżenia o kondycji e-mail/FTP, został już wydany w VESTA. NOVA dodaje akcje i kontekst do tego istniejącego doświadczenia:

* **Akcje dotyczące połączeń z powiadomienia o kondycji.** Otwórz dotknięte połączenie, przejrzyj dostępne działanie i potwierdź je z poziomu asystenta. Powiadomienia o kondycji mogą być również odrzucane. Podstawowe karty ostrzeżeń dla każdego kanału oraz ich informacje o błędach/ponownych próbach istnieją już w VESTA.
* **Widoczna historia dezaktywacji.** Tam, gdzie jest rejestrowana, wyłączony import pokazuje, kiedy został wyłączony i przez kogo.
* **Dodatkowe zweryfikowane akcje.** Administratorzy mogą podglądać i potwierdzać obsługiwane zmiany, takie jak aktywacja typów dokumentów, zmiana nazwy grupy, zmiana trybu wyszukiwania pola wyszukiwania, usunięcie pola lub utworzenie nieaktywnej niestandardowej reguły walidacji z katalogu.
* **Zarządzanie nieudolnymi połączeniami importu.** Obsługiwane karty mogą wyłączyć lub usunąć połączenie po potwierdzeniu. Odwracalne akcje oferują opcję cofnięcia; trwałe usunięcie jest odpowiednio oznaczone.
* **Wyjaśnienia stron.** Wybrane strony ustawień oferują filmy z napisami i transkrypcjami, w tym dotyczące układów, użytkowników, podorganizacji, zasad transformacji i walidacji e-faktur, jeśli dostępna jest wersja językowa.

## Reguły i układy: bezpośredni dostęp i lepsza diagnostyka

* **Byłe funkcje beta stają się standardowymi funkcjami.** Zarządzanie układami, [niestandardowe reguły walidacji](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) i [zasady transformacji](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) są widoczne w zaawansowanych ustawieniach typu dokumentu w NOVA bez linku beta. Ich przełączniki włączenia pozostają pod kontrolą administratora. Te elementy sterujące są uwzględnione w planowanej aktualizacji VESTA z 11 listopada 2026 r. wraz ze wszystkimi innymi byłymi funkcjami beta VESTA.
* **Bardziej użyteczna diagnostyka reguł.** Reguły wyboru układu zyskują opcję **Loguj wykonanie**. Wyszukiwanie reguł akceptuje identyfikatory reguł, a otwarcie edytora ładuje aktualnie zapisaną regułę. Istniejący log wykonania reguł pozostaje miejscem do przeglądania tego, co zostało uruchomione.
* **Wybieraj i otwieraj układy z większą ilością kontekstu.** Wyszukuj docelowe układy, podglądaj ich zawartość i otwieraj je bezpośrednio z reguły wyboru. Reguły wyboru zatwierdzania poprawnie akceptują obsługiwane typy układów zatwierdzania. Administratorzy otrzymują również skrót z walidacji dokumentu do edytora układu danego typu dokumentu.
* **Wybieraj wiele wartości warunków.** Warunki takie jak **jest jednym z** obsługują wiele wybranych wartości.
* **Szybciej znajdź pola wykrywania duplikatów.** Selektor pól w ustawieniach duplikatów dla typu dokumentu jest przeszukiwalny.

Transformacje po wyszukiwaniu danych podstawowych, podstawowy log wykonania reguł, szersze edytory reguł oraz poprawki klonowania reguł standardowych mają już implementacje w bazowej wersji VESTA. NOVA przenosi tę funkcjonalność i udostępnia dawne elementy sterujące zarządzania w wersji beta jako standardowe funkcje.

Aby zapoznać się z krokami konfiguracji, przykładami i testowaniem, zobacz [Niestandardowe reguły walidacji](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) oraz [Zasady transformacji](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Aby wybrać układ używany przez dokument, zobacz [Reguły wyboru układu](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## Walidacja e-faktur: czytelniejsze wyniki i kontrola polityk

* **Raport zorganizowany według poziomu walidacji.** Wyniki są grupowane w składnię, schemat, reguły biznesowe, reguły krzyżowe i reguły specyficzne dla kraju, z dodatkowymi grupami dla innych kontroli standardów i kontroli wartości. Komunikaty i podsumowania używają języka użytkownika, jeśli tłumaczenia są dostępne.
* **Bardziej kompletne kontrole i czytelniejsze wyniki.** Zaktualizowany walidator i raport rozróżniają błędy, ostrzeżenia i efektywną ważność po konfiguracji specyficznej dla organizacji. Strona nosi nazwę **Walidacja e-faktur**.
* **Polityki według typu dokumentu.** Administratorzy mogą sprawdzać, czy walidacja e-faktur jest włączona i czy błędy blokują przetwarzanie. Widok polityk identyfikuje nadpisania podtypów, a zmiany polityk są rejestrowane w historii zmian.
* **Inspekcja XML wewnątrz faktury PDF.** Przeglądarka XML może odczytywać osadzony XML w obsługiwanych plikach PDF ZUGFeRD/Factur-X, otwierać pozycję wskazaną przez wynik i wracać do dokumentu.
* **Odrzucanie z zapisaną przyczyną.** Autoryzowany recenzent może odrzucić kwalifikujący się dokument z raportu walidacji. Raport przygotowuje przyczynę na podstawie błędów do sprawdzenia przez recenzenta przed potwierdzeniem.
* **Dalsze poprawki formatów.** Faktury CII z narzędzia EDNA są rozpoznawane, a poprawki mapowania VAT dla XRechnung poprawiają sposób, w jaki istotne wartości faktur trafiają do pól DocBits.

Zobacz [Reguły walidacji dokumentów elektronicznych](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## Importy FTP/SFTP i e-mail

* **Konfiguracja FTP/SFTP z przewodnikiem.** Kreator połączeń oddziela szczegóły serwera, opcje importu i konfigurację. Testy połączeń i czytelniejsze błędy pomagają administratorom zidentyfikować nieprawidłowe połączenie lub brakujący folder źródłowy.
* **Logi importu według kroków.** Przeglądaj postęp pliku przez import FTP, w tym przesyłanie i skonfigurowaną akcję na pliku źródłowym.
* **Konfigurowalne zachowanie ponownych prób i powiadomień.** Ustaw interwał między późniejszymi ponownymi próbami, czas trwania ponownych prób i odbiorców powiadomień. Gdy okno ponownych prób zostanie wyczerpane, połączenie może zostać automatycznie wyłączone, a odbiorcy powiadomieni; kreator wyświetla powiadomienie o dezaktywacji.
* **Usuwanie po pomyślnym imporcie.** Oprócz zachowywania lub archiwizowania plików źródłowych, administratorzy mogą wybrać ich usunięcie z serwera FTP/SFTP po pomyślnym imporcie. Archiwizacja i usuwanie są odrębnymi alternatywami.
* **Bardziej niezawodne odzyskiwanie importu.** Nakładające się uruchomienia FTP są blokowane przed dwukrotnym przesyłaniem tego samego pliku źródłowego. Edycja połączenia zachowuje jego zapisane hasło, chyba że zostanie ono zastąpione. Obsługa e-maili nie oznacza wiadomości do usunięcia, gdy jej kopiowanie nie powiodło się.
* **Obsługa podpisanych e-maili.** Wiadomości S/MIME z podpisem opaque zawierające faktury mogą być rozpakowywane zamiast pomijane.
* **Historia i stan konfiguracji e-mail.** Ustawienia importu pokazują, kto ostatnio zapisał lub aktywował konfigurację. Przełącznik przychodzących e-maili odzwierciedla zapisany stan aktywny, w tym nowo zapisaną konfigurację.

Zobacz [Import FTP](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) oraz [Testowanie połączenia importu FTP](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Przetwarzanie i ekstrakcja dokumentów

* **Ponowne uruchomienie z wybraną liczbą stron.** Panel dodaje akcję ponownego uruchomienia, która pozwala recenzentom określić, ile stron przetworzyć dla danego dokumentu, w ramach jego faktycznej liczby stron.
* **Sprawdź limit przetwarzania.** Panel może wyświetlać liczbę przetworzonych stron w stosunku do całkowitej liczby stron dla dokumentu z ograniczeniem. Ustawienie **Liczba stron do przetworzenia** organizacji jest zgrupowane w sekcji Przetwarzanie dokumentów w module **Klasyfikuj i ekstrakcja**.
* **Kontroluj ekstrakcję pól ukrytych.** Administratorzy mogą decydować, czy pola ukryte biorą udział w ekstrakcji, za pomocą ustawienia **Ekstrahuj pola ukryte**.
* **Szybsza praca na większych partiach.** Wprowadzono ulepszenia wydajności dla masowych ponownych uruchomień dokumentów, importów danych podstawowych z plików CSV, przetwarzania plików PDF oraz ekstrakcji pól opartej na regułach.
* **Bardziej odporna ekstrakcja AI.** Przekroczenia limitu czasu są raportowane jako przekroczenia limitu czasu, a awarie obsługiwanych modeli mogą skutkować przełączeniem na inny dostępny model. Dodatkowe poprawki dotyczą powtarzających się kluczy w wynikach AI, skonfigurowanych synonimów pól oraz pustych zapisanych definicji tabel.
* **Zachowaj właśnie wprowadzoną wartość.** Zapisanie komórki tabeli bez uprzedniego kliknięcia w inne miejsce zachowuje wprowadzoną wartość. Daty z nazwami miesięcy rozpoznanymi błędnie przez OCR są obsługiwane w sposób bardziej niezawodny.

## Dopasowywanie zamówień, zatwierdzanie i eksport

[Przewodnik po regułach dopasowywania zamówień](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) wyjaśnia, jak włączyć dopasowywanie oparte na regułach, skonfigurować typy dopasowania i tolerancje, ustawić kolejność wykonania oraz zarządzać wersjami reguł.

* **Dopasowuj w obu kierunkach.** Wybierz pozycje dokumentu i połącz je z pozycjami zamówienia, lub zacznij od pozycji zamówienia. Jest to przydatne, gdy wiele pozycji noty dostawy odnosi się do jednej pozycji zamówienia.
* **Zachowaj szczegóły dopasowania jeden-do-wielu.** Konfiguracja dopasowania może teraz zachować indywidualną podpozycję dla każdej pozycji dokumentu, gdy wiele pozycji pasuje do jednej pozycji zamówienia. Ta opcja jest domyślnie wyłączona. Eksport przez generyczne API może grupować żądania według skonfigurowanych kolumn pozycji, wspierając dostawy lub kontenery wymagające osobnych rekordów docelowych.
* **Skonfiguruj awaryjne dopasowanie ostatniej pozycji.** Organizacje mogą kontrolować, czy pozostałe pozycje dokumentu i zamówienia mogą być dopasowane przez awaryjne dopasowanie pojedynczej pozycji.
* **Bardziej dokładne dopasowanie i wyświetlanie.** Poprawki zapewniają zachowanie prawidłowej podstawy cenowej dla dopasowań przeliczonych na opakowania, dziedziczenie statusu pozycji zamówienia w wierszach harmonogramu oraz wyświetlanie ilości przyjętych z pozycji przyjęcia.
* **Zapobiegaj przedwczesnemu zatwierdzaniu i duplikowaniu pracy.** Ostateczne zatwierdzenie jest blokowane, gdy nierozpatrzone rozbieżności dotyczące zamówienia pozostają niezatwierdzone. Powtórne wykonanie przepływu pracy nie tworzy kolejnego otwartego zadania dla tej samej grupy, a kontrole duplikatów eksportu są wykonywane przed zatwierdzeniem.
* **Oddziel Exported od Finished.** Akcje eksportu mogą wybrać status po pomyślnym eksporcie. **Exported** ma własną odznakę na panelu. Organizacje, które włączą blokadę dokumentów zakończonych, zapobiegają ponownemu otwieraniu zakończonych dokumentów przez zwykłe przepływy pracy lub ponowne uruchomienia; autoryzowane nadpisania są rejestrowane.
* **Łatwiejsze rozwiązywanie problemów z przepływem pracy.** Filtr na panelu pozwala znaleźć dokumenty zatrzymane przez limit wykonania przepływu pracy. Przebiegi przepływu pracy można przeglądać w oknie wyskakującym, a odrzucona zmiana statusu wskazuje nazwę statusu dokumentu.
* **Dodatkowe poprawki eksportu.** Dostosowano walidację M3 i ponowne próby zatwierdzania, a warunkowe konfiguracje eksportu dostawców są obsługiwane poprawnie.

## Codzienna użyteczność i dostęp

* **Bardziej niezawodna nawigacja.** Zaktualizowane adresy dokumentów mają przekierowania dla starszych linków. Głębokie linki NOVA zachowują zamierzony kanał podczas logowania, a postęp ładowania pokazuje, która część strony jest przygotowywana.
* **Osobiste preferencje pracy.** Kolejność kolumn zamówienia jest zapisywana dla każdego użytkownika, a ekran zatwierdzania pamięta otwarty panel boczny użytkownika.
* **Bardziej niezawodne widoki zadań i panelu.** Zadania bez przypisanej osoby mogą być wyświetlane, otwierane i przypisywane. Tablica zadań przeładowuje się, gdy wybrana organizacja jest gotowa, niestandardowe zakresy dat na panelu są stosowane poprawnie, a duplikaty wierszy dokumentów są unikane.
* **Lepsze etykiety i logi.** Administratorzy mogą edytować klucze tłumaczeń pól i kolumn tabel. Kolumny logów dokumentów można zmieniać rozmiarowo, niestandardowe kolumny panelu obsługują identyfikatory pól z wielkimi i małymi literami, a długie etykiety i nazwy plików mieszczą się bardziej spójnie.
* **Zakres powiadomień.** Reguły e-mailowe dotyczące statusu dokumentów mogą być ograniczone do podorganizacji.
* **Wdrożenie dostawców.** Magiczne linki do rejestracji w Portalu Dostawców pozostają ważne przez **21 dni zamiast 7 dni**. Administratorzy mogą również skonfigurować nagłówek błędu przesyłania dla pola pliku w układzie dostawcy.
* **Niezawodność logowania.** Logowanie SAML nie wykorzystuje już wygasłych ani unieważnionych sesji. Logowanie zarządcze obsługuje wymagany krok MFA, a nieaktywne członkostwa nie mogą otrzymać nowego zaproszenia do ustawienia hasła.
* **Obrazy w Tablicy Pomysłów.** Przesłane obrazy są przechowywane i udostępniane osobno od opisu pomysłu, co usprawnia obsługę obrazów.
* **Kontrolowane przełączanie kanałów.** Ustawienie Kanału wydania może być ustawione jako tylko do odczytu, jeśli przełączanie nie jest włączone dla danego środowiska. Dostępność zależy od ogłoszenia wydania.

## Połączeni asystenci i narzędzia integracyjne

Dla organizacji i partnerów korzystających z integracji DocBits MCP, NOVA dodaje narzędzia do wyświetlania listy rozwiązanych reguł walidacji, testowania jednej reguły na dokumencie bez zapisywania zmian oraz wyjaśniania przechowywanych dowodów wykonania reguł. Połączeni asystenci mogą również wyświetlać listę wniosków o ulepszenia i przesyłać zatwierdzenie autoryzowane przez administratora za pośrednictwem tego samego procesu przeglądu co aplikacja internetowa. Obowiązują istniejące uprawnienia organizacji i dokumentów.

## Funkcje już dostępne w VESTA

NOVA przenosi również poniższe funkcje. Tam, gdzie dostęp był wcześniej ograniczony do wersji beta VESTA, standardowa dostępność jest częścią tego wydania NOVA i jest planowana dla poprawki VESTA w dniu 11 listopada 2026 r. Lista opisuje wcześniejsze funkcje, wraz ze zmianami dostępności i ulepszeniami wyjaśnionymi powyżej:

* Oryginalny Asystent ustawień, jego wyszukiwarka dokumentacji, podstawowy przepływ podglądu/potwierdzenia/cofnięcia oraz proaktywne ostrzeżenia dotyczące zdrowia importu e-mail/FTP.
* Warstwy AI Fast, Full, Nexus i Auto oraz ustawienie trybu wizji.
* Kontrola pól nagłówka i oryginalny raport pochodzenia wartości.
* Pierwsze wydanie Touchless Intelligence, diagnoza dostawcy, analiza zbiorcza i diagram decyzji zamówienia zakupu.
* Podstawowe silniki reguł walidacji, transformacji i wyboru układu, transformacje po wyszukiwaniu danych głównych oraz podstawowy log wykonania reguł.
* Wcześniejsze ulepszenia wyszukiwania w panelu, MFA, zweryfikowane domeny e-mail organizacji, tolerancja opłat i zwiększenie limitu wykonania przepływu pracy do 50.

Zobacz [poprawkę VESTA z 14 października](incremental-updates-14-october-2026.md), [poprawkę z 15 września](incremental-updates-15-september-2026.md) i [wcześniejsze notatki wydania](README.md#vesta-hotfix-releases) dla historii wydań VESTA.

## Wersje usługi NOVA

Są to wersje i znaczniki czasu wdrożenia **kompilacji NOVA dostępnej w środowisku testowym od 16 października 2026 r.** Wydanie produkcyjne jest planowane na **4 listopada 2026 r.**; ten stan środowiska testowego nie określa ostatecznych wersji produkcyjnych. Znaczniki czasu dotyczą wdrożeń poszczególnych usług.

| Usługa | Wersja | Znacznik czasu wdrożenia |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Numery wersji postępują niezależnie na dwóch kanałach. Większa liczba nie oznacza sama w sobie, że usługa ma nową funkcję dla klienta. Zweryfikowane zmiany w Auto Accounting, Barcode, Docnet, Fulltext, OCR i Operator to zmiany konserwacyjne lub dotyczące niezawodności przetwarzania; nie wprowadzają one osobnego przepływu pracy dla klienta w tym porównaniu. Aktualizacje Auth Bridge poprawiają niezawodność synchronizacji kont między regionami.
