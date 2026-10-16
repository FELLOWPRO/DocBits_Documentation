# Dodawanie nowej kolumny

Dodaj kolumnę, gdy dla każdej pozycji trzeba zapisać wartość, której nie obejmują kolumny domyślne, na przykład centrum kosztów, numer projektu lub wewnętrzny numer artykułu.

## Zanim zaczniesz

* Zdecyduj, do której **tabeli** należy kolumna. Większość typów dokumentów ma jedną tabelę (na przykład `INVOICE_TABLE`). Jeśli lista jest pusta, najpierw kliknij **Create new table**; okno prosi tylko o nazwę tabeli.
* Zdecyduj o **typie**: `AMOUNT` dla kwot pieniężnych, `NUMBER` dla ilości, `DATE`, `BOOLEAN` dla tak/nie, `CURRENCY` dla kodu waluty ISO, `STRING` dla wszystkiego innego. Po zapisaniu nie można zmienić typu.
* Sprawdź, czy **kolumna domyślna** o tym samym znaczeniu już istnieje, ale jest ukryta. Ukryte kolumny są wyświetlane z ustawioną flagą _Hidden_; zamiast tworzyć duplikat, odkryj ją.

## Kroki

1. Otwórz **Settings → Global Settings → Document Types → Table Columns**.
2. Kliknij **Add new table column**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Okno Add new table column z polami Title, Is column required, Select column type i Select Table"><figcaption><p>Add new table column</p></figcaption></figure>

3. Wypełnij okno:

| Pole                    | Co wpisać                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Title**               | Etykieta widoczna dla użytkownika na ekranie walidacji, na przykład `Cost Centre`. Tylko litery i cyfry. DocBits tworzy z niej techniczną _Column name_ (`COST_CENTRE`). |
| **Is column required?** | Zaznacz, gdy dokumentu nie wolno zatwierdzić, dopóki kolumna jest pusta w którymkolwiek wierszu.                                                                         |
| **Select column type**  | Zobacz listę typów powyżej.                                                                                                                                              |
| **Select Table**        | Tabela, która otrzyma kolumnę.                                                                                                                                           |

4. Kliknij **Proceed**. Kolumna pojawi się na liście z niezaznaczonymi flagami _Read Only_, _Hidden_ i _Use AI_. W razie potrzeby przełącz te flagi na liście, zobacz [Edytowanie i usuwanie kolumn](editing-and-deleting-columns.md).

## Po dodaniu

* Kolumna jest **pusta w istniejących dokumentach**. Jest wypełniana w dokumentach przesłanych lub zrestartowanych po zmianie.
* Dla dostawców z **wytrenowanymi regułami** otwórz jeden z ich dokumentów w trenowaniu tabel i zmapuj nową kolumnę, w przeciwnym razie kolumna pozostanie dla tego dostawcy pusta. Zobacz [Defining tables and columns](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Przy **wyodrębnianiu tabel przez AI** AI wypełnia kolumnę, jeśli wartość jest rozpoznawalna w dokumencie. Oznacz kolumnę flagą _Use AI_, jeśli dostawca ma wytrenowane reguły, ale ta kolumna nadal ma pochodzić z AI.
* Dodaj kolumnę do **mapowania eksportu**, jeśli system ERP ma ją otrzymywać, zobacz [Export](../../../document-processing/export/).

## Komunikaty

| Komunikat                                                                  | Znaczenie                                                                             |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| _Column name already exists_                                               | Kolumna o tej nazwie technicznej już istnieje w tabeli. Wybierz inny tytuł.           |
| _Column name already exists – Please activate it in Table Column settings_ | Ukryta kolumna domyślna ma tę nazwę. Zamiast tworzyć nową, wyłącz jej flagę _Hidden_. |
| _No table exists. Please create table before creating columns._            | Typ dokumentu nie ma jeszcze tabeli: najpierw kliknij **Create new table**.           |
