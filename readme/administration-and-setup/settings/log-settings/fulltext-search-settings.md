# Ustawienia Wyszukiwania Pełnotekstowego

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Ustawienia Wyszukiwania Pełnotekstowego"><figcaption><p>Ustawienia Wyszukiwania Pełnotekstowego — Okno „Wymagany Moduł"</p></figcaption></figure>

Ustawienia Wyszukiwania Pełnotekstowego określają, co DocBits indeksuje i jak ta treść staje się przeszukiwalna w dokumentach, danych podstawowych ERP i szablonach. Strona ustawień otwiera się tylko wtedy, gdy **moduł Wyszukiwania Pełnotekstowego** jest włączony — zobacz [Wyszukiwanie Pełnotekstowe](../document-processing/module/fulltext-search.md), aby poznać język zapytań skierowany do użytkownika.

## Wymagania wstępne

Moduł Wyszukiwania Pełnotekstowego musi być włączony w **Ustawienia → Przetwarzanie Dokumentów → Moduł → Pulpity → Wyszukiwanie pełnotekstowe**. Jeśli moduł nie jest włączony, okno proponuje:

* **Przejdź do Modułów** — Otwórz stronę konfiguracji Modułów, aby przejrzeć ustawienia.
* **Włącz teraz** — Włącz moduł Wyszukiwania Pełnotekstowego bezpośrednio (uruchamia subskrypcję DocSearch).

Sama strona ustawień staje się dostępna, gdy moduł jest aktywny.

## Układ strony

Strona ustawień jest podzielona na trzy zakładki, z których każda obejmuje inny typ treści, który Wyszukiwanie Pełnotekstowe może indeksować.

### Zakładka „Dokumenty"

Zakładka Dokumenty obejmuje wszystko związane z indeksowaniem przetworzonych dokumentów:

* **Statystyki indeksowania** — sumy dokumentów zindeksowanych i oczekujących, odświeżane na żądanie.
* **Preferencje wektorowe** — trzy przełączniki na poziomie organizacji decydujące, czy indeksowanie wektorowe działa równolegle z indeksem tekstowym dla dokumentów. Indeksowanie wektorowe zasila tryb zapytania `vector:` oraz funkcję „Znajdź podobne".
* **Akcje reindeksacji** — rozpocznij pełną lub przyrostową reindeksację. Podczas trwania reindeksacji widzisz postęp na żywo (dokumenty na minutę, szacowany czas), bieżący stan strumienia oraz ostatni błąd (jeśli wystąpił).
* **Diagnostyka synchronizacji** — diagnostyka na żądanie dla przypadków, gdy indeks wydaje się być niesynchronizowany z bazą dokumentów.

<mark>Reindeksacja nie jest destrukcyjna — istniejące wyszukiwanie nadal działa, podczas gdy nowy indeks jest budowany.</mark>

### Zakładka „ERP"

Zakładka ERP zarządza indeksowaniem danych podstawowych ERP — dostawców, klientów, towarów i podobnych jednostek. Każda jednostka ma własny przełącznik:

* **Indeksowanie** — indeksuje jednostkę tekstowo, dzięki czemu jest przeszukiwalna z pulpitu.
* **Wektor** — indeksuje jednostkę wektorowo, dzięki czemu można ją dopasować zapytaniami semantycznymi.

Akcja **Przełącz wszystko** u góry listy stosuje ten sam stan włączenia/wyłączenia do wszystkich jednostek na raz. Indeksowanie rusza w tle; wskaźnik w każdym wierszu pokazuje, kiedy trwa.

### Zakładka „Szablony"

Zakładka Szablony wymienia wersje szablonów znane indeksowi Wyszukiwania Pełnotekstowego. Użyj tego widoku, aby po ponownym wdrożeniu potwierdzić, że wersje szablonów, od których zależysz, są obecne w indeksie.

## Co jest indeksowane

Po włączeniu i skonfigurowaniu Wyszukiwanie Pełnotekstowe pozwala użytkownikom:

* Wyszukiwać w całej treści dokumentu (nie tylko w polach metadanych).
* Znajdować dokumenty po tekście zawartym w przesłanych plikach.
* Używać zaawansowanych operatorów wyszukiwania do precyzyjnych zapytań.
* Korzystać z wyników wyszukiwania bezpośrednio z pulpitu.
* Używać wyszukiwania semantycznego (prefiks `vector:`), gdy indeksowanie wektorowe jest aktywne dla danego typu treści.

Pełna referencja języka zapytań — w tym zapytania zakresowe, inteligentne filtry i tryb wyszukiwania AI — znajduje się na stronie modułu [Wyszukiwanie Pełnotekstowe](../document-processing/module/fulltext-search.md).
