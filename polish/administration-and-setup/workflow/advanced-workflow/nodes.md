# Węzły

## Film: Węzły i ścieżki

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pl.mp4" %}

[Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pl.vtt) · 1:44

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

[Zobacz wszystkie pięć rozdziałów](../advanced-workflow-videos.md)

Zaawansowany Workflow to graf złożony z **węzłów** połączonych krawędziami. Węzły dodajesz z menu **+ Add** (lub klikając prawym przyciskiem myszy na kanwie) i łączysz je, aby zdefiniować przepływ wykonania.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu dodawania węzła z dostępnymi typami węzłów"><figcaption><p>Menu węzła <strong>+ Add</strong> — dostępne typy węzłów.</p></figcaption></figure>

## Typy węzłów

- **Start** — punkt wejścia workflow. Dodawany automatycznie; każdy przepływ rozpoczyna się tutaj.
- **When** — karta wyzwalacza, taka sama jak w kreatorze standardowym.
- **And** — karta warunku. Przyjmuje wartość prawda lub fałsz i może rozgałęziać przepływ.
- **Then** — karta akcji, która wykonuje pracę (ustawia pola, tworzy zadania, wywołuje API, …).
- **Wait ALL** — czeka, aż *wszystkie* przychodzące gałęzie zostaną ukończone, zanim przejdzie dalej.
- **Wait ANY** — kontynuuje, gdy tylko *którakolwiek* przychodząca gałąź zostanie ukończona.
- **OR** — rozgałęzia przepływ na alternatywne ścieżki.
- **Note** — dowolna adnotacja tekstowa na kanwie; nie wpływa na wykonanie.

Węzły **When / And / Then** korzystają z dokładnie tych samych kart, które opisano w sekcji [Karty](../cards-overview.md).

## Łączenie węzłów

Węzły są połączone **kolorowymi krawędziami**. Przeciągnij od uchwytu po **prawej** stronie węzła do uchwytu wejściowego po **lewej** stronie innego węzła, aby utworzyć połączenie. Każdy kolor oznacza inny wynik wykonania:

- **Success** (niebieski) — domyślna ścieżka wybierana, gdy węzeł zostanie pomyślnie ukończony. Dostępna dla wszystkich typów węzłów.
- **Failed Condition** (pomarańczowy) — wybierana, gdy warunek przyjmie wartość fałsz. Dostępna dla węzłów **And** (warunek).
- **Error** (czerwony) — wybierana, gdy węzeł napotka błąd podczas wykonania. Dostępna dla węzłów **And** oraz **Then** (akcja).

## Podświetlanie ścieżki wykonania

Kliknij dowolny węzeł, aby zobaczyć jego ścieżkę wykonania. Wszystkie węzły prowadzące do niego oraz wszystkie węzły następujące po nim zostają podświetlone — pozostałe są przyciemnione. W przypadku węzłów **Wait ALL** pokazywana jest każda przychodząca gałąź, dzięki czemu dokładnie widzisz, na co czeka bramka, zanim przejdzie dalej.

## Następne kroki

- Przekazuj dane między węzłami za pomocą [Zmiennych](variables.md).
- Sprawdź i uruchom przepływ w [Walidacji i Testowaniu](validation-and-testing.md).
