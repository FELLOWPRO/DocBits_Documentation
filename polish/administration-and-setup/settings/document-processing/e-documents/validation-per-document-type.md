# Walidacja dla każdego typu dokumentu

Administratorzy decydują dla każdego typu dokumentu, czy DocBits waliduje przychodzące e-faktury i czy nieudana kontrola blokuje dokument. Każda zmiana jest potwierdzana i zapisywana w [dzienniku zmian](validation-change-log.md).

> Te ustawienia mogą zmieniać tylko **administratorzy organizacji**. Inni użytkownicy widzą tabelę tylko do odczytu albo wcale.

## Tabela

Przejdź do **Ustawienia → Dokumenty elektroniczne → Walidacja e-faktury**. Karta **Zasady i polityka** zaczyna się od tabeli **Walidacja dla każdego typu dokumentu**.

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings-pl.png" alt="Tabela Walidacja dla każdego typu dokumentu z przełącznikami Włączony i Bloking"><figcaption><p>Jeden wiersz dla każdego typu dokumentu z przełącznikami Włączony i Bloking. Przykładowa organizacja.</p></figcaption></figure>

| Przełącznik | Co robi |
| --- | --- |
| **Włączony** | DocBits waliduje każdą przychodzącą e-fakturę tego typu dokumentu i zapisuje [raport walidacyjny](validation-report.md). |
| **Bloking** | Wynik będący błędem zatrzymuje dokument. Dokument dostaje status **Błąd**. Gdy blokowanie jest wyłączone, DocBits zapisuje raport, a dokument przechodzi dalej. **Bloking** możesz włączyć tylko wtedy, gdy włączony jest **Włączony**. |

Jeśli typ dokumentu ma nadpisania dla podtypów, tabela pokazuje o tym informację.

## Zmiana ustawienia

1. Wybierz przełącznik, który chcesz zmienić.
2. DocBits pokazuje okno **Potwierdź zmianę walidacji** z typem dokumentu i zmianą, na przykład *QUOTE: Włączony → NA*.

<figure><img src="../../../../.gitbook/assets/einvoice-validation-confirm-pl.png" alt="Okno Potwierdź zmianę walidacji"><figcaption><p>Każda zmiana wymaga potwierdzenia</p></figcaption></figure>

3. Przeczytaj informację: **Zapisane już raporty nie ulegają zmianie.** Zmiana dotyczy tylko nowych sprawdzeń, również w przypadku ponownego uruchomienia przetwarzania dokumentu.
4. Wybierz **Potwierdź zmianę** albo **Anulować**, aby zachować dotychczasowe ustawienie.

Jeśli nie masz uprawnień, DocBits pokazuje komunikat, że wymagany jest administrator organizacji, i nic się nie zmienia.

## Powiązane strony

* [Walidacja e-faktury](validation-rules.md)
* [Dziennik zmian](validation-change-log.md)
* [Konfiguracja walidacji i akceptowane wersje](validation-setup.md)
* [Raport walidacyjny](validation-report.md)
* [Włączanie lub wyłączanie walidacji e-faktur](README.md#wlaczanie-lub-wylaczanie-walidacji-e-faktur)
