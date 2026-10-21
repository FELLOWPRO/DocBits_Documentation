# Karty logiczne: zmienne, konwersje, JSON i wyzwalacze

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-e019409102f9-pl.png" alt="Karty konwersji i JSON w bibliotece. Karty zmiennych organizacji wymagają Advanced Builder; widoczne szablony zależą także od wydania. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Karty konwersji i JSON w bibliotece. Karty zmiennych organizacji wymagają Advanced Builder; widoczne szablony zależą także od wydania. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

Użyj tych kart w Advanced Workflow Builder, gdzie dostępna jest wybrana karta. Widoczność karty zależy od wersji i włączonych szablonów. Poniższe odniesienia opisują wersję 2. Porównując jej pola z tym przewodnikiem, należy pamiętać o wersji zapisanej w istniejącym przepływie pracy.

## Wybierz odpowiedni sklep wartościowy

Zmienna przepływu pracy organizacji wybrana z panelu Zmienne jest współużytkowana przez przepływy pracy i zapisywana niezależnie od obszaru roboczego. Nazwany tag używany przez karty konwersji, JSON i porównania tagów należy do bieżącego kontekstu wykonania. Utworzenie tagu nie powoduje utworzenia zmiennej organizacyjnej. Wprowadź nazwę tagu bez prefiksu pamięci wewnętrznej. Pole dokumentu to trzecie, osobne źródło danych.

Zmienna organizacyjna i znacznik wykonania pozostają oddzielne, nawet jeśli ich nazwy są zgodne. Wybierz kompatybilne pole zmiennej lub jawnie podaj wartość, jakiej oczekuje karta odbiorcza. Zobacz [Zmienne](../advanced-workflow/variables.md), aby zapoznać się z zakresem organizacji i natychmiastową trwałością.

## Działania zmiennych organizacji

Najpierw utwórz zmienną odpowiedniego typu i wybierz ją na karcie. Brak odniesienia do zmiennej zgłasza `MISSING_VARIABLE`. Karty ustawiające zmienne zapisują poprzednią i nową wartość w dzienniku karty. Unikaj prawdziwych danych osobowych lub poufnych w wartościach testowych i udostępnianych dziennikach.

| Karta | Wymagane dane wejściowe | Wynik i przykład | Awaria lub przypadek graniczny |
| --- | --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Zmienna tekstowa i `value` | Przechowuje tekst; na przykład ustaw etykietę routingu na `review`. | Brakująca wartość różni się od celowo pustej wartości tekstowej. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Zmienna typu Numer i numeryczna `value` | Przechowuje skończoną liczbę; na przykład ustaw próg na `1000.50`. | Nieprawidłowy tekst numeryczny, nieskończoność i NaN są odrzucane. Użyj kropki dziesiętnej bez symbolu waluty. |
| `ACTION_LOGIC_CALC_NUMBER` | Zmienna liczbowa i `expression` | Przechowuje wynik arytmetyczny; `(100 + 20) / 2` daje `60`. | Obsługuje literały numeryczne, nawiasy, `+`, `-`, `*`, `/`, `%` i `**`. Nazwy, wywołania funkcji i odniesienia do pól dokumentu nie są akceptowane w wyrażeniu. Nieprawidłowe wyrażenia lub dzielenie przez zero nie powiodło się. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Zmienna Tak/Nie i `value` | Ustawia flagę na Tak lub Nie. | Użyj wartości logicznej oferowanej przez kartę, a nie przetłumaczonego synonimu w wolnym tekście. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Tak/Nie zmienna | Odwraca bieżącą wartość; Tak staje się Nie. | Zainicjuj zmienną przed poleganiem na konkretnym pierwszym wyniku. |

### Akcja odniesienia do dokumentu

`ACTION_LOGIC_SET_DOCUMENT_VAR` przechowuje bieżący identyfikator dokumentu w wybranej zmiennej Dokumentu. Wymaga aktualnego dokumentu; bez niego zgłasza `NO_DOCUMENT`. Wyzwalany przepływ pracy otrzymuje identyfikator dokumentu, a nie serializowany obiekt dokumentu. Sprawdzona implementacja nie ma rozstawionego szablonu karty interfejsu użytkownika dla tej akcji, więc nie spodziewaj się, że pojawi się ona w każdym selektorze kart. Używaj go tylko wtedy, gdy administrator potwierdzi, że dostępny jest pasujący szablon; wprowadzenie identyfikatora dokumentu do formularza tworzenia zmiennej nie zastępuje.

