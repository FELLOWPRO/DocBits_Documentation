# Wyszukiwanie pełnotekstowe

Wyszukiwanie pełnotekstowe pozwala użytkownikom przeszukiwać rzeczywistą treść dokumentów i każde wyekstrahowane pole, a nie tylko nazwy plików i identyfikatory.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Okno dialogowe „Fulltext Module Required“ gdy moduł jest wyłączony"><figcaption><p>Okno «Fulltext Module Required» pojawia się na stronach zależnych od tego modułu.</p></figcaption></figure>

## Bez modułu

Gdy wyszukiwanie pełnotekstowe nie jest włączone, pasek wyszukiwania w panelu może przeszukiwać tylko niewielki zestaw pól strukturalnych. Tekst wolny porównywany jest jedynie z:

* `filename`
* `ID` dokumentu
* `invoice_id`
* `purchase_order`

Wszystko poza tymi polami jest ignorowane. Nie ma wyszukiwania po treści ani obsługi zakresów, operatorów lub filtrów inteligentnych.

## Z włączonym modułem

Włączenie wyszukiwania pełnotekstowego odblokowuje wyszukiwanie po każdym wyekstrahowanym polu dokumentu i zastępuje pasek wyszukiwania w panelu rozbudowanym językiem zapytań. Zapytania mogą łączyć filtry pól, porównania zakresów, operatory logiczne, daty względne i filtry inteligentne.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Pasek wyszukiwania w panelu z zapytaniem zakresowym i przefiltrowaną listą dokumentów"><figcaption><p>Pasek wyszukiwania w panelu obsługuje rozszerzony język zapytań. Wpisz zapytanie i naciśnij <kbd>Enter</kbd>, aby przefiltrować listę dokumentów.</p></figcaption></figure>

### Zapytania ukierunkowane na pole

Aby wyszukać w konkretnym wyekstrahowanym polu, poprzedź nazwę pola dwukropkiem. Nazwy pól zachowują konwencję API (małe litery, snake\_case) i obejmują każde pole rejestrowane przez typy dokumentów — dostawcę, metadane faktury, pozycje, pola niestandardowe.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Zapytania zakresowe

Operatory porównania działają na polach liczbowych i datowych. Obsługiwane są zarówno otwarte porównania, jak i ograniczone zakresy.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Operatory logiczne

Klauzule można łączyć za pomocą `AND`, `OR` i `NOT`, a nawiasy ustalają kolejność wykonania. Listy `IN` sprawdzają pole względem zbioru możliwych wartości.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Daty względne

Wyrażenia czasowe wyliczane w momencie wykonania zapytania. Można je stosować wszędzie, gdzie spodziewana jest data.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Filtry inteligentne

Jednowyrazowe skróty dla typowych zapytań. Działają samodzielnie lub w ramach większego wyrażenia.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — dokumenty po terminie płatności.
* `@User` — filtruj po osobie przypisanej; zamień `User` na nazwę użytkownika.
* `#INV-1234` — szybkie wyszukiwanie po identyfikatorze dokumentu.
* `$5k+` — kwoty większe niż 5 000 w walucie dokumentu.

## Funkcje pochodne

Dwa wyspecjalizowane tryby wyszukiwania są nadbudowane nad modułem wyszukiwania pełnotekstowego. Oba wymagają włączonego modułu i nie mogą działać niezależnie.

### Wyszukiwanie wektorowe

Wyszukiwanie wektorowe znajduje dokumenty semantycznie podobne do zapytania, a nie tylko zgodne leksykalnie. Panel traktuje każde zapytanie zaczynające się od `vector:` jako wyszukiwanie wektorowe, przepuszcza je przez osadzenia dokumentów i porządkuje wyniki według podobieństwa.

```
vector: frozen food invoices
```

Indeksowanie wektorowe jest sterowane niezależnie od indeksu tekstu pełnotekstowego na stronie **Ustawienia wyszukiwania pełnotekstowego**. Wyłączenie zatrzymuje generowanie osadzeń dla nowych dokumentów, ale indeks tekstowy pozostaje aktywny.

### Wyszukiwanie AI

Wyszukiwanie AI przyjmuje zapytania w języku naturalnym i wykorzystuje LLM do wyodrębnienia ustrukturyzowanych filtrów, które następnie są uruchamiane na indeksie pełnotekstowym. Poprzedź zapytanie ciągiem `ai:`.

```
ai: invoices from Ruiz over 1000 last quarter
```

Wyszukiwanie AI i wyszukiwanie wektorowe nie są wymienne: wektorowe znajduje podobną treść, AI tłumaczy język na filtry. Wyszukiwanie AI nie ma własnego przełącznika — korzysta z istniejących indeksów pełnotekstowego i wektorowego.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Strona „Ustawienia wyszukiwania pełnotekstowego“ z indeksami Documents, Vector Index i Fulltext (Text)"><figcaption><p>Ustawienia wyszukiwania pełnotekstowego. Indeks wektorowy ma własny przełącznik; indeks tekstowy działa zawsze, gdy moduł jest włączony.</p></figcaption></figure>

## Wymagania wstępne

* W tle działa infrastruktura OpenSearch, która zasila indeks.
* Przy pierwszym włączeniu modułu wszystkie istniejące dokumenty są reindeksowane. Czas zależy od liczby dokumentów w organizacji.
* Tylko administratorzy organizacji mogą włączać i wyłączać moduły.

## Jak włączyć moduł

1. Przejdź do **Ustawienia → Przetwarzanie dokumentów → Moduł**.
2. W grupie **Dashboards** włącz **Full text search**.
3. Potwierdź okno subskrypcji, jeśli się pojawi.
4. Poczekaj na zakończenie pierwszego indeksowania, zanim zaczniesz polegać na zapytaniach pełnotekstowych.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Strona „Moduły“ z przełącznikiem „Full text search“ pod grupą Dashboards"><figcaption><p>Przełącznik <strong>Full text search</strong> znajduje się w sekcji <strong>Moduł → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
Ceny modułu wyszukiwania pełnotekstowego ustala Twój opiekun handlowy DocBits. Potwierdzenie subskrypcji pojawi się przy pierwszej aktywacji modułu.
{% endhint %}

## Zobacz także

* [Ustawienia wyszukiwania pełnotekstowego](../../log-settings/fulltext-search-settings.md) — zarządzanie indeksem i przełącznik indeksu wektorowego.
* [Funkcje Fulltext i Vector Search](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — API skryptów dla `fulltext_search()` i `vector_search()`.
* [Przegląd modułów](README.md) — pełna lista opcjonalnych modułów DocBits.
