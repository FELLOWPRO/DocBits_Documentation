# Walidacja i testowanie

## Film: Zmienne, testy i aktywacja

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/pl.mp4" %}

[Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/pl.vtt) · 1:53

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

**Sprawdź wyniki**

Sprawdź komunikaty i czasy węzłów: zielony to sukces, pomarańczowy fałszywy warunek, czerwony błąd, szary pominięcie. Powtórz test po poprawkach. Menedżer testów zapewnia powtarzalne scenariusze: sukces, alternatywy, brak danych i błędy.

**Zapisz przed aktywacją**

Automatyczny zapis zachowuje lokalny szkic około trzydzieści sekund po zmianach. Zapisz jawnie na serwerze. Aktywacja wymaga pierwszego zapisu. Sprawdź stan włączenia na liście workflow, zanim oczekujesz automatycznego wykonania.

</details>

[Zobacz wszystkie pięć rozdziałów](../advanced-workflow-videos.md)

Podczas budowania Advanced Workflow dwa elementy sterujące na pasku narzędzi pozwalają sprawdzić go bez opuszczania kreatora. Służą one do *szybkich kontroli podczas budowania* — w przypadku zapisanych, powtarzalnych testów użyj [Test Managera](../test-manager.md).

## Validate

Kliknij element sterujący **Validate** (ikona okręgu z zaznaczeniem lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Walidacja sprawdza graf pod kątem problemów — niepołączonych węzłów, brakującej konfiguracji i nieprawidłowych połączeń — i wskazuje je, abyś mógł je naprawić, zanim przepływ pracy zostanie uruchomiony na rzeczywistych dokumentach.

## Test

Kliknij element sterujący **Test** (ikona odtwarzania lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), aby uruchomić bieżący przepływ na przykładowych danych i obserwować, jak się zachowuje, bez wpływu na rzeczywiste dokumenty. To najszybszy sposób na sprawdzenie poprawności zmiany, którą właśnie wprowadziłeś na kanwie.

## Kiedy czego używać

- **Validate / Test w kreatorze** (ta strona) — natychmiastowa informacja zwrotna podczas projektowania przepływu.
- **[Test Manager](../test-manager.md)** — zapisz scenariusz, aby móc go uruchomić ponownie później (i razem ze wszystkimi pozostałymi scenariuszami) w celu wykrycia regresji po przyszłych zmianach.

## Następne kroki

- Zapoznaj się z typami węzłów i połączeniami w [Węzły](nodes.md).
- Zobacz wszystkie elementy sterujące paska narzędzi i kanwy w [Pasek narzędzi i kanwa](toolbar-and-canvas.md).
