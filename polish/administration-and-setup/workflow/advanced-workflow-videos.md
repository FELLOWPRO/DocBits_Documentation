---
description: "Pięć rozdziałów po polsku o zaawansowanych workflow i dziennikach, z napisami oraz transkrypcjami."
---

# Filmy Advanced Workflow

Dowiedz się, jak tworzyć, testować i diagnozować zaawansowany workflow. Wszystkie pięć rozdziałów ma polską narrację.

Pierwsze trzy rozdziały pokazują prawdziwy interfejs DocBits. Dwa rozdziały o dziennikach korzystają ze schematów oznaczonych jako ilustracje. Zrzuty pokazują niezapisane szkice demonstracyjne.

Każdy film zawiera napisy WebVTT i rozwijaną transkrypcję.

1. [Edytor i płótno](#builder-and-canvas) · 1:44
2. [Węzły i ścieżki](#nodes-and-routes) · 1:44
3. [Zmienne, testy i aktywacja](#variables-tests-and-activation) · 1:53
4. [Znajdź właściwe wykonanie](#find-the-relevant-execution) · 1:44
5. [Śledź węzły i diagnozuj](#trace-nodes-and-diagnose) · 1:45

## Edytor i płótno {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.vtt) · 1:44

<details>
<summary>Transkrypcja</summary>

**Faktura z dwiema ścieżkami**

To prawdziwy zaawansowany workflow w DocBits. Sprawdzenie kwoty faktury prowadzi do dwóch działań. Połączenia określają, które działanie zostanie wykonane. Przykład wykorzystuje niezapisany szkic i pola demonstracyjne.

**Konfiguracja kontroli kwoty**

Otwórz Dodaj, wybierz And i warunek dotyczący pola dokumentu. Wskaż pole kwoty, wybierz Większe niż i wpisz tysiąc. Użyj dokładnego klucza pola z konfiguracji dokumentu.

**Konfiguracja działań**

Dodaj dwie karty Then. Obie ustawiają pole demonstracyjne approval route. Jedna wpisuje Approval, druga Standard. Wartości te oznaczają wybraną ścieżkę. W produkcyjnym workflow skonfiguruj właściwe działania biznesowe.

**Łączenie wyjść wyników**

Połącz Start z wejściem warunku. Niebieskie wyjście sukcesu połącz z Approval, a pomarańczowe wyjście fałszywego warunku ze Standard. Czerwone wyjście obsługuje osobno błędy oceny. Samo położenie kart nie tworzy ścieżki.

**Przygotowanie testów**

Otwórz Test na pasku narzędzi. Wybierz dokument testowy lub wprowadź jego pełne dane w formacie JSON. Sprawdź kwoty powyżej, poniżej i równe tysiąc oraz brakujące wartości. Po wykonaniu przejrzyj wyniki węzłów.

**Walidacja, zapis i aktywacja**

Zweryfikuj połączenia i ustawienia kart. Zapisz workflow na serwerze, a następnie osobno sprawdź aktywację. Automatyczne szkice przeglądarki nie zastępują zapisu. Wykonywanie i dostęp do dzienników wymagają odpowiedniego modułu i subskrypcji.

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/pl.vtt) · 1:44

<details>
<summary>Transkrypcja</summary>

**Otwórz dzienniki dokumentu**

W panelu dokumentów wybierz Workflow Logs z menu akcji. Dostęp do workflow musi być włączony. Dzienniki dotyczą wybranego dokumentu. Testy edytora oraz dzienniki zdarzeń i aktywności organizacji są oddzielne.

**Odczytaj liczniki**

Niebieski liczy wykonania w bieżących wynikach, czerwony błędy, żółty fałszywe warunki, zielony sukcesy. Liczniki dotyczą wykonań, a nie definicji workflow ani węzłów. Filtry mogą zmienić te liczby.

**Wybierz dokładne wykonanie**

Każdy wiersz pokazuje nazwę workflow, datę utworzenia, czas w sekundach i wynik. Jeden workflow może wykonać się wielokrotnie dla dokumentu. Porównaj znaczniki czasu. Krótkie wykonanie może pokazać zero przecinek zero zero sekund po zaokrągleniu.

**Zawęź wyniki**

Wyszukaj workflow. Ikona ustawień otwiera kierunek i kryterium sortowania, status oraz daty początku i końca. Sortuj według nazwy lub utworzenia. Wpisuj daty w kolejności rok, miesiąc, dzień i zastosuj.

**Sprawdź strony i filtry**

Paginacja udostępnia starsze wyniki. Wyczyść filtry ponownie wczytuje listę bez ustawień. Osobno usuń tekst wyszukiwania. Przy pustych wynikach sprawdź dokument, daty i status. Pusta lista nie dowodzi błędu wykonania.

**Szczególne stany**

Baner i ikona blokady wskazują limit wykonań dokumentu. Zbadaj powtarzające się wyzwalacze przed zmianą limitów. Pobieranie filmu DocOperator pojawia się tylko przy istniejącym nagraniu; jest to nagranie tego wykonania.

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
