# Wyjaśnianie i poprawa Touchless przez MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Rozdział filmu (wersja do oceny):** [Odpytywanie wskaźników przez MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pl.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Poniższe przepływy pracy używają narzędzi rzeczywiście udostępnianych przez DocBits MCP. Rozróżniaj czytanie i wyjaśnianie od zapisywania. Sprawdź organizację, rolę, typ dokumentu, okres i znacznik czasu danych; nie wymyślaj brakujących dowodów.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-pl.png" alt="Rzeczywisty angielski widok własnego fikcyjnego PO w Dev: 10 × 9 = 90. To porównanie źródła do diagnozy przez MCP, a nie zrzut klienta MCP ani dowód pomyślnego odczytu lub przetworzenia."><figcaption><p>Rzeczywisty angielski widok własnego fikcyjnego PO w Dev: 10 × 9 = 90. To porównanie źródła do diagnozy przez MCP, a nie zrzut klienta MCP ani dowód pomyślnego odczytu lub przetworzenia.</p></figcaption></figure>

## Wyjaśnianie Touchless przez MCP

> Wyjaśnij Pure Touchless, wyniki wymagające tylko zatwierdzenia i łączny wskaźnik AP dla faktur z ostatnich 30 dni. Podaj licznik, mianownik, dokumenty w toku i wyłączone, zakres oraz znacznik czasu danych. Poprawność odczytu trzymaj osobno.

Użyj `touchless_get_summary` z `period: "30d"` i `doc_type: "INVOICE"`. Dla podprocesu używaj tylko pól i wartości segmentów rzeczywiście zwróconych przez `touchless_list_segments`. Porównuj panel i MCP dla tej samej organizacji, typu dokumentu, segmentu i okresu; odczytaj `data_as_of`.

**Zweryfikowany kontrprzykład z Dev:** Trzy nowo przesłane faktury testowe były nadal `IN_PROGRESS`. Podsumowanie zwróciło `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` i `official_touchless_rate.ap_pct: null`. Nie było jeszcze mierzalnego wskaźnika. To ani 0% dokładności odczytu, ani 100% Touchless. Kwalifikowalność w podsumowaniu odnosi się tutaj do zakończonej populacji KPI; pojedynczy ślad może jednocześnie pokazywać `eligible: true` i `bucket_final: false`.

Przykłady MCP na tych pięciu stronach używają bezpośrednich narzędzi DocBits MCP sprawdzonych w Dev. Obowiązuje organizacja i rola Twojego połączonego konta; dostępność w innym interfejsie lub dodatkowa lista dozwolonych narzędzi nie jest tym testem potwierdzona.

## FAQ

**DocBits odczytał wszystko poprawnie. Dlaczego faktura jest AP assisted?**
Touchless mierzy cały proces. Nieprawidłowe lub nieaktualne dane w Infor mogą wymagać zarejestrowanej poprawki albo ręcznego restartu, nawet przy poprawnym odczycie. Sprawdź osobno oryginalną fakturę, wartości odczytane przez DocBits i zaimportowane dane źródłowe.

**Czy AP assisted mówi, czy pracę spowodował DocBits, czy Infor?**
Nie. Rejestruje interwencję, a nie odpowiedzialność. Aby potwierdzić przyczynę, użyj śladu dokumentu oraz samego dokumentu i danych źródłowych.

**Wskaźniki pokazują kreskę (—).** Żaden dokument nie osiągnął w okresie wyniku końcowego albo zmierzono mniej dokumentów niż minimum. Dokumenty, które są nadal w toku, nie są liczone.

**Brakuje karty.** Poproś administratora o włączenie modułu i przyznanie Twojej roli karty **Analytics dashboard**.

**Dokument jest liczony jako dotknięty, ale tym razem przeszedł bez nikogo.** Został dotknięty we wcześniejszym uruchomieniu (poprawka lub restart). Wskaźnik liczy pracę, która się odbyła.

**Dlaczego liczba zmienia się po kilku godzinach?** ERP może potwierdzić eksport kilka godzin po jego wysłaniu. Wynik jest przeliczany co 15 minut.

**Czy AI coś zmienia samodzielnie?** Nie. AI pisze wyłącznie wyjaśnienia. Ustawienie zmienia się dopiero wtedy, gdy administrator obejrzy podgląd i je zastosuje.

## Badanie rozbieżności przez MCP

> Sprawdź numer PO tej faktury, status importu i faktycznie aktywne reguły dopasowania. Oddziel odczyt, nieaktualny import, nieprawidłowe dane źródłowe i brakującą konfigurację. Na razie nic nie zmieniaj.

