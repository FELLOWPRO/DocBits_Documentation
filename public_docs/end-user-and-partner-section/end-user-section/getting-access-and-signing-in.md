# Uzyskiwanie dostępu i logowanie

Na tej stronie opisano, jak uzyskać konto DocBits i jak się zalogować:

* [Logowanie na istniejące konto](#logowanie-na-istniejace-konto) — pola na ekranie logowania i wybór regionu.
* [Rejestracja](#rejestracja) — utwórz własne konto DocBits.
* [Zapomniane hasło](#zapomniane-haslo) — zresetuj hasło za pomocą linku do resetowania.
* [Pierwsze hasło dla kont utworzonych przez administratora](#pierwsze-haslo-dla-kont-utworzonych-przez-administratora) — ustaw pierwsze hasło do konta, które administrator utworzył dla Ciebie.

Uwierzytelnianie dwuskładnikowe, passkeys i drugi krok logowania są opisane na stronie [Uwierzytelnianie dwuskładnikowe (2FA)](../../security/two-factor-authentication.md). Jeśli potrzebujesz innego języka wyświetlania, użyj menu języka w prawym górnym rogu tych formularzy.

## Logowanie na istniejące konto

Otwórz adres internetowy DocBits podany Twojej organizacji — na przykład `https://app.docbits.com` — i zaloguj się na ekranie logowania.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/getting-access-login-en-20261107.png" alt="Angielski ekran logowania DocBits z pustymi polami E-Mail i Password, Remember me, selektorem Auth region ustawionym na Europe, Log In, Sign in with a passkey, Sign in with Google i Sign in with Microsoft"><figcaption><p>Ekran logowania: e-mail i hasło, Remember me, selektor Auth region, Log In, passkey oraz przyciski logowania Google i Microsoft.</p></figcaption></figure>

<!-- Shared English screenshot, do not re-shoot: public_docs/.gitbook/assets/getting-access-login-en-20261107.png -->

1. **E-Mail** — adres, na który utworzono Twoje konto DocBits.
2. **Password** — Twoje hasło DocBits. Ikona oka w polu pokazuje lub ukrywa wpisane znaki.
3. **Remember me** — wypełnia Twój adres e-mail przy następnym otwarciu ekranu logowania.
4. **Auth region** — DocBits działa w dwóch regionach, **Europe** i **United States**, a każdy ma własną usługę logowania. Selektor jest widoczny w instalacjach, które używają obu (production, dev i sandbox). DocBits wstępnie wybiera Twój ostatni wybór, w przeciwnym razie region zgodny ze strefą czasową komputera, a w przeciwnym razie Europe. Jeśli Twoje konto utworzono w drugim regionie, wybierz go tutaj przed kliknięciem **Log In**.
5. Kliknij **Log In**.

Pod polami hasła:

* **Sign in with a passkey** — pojawia się, gdy przeglądarka obsługuje passkeys. Loguje Cię bez hasła. Zobacz [Logowanie bez hasła](../../security/two-factor-authentication.md).
* **Sign in with Google** i **Sign in with Microsoft** — dla organizacji korzystających z logowania jednokrotnego u tych dostawców. Logowanie obsługuje dostawca tożsamości, więc hasło DocBits i wymóg dwuskładnikowy DocBits nie mają zastosowania.
* **Forgot password?** — zobacz [Zapomniane hasło](#zapomniane-haslo) poniżej.
* **Register** — zobacz [Rejestracja](#rejestracja) poniżej.

{% hint style="info" %}
Wybierz **Auth region**, którego używa Twoja organizacja, przed kliknięciem **Log In**: wybór decyduje, która usługa logowania regionu otrzyma Twoje dane logowania. Jeśli nie masz pewności, zapytaj administratora.
{% endhint %}

## Rejestracja

Konto DocBits możesz utworzyć samodzielnie na stronie rejestracji. Otwórz ją za pomocą linku **Register** na ekranie logowania lub przejdź do adresu `https://app.docbits.com/register` (użyj adresu internetowego przekazanego Twojej organizacji).

<figure><img src="../../.gitbook/assets/dbdc-8-register-native-pl-20261101.png" alt="Polski formularz rejestracji DocBits z pięcioma pustymi polami, niezaznaczoną reCAPTCHA, warunkami korzystania, Rozpocznij, Google, Microsoft i Login"><figcaption><p>Rejestracja: wypełnij Imię, Nazwisko, E-mail, Hasło i Potwierdź hasło. Rozwiąż reCAPTCHA, jeśli się pojawi, zaakceptuj Warunki korzystania z serwisu i wybierz Rozpocznij. Login prowadzi z powrotem do logowania.</p></figcaption></figure>

Wypełnij formularz:

1. **First name** i **Last name** — Twoje imię i nazwisko, tak jak mają być widoczne w DocBits.
2. **E-mail** — Twój służbowy adres e-mail. Jest to Twój identyfikator logowania.
3. **Password** i **Confirm password** — patrz zasady haseł poniżej. Lista kontrolna pod polem hasła pokazuje, które zasady Twoje hasło już spełnia.
4. Jeśli strona wyświetla widget **reCAPTCHA**, wypełnij go. Widget pojawia się tylko wtedy, gdy wdrożenie DocBits ma włączoną ochronę przed botami.
5. Zaznacz pole wyboru, aby potwierdzić, że akceptujesz **Terms and Conditions**.
6. Kliknij **Get Started**. Jeśli masz już konto, kliknij **Login** na dole, aby wrócić do strony logowania. **Visit website** otwiera witrynę DocBits z informacjami o produkcie.

Użyj ikony oka obok pola hasła, aby pokazać lub ukryć wpisane znaki.

### Zasady haseł

Twoje hasło musi:

* mieć długość od **8 do 20 znaków**,
* zawierać co najmniej jedną **wielką** i jedną **małą** literę,
* zawierać co najmniej jedną **cyfrę**,
* zawierać co najmniej jeden **znak specjalny** (`!@#$%^&*()_+=\[{]\};:,.<>?/\|~-`).

Dozwolone są tylko litery, cyfry i te znaki specjalne.

### Rejestracja przez Google lub Microsoft

Zamiast hasła możesz kliknąć przycisk **Google** lub **Microsoft** pod napisem **Or sign up with**. DocBits utworzy Twoje konto za pośrednictwem Twojego dostawcy tożsamości, a później logujesz się w ten sam sposób.

### Potwierdź swój adres e-mail

Po wysłaniu formularza DocBits wyświetla stronę potwierdzenia i wysyła **e-mail weryfikacyjny** na podany adres. Otwórz e-mail i kliknij znajdujący się w nim link — prowadzi on do strony potwierdzenia, która weryfikuje Twój adres. Jeśli e-mail nie dotrze, strona potwierdzenia oferuje opcję **ponownego wysłania**. Gdy adres zostanie zweryfikowany, przejdź do ekranu logowania i zaloguj się swoim adresem e-mail oraz hasłem.

## Zapomniane hasło

DocBits przechowuje hasła logowania jako jednokierunkowe skróty kryptograficzne z solą. Istniejącego hasła nie można odzyskać ze skrótu, dlatego ta procedura ustawia nowe hasło. Zobacz [Bezpieczne przechowywanie danych uwierzytelniających](../../security/secure-storage-of-credentials.md).

Jeśli zapomniałeś hasła:

1. Na ekranie logowania kliknij **Forgot password?**.
2. Na stronie **Forgot Password** wpisz swój adres **E-mail** i kliknij **Reset Password**. Jeśli wyświetlany jest widget reCAPTCHA, najpierw go wypełnij.

   <figure><img src="../../.gitbook/assets/dbdc-8-forget-password-native-pl-20261101.png" alt="Polski formularz Zapomniałem hasła z pustym polem E-mail, niezaznaczoną reCAPTCHA, Zresetuj hasło i Powrót do logowania"><figcaption><p>Wpisz E-mail i wybierz Zresetuj hasło, aby poprosić o link do resetowania, albo użyj Powrót do logowania. Rozwiąż reCAPTCHA, gdy się pojawi.</p></figcaption></figure>

   Jeśli nie chcesz resetować hasła, kliknij **Back to Login**, aby wrócić do ekranu logowania.

3. DocBits wysyła Ci e-mailem **link do resetowania hasła**. Otwórz e-mail i kliknij link — otworzy się strona resetowania hasła.
4. Wpisz swoje **nowe hasło dwa razy**. Obowiązują te same zasady haseł co podczas [rejestracji](#zasady-hasel), a lista kontrolna pokazuje, które zasady są spełnione.
5. Kliknij **Reset Password**. DocBits potwierdza zmianę i przenosi Cię z powrotem na ekran logowania, gdzie możesz zalogować się nowym hasłem.

{% hint style="info" %}
Linki do resetowania hasła wygasają po krótkim czasie. Jeśli link już nie działa, powtórz powyższe kroki, aby poprosić o nowy.
{% endhint %}

## Pierwsze hasło dla kont utworzonych przez administratora

Gdy administrator doda Cię jako użytkownika (zobacz [Użytkownicy](../../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md)), otrzymasz e-mail z danymi do logowania oraz linkiem do ustawienia **pierwszego hasła**. Link otwiera stronę **Set Password**:

<figure><img src="../../.gitbook/assets/dbdc-8-set-password-native-pl-20261101.png" alt="Polski formularz Ustaw hasło z powitaniem, pustymi polami Hasło i Potwierdź hasło, ikonami oka, Ustaw hasło i Przejdź do logowania"><figcaption><p>Pierwsze hasło do konta utworzonego przez administratora: wypełnij Hasło i Potwierdź hasło, a następnie wybierz Ustaw hasło. Przejdź do logowania prowadzi do ekranu logowania.</p></figcaption></figure>

1. Kliknij link w e-mailu z zaproszeniem. Strona wita Cię komunikatem „Witamy w DocBits! Twoje konto zostało utworzone. Aby rozpocząć, ustaw hasło."
2. Wpisz swoje hasło dwa razy — obowiązują te same [zasady haseł](#zasady-hasel).
3. Kliknij **Set Password**. Następnie możesz zalogować się swoim adresem e-mail i tym hasłem.

Ikony oka pokazują lub ukrywają wpisane znaki. Jeśli wyjdziesz przed ustawieniem hasła, **Go to Login** wraca do ekranu logowania.

Link jest powiązany z Twoim kontem i działa tylko raz. Jeśli wygaśnie, zanim go użyjesz, poproś administratora o ponowne wysłanie zaproszenia albo użyj opcji **Forgot password?** ze swoim adresem e-mail.
