# Konfigurowanie DocBits przez Claude lub Codex

Opisz oczekiwany wynik, pozwól asystentowi odczytać konfigurację, sprawdź propozycję, a następnie zastosuj uzgodnioną zmianę. DocBits MCP udostępnia te narzędzia w Claude i Codex z uprawnieniami połączonego konta DocBits. Zmiany konfiguracji wymagają odpowiednich uprawnień administratora.

Ta instrukcja opisuje procedurę. Nie potwierdza wykonania poprawki u klienta ani pomyślnego testu eksportu.

## 1. Połącz się z właściwą organizacją

Wybierz region i środowisko w [instrukcji endpointów i logowania](setup-and-configuration.md). Polecenia używają **sandbox UE**; zmień URL, jeśli organizacja testowa korzysta z innego endpointu. Uruchom je na komputerze asystenta, zaloguj się i zatwierdź dostęp do DocBits w przeglądarce.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

W aplikacji Codex użyj ustawień MCP lub konfiguracji współdzielonej z CLI na tym samym komputerze. W Claude Desktop użyj własnego zdalnego konektora, jeśli plan go obsługuje, z tym samym endpointem HTTP. Rozpocznij nową rozmowę, jeśli narzędzia nie są widoczne. Aktualne instrukcje: [Codex MCP](https://developers.openai.com/codex/mcp) i [Claude MCP](https://code.claude.com/docs/en/mcp).

```text
Tylko odczyt. Sprawdź połączone środowisko i organizację DocBits przez
get_api_info i get_current_user. Wyświetl dostępne narzędzia konfiguracji.
Pokaż ID organizacji i host API, bez tokenów ani fragmentów kluczy.
Nie zmieniaj ustawień i nie przetwarzaj dokumentów.
```

Jeśli organizacja nie została jeszcze ustalona, odczytaj odpowiednią konfigurację i sprawdź `org_id` w odpowiedzi. Przerwij, jeśli to niewłaściwa organizacja. Nazwy narzędzi mogą zawierać prefiks klienta/serwera. Używaj narzędzi i schematów argumentów rzeczywiście udostępnianych przez połączenie.

## 2. Zmień proste ustawienie

```text
Znajdź przez find_setting ustawienie ekstrakcji kodów QR w tej organizacji
testowej. Pokaż dokładny setting_key i bieżącą wartość. Przy kilku wynikach
zapytaj, o który chodzi. Jeśli apply_setting obsługuje to ustawienie,
przygotuj podgląd włączenia. Pokaż current_value i proposed_value;
czekaj na moje potwierdzenie przed confirm_setting_change.
```

`apply_setting` tworzy tylko podgląd. Po potwierdzeniu konkretnej propozycji `confirm_setting_change(preview_id)` zapisuje zmianę. Odczytaj wartość ponownie i zachowaj `undo_id`: `undo_setting_change` pozwala cofnąć zmianę w zwróconym limicie czasu. Podgląd zwykle wygasa po 5 minutach, a cofnięcie po 15. Jeśli wartość się zmieniła lub podgląd wygasł, utwórz i sprawdź nowy.

Dla obsługiwanych zmian strukturalnych: `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Najpierw odczytaj dostępne typy akcji. Jeśli brak obsługiwanej akcji zapisu, poproś o `app_path` i wykonaj zmianę w DocBits. Nie wymyślaj klucza preferencji ani nie zastępuj tego ogólnym wywołaniem `set_preference`.

## 3. Zbadaj notę kredytową zapisaną jako Invoice

Transformacja Custom może stale zwracać `<INVOICE_TYPE>Invoice</INVOICE_TYPE>`, mimo że oryginalny XML zawiera kod noty kredytowej. To scenariusz z [instrukcji diagnostycznej z filmem z prawdziwego interfejsu DocBits](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Tylko odczyt. Dla dostarczonego oryginalnego XML i ID dokumentu ustal rodzinę
eDoc, składnię, wersję/profil i oryginalny kod typu. Wyświetl atrybuty Custom
i Default. Odczytaj efektywne i domyślne TRANSFORMATION i EXTRACTION_PATHS
przez get_edoc_attribute_source. Zapisz attribute_id, active_version
i active_value_id oraz odczytaj historię wersji.
Prześledź TypeCode -> przekształcony XML -> invoice_type -> zapisane pole,
podgląd eksportu i późniejsze skrypty. Pokaż dowody i niewiadome.
Niczego nie aktywuj, nie usuwaj, nie uruchamiaj ponownie, nie zatwierdzaj ani nie eksportuj.
```

Użyj **dokładnej etykiety wykrytego formatu**; nie zgaduj wersji ZUGFeRD ani Factur-X. Techniczny `doc_type_key` może nadal wynosić `INVOICE`; badana wartość biznesowa to `invoice_type`.

| Odczyt | Narzędzie MCP |
| --- | --- |
| Atrybuty Custom i Default | `list_edoc_custom_attributes` |
| Źródło efektywne lub domyślne i aktywne ID | `get_edoc_attribute_source`, z `source: "effective"` lub `"default"` |
| Historia i wersje robocze | `list_edoc_attribute_versions`, w razie potrzeby z `include_values: true` |
| Zapisane pola, logi, podgląd eksportu | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

Dzisiejsza aktywna wersja nie dowodzi, która przetwarzała dokument historyczny. Jeśli logi tego nie potwierdzają, zachowaj tę niepewność. Podgląd PDF nie dowodzi zapisanego typu ani wyeksportowanych kwot.

<figure><img src="../../.gitbook/assets/edocs-transformation-pl.png" alt="Przykład deweloperski tylko do odczytu: edytor źródła i wersji DocBits. Odczytaj własne źródło efektywne i aktywną wartość przez MCP; obraz nie pokazuje zapisanej zmiany."><figcaption><p>Przykład deweloperski tylko do odczytu: edytor źródła i wersji DocBits. Odczytaj własne źródło efektywne i aktywną wartość przez MCP; obraz nie pokazuje zapisanej zmiany.</p></figcaption></figure>

## 4. Sprawdź najmniejszą poprawkę bez zapisu

```text
Zaproponuj najmniejszą zmianę naszej istniejącej transformacji Custom,
aby 381 dawał Credit Note. Zachowaj pozostałe mapowania i wcześniej
obsługiwane kody not kredytowych. Nie klasyfikuj 383 ani 384 jako Credit Note.
Pokaż diff. Sprawdź kandydata na dokumentach testowych bez zapisu.
Pokaż przekształcone INVOICE_TYPE i istotne kwoty oraz brakujące testy.
```

Dla **istniejącego atrybutu własnej organizacji** wywołaj `preview_edoc_custom_xslt` z pełnym proponowanym kodem:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Zastąp wszystkie symbole zastępcze wartościami z odpowiedzi. XSLT/JSON musi zawierać pełne źródło z poprawnym kodowaniem znaków specjalnych JSON. Narzędzie używa istniejącego dokumentu tej samej organizacji. Zwraca **XML** dla `TRANSFORMATION`, pola/tabele dla `EXTRACTION_PATHS` lub **PDF** dla `PREVIEW`, bez zapisu kandydata. Aby porównać transformację domyślną, sprawdź jej źródło jako kolejnego kandydata z tym samym atrybutem Custom i dokumentem.

`compare_edoc_extraction` porównuje **EXTRACTION_PATHS** i wymaga własnego atrybutu ścieżek ekstrakcji. Nie porównuje dwóch transformacji. Nie twórz zbędnego nadpisania tylko dla tego narzędzia.

Jeśli nie ma atrybutu Custom, zatrzymaj się przed utworzeniem go w produkcji: `create_edoc_custom_attribute` tworzy pierwszą wersję **od razu aktywną**, bez opcji samego szkicu. Przygotuj nowe nadpisanie w organizacji testowej albo użyj obsługiwanego procesu tworzenia/podglądu w edytorze DocBits. Nie próbuj globalnie zmieniać współdzielonych reguł domyślnych.

## 5. Zapisz wersję roboczą, potem świadomie aktywuj

Po sprawdzeniu różnic i wyniku odczytaj ponownie aktywne źródło. Jeśli uległo zmianie, porównaj je ponownie. Dla istniejącego atrybutu Custom użyj `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Zawsze podawaj `activate: false` w tym kroku; domyślna wartość narzędzia to `true`. Zachowaj zwrócone ID wartości wersji i sprawdź przez `list_edoc_attribute_versions`, czy poprzednia wersja pozostaje aktywna. Zapisana wersja robocza nie zmienia normalnego przetwarzania.

Po testach administrator potwierdza konkretną organizację, atrybut, różnice i wersję. Aktywuj przez `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` to **ID wartości wersji**, nie numer wersji ani ID atrybutu. Ponownie odczytaj źródło efektywne i historię, aby potwierdzić aktywację dokładnie tej wartości. eDocs używa tych narzędzi bezpośrednio, bez ogólnego procesu ustawień z `preview_id`. Odczytuj ID w środowisku docelowym; ID z sandboxa nie działają w produkcji.

## 6. Sprawdź klasyfikację, kwoty i eksport

`test_electronic_document` testuje **obecnie aktywną** konfigurację bez zapisywania dokumentu. Nie ma parametru wyboru kandydata ani szkicu. Przy zdalnym HTTP MCP wyślij oryginalny XML jako `file_content_base64` z `file_name`; serwer nie odczyta lokalnego `file_path` z Twojego komputera. Aby sprawdzić cały proces dla kandydata, najpierw jawnie aktywuj go w organizacji testowej. Sam podgląd XSLT nie testuje późniejszych skryptów ani eksportu.

| Kod oryginalny | Oczekiwana kontrola |
| --- | --- |
| 380 | Invoice pozostaje Invoice |
| 381 | Nota kredytowa staje się Credit Note |
| 261 | Zachować zachowanie noty kredytowej, jeśli format/mapowanie je obsługuje |
| 383 | Nota debetowa nie staje się Credit Note tylko dlatego, że zmienia fakturę |
| 384 | Faktura skorygowana nie staje się Credit Note tylko dlatego, że koryguje fakturę |

Sprawdź własne pola, pozycje, sumy i ustawienie znaku ujemnego. Przetwórz **nowy dokument testowy** w odizolowanej organizacji z kontrolowanymi automatycznymi eksportami. Porównaj zapisane `invoice_type`, pulpit i `get_export_preview`. Faktyczny eksport do systemu docelowego wymaga osobno uzgodnionego testu; ani dry-run, ani podgląd nie dowodzą skutecznego dostarczenia do ERP.

`validate_all_edocs` testuje bez zapisu pliki testowe dostępne na serwerze; `verify_electronic_documents` **przesyła i przetwarza** pliki testowe. Nie zastępują reprezentatywnych dokumentów i kontroli dalszego przetwarzania. Jeśli brakuje plików lub narzędzi, użyj dostarczonych próbek.

## 7. Cofnij zmianę i osobno obsłuż stare dokumenty

Aby cofnąć zmianę, wywołaj `activate_edoc_attribute_version` z wcześniejszym `active_value_id` jako `draft_id` i sprawdź źródło efektywne. Nie usuwaj całego nadpisania, aby poprawić jedno pole: utracisz pozostałe mapowania i powrócą reguły domyślne.

Nie uruchamiaj zbiorczo ponownie historycznych dokumentów. Restart może usunąć wyodrębnione dane i logi eksportu oraz powtórzyć zatwierdzenia lub eksporty. Najpierw sprawdź dla każdego dokumentu status eksportu, zatwierdzenia i ręczne zmiany.

Inne pytania o konfigurację zaczynaj od `find_setting` lub `run_config_checks`, prosząc o obsługiwaną akcję lub ścieżkę w interfejsie. Zachowaj propozycję przed/po, wyniki testów, ID aktywnych wartości i sposób cofnięcia w rejestrze zmiany.
