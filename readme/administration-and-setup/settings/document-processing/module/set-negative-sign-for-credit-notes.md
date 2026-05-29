# Ustaw znak ujemny dla not kredytowych

### Przegląd

Ustawienie **Ustaw znak ujemny dla not kredytowych** (Set Negative Sign for Credit Notes) zapewnia, że **noty kredytowe** są zapisywane z **kwotami ujemnymi**. Nota kredytowa cofa lub zwraca część faktury, więc w księgowości jej wartości powinny zmniejszać sumy — czyli być ujemne. Gdy to ustawienie jest włączone, DocBits automatycznie stosuje ten znak ujemny.

To ustawienie jest **domyślnie włączone**.

### Co robi to ustawienie?

Gdy dokument zostanie rozpoznany jako **nota kredytowa**, DocBits automatycznie zamienia jego kwoty na wartości ujemne podczas przetwarzania. Dotyczy to pól pieniężnych, w tym kwot netto, kwot podatku i sum (np. kwota netto, kwota podatku, łączna kwota podatku, łączna kwota netto i kwota całkowita).

* **Włączone (domyślnie)** — Kwoty not kredytowych są zapisywane jako wartości ujemne (np. `150,00` staje się `-150,00`). Zwykłe faktury nie są zmieniane.
* **Wyłączone** — Kwoty pozostają dokładnie takie, jakie odczytano z dokumentu, bez zmiany znaku.

{% hint style="info" %}
Dotyczy to wyłącznie dokumentów zidentyfikowanych jako **noty kredytowe**. Zwykłe faktury zawsze pozostają niezmienione.
{% endhint %}

### Korzyści

* **Poprawna księgowość**: Noty kredytowe zmniejszają salda, więc wartości ujemne są tym, czego oczekują systemy księgowe i ERP.
* **Brak ręcznej edycji**: Zespół nie musi ręcznie odwracać znaku przy każdej nocie kredytowej.
* **Spójność**: Każda nota kredytowa jest traktowana tak samo w całej organizacji.

### Jak używać

1. Przejdź do **Ustawienia**.
2. Wybierz **Przetwarzanie dokumentów**.
3. Wybierz **Moduł**.
4. Otwórz sekcję **Typ dokumentu**.
5. Znajdź **Ustaw znak ujemny dla not kredytowych** i przełącz suwak.

### Kiedy używać tej funkcji

* **Pozostaw włączone**, jeśli Twój system księgowy lub ERP oczekuje, że noty kredytowe będą przychodzić z kwotami ujemnymi (jest to najczęstsza konfiguracja).
* **Wyłącz** tylko wtedy, gdy system docelowy sam obsługuje znak lub oczekuje, że kwoty not kredytowych pozostaną dodatnie.
