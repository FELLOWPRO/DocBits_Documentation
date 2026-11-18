# Sprawdzanie obecności i zawartości pola dokumentu

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v1-pl-pl.png" alt="Sprawdzanie obecności i zawartości pola dokumentu, Wersja 1" width="634"><figcaption><p>Wersja 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v2-pl-pl.png" alt="Sprawdzanie obecności i zawartości pola dokumentu, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pl.mp4" %}

**Film:** Karta: Pole puste czy nie · 1:00 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Pole puste czy nie** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pl.mp4#t=0.25)

Karta Pole jest sprawdza, czy pole dokumentu jest puste. Wybierz pole, na przykład Zamówienie zakupu, oraz status: puste lub nie ma w dokumencie, albo jest w dokumencie i niepuste.

**Brak liczy się jako puste** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pl.mp4#t=19.083)

Pole liczy się jako puste, gdy nie ma wartości, ma tylko spacje, niezaznaczone pole wyboru lub pustą listę. Pole, którego nie ma w dokumencie, też liczy się jako puste. Jeśli status się zgadza, karta jest prawdziwa. W przeciwnym razie jest fałszywa.

**Przykład: brak zamówienia zakupu** · [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pl.mp4#t=43.516)

Na przykład faktura bez zamówienia zakupu trafia do zatwierdzającego faktury bez zamówienia. Faktury z zamówieniem zakupu idą drugą ścieżką, na przykład dopasowaniem do zamówienia.

</details>

## Kiedy używać

Użyj tej karty, aby sprawdzić, czy pole dokumentu jest puste lub nieobecne, na przykład gdy faktura nie ma numeru i wymaga dodatkowej kontroli. To warunek; dalszą akcję konfiguruje się osobno.

**Gdzie:** Standardowy workflow → dodatkowe warunki (AND) → Pole dokumentu.

## Konfiguracja — wersja 2

| Ustawienie | Wartość w przykładzie |
| --- | --- |
| Pole | `invoice_id` — numer faktury |
| Stan pola | Puste lub nieobecne (`field_empty`) |

Wybierz rzeczywiste pole skonfigurowane w swojej organizacji. Opcja `field_not_empty` sprawdza, czy pole zawiera wartość.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

| Przykładowa wartość | Oczekiwany wynik dla `field_empty` |
| --- | --- |
| Puste lub nieobecne pole | Warunek spełniony |
| `DEMO-001` | Warunek niespełniony |
| Numer obecny, lecz niepoprawny | Warunek niespełniony — pole nadal zawiera wartość |

Są to przykłady oczekiwanych wyników. Do sprawdzania poprawności samego numeru dodaj odpowiedni warunek oceniający treść; ta karta sprawdza stan pola. W wersji 2 spacje są usuwane z początku i końca tekstu przed oceną pustego pola.

## Film z przykładem administratora

Kiedy używam karty, gdzie ją znaleźć i jak wykrywać brakujące numery faktur. Przykłady pokazują oczekiwane wyniki.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pl.mp4" %}

[Otwórz film z polskimi napisami](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pl-theme-v4.html)

[Przeczytaj transkrypcję](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pl.txt)
