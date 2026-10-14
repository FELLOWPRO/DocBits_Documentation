# Rozwiązywanie problemów z ekstrakcją tabeli

## **Krok 1: Otwórz widok OCR dla złych wyników ekstrakcji**

Jeśli wyniki szkolenia ekstrakcji tabeli nie są dobre:

1. Otwórz **widok OCR**, klikając na ikonę lupy z napisem **OCR**.
2. Przejrzyj wyniki ekstrakcji i sprawdź, czy proces OCR może poprawić przechwytywanie danych.
3. Jeśli wyniki nadal są złe, spróbuj innego dokumentu, aby sprawdzić, czy problem jest związany z dokumentem.
4. Jeśli problem jest związany z dokumentem, użyj innego dokumentu do ekstrakcji.
   * Jeśli problem nadal występuje, przejdź do kolejnych kroków.

## **Krok 2: Sprawdź dostępność e-tekstu**

1. Sprawdź, czy dokument zawiera dostępny **e-tekst**.
   * Możesz to zweryfikować za pomocą narzędzia takiego jak **Adobe Acrobat**.
   * Jeśli dokument zawiera e-tekst, przejdź do **Kroku 3.**
   * Jeśli dokument nie zawiera e-tekstu, przejdź do **Kroku 4.**

## **Krok 3: Włącz ekstrakcję e-tekstu**

Jeśli dokument zawiera e-tekst, masz dwie opcje:

1. **Włącz ekstrakcję e-tekstu tylko dla tego dostawcy**:
   * Wróć do **Walidacji Pola Dokumentów**.
   * Kliknij kwadrat z trzema kropkami w lewym pasku narzędzi.
   * Tutaj aktywuj opcję **Użyj e-tekstu, jeśli jest dostępny**, aby włączyć ją tylko dla tego dostawcy.
2. **Włącz ekstrakcję e-tekstu dla wszystkich dostawców**:
   * Przejdź do **Ustawienia** > **Przetwarzanie Dokumentów** > **Ustawienia OCR**.
   * W tej sekcji znajdziesz opcję **Użyj e-tekstu, jeśli jest dostępny** i możesz włączyć ją dla wszystkich dostawców.
3. Po włączeniu ekstrakcji e-tekstu, ponów szkolenie ekstrakcji tabeli.
   * Jeśli wyniki się poprawią, problem zostanie rozwiązany.
   * Jeśli wyniki nadal są złe, przejdź do **Kroku 4**.

## **Krok 4: Brak dostępnego e-tekstu - Zmień wersję AI OCR**

Jeśli dokument nie zawiera dostępnego e-tekstu:

1. Przejdź do **Ustawienia** > **Przetwarzanie Dokumentów** > **Ustawienia OCR**.
2. Zmień **Wersję AI OCR** na inną wersję.
3. Wróć do **Szkolenia Ekstrakcji Tabeli** i spróbuj ponownie.
4. Jeśli wynik jest lepszy:
   * Sprawdź inne dokumenty od różnych dostawców, aby upewnić się, że wyniki ekstrakcji dla tych dostawców nie są dotknięte tą zmianą.
   * **Bądź ostrożny, ponieważ ta zmiana może wpłynąć na wyniki ekstrakcji innych dostawców.**
   * Ta zmiana może wpłynąć na innych dostawców, dlatego upewnij się, że dokładnie zweryfikujesz wyniki, aby nie miały negatywnego wpływu na ekstrakcje dokumentów innych dostawców.
5. Jeśli wynik nie poprawił się po zmianie wersji AI OCR, prosimy o **kontakt z nami** w celu uzyskania dalszej pomocy.

## Komunikaty na tabeli <a href="#messages-on-the-table" id="messages-on-the-table"></a>

Ekstrakcja może wyglądać poprawnie, a dokument mimo to nie daje się zatwierdzić. Poniżej znajdziesz komunikaty, które DocBits wyświetla na tabeli pozycji lub pod nią, co je wywołuje i jak je usunąć.

