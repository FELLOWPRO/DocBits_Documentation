# Eksportowana ilość w podstawowej jednostce miary

Przełącznik **Export quantity in base unit of measure** znajduje się w sekcji **Purchase Order** w **More Settings** typu dokumentu. Zmienia ilość i cenę jednostkową, które eksport do Infor LN zapisuje dla dopasowanych linii zamówienia.

Otwórz go w **Settings → Document Types**, wybierz ikonę koła zębatego (**More Settings**) na karcie typu dokumentu i rozwiń **Purchase Order**.

## Co robi przełącznik

* **Off:** DocBits eksportuje ilość i cenę jednostkową w jednostce faktury.
* **On:** DocBits przelicza ilość i cenę jednostkową każdej dopasowanej linii zamówienia na podstawową jednostkę miary tej linii za pomocą jej współczynnika przeliczeniowego i zapisuje kod jednostki podstawowej zamiast kodu jednostki zafakturowanej.

Linia bez współczynnika przeliczeniowego jest eksportowana bez zmian, więc brakujący współczynnik nie blokuje eksportu.

{% hint style="info" %}
Przeliczenie dotyczy wyłącznie eksportu do Infor LN. Pozostałe cele eksportu zachowują jednostkę zafakturowaną.
{% endhint %}

## Kiedy go używać

Włącz przełącznik, gdy instancja Infor LN oczekuje ilości zamówienia w podstawowej jednostce miary. Przeliczenie używa współczynnika zapisanego w linii zamówienia, a nie współczynnika, który DocBits oblicza z kartoteki towarów.

Ustawienia mogą wpływać na dokumenty w użyciu. Sprawdź wynik na dokumencie testowym, zanim zapiszesz zmianę w środowisku produkcyjnym. Przełącznik zmienia eksportowane wartości; nie zmienia sposobu dopasowywania linii faktury i zamówienia.

## Powiązane strony

* [Zamówienie zakupu](README.md)
* [Eksport niepasujących linii PO](export-not-matched-po-lines.md)
* [Alternatywny eksport](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