1. Porównaj oryginał, `get_extracted_fields` i `get_extracted_tables`, zanim stwierdzisz poprawny odczyt.
2. Użyj `get_po_sync_status` z `po_number: "TL20261104X1-PO02"` i `language: "en"`. Test w Dev potwierdził przetworzony import i istniejące PO. Dowodzi to dotarcia, a nie poprawności biznesowej ani bieżącego rekordu w Infor.
3. Użyj `touchless_get_document_trace` i `touchless_explain_po_match` z tym samym `doc_id`. Odczytaj rzeczywisty silnik, wersję aktywnych reguł, kolumny i efektywne tolerancje. Dla rzeczywiście zwróconego klastra użyj jego `issue_signature` w `touchless_get_po_match_evidence`.
4. Zachowaj brakujące dowody: nasz nowy typ testowy zwrócił `state: "none_published"` i `parse_error: "no published rule set"`, a także puste pola odczytu. Nie udowodniono blokady ceny lub ilości ani udanego dopasowania. Ogólny przepływ decyzji nie zastąpi tych brakujących kontroli.
5. Usuń potwierdzoną przyczynę i sprawdź nowe faktury. Ręczna poprawka lub restart pozostają istotne po powodzeniu; końcowe niepowodzenie w ERP ma pierwszeństwo jako wyjątek, a niezakończony dokument jest poza mianownikiem wskaźnika.

Dla pełnego przypadku zachowaj oryginał, odczyt sprzed poprawki, zaimportowane i bieżące wartości źródłowe oraz czas importu, rzeczywiste reguły, działanie AP i wynik końcowy. Brakujące dowody pozostają otwarte.

## Odczyt dowodów przez MCP

> Sprawdź tę fakturę bez jej zmieniania. Porównaj oryginał, bieżące pola i tabele. Wyjaśnij zarejestrowane etapy i uruchomienia oraz wskaż brakujące historyczne dowody odczytu.

| Narzędzie, z tym samym `doc_id` | Dowód i ograniczenie |
| --- | --- |
| `get_extracted_fields` | Bieżące wartości nagłówka i pewność; to nie jest historyczny zapis |
| `get_extracted_tables` | Rzeczywiste tabele i wiersze; to nie dowód ich zgodności z oryginałem |
| `touchless_get_document_trace` | Zarejestrowane wyniki, interwencje, etapy i uruchomienia |
| `touchless_explain_pipeline` | Wyjaśnienie udokumentowanej ścieżki przetwarzania; nie uzupełnia brakujących dowodów |

**Zaobserwowana kontrola negatywna:** Nasza świeża faktura testowa miała etap odczytu nagłówka ze stanem `passed`, ale `extracted_field_count: 0`, osiem pustych wymaganych pól i brak tabeli. Walidacja pól zablokowała dokument z `REQUIRED_FIELD_MISSING`. Asystent musi zbadać brakujący odczyt lub konfigurację, a nie twierdzić, że odczyt był poprawny na podstawie zielonego etapu, ani że istnieje udowodniona blokada ceny PO na podstawie różnych wartości źródłowych.

### Czy działanie przez MCP liczy się jako dotknięcie przez człowieka?

Inspekcja tylko do odczytu nie zmienia faktury. Inne narzędzia MCP mogą zapisywać pola, walidować lub restartować. Klasyfikacja zależy od zarejestrowanego zdarzenia i od tego, czy jego wykonawcą jest człowiek, czy konto systemowe. Klucz API może działać jako konto systemowe; samo "wykonane przez MCP" nie dowodzi ani dotknięcia przez człowieka, ani Pure Touchless. Nigdy nie używaj poświadczeń systemowych, aby ukryć ręczną pracę.

Po działaniu na dokumencie sprawdź `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, status końcowy i uruchomienia. Samo zatwierdzenie biznesowe różni się od zapisanej poprawki, ręcznej walidacji lub ręcznego restartu.

## Priorytetyzacja dostawców i weryfikacja trwałej poprawy przez MCP

> Uszereguj dostawców tracących najwięcej faktur Touchless. Oddziel błędy odczytu, rozbieżności zaimportowanego źródła i ustawienia procesu. Zaproponuj jedno działanie i weryfikowalną kontrolę sukcesu dla każdej potwierdzonej przyczyny; na razie nic nie zmieniaj.

1. Użyj `touchless_rank_supplier_opportunities` z `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Użyj `search` dla numeru lub nazwy dostawcy; `limit` i `offset` dzielą wyniki na strony.
2. Przekaż zwrócony `supplier_key` bez zmian do `touchless_diagnose_supplier`. Użyj `window: 30` dla bieżących problemów albo 90, aby zbadać powtarzające się problemy.
3. Przekaż rzeczywiście zwrócony `issue_signature` do `touchless_get_issue_cluster`. Przed potwierdzeniem przyczyny przejrzyj przykładowe dokumenty i brakujące dowody. Nie wymyślaj identyfikatorów.
4. Użyj `touchless_get_recommendations`, aby wyjaśnić obsługiwane działanie. Oczekiwany wzrost to szacunek; nakładających się klastrów nie wolno po prostu dodawać.
5. Po poprawce sprawdź nowe porównywalne faktury oraz [pomiar zmiany](touchless-change-proposals.md). Wcześniej dotknięte faktury nie stają się wstecznie Pure Touchless.

