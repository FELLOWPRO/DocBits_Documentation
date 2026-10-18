# Przykłady

Prompty oraz pełna procedura diagnozy, szkicu, aktywacji i cofnięcia są w [Konfigurowanie DocBits przez Claude lub Codex](../docbits-mcp/configuration-with-claude-or-codex.md). Przykłady używają aktualnych parametrów. Zastąp symbole zastępcze wartościami swojej organizacji i podaj pełne źródła z poprawnym kodowaniem znaków specjalnych JSON.

## 1. Zmiana istniejącej reguły Custom

Odczytaj efektywną `TRANSFORMATION` przez `get_edoc_attribute_source`, używając dokładnej etykiety formatu zwróconej przez klasyfikację:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Zachowaj `attribute_id`, `active_value_id`, `active_version` i `value`. Osobno odczytaj `source: "default"` do porównania oraz historię przez `list_edoc_attribute_versions`. Dalsze kroki zakładają istniejący atrybut Custom Twojej organizacji.

Sprawdź pełnego kandydata bez zapisu przez `preview_edoc_custom_xslt`. Użyj istniejącego dokumentu tej samej organizacji:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Wynik to przekształcony XML dla `TRANSFORMATION`, PDF dla `PREVIEW` albo pola/tabele dla `EXTRACTION_PATHS`. Podgląd nie wybiera zapisanego szkicu i nie testuje późniejszych skryptów ani eksportu.

Po sprawdzeniu różnic i podglądu odczytaj ponownie aktywne źródło i zapisz szkic przez `update_edoc_custom_attribute`. Jawnie podaj `activate: false`; domyślna wartość to `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Po testach w organizacji testowej i potwierdzeniu konkretnej zmiany wywołaj `activate_edoc_attribute_version`. `draft_id` to ID wartości wersji. Odczytaj ponownie źródło efektywne. Cofnięcie używa wcześniejszego `active_value_id` w tym samym wywołaniu.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Gdy nie ma atrybutu Custom

`create_edoc_custom_attribute` tworzy od razu aktywną pierwszą wersję, nie szkic. Testuj nowe nadpisanie w organizacji testowej albo użyj obsługiwanego procesu edytora DocBits. Nie twórz ani nie usuwaj nadpisań produkcyjnych tylko dla podglądu. Zachowaj wymagane mapowania; nie zmieniaj globalnie współdzielonych reguł domyślnych.

## 3. Test aktywnej konfiguracji

Wywołaj `test_electronic_document` z oryginalnym XML zakodowanym jako base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

To testuje aktywne reguły bez zapisu dokumentu, nie nieaktywny szkic. Zdalny HTTP MCP nie odczyta lokalnego `file_path` z Twojego komputera. `compare_edoc_extraction` porównuje tylko Extraction Paths i wymaga własnego atrybutu ścieżek ekstrakcji; nie porównuje transformacji.

`validate_all_edocs` testuje bez zapisu dostępne pliki testowe serwera. `verify_electronic_documents` przesyła je i przetwarza, tworząc dokumenty. Żadne z nich nie dowodzi dostarczenia do ERP. Użyj reprezentatywnych próbek, osobno sprawdź zapisane pola/kwoty i eksport oraz nie restartuj zbiorczo dokumentów historycznych.
