# Status linii zamówienia PO

**Status zużytej linii zamówienia** koloruje linie zamówienia zakupu w widoku dopasowania zgodnie z tym, jaka część każdej linii została już dopasowana. Włącz to ustawienie dla typu dokumentu faktury, jeśli Twój zespół chce szybko rozpoznawać niewykorzystane, częściowo wykorzystane i w pełni wykorzystane linie PO. Kolor jest pomocą wizualną; przed podjęciem decyzji, czy linię można dopasować ponownie, sprawdź **Dopasowana ilość** oraz wybraną kolumnę ilości PO.

## Włączanie ustawienia

1. Otwórz **Ustawienia → Typy dokumentów**. Znajdź typ dokumentu używany dla Twoich faktur i wybierz koło zębate na jego karcie, aby otworzyć **Więcej ustawień**. Zrzut ekranu pokazuje kartę **Faktura**. Pozostaw przełączniki **Aktywować** i **Ekstrakcja** bez zmian.

   <figure><img src="../../../../../../.gitbook/assets/prior-u044-pl.png" alt="Dostęp do dodatkowych ustawień typu dokumentu Faktura."><figcaption><p>Dostęp do dodatkowych ustawień typu dokumentu Faktura.</p></figcaption></figure>

2. Rozwiń **Zamówienie zakupu**, jeśli sekcja jest zwinięta. Znajdź **Status zużytej linii zamówienia** i włącz jego przełącznik. Jest to osobne ustawienie od **Aktualizacja dokumentu Status zamówienia zakupu**, znajdującego się niżej w tej samej sekcji.

   <figure><img src="../../../../../../.gitbook/assets/prior-u045-pl.png" alt="Ustawienia statusów wykorzystanych wierszy zamówienia."><figcaption><p>Ustawienia statusów wykorzystanych wierszy zamówienia.</p></figcaption></figure>

3. Otwórz fakturę z dopasowaniem zamówienia zakupu i sprawdź jej linie PO. Poniższe przykłady pokazują, jak kolory linii odpowiadają stanowi dopasowania. Kroki dopasowania znajdziesz w [Purchase Order Matching](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Odczytywanie kolorów linii PO

| Wygląd | Znaczenie | Co sprawdzić |
| --- | --- | --- |
| Zwykły lub biały | Żadna ilość z tej linii PO nie została jeszcze dopasowana. | Przed dopasowaniem sprawdź ilość PO i linię faktury. |
| Niebieski odcień | Linia została wybrana w bieżącym widoku dopasowania. | Wybór jest tymczasowy; nie oznacza, że linia jest w pełni dopasowana. |
| Jasnopomarańczowy | Część ilości została dopasowana, ale dopasowana ilość jest mniejsza niż wybrana ilość PO. | Sprawdź, ile ilości pozostało. |
| Jasnofioletowy | Dopasowana ilość jest co najmniej równa wybranej ilości PO. | Nie zakładaj, że dostępna jest dodatkowa ilość. |

Przekreślona linia ma inne znaczenie: jej status PO może być wykluczony przez [PO disable statuses](purchase-order-disable-statuses.md). Jeśli nie można wybrać linii, sprawdź to ustawienie.

Poniższa legenda wyjaśnia statusy dopasowania bez obrazów starych wersji. Przed ponownym użyciem wiersza sprawdź wykorzystaną ilość.
