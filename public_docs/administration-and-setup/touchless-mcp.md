# Wyjaśnianie i poprawa Touchless przez MCP

Używaj rzeczywiście oferowanych narzędzi DocBits MCP. Oddziel odczyt od zapisu. Sprawdź organizację, rolę, typ, okres i datę; nie wymyślaj brakujących dowodów.

<figure><img src="../.gitbook/assets/touchless-owned-po-price-pl.png" alt="Prawdziwy polski widok fikcyjnego zamówienia na Dev: 10 × 9 = 90. To porównanie źródła do diagnozy MCP, nie zrzut klienta MCP ani dowód udanej ekstrakcji/przetwarzania."><figcaption><p>Prawdziwy polski widok fikcyjnego zamówienia na Dev: 10 × 9 = 90. To porównanie źródła do diagnozy MCP, nie zrzut klienta MCP ani dowód udanej ekstrakcji/przetwarzania.</p></figcaption></figure>

## Wyjaśnianie Touchless przez MCP

> Wyjaśnij Pure, samo zatwierdzenie i łączny AP faktur z 30 dni. Podaj licznik, mianownik, dokumenty w toku, wyłączenia, filtry i datę. Oddziel jakość odczytu od automatyzacji.

Użyj `touchless_get_summary` z `period: "30d"`, `doc_type: "INVOICE"`. Segmenty wybieraj wyłącznie z `touchless_list_segments`. Porównuj tę samą organizację, typ, okres i segment; sprawdzaj `data_as_of`.

**Rzeczywisty kontrprzykład Dev:** trzy faktury były `IN_PROGRESS`: `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0`, `official_touchless_rate.ap_pct: null`. Wskaźnika jeszcze nie można obliczyć; to nie oznacza 0 % poprawnego odczytu ani 100 % Touchless. W podsumowaniu `eligible` oznacza tu zakończoną populację KPI; pojedynczy ślad może równocześnie mieć `eligible: true`, `bucket_final: false`.

To rzeczywiście dostępne narzędzia MCP sprawdzone na Dev. Nadal obowiązują organizacja i uprawnienia. Nie dowodzi to dostępności w innym interfejsie lub dodatkowej liście dozwolonych narzędzi.

## Badanie rozbieżności przez MCP

> Sprawdź zamówienie, import i aktywne reguły. Oddziel ekstrakcję, starą kopię, błędne źródło i brak konfiguracji. Niczego nie zmieniaj.

1. Porównaj oryginał, `get_extracted_fields`, `get_extracted_tables` przed potwierdzeniem poprawnego odczytu.
2. `get_po_sync_status`: `po_number: "TL20261104X1-PO02"`, `language: "en"`. Obsługuje tylko `de` i `en`; wyjaśnij wynik po polsku. Przetworzony import nie dowodzi poprawności biznesowej ani bieżącego stanu Infor.
3. `touchless_get_document_trace`, `touchless_explain_po_match` z tym samym `doc_id`: sprawdź rzeczywisty silnik, wersję, kolumny i tolerancje. Otrzymany `issue_signature` przekaż do `touchless_get_po_match_evidence`.
4. Typ testowy zwrócił `state: "none_published"`, `parse_error: "no published rule set"` i puste pola. Nie udowodniono blokady ceny/ilości ani udanego dopasowania.
5. Usuń potwierdzoną przyczynę i sprawdź nowe faktury. Ręczne korekty/restarty pozostają po sukcesie; ostateczny błąd ERP ma pierwszeństwo. Dokumenty w toku są poza mianownikiem.

Pełny przypadek wymaga oryginału, ekstrakcji sprzed korekt, importu/aktualnego źródła z datą, użytych reguł, działania AP i wyniku końcowego. Brakujące dowody pozostają otwarte.

## Odczyt dowodów przez MCP

> Zbadaj fakturę bez zmian. Porównaj oryginał, bieżące pola i tabele. Wyjaśnij zapisane wykonania i brakujące dane historyczne.

| Narzędzie z tym samym `doc_id` | Ograniczenie |
| --- | --- |
| `get_extracted_fields` | Bieżące wartości i pewność, nie historyczna kopia |
| `get_extracted_tables` | Obecne tabele, nie dowód zgodności z oryginałem |
| `touchless_get_document_trace` | Zapisane wyniki, ingerencje i wykonania |
| `touchless_explain_pipeline` | Wyjaśnia dowiedzioną ścieżkę, nie uzupełnia braków |

