# Standard Workflow

Kreator **Standard Workflow** to liniowy, oparty na kartach edytor do automatyzacji przetwarzania dokumentów. Przepływ pracy składa się z trzech grup kart — **When** (wyzwalacz), **And** (dodatkowe warunki) oraz **Then** (akcje do wykonania). Gdy dokument spełnia warunki When/And, akcje Then są uruchamiane automatycznie.

## Jak uzyskać dostęp

Otwórz **Workflow Dashboard → Workflow List**, a następnie kliknij **Add Workflow**, aby utworzyć nowy przepływ pracy Standard, lub kliknij istniejący przepływ pracy, aby go edytować.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List with type, execution order and trigger"><figcaption><p>Workflow List — każdy wiersz to przepływ pracy, który możesz otworzyć, włączyć/wyłączyć lub edytować.</p></figcaption></figure>

## Model When / And / Then

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Standard Workflow canvas with When, And and Then cards"><figcaption><p>Obszar roboczy Standard Workflow. Ten przykład wyzwala się dla faktur w sub-organizacji i przypisuje je do użytkownika.</p></figcaption></figure>

- **When** — wyzwalacz, który uruchamia przepływ pracy (np. *Document type is Invoice*).
- **And** — dodatkowe warunki, które również muszą być spełnione (np. *Document is part of sub-organization*). Pozostaw puste, aby uruchamiać przy każdym dopasowaniu karty When.
- **Then** — akcje do wykonania (np. *Assign the document to the user*, utworzenie zadania, wywołanie API, wysłanie wiadomości e-mail).

## Dodawanie kart

Kliknij **Add Card** w dowolnej grupie, aby otworzyć bibliotekę kart. Karty są pogrupowane według kategorii, dzięki czemu łatwo znajdziesz potrzebny element:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card library grouped by category"><figcaption><p>Biblioteka <strong>Add Card</strong> — karty warunków, karty porównań, karty akcji i inne, pogrupowane według kategorii.</p></figcaption></figure>

Zapisz za pomocą **Save Workflow** lub zapisz układ jako wielokrotnego użytku szablon za pomocą **Save Template**.

## Następne kroki

- Zobacz, co robi każda karta, w sekcji **Cards**.
- Łącz karty w sprawdzone rozwiązania dzięki **Workflow Pattern Guides**.
- W przypadku przepływów rozgałęzionych z równoległymi ścieżkami (Wait ALL / Wait ANY / OR) użyj kreatora **Advanced Workflow**.
