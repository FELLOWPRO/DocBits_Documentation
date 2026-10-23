---
description: Korzystanie z DocBits przy użyciu logowania Microsoft bez (oddzielnego) hasła
---

# SSO w Azure

### Utwórz SAML SSO w Azure AD

Wykonaj następujące kroki, aby dodać SAML SSO w Azure AD:

*   W Azure przejdź do konsoli \`Azure Active Directory\`

    ![Okienko nawigacji portalu Azure z ulubionymi, takimi jak Resource groups, All resources i Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* W panelu po lewej stronie kliknij \`Enterprise applications\`

![Lewy panel usługi Azure Active Directory z wpisami sekcji Manage: Users, Groups, Roles and administrators i Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Kliknij \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Okno dialogowe Add Assignment w Azure z wybranymi 2 users selected, 2 groups selected i opcją Select Role ustawioną na User"><figcaption></figcaption></figure>

* Kliknij \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Menu przeglądu aplikacji przedsiębiorstwa w Azure z wpisami Manage: Properties, Owners, Users and groups, Single sign-on i Provisioning"><figcaption></figcaption></figure></div>

* Wprowadź nazwę swojej aplikacji. Pozostaw pozostałe ustawienia domyślne.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Okno dialogowe Create your own application w Azure z nazwą aplikacji MyApplication i opcjami integracji aplikacji"><figcaption></figcaption></figure>

* Kliknij \`Create\`

### Przypisz użytkowników do konfiguracji SSO

Następnie przypisz użytkowników lub grupy do konfiguracji SSO.

**Ważne**: Powinieneś mieć już utworzonych użytkowników i grupy w Azure AD. Jeśli nie masz żadnych użytkowników ani grup, utwórz je teraz, zanim przejdziesz dalej.

* W sekcji \`Getting Started\` kliknij \`Assign Users and Groups\`.
* Kliknij \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Strona Users and groups dla MyApplication w Azure z przyciskami Add user, Edit i Remove oraz pustą listą Display Name" width="563"><figcaption></figcaption></figure>

* Wybierz użytkowników i grupy, które chcesz przypisać do tej konfiguracji SSO. Ci użytkownicy będą mogli uwierzytelniać się w DocBits (za pomocą SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panel wyboru użytkowników i grup w Azure z listą użytkowników Daniel oraz panelem Selected items"><figcaption></figcaption></figure>

* Kliknij \`Select\`
* Gdy będziesz zadowolony ze swojego wyboru, kliknij \`Assign\`

![Okno dialogowe Add Assignment w Azure z wybranymi 2 users selected, 2 groups selected i opcją Select Role ustawioną na User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Okno dialogowe Create your own application w Azure z nazwą aplikacji MyApplication i opcjami integracji aplikacji"><figcaption></figcaption></figure></div>

* Przejdź do listy widoku \`Groups\` i odszukaj przypisane grupy.

### Skonfiguruj SSO w Azure

Następnie musisz dokończyć konfigurowanie logowania jednokrotnego w Azure.\\

* W panelu po lewej stronie kliknij \`Single sign-on\`

![Menu przeglądu aplikacji przedsiębiorstwa w Azure z wpisami Manage: Properties, Owners, Users and groups, Single sign-on i Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Kliknij \`SAML\`

![Karta opcji SAML w Azure opisująca bogate i bezpieczne uwierzytelnianie za pomocą protokołu Security Assertion Markup Language](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Kliknij \`Upload metadata file\`

![Panel SAML-based Sign-on w Azure z opcjami Upload metadata file i Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Prześlij plik **metadata.xml** DocBits, który znajdziesz w menu Ustawienia **Integracja** w sekcji **SSO Service Provider Settings** swojego konta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Strona SSO Service Provider Settings z identyfikatorem Tenant ID, identyfikatorem Entity ID oraz polami SSO Url, SLO Url i Metadata Url"><figcaption></figcaption></figure>

* Edytuj \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Ekran konfiguracji logowania jednokrotnego SAML z sekcją Basic SAML Configuration oraz polami Identifier, Reply URL, Sign on URL i Logout Url"><figcaption></figcaption></figure>

* Sprawdź, czy pola \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` oraz \`Logout URL\` zostały poprawnie wypełnione.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Edytor Basic SAML Configuration w Azure z polami Identifier, Reply URL, Sign on URL, Relay State i Logout Url oraz przyciskiem Save"><figcaption></figcaption></figure>

* Pobierz nowo wygenerowany plik **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sekcja SAML Signing Certificate w Azure z odciskiem palca, datą wygaśnięcia oraz linkami do pobrania Certificate (Raw) i Federation Metadata XML"><figcaption></figcaption></figure>

* Prześlij plik FederationMetadata.xml do sekcji **Identity Service Provider Settings** swojego konta DocBits, którą znajdziesz w menu Ustawienia **Integracja**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Okno dialogowe Identity Service Provider Settings w DocBits z identyfikatorem Tenant ID FELLOWPRO_PRD i przyciskiem Upload file"><figcaption></figcaption></figure>
