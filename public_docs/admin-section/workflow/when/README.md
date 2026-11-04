# Quand

<figure><img src="../../../.gitbook/assets/docbits_workflow_4.png" alt="DocBits Workflow 4"><figcaption></figcaption></figure>

#### Comprendre le "Quand" dans les Configurations de Workflow

**But du "Quand"**

* La section "Quand" dans une configuration de workflow définit les conditions de déclenchement qui initient une action de workflow particulière. Ces conditions sont basées sur des critères spécifiés liés aux attributs du document ou aux activités des utilisateurs dans le système ERP.

**Comment Ça Marche**

* Dans votre interface, le "Quand" semble être un point de départ où les utilisateurs peuvent sélectionner différentes cartes de déclenchement. Chaque carte spécifie les conditions dans lesquelles les actions ultérieures (définies dans une autre section de la configuration du workflow, probablement étiquetée "Action") seront exécutées.

**Cartes de Conditions de Type de Document**

* Les cartes affichées dans la capture d'écran sont des variations des conditions de "Type de Document", qui sont utilisées pour déclencher des workflows en fonction du type de document en cours de traitement. Voici un aperçu de chaque type de carte de condition montré :
* **Type de document (Opérateur) un de (Type)** : Cette carte déclenche une action lorsque le type d'un document correspond à l'un des types spécifiés dans une liste. L'opérateur peut inclure des options comme "est" ou "n'est pas", permettant des conditions inclusives ou exclusives.
* **Type de document (Opérateur) (Type)** : Cette variante plus simple se déclenche en fonction d'une seule condition de type de document. Elle vérifierait généralement si le type de document "est" ou "n'est pas" un type spécifique, sans l'option de sélectionner parmi plusieurs types.

#### Configuration d'une Carte de Déclenchement "Quand"

1. **Sélection du Type de Condition** : Les utilisateurs commencent par sélectionner un type de condition pertinent pour le workflow qu'ils souhaitent automatiser. Dans ce cas, les types de documents sont au centre de l'attention.
2. **Définition de l'Opérateur** : Les utilisateurs doivent décider de l'opérateur logique, tel que "est" ou "n'est pas", qui établit la base pour comparer les types de documents réels par rapport aux conditions définies.
3. **Spécification des Types de Document** : Selon la carte, les utilisateurs peuvent sélectionner un ou plusieurs types de documents qui déclencheront le workflow lorsque des documents de ces types sont traités.
4. **Finalisation du Déclenchement** : Une fois que la condition est configurée, elle devient la base pour déclencher des actions spécifiques définies dans le workflow. Si un document répond à la condition définie, les actions définies seront automatiquement initiées.

#### Application Pratique

En pratique, ces cartes de déclenchement sont cruciales pour automatiser des processus tels que les approbations, les notifications, ou toute procédure dépendant du type de document traité. Par exemple, si un type de document "est" une "Facture," et qu'il correspond aux conditions définies dans la carte "Quand," le workflow pourrait automatiquement acheminer le document pour le traitement des paiements.

Cette configuration garantit que les workflows sont non seulement efficaces, mais aussi adaptés aux besoins opérationnels spécifiques de l'organisation, réduisant la supervision manuelle et accélérant les processus de traitement des documents.

En résumé, la partie "Quand" de votre configuration de workflow consiste à préparer le terrain pour des actions automatisées basées sur des conditions spécifiques et prédéfinies. C'est un outil puissant pour garantir que votre système ERP réagisse de manière dynamique aux besoins de l'entreprise, améliorant à la fois la productivité et la précision dans la gestion des documents.
