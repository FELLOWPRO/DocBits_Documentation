# Uzyskiwanie dostępu i logowanie

Na tej stronie opisano, jak uzyskać konto DocBits i jak się zalogować, gdy nie masz swojego hasła:

* [Rejestracja](getting-access-and-signing-in.md#rejestracja) — utwórz własne konto DocBits.
* [Zapomniane hasło](getting-access-and-signing-in.md#zapomniane-hasło) — zresetuj hasło za pomocą linku do resetowania.
* [Pierwsze hasło dla kont utworzonych przez administratora](getting-access-and-signing-in.md#pierwsze-hasło-dla-kont-utworzonych-przez-administratora) — ustaw pierwsze hasło do konta, które administrator utworzył dla Ciebie.

Logowanie do istniejącego konta oraz Uwierzytelnianie dwuskładnikowe są opisane na stronie [Uwierzytelnianie dwuskładnikowe (2FA)](../../overview-and-basics/two-factor-authentication.md). Jeśli potrzebujesz innego języka wyświetlania, użyj menu języka w prawym górnym rogu tych formularzy.

## Rejestracja

Konto DocBits możesz utworzyć samodzielnie na stronie rejestracji. Otwórz ją za pomocą linku **Rejestr** na ekranie logowania lub przejdź do adresu `https://app.docbits.com/register` (użyj adresu internetowego przekazanego Twojej organizacji).

<figure><img src="../../.gitbook/assets/dbdc745-getting-access-register-form-pl-20261011.png" alt="Formularz rejestracji DocBits z pustymi polami"><figcaption><p>Formularz rejestracji. Wszystkie pola są wymagane, chyba że zaznaczono inaczej.</p></figcaption></figure>

Wypełnij formularz:

1. **Imię** i **Nazwisko** — Twoje imię i nazwisko, tak jak mają być widoczne w DocBits.
2. **E-mail** — Twój służbowy adres e-mail. Jest to Twój identyfikator logowania.
3. **Hasło** i **Potwierdź hasło** — patrz zasady haseł poniżej. Lista kontrolna pod polem hasła pokazuje, które zasady Twoje hasło już spełnia.
4. Jeśli strona wyświetla widget **reCAPTCHA**, wypełnij go. Widget pojawia się tylko wtedy, gdy wdrożenie DocBits ma włączoną ochronę przed botami.
5. Zaznacz pole wyboru, aby potwierdzić, że akceptujesz **Warunki korzystania z serwisu**.
6. Kliknij **Rozpocznij**. Jeśli masz już konto, kliknij **Login** na dole, aby wrócić do strony logowania. **Odwiedź stronę internetową** otwiera witrynę DocBits z informacjami o produkcie.

Użyj ikony oka obok pola hasła, aby pokazać lub ukryć wpisane znaki.

### Zasady haseł

Twoje hasło musi:

* mieć długość od **8 do 20 znaków**,
* zawierać co najmniej jedną **wielką** i jedną **małą** literę,
* zawierać co najmniej jedną **cyfrę**,
* zawierać co najmniej jeden **znak specjalny** (`!@#$%^&*()_+=\[{]\};:,.<>?/\|~-`).

Dozwolone są tylko litery, cyfry i te znaki specjalne.

### Rejestracja przez Google lub Microsoft

Zamiast hasła możesz kliknąć przycisk **Google** lub **Microsoft** pod napisem **LUB ZAREJESTRUJ SIĘ ZA POMOCĄ**. DocBits utworzy Twoje konto za pośrednictwem Twojego dostawcy tożsamości, a później logujesz się w ten sam sposób.

### Potwierdź swój adres e-mail

Po wysłaniu formularza DocBits wyświetla stronę potwierdzenia i wysyła **e-mail weryfikacyjny** na podany adres. Otwórz e-mail i kliknij znajdujący się w nim link — prowadzi on do strony potwierdzenia, która weryfikuje Twój adres. Jeśli e-mail nie dotrze, strona potwierdzenia oferuje opcję **ponownego wysłania**. Gdy adres zostanie zweryfikowany, kliknij **Sign in** i zaloguj się swoim adresem e-mail oraz hasłem.

## Zapomniane hasło

Jeśli zapomniałeś hasła:

1. Na ekranie logowania kliknij **Zapomniałeś hasła?**.
2.  Na stronie **Zapomniałem hasła** wpisz swój adres **E-mail** i kliknij **Zresetuj hasło**. Jeśli wyświetlany jest widget reCAPTCHA, najpierw go wypełnij.

    <figure><img src="../../.gitbook/assets/dbdc745-getting-access-forgot-password-form-pl-20261011.png" alt="Strona Zapomniałem hasła z polem adresu e-mail"><figcaption><p>Strona Zapomniałem hasła. Podaj e-mail swojego konta, a DocBits wyśle Ci link do resetowania hasła.</p></figcaption></figure>

    Jeśli nie chcesz resetować hasła, kliknij **Powrót do logowania**, aby wrócić do ekranu logowania.
3. DocBits wysyła Ci e-mailem **link do resetowania hasła**. Otwórz e-mail i kliknij link — otworzy się strona resetowania hasła.
4. Wpisz swoje **nowe hasło dwa razy**. Obowiązują te same zasady haseł co podczas [rejestracji](getting-access-and-signing-in.md#zasady-haseł), a lista kontrolna pokazuje, które zasady są spełnione.
5. Kliknij **Zresetuj hasło**. DocBits potwierdza zmianę i przenosi Cię z powrotem na ekran logowania, gdzie możesz zalogować się nowym hasłem.

{% hint style="info" %}
Linki do resetowania hasła wygasają po krótkim czasie. Jeśli link już nie działa, powtórz powyższe kroki, aby poprosić o nowy.
{% endhint %}

## Pierwsze hasło dla kont utworzonych przez administratora

Gdy administrator doda Cię jako użytkownika (zobacz [Użytkownicy](../../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/)), otrzymasz e-mail z danymi do logowania oraz linkiem do ustawienia **pierwszego hasła**. Link otwiera stronę **Ustaw hasło**:

<figure><img src="../../.gitbook/assets/dbdc745-getting-access-set-password-form-pl-20261011.png" alt="Strona Ustaw hasło z komunikatem powitalnym"><figcaption><p>Strona Ustaw hasło, wyświetlana po utworzeniu Twojego konta przez administratora.</p></figcaption></figure>

1. Kliknij link w e-mailu z zaproszeniem. Strona wita Cię komunikatem „Witamy w DocBits! Twoje konto zostało utworzone. Aby rozpocząć, ustaw hasło."
2. Wpisz swoje hasło dwa razy — obowiązują te same [zasady haseł](getting-access-and-signing-in.md#zasady-haseł).
3. Kliknij **Ustaw hasło**. Następnie możesz zalogować się swoim adresem e-mail i tym hasłem.

Ikony oka pokazują lub ukrywają wpisane znaki. Jeśli wyjdziesz przed ustawieniem hasła, **Przejdź do logowania** wraca do ekranu logowania.

Link jest powiązany z Twoim kontem i działa tylko raz. Jeśli wygaśnie, zanim go użyjesz, poproś administratora o ponowne wysłanie zaproszenia albo użyj opcji **Zapomniałeś hasła?** ze swoim adresem e-mail.
