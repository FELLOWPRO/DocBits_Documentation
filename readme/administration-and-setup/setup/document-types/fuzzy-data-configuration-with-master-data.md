# Configuration des données floues avec les données maîtres

## **Aperçu**

Chaque type de document a ses propres configurations par défaut et doit être configuré séparément. Alors que cet exemple explique la configuration des **Factures**, le même processus s'applique à tous les types de documents.

## Pour configurer les données floues, accédez à :

Paramètres → Paramètres globaux → Types de documents → Facture → Champs → Paramètres des données maîtres → Rechercher les données maîtres

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Recherches par défaut**

Il existe **quatre groupes de recherche par défaut** pour les factures :

1. **Données de l'entreprise**
2. **En-tête de commande d'achat**
3. **Fournisseur**
4. **Code de taxe**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Chaque groupe contient des champs spécifiques. Cliquez sur un groupe pour le **développer** et voir les champs. Les groupes de recherche par défaut sont étiquetés avec une balise **"Par défaut"**.

## **État de configuration de recherche**

* Les **configurations actives** sont marquées avec une balise **"Activé"**.
* Les **configurations désactivées** sont marquées avec une balise **"Désactivé"**.

## **Prérequis : Importation des données maîtres**

Pour que les données floues fonctionnent correctement, les **données maîtres** pertinentes doivent être importées. Sans cela, le système n'a pas de données de référence à utiliser. Voici comment importer les données maîtres :

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gestion des groupes de recherche**

Chaque groupe de recherche est **activé par défaut** mais peut être modifié en cliquant sur les trois points :

* **Désactiver** → Désactive un groupe. _(Disponible uniquement pour les groupes activés)_
* **Activer** → Active un groupe. _(Disponible uniquement pour les groupes désactivés)_
* **Dupliquer** → Crée une copie qui peut être modifiée sans affecter l'original.
* **Afficher** → Affiche des informations telles que le **type de document** auquel il appartient et la **table de recherche** qu'il utilise. _(Disponible uniquement pour les groupes par défaut)_
* **Modifier** → Disponible pour les groupes **non par défaut**. Permet de modifier les détails du groupe.
* **Supprimer** → Supprime complètement le groupe. _(Uniquement pour les groupes non par défaut)_

## **Création d'une nouvelle configuration de recherche**

Il existe **deux façons** de créer une configuration de recherche :

1.  **Dupliquer une recherche existante**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Cela copie toutes les informations et les champs d'un groupe existant.
    * Vous devez uniquement fournir un **nouveau nom**.
2.  **Créer une recherche à partir de zéro**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Cliquez sur **"Créer une configuration de recherche"**.
    * Remplissez les détails requis :
      * **Nom de la configuration**
      * **Table de recherche** (Table de données maîtres à utiliser)
      * **Gestionnaire de conflits** (Choisissez parmi : Meilleur score, Aucun retour, Premier retour)
      * **Type de contexte** (En-tête ou Ligne) besoin de contexte
      * **Correspondance totale** (Option de case à cocher) besoin de contexte

## **Gestion des champs au sein d'un groupe de recherche**

Chaque groupe contient des champs qui peuvent être **ajoutés, supprimés, modifiés ou consultés**, selon qu'ils sont des champs par défaut ou des champs personnalisés.

### **Champs par défaut**

*   Marqués d'une balise **"Par défaut"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Peuvent seulement être consultés**, pas modifiés ou supprimés.

### **Champs non par défaut**

* **Peuvent être modifiés ou supprimés** en cliquant sur les trois points et en sélectionnant **Modifier** ou **Supprimer**.

### **Ajout d'un nouveau champ**

**Remarque :** Vous pouvez créer des champs à l'intérieur de configurations de recherche par défaut.

Pour ajouter un nouveau champ dans un groupe :

