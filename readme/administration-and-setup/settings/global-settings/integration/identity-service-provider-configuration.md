# Konfiguracja dostawcy tożsamości (Identity Service Provider)

Skonfigurowanie dostawcy tożsamości (IdP) pod kątem integracji z DocBits wymaga kilku konkretnych kroków. Oto przewodnik:

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Dostęp do interfejsu konfiguracji IdP**

* Zaloguj się do swojego dostawcy tożsamości (IdP) jako administrator.
* Przejdź do ustawień lub interfejsu konfiguracji przeznaczonego do zarządzania integracjami SAML.

**Wprowadzanie Tenant ID:**

* Znajdź sekcję umożliwiającą konfigurację nowych integracji SAML.
* Wprowadź identyfikator tenanta DocBits. Ten identyfikator wskazuje Twoje konto DocBits w IdP i umożliwia bezpieczną komunikację między obydwoma systemami.

**Importowanie wymaganych plików:**

* DocBits zazwyczaj wymaga pobrania metadanych lub dodania określonych szczegółów konfiguracji. Sprawdź w dokumentacji swojego IdP, jakie kroki są wymagane.
* Pobierz plik metadanych DocBits lub zaimportuj go w menu konfiguracji swojego IdP. Możesz też ręcznie wprowadzić wymagane szczegóły konfiguracji, zależnie od tego, co obsługuje Twój IdP.

**Konfiguracja ustawień integracji:**

* Upewnij się, że ustawienia integracji, takie jak SSO URL, Entity ID i certyfikat SAML, są poprawne.
* Sprawdź, czy adres URL Single Log-Out (SLO) oraz inne wymagane parametry są skonfigurowane prawidłowo. Mają one kluczowe znaczenie dla sprawnego uwierzytelniania i wylogowywania przez SAML.

**Weryfikacja konfiguracji:**

* Poświęć czas, aby upewnić się, że wszystkie wprowadzone informacje są poprawne i nie ma literówek ani błędów konfiguracji.
* Przeprowadź testy, aby upewnić się, że użytkownicy mogą pomyślnie logować się do DocBits przez SAML oraz że Single Log-Out działa prawidłowo.

**Względy bezpieczeństwa:**

* Upewnij się, że wszystkie przesyłane pliki i szczegóły konfiguracji są obsługiwane w sposób bezpieczny, aby uniknąć wycieków danych lub nieautoryzowanego dostępu.
* Chroń poufne informacje, takie jak certyfikaty SAML i dane uwierzytelniające, przed nieautoryzowanym dostępem i przechowuj je w bezpiecznym miejscu.
