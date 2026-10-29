# Tâches et notifications

### Aperçu

Le paramètre **Tâches et notifications** (Tasks & Notifications) active la gestion des tâches intégrée à DocBits. Lorsqu'il est activé, les membres de l'équipe peuvent créer des tâches, s'attribuer des documents (par exemple pour la validation, la correction ou l'approbation) et recevoir des notifications à leur sujet.

Ce paramètre est **désactivé par défaut**. Lorsqu'il est activé, quatre options supplémentaires apparaissent en dessous :

* **Tâches du tableau de bord Nombre** : affiche sur le tableau de bord les documents qui ont des tâches ouvertes.
* **Autoriser le filtre « Tous » pour les non-administrateurs** : permet aux utilisateurs qui ne sont pas administrateurs de voir toutes les tâches.
* **Suppression de tâches non admin** : définit les tâches que les utilisateurs non administrateurs peuvent supprimer.
* **Achèvement des tâches non administratives** : définit les tâches que les utilisateurs non administrateurs peuvent clôturer.

Ces options ne restreignent jamais les administrateurs de l'organisation.

### Que fait ce paramètre ?

* **Activé** — Les fonctions Tâches et notifications deviennent disponibles dans DocBits. Les utilisateurs peuvent attribuer des tâches, suivre leur statut et être notifiés lorsqu'un élément requiert leur attention.
* **Désactivé** — L'attribution des tâches et les notifications associées sont désactivées. La désactivation désactive également **Tâches du tableau de bord Nombre**.

### Tâches du tableau de bord Nombre

L'option **Tâches du tableau de bord Nombre** détermine si le tableau de bord signale les documents qui ont des tâches ouvertes. Il ne s'agit pas d'un compteur global : l'indication se fait document par document.

* **Activé** — Un document qui a des tâches au statut **Ouvert** ou **En cours** affiche une icône de tâche dans la liste du tableau de bord. Au survol de l'icône, le nombre de tâches ouvertes du document s'affiche, par exemple « 2 Tâche(s) ouverte(s) ». Les tâches terminées, rejetées ou supprimées ne sont pas comptées.
* **Désactivé** — L'icône est masquée. Les tâches fonctionnent normalement.

{% hint style="info" %}
**Tâches du tableau de bord Nombre** dépend de **Tâches et notifications**. Si vous désactivez Tâches et notifications, l'affichage des tâches sur le tableau de bord est également désactivé.
{% endhint %}

### Autoriser le filtre « Tous » pour les non-administrateurs

L'aperçu des tâches comporte un filtre **Assigné à** avec les options **Tous** et **Assigné à moi**. Les administrateurs disposent toujours des deux options.

* **Activé** — Les utilisateurs qui ne sont pas administrateurs peuvent également choisir **Tous** et voir toutes les tâches de l'organisation.
* **Désactivé** (par défaut) — Les utilisateurs qui ne sont pas administrateurs ne disposent que de **Assigné à moi** : l'aperçu affiche alors les tâches qui leur sont assignées.

### Suppression de tâches non admin

L'option **Suppression de tâches non admin** définit quelles tâches et notifications les utilisateurs qui ne sont pas administrateurs peuvent supprimer. Les administrateurs peuvent toujours supprimer toutes les tâches.

| Option | Les utilisateurs non administrateurs peuvent supprimer |
| --- | --- |
| **Aucun** | Aucune tâche. |
| **Tâches créées uniquement** | Les tâches qu'ils ont créées. |
| **Création et attribution des tâches** | Les tâches qu'ils ont créées, ainsi que les tâches qui leur sont assignées ou assignées à l'un de leurs groupes. C'est le comportement appliqué tant que l'option n'a jamais été modifiée. |
| **Toutes les tâches** | Toutes les tâches. |

Les utilisateurs peuvent toujours supprimer les tâches qu'ils ont créées, sauf avec **Aucun**. Une tâche assignée à personne ne peut donc être supprimée que par l'utilisateur qui l'a créée, par un administrateur ou avec **Toutes les tâches**. Une tâche dont le créateur n'est pas enregistré, par exemple une tâche créée par le système, ne peut être supprimée que par les utilisateurs à qui elle est assignée (avec **Création et attribution des tâches**), par un administrateur ou avec **Toutes les tâches**.

{% hint style="warning" %}
Supprimer une tâche la retire de la liste des tâches sans qu'aucune décision ne soit prise. Si les tâches ne doivent être clôturées que par une décision, réglez **Suppression de tâches non admin** sur **Aucun** et **Achèvement des tâches non administratives** (voir ci-dessous) sur **Réservé aux administrateurs**.
{% endhint %}

### Achèvement des tâches non administratives

L'option **Achèvement des tâches non administratives** définit quels utilisateurs non administrateurs peuvent clôturer une tâche, c'est-à-dire la passer à **Terminé** ou **Rejeté**. Malgré son libellé, elle ne concerne pas un type de tâche : elle s'applique aux utilisateurs qui ne sont pas administrateurs. Les administrateurs peuvent toujours clôturer les tâches, quelle que soit l'option choisie.

| Option | Qui peut clôturer une tâche |
| --- | --- |
| **Comportement par défaut** | Le paramètre n'ajoute aucune restriction. Les utilisateurs peuvent clôturer les tâches qui leur sont assignées ou assignées à l'un de leurs groupes, comme avant l'existence de ce paramètre. C'est le comportement appliqué tant que l'option n'a jamais été modifiée. |
| **Administrateurs et utilisateurs assignés** | Les administrateurs, ainsi que les utilisateurs à qui la tâche est assignée, directement ou par l'intermédiaire de l'un de leurs groupes. Une tâche assignée à quelqu'un d'autre, ou à personne, ne peut pas être clôturée par les autres utilisateurs. DocBits vérifie également cette règle lorsqu'une tâche est modifiée via l'API. |
| **Réservé aux administrateurs** | Uniquement les administrateurs. |