1.  Cliquez sur **"Créer"** à l'intérieur du groupe pertinent.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Fournissez les détails suivants :
   * **Champ de recherche** → Nom de colonne de la table de recherche des données maîtres.
   * **Champ de validation** → Champ DocBits correspondant.
   * **Champ parent** → _(Plus de détails nécessaires)_
   * **Opérateur de recherche** → Choisissez parmi :
     * Intelligent
     * Contient
     * Exact
     * Commence par
     * Se termine par
   * **Cases à cocher :**
     * **Déclenchement automatique** → Lorsqu'il est activé, si un autre champ dans une configuration de recherche différente partage la même colonne, ce champ se mettra à jour **automatiquement** chaque fois que l'autre champ est mis à jour
     * **Recherche** → Active le champ en tant que champ **Données floues**, permettant des recherches dans la recherche de données maîtres (icône bleue dans l'écran de validation).

## **Étape finale : Ajout des champs à la mise en page**

Après avoir configuré les champs de données floues, **assurez-vous de les ajouter à la mise en page en utilisant le générateur de mise en page**. Si les champs ne sont pas ajoutés à la mise en page, ils ne seront pas disponibles pour une utilisation.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

## **Comment DocBits choisit un fournisseur**

Lorsqu'un document arrive, DocBits recherche le fournisseur dans vos données maîtres. Trois réglages déterminent le résultat. Cette section les explique étape par étape, avec des exemples.

### **Étape 1 — Quels champs servent à la recherche**

DocBits utilise un champ pour la recherche uniquement si les deux points sont vrais :

* le champ est coché **Recherchable (Searchable)** ou **Auto Trigger** dans la configuration de recherche, et
* le champ a une valeur sur le document.

La provenance de la valeur n'a pas d'importance. Un champ entraîné, un champ rempli par l'IA et une valeur saisie par un utilisateur sont traités de la même façon.

{% hint style="warning" %}
**Recherchable fait deux choses.** Il affiche l'icône bleue de recherche dans l'écran de validation **et** il ajoute le champ à la recherche automatique de fournisseur. Un champ qui ne doit être cherché qu'à la main reste décoché.
{% endhint %}

### **Étape 2 — Une seule recherche, pas une recherche par champ**

DocBits ne recherche **pas** chaque champ séparément. Il construit **une** recherche sur tous les champs utilisés. **Tout faire correspondre (Match All)** décide de la combinaison :

* **Tout faire correspondre désactivé** (par défaut) → « trouver tous les fournisseurs qui correspondent au numéro de TVA **OU** au nom du fournisseur ». Cela donne une liste **plus longue**.
* **Tout faire correspondre activé** → « trouver tous les fournisseurs qui correspondent au numéro de TVA **ET** au nom du fournisseur ». Cela donne une liste **plus courte**.

N'oubliez pas que les opérateurs **Smart** et **Contains** cherchent une partie du texte. Le nom « Meier » trouve aussi « Meier Bau GmbH » et « Meier & Sons Ltd ». Un nom de fournisseur trouve donc souvent plusieurs fournisseurs.

### **Étape 3 — Ce qui se passe quand la liste contient plusieurs fournisseurs**

Le **Gestionnaire de conflits (Conflict Handler)** décide :

* **Best Score** → prend le fournisseur qui correspond au plus grand nombre de champs. Ne laisse jamais le fournisseur vide.
* **Return None** → laisse le fournisseur vide, pour qu'un utilisateur le choisisse.
* **Return First** → prend le premier fournisseur de la liste.

### **Exemples**

Dans tous les exemples, le document porte un numéro de TVA et un nom de fournisseur, et les deux champs sont **Recherchables**.

<table><thead><tr><th width="150">Le numéro de TVA trouve</th><th width="150">Le nom trouve</th><th width="150">Tout faire correspondre désactivé + Return None</th><th width="150">Tout faire correspondre activé + Return None</th><th width="150">Tout faire correspondre désactivé + Best Score</th></tr></thead><tbody>
<tr><td>seulement A</td><td>A et B</td><td>vide</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A et B</td><td>seulement B</td><td>vide</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A, B et C</td><td>C, D et E</td><td>vide</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A, B et C</td><td>B, C et D</td><td>vide</td><td>vide</td><td>B ou C, peu fiable</td></tr>
<tr><td>seulement A</td><td>rien</td><td><strong>A</strong></td><td>vide</td><td><strong>A</strong></td></tr>
</tbody></table>

Comment lire le tableau :

* **Les lignes 1 à 3** sont le cas normal. Un champ est unique, l'autre non. Avec **Tout faire correspondre désactivé**, la liste contient plusieurs fournisseurs et **Return None** laisse le champ vide. **Tout faire correspondre activé** ne garde que le fournisseur qui correspond aux deux champs et le trouve.
* **La ligne 4** n'a aucun fournisseur unique. Laisser le champ vide est correct. **Best Score** en choisit quand même un, qui peut être le mauvais.
* **La ligne 5** est le risque de **Tout faire correspondre activé**. Voir l'avertissement ci-dessous.

{% hint style="warning" %}
**Tout faire correspondre peut perdre un fournisseur.** Avec **Tout faire correspondre activé**, chaque champ utilisé doit correspondre. Si un champ porte une valeur qui n'existe pas dans vos données maîtres — une faute de frappe, un ancien nom d'entreprise, une valeur lue sur la page — la recherche entière ne renvoie rien et aucun fournisseur n'est trouvé, alors que le numéro de TVA seul aurait trouvé le bon.
{% endhint %}

### **Un fournisseur était reconnu avant et ne l'est plus**

Presque toujours, un champ de plus fournit désormais une valeur. Vérifiez dans cet ordre :

1. Ouvrez le document. Quel champ du groupe de recherche porte maintenant une valeur qui était vide avant ?
2. Ouvrez la configuration de recherche. Ce champ est-il coché **Recherchable** ou **Auto Trigger** ? Si oui, il participe désormais à la recherche et allonge la liste des résultats.
3. Choisissez l'une des trois solutions :
   * **Le champ ne doit pas participer à la recherche** → décochez **Recherchable** et **Auto Trigger** pour ce champ. Le champ garde sa valeur sur le document et reste affiché à l'utilisateur. C'est la plus petite modification.
   * **Le champ doit participer** → activez **Tout faire correspondre**, mais lisez d'abord l'avertissement ci-dessus.
   * **Vous voulez un fournisseur dans tous les cas** → réglez le **Gestionnaire de conflits** sur **Best Score**. Acceptez qu'il puisse choisir le mauvais fournisseur au lieu de laisser le champ vide.