Dla poprawnego odczytu i nieaktualnych PO popraw dane źródłowe lub import. Dla rozbieżności między oryginałem a odczytem zbadaj konfigurację odczytu. Zatwierdzenie wymagane przez politykę to odrębny, pomyślny wynik AP Touchless. Pusty ranking nie jest dowodem braku problemów: nasze trzy faktury testowe w toku nie dały jeszcze żadnego uszeregowania dostawców. Sprawdź zakres, znacznik czasu danych, identyfikację dostawcy i zakończony wolumen.

## Podgląd, zastosowanie i pomiar przez MCP

> Wyjaśnij potwierdzoną przyczynę i wymień obsługiwane propozycje. Pokaż podgląd wybranej zmiany, jej zasięg i ryzyka. Zastosuj tylko tę wybraną zmianę, a następnie zweryfikuj zapisane ustawienie, historię zmian i mierzalny efekt.

| Krok | Narzędzie i rzeczywiste zwracane identyfikatory | Co to dowodzi |
| --- | --- | --- |
| Lista | `touchless_list_change_proposals`, opcjonalnie `issue_signature`, `window: "30d"`, `lang: "en"` | Dostępne propozycje; żadne ustawienie nie jest zapisane |
| Podgląd | `touchless_preview_change` ze zwróconym `proposal_id` i pasującym `issue_signature` | Konkretny zasięg i powiązany `preview_token`, gdy jest dozwolony |
| Zastosowanie wybranej zmiany | `touchless_apply_change` z tymi samymi identyfikatorami, `preview_token`, `overrides` i `window` | **Zapisuje** obsługiwane ustawienie; pomyślna odpowiedź zwraca `change_id` |
| Odczyt efektu | `touchless_verify_change` z tym `change_id` i tym samym `window` | Pomiar przed/po; nadal wymagane co najmniej 20 kwalifikujących się zakończonych dokumentów w każdym okresie |

Kopiuj identyfikatory i tokeny z rzeczywistych odpowiedzi. Token z podglądem jednej wartości nie może zastosować innej wartości. Wygasły, zabroniony lub niekompletny podgląd nie jest dowodem zastosowanej zmiany. Narzędzi tylko do odczytu i zastosowania nie wolno przedstawiać jako równoważnych. Ta tabela wyjaśnia sekwencję narzędzi; nie twierdzi, że demonstracja wykonała propozycję lub zmierzyła zysk.

**Przykład konfiguracji:** Po potwierdzonej poprawce konfiguracji sprawdź rzeczywiście zapisaną wartość i nowe faktury. 52% przed i 61% po to zaobserwowana różnica 9 punktów procentowych, a nie dowód, że spowodowała ją wyłącznie ta zmiana. **Przykład danych źródłowych:** Błędne PO w Infor wymaga korekty biznesowej i zweryfikowanego importu. `touchless_apply_change` nie jest ogólnym narzędziem zapisu do Infor. Nie poszerzaj tolerancji, aby ukryć nieprawidłowe dane źródłowe.

Zrzut raportu pokazuje rekomendacje i szacowany wpływ, a nie zastosowanie lub wycofanie. Pomyślne zastosowanie wymaga odpowiedzi o sukcesie i wpisu w historii. Undo jest dostępne tylko tam, gdzie wybrana propozycja je obsługuje; zweryfikuj rzeczywiście przywrócone ustawienie. Ponowne wczytanie historii nie stosuje ustawienia, a wycofanie nie usuwa przeszłych interwencji na dokumentach.

## Powiązane strony

* [Touchless Intelligence](./)
* [Wskaźniki i obliczenia](../../touchless-metrics.md)
* [Korzystanie z panelu](touchless-dashboard.md)
* [Przykłady: cena i ilość](touchless-examples.md)
* [Diagnoza dostawcy i klastry problemów](../../touchless-supplier-diagnosis.md)
* [Diagnoza dopasowania PO](../../touchless-po-matching-diagnosis.md)
* [Ślad dokumentu](touchless-document-trace.md)
* [Propozycje zmian i raporty](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
