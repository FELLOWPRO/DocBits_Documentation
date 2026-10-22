# Przychodzące wiadomości e-mail

## Tabela `public.inbound_emails`

### Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `is_active`: boolean
* `email_senders`: internal
* `email_receiver`: internal
* `token`: internal
* `created_by`: integer
* `created_on`: znacznik czasu ze strefą czasową
* `last_modified_by`: internal
* `last_modified_on`: znacznik czasu ze strefą czasową
* `is_deleted`: boolean
* `deleted_by`: internal
* `deleted_on`: znacznik czasu ze strefą czasową

### Analiza i opis

## Dokumentacja techniczna: tabela `public.inbound_emails`

### Wprowadzenie

Tabela `public.inbound_emails` służy do przechowywania i zarządzania informacjami o wiadomościach e-mail otrzymanych przez organizację. Śledzi dane nadawcy i odbiorcy, status wiadomości oraz różne metadane dotyczące tworzenia, modyfikowania i usuwania rekordów. Wydaje się być częścią systemu zarządzania pocztą e-mail w organizacji, prawdopodobnie używaną do śledzenia przychodzącej korespondencji e-mail.

### Opis kolumn

#### id

* **Znaczenie**: Unikalny identyfikator każdego rekordu w tabeli.
* **Rola**: Klucz główny.
* **Typowa zawartość**: Unikalny ciąg znaków, prawdopodobnie UUID, taki jak `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Znaczenie**: Identyfikator organizacji powiązanej z przychodzącą wiadomością e-mail.
* **Rola**: Klucz obcy, odwołujący się do innej tabeli zawierającej dane organizacji.
* **Typowa zawartość**: Unikalny ciąg znaków, prawdopodobnie UUID, taki jak `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Znaczenie**: Wskazuje, czy rekord wiadomości e-mail jest aktualnie aktywny.
* **Rola**: Wskaźnik statusu.
* **Typowa zawartość**: Wartość logiczna: `True` lub `False`.

#### email\_senders

* **Znaczenie**: Przechowuje informacje o nadawcach wiadomości e-mail.
* **Rola**: Pole danych.
* **Typowa zawartość**: Ciąg znaków w formacie zbliżonym do JSON, zawierający szczegóły nadawców, np. `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Znaczenie**: Adres e-mail głównego odbiorcy.
* **Rola**: Pole danych.
* **Typowa zawartość**: Ciąg znaków z adresem e-mail. W przykładzie jest puste, co sugeruje opcjonalne lub zmienne użycie.

#### token

* **Znaczenie**: Token powiązany z wiadomością e-mail, prawdopodobnie do uwierzytelniania lub identyfikacji.
* **Rola**: Pole uwierzytelniania lub śledzenia.
* **Typowa zawartość**: Długi, losowo wygenerowany ciąg znaków.

#### created\_by

* **Znaczenie**: Identyfikator użytkownika, który utworzył rekord.
* **Rola**: Klucz obcy, odwołujący się do tabeli użytkowników lub pracowników.
* **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika, np. `1`.

#### created\_on

* **Znaczenie**: Znacznik czasu utworzenia rekordu.
* **Rola**: Pole metadanych.
* **Typowa zawartość**: Wartość daty i godziny z informacją o strefie czasowej, np. `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Znaczenie**: Identyfikator użytkownika, który ostatnio zmodyfikował rekord.
* **Rola**: Klucz obcy, odwołujący się do tabeli użytkowników lub pracowników.
* **Typowa zawartość**: Może to być identyfikator użytkownika lub null, jeśli nie wprowadzono żadnych modyfikacji.

#### last\_modified\_on

* **Znaczenie**: Znacznik czasu ostatniej modyfikacji rekordu.
* **Rola**: Pole metadanych.
* **Typowa zawartość**: Wartość daty i godziny wskazująca czas ostatniej modyfikacji, np. `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Znaczenie**: Wskazuje, czy rekord wiadomości e-mail został oznaczony jako usunięty.
* **Rola**: Wskaźnik statusu.
* **Typowa zawartość**: Wartość logiczna: `True` lub `False`.

#### deleted\_by

* **Znaczenie**: Identyfikator użytkownika, który oznaczył rekord jako usunięty.
* **Rola**: Klucz obcy, odwołujący się do tabeli użytkowników lub pracowników.
* **Typowa zawartość**: Może to być identyfikator użytkownika lub null, jeśli rekord nie został usunięty.

#### deleted\_on

* **Znaczenie**: Znacznik czasu oznaczenia rekordu jako usuniętego.
* **Rola**: Pole metadanych.
* **Typowa zawartość**: Wartość daty i godziny wskazująca czas usunięcia lub domyślna data, jeśli nie dotyczy, np. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