## Tagi i konwersje typów

Akcje te korzystają z nazw znaczników w bieżącym kontekście wykonania. Utwórz znacznik wejściowy przed jego przeczytaniem. Brakujący znacznik wejściowy lub brakująca nazwa zgłasza `MISSING_VARIABLE`; nieprawidłowa konwersja numeryczna zgłasza błąd konfiguracji. Dane wyjściowe to nowy lub nadpisany znacznik, a nie wyodrębnione pole dokumentu.

| Karta | Wejścia | Dane wyjściowe i przykład |
| --- | --- | --- |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | `tag_name`, `value` | Tworzy znacznik tekstowy; `raw_amount` o wartości `125.50`. Dozwolona jest pusta wartość tekstowa. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | `input_tag`, `output_tag` | Konwertuje `125.50` na liczbę `125.5`. Wartość logiczna zmienia się na `1` lub `0`. Tekst taki jak `EUR 125,50` nie jest prawidłowym wejściem numerycznym. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | `input_tag`, `output_tag` | Konwertuje zapisaną wartość na tekst. Nie formatuje waluty ani nie lokalizuje separatorów dziesiętnych. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | `input_tag`, `output_tag` | Bezpośrednio konwertuje istniejącą wartość logiczną; liczba różna od zera staje się prawdą, a zero staje się fałszem. Użyj `true` lub `false`, aby zapewnić przewidywalne wprowadzanie tekstu i przetestuj inne akceptowane reprezentacje. |

### Przykład konwersji

1. Utwórz znacznik tekstowy `raw_amount` o wartości `125.50`.
2. Konwertuj `raw_amount` na liczbę, zapisując do `amount_number`.
3. Użyj liczby większej niż przy `tag_name` ustawionym na `amount_number` i `value` ustawionym na `100`.
4. Sprawdź, czy warunek jest pomyślny dla `125.50`, nie dla `100` i zgłasza błąd konwersji dla `EUR 125,50` w kroku 2.

## Odczytaj wartości z JSON

Wszystkie trzy odczytane karty zajmują `json_text`, `json_path` i `output_tag`. Pomimo swojej nazwy, `json_text` jest nazwą znacznika zawierającego JSON, a nie polem do wklejenia prawdziwego dokumentu JSON. Najpierw utwórz ten znacznik, na przykład za pomocą opcji Utwórz znacznik tekstowy.

Ścieżki to klucze oddzielone kropkami i indeksy list liczone od zera: `invoice.lines.0.amount`. Nie używaj składni JSONPath, takiej jak `$.invoice.lines[0].amount`. Jeśli brakuje klucza, indeks jest nieprawidłowy lub JSON jest nieprawidłowy, wynikiem jest `ERROR_CARD_SETUP`; brakujący znacznik źródłowy zgłasza `MISSING_VARIABLE`.

| Karta | Wyjście |
| --- | --- |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Wartość liczbowa; tekst numeryczny jest konwertowany, a wartość logiczna przyjmuje postać `1` lub `0`. Nieprawidłowy tekst numeryczny nie powiódł się. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Reprezentacja tekstowa wybranej wartości. Nie jest to obietnica serializacji JSON dla zagnieżdżonych obiektów. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Wartość logiczna; tekst `true`, `1` lub `yes` jest prawdziwy po małych literach, podczas gdy inny tekst jest fałszywy. Liczby podążają za swoją wartością zerową/niezerową. |

W przypadku znacznika `payload` zawierającego następujący kod JSON, wczytanie `invoice.lines.0.amount` do `amount` z JSON na numer daje `125.5`:

```json
{"invoice":{"lines":[{"amount":"125.50"}],"approved":false}}
```

Przetestuj także nieistniejącą ścieżkę, indeks spoza zakresu i zniekształcony JSON. Nieudany odczyt nie może być traktowany jako prawidłowe zero lub pomyślne zatwierdzenie.

## Zaktualizuj JSON

Cztery karty zapisu zajmują `json_tag`, `json_path` i `value`. `json_tag` nazywa istniejący tag zawierający JSON. Aktualizują ten tag za pomocą serializowanego JSON. Obowiązuje ta sama składnia ścieżki oddzielonej kropkami; można utworzyć brakujące klucze obiektów pośrednich, ale indeksy list muszą identyfikować istniejące elementy. Nie rozszerzają listy ani nie obsługują ścieżek z symbolami wieloznacznymi.