**Negatywny test:** `header_extraction: passed`, ale `extracted_field_count: 0`, osiem pustych wymaganych pól, brak tabel. Blokada: `REQUIRED_FIELD_MISSING`. Sprawdź ekstrakcję/konfigurację; zielony etap nie dowodzi poprawnego odczytu ani blokady cenowej.

### Czy MCP oznacza ludzką ingerencję?

Czytanie niczego nie zmienia; inne narzędzia mogą pisać, walidować lub restartować. Klucz API może reprezentować system. Samo „przez MCP” nie dowodzi ingerencji człowieka ani Pure. Nie maskuj pracy człowieka kontem systemowym. Sprawdź `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, wynik i wykonania. Samo zatwierdzenie różni się od korekty, walidacji i restartu.

## Priorytety dostawców i kontrola poprawy przez MCP

> Uszereguj dostawców według utraconych dokumentów Touchless. Oddziel odczyt, dane źródłowe i konfigurację. Zaproponuj działanie i kontrolę dla potwierdzonej przyczyny, bez zmian.

1. `touchless_rank_supplier_opportunities`: `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. `search` szuka nazwy/numeru; `limit`, `offset` stronicują.
2. Przekaż otrzymany `supplier_key` do `touchless_diagnose_supplier`; `window: 30` dla stanu bieżącego, 90 do badania nawrotów.
3. Przekaż prawdziwy `issue_signature` do `touchless_get_issue_cluster`; sprawdź dokumenty i brakujące dowody.
4. `touchless_get_recommendations` opisuje obsługiwane działania. Zysk jest szacowany; nie sumuj nakładających się klastrów.
5. Sprawdź nowe porównywalne faktury i pomiar po zmianie. Dawniej obsłużona ręcznie faktura nie staje się Pure wstecz.

Poprawny odczyt i stare zamówienie wymagają naprawy źródła/importu. Rozbieżny odczyt wymaga kontroli ekstrakcji. Pusty ranking nie dowodzi braku problemu: trzy faktury w toku nie dawały zakończonych wyników dostawców. Sprawdź filtry, datę, identyfikację i liczbę zakończonych dokumentów.

## Podgląd, zastosowanie i pomiar przez MCP

> Wyjaśnij potwierdzoną przyczynę. Pokaż obsługiwane propozycje i podgląd wybranej zmiany. Zastosuj tylko ją, następnie sprawdź wartość, historię i efekt.

| Krok | Narzędzie | Wynik |
| --- | --- | --- |
| Lista | `touchless_list_change_proposals`, opcjonalnie `issue_signature`, `window: "30d"`, `lang: "pl"` | Istniejące propozycje, bez zapisu |
| Podgląd | `touchless_preview_change` z otrzymanymi `proposal_id`, `issue_signature` | Zakres i dozwolony powiązany `preview_token` |
| Zastosowanie | `touchless_apply_change` z tymi samymi ID, tokenem, `overrides`, `window` | **Zapisuje** ustawienie; sukces zwraca `change_id` |
| Pomiar | `touchless_verify_change` z tym `change_id` i `window` | Przed/po, co najmniej 20 zakończonych kwalifikujących się dokumentów na okres |

Nie wymyślaj ID ani tokenów. Inna wartość wymaga nowego podglądu; wygasły/niedozwolony podgląd nie dowodzi zapisu. Demo nie potwierdza zastosowanej propozycji ani zysku.

52 do 61 % to 9 zaobserwowanych punktów, nie dowód jednej przyczyny. `touchless_apply_change` nie jest ogólnym narzędziem zapisu Infor; błędne zamówienie wymaga korekty biznesowej i sprawdzonego importu. Nie rozszerzaj tolerancji, aby ukryć błąd.

Raport szacuje, nie stosuje ani nie cofa. Wymagaj sukcesu i wpisu historii. Cofnięcie jest dostępne tylko dla obsługujących je propozycji; sprawdź przywróconą wartość. Odświeżenie historii niczego nie stosuje. Cofnięcie nie usuwa wcześniejszych ingerencji.

## Powiązane strony

* [Touchless Intelligence](touchless-intelligence.md)
* [Wskaźniki i obliczenia](touchless-metrics.md)
* [Korzystanie z panelu](touchless-dashboard.md)
* [Przykłady: cena i ilość](touchless-examples.md)
* [Touchless Intelligence: Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Ślad dokumentu](touchless-document-trace.md)
* [Touchless Intelligence: Propozycje zmian i raporty](touchless-change-proposals.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
