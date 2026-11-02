---
description: Korzystanie z DocBits przy użyciu logowania Microsoft bez (oddzielnego) hasła
---

# SSO w Azure

### Utwórz SAML SSO w Azure AD

Wykonaj następujące kroki, aby dodać SAML SSO w Azure AD:

*   W Azure przejdź do konsoli \`Azure Active Directory\`

    ![Strona główna portalu Azure z Azure Active Directory w ulubionych lewej nawigacji](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* W panelu po lewej stronie kliknij \`Enterprise applications\`

![Lewa nawigacja Azure Active Directory z grupą Zarządzaj i pozycją Aplikacje dla przedsiębiorstw](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Kliknij \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Strona Aplikacje dla przedsiębiorstw w Azure Active Directory z listą Wszystkie aplikacje i przyciskiem Nowa aplikacja"><figcaption></figcaption></figure>

* Kliknij \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Okno Przeglądaj galerię Azure AD z przyciskami Utwórz własną aplikację i Poproś o nową aplikację z galerii oraz polem wyszukiwania Szukaj aplikacji"><figcaption></figcaption></figure></div>

* Wprowadź nazwę swojej aplikacji. Pozostaw pozostałe ustawienia domyślne.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Okno Utwórz własną aplikację z nazwą MyApplication i wybraną opcją Zintegruj dowolną inną aplikację, której nie ma w galerii"><figcaption></figcaption></figure>

* Kliknij \`Create\`

### Przypisz użytkowników do konfiguracji SSO

Następnie przypisz użytkowników lub grupy do konfiguracji SSO.

**Ważne**: Powinieneś mieć już utworzonych użytkowników i grupy w Azure AD. Jeśli nie masz żadnych użytkowników ani grup, utwórz je teraz, zanim przejdziesz dalej.

* W sekcji \`Getting Started\` kliknij \`Assign Users and Groups\`.
* Kliknij \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Strona Użytkownicy i grupy aplikacji MyApplication z przyciskami Dodaj użytkownika, Edytuj, Usuń i Aktualizuj oraz komunikatem Nie znaleziono przypisań aplikacji" width="563"><figcaption></figcaption></figure>

* Wybierz użytkowników i grupy, które chcesz przypisać do tej konfiguracji SSO. Ci użytkownicy będą mogli uwierzytelniać się w DocBits (za pomocą SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panel wyboru użytkowników z listą kilku użytkowników i sekcją Wybrane"><figcaption></figcaption></figure>

* Kliknij \`Select\`
* Gdy będziesz zadowolony ze swojego wyboru, kliknij \`Assign\`

![Okno Dodaj przypisanie dzierżawy chimdustries z komunikatem Wybrano 2 użytkowników i 2 grupy](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Przycisk Przypisz wyróżniony zieloną ramką w oknie przypisywania Azure Active Directory"><figcaption></figcaption></figure></div>

* Przejdź do listy widoku \`Groups\` i odszukaj przypisane grupy.

### Skonfiguruj SSO w Azure

Następnie musisz dokończyć konfigurowanie logowania jednokrotnego w Azure.\\

* W panelu po lewej stronie kliknij \`Single sign-on\`

![Lewa nawigacja aplikacji dla przedsiębiorstw MyApplication z pozycją Logowanie jednokrotne](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Kliknij \`SAML\`

![Strona Logowanie jednokrotne z kaflem SAML i tekstem Bezpieczne i niezawodne uwierzytelnianie aplikacji za pomocą protokołu SAML](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Kliknij \`Upload metadata file\`

![Strona Logowanie oparte na SAML z linkami Prześlij plik metadanych i Skonfiguruj logowanie jednokrotne](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Prześlij plik **metadata.xml** DocBits, który znajdziesz w menu Ustawienia **Integracja** w sekcji **SSO Service Provider Settings** swojego konta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Ustawienia dostawcy usług SSO w DocBits z Entity ID, adresem SLO URI i SSO URI oraz przyciskami Pobierz certyfikat i Pobierz metadane"><figcaption></figcaption></figure>

* Edytuj \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Strona Skonfiguruj logowanie jednokrotne z SAML z sekcją Podstawowa konfiguracja SAML i polami Identyfikator Entity ID, Adres URL odpowiedzi, Adres URL logowania, Stan przekaźnika i Adres URL wylogowania"><figcaption></figcaption></figure>

* Sprawdź, czy pola \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` oraz \`Logout URL\` zostały poprawnie wypełnione.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Podstawowa konfiguracja SAML w Azure z tekstami opisowymi, Identyfikatorem Entity ID ustawionym na adres URL metadanych SAML dzierżawy i Adresem URL odpowiedzi jako Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Pobierz nowo wygenerowany plik **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sekcja Certyfikat podpisywania SAML ze stanem Aktywny, odciskiem palca, datą wygaśnięcia, adresem e-mail powiadomień i linkami pobierania Certyfikat nieprzetworzony i XML metadanych federacji"><figcaption></figcaption></figure>

* Prześlij plik FederationMetadata.xml do sekcji **Identity Service Provider Settings** swojego konta DocBits, którą znajdziesz w menu Ustawienia **Integracja**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Ustawienia dostawcy usług tożsamości w DocBits z identyfikatorem dzierżawy, przyciskami Prześlij plik i Importuj oraz pozycją istniejącego pliku"><figcaption></figcaption></figure>
