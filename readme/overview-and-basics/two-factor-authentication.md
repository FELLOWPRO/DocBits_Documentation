# Uwierzytelnianie dwuskładnikowe (2FA)

## Przegląd

Uwierzytelnianie dwuskładnikowe (2FA) dodaje drugi krok do logowania. Po podaniu hasła DocBits prosi o drugi składnik, który masz tylko Ty — kod z aplikacji uwierzytelniającej, kod wysłany e-mailem lub klucz dostępu (Touch ID, Windows Hello, YubiKey, 1Password). Nawet jeśli ktoś pozna Twoje hasło, nie zaloguje się bez tego drugiego składnika.

2FA jest **opcjonalne dla każdego użytkownika** i może być **wymagane przez administratora Twojej organizacji**. Logowania przez pojedyncze logowanie (SSO) (Google, Microsoft, SAML) są wyłączone — Twój dostawca tożsamości egzekwuje już własne MFA.

Możesz zarejestrować więcej niż jedną metodę. DocBits obsługuje następujące metody:

* **Aplikacja uwierzytelniająca (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy itp.
* **Kod e-mail** — 6-cyfrowy kod wysyłany na adres e-mail Twojego konta.
* **Klucz dostępu (WebAuthn/FIDO2)** — Touch ID, Windows Hello, klucz sprzętowy (YubiKey) lub menedżer haseł.

Po włączeniu pierwszego składnika DocBits przekazuje Ci również **dziesięć kodów zapasowych**, których możesz użyć, jeśli kiedykolwiek stracisz dostęp do swojej metody.

## Gdzie to znaleźć

Otwórz **ustawienia profilu / konta** (menu konta w prawym górnym rogu → **Edytuj profil**) i wybierz **Uwierzytelnianie dwuskładnikowe**. Okno dialogowe 2FA pokazuje bieżący stan i metody, które możesz dodać.

<figure><img src="../.gitbook/assets/mfa-2fa-dialog.png" alt="The Two-factor authentication dialog"><figcaption><p>Okno dialogowe uwierzytelniania dwuskładnikowego. Stąd możesz włączyć aplikację uwierzytelniającą, weryfikację e-mail, dodać klucz dostępu lub otworzyć <strong>Zarządzaj</strong>.</p></figcaption></figure>

## Konfiguracja aplikacji uwierzytelniającej (TOTP)

1. W oknie dialogowym 2FA kliknij **Włącz 2FA**.
2. Zeskanuj kod QR za pomocą aplikacji uwierzytelniającej (Google Authenticator, 1Password, Authy, …). Jeśli nie możesz zeskanować, użyj **klucza ręcznego** wyświetlonego pod kodem QR.
3. Wprowadź 6-cyfrowy kod wyświetlany przez aplikację i potwierdź.
4. DocBits włącza 2FA i wyświetla Twoje **kody zapasowe** (patrz poniżej).

<figure><img src="../.gitbook/assets/mfa-totp-setup.png" alt="The authenticator-app setup screen with QR code"><figcaption><p>Zeskanuj kod QR za pomocą aplikacji uwierzytelniającej lub wprowadź klucz ręczny. Następnie potwierdź 6-cyfrowym kodem wyświetlanym przez aplikację.</p></figcaption></figure>

## Konfiguracja weryfikacji e-mail

1. W oknie dialogowym 2FA kliknij **Włącz weryfikację e-mail**.
2. DocBits wysyła 6-cyfrowy kod na adres e-mail Twojego konta.
3. Wprowadź kod, aby potwierdzić. Weryfikacja e-mail jest teraz włączona.

## Dodawanie klucza dostępu

1. W oknie dialogowym 2FA kliknij **Dodaj klucz dostępu**.
2. Przeglądarka lub urządzenie poprosi o potwierdzenie za pomocą Touch ID, Windows Hello, klucza sprzętowego lub menedżera haseł.
3. Klucz dostępu zostaje zapisany. Możesz dodać kilka kluczy dostępu, a później zmieniać ich nazwy lub je usuwać.

## Kody zapasowe

Po włączeniu **pierwszego** składnika DocBits wyświetla **dziesięć kodów zapasowych** — **jednorazowo**. Każdy kod działa tylko raz i umożliwia zalogowanie się, jeśli stracisz aplikację uwierzytelniającą lub telefon.

* Zapisz je w bezpiecznym miejscu (menedżer haseł jest idealny).
* W dowolnym momencie możesz wygenerować nowy zestaw za pomocą **Wygeneruj ponownie kody zapasowe** (unieważnia to stary zestaw).

<figure><img src="../.gitbook/assets/mfa-backup-codes.png" alt="The backup codes screen"><figcaption><p>Twoje dziesięć kodów zapasowych, wyświetlanych jednorazowo. Każdy działa tylko raz — przechowuj je w bezpiecznym miejscu.</p></figcaption></figure>

{% hint style="warning" %}
Kody zapasowe są wyświetlane tylko w momencie ich wygenerowania. DocBits nie może wyświetlić ich ponownie — zapisz je natychmiast.
{% endhint %}

## Logowanie za pomocą 2FA

1. Wprowadź swój adres e-mail i hasło jak zwykle.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>Ekran logowania. Możesz też zalogować się bez hasła za pomocą <strong>Zaloguj się kluczem dostępu</strong>.</p></figcaption></figure>
2. DocBits prosi o drugi składnik. Wybierz swoją metodę:
   * **Aplikacja uwierzytelniająca** — wpisz bieżący 6-cyfrowy kod z aplikacji.
   * **E-mail** — kliknij **Wyślij mi kod e-mailem**, aby otrzymać kod e-mailem, a następnie go wpisz.
   * **Klucz dostępu** — kliknij **Użyj klucza dostępu** i potwierdź za pomocą Touch ID / Windows Hello / swojego klucza.
   * **Kod zapasowy** — jeśli nie możesz użyć swojej zwykłej metody.

    <figure><img src="../.gitbook/assets/mfa-challenge.png" alt="The second-factor challenge screen"><figcaption><p>Po podaniu hasła DocBits prosi o drugi składnik. Zmień metodę za pomocą <strong>Użyj klucza dostępu</strong> lub <strong>Wyślij mi kod e-mailem</strong> i opcjonalnie zaufaj urządzeniu na 30 dni.</p></figcaption></figure>
3. Po pomyślnym potwierdzeniu jesteś zalogowany.

### Jak wygląda kod e-mail

Jeśli wybierzesz **E-mail**, DocBits wyśle wiadomość z 6-cyfrowym kodem, który wygasa po 10 minutach:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>Wiadomość e-mail z kodem weryfikacyjnym. Kod wygasa po 10 minutach i może zostać użyty raz.</p></figcaption></figure>

## Zaufaj temu urządzeniu

Na ekranie drugiego składnika możesz zaznaczyć **Zapamiętaj to urządzenie**. DocBits pominie wtedy krok 2FA na tym urządzeniu przez **30 dni**. Zaufanie jest automatycznie usuwane po zmianie hasła, a Ty możesz je odwołać samodzielnie w dowolnym momencie (patrz poniżej).

## Zarządzanie kluczami dostępu i zaufanymi urządzeniami

Otwórz okno dialogowe 2FA i kliknij **Zarządzaj**, aby przejrzeć zarejestrowane elementy.

* **Klucze dostępu** — zmień nazwę klucza dostępu (kliknij jego nazwę) lub usuń go. Usunięcie ostatniego pozostałego składnika wyłącza 2FA.
* **Zaufane urządzenia** — odwołaj pojedyncze urządzenie lub użyj **Odwołaj wszystkie urządzenia**, aby wymusić ponowne pytanie o 2FA wszędzie.

<figure><img src="../.gitbook/assets/mfa-passkeys-list.png" alt="Managing enrolled passkeys and trusted devices"><figcaption><p>Widok Zarządzaj wyświetla zarejestrowane klucze dostępu i zaufane urządzenia, w którym możesz zmieniać ich nazwy lub je usuwać.</p></figcaption></figure>

## Wyłączanie 2FA

W oknie dialogowym 2FA kliknij **Wyłącz 2FA** i potwierdź bieżącym kodem z aplikacji uwierzytelniającej lub kodem zapasowym. Wyłączenie 2FA usuwa również Twoje kody zapasowe i odwołuje zaufane urządzenia.

{% hint style="info" %}
Jeśli Twoja organizacja **wymaga** MFA, nie możesz zalogować się hasłem, dopóki nie skonfigurujesz co najmniej jednego składnika. Zapytaj administratora, jeśli nie masz pewności, czy MFA jest obowiązkowe w Twojej organizacji.
{% endhint %}

## Logowanie bez hasła (opcjonalne)

Gdy masz już klucz dostępu, możesz zalogować się **bez wpisywania hasła** za pomocą **Zaloguj się kluczem dostępu** na ekranie logowania. Twoje hasło nadal działa jako opcja awaryjna. Logowanie bez hasła wymaga, aby klucz dostępu Cię zweryfikował (Touch ID / Windows Hello / PIN), dzięki czemu jest szybsze i odporne na phishing.
