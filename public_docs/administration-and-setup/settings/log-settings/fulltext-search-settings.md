# Ustawienia Wyszukiwania Pełnotekstowego

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Ustawienia Wyszukiwania Pełnotekstowego w piaskownicy z oknem informującym, że wymagany jest moduł, oraz przyciskami Go to Modules i Enable Now"><figcaption><p>Gdy Wyszukiwanie Pełnotekstowe jest wyłączone, to okno wyjaśnia kolejne kroki.</p></figcaption></figure>

Ustawienia Wyszukiwania Pełnotekstowego określają, co DocBits indeksuje i jak udostępnia tę treść do wyszukiwania w dokumentach, danych podstawowych ERP i szablonach. Strona ustawień wyświetla okno wymagania, dopóki **moduł Wyszukiwania Pełnotekstowego** nie zostanie włączony — zobacz [Wyszukiwanie Pełnotekstowe](../document-processing/module/fulltext-search.md), aby poznać język zapytań dla użytkownika.

## Wymagania wstępne

Moduł Wyszukiwania Pełnotekstowego musi być aktywowany w **Settings → Module → Dashboards & Analytics → Full text search**. Jeśli moduł nie jest włączony, okno oferuje trzy działania:

* **Help (?)** — otwiera dokumentację Wyszukiwania Pełnotekstowego w nowej karcie, zanim zmienisz jakiekolwiek ustawienie.
* **Go to Modules** — otwiera ustawienia modułu Dashboards & Analytics, aby przejrzeć konfigurację.
* **Enable Now** — otwiera okno subskrypcji. Przejrzyj i potwierdź to okno, zanim moduł zostanie włączony; samo kliknięcie tego przycisku nie włącza modułu.

Strona ustawień sama staje się dostępna, gdy moduł jest aktywny.

## Układ strony

Strona ustawień jest podzielona na trzy karty: **Documents**, **ERP** i **Templates**. Każda karta obejmuje inny typ treści, który Wyszukiwanie Pełnotekstowe może indeksować.

### Karta Documents

Karta Documents obejmuje wszystko, co dotyczy indeksowania przetworzonych dokumentów:

* **Indexing statistics** — sumy dokumentów zindeksowanych i oczekujących, odświeżane na żądanie.
* **Vector preferences** — trzy przełączniki na poziomie organizacji, które określają, czy indeksowanie wektorowe działa równolegle z indeksem tekstowym dokumentów. Indeksowanie wektorowe obsługuje tryb zapytania `vector:` oraz funkcję „Find Similar”.
* **Reindex actions** — uruchamiają pełną lub przyrostową reindeksację. Podczas trwania reindeksacji widoczny jest postęp na żywo (dokumenty na minutę, ETA), bieżący stan strumienia oraz ostatni błąd (jeśli wystąpił).
* **Sync diagnostics** — diagnostyka na żądanie w przypadkach, gdy indeks wydaje się niespójny z bazą dokumentów.

<mark>Reindeksacja nie powoduje utraty danych — istniejące wyszukiwanie działa dalej, podczas gdy nowy indeks jest odbudowywany.</mark>

### Karta ERP

Karta ERP steruje indeksowaniem danych podstawowych ERP — dostawców, klientów, towarów i podobnych encji. Każda encja ma własny przełącznik:

* **Indexing** — indeksuje encję tekstowo, dzięki czemu można jej szukać w Dashboard.
* **Vector** — indeksuje encję wektorowo, dzięki czemu można ją dopasować zapytaniami semantycznymi.

Użyj akcji **Toggle all** u góry listy, aby zastosować ten sam stan włączenia lub wyłączenia do wszystkich encji jednocześnie. Indeksowanie uruchamia się w tle; wskaźnik w każdym wierszu pokazuje, kiedy trwa.

### Karta Templates

Karta Templates wymienia wersje szablonów znane indeksowi Wyszukiwania Pełnotekstowego. Użyj tego widoku, aby po ponownym wdrożeniu potwierdzić, że wersje szablonów, od których zależysz, są obecne w indeksie.

## Co jest indeksowane

Po włączeniu i skonfigurowaniu Wyszukiwanie Pełnotekstowe umożliwia użytkownikom:

* Wyszukiwanie w całej treści dokumentów (nie tylko w polach metadanych).
* Znajdowanie dokumentów po tekście zawartym w przesłanych plikach.
* Korzystanie z zaawansowanych operatorów wyszukiwania do precyzyjnych zapytań.
* Dostęp do wyników wyszukiwania bezpośrednio w Dashboard.
* Korzystanie z wyszukiwania semantycznego (prefiks `vector:`), gdy indeksowanie wektorowe jest włączone dla danego typu treści.

Pełną referencję języka zapytań — w tym zapytania zakresowe, inteligentne filtry i tryb wyszukiwania AI — znajdziesz na stronie modułu [Wyszukiwanie Pełnotekstowe](../document-processing/module/fulltext-search.md).