| Komunikat | Przyczyna | Rozwiązanie |
|---|---|---|
| **Pusta wymagana kolumna** (komórka oznaczona na czerwono, nazwa kolumny w podpowiedzi) | Kolumna oznaczona *Is Required* w ustawieniach kolumn tabeli nie ma wartości w tym wierszu. | Wypełnij komórkę. Jeśli wartość nigdy nie występuje dla tego typu dokumentu, administrator odznacza *Is Required* w Ustawienia → Typy dokumentów → Kolumny tabeli, a Ty uruchamiasz dokument ponownie. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits sprawdza każdy wiersz: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, minus `DISCOUNT`, albo × (100 − `DISCOUNT_PERCENT`) / 100, albo minus `DISCOUNT_PER_UNIT × QUANTITY`, w zależności od tego, która kolumna rabatu jest wypełniona. Różnica powyżej 0,02 wywołuje komunikat. Kontrola działa tylko wtedy, gdy ilość, cena jednostkowa i suma są wypełnione. | Porównaj cztery wartości z dokumentem. Zwykle jedna z nich została odczytana do niewłaściwej kolumny; najczęstszy przypadek to wartość opłat lub rabatu w niewłaściwej komórce. Popraw komórkę; komunikat znika po zapisaniu. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Ta sama kontrola, z wypełnioną kolumną rabatu. | Jak wyżej; najpierw sprawdź komórkę rabatu. |
| **Line items add up to … but the net total is …** (ostrzeżenie) | Suma wszystkich komórek `TOTAL_AMOUNT` różni się od kwoty netto w nagłówku. | Poszukaj brakującego wiersza, zdublowanego wiersza albo źle odczytanej kwoty netto w nagłówku. Ostrzeżenie nie blokuje zatwierdzenia. |
| **Total does not add up: expected …, got …** (nagłówek) | Netto + podatek (+ wysyłka w układach US) różni się od kwoty całkowitej w nagłówku. | Kontrola nagłówka, nie problem tabeli: popraw kwoty w nagłówku. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | Dopasowanie PO wymaga tych czterech kolumn domyślnych, a jedna z nich jest ukryta lub zastąpiona kolumną własną. | Administrator: odkryj kolumnę domyślną w Kolumnach tabeli albo zmapuj wartość na nią w szkoleniu tabeli. |
| **Table is already extracted by AI. Do you want to train manually?** | Otworzono szkolenie tabeli dla dostawcy, którego tabela pochodzi z AI. | Potwierdź, aby trenować; zapisane reguły zastąpią wtedy tabelę AI dla tego dostawcy. Anuluj, aby zachować tabelę AI. |
| **AI Table will display here. Enable in …** | Ekstrakcja tabeli AI jest wyłączona dla organizacji. | Administrator: Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja → *AI Table extraction*. |
| **No line items yet** | Nic nie zostało wyodrębnione: brak reguł dla tego dostawcy i AI nie znalazło tabeli, albo dokument nie ma czytelnego tekstu. | Wykonaj Kroki 1–4 powyżej (widok OCR, E-Text). Następnie wytrenuj tabelę raz albo dodaj wiersze ręcznie za pomocą *Add new table row*. |

### AI wciąż wypełnia kolumnę niewłaściwą wartością

Przykład z praktyki: AI wpisuje sumę pozycji do kolumny `CHARGES`. Każdy wiersz nie przechodzi wtedy kontroli sumy pozycji, ponieważ opłaty są dodawane do iloczynu ilość × cena jednostkowa.

1. Jeśli dostawca ma zapisane reguły, odznacz *Use AI* dla tej kolumny (Ustawienia → Typy dokumentów → Kolumny tabeli), aby wypełniały ją reguły.
2. Jeśli dostawca nie ma reguł, wytrenuj tabelę raz, aby kolumna została powiązana ze swoją pozycją na stronie, albo ukryj kolumnę, jeśli dostawca nigdy nie drukuje tej wartości.
3. Dodaj [tag tabeli AI](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md), na przykład *"kolumna opłat jest pusta u tego dostawcy"*; tagi są zapisywane dla każdego dostawcy osobno.

### Wyłączanie kontroli tabeli

Ustawienia → Typy dokumentów → *Twój typ* → Więcej ustawień → **Pomiń walidację tabeli** oznacza tabelę każdego dokumentu tego typu jako poprawną: niezgodności sum pozycji i puste wymagane kolumny nie są już zgłaszane. Kontrole nagłówka (suma = netto + podatek) pozostają. Używaj tej opcji tylko dla typów dokumentów, których tabele mają charakter informacyjny i nie są eksportowane do systemu ERP.
