# Activation et gestion des scripts

Les administrateurs peuvent utiliser les **scripts** pour gérer les règles de traitement d'un type de document. Ce guide montre où trouver les scripts, comment les activer ou les désactiver et comment modifier un script publié en toute sécurité.

## Trouver un script

1. Ouvrez **Paramètres → Types de Documents**.
2. Sur le type de document à gérer, sélectionnez **Scénarios**. La page liste les scripts de ce type de document.
3. Recherchez par nom ou utilisez **Tous**, **Actif** et **Inactif** pour affiner la liste. Vous pouvez aussi la trier par nom ou par date de modification.

Chaque carte affiche le nom du script, le déclencheur, la version et le statut. Le crayon ouvre l'éditeur ; l'icône de copie duplique le script. **Nouveau** ouvre l'éditeur pour un nouveau script.

<figure><img src="../../../../../.gitbook/assets/dbdc655-scripts-list-inactive-fr-20261011.png" alt="Liste des scripts du type de document Facture avec un exemple de documentation inactif et les filtres Tous, Actif, Inactif"><figcaption><p>Vérifiez le statut à droite de la carte du script avant de le modifier.</p></figcaption></figure>

## Activer ou désactiver un script

Utilisez l'interrupteur **Actif/Inactif** de la carte du script. La modification est enregistrée immédiatement ; les compteurs de la liste se mettent à jour pour montrer le résultat. Un script inactif reste consultable et modifiable, mais il ne s'exécute pas pendant le traitement des documents.

**Vérifiez le statut après la création d'un script.** Dans l'interface Sandbox actuelle, l'enregistrement d'un nouveau script crée une version active et passe la carte à **Actif**. Passez-le à **Inactif** s'il ne s'agit que d'un brouillon ou d'un exemple de test.

## Modifier un script existant

1. Sélectionnez la carte du script ou son icône crayon. Une version publiée est en lecture seule : vous ne pouvez donc pas la modifier directement.
2. Dans **Historique des versions**, sélectionnez l'icône crayon de la version à modifier. Cela crée un **Brouillon** à partir de cette version.
3. Modifiez le brouillon et sélectionnez l'icône **Enregistrer**. Vérifiez le nom, le type de document, le déclencheur et le code avant d'enregistrer.
4. Testez le script modifié avec des documents représentatifs dans un environnement de test. Lorsqu'il est prêt, sélectionnez l'icône de validation du brouillon dans **Historique des versions** pour rendre cette version active.
5. Revenez à la liste des scripts et vérifiez l'interrupteur **Actif/Inactif** de la carte. La version marquée **ACTIF** dans l'Historique des versions identifie la version sélectionnée ; l'interrupteur de la carte commande si le script s'exécute.

<figure><img src="../../../../../.gitbook/assets/dbdc655-script-published-version-fr-20261011.png" alt="Version publiée du script affichée en lecture seule avec un message invitant à la cloner en brouillon"><figcaption><p>Une version publiée ne peut pas être modifiée directement. Utilisez le crayon dans l'Historique des versions pour créer un brouillon.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc655-script-editable-draft-fr-20261011.png" alt="Brouillon modifiable dans l'Historique des versions à côté de la version actuellement active du script"><figcaption><p>Enregistrez et vérifiez le brouillon avant de le rendre version active.</p></figcaption></figure>

Pour des exemples de scripts et les fonctions disponibles, voir [Scripting dans DocBits](scripting-in-docbits/README.md).
