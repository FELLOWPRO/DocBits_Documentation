# Następny krok i odrzucenie dokumentu

> W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.

Po przeczytaniu [raportu walidacyjnego](validation-report.md) raport podpowiada, co zrobić. Możesz też odrzucić dokument.

## Co zrobić dalej

<figure><img src="../../../../../.gitbook/assets/einvoice-report-next-step-pl.png" alt="Ocena, następny krok i działania w raporcie."><figcaption><p>Ocena, następny krok i działania w raporcie.</p></figcaption></figure>

**Assessment** mówi jednym zdaniem, czy faktura jest zgodna. Blok **Next step** mówi, co zrobić:

| Wynik | Następny krok |
| --- | --- |
| Co najmniej jeden **błąd** | Poproś nadawcę o poprawioną fakturę albo odrzuć dokument. Poprawiona faktura to nowy dokument. |
| Tylko **ostrzeżenia** | Możesz kontynuować pracę z dokumentem. |

Przyciski na końcu raportu:

* **Reject document**: otwiera okno odrzucenia (patrz niżej).
* **Report (HTML)** i **Report (XML)**: pobierają raport, na przykład aby wysłać go dostawcy.
* **Close** (lub **Back to document**): wraca do dokumentu.

## Odrzucanie dokumentu

<figure><img src="../../../../../.gitbook/assets/einvoice-reject-dialog-pl.png" alt="Okno odrzucenia fikcyjnej faktury. Odrzucenie zostało anulowane."><figcaption><p>Okno odrzucenia fikcyjnej faktury. Odrzucenie zostało anulowane.</p></figcaption></figure>

1. W raporcie wybierz **Reject document**.
2. Sprawdź **Reason**. DocBits wypełnia go na podstawie błędów z raportu. Możesz edytować tekst.
3. Wybierz **Reject document**, aby potwierdzić. Status zmienia się na **Rejected**. Powód jest zapisywany jako notatka, a raport pozostaje w dokumencie.

Wybierz **Cancel**, aby zostawić dokument bez zmian.

> **Reject document** widzą tylko użytkownicy, którzy mogą edytować dokumenty. Przycisk jest ukryty, gdy dokument jest już odrzucony lub zakończony.
