---
description: "Ścieżka od początkującego do eksperta"
---

# Ścieżka od początkującego do eksperta

Siedem poziomów prowadzi od pierwszego spojrzenia na projektanta workflow do samodzielnej odpowiedzialności za zmianę w działającym workflow. Każdy poziom podaje cel, kroki do wykonania we własnej organizacji testowej oraz wynik, który można sprawdzić. Przechodź je po kolei i zbuduj każde ćwiczenie samodzielnie: każdy poziom opiera się na konfiguracji z poprzedniego.

1. [Orientacja i model wykonania](#level-1)
2. [Pierwsza własna reguła](#level-2)
3. [Pola, typy i granice](#level-3)
4. [Reguły biznesowe i zatwierdzenia](#level-4)
5. [Sterowanie Advanced i podworkflow](#level-5)
6. [Obliczenia, integracja i eksport](#level-6)
7. [Zmiany i eksploatacja ekspercka](#level-7)

## Zanim zaczniesz

* Własna organizacja testowa z syntetycznym dokumentem w środku. Nigdy nie ćwicz na dokumentach klientów.
* Twoja rola, licencja workflow i uprawnienie Advanced, sprawdzone przed poziomem 1.
* Zaimportowane ćwiczenia pozostają nieaktywne, dopóki ich nie przetestujesz.
* Pełne dane JSON należą do **Advanced Test → Custom Data**.
* Prawdziwe zatwierdzenia i integracje wymagają własnych użytkowników i celów testowych; test w projektancie ich nie zastąpi.

## 1. Orientacja i model wykonania <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pl.html).

**Cel:** Wiedzieć, co uruchamia workflow i co wynik testu mówi, a czego nie mówi, o rzeczywistym wykonaniu.

1. Sprawdź organizację, swój dostęp, moduł workflow i uprawnienie Advanced.
2. Powiedz When–And–Then własnymi słowami, a potem wyjaśnij, gdzie kończy się reguła liniowa i jak graf Advanced podąża za swoimi połączonymi wyjściami.
3. Rozróżniaj cztery rzeczy, które w projektancie wyglądają podobnie: filtr typu dokumentu, zdarzenie wykonania, zapis i aktywację.

**Warunek ukończenia:** Umiesz powiedzieć, kiedy reguła jest w ogóle brana pod uwagę i jaki dowód oddziela symulację od wykonania na rzeczywistym dokumencie.

**Pogłębienie:** [Kiedy uruchamia się mój workflow?](workflow-execution-model.md) · [Zmiana statusu bez ponownego uruchamiania workflow](masterclass/status-and-reentry.md)

## 2. Pierwsza własna reguła <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pl.html).

**Cel:** Doprowadzić regułę od projektanta do sprawdzonego wyniku bez dotykania dokumentu.

1. Zbuduj ją w Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Reguła liniowa tej wielkości nie potrzebuje węzła sterowania.
2. Zapisz ją i sprawdź na liście reguł, czy nadal jest nieaktywna, bo zapis nowej reguły może ją już aktywować. Advanced Test to osobna powierzchnia wykonania: ocenia graf w kreatorze, a nie aktywowaną regułę.
3. Uruchom Advanced Test z pełnymi danymi dla 999, 1000 i 1000.01. Zanotuj dla każdego przypadku typ pola, operator i wybrane wyjście, a potem dodaj przypadek, w którym kwoty brakuje całkowicie.

**Warunek ukończenia:** REVIEW jest osiągane tylko przy 1000.01, brakująca kwota pojawia się jako błąd, a nie jako zwykły wynik poniżej progu, i na końcu reguła jest znów wyłączona.

**Pogłębienie:** [Przypadek biznesowy Advanced: trasowanie faktur](advanced-workflow-case-study.md) · [Zestaw ćwiczeń workflow](workflow-training-kit.md)

## 3. Pola, typy i granice <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pl.html).

**Cel:** Wiedzieć, co warunek naprawdę porównuje, zanim zaufasz jego wynikowi.

1. Sprawdź kontrolę pustości dla brakującego pola, `null`, pustego tekstu, spacji, `false`, `0`, `"0"` i `"false"` i zanotuj, które z nich liczą się jako puste.
2. Policz tę samą tolerancję 2 procent dwa razy: raz z zamówieniem jako odniesieniem (zamówienie 100, dokument 102.02), a raz z dokumentem jako odniesieniem.
3. Przełącz na karcie zamówienia między Any i All i policz, ile pozycji rzeczywiście porównano.

**Warunek ukończenia:** Wyjaśniasz prawdę, fałsz i błąd na podstawie wartości, typu, odniesienia i dostępnych danych. W wersji 5 karty zamówienia dokument bez porównywalnej pozycji to błąd danych, a nie udane zatwierdzenie.

**Pogłębienie:** [P1: Field is, Docfield is i porównanie dwóch pól](masterclass/field-conditions.md) · [P1: Jednoznaczne tolerancje i odniesienie do zamówienia](masterclass/tolerances-and-po.md)

## 4. Reguły biznesowe i zatwierdzenia <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pl.html).

**Cel:** Wysłać fakturę do właściwej osoby przez tabelę decyzyjną, a następnie przeprowadzić łańcuch zatwierdzeń, który czeka na pierwszą osobę sprawdzającą.

**Ćwiczenie 1: tabela decyzyjna z bezpośrednim przypisaniem**

1. Utwórz tabelę decyzyjną z dwiema regułami, które nie mogą zadziałać jednocześnie: sprawdzająca A do 1000, sprawdzający B powyżej 1000, z `cost_center=4711` i `total_amount`.
2. W **Decision Table has Returns** w wersji 3 ustaw `store_data=wf_store_data`. Przypisz dokument kartą **Assign document based on decision table** z `assignee_type=user`, używając rzeczywistych użytkowników z Twojej organizacji testowej.
3. Przetestuj jedno dopasowanie, brak dopasowania, kilka dopasowań i nieprawidłowy identyfikator użytkownika, a braki dopasowania i błędy przypisania skieruj do jawnego wariantu zastępczego. Zaakceptuj przypisanie na samym dokumencie.

**Ćwiczenie 2: zatwierdzenie sekwencyjne bez bezpośredniego przypisania**

1. Utwórz drugą, osobną regułę z kartami sekwencyjnymi: karta przypisania sekwencyjnego na pozycji 10 dla sprawdzającej A, potem karta zadania sekwencyjnego na pozycji 20 dla sprawdzającego B. Pomiń w tym przebiegu przypisanie bezpośrednie, ponieważ sprawdzone zakończenie może pominąć pierwszego odbiorcę sekwencyjnego, gdy dokument został już przypisany bezpośrednio w tym samym przebiegu.
2. Zatwierdź jako A i sprawdź, że B otrzymuje dokument dopiero po przetworzonej decyzji A; następnie zatwierdź jako B.
3. Odrzuć jako A w nowym przebiegu i potwierdź, że eksport nie następuje. Sprawdź potem, co się dzieje, gdy nie można ustalić żadnego odbiorcy.

**Warunek ukończenia:** Rozróżniasz odpowiedzialność, zadanie, powiadomienie i rzeczywiste zatwierdzenie; A → zatwierdzenie → B → zatwierdzenie nastąpiło w tej kolejności; odrzucenie przez A uniemożliwiło eksport; a brakujący odbiorca nie został uznany za zakończone zatwierdzenie.

**Pogłębienie:** [P1: Prześledzenie tabeli decyzyjnej do przypisania](masterclass/decision-table-routing.md) · [P1: Rozróżnianie przypisania, zadania i zatwierdzenia sekwencyjnego](masterclass/assignment-task-sequential.md)

## 5. Sterowanie Advanced i podworkflow <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pl.html).

**Cel:** Poprawnie łączyć równoległe ścieżki i przekazywać pracę do innego workflow.

1. Porównaj ALL, ANY i OR na dwóch kontrolach, które są rzeczywiście osiągane: ALL wymaga pasującego wyjścia z każdego źródła, ANY i OR wymagają jednego, a zielony plus pomarańczowy z jednego źródła nadal liczą się jako jedno źródło.
2. Przyjrzyj się gałęzi, której przebieg nie wybrał, jak w przypadku MERGE-04: Advanced Test nadal ocenia oczekujące połączenie, a zwykły przebieg pomija je, gdy poprzednik nigdy nie dotrze.
3. Przejdź siedem przypadków studium przypadku v2 (powyżej, poniżej, granica, tuż powyżej, brak, nieprawidłowa liczba, inna faktura). Potem wywołaj przez Run Workflow własny nieaktywny workflow i otwórz ścieżkę w samym celu.

**Warunek ukończenia:** Wyjaśniasz różnicę z przypadku MERGE-04 między testem a przebiegiem z kroku 2, sposób liczenia źródeł i to, dokąd trafia błąd. Zielone wywołanie Run Workflow nadal wymaga sprawdzenia w celu. V2 oznacza tutaj drugą wersję grafu studium przypadku: karta statusu każdej ścieżki prowadzi bezpośrednio do wspólnej karty zakończenia, bez oczekującego węzła OR.

**Pogłębienie:** [P0: Poprawne łączenie Wait ALL, Wait ANY i OR](masterclass/control-nodes.md) · [P0: Run Workflow, warunki celu i błędy](masterclass/run-workflow.md) · [Przypadek biznesowy Advanced: trasowanie faktur](advanced-workflow-case-study.md)

## 6. Obliczenia, integracja i eksport <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pl.html).

**Cel:** Obliczać wartości, odbierać wynik z systemu zewnętrznego i eksportować dopiero po rzeczywistym zatwierdzeniu.

1. Oblicz kolumnę i porównaj całą tabelę przed i po, łącznie z wierszem, w którym wyrażenie regularne nie pasuje, oraz z dzieleniem przez zero.
2. Zapisz kontrakt zapisu zwrotnego z systemem zewnętrznym: które pole dokumentu przyjmuje wynik, która karta lub rozszerzenie go tam zapisuje i jak potem sprawdzasz zapisaną wartość. Samo HTTP 200 nie jest wynikiem.
3. Zaplanuj eksport po zatwierdzeniu z własną konfiguracją eksportu i zanotuj, co sprawdzisz u odbiorcy.

**Warunek ukończenia:** Kolejne wartości w polu, odbiór u odbiorcy i przetworzenie w ERP mają każdy własny dowód. Symulacja ani eksport w kolejce nie są dostarczeniem.

**Pogłębienie:** [P1: Obliczenia w tabeli i sprawdzenie zależności od regex](masterclass/table-calculations.md) · [P1: Wywołanie API i wykorzystanie odpowiedzi](masterclass/api-response-contract.md) · [P1: Warianty eksportu, otwarte zadania i status zakończenia](masterclass/export-lifecycle.md)

## 7. Zmiany i eksploatacja ekspercka <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pl.mp4" %}

[Otwórz wideo z polskimi napisami i transkrypcją](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pl.html).

**Cel:** Zmienić workflow, którego nie zbudowałeś, i móc tę zmianę wycofać.

1. Wyeksportuj workflow i zanotuj wersje kart, zanim czegokolwiek dotkniesz.
2. Po zmianie powtórz przypadki pozytywne, negatywne, błędne i graniczne oraz dodatkowo drugi przebieg tego samego przypadku.
3. Powiąż pierwszy błąd z jednym wejściem i jedną konfiguracją i trzymaj zapisany eksport jako drogę powrotu.

**Warunek ukończenia:** Umiesz odebrać zmianę, przywrócić zapisaną konfigurację i porównać nowy przebieg dokumentu z dowodami. Zanotuj przyczynę, poprawkę i granice, które pozostają.

**Pogłębienie:** [Systematyczne diagnozowanie błędów workflow](workflow-troubleshooting.md) · [Rozumienie kart i niezawodna konfiguracja](card-reference-standard.md)

## Sprawdź wiedzę

| Pytanie | Odpowiedź |
| --- | --- |
| Czy `false` jest puste w Field is v2? | Tak. Liczba 0 i tekst "false" nie są puste. |
| Czy zielony test OR gwarantuje przebieg dokumentu? | Nie. W sprawdzonym przypadku MERGE-04 test ocenia połączenie, które przebieg dokumentu pomija, gdy poprzednik nigdy nie dotrze. |
| Czy Run Workflow może wywołać nieaktywny cel? | Tak, w sprawdzonym jawnym wywołaniu. Mimo to sprawdź warunki celu i wynik. |
| Czy HTTP 200 automatycznie udostępnia api.response.cost\_center? | Nie. Sprawdzone akcje nie oferują tego automatycznego kontraktu wyjścia JSON. |
| Czy zielony test dowodzi odbioru eksportu? | Nie. Przebieg dokumentu, odbiór u odbiorcy i przetworzenie w ERP wymagają osobnych dowodów. |

## Zapisanie tego, co zostało odebrane

Pobierz `workflow-training-kit-v2.zip` z [zestawu ćwiczeń workflow](workflow-training-kit.md), rozpakuj i otwórz `acceptance-record-template.json`. To pusty protokół, a nie coś do zaimportowania; ten sam plik ZIP zawiera też dane, oczekiwania i zapisane odpowiedzi testowe, do których odwołują się poziomy.

Zapisz, co przetestowałeś i skąd to wiesz: scenariusz, konfigurację (hash eksportu workflow, wersje kart), swoje oczekiwanie, obserwację i rodzaj dowodu, jaki masz. Rozdzielaj test w Advanced Test, odosobnioną kontrolę źródła, rzeczywisty przebieg dokumentu, odbiór u odbiorcy i przetworzenie w ERP, a kroki, których nie przetestowałeś, pozostaw jako otwarte.
