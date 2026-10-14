# Privilèges d'administration

Le rôle d'un administrateur est essentiel pour gérer les systèmes informatiques, les réseaux et les plateformes numériques au sein d'une organisation. Un administrateur dispose de permissions et de responsabilités étendues qui lui permettent de contrôler différents aspects de l'infrastructure technique et de garantir qu'elle fonctionne de manière efficace et sécurisée. Voici quelques-unes des principales responsabilités d'un administrateur :

* **Gestion des utilisateurs :** les administrateurs gèrent les comptes utilisateurs, les droits d'accès et les permissions. Ils créent de nouveaux comptes utilisateurs, leur attribuent les permissions nécessaires et gèrent le contrôle d'accès afin de garantir que seuls les utilisateurs autorisés peuvent accéder à certaines ressources.
* **Sécurité :** les administrateurs sont responsables de la sécurité des systèmes informatiques afin de les protéger contre la perte de données et les accès non autorisés.
* **Dépannage et assistance :** l'administrateur est souvent le premier interlocuteur en cas de problème technique. Il aide les utilisateurs à diagnostiquer et à résoudre les problèmes et veille au bon fonctionnement du système.

Au-delà de ces responsabilités, les administrateurs sont également chargés de gérer des paramètres sensibles et de s'assurer que les systèmes respectent les exigences de conformité et les meilleures pratiques en matière de sécurité de l'information. Cela comprend la gestion des données sensibles, la configuration des contrôles d'accès et des permissions, ainsi que la surveillance et l'analyse des journaux système afin d'identifier et de traiter les risques de sécurité potentiels.

## Admin vs System Admin

DocBits propose deux rôles d'administrateur : **Admin** et **System Admin**. Leurs noms se ressemblent, mais ils remplissent des fonctions différentes. Voici l'essentiel, en quelques mots.

### Admin — une personne qui gère votre organisation

Un **Admin** est une personne réelle de votre équipe autorisée à gérer DocBits. Les Admins peuvent :

* Ouvrir toutes les sections des **Paramètres** et modifier le fonctionnement de votre organisation.
* Ajouter de nouveaux utilisateurs, les modifier, les activer ou les désactiver, et décider qui d'autre devient Admin.
* Configurer les groupes, les permissions, les intégrations et les flux de travail.

Vous pouvez avoir **autant d'Admins que nécessaire**, et vous pouvez accorder ou retirer le rôle d'Admin à n'importe quel utilisateur à tout moment. La plupart des administrateurs de votre équipe sont de ce type.

### System Admin — le compte que DocBits utilise pour agir de lui-même

Un **System Admin** est **un compte spécial unique par organisation** que DocBits utilise pour les actions qui se produisent **automatiquement, sans qu'une personne clique sur un bouton** — par exemple lorsque des documents sont importés depuis un e-mail, exportés vers un autre système ou transmis en arrière-plan par un service connecté.

Considérez-le comme le compte « robot » de l'organisation. Lorsque le système fait quelque chose de lui-même, il le fait **en tant que System Admin**, de sorte que cette activité automatique soit facile à reconnaître et ne se confonde pas avec le travail de vos collaborateurs réels.

Un System Admin se distingue de trois manières :

* **C'est toujours aussi un Admin.** Choisir System Admin accorde automatiquement à ce compte l'ensemble des droits d'Admin.
* **Il n'y en a qu'un seul par organisation.** Une fois qu'un System Admin existe, vous ne pouvez désigner aucun autre utilisateur comme System Admin.
* **Il se définit uniquement à la création de l'utilisateur.** Vous le décidez au moment où vous ajoutez l'utilisateur. Il **ne peut pas être activé ni désactivé par la suite**.

> **Recommandation :** créez un compte dédié à cet usage — par exemple `system@your-company.com` — et désignez-le comme System Admin. Ainsi, toute action effectuée automatiquement par DocBits apparaît clairement comme celle du **System Admin** dans vos journaux et l'historique de vos documents, séparément de vos utilisateurs réels.

### En un coup d'œil

| | Admin | System Admin |
|---|---|---|
| Accès complet à la gestion de l'organisation | Oui | Oui |
| Nombre possible | Autant que nécessaire | Un seul |
| Modifiable après la création de l'utilisateur | Oui, à tout moment | Non, défini uniquement à la création |
| Utilisé pour les actions automatiques, en arrière-plan | Non | Oui |
| Dispose toujours des droits d'Admin | — | Oui |

## Meilleures pratiques de sécurité

La sécurité est un aspect essentiel de toute organisation, en particulier lorsqu'il s'agit de gérer les comptes utilisateurs et les droits d'accès. Voici quelques meilleures pratiques pour maintenir un protocole de gestion des utilisateurs sécurisé :

* **Mises à jour régulières des mots de passe :** encouragez les utilisateurs à mettre à jour régulièrement leurs mots de passe pour préserver la sécurité de leurs comptes. Établissez des règles de complexité des mots de passe et exigez l'utilisation de mots de passe forts combinant lettres, chiffres et caractères spéciaux.
* **Surveiller les actions des administrateurs :** mettez en place des mécanismes pour surveiller les activités des administrateurs afin de détecter toute activité suspecte ou inhabituelle. Enregistrez toutes les actions des administrateurs, y compris l'accès à des données ou des paramètres sensibles, pour garantir la responsabilité et identifier les éventuelles failles de sécurité.
* **Limiter le nombre d'administrateurs :** réduisez au minimum le nombre d'administrateurs et n'accordez de privilèges administratifs qu'à ceux qui en ont réellement besoin. En limitant le nombre d'administrateurs, vous réduisez le risque de failles de sécurité et facilitez la gestion et la surveillance des comptes utilisateurs.
* **Authentification à deux facteurs (2FA) :** mettez en place une authentification à deux facteurs pour les comptes administrateurs afin de renforcer encore la sécurité. Cela ajoute une étape de sécurité supplémentaire qui garantit que, même en cas de compromission d'un mot de passe, un attaquant ne puisse pas obtenir d'accès non autorisé au compte.
* **Audits de sécurité réguliers :** réalisez des contrôles et des audits de sécurité réguliers afin d'identifier et de corriger les failles ou les vulnérabilités potentielles. Vérifiez les droits d'accès et les permissions des comptes utilisateurs pour vous assurer qu'ils correspondent aux exigences actuelles et aux meilleures pratiques.
* **Formation et sensibilisation :** formez régulièrement les employés et les administrateurs aux meilleures pratiques de sécurité et sensibilisez-les aux attaques de phishing et autres menaces informatiques. Faites-leur prendre conscience de l'importance de la sécurité et encouragez-les à signaler toute activité suspecte.

En appliquant ces meilleures pratiques, les organisations peuvent renforcer la sécurité de leur protocole de gestion des utilisateurs et réduire le risque de failles de sécurité et de perte de données. Il est important de considérer la sécurité comme un processus continu et de procéder à des mises à jour et des ajustements réguliers afin de suivre l'évolution constante des menaces et des exigences de sécurité.
