# Walidacja i testowanie

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
