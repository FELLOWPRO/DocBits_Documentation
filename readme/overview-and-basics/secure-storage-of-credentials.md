---
description: Haszowanie haseł, przechowywanie kluczy API, TLS, dostęp do danych uwierzytelniających i odzyskiwanie dostępu do konta w DocBits.
---

# Bezpieczne przechowywanie danych uwierzytelniających

DocBits obsługuje hasła logowania, klucze API DocBits, informacje o kontach i dane uwierzytelniające systemów zewnętrznych zgodnie z ich przeznaczeniem. Ta strona opisuje ochronę i odzyskiwanie dostępu dla każdej z tych kategorii.

## Hasła logowania

DocBits przechowuje hasła logowania jako **jednokierunkowe skróty kryptograficzne z solą**. Podczas uwierzytelniania wprowadzone hasło jest sprawdzane względem zapisanego skrótu. Oryginalne hasło nie jest przechowywane w postaci, którą można odszyfrować i odczytać.

Administratorzy i pomoc techniczna DocBits nie mogą więc odzyskać istniejącego hasła w postaci jawnej z zapisanego skrótu. Jeśli użytkownik zapomni hasła, musi je zresetować, aby ponownie logować się przy użyciu hasła.

### Resetowanie hasła

1. Wybierz **Zapomniałeś hasła?** na ekranie logowania.
2. Wprowadź adres e-mail powiązany z kontem.
3. Otwórz link do resetowania wysłany na ten adres.
4. Ustaw nowe hasło i zaloguj się za jego pomocą.

