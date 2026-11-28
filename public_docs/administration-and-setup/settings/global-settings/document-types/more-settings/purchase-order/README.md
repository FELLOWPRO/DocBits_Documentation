# Zamówienie zakupu

Karta **Purchase Order** w **More Settings** typu dokumentu określa, jak dokumenty tego typu są dopasowywane do zamówień zakupu. Ustawienia dotyczą jednego typu dokumentu naraz, więc najpierw otwórz typ dokumentu, który chcesz zmienić, w **Settings → Document Types**.

Aby znaleźć ustawienia faktury:

1. Otwórz **Settings → Document Types**.
2. Znajdź kartę **Invoice** i wybierz jej ikonę koła zębatego (**More Settings**).
3. Otwórz sekcję **Purchase Order**, aby przejrzeć opcje dopasowywania i walidacji.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>Karta Invoice w bieżącym angielskim środowisku testowym Dev. Ikona koła zębatego otwiera More Settings; pozostałe elementy sterujące dotyczą typu dokumentu.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>Sekcja Purchase Order w More Settings, pokazana w stanie zwiniętym. Rozwiń jej nagłówek, aby zobaczyć opcje; do tego zrzutu nie zmieniono żadnego ustawienia.</p></figcaption></figure>

Zacznij od reguł dopasowania i tolerancji, a następnie dostosuj zachowanie dopasowania i eksportu:

* [Zasady Dopasowywania Zamówień Zakupu](purchase-order-matching-rules.md) i [Ustawienia tolerancji zamówienia zakupu / Dodatkowa tolerancja zamówienia zakupu](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) określają, jak porównywane są linie faktury i zamówienia.
* [Opcje automatycznego dopasowania i eksportu](auto-match-and-export-options.md), [Eksport niepasujących linii PO](export-not-matched-po-lines.md) i [Alternatywny eksport](alternate-export.md) opisują, co dzieje się po dopasowaniu.
* [Eksportowana ilość w podstawowej jednostce miary](export-quantity-in-base-unit-of-measure.md) przelicza eksportowaną ilość i cenę jednostkową na podstawową jednostkę miary, na potrzeby eksportu do Infor LN.
* [Tabela PO w Kreatorze Układów](po-table-in-layout-builder.md), [Status linii zamówienia PO](consumed-po-line-status.md) i [Oblicz cenę jednostkową zamówienia](calculate-po-unit-price.md) zmieniają to, co użytkownicy widzą w widoku dopasowania.
* [Automatyczne sprawdzanie aktualizacji PO](auto-check-for-po-updates.md), [Statusy wyłączenia zamówienia zakupu](purchase-order-disable-statuses.md) i [Aktualizuj status zamówienia zakupu](update-document-purchase-order-status.md) kontrolują, jak dane i statusy zamówienia zakupu pozostają aktualne.
* [Mapa Numerów Przedmiotów Dostawcy - Dokumentacja Administracyjna](supplier-item-number-map-admin-documentation.md) oraz ogólna strona [Zamówienie zakupu](purchase-order.md) dostarczają dalszego kontekstu.

Ustawienia mogą wpływać na dokumenty produkcyjne. Sprawdź zmiany na dokumencie testowym, zanim zapiszesz je w środowisku produkcyjnym.

Ten przegląd pokazuje, gdzie znaleźć ustawienia. Nie weryfikuje zakończonego dopasowania PO ani eksportu.
