# eDocs MCP

API DocBits udostępnia serwer **Model Context Protocol (MCP)** z narzędziami do sprawdzania i dostosowywania przetwarzania dokumentów elektronicznych (eDoc). Połączyć się i korzystać z tych narzędzi może dowolny klient zgodny z MCP — Claude Code, Claude Desktop lub niestandardowe integracje.

## Co możesz zrobić?

Dzięki narzędziom eDocs MCP możesz:

- **Sprawdzać**, jak klasyfikowany jest dowolny typ dokumentu elektronicznego i jakie reguły ekstrakcji mają zastosowanie
- **Testować** dokumenty w pełnym potoku przetwarzania bez zapisu do bazy danych
- **Tworzyć niestandardowe reguły** dla swojej organizacji — podglądy XSLT, ścieżki ekstrakcji, transformacje
- **Aktualizować** regułę niestandardową nową wersją (z natychmiastową aktywacją lub bez)
- **Usuwać** regułę niestandardową, aby wrócić do wbudowanej wartości domyślnej
- **Weryfikować**, czy wszystkie obsługiwane próbki eDoc są przetwarzane poprawnie

## Model uprawnień

DocBits zawiera bibliotekę wbudowanych reguł domyślnych współdzielonych przez wszystkich klientów. Reguły domyślne używają zarezerwowanego identyfikatora organizacji `00000000-0000-0000-0000-000000000000`.

**Reguły domyślne są niezmienne przez MCP.** Każde narzędzie zapisu sprawdza identyfikator Twojej organizacji przed wysłaniem jakiegokolwiek żądania. Jeśli wskazuje on organizację domyślną, operacja jest natychmiast odrzucana — wywołanie API nigdy nie jest wykonywane.

Klienci mogą tworzyć, zmieniać i usuwać reguły wyłącznie **w obrębie własnej organizacji**. Gdy dla Twojej organizacji istnieje reguła niestandardowa, ma ona pierwszeństwo przed domyślną. Usunięcie reguły niestandardowej automatycznie przywraca zachowanie domyślne.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Przegląd narzędzi

### Sprawdzanie (tylko do odczytu)

| Narzędzie | Opis |
|------|-------------|
| `test_electronic_document` | Próbne uruchomienie pełnego potoku eDoc — klasyfikacja, ekstrakcja, podgląd — bez zapisu |
| `list_electronic_document_types` | Wyświetla wszystkie obsługiwane typy eDoc wraz ze statusem konfiguracji |
| `get_extraction_rules` | Pokazuje reguły XPath używane do wyodrębniania pól dla danego typu dokumentu |
| `get_extracted_fields` | Pobiera pola nagłówka wyodrębnione z przetworzonego dokumentu |
| `get_extracted_tables` | Pobiera pozycje wyodrębnione z przetworzonego dokumentu |
| `get_preview_pdf` | Pobiera podgląd PDF wyrenderowany przez XSLT dla dokumentu |
| `get_preview_image` | Pobiera wyrenderowany obraz strony przetworzonego dokumentu |
| `extract_edoc_table` | Wyodrębnia przekazany plik XML/EDI i zwraca pola jako płaską tabelę wraz z regułą, która wytworzyła każde z nich |
| `compare_edoc_extraction` | Porównuje ekstrakcję domyślną i Twoją niestandardową (oraz opcjonalnie regułę kandydującą) na jednym dokumencie |

### Dostosowywanie (w zakresie organizacji, organizacja domyślna zablokowana)

| Narzędzie | Opis |
|------|-------------|
| `list_edoc_custom_attributes` | Wyświetla niestandardowe nadpisania Twojej organizacji w porównaniu z wbudowanymi wartościami domyślnymi dla typu dokumentu |
| `create_edoc_custom_attribute` | Tworzy nową regułę niestandardową (EXTRACTION_PATHS, TRANSFORMATION lub PREVIEW) |
| `update_edoc_custom_attribute` | Dodaje nową wersję reguły niestandardowej, opcjonalnie od razu ją aktywując |
| `delete_edoc_custom_attribute` | Usuwa regułę niestandardową — system automatycznie wraca do wartości domyślnej |
| `preview_edoc_custom_xslt` | Próbne uruchomienie transformacji XSLT na dokumencie XML przed aktywacją |
| `get_edoc_attribute_source` | Pobiera edytowalne źródło atrybutu (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION), aby go zmienić |
| `list_edoc_attribute_versions` | Historia wersji atrybutu niestandardowego: wersje robocze i aktywna wersja |
| `activate_edoc_attribute_version` | Aktywuje konkretną wersję lub wersję roboczą (w ten sposób wykonujesz wycofanie) |
| `delete_edoc_attribute_draft` | Usuwa wersję roboczą, która nigdy nie została aktywowana |

### Weryfikacja

| Narzędzie | Opis |
|------|-------------|
| `verify_electronic_documents` | Przesyła próbki i weryfikuje klasyfikację, ekstrakcję i podgląd od początku do końca |
| `validate_all_edocs` | Uruchamia wszystkie próbki eDoc w potoku próbnym i zgłasza problemy |

## Typy atrybutów

Każda reguła, którą można dostosować, ma określony typ i format:

| Nazwa atrybutu | Format | Cel |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | Wyrażenia XPath mapujące węzły XML na pola DocBits |
| `TRANSFORMATION` | XSLT | Arkusz stylów stosowany do XML przed ekstrakcją |
| `PREVIEW` | XSLT | Arkusz stylów renderujący czytelny dla człowieka podgląd PDF |
| `STRUCTURE_DESCRIPTOR` | JSON | Mapa struktury wyłącznie dla dokumentów EDI |

Narzędzie `create_edoc_custom_attribute` automatycznie określa właściwy format na podstawie nazwy atrybutu.

## Szybki start

### Wyświetl, co Twoja organizacja dostosowała

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Zwraca dwie listy: `custom` (nadpisania Twojej organizacji) i `default` (współdzielone reguły, które dziedziczysz).

### Utwórz niestandardowy podgląd dla XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Zwraca nowy `attribute_id` — zachowaj go do aktualizacji i usuwania.

### Zaktualizuj istniejącą regułę niestandardową

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Tworzy nową wersję i ją aktywuje. Poprzednia wersja jest zachowywana w historii.

### Wróć do wartości domyślnej

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Usuwa niestandardowe nadpisanie. System natychmiast wraca do wbudowanej reguły domyślnej.

## Zasady bezpieczeństwa

| Akcja | Dozwolone |
|--------|---------|
| Odczyt reguł domyślnych | ✅ Tak |
| Tworzenie reguły niestandardowej dla Twojej organizacji | ✅ Tak |
| Aktualizacja reguły niestandardowej dla Twojej organizacji | ✅ Tak |
| Usuwanie reguły niestandardowej dla Twojej organizacji | ✅ Tak |
| Modyfikowanie lub usuwanie reguł domyślnych | ❌ **Nigdy** — blokowane w warstwie MCP |

Próba zapisu do `00000000-0000-0000-0000-000000000000` zwraca:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

## Faktycznie używane reguły i aktywacja

Jeśli elektroniczna nota kredytowa jest wyświetlana jako Invoice, skorzystaj z [przewodnika rozwiązywania problemów z klasyfikacją](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md). Opisuje on faktycznie używane źródło niestandardowe lub domyślne, kody typów, Extraction Paths i bezpieczną aktywację.

[Konfigurowanie DocBits przez Claude lub Codex](../docbits-mcp/configuration-with-claude-or-codex.md): połączenie, prompty, podglądy, wersjonowane zmiany, kontrole i cofnięcie.
