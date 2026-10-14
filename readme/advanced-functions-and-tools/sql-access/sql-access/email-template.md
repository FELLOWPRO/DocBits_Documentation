# Email template

## Kolumny

* `id`: wewnętrzne
* `org_id`: ID organizacji
* `name`: wewnętrzne
* `email_type`: wewnętrzne
* `value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `subject`: wewnętrzne
* `last_modified_by`: wewnętrzne
* `deleted_by`: wewnętrzne
* `doc_type`: typ DOC

## Analiza i opis

```markdown
# Dokumentacja techniczna tabeli `public.email_template`

## Wprowadzenie

Tabela `public.email_template` służy do przechowywania szablonów wiadomości e-mail używanych w systemie. Szablony te są powiązane z różnymi organizacjami i prawdopodobnie służą do wysyłania ustandaryzowanej korespondencji e-mail. Tabela zawiera metadane szablonów, w tym szczegóły utworzenia i modyfikacji, a także śledzi, czy szablon został usunięty.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego szablonu e-mail.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Ciąg UUID, np. `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Uwaga**: Stanowi główny identyfikator rekordu szablonu.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z szablonem e-mail.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Ciąg UUID.
- **Uwaga**: Łączy szablon z konkretną organizacją.

### name
- **Znaczenie**: Nazwa szablonu e-mail.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Tekst opisowy, np. `Supplier Magic Link Email`.
- **Uwaga**: Służy do identyfikacji przeznaczenia szablonu.

### email_type
- **Znaczenie**: Typ lub kategoria szablonu e-mail.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków, takie jak `supplier_invite`.
- **Uwaga**: Wskazuje kontekst lub sposób użycia szablonu.

### value
- **Znaczenie**: Treść szablonu e-mail, zazwyczaj w formacie HTML.
- **Rola**: Pole treści.
- **Typowa zawartość**: Ciąg HTML zawierający układ i treść wiadomości e-mail.
- **Uwaga**: Jest to właściwy szablon używany w wiadomościach e-mail.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył szablon.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.
- **Uwaga**: Rejestruje, kto utworzył szablon.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia szablonu.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Znacznik czasu, np. `2024-07-18 13:29:59 UTC`.
- **Uwaga**: Rejestruje datę i godzinę utworzenia.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji szablonu.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Znacznik czasu.
- **Uwaga**: Rejestruje najnowszą aktualizację szablonu.

### is_deleted
- **Znaczenie**: Wskazuje, czy szablon został oznaczony jako usunięty.
- **Rola**: Pole techniczne.
- **Typowa zawartość**: Wartość logiczna, `True` lub `False`.
- **Uwaga**: Służy do miękkiego usuwania szablonu.

### deleted_on
- **Znaczenie**: Znacznik czasu oznaczenia szablonu jako usuniętego.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Znacznik czasu lub `None`, jeśli szablon nie został usunięty.
- **Uwaga**: Rejestruje, kiedy szablon został usunięty.

### subject
- **Znaczenie**: Temat wiadomości w szablonie e-mail.
- **Rola**: Pole treści.
- **Typowa zawartość**: Tekst, np. `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Uwaga**: Używany jako temat wiadomości e-mail podczas wysyłania szablonu.

### last_modified_by
- **Znaczenie**: Identyfikator użytkownika, który ostatni zmodyfikował szablon.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Identyfikator użytkownika.
- **Uwaga**: Rejestruje, kto ostatni zmodyfikował szablon.

### deleted_by
- **Znaczenie**: Identyfikator użytkownika, który oznaczył szablon jako usunięty.
- **Rola**: Pole metadanych.
- **Typowa zawartość**: Identyfikator użytkownika.
- **Uwaga**: Rejestruje, kto usunął szablon.

### doc_type
- **Znaczenie**: Typ lub format dokumentu powiązanego z szablonem.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków wskazujące typ dokumentu.
- **Uwaga**: Może odnosić się do formatu lub kategorii treści wiadomości e-mail.
```
