---
description: Szyfrowanie danych DocBits w spoczynku na DigitalOcean, w tym bazy danych, Spaces i zakres kopii zapasowych.
---

# Szyfrowanie danych w spoczynku

DocBits korzysta z DigitalOcean Managed Databases i DigitalOcean Spaces. Weryfikacja z **16 października 2026 r.** potwierdziła zarządzane usługi PostgreSQL, OpenSearch i Valkey dla produkcji w UE we Frankfurcie. [FAQ dotyczące bezpieczeństwa i zgodności](security-and-compliance-faq.md) opisuje wykorzystanie Spaces do przechowywania danych.

Ta strona opisuje zabezpieczenia szyfrowania opublikowane przez DigitalOcean dla tych usług. Instalacje lokalne i kopie przechowywane w innych systemach wymagają osobnej oceny.

## Metody szyfrowania i zakres

| Usługa przechowywania | Szyfrowanie w spoczynku | Zakres ochrony |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | Szyfrowanie całych woluminów za pomocą LUKS; `aes-xts-plain64:sha256` z 512-bitowym materiałem klucza XTS | Woluminy usługi bazy danych, w tym przechowywane na nich dane. Jest to ochrona na poziomie pamięci masowej, a nie zapewnienie osobnego szyfrowania każdego pola bazy danych. |
| Kopie zapasowe Managed Databases | AES-256 w trybie CTR, z HMAC-SHA256 dla integralności; klucze poszczególnych plików chronione przez RSA-3072 | Kopie tworzone przez zarządzaną usługę bazy danych. Dodatkowe eksporty i kopie wymagają osobnej weryfikacji. |
| DigitalOcean Spaces | Szyfrowanie całych dysków za pomocą 256-bitowego AES-XTS | Dane na fizycznych dyskach. Jest to zabezpieczenie odrębne od opcjonalnego szyfrowania obiektów lub szyfrowania po stronie klienta. |
| DigitalOcean Volumes, jeśli są używane | Szyfrowanie klastra pamięci masowej za pomocą LUKS | Dane na tych woluminach blokowych; migawki woluminów dziedziczą szyfrowanie. |

XTS używa dwóch kluczy AES. Łączne 512 bitów materiału klucza XTS zarządzanej usługi bazy danych odpowiada dwóm 256-bitowym kluczom AES (AES-256-XTS), a nie algorytmowi AES z kluczem 512-bitowym.

Szczegóły dotyczące baz danych i kopii pochodzą z [modelu bezpieczeństwa Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). [Model bezpieczeństwa Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) potwierdza szyfrowanie w spoczynku; [model bezpieczeństwa App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) wskazuje 256-bitowy AES-XTS dla fizycznych dysków Spaces. [Funkcje Volumes](https://docs.digitalocean.com/products/volumes/details/features/) opisują zakres ochrony woluminów i migawek.

## Zarządzanie kluczami i uprawniony dostęp

DigitalOcean zarządza opisanym szyfrowaniem infrastruktury. Dla Managed Databases dokumentuje losowo generowany klucz dla każdej instancji i woluminu, usuwany podczas niszczenia instancji. Kopie zapasowe zarządzanych baz danych używają losowego klucza dla każdego pliku, chronionego parą kluczy RSA przypisaną do usługi.

Szyfrowanie pamięci masowej chroni dane na nośnikach. Uprawnione aplikacje i użytkownicy bazy danych nadal mogą odczytywać dane za pośrednictwem usługi. Nie potwierdza to, że personel dostawcy nie może uzyskać dostępu do informacji o kontach ani że każde pole jest szyfrowane na poziomie aplikacji. Haszowanie haseł i kluczy API jest osobnym zabezpieczeniem; zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).

Spaces obsługuje również [SSE-C z kluczami dostarczonymi przez klienta](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Ta opcjonalna funkcja nie potwierdza, że DocBits używa SSE-C lub kluczy szyfrowania zarządzanych przez klienta.

## Szyfrowanie kopii zapasowych

Kopie zapasowe tworzone przez DigitalOcean Managed Databases są szyfrowane za pomocą AES-256-CTR i chronione przed niewykrytymi zmianami przez HMAC-SHA256. Klucze szyfrowania poszczególnych plików są chronione za pomocą RSA-3072. Migawki woluminów zachowują szyfrowanie bazowego woluminu DigitalOcean. Te informacje opisują funkcje tworzenia kopii zapasowych wymienionych usług zarządzanych.

## Rodzaje szyfrowania danych w spoczynku

Poniżej przedstawiono główne metody szyfrowania wymienionych usług:

> DocBits korzysta z DigitalOcean Managed Databases i Spaces. Dane zarządzanych baz danych są szyfrowane w spoczynku na poziomie całych woluminów za pomocą LUKS z AES-256-XTS (łącznie 512 bitów materiału klucza XTS). Kopie zapasowe zarządzanych baz danych używają AES-256-CTR z ochroną integralności HMAC-SHA256 oraz RSA-3072 do ochrony kluczy szyfrowania poszczególnych plików. Spaces stosuje szyfrowanie całych dysków za pomocą 256-bitowego AES-XTS na fizycznych nośnikach.
>
> Te zabezpieczenia na poziomie pamięci masowej obejmują dane na chronionych woluminach i dyskach; nie oznaczają osobnego szyfrowania każdego pola bazy danych. DigitalOcean zarządza kluczami szyfrowania infrastruktury. Oświadczenie obejmuje wymienione usługi zarządzane.
