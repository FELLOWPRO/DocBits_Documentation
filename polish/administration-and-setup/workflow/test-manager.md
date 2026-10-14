# Test Manager

**Test Manager** umożliwia zapisywanie wielokrotnego użytku **scenariuszy testowych** dla Twoich przepływów pracy i uruchamianie ich razem — dzięki czemu możesz potwierdzić, że przepływ pracy nadal działa poprawnie po wprowadzeniu w nim zmian. Działa zarówno dla przepływów Standard, jak i Advanced.

Otwórz go z poziomu **Workflow Dashboard → Test Manager List**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Lista Test Manager ze scenariuszami testowymi, statusem i Run All Tests"><figcaption><p>Test Manager List — każdy zapisany scenariusz pokazuje wynik zaliczono/niezaliczono.</p></figcaption></figure>

## Czym jest scenariusz testowy

Scenariusz testowy obejmuje przepływ pracy, przykładowe dane wejściowe oraz **oczekiwany wynik**. Po uruchomieniu Test Manager odtwarza przepływ pracy na tych danych wejściowych i porównuje rezultat z tym, czego oczekiwałeś — zmieniając wiersz na **zielony** (zaliczono) lub **czerwony** (niezaliczono).

## Praca ze scenariuszami

- **Add Test Scenario** — utwórz nowy scenariusz na podstawie przepływu pracy i przykładowego dokumentu.
- **Run All Tests** — uruchom wszystkie scenariusze naraz i zobacz na pierwszy rzut oka, które przepływy pracy nadal są zaliczane.
- **View Details** — otwórz scenariusz, aby sprawdzić jego wynik.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Szczegóły scenariusza testowego przepływu pracy ze statusem, czasem uruchomienia i danymi"><figcaption><p>Szczegóły scenariusza — nazwa, status, czas uruchomienia oraz rzeczywiste i wyodrębnione dane wygenerowane przez uruchomienie.</p></figcaption></figure>

Widok szczegółów pokazuje nazwę scenariusza i **status**, **nazwę przepływu pracy**, **czas uruchomienia** oraz **rzeczywiste** i **wyodrębnione dane** wygenerowane przez uruchomienie — dzięki czemu widzisz dokładnie, dlaczego scenariusz został zaliczony lub niezaliczony.

## Test Manager a testowanie w kreatorze

To dwie różne rzeczy:

- **Test Manager** (ta strona) — *zapisane, powtarzalne* scenariusze z oczekiwanymi wynikami, uruchamiane razem za pomocą **Run All Tests**. Używaj go do testów regresji po wprowadzeniu zmian.
- **Testowanie w kreatorze** — wbudowane elementy sterujące **Validate** i **Test** wewnątrz kreatora Advanced Workflow, do szybkich kontroli podczas budowania. Zobacz [Walidacja i testowanie](advanced-workflow/validation-and-testing.md).
