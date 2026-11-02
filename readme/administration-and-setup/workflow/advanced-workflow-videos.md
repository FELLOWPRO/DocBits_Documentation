---
description: "Pięć rozdziałów po polsku o zaawansowanych workflow i dziennikach, z napisami oraz transkrypcjami."
---

# Filmy Advanced Workflow

Wszystkie pięć rozdziałów zawiera polską narrację, plik napisów i transkrypcję. Pierwszy pokazuje tworzenie przykładowego workflow krok po kroku; kolejne rozwijają poszczególne tematy.

Pierwsze trzy rozdziały pokazują rzeczywisty edytor DocBits ze szkicami demonstracyjnymi. Wersja testowa wyszukiwania pokazuje rzeczywiste przetwarzanie dokumentów i elementy sterujące logami z pustymi wynikami. Rozdział diagnostyki nadal korzysta ze schematów oznaczonych jako ilustracje.

Każdy film zawiera napisy WebVTT i rozwijaną transkrypcję.

1. [Edytor i płótno](#builder-and-canvas) · 3:15
2. [Węzły i ścieżki](#nodes-and-routes) · 1:44
3. [Zmienne, testy i aktywacja](#variables-tests-and-activation) · 1:53
4. [Znajdź właściwe wykonanie](#find-the-relevant-execution) · 1:44
5. [Śledź węzły i diagnozuj](#trace-nodes-and-diagnose) · 1:45

## Edytor i płótno {#builder-and-canvas}

Poznaj Piotra i śledź jego wyjaśnienia w rzeczywistym polskim interfejsie DocBits. Sprawdza pulpit, listę workflow i licencję, a następnie otwiera niezapisany szkic w projektancie. Krok po kroku nadaje nazwę workflow, konfiguruje kontrolę kwoty oraz dwie akcje, rozmieszcza karty i łączy obie ścieżki. Następnie pokazuje przygotowanie testów z dokumentem lub własnymi danymi. Konto demonstracyjne nie ma subskrypcji Advanced Workflow i blokuje walidację; szkic pozostaje niezapisany i nieaktywny.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.vtt) · [Transkrypcja (tekst)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.txt) · 3:15

| W tym filmie | Początek |
| --- | --- |
| Poznaj administratora | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=0) |
| Sprawdź dostęp | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=4) |
| Nazwij workflow | [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=29) |
| Skonfiguruj kontrolę kwoty | [0:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=42) |
| Dodaj akcję Approval | [1:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=68) |
| Dodaj akcję Standard | [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=89) |
| Rozmieść karty | [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=109) |
| Połącz ścieżki | [2:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=124) |
| Przygotuj testy | [2:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=148) |
| Walidacja, zapis i aktywacja | [2:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=169) |

<details>
<summary>Transkrypcja</summary>

**Poznaj administratora**

Zarządzam DocBits. Zbudujemy kontrolę kwoty faktury.

**Sprawdź dostęp**

Zaczynam od pulpitu workflow i otwieram listę. Następnie sprawdzam licencję. Workflow i Advanced Workflow wymagają aktywnego dostępu. Po włączeniu obu uprawnień opcja Nowy workflow oferuje Advanced Workflow. To konto dokumentacyjne nie ma aktywnej licencji workflow. Dlatego pracuję dalej na niezapisanym podglądzie w projektancie.

**Nazwij workflow**

Pracuję w prawdziwym projektancie DocBits. Najpierw nadaję wersji roboczej czytelną nazwę. Sprawdzimy kwotę faktury i pokażemy dwie możliwe ścieżki za pomocą prostych akcji. Ta demonstracja pozostanie niezapisana.

**Skonfiguruj kontrolę kwoty**

Otwieram menu dodawania i wybieram kartę warunku. W kategorii Pole dokumentu wybieram warunek Docfield. Wpisuję pole total_amount. Następnie wybieram porównanie większe niż. I wpisuję tysiąc. Użyjcie klucza pola ze swojego dokumentu. Kwota równa dokładnie tysiąc nie spełnia tego porównania.

**Dodaj akcję Approval**

Teraz dodaję kartę akcji z kategorii Pole dokumentu. Akcja ustawia wartość pola dokumentu. Używam przykładowego klucza approval_route. I wpisuję wartość Approval. To oznacza ścieżkę. Rzeczywisty proces zatwierdzania wymaga odpowiednich akcji biznesowych.

**Dodaj akcję Standard**

Dodaję drugą kartę z tą samą akcją. Akcja ustawia wartość pola dokumentu. Używam przykładowego klucza approval_route. Tym razem przykładowe pole otrzymuje wartość Standard. Obie karty są skonfigurowane. Potrzebują jeszcze połączeń, które określą wykonywaną akcję.

**Rozmieść karty**

Przeciągam karty, aby układ był czytelny. Obie akcje umieszczam po prawej stronie. Warunek znajduje się pośrodku, a Start po lewej. Przeniesienie karty zmienia jej położenie. Nie tworzy połączenia.

**Połącz ścieżki**

Przeciągam od wyjścia Start do wejścia warunku. Ścieżka sukcesu prowadzi do Approval przez niebieskie połączenie. Pomarańczowa ścieżka niespełnionego warunku prowadzi do Standard. Czerwone wyjście błędu jest osobnym wyjściem dla błędów oceny. Tutaj pozostaje niepołączone. W produkcyjnym workflow ustalcie sposób obsługi takich błędów.

**Przygotuj testy**

Przycisk testu na pasku otwiera wybór dokumentu testowego. Mogę wybrać dokument demonstracyjny albo przygotować kompletne dane niestandardowe. Przetestujcie kwoty większe, mniejsze i równe tysiąc. Sprawdźcie też brakującą kwotę. To konto nie ma licencji Advanced Workflow. Pokazuję przygotowanie testu, a nie wykonany wynik.

**Walidacja, zapis i aktywacja**

Walidacja sprawdza połączenia i ustawienia kart. Tutaj brak licencji blokuje walidację. Na koncie z dostępem zapisałbym workflow bezpośrednio na serwerze. Następnie osobno sprawdziłbym aktywację. Przed pierwszym zapisem przełącznik jest wyłączony. Wskaźnik automatycznego szkicu dotyczy lokalnej kopii w przeglądarce. Nie oznacza, że workflow jest zapisany lub aktywny.

</details>

## Węzły i ścieżki {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pl.vtt) · 1:44

<details>
<summary>Transkrypcja</summary>

**Rola każdego węzła**

Start uruchamia ręcznie. When definiuje zdarzenie. Oba nie przyjmują połączeń wejściowych. And sprawdza warunek. Then wykonuje akcję. Oba edytory korzystają z tego samego katalogu kart. Notatki wyjaśniają projekt i nie są wykonywane.

**Trzy różne wyniki**

Przeciągnij wyjście do następnego wejścia. W edytorze niebieski oznacza sukces, pomarańczowy fałszywy warunek, czerwony błąd. And ma trzy wyniki; Then sukces i błąd. Widok wykonania oznacza sukces kolorem zielonym.

**Utwórz alternatywną ścieżkę**

Sprawdź, czy kwota faktury przekracza próg. Połącz niebieski z akceptacją, pomarańczowy ze zwykłą obsługą, czerwony z obsługą błędów. Fałszywy warunek może kontynuować połączoną ścieżką; nie zatrzymuje wszystkich gałęzi.

**Łączenie przez Wait ALL**

Wait ALL łączy gałęzie. Każdy węzeł źródłowy musi wybrać ścieżkę połączoną z bramką. Połącz oba wymagane sprawdzenia i następną akcję. Niewybrana ścieżka nie dostarcza wymaganego wyniku.

**Alternatywy ANY i OR**

Wait ANY i OR łączą gałęzie, gdy co najmniej jedno źródło wybierze połączoną ścieżkę. OR wymaga dwóch różnych węzłów źródłowych. Bramki nie tworzą wykluczających się wyborów ani nie anulują innych akcji. Przetestuj cały graf.

**Graf gotowy do wykonania**

Węzły muszą być osiągalne od wejścia. Unikaj cykli i połączeń wejściowych do Start lub When. Dodaj akcję Then i sprawdź ścieżki. Importowane węzły Delay wymagają dodatniego czasu; menu dodawania nie oferuje Delay.

</details>

## Zmienne, testy i aktywacja {#variables-tests-and-activation}

Śledź połączony workflow faktur w rzeczywistym edytorze DocBits. Otwórz Zmienne, porównaj typy i odwołanie do dokumentu, znajdź walidację, przygotuj testy z dokumentem lub danymi niestandardowymi oraz zobacz zapis i aktywację. Sceny testowe pokazują konfigurację przykładowych danych; nie przedstawiają wykonanego wyniku testu.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.vtt) · 1:56

<details>
<summary>Transkrypcja</summary>

**Wybierz typ zmiennej**

Otwórz zmienne ikoną nawiasów klamrowych. Wybierz tekst, liczbę, tak lub nie albo dokument. Szukaj według nazwy. Zmienna Document przechowuje odwołanie ustawiane dedykowaną akcją; formularz nie przyjmuje wartości dokumentu.

**Zmienne organizacji**

Wybierz unikalną nazwę, typ i wartość początkową. Tworzenie, edycja i usuwanie zmiennych zapisują się natychmiast dla organizacji. Inne workflow mogą je współdzielić. Zapisanie lub odrzucenie płótna nie cofa zmian zmiennych.

**Najpierw sprawdź strukturę**

Wybierz walidację. Przejrzyj błędy i ostrzeżenia nad płótnem. Kliknij komunikat, aby przejść do węzła. Sprawdź akcje, wejścia, wyjścia, cykle i połączenia gałęzi. Poprawna struktura nie gwarantuje poprawności danych wykonania.

**Wybierz kontekst testu**

Odtwarzanie na pasku otwiera wybór dokumentu. Użyj dokumentu, danych niestandardowych lub testu bez dokumentu dla niezależnych kart. Odtwarzanie na Start uruchamia bezpośrednio. Test obejmuje bieżące płótno z niezapisanymi zmianami i symuluje działania destrukcyjne.

**Przygotowanie i sprawdzanie scenariuszy testowych**

Przygotuj oddzielne testy dla kwot powyżej, poniżej i równych tysiąc oraz brakujących danych. Po uruchomieniu sprawdź komunikaty i czasy: zielony oznacza sukces, pomarańczowy fałsz, czerwony błąd, szary pominięcie. Ponownie przetestuj poprawki. Menedżer testów pozwala powtarzać scenariusze.

**Zapisz przed aktywacją**

Automatyczny zapis zachowuje lokalny szkic około trzydzieści sekund po zmianach. Zapisz jawnie na serwerze. Aktywacja wymaga pierwszego zapisu. Sprawdź stan włączenia na liście workflow, zanim oczekujesz automatycznego wykonania.

</details>

## Znajdź właściwe wykonanie {#find-the-relevant-execution}

{% hint style="info" %}
Wersja testowa: rzeczywiste ekrany DocBits z akcjami dokumentu, przepływem dokumentów, czasami kroków, pustymi logami oraz filtrami statusu i daty. Dokument nie ma zapisanego wykonania Advanced Workflow. Ta wersja nie obejmuje jeszcze wierszy wykonań, stronicowania ani diagnostyki węzłów.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/pl.vtt) · 1:58