Avec **Administrateurs et utilisateurs assignés** ou **Réservé aux administrateurs**, un utilisateur qui n'a pas le droit de clôturer une tâche :

* ne voit pas le bouton vert **Terminé** sur la page de la tâche, et la liste des statuts n'y propose que **Ouvert** et **En cours** ;
* ne peut pas cliquer sur le cercle de statut de la tâche dans le panneau des tâches du document. Au survol, le message « Vous n'êtes pas autorisé à marquer cette tâche comme terminée ou rejetée. » s'affiche ;
* ne voit pas **Marquer comme terminé** pour cette tâche dans la liste des tâches, et **Marquer comme terminé** pour une sélection reste masqué tant qu'une telle tâche est sélectionnée ;
* ne peut pas faire glisser la tâche dans la colonne **Terminé** ou **Rejeté** du tableau des tâches. La carte revient dans sa colonne et le même message s'affiche.

Le paramètre restreint uniquement la clôture. Les utilisateurs conservent tous les autres droits qu'ils avaient auparavant : les utilisateurs à qui une tâche est assignée peuvent toujours la modifier, l'enregistrer, la déplacer entre **Ouvert** et **En cours**, et la rouvrir une fois terminée. Les utilisateurs à qui une tâche n'est pas assignée ne pouvaient pas modifier son statut auparavant, et ne le peuvent toujours pas.

Pour les types de document dont **Historique de l'approbation** est activé, **Approuver** termine toujours des tâches ouvertes du document, quelle que soit l'option choisie ici : les tâches assignées à l'approbateur ou à l'un de ses groupes, et les tâches assignées à personne. Si l'approbateur est administrateur, toutes les tâches ouvertes du document sont terminées.

#### Tâches des documents renvoyés en validation

Comme les utilisateurs ne peuvent pas clôturer eux-mêmes leurs tâches avec **Administrateurs et utilisateurs assignés** ou **Réservé aux administrateurs**, DocBits clôture lui-même les tâches ouvertes d'un document lorsqu'un document en attente d'approbation est renvoyé en validation :

* **Restart workflow** sur l'écran d'approbation : toutes les tâches ouvertes du document sont rejetées.
* **Rejeter et corriger** : toutes les tâches ouvertes du document sont rejetées.
* **Approuver et corriger** : les tâches que **Approuver** terminerait (voir ci-dessus) sont terminées, uniquement pour les types de document dont **Historique de l'approbation** est activé. Toutes les autres tâches ouvertes sont rejetées.

Les tâches ouvertes sont clôturées avant que le document ne retourne en validation. Les workflows déclenchés par le changement de statut peuvent ensuite créer de nouvelles tâches pour tout ce qui nécessite encore une intervention.

Avec **Comportement par défaut**, les tâches ouvertes restent ouvertes lorsqu'un document est renvoyé, comme auparavant.

### Avantages

* **Responsabilités claires** : Les documents peuvent être attribués à la bonne personne au lieu de s'appuyer sur les e-mails.
* **Rien n'est oublié** : Les notifications rappellent aux utilisateurs les documents qui nécessitent leur action.
* **Travail en cours en un coup d'œil** : Avec Tâches du tableau de bord Nombre, le tableau de bord indique quels documents ont encore des tâches ouvertes.
* **Des décisions traçables** : Avec les options de suppression et de clôture, les tâches ne quittent la file d'attente que par une décision ou par l'intervention d'un administrateur.

### Utilisation

1. Allez dans **Paramètres**.
2. Sélectionnez **Traitement des documents**.
3. Sélectionnez **Module**.
4. Ouvrez la section **Type de document**.
5. Activez **Tâches et notifications**.
6. (Facultatif) Activez **Tâches du tableau de bord Nombre** pour afficher l'icône de tâche sur le tableau de bord.
7. (Facultatif) Activez **Autoriser le filtre « Tous » pour les non-administrateurs** si tous les utilisateurs doivent voir toutes les tâches.
8. (Facultatif) Choisissez dans **Suppression de tâches non admin** les tâches que les utilisateurs peuvent supprimer.
9. (Facultatif) Choisissez dans **Achèvement des tâches non administratives** qui peut clôturer les tâches.

Les options de suppression et de clôture sont enregistrées dès que vous choisissez une valeur.

### Quand utiliser cette fonction

* **Équipes qui partagent le travail sur les documents** : Activez-la lorsque plusieurs personnes valident ou approuvent des documents et doivent se transmettre le travail.
* **Visibilité de la charge de travail** : Activez également Tâches du tableau de bord Nombre lorsque l'équipe doit voir sur le tableau de bord quels documents ont encore des tâches ouvertes.
* **Tâches que seuls un administrateur ou une décision doivent clôturer** : Réglez **Achèvement des tâches non administratives** sur **Réservé aux administrateurs** ou **Administrateurs et utilisateurs assignés**, et **Suppression de tâches non admin** sur **Aucun**, lorsque les utilisateurs ne doivent pas retirer des tâches qui n'ont pas réellement été traitées.
* **Configurations mono-utilisateur ou entièrement automatisées** : Vous pouvez la laisser désactivée si personne n'a besoin d'attribuer des documents ni de suivre des tâches.
