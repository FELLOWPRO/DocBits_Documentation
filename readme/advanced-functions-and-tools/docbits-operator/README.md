# DocBits Operator

## Aperçu

Le **DocBits Operator** est un assistant d'automatisation alimenté par l'IA, conçu pour simplifier les tâches répétitives dans vos workflows. Les utilisateurs créent des _invites_ (prompts) — des instructions étape par étape enrichies de variables — qui guident l'IA pour naviguer, saisir des données et cliquer automatiquement dans les interfaces. Cela réduit l'effort manuel et accélère les opérations courantes.

## Activation du DocBits Operator

Pour activer le DocBits Operator, suivez ces étapes :

1. **Accéder aux paramètres** :
   * Depuis le tableau de bord, accédez à **Settings**.
   *   Sélectionnez **Document Processing**, puis choisissez **Module**.

       <figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-fr.png" alt="Module d’intégration des documents, avec l’option DocBits Operator dans son état existant. Aucun module n’a été activé pendant la capture."><figcaption><p>Module d’intégration des documents, avec l’option DocBits Operator dans son état existant. Aucun module n’a été activé pendant la capture.</p></figcaption></figure>
2. **Activer la fonctionnalité** :
   * Faites défiler la page pour trouver l'option **DocBits Operator**.
   *   Basculez le curseur pour activer le **DocBits Operator**.

       <div align="left"></div>

## Accès à l'interface

* Une fois la fonctionnalité activée, ouvrez le **DocBits Operator** depuis le menu de navigation principal.

### **1. Saisie de l'invite**

En bas de l'écran se trouve un champ de saisie intitulé _« Enter your prompt here… »_. C'est ici que les utilisateurs rédigent les instructions que l'operator doit suivre.

À côté du champ de saisie se trouvent plusieurs boutons de commande :

* **Prompt Variables** – Ouvre une fenêtre contextuelle dans laquelle vous pouvez saisir des paires clé-valeur utilisées dans l'invite. Les variables s'écrivent entre accolades, par exemple `{invoice_number}` ou `{url}`. Ces valeurs ne s'appliquent qu'à l'invite en cours dans le champ de saisie.
* **Save Prompt** – Enregistre l'invite en cours. Choisissez de l'enregistrer comme :
  * **Organization Prompt** – Modifiable au sein de votre organisation ; inclut à la fois l'invite et les valeurs de variables définies.
  * **Global Prompt** – Partagée entre tous les tenants ; inclut uniquement l'invite et les espaces réservés des variables (aucune valeur n'est enregistrée).
* **Clear Chat** – Efface la conversation en cours avec l'operator, mais laisse l'invite du champ de saisie inchangée. Utile pour réutiliser ou affiner une invite.

Pour des conseils détaillés sur la rédaction d'invites efficaces — y compris la syntaxe, les variables et des exemples — consultez le [**Prompt Writing Guide**](prompt-writing-guide.md).

### **2. Navigation dans la barre latérale**

Utilisez l'icône en haut à gauche pour ouvrir ou fermer la barre latérale. Elle affiche les invites enregistrées, organisées en deux catégories :

* **Organization Prompts** : modifiables et réutilisables au sein de votre organisation.
* **Global Prompts** : partagées entre tous les tenants. Elles ne peuvent pas stocker de variables et ne peuvent être ni modifiées ni supprimées.
  * Une invite globale reste modifiable et supprimable par l'**organisation qui l'a créée**, où elle apparaît sous Organization Prompts.
* **Fonction de recherche :** une barre de recherche en haut de la barre latérale permet de retrouver rapidement des invites enregistrées par nom ou par mot-clé.
* **Référence des icônes :** chaque invite enregistrée dispose d'un ensemble d'icônes d'action
  * **Flèche** – Démarrer l'invite
  * **Stylo** – Modifier l'invite (disponible uniquement pour les invites de votre propre organisation)
  * **Corbeille** – Supprimer l'invite (disponible uniquement pour les invites de votre propre organisation)

### 3. Enregistrer le prompt

Un clic sur le bouton **Save Prompt** ouvre une fenêtre contextuelle dans laquelle vous pouvez enregistrer l'invite en cours pour un usage ultérieur.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Fenêtre contextuelle Save Prompt"><figcaption></figcaption></figure></div>

#### **Champs de la fenêtre contextuelle Save Prompt**

* **Prompt Name :** saisissez un nom pour identifier l'invite.
* **Save Prompt Publicly (case à cocher) :** lorsqu'elle est cochée, l'invite est enregistrée comme **Global Prompt**. Les Global Prompts sont partagées entre tous les tenants et ne peuvent pas stocker de **valeurs** de variables (uniquement des **noms** de variables).
* **Edit Variables :** ouvre la [**fenêtre contextuelle Prompt Variables**](prompt-writing-guide.md#popup-des-variables-de-prompt) pour vérifier ou ajuster les définitions de variables avant l'enregistrement.

**Actions**

* **Cancel :** ferme la fenêtre contextuelle sans enregistrer.
* **Save :** enregistre l'invite avec le nom et le paramètre de visibilité indiqués.

### 4. Commandes d'exécution de l'invite

Lorsqu'une invite est en cours d'exécution, les utilisateurs disposent de plusieurs commandes pour gérer le processus d'exécution ou y intervenir :

* **Pause Prompt :** interrompt temporairement l'exécution en cours. Utile si vous souhaitez observer l'état actuel ou préparer le système pour les étapes suivantes.&#x20;
* **Resume Prompt :** reprend l'exécution à partir du point où elle a été mise en pause. ![](<../../.gitbook/assets/image (3) (1).png>)
* **Cancel Prompt :** arrête complètement l'exécution et réinitialise la session. C'est utile si l'invite doit être abandonnée ou redémarrée en raison d'un comportement incorrect ou d'une modification des données saisies.&#x20;
* **Take Control :** permet à l'utilisateur d'intervenir manuellement en interagissant directement avec le système. C'est utile si l'operator se bloque ou interprète mal une étape. La prise de contrôle **met automatiquement l'invite en pause** et passe en mode manuel jusqu'à ce que vous choisissiez de reprendre ou d'annuler.

### 5. Vue détaillée de l'operator

Une fois qu'une invite est démarrée, un bouton supplémentaire permet de basculer vers une **vue d'exécution détaillée**. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View :** ce bouton vous mène à une vue dédiée qui montre, étape par étape, ce que fait l'operator en temps réel.

Dans la vue détaillée, les utilisateurs peuvent :

* Suivre chaque action effectuée (par exemple, clics, saisies, attentes).
* Voir quelle étape est actuellement active.
* Identifier où surviennent les problèmes lorsque l'invite rencontre des difficultés.
* Utiliser les mêmes actions **Pause**, **Resume**, **Cancel** et **Take Control**.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
