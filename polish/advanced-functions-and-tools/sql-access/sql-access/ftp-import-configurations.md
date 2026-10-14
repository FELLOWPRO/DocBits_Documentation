# FTP Import Configurations

## Kolumny

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `server_url`: internal
* `username`: internal
* `password`: internal
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `port`: integer
* `default_directory`: internal
* `ftp_type`: internal
* `token`: internal
* `file_name_matching_patterns`: internal
* `last_mtime`: internal
* `auth_failed_count`: integer
* `auth_message`: text
* `ignore_certificate`: boolean
* `move_after_import`: boolean
* `destination_directory`: internal
* `import_directory`: internal
* `include_subfolder_content`: boolean

## Analiza i opis

```markdown
# Dokumentacja tabeli FTP Import Configurations

## Wprowadzenie

Tabela `public.ftp_import_configurations` służy do przechowywania szczegółów konfiguracji procesów importu przez FTP. Zawiera informacje niezbędne do łączenia się z serwerami FTP, zarządzania uwierzytelnianiem i obsługi importu plików. Obsługuje protokoły FTP i SFTP oraz zawiera pola dotyczące szczegółów serwera FTP, danych uwierzytelniających i ustawień operacyjnych, takich jak przenoszenie plików po imporcie oraz uwzględnianie zawartości podfolderów.

## Opis kolumn

### id
- **Znaczenie**: Unikalny identyfikator każdego rekordu konfiguracji importu FTP.
- **Rola**: Klucz główny.
- **Typowa zawartość**: Format UUID, np. `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Znaczenie**: Identyfikator organizacji powiązanej z tą konfiguracją.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Format UUID.

### sub_org_id
- **Znaczenie**: Identyfikator podorganizacji, jeśli dotyczy.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Format UUID lub `null`, jeśli nie dotyczy.

### server_url
- **Znaczenie**: Adres URL lub adres IP serwera FTP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Nazwa domeny lub adres IP, np. `sftp.it.doxee.com`.

### username
- **Znaczenie**: Nazwa użytkownika używana do uwierzytelniania na serwerze FTP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Nazwa użytkownika w postaci zwykłego tekstu.

### password
- **Znaczenie**: Hasło używane do uwierzytelniania na serwerze FTP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zaszyfrowany ciąg znaków z hasłem.

### is_active
- **Znaczenie**: Wskazuje, czy konfiguracja jest aktualnie aktywna.
- **Rola**: Flaga statusu.
- **Typowa zawartość**: `True` lub `False`.

### created_by
- **Znaczenie**: Identyfikator użytkownika, który utworzył konfigurację.
- **Rola**: Klucz obcy.
- **Typowa zawartość**: Liczba całkowita reprezentująca identyfikator użytkownika.

### created_on
- **Znaczenie**: Znacznik czasu utworzenia konfiguracji.
- **Rola**: Pole audytowe.
- **Typowa zawartość**: Data i godzina wraz z informacją o strefie czasowej.

### last_modified_on
- **Znaczenie**: Znacznik czasu ostatniej modyfikacji konfiguracji.
- **Rola**: Pole audytowe.
- **Typowa zawartość**: Data i godzina wraz z informacją o strefie czasowej.

### is_deleted
- **Znaczenie**: Wskazuje, czy konfiguracja została oznaczona jako usunięta.
- **Rola**: Flaga statusu.
- **Typowa zawartość**: `True` lub `False`.

### deleted_on
- **Znaczenie**: Znacznik czasu oznaczenia konfiguracji jako usuniętej.
- **Rola**: Pole audytowe.
- **Typowa zawartość**: Data i godzina wraz z informacją o strefie czasowej lub domyślna data dla rekordów, które nie zostały usunięte.

### port
- **Znaczenie**: Numer portu używany do połączenia z serwerem FTP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita, np. `22` dla SFTP.

### default_directory
- **Znaczenie**: Domyślna ścieżka katalogu na serwerze FTP.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków ze ścieżką katalogu.

### ftp_type
- **Znaczenie**: Typ używanego protokołu FTP (np. FTP, SFTP).
- **Rola**: Pole opisowe.
- **Typowa zawartość**: `FTP` lub `SFTP`.

### token
- **Znaczenie**: Token zabezpieczający służący do dodatkowego uwierzytelnienia lub identyfikacji.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Zaszyfrowany lub zakodowany ciąg znaków.

### file_name_matching_patterns
- **Znaczenie**: Wzorce używane do dopasowywania nazw plików do importu.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciągi znaków ze wzorcami lub `null`.

### last_mtime
- **Znaczenie**: Czas ostatniej modyfikacji plików, używany do filtrowania importów.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków reprezentujący znacznik czasu lub `null`.

### auth_failed_count
- **Znaczenie**: Licznik nieudanych prób uwierzytelnienia.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Liczba całkowita, np. `0` lub `5`.

### auth_message
- **Znaczenie**: Komunikat opisujący wynik ostatniej próby uwierzytelnienia.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Komunikat tekstowy lub `null`.

### ignore_certificate
- **Znaczenie**: Wskazuje, czy walidacja certyfikatu SSL ma być pomijana.
- **Rola**: Flaga statusu.
- **Typowa zawartość**: `True` lub `False`.

### move_after_import
- **Znaczenie**: Wskazuje, czy pliki mają być przenoszone po zakończeniu importu.
- **Rola**: Flaga statusu.
- **Typowa zawartość**: `True` lub `False`.

### destination_directory
- **Znaczenie**: Ścieżka katalogu, do którego pliki mają być przenoszone po imporcie.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków ze ścieżką katalogu lub `null`.

### import_directory
- **Znaczenie**: Ścieżka katalogu, z którego importowane są pliki.
- **Rola**: Pole opisowe.
- **Typowa zawartość**: Ciąg znaków ze ścieżką katalogu lub `null`.

### include_subfolder_content
- **Znaczenie**: Wskazuje, czy zawartość podfolderów ma być uwzględniana w imporcie.
- **Rola**: Flaga statusu.
- **Typowa zawartość**: `True` lub `False`.
```

Niniejsza dokumentacja zapewnia kompleksowe zrozumienie każdej kolumny w tabeli `public.ftp_import_configurations`, wyjaśniając jej przeznaczenie, rolę i typową zawartość na podstawie podanych danych i nazw kolumn.
