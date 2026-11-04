---
description: "Pobierz syntetyczną fakturę, workflow JSON, dane wejściowe, oczekiwania i prawdziwe odpowiedzi testowe."
---

# Pakiet szkoleniowy workflow

Używaj pakietu z [przykładem Advanced](advanced-workflow-case-study.md). Zawiera syntetyczną fakturę, importowalny workflow, siedem pełnych wejść dokumentowych, niezależne oczekiwania oraz zapisane prawdziwe odpowiedzi. Klucze techniczne i nazwy ścieżek pozostają identyczne we wszystkich językach.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Pakiet szkoleniowy z przykładami i wynikami
{% endfile %}

## Zawartość i formaty

| Plik | Zastosowanie |
| --- | --- |
| `training-invoice.pdf` | Syntetyczna faktura: 1500 EUR netto, 285 EUR podatku, łącznie 1785 EUR. Nie jest przeznaczona do zapłaty. |
| `advanced-workflow.json` | Import przez **Import Workflow** w stanie nieaktywnym; bez zmiennej globalnej, tylko Faktura i dokładny numer szkoleniowy. |
| `*-input.json` | Pełne dane dla **Advanced Test → Custom Data**. |
| `expectations.json` | Oczekiwane ścieżki, komunikaty statusu i wyniki; specyfikacja biznesowa, nie plik importu Test Manager. |
| `*-result.json` | Prawdziwe odpowiedzi Dev z wynikami i komunikatami; prywatne odniesienia organizacji zastąpiono. |
| `prepare_inputs.py` | Zastępuje syntetyczną organizację w obu wymaganych miejscach. |
| `verify_results.py` | Sprawdza odpowiedzi względem niezależnych oczekiwań. Wymaga Python 3, bez klucza dostępu. |

## Użycie

1. Rozpakuj ZIP i przeczytaj dołączoną instrukcję.
2. Zaimportuj workflow do swojej organizacji testowej i potwierdź, że jest nieaktywny.
3. Ustal ID własnej organizacji testowej i uruchom lokalnie:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Użyj plików z `prepared/` w oknie Advanced. Nie zastępuj syntetycznej ID dokumentu identyfikatorem rzeczywistej faktury klienta.
5. Sprawdź siedem przypadków według [tabeli wyników](advanced-workflow-case-study.md). Różnice kwoty są celowymi wariantami testowymi; nie zmieniają załączonej faktury.

Dane zawierają `id`, `org_id`, `doc_type`, `status` i `extracted_data` z `layout.groups`, `fields` oraz `tables`. Organizacja na najwyższym poziomie i w `extracted_data` musi odpowiadać zalogowanemu kontu. Wartość bez definicji w layout może nie zostać odczytana jako istniejące pole dokumentu.

## Zakres ćwiczenia

Oczekiwania sprawdzają wybrane ścieżki, tekst kierowania, komunikaty statusu i węzły końcowe, a nie tylko status dokumentu. Nie odpowiadają porównaniu statusu w zapisanym scenariuszu Test Manager.

Pomyślny test Advanced potwierdza przetworzenie dostarczonych danych. Symulowane działania nie są rzeczywistym przypisaniem, emailem lub dostarczeniem. Aktywacja wymaga odpowiedniego wejścia zdarzenia i osobno zweryfikowanego prawdziwego wykonania. Zobacz [Kiedy uruchamia się mój workflow?](workflow-execution-model.md).

## WF-03: Ćwiczenie i odbiór

Rozpakuj v2, dostosuj organizację przez prepare_inputs.py i uruchom verify_results.py. decision-table-setup.json opisuje konfigurację, acceptance-record-template.json to wzór protokołu; żaden nie importuje workflow. Potwierdź nieaktywny stan przed importem.

[Ścieżka nauki](workflow-learning-path.md)
