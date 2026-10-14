# O365 Tenant

## Zarejestruj aplikację w Azure AD

<mark style="color:red;">**Uwaga**</mark>: Uprawnienia mogą wymagać autoryzacji od administratora.

1. Zaloguj się do [Portalu Azure](https://portal.azure.com/) używając swoich danych uwierzytelniających.
2. Z usług Azure znajdź i otwórz Azure Active Directory (znany również jako Azure AD).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. W sekcji **Manage** wybierz **App registrations**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Na ekranie App registrations kliknij **+ New registration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Wyświetli się ekran **Register an application**. Wprowadź nazwę wyświetlaną aplikacji skierowaną do użytkownika w polu **Name**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Wybierz jeden z następujących typów kont w zależności od swoich potrzeb:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Pozostaw opcję **Redirect URI (optional)** bez zmian.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Kliknij **Register**, aby zakończyć rejestrację aplikacji. Spowoduje to powrót do ekranu nowej aplikacji.
9. Na ekranie aplikacji znajdź **Application (client) ID**. Skopiuj je, aby użyć podczas konfigurowania importu e-maili dla **DocBits**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Z lewego panelu wybierz **Certificates & secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Na ekranie **Certificates & secrets** kliknij przycisk **+ New client secret** w sekcji **Client secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. W oknie dialogowym **Add a client secret** kliknij przycisk **Add**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Zaleca się wypełnienie opisu, aby zidentyfikować ten sekret wśród wielu (obecnie limit wynosi 2 sekrety na aplikację).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Uwaga**</mark>: Wybierz tę datę wygaśnięcia zgodnie z polityką firmy. Po wygaśnięciu należy utworzyć nowy client secret i określić go dla każdej konfiguracji e-mail, w której był wcześniej używany.

13. Nowo wygenerowany client secret będzie widoczny. Skopiuj ten client secret, aby użyć go podczas konfigurowania importu e-maili dla DocBits.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Ważne:** Upewnij się, że skopiowałeś client secret, ponieważ client secret nie będzie wyświetlany ponownie po zamknięciu.

14. Wybierz **Authentication** w lewym panelu. Spowoduje to wyświetlenie ekranu **Authentication** po prawej stronie.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. W sekcji **Advanced settings** kliknij **Yes** dla **Default client type**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Kliknij **Save**, aby potwierdzić zmiany.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Wybierz **API permissions** w lewym panelu. Spowoduje to wyświetlenie ekranu uprawnień API.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Domyślnie obecne jest uprawnienie **User.Read** z **Microsoft Graph**, pozostaw je bez zmian.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Uwaga**</mark>: Jest to wymagane uprawnienie. Jeśli to uprawnienie nie jest dostępne, dodaj uprawnienie wykonując poniższe kroki dla uprawnienia **Mail.ReadWrite**.

19. Kliknij **+ Add a permission**. Spowoduje to otwarcie panelu **Request API permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Kliknij **Microsoft Graph**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Z dwóch podkategorii wybierz **App Permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Wpisz **Mail.ReadWrite** w polu wyszukiwania. Zaznacz pole wyboru **Mail.ReadWrite** dla uprawnienia.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Spowoduje to aktywowanie przycisku **Add permissions** na dole panelu. Kliknij **Add permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Spowoduje to dodanie uprawnienia **Mail.ReadWrite** do listy **Configured permissions** dla aplikacji.

<mark style="color:red;">**Uwaga**</mark>: Mogą być wymagane uprawnienia administratora. Administrator będzie musiał autoryzować aplikację do używania tych uprawnień. Po autoryzacji przyznany status zostanie wskazany w następujący sposób:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
