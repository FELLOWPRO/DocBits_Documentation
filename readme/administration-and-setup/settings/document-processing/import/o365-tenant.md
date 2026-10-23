# O365 Tenant

## Zarejestruj aplikację w Azure AD

<mark style="color:red;">**Uwaga**</mark>: Uprawnienia mogą wymagać autoryzacji od administratora.

1. Zaloguj się do [Portalu Azure](https://portal.azure.com/) używając swoich danych uwierzytelniających.
2. Z usług Azure znajdź i otwórz Azure Active Directory (znany również jako Azure AD).

![Strona portalu Azure z wpisem Azure Active Directory i paskiem wyszukiwania usług](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. W sekcji **Manage** wybierz **App registrations**.

![Strona przeglądu Azure Active Directory z otwartym menu Manage po lewej stronie i wyróżnioną pozycją App registrations](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Na ekranie App registrations kliknij **+ New registration**.

![Ekran App registrations w Azure z przyciskiem New registration na pasku narzędzi i listą zarejestrowanych aplikacji](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Wyświetli się ekran **Register an application**. Wprowadź nazwę wyświetlaną aplikacji skierowaną do użytkownika w polu **Name**.

![Ekran Register an application w portalu Azure z pustym polem Name dla nowej aplikacji](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Wybierz jeden z następujących typów kont w zależności od swoich potrzeb:

* **Konta w dowolnym katalogu organizacyjnym (dowolny katalog Azure AD Multitenant) i osobiste konta Microsoft (np. Skype, Xbox)**
* **Konta w dowolnym katalogu organizacyjnym (dowolny katalog AD platformy Azure dla wielu dzierżawców)**

![Ekran Register an application z opcjami typu obsługiwanych kont dla katalogów organizacyjnych i osobistych kont Microsoft](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Pozostaw opcję **Redirect URI (optional)** bez zmian.

![Ekran Register an application z sekcją Redirect URI (optional) pozostawioną bez zmian na dole](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Kliknij **Register**, aby zakończyć rejestrację aplikacji. Spowoduje to powrót do ekranu nowej aplikacji.
9. Na ekranie aplikacji znajdź **Application (client) ID**. Skopiuj je, aby użyć podczas konfigurowania importu e-maili dla **DocBits**.

![Strona przeglądu zarejestrowanej aplikacji pokazująca Display name Ephesoft OAuth2 App oraz Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Z lewego panelu wybierz **Certificates & secrets**:

![Strona przeglądu zarejestrowanej aplikacji z wybraną pozycją Certificates and secrets w sekcji Manage lewego panelu](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Na ekranie **Certificates & secrets** kliknij przycisk **+ New client secret** w sekcji **Client secrets**:

![Ekran Certificates & secrets z sekcją Client secrets i przyciskiem + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. W oknie dialogowym **Add a client secret** kliknij przycisk **Add**:

![Okno dialogowe Add a client secret z polami Description i Expires oraz przyciskiem Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Zaleca się wypełnienie opisu, aby zidentyfikować ten sekret wśród wielu (obecnie limit wynosi 2 sekrety na aplikację).

![Lista client secretów z nowym sekretem oraz kolumnami opisu, Value i Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Uwaga**</mark>: Wybierz tę datę wygaśnięcia zgodnie z polityką firmy. Po wygaśnięciu należy utworzyć nowy client secret i określić go dla każdej konfiguracji e-mail, w której był wcześniej używany.

13. Nowo wygenerowany client secret będzie widoczny. Skopiuj ten client secret, aby użyć go podczas konfigurowania importu e-maili dla DocBits.

![Sekcja Client secrets w Certificates & secrets z wygenerowaną wartością sekretu gotową do skopiowania](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Ważne:** Upewnij się, że skopiowałeś client secret, ponieważ client secret nie będzie wyświetlany ponownie po zamknięciu.

14. Wybierz **Authentication** w lewym panelu. Spowoduje to wyświetlenie ekranu **Authentication** po prawej stronie.

![Ekran uwierzytelniania rejestracji aplikacji otwarty z panelu po lewej stronie z ustawieniami platformy po prawej](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. W sekcji **Advanced settings** kliknij **Yes** dla **Default client type**.

![Sekcja Advanced settings ekranu Authentication z opcją Default client type ustawioną na Yes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Kliknij **Save**, aby potwierdzić zmiany.

![Górny pasek rejestracji aplikacji z wyróżnionym przyciskiem Save po włączeniu domyślnego typu klienta](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Wybierz **API permissions** w lewym panelu. Spowoduje to wyświetlenie ekranu uprawnień API.

![Ekran API permissions otwarty z lewego panelu pokazujący skonfigurowane uprawnienia dla aplikacji](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Domyślnie obecne jest uprawnienie **User.Read** z **Microsoft Graph**, pozostaw je bez zmian.

![Lista skonfigurowanych uprawnień pokazująca domyślne uprawnienie delegowane User.Read dla Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Uwaga**</mark>: Jest to wymagane uprawnienie. Jeśli to uprawnienie nie jest dostępne, dodaj uprawnienie wykonując poniższe kroki dla uprawnienia **Mail.ReadWrite**.

19. Kliknij **+ Add a permission**. Spowoduje to otwarcie panelu **Request API permissions**.

![Panel Request API permissions z opcjami Microsoft APIs, APIs my organization uses i przepływem + Add a permission](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Kliknij **Microsoft Graph**.

![Panel Request API permissions z wyróżnionym Microsoft Graph wśród często używanych interfejsów API firmy Microsoft](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Z dwóch podkategorii wybierz **App Permissions**.

![Panel Request API permissions dla Microsoft Graph z opcjami Delegated permissions i Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Wpisz **Mail.ReadWrite** w polu wyszukiwania. Zaznacz pole wyboru **Mail.ReadWrite** dla uprawnienia.

![Pole wyszukiwania uprawnień aplikacji z wpisanym Mail.ReadWrite i zaznaczonym polem wyboru uprawnienia Mail.ReadWrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Spowoduje to aktywowanie przycisku **Add permissions** na dole panelu. Kliknij **Add permissions**.

![Panel Request API permissions z wybranym uprawnieniem Mail.ReadWrite i przyciskiem Add permissions na dole](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Spowoduje to dodanie uprawnienia **Mail.ReadWrite** do listy **Configured permissions** dla aplikacji.

<mark style="color:red;">**Uwaga**</mark>: Mogą być wymagane uprawnienia administratora. Administrator będzie musiał autoryzować aplikację do używania tych uprawnień. Po autoryzacji przyznany status zostanie wskazany w następujący sposób:

![Lista skonfigurowanych uprawnień z dodanym uprawnieniem aplikacji Mail.ReadWrite i pokazanym jego stanem udzielenia](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