Linki do resetowania wygasają. Jeśli link wygasł, poproś o nowy. Procedura ustawia nowe hasło; nie ujawnia poprzedniego. Pełne instrukcje znajdują się na stronie [Uzyskiwanie dostępu i logowanie](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

Konta ze skonfigurowanym SSO lub kluczem dostępu (passkey) mogą korzystać z tej alternatywnej metody logowania. W przypadku SSO odzyskiwaniem hasła zajmuje się dostawca tożsamości. Zobacz [Uwierzytelnianie dwuskładnikowe](two-factor-authentication.md).

## Klucze API DocBits

Klucze utworzone w funkcji **Zarządzanie kluczami API** są wyświetlane w całości tylko raz, podczas tworzenia. DocBits zapisuje jednokierunkowy skrót klucza oraz krótki prefiks identyfikacyjny. Prefiks i metadane pozostają widoczne na liście zarządzania; pełnego oryginalnego klucza nie można odzyskać z jego skrótu.

Ani administratorzy, ani pomoc techniczna DocBits nie mogą odczytać pełnego klucza po jego utworzeniu. Jeśli klucz zostanie utracony, unieważnij go i utwórz nowy. Każdy klucz może mieć datę wygaśnięcia i można go unieważnić oddzielnie. Zobacz [Zarządzanie kluczami API](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Dane kont i dane uwierzytelniające systemów zewnętrznych

Imiona i nazwiska, adresy e-mail, role i statusy kont to informacje, które upoważnieni administratorzy organizacji mogą przeglądać i którymi mogą zarządzać. Są one odrębne od sekretu używanego do uwierzytelniania. Zobacz [Użytkownicy](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Dane uwierzytelniające przekazane dla systemów zewnętrznych, takich jak konto usługi ERP, skrzynka pocztowa lub serwer SFTP, również różnią się od hasła DocBits lub klucza API wydanego przez DocBits. Konektor może potrzebować sekretu w użytecznej postaci, aby uwierzytelnić się w systemie zewnętrznym. Dlatego sposób przechowywania i kontrole dostępu należy ocenić osobno dla danego konektora.

Brak możliwości odzyskania hasła lub klucza API DocBits przechowywanego jako skrót **nie oznacza**, że wszystkie informacje o kontach lub sekrety integracji są niedostępne dla dostawcy. Każde zapewnienie dotyczące dostępu personelu do danych uwierzytelniających integracji wymaga potwierdzenia odpowiednich operacyjnych kontroli dostępu.

## Szyfrowanie podczas przesyłania

Poniższe publiczne punkty końcowe DocBits obsługują **TLS 1.2 i TLS 1.3** przez HTTPS. Sprawdzenie przeprowadzone **16 października 2026 r.** potwierdziło odrzucanie TLS 1.0 i TLS 1.1.

| Punkt końcowy | Przeznaczenie | Zweryfikowane wersje TLS |
| --- | --- | --- |
| `app.docbits.com` | Aplikacja internetowa | TLS 1.2 i TLS 1.3 |
| `auth.docbits.com` | Usługa uwierzytelniania | TLS 1.2 i TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 i TLS 1.3 |

### Jakie rodzaje szyfrowania są obsługiwane podczas przesyłania?

| Pytanie | Odpowiedź dla powyższych publicznych punktów końcowych |
| --- | --- |
| Czy TLS 1.1 jest obsługiwany? | **Nie.** Połączenia korzystające z TLS 1.1 są odrzucane. |
| Czy TLS 1.2 jest obsługiwany? | **Tak.** |
| Czy TLS 1.3 jest obsługiwany? | **Tak.** |

Poniższe metody szyfrowania zostały pomyślnie wynegocjowane na **wszystkich trzech punktach końcowych** w testach z walidacją certyfikatów 16 października 2026 r.:

| Metoda szyfrowania | Długość klucza symetrycznego | Zweryfikowane wersje TLS |
| --- | --- | --- |
| AES-128-GCM | 128 bitów | TLS 1.2 i TLS 1.3 |
| AES-256-GCM | 256 bitów | TLS 1.2 i TLS 1.3 |
| ChaCha20-Poly1305 | 256 bitów | TLS 1.3 |

Metody te zapewniają szyfrowanie uwierzytelnione, chroniąc poufność i integralność przesyłanych danych. Wynegocjowana metoda zależy od możliwości i konfiguracji klienta oraz serwera. Podane długości dotyczą symetrycznych kluczy szyfrowania danych, niezależnie od rozmiarów kluczy certyfikatów. Przetestowane zestawy szyfrów TLS 1.2 używają ECDHE do wymiany kluczy efemerycznych.

Weryfikacja obejmuje połączenia z tymi publicznymi punktami końcowymi, w tym połączenia klientów i innych serwerów. Nie określa ustawień protokołów ani szyfrowania każdego wewnętrznego połączenia między usługami, połączenia z bazą danych, regionalnego punktu końcowego czy integracji zewnętrznej. Połączenia te wymagają potwierdzenia dla danego wdrożenia i integracji.

## Szyfrowanie przechowywanych informacji o kontach

Haszowanie haseł i kluczy API jest innym zabezpieczeniem niż szyfrowanie baz danych, woluminów, obiektów i kopii zapasowych. Opisane kontrole nie dowodzą, że każda nazwa użytkownika, każde pole konta lub każdy sekret integracji są szyfrowane indywidualnie ani że wszystkie przechowywane dane korzystają z określonego algorytmu szyfrowania.

Jeśli wymaganie obejmuje wszystkie informacje o kontach klientów, należy uzyskać od FELLOWPRO AG oświadczenie dotyczące konkretnego wdrożenia, obejmujące odpowiednie magazyny danych i kopie zapasowe, metody szyfrowania, zarządzanie kluczami oraz dostęp personelu. Sam model hostingu w chmurze lub serverless nie potwierdza tych właściwości.

## Odpowiedź na kwestionariusz bezpieczeństwa klienta

Poniższy tekst opisuje potwierdzony zakres:

> Hasła logowania DocBits są przechowywane jako jednokierunkowe skróty kryptograficzne z solą. Administratorzy i pomoc techniczna DocBits nie mogą odzyskać oryginalnego hasła w postaci jawnej z zapisanego skrótu. Użytkownicy, którzy zapomnieli hasła, muszą ustawić nowe za pomocą procedury resetowania przez e-mail, aby ponownie logować się hasłem. Skonfigurowane SSO lub klucze dostępu zapewniają alternatywne metody logowania.
>
> Klucze utworzone w funkcji Zarządzanie kluczami API DocBits są pokazywane tylko raz i zapisywane jako jednokierunkowe skróty. Ani administratorzy, ani pomoc techniczna DocBits nie mogą później odzyskać pełnego klucza. Utracone klucze należy unieważnić i zastąpić nowymi.
>
> Wymienione powyżej publiczne punkty końcowe aplikacji internetowej, uwierzytelniania i API DocBits obsługują HTTPS z TLS 1.2 i TLS 1.3; TLS 1.0 i TLS 1.1 zostały odrzucone podczas sprawdzenia 16 października 2026 r. Zweryfikowano AES-128-GCM z kluczem 128-bitowym i AES-256-GCM z kluczem 256-bitowym dla TLS 1.2 i TLS 1.3 oraz ChaCha20-Poly1305 z kluczem 256-bitowym dla TLS 1.3. Oświadczenie dotyczy połączeń z tymi punktami końcowymi. Szyfrowanie wszystkich przechowywanych informacji o kontach i kopii zapasowych, ochrona każdego wewnętrznego połączenia między serwerami oraz dostęp personelu do danych uwierzytelniających integracji zewnętrznych wymagają osobnego potwierdzenia dla danego wdrożenia.
