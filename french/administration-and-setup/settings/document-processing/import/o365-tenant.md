# O365 Tenant

## Enregistrer une App sur Azure AD

<mark style="color:red;">**Remarque**</mark>: Les autorisations peuvent nécessiter une autorisation d'un administrateur.

1. Connectez-vous au [Portail Azure](https://portal.azure.com/) en utilisant vos identifiants.
2. Depuis les services Azure, localisez et ouvrez Azure Active Directory (également connu sous le nom d'Azure AD).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Dans la section **Manage**, sélectionnez **App registrations**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Dans l'écran App registrations, cliquez sur **+ New registration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. L'écran **Register an application** s'affiche. Entrez le nom d'affichage destiné à l'utilisateur pour l'App dans **Name**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Sélectionnez l'un des types de compte suivants en fonction de vos besoins:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Laissez l'option **Redirect URI (optional)** telle quelle.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Cliquez sur **Register** pour terminer l'enregistrement de l'App. Cela vous ramènera à l'écran de la nouvelle App.
9. Dans l'écran de l'App, localisez l'**Application (client) ID**. Copiez-le pour l'utiliser lors de la configuration de l'importation d'e-mails pour **DocBits**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Depuis le panneau de gauche, sélectionnez **Certificates & secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Dans l'écran **Certificates & secrets**, cliquez sur le bouton **+ New client secret** dans la section **Client secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Dans la boîte de dialogue **Add a client secret**, cliquez sur le bouton **Add**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Il est recommandé de remplir une description pour identifier ce secret parmi plusieurs (pour l'instant, la limite est de 2 secrets par App).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Remarque**</mark>: Sélectionnez cette date d'expiration selon la politique de votre entreprise. Une fois expiré, un nouveau client secret devra être créé et spécifié pour chaque configuration d'e-mail où il a été utilisé précédemment.

13. Le client secret nouvellement généré sera visible. Copiez ce client secret pour l'utiliser lors de la configuration de l'importation d'e-mails pour DocBits.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Important:** Assurez-vous d'avoir copié le client secret car le client secret ne s'affichera plus une fois fermé.

14. Sélectionnez **Authentication** dans le panneau de gauche. Cela affichera l'écran **Authentication** sur le côté droit.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Dans la section **Advanced settings**, cliquez sur **Yes** pour **Default client type**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Cliquez sur **Save** pour confirmer les modifications.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Sélectionnez **API permissions** dans le panneau de gauche. Cela affichera l'écran des autorisations API.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Par défaut, l'autorisation **User.Read** de **Microsoft Graph** est présente, laissez-la telle quelle.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Remarque**</mark>: Il s'agit d'une autorisation requise. Si cette autorisation n'est pas disponible, ajoutez l'autorisation avec les étapes mentionnées ci-dessous pour l'autorisation **Mail.ReadWrite**.

19. Cliquez sur **+ Add a permission**. Cela ouvrira le panneau **Request API permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Cliquez sur **Microsoft Graph**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Parmi les deux sous-catégories, sélectionnez **App Permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Tapez **Mail.ReadWrite** dans la zone de recherche. Cochez la case **Mail.ReadWrite** pour l'autorisation.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Cela activera le bouton **Add permissions** en bas du panneau. Cliquez sur **Add permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Cela ajoutera l'autorisation **Mail.ReadWrite** à la liste des **Configured permissions** pour l'App.

<mark style="color:red;">**Remarque**</mark>: Des autorisations d'administrateur peuvent être requises. L'administrateur devra autoriser l'App à utiliser ces autorisations. Une fois autorisé, le statut accordé sera indiqué comme suit:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
