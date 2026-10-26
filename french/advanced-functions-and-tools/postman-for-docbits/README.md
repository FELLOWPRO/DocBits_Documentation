# Postman pour DocBits

Ce guide vous montrera comment faire des demandes HTTP à votre organisation DocBits via Postman. Il est facile à utiliser et très utile pour les administrateurs d’organisation.

## Configuration

Tout d’abord, téléchargez Postman sur votre système et connectez-vous/inscrivez-vous.

Suivez maintenant ce guide étape par étape pour savoir comment fonctionnent les requêtes HTTP dans Postman.

Authorization in Postman

Avant de pouvoir créer vos requêtes HTTP, vous devez saisir votre clé API de DocBits pour les autoriser.

* Cliquez sur l'onglet \`Authorization\` et choisissez \`API Key\` comme type d'autorisation.

![Requête Postman avec l'onglet Authorization ouvert et la liste Type contenant Inherit auth from parent, Bearer Token, Basic Auth, Digest Auth, OAuth 1.0 et OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Remplissez les valeurs. Entrez “X-API-key” dans le champ \`Key\` et votre clé API comme valeur (trouvée dans le menu Paramètres DocBits sous Intégration) Sélectionnez Ajouter à \`Header\`.

&#x20;

* Cela devrait ressembler à ceci :

![Onglet Authorization de Postman avec le type API Key, la Key x-api-key, le champ Value pour la clé API et la sélection Header dans Add to](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Available at https://api.polydocs.io

* Cliquez sur Autoriser dans le coin supérieur droit

![Bouton Authorize en haut à droite de la vue API de Postman](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Entrez votre clé API et confirmez en cliquant sur \`Authorize\`

![Boîte de dialogue Available authorizations avec l'entrée APIKeyHeader de type apiKey, le Name X-API-KEY, In header, un champ Value vide et le bouton Authorize](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Créer un espace de travail dans Postman

* Cliquez sur Espaces de travail et créez un nouvel espace de travail (vous pouvez le nommer comme vous le souhaitez

![Vue d'ensemble des espaces de travail Postman avec le bouton Create Workspace et la liste des espaces récemment consultés](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Vous devez sélectionner la visibilité qui détermine qui peut accéder à cet espace de travail.

![Boîte de dialogue Create workspace avec les champs Name et Summary, les options de visibilité Personal, Private, Team, Partner et Public, et les boutons Create Workspace et Cancel](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Après avoir fait votre sélection et cliqué sur \`Create Workspace\`, sélectionnez Collections sur le côté gauche de l'application et créez une nouvelle collection pour vos demandes HTTP en cliquant sur \`+\`.

![Barre latérale de Postman avec le groupe Collections et l'entrée New Collection pour créer une collection](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

Dans cette collection, vous pouvez ajouter plusieurs requêtes HTTP. Pour cela, cliquez sur les 3 points de la collection et sélectionnez \`Add request\`.

![Menu contextuel d'une collection dans Postman avec les entrées Share, Move, Run collection, Edit, Add request, Add folder, Monitor collection, Mock collection, Create a fork, Create pull request, Merge changes et Pull changes](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Exemple de méthode "GET"

La méthode GET est très utile pour obtenir des informations sur les utilisateurs, les sous-organisations, les documents traités et bien plus encore.

* Choisissez la méthode GET dans votre requête HTTP.
* Autorisez-vous comme décrit ci-dessus.
* Ouvrez https://api.polydocs.io et ajoutez le chemin de la fonction derrière le Polydocs URL. Par exemple :

![Documentation de l'API pour l'opération GET /users/get_users intitulée Get Users, avec la section Parameters sans entrée et la section Responses avec le code 200 Successful Response](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Collez maintenant ce lien dans la zone de texte à côté de la méthode GET dans Postman.

Cliquez sur \`Send\` et vous devriez recevoir toutes les informations sur chaque utilisateur de votre organisation.

## Exemple de méthode "POST"

La méthode POST est généralement utilisée pour créer des utilisateurs ou des organisations, par exemple. Cette méthode insère des informations dans la base de données.

Create User

* Sélectionnez la méthode POST.
* Autorisez-vous comme décrit ci-dessus
* Ouvrez https://api.polydocs.io et ajoutez le chemin de la fonction derrière le Polydocs URL. Dans ce cas :

![Documentation de l'API pour l'opération POST /users/create intitulée Create User avec les champs obligatoires first_name, last_name, email et password dans le corps de la requête et le champ booléen is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Collez maintenant ce lien dans la zone de texte à côté de la méthode POST dans Postman.
* Sélectionnez l'onglet \`Body\` dans votre requête HTTP et entrez les clés et les valeurs pour chaque identifiant qui a un astérisque rouge à côté de son nom.

Lorsque vous avez terminé, cela devrait ressembler à ceci :

![Onglet Body de Postman avec form-data sélectionné et les lignes first_name avec First_Name, lastname avec Last_Name, email avec test@test.com, password et is_admin avec False](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Si vous souhaitez créer un compte administrateur, définissez la valeur \`is\_admin\` sur true.

Enfin, cliquez sur \`Send\` et vous pourrez voir toutes les informations d'identification que vous avez définies dans la réponse ci-dessous. Cela signifie que l'utilisateur a été créé.

### Importer un document

Vous pouvez également utiliser la méthode POST pour téléverser un document vers DocBits.

* Sélectionnez la méthode POST.
* Autorisez-vous comme décrit ci-dessus.
* Ouvrez https://api.polydocs.io et ajoutez le chemin de la fonction derrière le Polydocs URL.

Dans ce cas :

![Documentation de l'API pour l'opération POST /document/process intitulée Process avec les champs facultatifs source, org_id, priority, sub_org_id et metadata dans le corps de la requête et le champ obligatoire file de type string binary](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Collez maintenant ce lien dans la zone de texte à côté de la méthode POST dans Postman.
* Sélectionnez l'onglet \`Body\` dans votre requête HTTP et choisissez \`form-data\`

![Requête Postman POST https://api.polydocs.io/document/process avec l'onglet Body ouvert, form-data sélectionné et une ligne KEY vide pour le fichier](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![Requête Postman POST https://api.polydocs.io/document/process avec l'onglet Body ouvert, form-data sélectionné et la ligne file avec la valeur Mango_invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Entrez le fichier dans le champ \`KEY\` où vous trouverez la liste déroulante Fichier masquée. Sélectionnez \`File\` et accédez au champ \`VALUE\` où vous pouvez sélectionner votre fichier en cliquant sur \`Select Files\`.

Lorsque vous cliquez sur \`Send\`, vous devriez voir “success”: true dans la réponse.

Cela devrait ressembler à ceci :

![Requête Postman POST https://api.polydocs.io/document/process avec Status 200 OK et la réponse JSON contenant success true, le doc_id et le nom de fichier Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Exemple de méthode "DELETE"

La méthode DELETE est utilisée pour supprimer, par exemple, des utilisateurs, des organisations, etc.

* Sélectionnez la méthode DELETE
* Autorisez-vous comme décrit ci-dessus.
* Ouvrez https://api.polydocs.io et ajoutez le chemin de la fonction derrière le Polydocs URL.

Par exemple :

![Documentation de l'API pour l'opération DELETE /users/delete/{user_id} intitulée Delete User avec le paramètre de chemin user_id](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Collez maintenant ce lien dans la zone de texte à côté de la méthode DELETE dans Postman.
* Remplacez le {user\_id} à la fin de l’URL par l'ID réel de l’utilisateur que vous souhaitez supprimer. (Vous pouvez obtenir le user\_id en utilisant la méthode GET).
* Si vous avez inclus le user\_id dans l’URL, vous n'avez pas besoin d'ajouter une clé de corps et une valeur pour celui-ci.
* Lorsque vous cliquez sur \`Send\`, vous devriez voir “success”: true dans la réponse.

Cela devrait ressembler à ceci :

![Requête Postman DELETE https://api.polydocs.io/users/delete/508 avec Status 200 OK et la réponse JSON success true](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Exemple de méthode "PUT"

La méthode PUT est principalement utilisée pour mettre à jour les données des utilisateurs ou des organisations. Il est très simple à comprendre et à utiliser.

* Sélectionnez la méthode PUT.
* Autorisez-vous comme décrit ci-dessus.
* Ouvrez https://api.polydocs.io et ajoutez le chemin de la fonction derrière le Polydocs URL.

Par exemple :

![Documentation de l'API pour l'opération PUT /users/update/{user_id} intitulée Update User avec le paramètre de chemin user_id et les champs first_name, last_name, email, is_organisation_admin et password dans le corps de la requête](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Collez maintenant ce lien dans la zone de texte à côté de la méthode PUT dans Postman.
* Remplacez le {user\_id} à la fin de l’URL par l'ID réel de l’utilisateur que vous souhaitez supprimer. (Vous pouvez obtenir le user\_id en utilisant la méthode GET).

## Modifier l’adresse e-mail d’un utilisateur

* Dans le corps, saisissez “email” comme clé et la nouvelle adresse e-mail comme valeur.
* Ensuite, appuyez simplement sur \`Send\` et vous devriez voir “success” dans la réponse.
