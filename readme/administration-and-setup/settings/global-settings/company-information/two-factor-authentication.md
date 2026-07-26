# Uwierzytelnianie dwuskładnikowe (administrator)

## Przegląd

Jako administrator organizacji możesz **wymagać od każdego członka używania uwierzytelniania dwuskładnikowego (2FA)** podczas logowania hasłem. Gdy wymóg jest włączony, członek, który nie skonfigurował jeszcze drugiego składnika, zostaje przeprowadzony przez rejestrację, zanim będzie mógł dokończyć logowanie.

Logowania przez pojedyncze logowanie (SSO) — Google, Microsoft, SAML — są **wyłączone**: ich dostawca tożsamości egzekwuje już własne MFA, więc wymóg dotyczy tylko logowań hasłem.

To ustawienie znajduje się w **Ustawienia → Ustawienia globalne → Informacje o firmie → Uwierzytelnianie dwuskładnikowe** i jest dostępne tylko dla administratorów organizacji.

## Wymaganie MFA w Twojej organizacji

1. Przejdź do **Ustawienia → Ustawienia globalne → Informacje o firmie**.
2. Otwórz sekcję **Uwierzytelnianie dwuskładnikowe**.
3. Włącz **Wymagaj uwierzytelniania dwuskładnikowego od wszystkich członków** i kliknij **Zapisz**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Włącz wymóg dla wszystkich członków i monitoruj poziom wdrożenia poniżej.</p></figcaption></figure>

Po zapisaniu zmiana zaczyna obowiązywać w ciągu minuty. Od tego momentu:

* Członek **posiadający** drugi składnik jest o niego proszony po podaniu hasła, jak zwykle.
* Członek **nieposiadający** drugiego składnika musi go zarejestrować, zanim otrzyma sesję.
* Logowania przez SSO / media społecznościowe pozostają bez zmian.

{% hint style="warning" %}
Włączenie tej opcji blokuje logowania hasłem członkom, którzy nie mają drugiego składnika, dopóki nie zakończą rejestracji. Poinformuj o zmianie swój zespół i rozważ włączenie jej poza godzinami szczytu.
{% endhint %}

## Raport wdrożenia MFA

Pod przełącznikiem panel **Wdrożenie MFA** pokazuje, jak szeroko 2FA jest używane w Twojej organizacji, zanim je wymusisz:

* ogólny **procent wdrożenia** i pasek postępu,
* ilu Twoich członków ma włączone 2FA (np. *0 z 74 członków*),
* podział według składników — **Aplikacja uwierzytelniająca**, **E-mail** i **Klucz dostępu**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>Raport wdrożenia MFA: ogólny procent, zarejestrowani członkowie i podział według składników.</p></figcaption></figure>

Użyj go do oceny gotowości: najpierw zwiększ poziom wdrożenia, a następnie włącz wymóg, gdy mniej członków zostanie zablokowanych na etapie rejestracji.

## Co widzą członkowie

Członek, który musi się zarejestrować, zostaje przekierowany do konfiguracji 2FA przy następnym logowaniu i wybiera metodę (aplikacja uwierzytelniająca, kod e-mail lub klucz dostępu). Kroki dla użytkownika końcowego są opisane w [Uwierzytelnianie dwuskładnikowe (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Powiązane mechanizmy zabezpieczeń

Wymóg MFA obejmujący całą organizację uzupełnia wbudowane zabezpieczenia, które zawsze obowiązują, gdy użytkownik ma włączone 2FA: jednorazowe kody logowania, ochronę przed powtórzeniem TOTP, limity prób na żądanie i na konto (konto zostaje tymczasowo zablokowane po zbyt wielu nieudanych próbach) oraz automatyczne odwoływanie zaufanych urządzeń po zmianie hasła przez członka.
