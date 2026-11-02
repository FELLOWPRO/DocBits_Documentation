# Obsługa opłat dodatkowych w Infor M3

## Przegląd

Ten dokument zawiera szczegółowe informacje o tym, jak DocBits integruje się z Infor M3 w celu obsługi opłat dodatkowych powiązanych z fakturami i zamówieniami zakupu (PO). Zawiera scenariusze dotyczące opłat zewnętrznych oraz oczekiwane rozwiązania.

## Scenariusze obsługi opłat dodatkowych

| ID scenariusza | Opis                                                                                  | Przypadek biznesowy                                                                                                                         | Oczekiwane rozwiązanie                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1              | Opłaty zewnętrzne nieujęte w PO, ale widoczne na fakturze (zaakceptowane)             | Opłaty zewnętrzne pojawiają się na fakturze, ale nie są wymienione w PO. Opłaty te są zaakceptowane.                                        | Opłaty zostaną zaksięgowane na regule księgowej PP20-228 na podstawie elementu kosztowego przesłanego przez DocBits.                                                                                                                                     |
| 2              | Opłaty zewnętrzne nieujęte w PO, ale widoczne na fakturze (niezaakceptowane)          | Opłaty zewnętrzne pojawiają się na fakturze, ale nie są wymienione w PO. Opłaty te nie są zaakceptowane ani zatwierdzone.                   | Łączna wartość faktury jest rejestrowana wraz z opłatą nagłówkową za niezatwierdzone opłaty. Dodatkowo dla tych opłat tworzona jest nota obciążeniowa.                                                                                                   |
| 3              | Opłaty zewnętrzne na fakturze wyższe lub niższe niż w PO (w granicach tolerancji)     | Opłaty zewnętrzne na fakturze są wyższe lub niższe niż w PO, ale mieszczą się w akceptowanej tolerancji.                                    | Dodatkowe opłaty są księgowane na regule księgowej PP20-228 na podstawie elementu kosztowego przesłanego przez DocBits.                                                                                                                                  |
| 4              | Opłaty zewnętrzne na fakturze wyższe niż w PO (poza tolerancją, niezatwierdzone)      | Opłaty zewnętrzne na fakturze są wyższe niż w PO, wykraczają poza akceptowaną tolerancję i nie są zatwierdzone.                             | Faktura jest rejestrowana z łączną kwotą faktury. Dodatkowa niezatwierdzona opłata jest dodawana jako opłata nagłówkowa, a dla tej dodatkowej opłaty tworzona jest nota obciążeniowa.                                                                     |
| 5              | Opłaty zewnętrzne na fakturze wyższe niż w PO (poza tolerancją, zatwierdzone w DocBits) | Opłaty zewnętrzne na fakturze są wyższe niż w PO, wykraczają poza akceptowaną tolerancję i są zatwierdzone w DocBits.                       | Dodatkowe opłaty są księgowane na PP20-228. Rozważane są dwie opcje:\<br>- Jeśli tolerancja APS900 > DocBits, dodatkowe opłaty są księgowane automatycznie.\<br>- Jeśli tolerancja APS900 = DocBits, dodatkowe opłaty są księgowane z nowymi elementami opłat nieujętymi w PO. |
| 6              | Opłaty zewnętrzne na fakturze niższe niż w PO (poza tolerancją, niezatwierdzone)      | Opłaty zewnętrzne na fakturze są niższe niż w PO, wykraczają poza akceptowaną tolerancję i nie są zatwierdzone.                             | Faktura jest księgowana jako niezatwierdzona w APS110. Zespół AP koryguje opłaty za pomocą opcji Invoice Control w APS110, która wywołuje APS360.                                                                                                         |
| 7              | Opłaty zewnętrzne w PO i brak opłat na fakturze                                       | Opłaty zewnętrzne są wymienione w PO, ale na fakturze nie ma żadnych opłat.                                                                 | Faktura jest księgowana jako niezatwierdzona w APS110. Zespół AP koryguje opłaty za pomocą opcji Invoice Control w APS110, która wywołuje APS360.                                                                                                         |

## Przykład dla scenariusza 5

| Pole              | Wartość w PO | Wartość na fakturze dostawcy |
| ----------------- | ------------ | ---------------------------- |
| Linia 1           | $6000        | $6000                        |
| Fracht (E001)     | $1000        | $3000                        |
| **Razem**         | $7000        | $9000                        |

**Tolerancja dla frachtu:** $100 zatwierdzane automatycznie w M3 (APS900) i DocBits. Łączna wartość faktury $9000 zatwierdzona (wraz z opłatami) ręcznie.

**APS451 (linia faktury):**

* Typ linii 1 (linia faktury): $9000
* Typ linii 5 (opłata liniowa): $1000 (element: E001 dla frachtu w PO $1000)
* Typ linii 5 (opłata liniowa): $2000 (element: E101 dla frachtu w PO $0)

### Ważne pola i wartości dla obsługi opłat dodatkowych w DocBits

| Pole                        | Opis                                                              |
| --------------------------- | ----------------------------------------------------------------- |
| Sequence Number             | Unikalny identyfikator każdego scenariusza opłat                  |
| Costing Element ID          | Identyfikator elementu kosztowego                                 |
| Costing Element Description | Opis elementu kosztowego                                          |
| Charge Type                 | Zazwyczaj "External"                                              |
| Charge Invoicing            | Istotność do ustalenia                                            |
| Distribution Method         | Metoda używana do rozdzielania opłat                              |
| Gross Weight                | Ma zastosowanie, jeśli waga brutto jest dostępna na fakturze      |
| Volume                      | Przypadki zastosowania do zdefiniowania                           |
| Net Amount                  | Przypadki zastosowania do zdefiniowania                           |
| 3rd Party Charge            | Występowanie na fakturze i wymagania dotyczące przetwarzania      |
| Invoice Charge Quantity     | Wymaga wyjaśnienia                                                |
| Markup                      | Przyjmuje się, że jest to różnica między opłatą a rabatem         |
| Charge Category             | Istotność do zdefiniowania                                        |
| Costing Operator            | Istotność do zdefiniowania                                        |

\
