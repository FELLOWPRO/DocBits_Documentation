# Rozwiązywanie problemów

## Nowa kolumna nie pojawia się na ekranie walidacji

* Dokument został przetworzony przed dodaniem kolumny. Zmiany obowiązują dla dokumentów przesłanych lub uruchomionych ponownie później, więc **uruchom dokument ponownie** (Dashboard → menu dokumentu → Restart).
* Kolumna jest **Hidden**. Sprawdź flagę na liście Table Columns.
* Kolumna została dodana do **innej tabeli** niż wyświetlana. Ekran walidacji pokazuje tabele typu dokumentu; porównaj kolumnę *Table name*.
* Dokument nie jest typu, który skonfigurowano.

## Kolumna jest, ale zawsze pusta

* Dostawca ma **wytrenowane reguły**, a nowa kolumna nie jest w nich zmapowana. Otwórz jeden z dokumentów dostawcy w trenowaniu tabeli i zmapuj kolumnę albo ustaw *Use AI* dla tej kolumny.
* W przypadku ekstrakcji przez AI wartość nie jest rozpoznawalna w dokumencie (brak nagłówka, skrót, inny język). Dodaj [tag tabeli AI](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md), który nazywa kolumnę, albo zmapuj ją podczas trenowania.

## „Column name already exists"

Kolumna o tej samej nazwie technicznej już istnieje w tabeli. Jeśli nie ma jej na liście, jest to ukryta kolumna domyślna: komunikat brzmi *Please activate it in Table Column settings*. Odznacz *Hidden* dla tej kolumny zamiast tworzyć nową.

## Zatwierdzenie jest blokowane przez wymaganą kolumnę

Komunikat przy tabeli wskazuje kolumnę. Wypełnij komórkę w każdym wierszu albo (jeśli wartość nie występuje w tym dokumencie) odznacz *Is Required* dla kolumny, uruchom dokument ponownie i spróbuj jeszcze raz. Zastanów się, czy kolumna w ogóle powinna być wymagana (zobacz [Najlepsze praktyki](best-practices-2.md)).

## AI wypełnia kolumnę błędną wartością

Typowy przypadek: `CHARGES` otrzymuje wartość pozycji, a każdy wiersz kończy się wtedy niepowodzeniem kontroli wartości pozycji z komunikatem *Line total does not match quantity x unit price (expected …, got …)*, ponieważ opłaty są częścią wzoru `ilość × cena jednostkowa + opłaty`.

* Odznacz *Use AI* dla kolumny, jeśli wytrenowane reguły rozpoznają ją poprawnie.
* Jeśli dostawca nie ma reguł, wytrenuj tabelę raz (Table training), aby kolumna została powiązana z właściwą pozycją, albo ukryj kolumnę, jeśli dostawca nigdy nie drukuje tej wartości.
* W ostateczności *Skip table validation* w More Settings typu dokumentu wyłącza wszystkie kontrole tabel dla całego typu dokumentu; niezgodność nie jest wtedy wykrywana, podobnie jak puste wymagane kolumny.

## Dopasowanie PO: „Brak tabeli pozycji zamówienia Kolumna obowiązkowa”

PO matching wymaga kolumn domyślnych: numer artykułu, cena jednostkowa, ilość i kwota całkowita. Jedna z nich jest ukryta lub została zastąpiona kolumną własną. Odkryj kolumnę domyślną albo zmapuj wartość na nią podczas trenowania tabeli.

## Skrypt lub eksport kończy się błędem po usunięciu kolumny

Skrypt lub mapowanie eksportu nadal odwołuje się do usuniętej *Column name*. Usuń odwołanie albo dodaj kolumnę ponownie z tym samym tytułem; nazwa techniczna jest tworzona na podstawie tytułu i znów pasuje.

## Gdzie szukać dalej

* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): jakość ekstrakcji, OCR, E-Text
* [Pola linii treningowych / Trening na stole](../../../../setup/document-training/training-line-fields-table-training/README.md)
