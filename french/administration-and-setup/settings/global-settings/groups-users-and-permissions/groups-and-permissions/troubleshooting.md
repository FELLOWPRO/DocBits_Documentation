# Résolution des problèmes de contrôle d'accès et de permissions

Si les utilisateurs rencontrent des restrictions d'accès inattendues, telles que des documents manquants, l'incapacité à modifier des champs ou des actions refusées, utilisez la liste de contrôle suivante pour identifier et résoudre le problème en fonction de la configuration des autorisations dans DocBits.

### 1. Vérifier si le contrôle d'accès est activé

Les paramètres de contrôle d'accès s'appliquent uniquement si la fonctionnalité est **activée**.

* Accédez à : `Paramètres` > `Traitement de documents` > `Module`.
* Assurez-vous que le commutateur **Contrôle d'accès** est activé.
* Si désactivé, tous les utilisateurs ont généralement un accès illimité indépendamment des autorisations de groupe ou de champ.

### 2. Vérifier les affectations de groupe

Assurez-vous que l'utilisateur est correctement affecté au(x) groupe(s) approprié(s) :

* Accédez à : `Paramètres` > `Paramètres globaux` > `Groupes, utilisateurs et autorisations`.
* Sélectionnez **Groupes et autorisations**.
* Confirmez que l'utilisateur est répertorié sous le groupe attendu.
* Si le groupe utilise un contrôle d'accès spécifique, une affectation de groupe manquante bloquera l'accès aux documents et aux actions.

### 3. Examiner les autorisations d'accès au groupe

L'accès est accordé par type de document et par action :

* Dans l'écran de **Contrôle d'accès** pour le groupe, vérifiez le type de document (par ex. : Facture, Bon de commande).
* Validez des autorisations telles que :
  * **Liste**, **Affichage**, **Modification**, **Suppression**, **Mise à jour en masse**
  * **Niveaux d'approbation** (1er, 2ème), **Déverrouiller le document**
* Assurez-vous que le niveau d'accès n'est pas limité à **Propriétaire** ou **Administrateur** sauf si approprié.

### 4. Confirmer les autorisations au niveau des champs

L'accès peut également être restreint au niveau des **champs**, ce qui peut bloquer la modification ou la visibilité :

* Dans la configuration de contrôle d'accès du groupe, accédez au type de document et vérifiez les paramètres au niveau des champs.
* Confirmez si les champs sont définis comme :
  * **Lecture/Écriture**, **Lecture seule**, **Écriture propriétaire**, **Aucun**
* Ajustez si nécessaire en fonction du rôle de l'utilisateur.

### 5. Vérifier le paramètre "Uniquement les documents assignés"

Ce paramètre global limite la visibilité des documents :

* Accédez à : `Paramètres` > `Paramètres globaux` > `Groupes, utilisateurs et autorisations`.
* Si **Uniquement les documents assignés** sont **activés**, les utilisateurs ne peuvent voir que les documents qui leur sont explicitement assignés ou à leur groupe.
* Si les utilisateurs ne peuvent pas voir les documents attendus :
  * Vérifiez les affectations de documents.
  * Désactivez temporairement le paramètre pour tester s'il est à l'origine du problème.

### 6. Tester avec un utilisateur ou un groupe dont le fonctionnement est connu

Pour isoler le problème :

* Connectez-vous avec un utilisateur d'un groupe ayant un accès confirmé.
* Comparez la visibilité des documents et les actions disponibles.
* Cela aide à déterminer si le problème est spécifique à l'utilisateur, au groupe ou à l'ensemble du système.

### 7. Vérifier à nouveau les affectations de documents

Si "Uniquement les documents assignés" est **activé**, assurez-vous que :

* Le document est **assigné** à l'utilisateur ou à l'un de ses groupes.
* Utilisez les contrôles d'affectation dans la vue détaillée du document pour effectuer ou revoir les affectations.

### 8. Réinitialiser ou reconfigurer les autorisations

Si les autorisations ont été récemment modifiées ou si les utilisateurs ont été déplacés entre les groupes :

* Vérifiez à nouveau que les paramètres de contrôle d'accès reflètent les nouvelles configurations de groupe.
* Ajustez les autorisations des champs et des documents si nécessaire.
* En cas de doute, créez un groupe de test avec des autorisations étendues et testez le comportement d'accès avant d'appliquer des modifications aux groupes en production.
