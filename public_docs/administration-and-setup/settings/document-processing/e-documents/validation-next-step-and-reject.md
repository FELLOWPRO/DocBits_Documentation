# Następny krok i odrzucenie dokumentu

> W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.

Po przeczytaniu [raportu walidacyjnego](validation-report.md) raport podpowiada, co zrobić. Możesz też odrzucić dokument.

## Co zrobić dalej

<figure><img src="../../../../.gitbook/assets/einvoice-report-next-step-pl-20261104-v2.png" alt="Ocena, następny krok i działania w raporcie."><figcaption><p>Ocena, następny krok i działania w raporcie.</p></figcaption></figure>

**Ocena** mówi jednym zdaniem, czy faktura jest zgodna. Blok **Następny krok** mówi, co zrobić:

| Wynik | Następny krok |
| --- | --- |
| Co najmniej jeden **błąd** | Poproś nadawcę o poprawioną fakturę albo odrzuć dokument. Poprawiona faktura to nowy dokument. |
| Tylko **ostrzeżenia** | Możesz kontynuować pracę z dokumentem. |

Przyciski na końcu raportu:

* **Odrzuć dokument**: otwiera okno odrzucenia (patrz niżej).
* **Raport (HTML)** i **Raport (XML)**: pobierają raport, na przykład aby wysłać go dostawcy.
* **Zamknij**: wraca do dokumentu.

## Odrzucanie dokumentu

<figure><img src="../../../../.gitbook/assets/einvoice-reject-dialog-pl-20261104-v2.png" alt="Okno odrzucenia fikcyjnej faktury. Odrzucenie zostało anulowane."><figcaption><p>Okno odrzucenia fikcyjnej faktury. Odrzucenie zostało anulowane.</p></figcaption></figure>

1. W raporcie wybierz **Odrzuć dokument**.
2. Sprawdź **Powód**. DocBits wypełnia go na podstawie błędów z raportu. Możesz edytować tekst.
3. Wybierz **Odrzuć dokument**, aby potwierdzić. Status zmienia się na **Odrzucony**. Powód jest zapisywany jako notatka, a raport pozostaje w dokumencie.

Wybierz **Anuluj**, aby zostawić dokument bez zmian.

> **Odrzuć dokument** widzą tylko użytkownicy, którzy mogą edytować dokumenty. Przycisk jest ukryty, gdy dokument jest już odrzucony lub zakończony.
