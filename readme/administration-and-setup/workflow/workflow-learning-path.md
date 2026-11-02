---
description: "Ścieżka od początkującego do eksperta"
---

# Ścieżka od początkującego do eksperta

Przechodź poziomy po kolei. Samo czytanie nie wystarcza: każdy kończy się własną konfiguracją, sprawdzalnym oczekiwaniem i dowodem. P0 zapobiega podstawowym błędom wykonania; P1 rozwija dane, decyzje biznesowe i integracje.

1. [Orientacja i model wykonania](#level-1)
2. [Pierwsza własna reguła](#level-2)
3. [Pola, typy i granice](#level-3)
4. [Reguły biznesowe i zatwierdzenia](#level-4)
5. [Sterowanie Advanced i podworkflow](#level-5)
6. [Obliczenia, integracja i eksport](#level-6)
7. [Zmiany i eksploatacja ekspercka](#level-7)

## Wymagania

Używaj własnej organizacji testowej i syntetycznego dokumentu. Sprawdź organizację, rolę, licencję workflow i dostęp Advanced. Pozostaw importowane ćwiczenia nieaktywne. Pełne JSON służą do Advanced Test → Custom Data. Rzeczywiste zatwierdzenia i integracje wymagają osobnych użytkowników oraz celów testowych.

## 1. Orientacja i model wykonania <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pl.html).

**Ćwiczenie:** Wyjaśnij organizację, dostęp, When–And–Then i różnicę między regułą liniową a grafem Advanced. Odróżnij filtr dokumentu, zdarzenie, zapis i aktywację.

**Warunek ukończenia:** Wyjaśniasz, kiedy reguła jest uwzględniana i jaki dowód odróżnia symulację od wykonania dokumentu.

Czytaj i buduj: [Kiedy uruchamia się mój workflow?](workflow-execution-model.md) · [P0: zmiana statusu i ograniczanie ponownych wykonań](masterclass/status-and-reentry.md).

## 2. Pierwsza własna reguła <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pl.html).

**Ćwiczenie:** Zbuduj When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Pozostaw nieaktywną. Sprawdź pełne dane dla 999, 1000 i 1000.01. Reguła liniowa nie potrzebuje jeszcze węzła sterowania.

**Warunek ukończenia:** REVIEW jest osiągane tylko powyżej 1000. Zapisz typ, operator i wyjście. Brak wejścia obsłuż osobno.

Czytaj i buduj: [Przykład Advanced: kierowanie faktur](advanced-workflow-case-study.md) · [Pakiet szkoleniowy workflow](workflow-training-kit.md).

## 3. Pola, typy i granice <a id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pl.html).

**Ćwiczenie:** Sprawdź brak, null, pusty tekst, spacje, false, 0 i liczby tekstowe. Oblicz tolerancję względem zamówienia oraz dokumentu. Porównaj jedną i wszystkie faktycznie dopasowane pozycje.

**Warunek ukończenia:** Wyjaśniasz prawdę, fałsz i błąd według wartości, typu, odniesienia i danych. Brak porównywalnej pozycji nie jest udanym zatwierdzeniem.

Czytaj i buduj: [P1: wybór Field is, Docfield is i Compare two Fields](masterclass/field-conditions.md) · [P1: jawna podstawa tolerancji i kierunek porównania PO](masterclass/tolerances-and-po.md).

## 4. Reguły biznesowe i zatwierdzenia <a id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pl.html).

**Ćwiczenie:** Ustaw dwie niepokrywające się reguły kwotowe. Prześledź zapisany wynik użytkownika do przypisania. Zaplanuj A z kolejnością 10, B z 20, odrzucenie i rezerwę.

**Warunek ukończenia:** Odróżniasz odpowiedzialność, zadanie, powiadomienie i zgodę. Rzeczywiste przekazanie do B wymaga przetworzonej decyzji A.

Czytaj i buduj: [P1: od tabeli decyzyjnej do przypisania dokumentu](masterclass/decision-table-routing.md) · [P1: przypisanie, zadanie i zatwierdzanie sekwencyjne](masterclass/assignment-task-sequential.md).

## 5. Sterowanie Advanced i podworkflow <a id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pl.html).

**Ćwiczenie:** Porównaj ALL, ANY i OR dla dwóch osiągniętych kontroli. Zbadaj niewybraną gałąź. Wykonaj siedem przypadków v2 i sprawdź Run Workflow z własnym nieaktywnym celem.

**Warunek ukończenia:** Wyjaśniasz różnice test/harmonogram, liczenie źródeł i błędy. V2 kończy bez zablokowanego OR; sprawdzasz cel zielonego wywołania.

Czytaj i buduj: [P0: poprawne łączenie Wait ALL, Wait ANY i OR](masterclass/control-nodes.md) · [P0: Run Workflow, warunki celu i obsługa błędów](masterclass/run-workflow.md) · [Przykład Advanced: kierowanie faktur](advanced-workflow-case-study.md).

## 6. Obliczenia, integracja i eksport <a id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pl.html).

**Ćwiczenie:** Porównaj całą tabelę przed/po, z niedopasowaniem regex i dzieleniem przez zero. Określ rzeczywisty kontrakt zapisu wyników integracji. Zaplanuj eksport po zgodzie z własną konfiguracją testową.

**Warunek ukończenia:** Osobno potwierdzasz dalsze wartości, odbiór i ERP. Symulacji ani żądania eksportu nie zapisujesz jako dostarczenia.

Czytaj i buduj: [P1: obliczanie kolumn i zależności od regex](masterclass/table-calculations.md) · [P1: sprawdzanie wywołań API i użycia odpowiedzi](masterclass/api-response-contract.md) · [P1: wariant eksportu, otwarte zadania i status końcowy](masterclass/export-lifecycle.md).

## 7. Zmiany i eksploatacja ekspercka <a id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pl.html).

**Ćwiczenie:** Zapisz eksport workflow i wersje kart przed zmianą. Powtórz dodatnie, ujemne, błędne, graniczne przypadki i drugie wykonanie. Powiąż pierwszy błąd z konkretnymi danymi i konfiguracją.

**Warunek ukończenia:** Potrafisz odebrać zmianę, przywrócić konfigurację i porównać nowe wykonanie ze skutkami. Zapisujesz przyczynę, poprawkę i ograniczenia.

Czytaj i buduj: [Systematyczna diagnostyka problemów workflow](workflow-troubleshooting.md) · [Zrozumieć i skonfigurować karty workflow](card-reference-standard.md).

## Sprawdź wiedzę

| Pytanie | Odpowiedź |
| --- | --- |
| Czy false jest puste w Field is v2? | Tak; liczba 0 i tekst "false" nie są puste. |
| Czy zielony test OR gwarantuje wykonanie dokumentu? | Nie. Nieosiągnięci poprzednicy są inaczej obsługiwani w teście i sprawdzonym harmonogramie. |
| Czy Run Workflow wywoła nieaktywny cel? | Tak, przez sprawdzone jawne wywołanie. Nadal sprawdzaj warunki i wynik celu. |
| Czy HTTP 200 automatycznie udostępnia api.response.cost_center? | Nie. Sprawdzone akcje nie mają takiego automatycznego kontraktu wyjścia JSON. |
| Czy zielony test dowodzi odbioru eksportu? | Nie. Wykonanie dokumentu, odbiór i ERP wymagają osobnych dowodów. |

## Pięć przewodników towarzyszących

Używaj w ćwiczeniach: model wykonania → odtwarzalny przykład → pakiet → diagnostyka → opis karty. To materiały poziomów, a nie pięć dodatkowych niesprawdzonych zadań.

1. [Kiedy uruchamia się mój workflow?](workflow-execution-model.md)
2. [Przykład Advanced: kierowanie faktur](advanced-workflow-case-study.md)
3. [Pakiet szkoleniowy workflow](workflow-training-kit.md)
4. [Systematyczna diagnostyka problemów workflow](workflow-troubleshooting.md)
5. [Zrozumieć i skonfigurować karty workflow](card-reference-standard.md)

## Protokół ukończenia

Użyj acceptance-record-template.json z pakietu. Zapisz scenariusz, rewizję, oczekiwanie, obserwację i rodzaj dowodu. Odróżnij test Dev, izolowaną kontrolę kodu, rzeczywiste wykonanie, odbiór i ERP. Jawnie pozostaw otwarte niesprawdzone kroki.