<details>
<summary>Transkrypcja</summary>

**Zacznij od dokumentu**

Na pulpicie dokumentów otwórz menu akcji i wybierz Przepływ dokumentów. Rzeczywista historia pokazuje import i OCR. Otwórz krok, aby sprawdzić czas oczekiwania i przetwarzania. Te kroki są odrębne od węzłów Advanced Workflow.

**Odczytaj rzeczywiste liczniki**

Tutaj widzisz logi workflow tego samego dokumentu. Niebieski oznacza liczbę wszystkich wykonań, czerwony błędy, żółty niespełnione warunki, a zielony sukcesy. Ten dokument demonstracyjny nie ma zapisanych wykonań. Dlatego wszystkie cztery liczniki pokazują zero.

**Sprawdź kolumny wykonań**

Tabela zawiera nazwę workflow, czas utworzenia, czas trwania i wynik. Rozróżniaj powtarzające się wykonania na podstawie znacznika czasu. W tej wersji testowej nie ma wiersza do otwarcia. Pusta lista sama w sobie nie dowodzi błędu wykonania.

**Otwórz filtry statusu**

Ikona filtrów otwiera rzeczywiste menu. Wybierz sortowanie według nazwy lub czasu utworzenia, rosnąco albo malejąco. Status oferuje sukces, niespełniony warunek i błąd. Na ekranie widzisz rzeczywisty interfejs DocBits.

