# Status zużytej linii zamówienia PO

**Status zużytej linii zamówienia PO** koloruje linie zamówienia zakupu na ekranie dopasowywania według tego, jak duża część każdej linii została już dopasowana. Włącz to ustawienie dla typu dokumentu używanego dla faktur, jeśli zespół musi szybko rozpoznać linie PO jeszcze niedopasowane, częściowo dopasowane i w pełni dopasowane. Kolor to tylko pomoc wizualna; przed decyzją, czy linię można dopasować ponownie, sprawdź **Dopasowaną ilość** i wybraną kolumnę ilości zamówienia zakupu.

## Włączanie ustawienia

1. Otwórz **Ustawienia → Typy dokumentów**. Znajdź typ dokumentu używany dla faktur i wybierz zębatkę na jego karcie, aby otworzyć **Więcej ustawień**. Zrzut pokazuje kartę **Faktura**. Przełączników **Aktywować** i **Extraction** nie zmieniaj.

   <figure><img src="../../../../../../.gitbook/assets/1-consumed-po-line-document-types-pl.png" alt="Strona Typy dokumentów z kartą Faktura i zębatką Więcej ustawień"><figcaption><p>Otwórz Więcej ustawień z karty Faktura.</p></figcaption></figure>

2. Rozwiń sekcję **Zamówienie zakupu**, jeśli jest zwinięta. Znajdź pozycję **Status zużytej linii zamówienia** i włącz jej przełącznik. To ustawienie jest oddzielne od **Aktualizacja dokumentu Status zamówienia zakupu** dalej w tej samej sekcji.

   <figure><img src="../../../../../../.gitbook/assets/2-consumed-po-line-settings-pl.png" alt="Sekcja Zamówienie zakupu w Więcej ustawień z widocznym przełącznikiem Status zużytej linii zamówienia"><figcaption><p>Wybierz przełącznik Status zużytej linii zamówienia.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/3-consumed-po-line-toggle-pl.png" alt="Zbliżenie etykiety Status zużytej linii zamówienia i przełącznika"><figcaption><p>Na tym przykładzie przełącznik jest wyłączony; włącz go, aby zobaczyć kolory dopasowania.</p></figcaption></figure>

3. Otwórz fakturę z dopasowywaniem zamówień zakupu i przejrzyj jej linie PO. Poniższe przykłady pokazują, jak kolory linii odnoszą się do stanu dopasowania. Kroki dopasowania opisuje [Ekran dopasowywania zamówień zakupu](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Co oznaczają kolory linii PO

| Wygląd | Znaczenie | Co sprawdzić |
| --- | --- | --- |
| Zwykły lub biały | Żadna ilość w tej linii PO nie została jeszcze dopasowana. | Przed dopasowaniem sprawdź ilość zamówienia zakupu i linię faktury. |
| Niebieski odcień | Linia została wybrana w bieżącym widoku dopasowania. | Wybór jest tymczasowy; nie oznacza, że linia jest w pełni dopasowana. |
| Blady pomarańczowy | Część ilości została dopasowana, ale dopasowana ilość jest mniejsza niż wybrana ilość zamówienia zakupu. | Sprawdź, ile ilości jeszcze pozostaje. |
| Blady fioletowy | Dopasowana ilość jest co najmniej równa wybranej ilości zamówienia zakupu. | Nie zakładaj, że dostępna jest dodatkowa ilość. |

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FjwYiBzpTPFv8tQaTTaeJ%252Fimage.png%3Falt%3Dmedia%26token%3D20a99b45-2d61-4bd5-84b7-b0c24b04e223&width=768&dpr=4&quality=100&sign=ebdb365&sv=2" alt="Linia PO z zerową dopasowaną ilością i bez koloru statusu"><figcaption><p>Żadna ilość nie została jeszcze dopasowana.</p></figcaption></figure>

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FwJK44aAJJPzJm4f4miFg%252Fimage.png%3Falt%3Dmedia%26token%3D3a51bd26-5b87-4b61-a056-ae40bccc4e55&width=768&dpr=4&quality=100&sign=d445fa07&sv=2" alt="Linia PO z niebieskim tłem wyboru na ekranie dopasowywania"><figcaption><p>Linia jest wybrana do bieżącego dopasowania.</p></figcaption></figure>

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNoof3pErQqAvAWZpo4Fd%252Fimage.png%3Falt%3Dmedia%26token%3D21a15672-8e84-4e22-a0f2-8b65bcbfda54&width=768&dpr=4&quality=100&sign=4a68abca&sv=2" alt="Linia PO z bladym pomarańczowym tłem i dopasowaną ilością mniejszą niż ilość zamówienia zakupu"><figcaption><p>Linia jest częściowo użyta.</p></figcaption></figure>

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F722yxDRHmvz6CLfIamq8%252Fimage.png%3Falt%3Dmedia%26token%3D15aecf8c-aa63-4de4-b77f-1147c8ed593a&width=768&dpr=4&quality=100&sign=c1b2c2ab&sv=2" alt="Linia PO z bladym fioletowym tłem i dopasowaną ilością równą ilości zamówienia zakupu"><figcaption><p>Linia jest w pełni użyta.</p></figcaption></figure>

Przekreślona linia ma inne znaczenie: jej status zamówienia zakupu może być wyłączony przez ustawienie [Statusy wyłączenia zamówienia zakupu](purchase-order-disable-statuses.md). Sprawdź to ustawienie, jeśli linii nie można wybrać.
