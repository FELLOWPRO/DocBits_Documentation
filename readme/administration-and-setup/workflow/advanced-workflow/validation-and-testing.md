# Walidacja i Testowanie

Zanim zaczniesz polegać na Zaawansowanym Workflow, użyj elementów sterujących paska narzędzi, aby potwierdzić, że jest poprawny i zachowuje się zgodnie z oczekiwaniami.

## Validate

Kliknij element **Validate** (ikona okręgu z haczykiem lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Walidacja sprawdza graf pod kątem problemów — niepołączonych węzłów, brakującej konfiguracji i nieprawidłowych połączeń — dzięki czemu możesz je naprawić, zanim workflow zostanie uruchomiony na rzeczywistych dokumentach.

## Test

Kliknij element **Test** (ikona odtwarzania lub naciśnij <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>), aby uruchomić workflow na próbce i zobaczyć, jak się zachowuje, bez wpływu na bieżące dokumenty.

## Scenariusze testowe

Aby przeprowadzać powtarzalne kontrole, zapisz **scenariusze testowe** w **Test Manager** (zobacz [Pulpit](../workflow-dashboard.md)). Każdy scenariusz rejestruje oczekiwany wynik i pokazuje rezultat pass/fail, a **Run All Tests** uruchamia je ponownie wszystkie razem — dzięki czemu możesz potwierdzić, że Twoje workflow nadal zachowują się poprawnie po zmianie.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Lista Test Managera ze scenariuszami testowymi i przyciskiem Run All Tests"><figcaption><p>Test Manager — zapisane scenariusze z wynikami pass/fail oraz przyciskiem <strong>Run All Tests</strong>.</p></figcaption></figure>

## Następne kroki

- Przejrzyj typy węzłów i połączenia w sekcji [Węzły](nodes.md).
- Zobacz wszystkie elementy sterujące paska narzędzi i kanwy w [Pasku narzędzi i Kanwie](toolbar-and-canvas.md).
