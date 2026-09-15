# Pozycje w eksporcie

To, co dzieje się z tabelą pozycji, gdy dokument zostaje zatwierdzony i wyeksportowany, zależy od metody eksportu. Ta strona wyjaśnia, które kolumny opuszczają DocBits, które są obowiązkowe i dlaczego eksport może zawierać mniej pozycji niż ekran walidacji.

## Dwa rodzaje eksportu

| Metoda eksportu | Co jest wysyłane dla tabeli |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | Tabela w takiej postaci, jak na ekranie walidacji: każda nieukryta [kolumna tabeli](../global-settings/document-types/table-columns.md) każdego wiersza, z wartością, wartością sformatowaną i pewnością. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (BOD-y Infor ERP / SAP) | Nie surowa tabela. DocBits buduje z niej **pozycje przyjęcia** (receipt lines) i **pozycje kosztowe** (cost lines) (patrz poniżej) i mapuje je na pola BOD zgodnie z mapowaniem skonfigurowanym w sekcji [Eksportowanie do Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Pozycje przyjęcia i pozycje kosztowe (eksporty Infor)

Pozycja faktury w ERP jest albo **pozycją przyjęcia**, która rozlicza przyjęcie z zamówienia zakupu, albo **pozycją kosztową**, która księguje kwotę na konto księgi głównej z wymiarami. DocBits decyduje o tym dla każdej pozycji faktury:

* **Pozycje przyjęcia** pochodzą z **dopasowania PO**. Każda pozycja faktury dopasowana do pozycji PO (Pulpit → Dopasowanie PO albo automatycznie z opcją *PO auto match*) staje się pozycją przyjęcia z numerem PO, pozycją PO, pozycją przyjęcia oraz dopasowaną ilością i kwotą. Faktura bez dopasowania PO **nie ma pozycji przyjęcia**; podgląd eksportu pokazuje wtedy `receipt_lines: []`, co jest poprawne, a nie jest błędem.
* **Pozycje kosztowe** pochodzą z **rekordu księgowego**, który tworzy krok księgowania kosztów (lub Auto Accounting): konto księgi głównej, wymiary, kwota, ilość dla każdej pozycji. Faktura bez rekordu księgowego nie ma pozycji kosztowych.
* **Pozycje podatkowe** są budowane z kwot podatku w nagłówku, nie z tabeli.

Dlatego w eksportach Infor tabela pozycji jest *danymi wejściowymi* dla dopasowania PO i księgowania; to, co otrzymuje ERP, jest wynikiem tych dwóch kroków. Pozycja, która nie jest ani dopasowana do PO, ani zaksięgowana, nie trafia do ERP.

{% hint style="warning" %}
Aby dopasowanie PO działało, tabela musi mieć kolumny domyślne **numer pozycji, cena jednostkowa, ilość i kwota całkowita**. Jeśli jedna z nich jest ukryta, ekran walidacji pokazuje komunikat *Line Item Table is missing Mandatory column for PO* i nie można zbudować pozycji przyjęcia.
{% endhint %}

## Kolumny obowiązkowe i okno zatwierdzania

Zanim dokument będzie można zatwierdzić, DocBits sprawdza tabelę:

1. Każda kolumna oznaczona **Wymagana** (*Is Required*, Ustawienia → Typy dokumentów → Kolumny tabeli) musi mieć wartość w każdym wierszu.
2. Każdy wiersz musi przejść **kontrolę sumy pozycji**: `suma = ilość × cena jednostkowa + opłaty − rabat` z tolerancją 0,02. Wiersze, które jej nie przechodzą, są oznaczane; komunikat podaje wartość oczekiwaną i rzeczywistą.
3. **Suma sum pozycji** jest porównywana z kwotą netto w nagłówku. Różnica jest ostrzeżeniem i nie blokuje zatwierdzenia.

Okno zatwierdzania wymienia, czego jeszcze brakuje. Administrator może wyłączyć wszystkie kontrole tabeli dla typu dokumentu opcją **Pomiń walidację tabeli** (Typy dokumentów → Więcej ustawień); sumy pozycji i wymagane kolumny nie są wtedy sprawdzane, kontrole nagłówka pozostają.

Szczegóły komunikatów: [Rozwiązywanie problemów z ekstrakcją tabeli](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#messages-on-the-table).

## Pusta tabela

* **Eksporty JSON / XML** wysyłają dokument z `tables: []` (albo tabelę z zerową liczbą wierszy). System odbierający musi obsłużyć pustą tabelę.
* **Eksporty Infor** bez pozycji przyjęcia i bez pozycji kosztowych wysyłają tylko nagłówek i pozycje podatkowe. Większość systemów ERP odrzuca fakturę bez pozycji; skonfiguruj Auto Accounting lub domyślną pozycję kosztową dla takich typów dokumentów albo kieruj je do innego eksportu.
* Typ dokumentu **bez tabeli** (brak skonfigurowanej tabeli) nigdy nie wysyła danych pozycji; jest to oczekiwane dla typów dokumentów, takich jak potwierdzenia zamówień, które są dopasowywane na poziomie nagłówka.

## Sprawdzenie przed zatwierdzeniem

Partnerzy i wsparcie z dostępem do API lub MCP mogą pobrać ładunek eksportu dokumentu przed jego wysłaniem: narzędzie MCP `get_export_preview(doc_id)` zwraca dokładnie to, co wyśle eksport, czyli `receipt_lines`, `cost_lines` i `tax_lines` dla eksportów Infor oraz `tables` dla eksportów JSON. Użyj go, gdy ERP zgłasza brakujące pozycje: jeśli `receipt_lines` jest puste, faktura nie została dopasowana do PO; jeśli `cost_lines` jest puste, nie istnieje rekord księgowy.

## Powiązane strony

* [Eksport](export.md): konfiguracje i metody eksportu
* [Kolumny tabeli](../global-settings/document-types/table-columns.md)
* [Eksportowanie do Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md): mapowania pól BOD dla pozycji przyjęcia, kosztowych i podatkowych
