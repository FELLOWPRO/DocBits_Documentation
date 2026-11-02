# Cel i zastosowanie

Kolumna tabeli to jedno pole tabeli pozycji. Wszystko, co DocBits robi z tabelą (ekstrakcja, walidacja, PO matching, eksport), opiera się na kolumnach skonfigurowanych tutaj.

## Gdzie występuje kolumna

| Miejsce | Do czego służy tam kolumna |
|---|---|
| **Validation screen** | Jedna kolumna w tabeli pozycji. *Title* jest nagłówkiem, a *Column Type* określa edytor (kwota, data, tekst, tak/nie). Ukryte kolumny nie są wyświetlane. |
| **Table training** | Podczas trenowania tabeli dostawcy każdą wykrytą kolumnę tabeli mapujesz na jedną ze skonfigurowanych kolumn. Mapować można tylko skonfigurowane kolumny. |
| **AI table extraction** | AI wypełnia skonfigurowane kolumny. Kolumna oznaczona *Use AI* jest wypełniana przez AI nawet dla dostawców z wytrenowanymi regułami. |
| **Validation rules** | Kontrole pozycji, takie jak *ilość × cena jednostkowa = wartość pozycji*, działają na kolumnach domyślnych `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Wymaga kolumn domyślnych: numer artykułu, cena jednostkowa, ilość i kwota całkowita. Bez nich dokument pokazuje komunikat *Line Item Table is missing Mandatory column for PO*. |
| **Export** | Każda nieukryta kolumna jest częścią danych pozycji wysyłanych do ERP. Mapowanie eksportu odwołuje się do *Column name*. |
| **Scripts** | Skrypty odczytują i zapisują kolumny według *Column name*, na przykład `row["TOTAL_AMOUNT"]`. |

## Zakres

* Kolumny tabeli są konfigurowane **dla każdej tabeli**, a tabela należy do **typu dokumentu**. Kolumny faktury nie wpływają na dowody dostawy.
* Konfiguracja jest **dla każdej organizacji**. Podorganizacje ją dziedziczą.
* To, które kolumny są *wypełniane* dla danego dostawcy, zależy od trenowania tego dostawcy lub od AI; konfiguracja kolumn określa tylko, które kolumny istnieją.

## Typowe powody zmiany konfiguracji

* Wartość specyficzna dla klienta musi być rejestrowana w każdej pozycji (centrum kosztów, numer projektu, wewnętrzny numer artykułu) → dodaj kolumnę.
* Kolumna domyślna nigdy nie jest używana i zaśmieca ekran walidacji → ukryj ją.
* Kolumna musi być zawsze wypełniona przed eksportem → oznacz ją jako *Required*.
* Wartość pochodzi z wyszukiwania w ERP i użytkownicy nie mogą jej edytować → oznacz ją jako *Read Only*.
* AI rozpoznaje kolumnę lepiej niż wytrenowane reguły (na przykład opisy w dowolnym tekście) → oznacz ją jako *Use AI*.

## Powiązane strony

* [Dodawanie nowej kolumny](adding-a-new-column.md)
* [Edytowanie i usuwanie kolumn](editing-and-deleting-columns.md)
* [Rozwiązywanie problemów z wyodrębnianiem tabeli](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