**Wybierz daty i wyczyść filtry**

Wybierz okres za pomocą daty rozpoczęcia i zakończenia lub kalendarza. Format to rok, miesiąc i dzień. Przycisk zastosowania pobiera wyniki. Wyczyść filtry resetuje wybór. Wyszukiwanie wyczyść oddzielnie. W tej wersji nazwy miesięcy w kalendarzu pozostają angielskie.

**Podgląd: nadal brakuje zapisanego wykonania**

Ta wersja testowa pozwala sprawdzić dostęp do dokumentu, szczegóły przetwarzania i elementy sterujące logami. Nadal brakuje zapisanego wykonania Advanced Workflow, aby pokazać rzeczywiste wiersze, stronicowanie, ścieżki i komunikaty węzłów. Film nie symuluje tych wyników.

</details>

## Śledź węzły i diagnozuj {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/pl.vtt) · 1:45

<details>
<summary>Transkrypcja</summary>

**Rozwiń wykonanie**

Rozwiń wiersz workflow. Wykonanie zaawansowane pokazuje graf po lewej i komunikaty po prawej; standardowe pokazuje sekwencję kart. Dane opisują tamto wykonanie i mogą różnić się od bieżącego edytora.

**Wybierz węzeł**

Przesuń lub powiększ graf i kliknij węzeł. Card Logs pokazuje komunikaty. Wait ALL i Wait ANY także mogą zawierać komunikaty węzła. Odczytuj je wraz z wybranym węzłem i znacznikiem czasu wykonania.

