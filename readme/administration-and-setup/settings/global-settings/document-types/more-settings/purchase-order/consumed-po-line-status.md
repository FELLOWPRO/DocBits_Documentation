# Status linii zamówienia PO

**Consumed PO line status** koloruje linie zamówienia zakupu w widoku dopasowania zgodnie z tym, jaka część każdej linii została już dopasowana. Włącz to ustawienie dla typu dokumentu faktury, jeśli Twój zespół chce szybko rozpoznawać niewykorzystane, częściowo wykorzystane i w pełni wykorzystane linie PO. Kolor jest pomocą wizualną; przed podjęciem decyzji, czy linię można dopasować ponownie, sprawdź **Matched Quantity** oraz wybraną kolumnę ilości PO.

## Włączanie ustawienia

1. Otwórz **Settings → Document Types**. Znajdź typ dokumentu używany dla Twoich faktur i wybierz koło zębate na jego karcie, aby otworzyć **More Settings**. Zrzut ekranu pokazuje kartę **Invoice**. Pozostaw przełączniki **Activate** i **Extraction** bez zmian.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-document-types-en.png" alt="Strona Document Types z kartą Invoice i jej kołem zębatym More Settings"><figcaption><p>Otwórz More Settings z karty Invoice.</p></figcaption></figure>

2. Rozwiń **Purchase Order**, jeśli sekcja jest zwinięta. Znajdź **Consumed PO line status** i włącz jego przełącznik. Jest to osobne ustawienie od **Update Document Purchase Order Status**, znajdującego się niżej w tej samej sekcji.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-settings-en.png" alt="Sekcja Purchase Order w More Settings z widocznym przełącznikiem Consumed PO line status"><figcaption><p>Wybierz przełącznik Consumed PO line status.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-toggle-en.png" alt="Zbliżenie na etykietę i przełącznik Consumed PO line status"><figcaption><p>W tym przykładzie przełącznik jest wyłączony; włącz go, aby wyświetlać kolory dopasowania.</p></figcaption></figure>

3. Otwórz fakturę z dopasowaniem zamówienia zakupu i sprawdź jej linie PO. Poniższe przykłady pokazują, jak kolory linii odpowiadają stanowi dopasowania. Kroki dopasowania znajdziesz w [Purchase Order Matching](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Odczytywanie kolorów linii PO

| Wygląd | Znaczenie | Co sprawdzić |
| --- | --- | --- |
| Zwykły lub biały | Żadna ilość z tej linii PO nie została jeszcze dopasowana. | Przed dopasowaniem sprawdź ilość PO i linię faktury. |
| Niebieski odcień | Linia została wybrana w bieżącym widoku dopasowania. | Wybór jest tymczasowy; nie oznacza, że linia jest w pełni dopasowana. |
| Jasnopomarańczowy | Część ilości została dopasowana, ale dopasowana ilość jest mniejsza niż wybrana ilość PO. | Sprawdź, ile ilości pozostało. |
| Jasnofioletowy | Dopasowana ilość jest co najmniej równa wybranej ilości PO. | Nie zakładaj, że dostępna jest dodatkowa ilość. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="Linia PO z zerową dopasowaną ilością i bez koloru statusu"><figcaption><p>Żadna ilość nie została jeszcze dopasowana.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="Linia PO z niebieskim odcieniem zaznaczenia w widoku dopasowania"><figcaption><p>Linia jest wybrana do bieżącego dopasowania.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="Linia PO z jasnopomarańczowym tłem i dopasowaną ilością mniejszą niż ilość PO"><figcaption><p>Linia jest częściowo wykorzystana.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="Linia PO z jasnofioletowym tłem i dopasowaną ilością równą ilości PO"><figcaption><p>Linia jest w pełni wykorzystana.</p></figcaption></figure>

Przekreślona linia ma inne znaczenie: jej status PO może być wykluczony przez [PO disable statuses](purchase-order-disable-statuses.md). Jeśli nie można wybrać linii, sprawdź to ustawienie.
