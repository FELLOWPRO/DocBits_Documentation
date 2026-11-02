# Hotfixy 8 września 2026

> Dopasowywanie zamówień zakupowych: co się zmieniło wraz z hotfixami wdrożonymi 8 września 2026. Poniższe zachowanie jest aktywne w środowisku deweloperskim i trafi do stage, sandbox oraz produkcji przy kolejnych aktualizacjach.

## Dopasowywanie zamówień zakupowych

- **Dopasowanie przetrwa zapis.** Dopasowanie zamówienia zakupowego, które reguła transformacji wcześniej usuwała bez słowa przy każdym zapisie (reguły przebudowujące pozycje), jest teraz zachowywane tak długo, jak reguła generuje te same linie. Gdy reguła faktycznie zastępuje dopasowane linie, dokument zapisuje regułę, a ekran ją wyświetla.
- **Dopasowywanie uruchamia się ponownie przy zapisie.** Gdy numer zamówienia na dokumencie się zmienia — lub gdy dane podstawowe uzupełniły go po przetworzeniu i jeszcze nie wykonano dopasowania — zapis natychmiast dopasowuje dokument. Istniejące dopasowanie nigdy nie jest nadpisywane przez zapis.
- **Ekran informuje, dlaczego nie ma dopasowania.** Ekran Dopasowywania Zamówień Zakupowych pokazuje jedno zdanie nad obszarem zamówienia: brak numeru zamówienia, zamówienie nie znalezione w ERP, jeszcze nie wyszukano, załadowano, ale nie połączono, brak dopasowanych linii, brak tabeli, kolumny tabeli nie zmapowane, brak otwartych linii. Kandydaci odrzuceni są wymienieni wraz z powodem (np. numer faktury wczytany do kolumny zamówienia).
- **Odrzucone dopasowanie nigdy nie jest raportowane jako zapisane.** Jeśli serwer nie zachowa dopasowania, ekran je przywraca, oznacza dokument jako niezapisany i zgłasza odrzucenie wraz z powodem zamiast „zapisano”.
- **Historia dopasowań pokazuje reguły transformacji.** Historia dopasowań dokumentu zawiera teraz krok _Reguły transformacji_ przed pierwszym etapem dopasowania, wymieniając reguły, które zostały uruchomione oraz czy któraś z nich odrzuciła dopasowanie. Administratorzy mają link do reguły.
- **Cena jednostkowa PO z kwoty netto.** Przy włączonej opcji _Oblicz cenę jednostkową PO_ cena jest teraz najpierw wyprowadzana z **netto** pozycji zamówienia, a z sumy tylko gdy brak kwoty netto. Zamówienia z Infor zawierają podatek w sumie pozycji; faktury wyceniane netto wcześniej pokazywały „cena jednostkowa niedopasowana” dokładnie o stawkę podatku. Obliczona cena jest odświeżana przy każdym dopasowaniu, więc istniejące dokumenty korzystają bez ponownego ładowania zamówienia.
- **Numery faktur nie są już mylone z numerami zamówień.** Kandydat z kolumny pozycji lub wcześniejszego wyszukiwania, który jest równy własnemu numerowi faktury dokumentu, jest odrzucany.

## Dokumentacja

- Nowa strona [Reguły transformacji](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Reguły dopasowywania zamówień zakupowych](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) obejmują teraz typy reguł, warunki aktywacji, reguły zapasowe, domyślny zestaw reguł, typy tolerancji oraz efektywne kolumny.
- [Obliczanie ceny jednostkowej PO](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) opisuje obliczanie kwoty netto.
- [Ekran dopasowywania zamówień zakupowych](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) wyjaśnia komunikaty „dlaczego nie ma dopasowania” oraz historię dopasowań.