---
description: Korzystanie z DocBits przy użyciu logowania Microsoft bez (oddzielnego) hasła
---

# Azure SSO

### Utwórz SAML SSO w Azure AD

Wykonaj następujące kroki, aby dodać SAML SSO w Azure AD:

*   W Azure przejdź do konsoli \`Azure Active Directory\`

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* W panelu po lewej stronie kliknij \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Kliknij \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Kliknij \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Wprowadź nazwę swojej aplikacji. Pozostaw pozostałe ustawienia domyślne.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Kliknij \`Create\`

### Przypisz użytkowników do konfiguracji SSO

Następnie przypisz użytkowników lub grupy do konfiguracji SSO.

**Ważne**: Powinieneś mieć już utworzonych użytkowników i grupy w Azure AD. Jeśli nie masz żadnych użytkowników ani grup, utwórz je teraz, zanim przejdziesz dalej.

* W sekcji \`Getting Started\` kliknij \`Assign Users and Groups\`.
* Kliknij \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Wybierz użytkowników i grupy, które chcesz przypisać do tej konfiguracji SSO. Ci użytkownicy będą mogli uwierzytelniać się w DocBits (za pomocą SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Kliknij \`Select\`
* Gdy będziesz zadowolony ze swojego wyboru, kliknij \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Przejdź do listy widoku \`Groups\` i odszukaj przypisane grupy.

### Skonfiguruj SSO w Azure

Następnie musisz dokończyć konfigurowanie logowania jednokrotnego w Azure.\\

* W panelu po lewej stronie kliknij \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Kliknij \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Kliknij \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Prześlij plik **metadata.xml** DocBits, który znajdziesz w menu Ustawienia **Integracja** w sekcji **SSO Service Provider Settings** swojego konta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Edytuj \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Sprawdź, czy pola \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` oraz \`Logout URL\` zostały poprawnie wypełnione.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Pobierz nowo wygenerowany plik **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Prześlij plik FederationMetadata.xml do sekcji **Identity Service Provider Settings** swojego konta DocBits, którą znajdziesz w menu Ustawienia **Integracja**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