| Karta | Wartość i efekt |
| --- | --- |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Wartość liczbowa, taka jak `125.5`; przechowuje numer JSON. Nieprawidłowy tekst numeryczny nie powiódł się. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Tekst, taki jak `review`; przechowuje ciąg JSON. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Tekst `true`, `1` lub `yes` ustawia wartość true po małych literach; inny tekst ustawia wartość false. Preferuj `true` i `false`. |
| `ACTION_LOGIC_JSON_SET_JSON` | Prawidłowy JSON, taki jak `{"status":"review"}`; wstawia tę przeanalizowaną wartość, a nie jej cytowany tekst. Nieprawidłowy JSON kończy się niepowodzeniem. |

Na przykład ustaw ścieżkę `invoice.approved` na `true` w `payload` z ustawieniem JSON Boolean. Następnie przeczytaj tę samą ścieżkę z JSON do Boolean i sprawdź, czy to prawda. Przed kontynuowaniem należy zdiagnozować brakujący tag źródłowy, nieprawidłowy JSON lub nieprawidłową ścieżkę w dzienniku karty.

## Warunki

Wszystkie sześć poniższych warunków to wersja 2. Fałszywy warunek jest wynikiem biznesowym, a nie pomyślnym działaniem lub błędem wykonania. W sekwencji warunków w stylu standardowym uniemożliwia wykonanie następujących działań; w zaawansowanym przepływie pracy połącz wynik z zamierzoną gałęzią.

