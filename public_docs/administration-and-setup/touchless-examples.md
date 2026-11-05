# Przykłady: cena i ilość

<!-- touchless-admin-video-v2-20261104:start -->
**Rozdział filmu (wersja do oceny):** [Śledzenie dokumentu](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pl.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Pełny przykład: poprawny odczyt, inne dane Infor

Przykład ilustracyjny: faktura **10 sztuk × 10 € = 100 €**, odczyt poprawny. Importowane zamówienie **10 × 9 € = 90 €**. Zakładamy, że aktywne reguły blokują różnicę.

1. Porównaj oryginał i odczyt; wartości są zgodne.
2. Sprawdź import, aktualne Infor, jednostkę ceny i datę. Błędne źródło i stara kopia to różne problemy.
3. Zakupy potwierdzają 10 € i poprawiają zamówienie. Gdyby uzgodniono 9 €, należałoby wyjaśnić fakturę.
4. Potwierdź poprawne wartości po imporcie do DocBits.
5. AP uruchamia ponownie ręcznie; po sukcesie wynik to **AP Assisted**, mimo poprawnego odczytu.
6. Sprawdź nowe faktury bez dalszych ingerencji. Historia wcześniejszych pozostaje.

Nie zmieniaj poprawnie odczytanych wartości ani tolerancji, aby ukryć błędną informację. Usuń potwierdzoną przyczynę. Zrzuty nie dowodzą całej tej ścieżki.

## Trzy zamówienia demonstracyjne: zgodność, cena i ilość

Fikcyjny dostawca, towar i faktury utworzone tylko na **Dev**. Każda faktura ma **10 sztuk × 10 € = 100 € netto**. Karty zachowują prawdziwy polski interfejs i powiększają liczby. Nie dowodzą połączenia klienta z Infor, poprawnej ekstrakcji ani udanego procesu automatycznego.

| Przypadek | Faktura | Importowane zamówienie | Dowód |
| --- | --- | --- | --- |
| PO01 / RE01 | 10 × 10 € = 100 € | 10 × 10 € = 100 € | Zgodne dane źródłowe; Pure wymaga jeszcze odczytu i zakończenia bez ingerencji/zatwierdzeń |
| PO02 / RE02 | 10 × 10 € = 100 € | 10 × 9 € = 90 € | Różnica 10 €, około 11,11 % ceny jednostkowej zamówienia; blokadę określają aktywne reguły |
| PO03 / RE03 | 10 × 10 € = 100 € | 8 × 10 € = 80 € | Dwie sztuki więcej, 25 % zamówionej ilości; sprawdź otwarte/otrzymane ilości i podstawę porównania |

<figure><img src="../.gitbook/assets/touchless-owned-po-match-pl.png" alt="PO01: zgodne wartości fikcyjnego zamówienia. Powiększony prawdziwy widok ilości, ceny i sumy nie dowodzi poprawnego odczytu ani Pure Touchless."><figcaption><p>PO01: zgodne wartości fikcyjnego zamówienia. Powiększony prawdziwy widok ilości, ceny i sumy nie dowodzi poprawnego odczytu ani Pure Touchless.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/touchless-owned-po-price-pl.png" alt="PO02: import pokazuje 10 × 9 = 90, fikcyjna faktura 10 × 10 = 100. Sprawdź uzgodnioną cenę, jednostkę ceny i import. Zapisana ingerencja człowieka i sukces oznaczają AP Assisted."><figcaption><p>PO02: import pokazuje 10 × 9 = 90, fikcyjna faktura 10 × 10 = 100. Sprawdź uzgodnioną cenę, jednostkę ceny i import. Zapisana ingerencja człowieka i sukces oznaczają AP Assisted.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/touchless-owned-po-quantity-pl.png" alt="PO03: zamówiono 8 sztuk, zafakturowano 10. Pusta ilość otrzymana nie dowodzi dostawy. Karta pokazuje porównanie, nie udane dopasowanie."><figcaption><p>PO03: zamówiono 8 sztuk, zafakturowano 10. Pusta ilość otrzymana nie dowodzi dostawy. Karta pokazuje porównanie, nie udane dopasowanie.</p></figcaption></figure>

## Powiązane strony

* [Touchless Intelligence](touchless-intelligence.md)
* [Wskaźniki i obliczenia](touchless-metrics.md)
* [Korzystanie z panelu](touchless-dashboard.md)
* [Touchless Intelligence: Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Ślad dokumentu](touchless-document-trace.md)
* [Touchless Intelligence: Propozycje zmian i raporty](touchless-change-proposals.md)
* [Wyjaśnianie i poprawa Touchless przez MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
