# Eksportuj z alternatywnym eksportem

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## Kiedy używać tej karty

Użyj tej akcji Następnie dla alternatywnego eksportu skonfigurowanego dla bieżącego typu dokumentu. Skonfiguruj i zatwierdź tę trasę przed dodaniem akcji.

## Konfiguracja wynika z typu dokumentu

Karta nie posiada selektora konfiguracji eksportu. Odczytuje, czy włączony jest alternatywny eksport, alternatywną konfigurację eksportu i stan po eksporcie z ustawień typu dokumentu. Wewnętrznie są to `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` i `DOC_ALTERNATE_EXPORT_STATUS`.

Jawnie wyłączony alternatywny eksport powoduje niepowodzenie. Brakujące dane aktywacyjne, konfiguracja lub status wyników są zgłaszane, zamiast dyskretnie zastępować trasę domyślną. Żądanie eksportu sprawdza oczekujące zadania.

## Sprawdź wynik

Sprawdź dziennik karty, historię eksportu, status dokumentu i autoryzowane miejsce docelowe testu. Samo żądanie, przekroczenie limitu czasu lub zmiana statusu nie gwarantują, że dane dotarły do ​​miejsca docelowego. Sprawdź historię eksportu przed ponowną próbą wykonania operacji, która może spowodować utworzenie duplikatów.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Alternatywny przykład eksportu

**Konfiguracja:** Przygotuj syntetyczny typ dokumentu `DEMO_INVOICE` z włączonym alternatywnym eksportem, autoryzowaną konfiguracją eksportu testowego i żądanym statusem wyniku w ustawieniach typu dokumentu. Dodaj tę akcję Następnie po wymaganych kontrolach. Ta karta odczytuje te ustawienia; nie oferuje selektora konfiguracji eksportu.

**Oczekiwany wynik i kontrprzykład:** Akcja żąda eksportu przez tę alternatywną konfigurację i sprawdza oczekujące zadania. Sprawdź oddzielnie wynik eksportu i miejsce docelowe testu. Wyłączenie alternatywnego eksportu powoduje niepowodzenie; brak ustawienia aktywacji lub konfiguracji nie oznacza pomyślnego eksportu. Nie uruchamiaj tego przykładu w odniesieniu do miejsca docelowego rozliczania.

To jest ilustracyjna konfiguracja testu i oczekiwany wynik; nie zostało ono wykonane. Skorzystaj z danych i odbiorców skonfigurowanych w Twojej organizacji testowej.
