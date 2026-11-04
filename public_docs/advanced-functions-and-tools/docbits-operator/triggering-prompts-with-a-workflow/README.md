# Déclenchement des invites avec un flux de travail

Ce guide explique comment configurer un flux de travail DocBits pour déclencher automatiquement une invite enregistrée. Cela vous permet d'intégrer des invites d'opérateur dans les flux de traitement de documents sans saisie manuelle.

## Étape 1 : Créer une invite

Avant de lier une invite à un flux de travail :

* Assurez-vous que votre invite est déjà créée
* Incluez toutes les **variables** nécessaires dans le corps de l'invite.

Si vous avez besoin d'aide pour rédiger ou enregistrer des invites, consultez le [Guide d'écriture d'invite](../prompt-writing-guide.md) et [Aperçu de l'interface de l'opérateur](../).

## Étape 2 : Configurer le flux de travail

Avant de configurer la carte d'invite d'opérateur, assurez-vous que votre flux de travail est correctement créé.

1. Accédez au **Constructeur de flux de travail** dans l'interface DocBits.
2. Créez un nouveau flux de travail ou ouvrez un existant.
3. Définissez les **conditions de déclenchement** - celles-ci déterminent quand le flux de travail démarrera (par exemple, type de document, statut, présence de champ, etc.).
4. Ajoutez les étapes d'action nécessaires à votre flux de travail selon vos besoins.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Étape 3 : Configurer la carte d'invite d'opérateur dans le flux de travail

Dans le Constructeur de flux de travail, utilisez la **carte d'invite d'opérateur** pour configurer une invite qui doit s'exécuter lorsque les conditions du flux de travail sont remplies.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Options de configuration clés

* **Script :** Sélectionnez l'**Invite d'organisation** enregistrée à exécuter.
* **Données de script (Variables) :** Si l'invite sélectionnée contient des variables, définissez leurs valeurs ici en utilisant des paires clé-valeur.
  * Si une variable est laissée vide ici, le système tentera de la remplir automatiquement **à partir du document**.
  * Pour que cela fonctionne, le nom de la variable dans l'invite doit correspondre exactement à l'**ID de champ** de l'attribut du document.
* **Nombre maximal d'étapes :** Définissez le nombre maximal d'étapes que l'opérateur est autorisé à exécuter pendant cette invite.
* **Nombre maximal de tentatives :** Définissez combien de fois le système doit réessayer l'invite en cas d'échec.
* **Mode d'exécution :** Choisissez si l'invite doit s'exécuter :
  * **Dans le Cloud**
  * **Sur site** (nécessaire si votre ERP ou système cible est hébergé localement)