| Karta | Pola | Ocena i ważna granica |
| --- | --- | --- |
| `CONDITION_LOGIC_VALUE_EQUALS` | `tag_name`, `value` | Dokładnie porównuje reprezentacje tekstu, łącznie z wielkością liter. Nie używaj tego do sprawdzania obecności: brakujący tag nie jest automatycznie zgłaszany jako błąd. |
| `CONDITION_LOGIC_BOOLEAN_IS` | `tag_name` | Sprawdza, czy tag jest prawdziwy. Brakujący tag daje wartość false. Aby uzyskać wiarygodne wyniki, użyj prawdziwej wartości logicznej. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | `tag_name`, `value` | Wyszukiwanie podciągów z uwzględnieniem wielkości liter. Brakujący tag jest traktowany jako pusty tekst. Pasuje pusty ciąg wyszukiwania; zawsze celowo ustawiaj wartość wyszukiwania. |
| `CONDITION_LOGIC_NUMBER_LESS` | `tag_name`, numeryczne `value` | Ściśle mniej niż. Brakujący znacznik lub pominięta wartość porównawcza ma domyślnie wartość zero; nieprawidłowe dane liczbowe oznaczają błąd konfiguracji. |
| `CONDITION_LOGIC_NUMBER_GREATER` | `tag_name`, numeryczne `value` | Ściśle większe niż. Wartość równa progowi nie spełnia tego warunku. Obowiązują te same wartości domyślne zera i zachowanie związane z błędami numerycznymi. |
| `CONDITION_LOGIC_EXPRESSION` | `value1`, `operator`, `value2` | Obsługuje `==`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not_contains`. Najpierw próbuje porównać numerycznie, a następnie porównuje tekst. Nie jest to dowolne pole wyrażenia Pythona. |

Dla liczby większej niż `100` przetestuj `99`, `100` i `101`. Dla tekstu zawierającego `ABC`, test `ABC`, `abc` i puste wyszukiwanie. Sprawdź zarówno gałąź, jak i kłodę; szary węzeł został pominięty, co dowodzi niepomyślnego porównania.

## Wyzwalacze

| Karta | Konfiguracja | Kiedy pasuje |
| --- | --- | --- |
| `CONDITION_LOGIC_VAR_CHANGED` | Wybierz zmienną organizacyjną. Przechowywane odwołanie wykorzystuje swój identyfikator, więc zmiana nazwy zmiennej nie powoduje celowej zmiany celu. | Podane wartości bieżące i poprzednie zmiennych różnią się. Powtarzanie tej samej wartości nie jest zmianą. Brakujące odwołanie do zmiennej zgłasza `MISSING_VARIABLE`. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Opcjonalnie `event_name`. | Ładunek elementu webhook jest obecny w kontekście wykonywania przepływu pracy. W przypadku nazwy wartość `event` ładunku musi dokładnie odpowiadać; bez nazwy pasują wszystkie dostarczone zdarzenia webhooka. Brak zdarzenia oznacza fałsz. |

Wybranie zdarzenia webhook nie powoduje utworzenia publicznego punktu końcowego webhooka ani jego uwierzytelnienia. Twoja integracja musi dostarczać zdarzenie przez skonfigurowany punkt wejścia. Przetestuj pasujące zdarzenie, inne zdarzenie i brak zdarzenia. W przypadku wyzwalacza zmiennej przetestuj rzeczywistą zmianę wartości i niezmienioną wartość i unikaj łańcucha, który wielokrotnie zapisuje tę samą wspólną zmienną.

## Testuj i diagnozuj

Sprawdź poprawność wykresu, przetestuj każdą gałąź za pomocą reprezentatywnych danych wejściowych i sprawdź [Dzienniki przepływu pracy](../workflow-logs.md). Uwzględnij brakujące tagi, nieprawidłowy JSON, nieprawidłowe typy zmiennych, granice liczbowe i fałszywe warunki. Test bez dokumentu nie może wykazać działania zależnego od dokumentu. Przed skorzystaniem z automatycznego wykonania sprawdź ponownie wersję zapisanej karty i stan jej włączenia.

<!-- workflow-card-logic-examples-20261021 -->

## Sprawdzone przykłady dla każdej karty logicznej

Są to przykładowe dane wejściowe i oczekiwane wyniki dla wersji 2. Używaj kart ze zmiennymi organizacyjnymi tylko wtedy, gdy Advanced Builder udostępnia ich szablony.

| Karta | Przykładowa konfiguracja | Oczekiwany wynik i kontrprzykład |
| --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Ustaw zmienną tekstową organizacji `routing_label` na `review`. | Wspólna zmienna zawiera `review`. Późniejszy przepływ pracy może odczytać tę samą zmienną organizacyjną. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Ustaw zmienną liczbową `approval_limit` na `1000.50`. | Przechowuje cyfrę `1000.5`. Tekst `EUR 1000,50` nie jest prawidłowym wejściem numerycznym. |
| `ACTION_LOGIC_CALC_NUMBER` | Zapisz wyrażenie `(100 + 20) / 2` w zmiennej liczbowej `calculated_limit`. | Wynikiem jest `60`. Nazwa pola dokumentu lub dzielenie przez zero nie jest prawidłowym substytutem. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Ustaw zmienną Tak/Nie `review_required` na oferowaną wartość logiczną `true`. | Flaga organizacji jest prawdziwa. Aby to wyczyścić, użyj wartości logicznej `false` w osobnym przypadku. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Zacznij od zmiennej organizacyjnej `demo_flag` równej `true`. | Jedno wykonanie daje `false`. Ponowne wykonanie powoduje, że uzyskuje się `true`, więc wielokrotne wykonanie nie jest idempotentne. |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | Utwórz znacznik wykonania `raw_amount` z tekstem `125.50`. | Znacznik zawiera ten tekst w tym wykonaniu; nie jest to nowa zmienna organizacyjna ani pole dokumentu. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | Konwertuj znacznik wejściowy `raw_amount` zawierający `125.50` na znacznik wyjściowy `amount_number`. | Dane wyjściowe są numeryczne `125.5`. `EUR 125,50` powoduje błąd konwersji. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | Konwertuj znacznik numeryczny `amount_number` zawierający `125.5` na `amount_text`. | Wynikiem jest tekst `125.5`; nie jest zlokalizowana jako kwota w walucie. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | Konwertuj numeryczny znacznik wejściowy zawierający `1` na znacznik wyjściowy `has_value`. | Dane wyjściowe są prawdziwe. Numeryczne `0` daje fałsz. |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Utwórz znacznik źródłowy `payload` za pomocą `{"invoice":{"amount":"125.50"}}`; przeczytaj ścieżkę `invoice.amount` do `amount_number`. | Dane wyjściowe są numeryczne `125.5`. Brak ścieżki oznacza błąd, a nie prawidłowe zero. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Użyj znacznika źródłowego `payload` zawierającego `{"invoice":{"status":"review"}}` i ścieżkę `invoice.status`. | Znacznik wyjściowy zawiera tekst `review`. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Użyj znacznika źródłowego `payload` zawierającego `{"invoice":{"approved":false}}` i ścieżkę `invoice.approved`. | Dane wyjściowe to wartość logiczna false. Brakująca ścieżka to nie to samo, co zapisana wartość false. |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Użyj istniejącego tagu JSON `payload` zawierającego `{"invoice":{}}`; ustaw `invoice.total` na `125.5`. | Znacznik zawiera sumę liczbową JSON, a nie ciąg liczbowy w cudzysłowie. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Użyj istniejącego tagu JSON `payload` zawierającego `{"invoice":{}}`; ustaw `invoice.status` na `review`. | Zapisana wartość JSON to ciąg znaków: `{"invoice":{"status":"review"}}`. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Użyj istniejącego tagu JSON `payload` zawierającego `{"invoice":{}}`; ustaw `invoice.approved` z tekstem `true`. | Zapisana wartość JSON to wartość logiczna true. Użyj `false`, aby to wyczyścić. |
| `ACTION_LOGIC_JSON_SET_JSON` | Użyj istniejącego tagu JSON `payload` zawierającego `{"invoice":{}}`; ustaw `invoice.metadata` na prawidłowy JSON `{"source":"demo"}`. | Wstawiona wartość jest obiektem. Należy zgłosić nieprawidłowy kod JSON, a nie zapisać go jako pomyślną aktualizację obiektu. |
| `CONDITION_LOGIC_VALUE_EQUALS` | Utwórz znacznik `route` z tekstem `review` i porównaj go z `review`. | To mija. Porównanie z `Review` kończy się niepowodzeniem, ponieważ w porównaniu rozróżniana jest wielkość liter. |
| `CONDITION_LOGIC_BOOLEAN_IS` | Użyj znacznika `review_required` zawierającego rzeczywistą wartość logiczną `true`. | To mija; false lub brakujący znacznik nie pozwala na ustalenie prawdziwego wyniku. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | Użyj tagu `note` z tekstem `manual review` i wyszukaj `review`. | To mija. Wyszukiwanie wielkich liter `REVIEW` nie powiodło się. Pusty ciąg wyszukiwania pasuje i należy go unikać, chyba że jest to zamierzone. |
| `CONDITION_LOGIC_NUMBER_LESS` | Użyj znacznika numerycznego `amount` równego `50` i wartości porównawczej `100`. | To mija. Wartość `100` nie spełnia ścisłego porównania typu „mniej niż”. |
| `CONDITION_LOGIC_NUMBER_GREATER` | Użyj znacznika numerycznego `amount` równego `125` i wartości porównawczej `100`. | To mija. `100` nie przechodzi ścisłego porównania przez więcej niż. |
| `CONDITION_LOGIC_EXPRESSION` | Wybierz wartość1 `120`, operator `>` i wartość2 `100`. | Porównanie liczbowe przebiega pomyślnie. Użyj `80` jako wartości 1 dla fałszywej gałęzi; nie jest to swobodne wyrażenie w języku Python. |
| `CONDITION_LOGIC_VAR_CHANGED` | Wybierz zmienną organizacyjną, której poprzednia wartość to `new`, a podana bieżąca wartość to `review`. | Zdarzenie o zmienionej wartości jest zgodne. Powtarzanie `review`, ponieważ zarówno poprzednia, jak i bieżąca wartość nie są zgodne. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Wybierz nazwę zdarzenia `invoice.ready` i podaj skonfigurowane zdarzenie integracyjne z ładunkiem `{"event":"invoice.ready"}`. | Pasuje. `{"event":"invoice.updated"}` i żadne zdarzenie nie pasuje. Karta nie tworzy punktu końcowego webhooka. |

Opcjonalna akcja odniesienia do dokumentu `ACTION_LOGIC_SET_DOCUMENT_VAR` nie ma szablonu zaszczepionego w sprawdzanym źródle. Jeśli administrator udostępnia obsługiwany szablon, wybierz zmienną Dokument i wykonaj z bieżącym dokumentem demonstracyjnym: przechowuje on identyfikator tego dokumentu. Bez dokumentu zgłasza `NO_DOCUMENT`. Nie traktuj jej jako dostępnej karty tylko dlatego, że istnieje implementacja.
