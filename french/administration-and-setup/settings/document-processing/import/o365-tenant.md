# O365 Tenant

## Enregistrer une App sur Azure AD

<mark style="color:red;">**Remarque**</mark>: Les autorisations peuvent nécessiter une autorisation d'un administrateur.

1. Connectez-vous au [Portail Azure](https://portal.azure.com/) en utilisant vos identifiants.
2. Depuis les services Azure, localisez et ouvrez Azure Active Directory (également connu sous le nom d'Azure AD).

![Entrée Azure Active Directory dans la recherche et la liste des services du portail Azure](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Dans la section **Manage**, sélectionnez **App registrations**.

![Page de présentation d'Azure Active Directory avec la section Manage et l'entrée App registrations dans le menu de gauche](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Dans l'écran App registrations, cliquez sur **+ New registration**.

![Page App registrations avec le bouton + New registration dans la barre d'outils](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. L'écran **Register an application** s'affiche. Entrez le nom d'affichage destiné à l'utilisateur pour l'App dans **Name**.

![Formulaire Register an application avec le champ Name et son texte d'aide pour le nom affiché](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Sélectionnez l'un des types de compte suivants en fonction de vos besoins:

* **Comptes dans n'importe quel annuaire organisationnel (n'importe quel annuaire Azure AD Multitenant) et comptes Microsoft personnels (par exemple Skype, Xbox)**
* **Comptes dans n'importe quel répertoire organisationnel (n'importe quel répertoire Azure AD Multitenant)**

![Liste Supported account types avec les options pour locataire unique, multilocataire et comptes Microsoft personnels](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Laissez l'option **Redirect URI (optional)** telle quelle.

![Formulaire Register an application avec les types de comptes pris en charge et l'option multilocataire sélectionnée](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Cliquez sur **Register** pour terminer l'enregistrement de l'App. Cela vous ramènera à l'écran de la nouvelle App.
9. Dans l'écran de l'App, localisez l'**Application (client) ID**. Copiez-le pour l'utiliser lors de la configuration de l'importation d'e-mails pour **DocBits**.

![Section Redirect URI (optional) du formulaire d'inscription et le bouton Register en dessous](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Depuis le panneau de gauche, sélectionnez **Certificates & secrets**:

![Page de présentation de l'application inscrite avec Display name, Application (client) ID et les boutons Delete et Endpoints](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Dans l'écran **Certificates & secrets**, cliquez sur le bouton **+ New client secret** dans la section **Client secrets**:

![Entrée Certificates & secrets dans le menu de gauche de l'application inscrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Dans la boîte de dialogue **Add a client secret**, cliquez sur le bouton **Add**:

![Section Client secrets avec sa description et la mention qu'aucun secret client n'a encore été créé](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Il est recommandé de remplir une description pour identifier ce secret parmi plusieurs (pour l'instant, la limite est de 2 secrets par App).

![Boîte de dialogue Add a client secret avec le champ Description et les options d'expiration 1 an, 2 ans et jamais](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Remarque**</mark>: Sélectionnez cette date d'expiration selon la politique de votre entreprise. Une fois expiré, un nouveau client secret devra être créé et spécifié pour chaque configuration d'e-mail où il a été utilisé précédemment.

13. Le client secret nouvellement généré sera visible. Copiez ce client secret pour l'utiliser lors de la configuration de l'importation d'e-mails pour DocBits.

![Tableau Client secrets avec le secret créé, sa date d'expiration et l'icône de copie à côté de la valeur](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Important:** Assurez-vous d'avoir copié le client secret car le client secret ne s'affichera plus une fois fermé.

14. Sélectionnez **Authentication** dans le panneau de gauche. Cela affichera l'écran **Authentication** sur le côté droit.

![Entrée Authentication dans le menu de gauche de l'application inscrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Dans la section **Advanced settings**, cliquez sur **Yes** pour **Default client type**.

![Page Authentication, section Advanced settings, avec Default client type sur Yes pour un client public](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Cliquez sur **Save** pour confirmer les modifications.

![Page Authentication avec les boutons Save et Discard dans la barre d'outils](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Sélectionnez **API permissions** dans le panneau de gauche. Cela affichera l'écran des autorisations API.

![Entrée API permissions dans le menu de gauche de l'application inscrite](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Par défaut, l'autorisation **User.Read** de **Microsoft Graph** est présente, laissez-la telle quelle.

![Tableau API permissions avec l'autorisation déléguée User.Read de Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Remarque**</mark>: Il s'agit d'une autorisation requise. Si cette autorisation n'est pas disponible, ajoutez l'autorisation avec les étapes mentionnées ci-dessous pour l'autorisation **Mail.ReadWrite**.

19. Cliquez sur **+ Add a permission**. Cela ouvrira le panneau **Request API permissions**.

![Panneau Configured permissions avec le bouton + Add a permission et une liste d'autorisations vide](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Cliquez sur **Microsoft Graph**.

![Panneau Request API permissions avec l'entrée Microsoft Graph parmi les API Microsoft courantes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Parmi les deux sous-catégories, sélectionnez **App Permissions**.

![Panneau des autorisations Microsoft Graph avec le choix entre Delegated permissions et Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Tapez **Mail.ReadWrite** dans la zone de recherche. Cochez la case **Mail.ReadWrite** pour l'autorisation.

![Panneau Request API permissions avec Mail.ReadWrite dans la recherche d'autorisations et l'autorisation Mail correspondante](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Cela activera le bouton **Add permissions** en bas du panneau. Cliquez sur **Add permissions**.

![Panneau Request API permissions avec la case Mail.ReadWrite cochée et le bouton Add permissions actif](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Cela ajoutera l'autorisation **Mail.ReadWrite** à la liste des **Configured permissions** pour l'App.

<mark style="color:red;">**Remarque**</mark>: Des autorisations d'administrateur peuvent être requises. L'administrateur devra autoriser l'App à utiliser ces autorisations. Une fois autorisé, le statut accordé sera indiqué comme suit:

![Panneau Configured permissions avec l'autorisation Mail.ReadWrite et le bouton Grant admin consent pour le locataire](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
