# Walidacja dla każdego typu dokumentu

> W niektórych wersjach przełącznik blokowania ma błędną etykietę «Bloking».

Administratorzy decydują dla każdego typu dokumentu, czy DocBits waliduje przychodzące e-faktury i czy nieudana kontrola blokuje dokument. Każda zmiana jest potwierdzana i zapisywana w [dzienniku zmian](validation-change-log.md).

> Te ustawienia mogą zmieniać tylko **administratorzy organizacji**. Inni użytkownicy widzą tabelę tylko do odczytu albo wcale.

## Tabela

Przejdź do **Settings → E-Documents → E-Invoice Validation**. Karta **Rules and policy** zaczyna się od tabeli **Validation for each document type**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-pl-20261104.png" alt="Walidacja i blokowanie według typu dokumentu. Skonfigurowane nazwy są ukryte. Przykład z Dev. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs."><figcaption><p>Walidacja i blokowanie według typu dokumentu. Skonfigurowane nazwy są ukryte. Przykład z Dev. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.</p></figcaption></figure>

| Przełącznik | Co robi |
| --- | --- |
| **Enabled** | DocBits waliduje każdą przychodzącą e-fakturę tego typu dokumentu i zapisuje [raport walidacyjny](validation-report.md). |
| **Blocking** | Wynik będący błędem zatrzymuje dokument. Dokument dostaje status **Error**. Gdy blokowanie jest wyłączone, DocBits zapisuje raport, a dokument przechodzi dalej. **Blocking** możesz włączyć tylko wtedy, gdy włączony jest **Enabled**. |

Jeśli typ dokumentu ma nadpisania dla podtypów, tabela pokazuje o tym informację.

## Zmiana ustawienia

1. Wybierz przełącznik, który chcesz zmienić.
2. DocBits pokazuje okno **Confirm validation change** z typem dokumentu i zmianą, na przykład *QUOTE: Włączony → Włączone*.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm-pl.png" alt="Potwierdzenie zmiany ustawienia. Zmiana została anulowana na potrzeby tego zrzutu."><figcaption><p>Potwierdzenie zmiany ustawienia. Zmiana została anulowana na potrzeby tego zrzutu.</p></figcaption></figure>

3. Przeczytaj informację: **Zapisane już raporty nie ulegają zmianie.** Zmiana dotyczy tylko nowych sprawdzeń, również w przypadku ponownego uruchomienia przetwarzania dokumentu.
4. Wybierz **Confirm change** albo **Cancel**, aby zachować dotychczasowe ustawienie.

Jeśli nie masz uprawnień, DocBits pokazuje komunikat, że wymagany jest administrator organizacji, i nic się nie zmienia.

## Powiązane strony

* [Walidacja e-faktury](./)
* [Dziennik zmian](validation-change-log.md)
* [Konfiguracja walidacji i akceptowane wersje](validation-setup.md)
* [Raport walidacyjny](validation-report.md)
* [Włączanie lub wyłączanie walidacji e-faktur](../#wlaczanie-lub-wylaczanie-walidacji-e-faktur)