**Rozróżnij wyniki**

Zielony oznacza sukces, pomarańczowy fałszywy warunek, czerwony błąd, szary pominięcie. Pominięty węzeł nie wykonał się. Przed zmianą sprawdź, czy wybrano inną gałąź albo zabrakło wymaganego wejścia do bramki.

**Znajdź pierwszą rozbieżność**

Śledź rzeczywistą ścieżkę od wejścia. Dla fałszywego warunku kwoty sprawdź pomarańczowy. Przy błędzie odczytaj komunikat i sprawdź czerwony. Obsługa błędu może się udać, choć całe wykonanie nadal zgłasza pierwotny błąd.

**Sprawdź łączenie gałęzi**

Dla Wait ALL sprawdź każde źródło i połączony wynik. Dla ANY lub OR znajdź pasujące źródło. Dwa wyjścia jednego węzła nie są niezależnymi akceptacjami. Pomarańczowy wynik warunku może być zamierzony.

**Popraw i sprawdź**

Zapisz nazwę workflow, odwołanie dokumentu, czas, węzeł i dokładny komunikat. Popraw konfigurację lub dane i przetestuj powtarzalny scenariusz. Zapisz i sprawdź aktywację. Porównaj nowe wykonanie ze starym; wcześniejsze dzienniki opisują wcześniejsze zachowanie.

</details>
