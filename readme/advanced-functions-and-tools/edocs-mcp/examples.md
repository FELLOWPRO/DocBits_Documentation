# Przykłady

Kompleksowe przykłady pokazujące, jak używać narzędzi eDocs MCP razem.

## Przykład 1: Utwórz niestandardowy podgląd dla XRechnung

Ten przykład przeprowadza przez pełny cykl życia niestandardowej reguły PREVIEW:
1. Sprawdź, jakie reguły już istnieją
2. Wyświetl podgląd XSLT bez jego aktywacji
3. Utwórz regułę niestandardową
4. Zaktualizuj ją do nowej wersji
5. Wróć do wartości domyślnej

### Krok 1: Sprawdź istniejące dostosowania

Wywołaj `list_edoc_custom_attributes`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

Odpowiedź zawiera dwie listy. Jeśli `custom` jest puste dla atrybutu `PREVIEW`, Twoja organizacja korzysta obecnie z wbudowanego domyślnego arkusza stylów podglądu.

### Krok 2: Przetestuj XSLT przed jego utworzeniem

Wywołaj `preview_edoc_custom_xslt` z identyfikatorem istniejącego atrybutu (użyj domyślnego z odpowiedzi `list`) oraz przykładowym plikiem XML zakodowanym w base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Sprawdź wyrenderowany wynik, aby upewnić się, że Twój XSLT daje oczekiwany rezultat, zanim go zatwierdzisz.

### Krok 3: Utwórz regułę niestandardową

Wywołaj `create_edoc_custom_attribute`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Zachowaj `attribute_id` z odpowiedzi. Od tej chwili każda faktura XRechnung 2.1 CII przetwarzana przez Twoją organizację będzie używać Twojego niestandardowego podglądu.

### Krok 4: Zaktualizuj regułę do nowej wersji

Później, jeśli chcesz udoskonalić XSLT, wywołaj `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Ustawienie `activate: true` natychmiast przełącza na nową wersję. Poprzednia wersja jest zachowywana w historii. Ustaw `activate: false`, aby zapisać ją jako wersję roboczą i aktywować osobno.

### Krok 5: Wróć do wbudowanej wartości domyślnej

Jeśli chcesz wrócić do domyślnego podglądu, wywołaj `delete_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

Reguła niestandardowa zostaje usunięta, a system automatycznie wraca do współdzielonego domyślnego arkusza stylów. Nie ma to wpływu na innych klientów.

---

## Przykład 2: Dostosuj ścieżki ekstrakcji dla EDI

Twoja organizacja otrzymuje faktury EDI o niestandardowym układzie pól. Ten przykład pokazuje, jak nadpisać ścieżki ekstrakcji dla Twojej organizacji.

### Krok 1: Sprawdź bieżące reguły

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Jeśli widzisz wpis `EXTRACTION_PATHS` w `default`, ale nie w `custom`, Twoja organizacja dziedziczy współdzielone reguły XPath.

### Krok 2: Utwórz własne ścieżki ekstrakcji

Wywołaj `create_edoc_custom_attribute` ze swoim dostosowanym JSON-em XPath:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Krok 3: Zweryfikuj próbnym testem

Wywołaj `test_electronic_document` z przykładowym plikiem EDI, aby potwierdzić, że niestandardowe ścieżki ekstrakcji pobierają właściwe wartości:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

Odpowiedź zawiera `extracted_fields` oraz obraz PNG `preview.image_base64` — sprawdź oba, aby zweryfikować poprawność przed wdrożeniem.

---

## Przykład 3: Uruchom pełną weryfikację eDoc

Przed wdrożeniem zmiany sprawdź, czy wszystkie obsługiwane próbki eDoc nadal przechodzą:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

Narzędzie uruchamia w potoku każdą próbkę XRechnung i zgłasza wynik pass/fail/warn dla każdej z nich. Czysty przebieg potwierdza, że Twoje dostosowania nie zepsuły innych typów dokumentów.

Aby szybko przetestować tylko jeden typ:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Przesyła do 3 próbek ZUGFeRD, czeka na przetworzenie i weryfikuje klasyfikację, ekstrakcję oraz generowanie podglądu od początku do końca.
