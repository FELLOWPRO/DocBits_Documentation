# Klucz API

<figure><img src="https://lh7-us.googleusercontent.com/ulCymk1gu-de14qTaFfJwTEmAUp7DY000A40P3nTgRIb7pYXolCbh_GPJvRib5haIH75dPFewY5tJQ0xNbGP3wdSOgCxu7gdVBwlvxkHFcP_3HM3R15zuuBOZM2jEdFxlp2CpV1VDfktmLFSSw4BuLs" alt=""><figcaption></figcaption></figure>

### Klucz API

* **Klucz:** To unikalny identyfikator używany przez aplikacje zewnętrzne w celu uzyskania dostępu do API DocBits. Ma kluczowe znaczenie dla uwierzytelniania żądań kierowanych do DocBits z innego oprogramowania.
* Można tutaj wykonywać takie czynności jak wyświetlanie, ponowne generowanie lub kopiowanie klucza API, w zależności od konkretnych potrzeb i protokołów bezpieczeństwa.

### Ustawienia dostawcy usług SSO (logowanie jednokrotne)

* **Entity ID:** To identyfikator DocBits jako dostawcy usług w konfiguracji SSO. Jednoznacznie identyfikuje on DocBits w ramach struktury SSO.
* **SLO (Single Logout) URL:** Adres URL, na który wysyłane są sesje SSO w celu jednoczesnego wylogowania ze wszystkich aplikacji połączonych za pośrednictwem SSO.
* **SSO URL: Adres URL** używany do zainicjowania procesu logowania jednokrotnego.
* Dostępne są czynności takie jak „Pobierz certyfikat” oraz „Pobierz metadane” służące do uzyskania niezbędnych certyfikatów bezpieczeństwa oraz informacji o metadanych wykorzystywanych podczas konfigurowania i utrzymywania integracji SSO.

{% hint style="info" %}
Zobacz Konfiguracja SSO
{% endhint %}

### Ustawienia dostawcy usług tożsamości

* Tenant ID: Może być używany, gdy DocBits integruje się z usługami chmurowymi wymagającymi identyfikatora dzierżawcy do zarządzania danymi oraz konfiguracjami dostępu właściwymi dla firmy korzystającej z DocBits.
* Prześlij plik: Umożliwia administratorowi przesłanie plików konfiguracyjnych lub innych niezbędnych plików ułatwiających integrację z dostawcą tożsamości.
* Konfiguruj: Przycisk służący do zastosowania lub aktualizacji ustawień po wprowadzeniu zmian lub przesłaniu nowych konfiguracji.
