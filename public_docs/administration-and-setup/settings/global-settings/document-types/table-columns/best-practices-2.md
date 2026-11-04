# Najlepsze praktyki

## Zachowaj kolumny domyślne dla kwot i ilości

Kontrole pozycji (*ilość × cena jednostkowa = wartość pozycji*) oraz dopasowanie zamówień zakupu (PO matching) korzystają z kolumn domyślnych `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Jeśli zamiast nich utworzysz własne kolumny dla tych wartości, kontrole nie zostaną uruchomione, a PO matching zgłosi brakujące kolumny obowiązkowe. Jeśli brzmienie Ci nie odpowiada, zmień *tytuł*, ale zachowaj kolumnę.

## Ukrywaj, nie usuwaj

Niepotrzebne kolumny domyślne są ukrywane, a nie usuwane; i tak nie można ich usunąć. W przypadku własnych kolumn ukrycie jest również bezpieczniejszym wyborem, dopóki nie masz pewności, czy skrypt lub mapowanie eksportu nadal odwołuje się do tej kolumny.

## Oznaczaj jako wymagane tylko to, co blokuje eksport

Każda wymagana kolumna musi być wypełniona w każdym wierszu, zanim użytkownik będzie mógł zatwierdzić dokument. Stosuj to dla wartości, które ERP odrzuca, gdy ich brakuje (na przykład centrum kosztów w eksporcie księgowym), a nie dla wartości, które są jedynie przydatne.

## Używaj *Read Only* dla wartości pobieranych z wyszukiwania

Wartości, które skrypt lub wyszukiwanie w danych podstawowych zapisuje w tabeli (opis artykułu z kartoteki artykułów, kod podatkowy z danych dostawcy), powinny być tylko do odczytu, aby użytkownicy poprawiali źródło, a nie kopię.

## Używaj AI dla kolumny, a nie dla dostawcy

W przypadku dostawcy z wytrenowanymi regułami większość kolumn jest poprawnie wypełniana na podstawie reguł. Jeśli jedna kolumna jest niewiarygodna (długie opisy zawijane w kilku wierszach, rabat, który czasem znajduje się w innym miejscu), ustaw *Use AI* tylko dla tej kolumny. Reguły obsłużą resztę.

## Nazywaj kolumny z myślą o ERP, a nie o dokumencie

*Column name* trafia do mapowań eksportu i skryptów. `COST_CENTRE` łatwiej zmapować niż `KST`, a nazwa nie zmienia się, gdy dostawca drukuje ją inaczej.

## Testuj na ponownie uruchomionym dokumencie

Po zmianie uruchom ponownie jeden istniejący dokument danego typu i otwórz go: nowa kolumna jest widoczna, ukryta zniknęła, a wymagane komórki są oznaczone. Dopiero potem udostępnij zmianę użytkownikom.

## Jedna tabela na strukturę pozycji

Drugą tabelę utwórz tylko wtedy, gdy typ dokumentu naprawdę ma dwie niezależne tabele (na przykład pozycje artykułowe i osobna tabela opłat). Dodatkowe puste tabele pojawiają się w każdym dokumencie tego typu.
