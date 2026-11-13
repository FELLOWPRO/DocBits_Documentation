# Walidacja i testowanie

## Film: Zmienne, testy i aktywacja

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

[Zobacz wszystkie pięć rozdziałów](../advanced-workflow-videos.md)

Podczas budowania Advanced Workflow dwa elementy sterujące na pasku narzędzi pozwalają sprawdzić go bez opuszczania kreatora. Służą one do *szybkich kontroli podczas budowania* — w przypadku zapisanych, powtarzalnych testów użyj [Test Managera](../test-manager.md).

## Walidacja

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.mp4" %}

**Film:** Walidacja Workflow · 1:08 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Walidacja sprawdza budowę Workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.mp4#t=0.25)

Przed zapisaniem kliknij Waliduj na pasku narzędzi. Sprawdza to budowę Workflow: czy uruchamia go karta Gdy, czy każda karta jest połączona i czy ścieżki mają sens. Problemy pojawiają się nad obszarem roboczym.

**Kliknij komunikat, aby znaleźć kartę** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.mp4#t=20.383)

Kliknij komunikat, aby przejść do jego karty. Tutaj karta przypisania nie jest połączona, więc nigdy by się nie wykonała. Połącz ją.

**Brak komunikatów: Workflow jest poprawny** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.mp4#t=35.183)

Sprawdź ponownie. Gdy nic nie zostanie, Workflow jest poprawny i możesz go zapisać.

**Najpierw walidacja, potem test** · [0:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/pl.mp4#t=44.016)

Zapisz wykonuje te same kontrole, ale zapisuje Workflow nawet z problemami, więc najpierw sprawdź poprawność. Walidacja nie sprawdza twoich danych ani ustawień w kartach. Aby zobaczyć, co Workflow robi z prawdziwym dokumentem, przetestuj go.

</details>

Kliknij element sterujący **Validate** (ikona okręgu z zaznaczeniem lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Walidacja sprawdza graf pod kątem problemów — niepołączonych węzłów, brakującej konfiguracji i nieprawidłowych połączeń — i wskazuje je, abyś mógł je naprawić, zanim przepływ pracy zostanie uruchomiony na rzeczywistych dokumentach.

## Test

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4" %}

**Film:** Testowanie Workflow · 2:24 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Testuj przed włączeniem** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=0.25)

Przetestuj Workflow, zanim go włączysz. Test wykonuje to, co jest teraz na obszarze roboczym, także niezapisane zmiany. Akcje takie jak przypisanie czy eksport są tylko symulowane, więc dokument się nie zmienia.

**Testuj cały Workflow** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=21.483)

Oto Workflow, który nie jest jeszcze zapisany. Aby przetestować cały Workflow, kliknij Testuj przepływ pracy na pasku narzędzi.

**Wybierz dokument testowy** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=34.483)

Wybierz dokument do testu. Workflows, które nie potrzebują dokumentu, można też testować bez niego. Wyszukaj dokument po nazwie, zaznacz go i kliknij Test.

**Odczytaj wynik na obszarze roboczym** · [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=50.116)

Test idzie ścieżką dokumentu. Ta faktura nie czeka na akceptację, więc karta I kończy się niespełnionym warunkiem, a pomarańczowa ścieżka prowadzi do karty przypisania. Niewybrane ścieżki są wyszarzone, a baner u góry pokazuje wynik i czas trwania testu.

**Szczegóły każdej karty** · [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=74.883)

Kliknij Szczegóły, aby zobaczyć każdą kartę z wynikiem i komunikatem. Ponowny test uruchamia test jeszcze raz po zmianach.

**Testuj jedną kartę** · [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=89.316)

Aby przetestować jedną kartę, najedź na nią i kliknij przycisk odtwarzania. Możesz też kliknąć kartę prawym przyciskiem i wybrać Test z tego węzła. Test zaczyna się od tej karty, z tym samym wyborem dokumentu.

**Najedź na plakietkę po szczegóły** · [1:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=110.95)

Wykonuje się tylko ta karta i karty po niej. Najedź na plakietkę, aby zobaczyć wynik karty. Zmieniaj kartę i testuj ponownie, aż zrobi to, czego oczekujesz.

**Co oznaczają kolory** · [2:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v1/pl.mp4#t=128.35)

Krótko: zielony oznacza sukces, pomarańczowy niespełniony warunek, a czerwony błąd. Karty, które się nie wykonały, są przygaszone i mają szarą plakietkę.

</details>

Kliknij element sterujący **Test** (ikona odtwarzania lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), aby uruchomić bieżący przepływ na przykładowych danych i obserwować, jak się zachowuje, bez wpływu na rzeczywiste dokumenty. To najszybszy sposób na sprawdzenie poprawności zmiany, którą właśnie wprowadziłeś na kanwie.

## Kiedy czego używać

- **Validate / Test w kreatorze** (ta strona) — natychmiastowa informacja zwrotna podczas projektowania przepływu.
- **[Test Manager](../test-manager.md)** — zapisz scenariusz, aby móc go uruchomić ponownie później (i razem ze wszystkimi pozostałymi scenariuszami) w celu wykrycia regresji po przyszłych zmianach.

## Następne kroki

- Zapoznaj się z typami węzłów i połączeniami w [Węzły](nodes.md).
- Zobacz wszystkie elementy sterujące paska narzędzi i kanwy w [Pasek narzędzi i kanwa](toolbar-and-canvas.md).
