# Panel

**Panel przepływu pracy** to strona główna obszaru przepływów pracy. Pokazuje, jak działają Twoje przepływy pracy — łączne liczby uruchomień, wskaźniki sukcesu i niepowodzeń, wykres uruchomień w czasie oraz ostatnią aktywność — i daje dostęp do listy przepływów pracy, menedżera testów oraz Card SDK.

Poniższe fragmenty pokazują metryki wolumenu, wyniki uruchomień i wykres uruchomień. Ostatnia aktywność i elementy nawigacji znajdują się poza tymi wycinkami.

<figure><img src="../../.gitbook/assets/workflow-kpi-volume-pl-20261112.png" alt="Metryki wolumenu: przepływy pracy wykonane dzisiaj, przepływy pracy utworzone w wybranym okresie oraz łączna liczba przebiegów z okresem ponad 31 dni."><figcaption><p>Metryki wolumenu: przepływy pracy wykonane dzisiaj, przepływy pracy utworzone w wybranym okresie oraz łączna liczba przebiegów (w tym przykładzie ponad 31 dni).</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/workflow-kpi-outcomes-pl-20261112.png" alt="Wyniki uruchomień: udane biegi, wskaźnik sukcesu i współczynnik niepowodzeń wraz z liczbą przebiegów, na której są liczone."><figcaption><p>Wyniki uruchomień: udane biegi, wskaźnik sukcesu i współczynnik niepowodzeń, wraz z liczbą przebiegów, na której są liczone.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/workflow-chart-pl-20261112.png" alt="Przebiegi przepływu pracy w siedmiu widocznych miesiącach; serie Sukces i Niepowodzenie są pokazane osobno."><figcaption><p>Przebiegi przepływu pracy w siedmiu widocznych miesiącach; serie Sukces i Niepowodzenie są pokazane osobno.</p></figcaption></figure>

## Zakładki

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.mp4" %}

**Film:** Wyszukiwanie i filtrowanie na panelu Workflows · 1:04 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Szukanie po nazwie** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.mp4#t=0.25)

Na karcie Lista przepływów pracy pole wyszukiwania znajduje Workflows po nazwie. Wpisz część nazwy, a na liście zostaną tylko pasujące Workflows.

**Wyczyść wyszukiwanie** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.mp4#t=12.683)

Wyczyść wyszukiwanie, aby znów zobaczyć wszystkie Workflows. Wyszukiwanie jest też w adresie strony, więc po powrocie do listy zostaje.

**Daty i Workflow** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.mp4#t=26.25)

Na zakładce Panel filtry u góry decydują, co zliczają liczby i wykres: data rozpoczęcia i zakończenia, domyślnie ostatni miesiąc, oraz wszystkie Workflows albo jeden.

**Porównanie dwóch okresów** · [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-filtering/v1/pl.mp4#t=43.016)

Opcja Porównaj dodaje drugi okres: wpisz jego datę rozpoczęcia i zakończenia. Każda liczba pokazuje wtedy też wartość tego okresu i różnicę. Ta przeglądarka zapamięta filtry na następną wizytę.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4" %}

**Film:** Pobieranie i przesyłanie Workflow jako JSON · 1:11 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Pobierz jako JSON** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4#t=0.25)

Aby zachować kopię Workflow, otwórz jego akcje na liście i wybierz Pobierz. Otrzymasz jeden plik JSON z nazwą, typem oraz wszystkimi kartami i połączeniami.

**Kopia lub przeniesienie** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4#t=14.95)

Użyj go jako kopii zapasowej albo do przeniesienia Workflow zbudowanego i przetestowanego w środowisku testowym.

**Importuj przepływ pracy** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4#t=27.25)

Aby go przywrócić, kliknij Importuj przepływ pracy i wybierz pliki JSON, do dziesięciu naraz.

**Trafia wyłączony** · [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4#t=37.383)

Przesłany Workflow trafia wyłączony, więc nic nie działa, zanim go nie sprawdzisz.

**Sprawdź użytkowników, grupy i tabele** · [0:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-json/v1/pl.mp4#t=47.016)

Karty wskazujące użytkowników, grupy, podorganizacje lub tabele decyzyjne odwołują się do nich przez wewnętrzny identyfikator. Po przesłaniu z innego środowiska otwórz karty i sprawdź, czy nadal są ustawione tak, jak chcesz. Potem przetestuj go i włącz.

</details>

- **Panel** — metryki uruchomień i ostatnia aktywność (pokazane powyżej).
- **Lista przepływów pracy** — każdy przepływ pracy wraz z typem, kolejnością wykonania i wyzwalaczem. Przycisk **Nowy przepływ pracy** w pasku narzędzi tworzy nowy przepływ pracy.
- **Lista menedżerów testów** — scenariusze testowe, które walidują Twoje przepływy pracy; uruchom je przyciskiem **Uruchom wszystkie testy**.
- **Licencja** — informacje o licencjonowaniu przepływów pracy.
- **Card SDK** — tworzenie i przesyłanie własnych kart przepływów pracy (zobacz [Card SDK](card-sdk.md)).

Pasek narzędzi oferuje także **Szablony**, który otwiera bibliotekę [szablonów przepływu pracy](standard-workflow-builder.md#workflow-templates), oraz **Importuj przepływ pracy**, który importuje przepływ pracy z pliku JSON.

**Zarządzanie testami** pozwala zapisywać scenariusze testowe dla każdego przepływu pracy i uruchamiać je razem, dzięki czemu możesz sprawdzić, czy Twoje przepływy pracy nadal działają poprawnie po wprowadzeniu zmian:

<figure><img src="../../.gitbook/assets/prior-u032-pl.png" alt="Lista scenariuszy testowych przepływów."><figcaption><p>Lista scenariuszy testowych przepływów.</p></figcaption></figure>

## Następne kroki

- Zbuduj liniową automatyzację za pomocą buildera **Standardowy przepływ**.
- Zbuduj rozgałęziony przepływ za pomocą buildera **Zaawansowany przepływ pracy**.
