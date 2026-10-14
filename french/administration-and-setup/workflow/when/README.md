

Les cartes de cette catégorie dans le sélecteur **Add Card** du Workflow Builder :

<figure><img src="../../../.gitbook/assets/workflow_cards_when.png" alt="Workflow Builder card category"><figcaption><p>Les cartes de cette catégorie.</p></figcaption></figure>
---
description: Configuration du déclencheur Quand dans les workflows DocBits
---

# Quand

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKwAT37pCkZRziNLyWMsL%252Fimage.png%3Falt%3Dmedia%26token%3Db95d040f-e9e6-496d-97cd-d2c8f1c30d60\&width=768\&dpr=4\&quality=100\&sign=c323483b\&sv=2)

#### Comprendre le "Quand" dans les configurations de flux de travail

**But du "Quand"**

* La section "Quand" dans une configuration de flux de travail définit les conditions de déclenchement qui initient une action de flux de travail particulière. Ces conditions sont basées sur des critères spécifiés liés aux attributs du document ou aux activités des utilisateurs dans le système ERP.

**Comment ça fonctionne**

* Dans votre interface, "Quand" semble être un point de départ où les utilisateurs peuvent sélectionner différentes cartes de déclenchement. Chaque carte spécifie les conditions dans lesquelles les actions ultérieures (définies dans la section "Et") seront exécutées.

**Cartes de condition de type de document**

* Les cartes avec l'icône de document affichée dans la capture d'écran sont des variations des conditions de "Type de document", qui sont utilisées pour déclencher des flux de travail en fonction du type de document traité. Voici un aperçu de chaque type de carte de condition montré :
  * **Type de document (Opérateur) un de (Type)** : Cette carte déclenche une action lorsque le type d'un document correspond à l'un des types spécifiés dans une liste. L'opérateur peut inclure des options telles que "est" ou "n'est pas", permettant des conditions inclusives ou exclusives.
  * **Type de document (Opérateur) (Type)** : Cette variante plus simple déclenche en fonction d'une seule condition de type de document. Elle vérifierait généralement si le type de document "est" ou "n'est pas" un type spécifique, sans l'option de sélectionner parmi plusieurs types.
  *

**Celery Beat**

* La carte avec l'icône d'horloge dans la capture d'écran est une condition "Celery Beat", qui est utilisée pour déclencher des flux de travail en fonction de la date et de l'heure.

#### Configuration d'une carte de déclenchement "Quand"

1. **Sélection du type de condition** : Les utilisateurs commencent par sélectionner un type de condition pertinent pour le flux de travail qu'ils souhaitent automatiser. Dans ce cas, les types de documents sont au centre de l'attention.
2. **Définition de l'opérateur** : Les utilisateurs doivent décider de l'opérateur logique, tel que "est" ou "n'est pas", qui définit la base pour comparer les types de documents réels par rapport aux conditions définies.
3. **Spécification des types de documents** : Selon la carte, les utilisateurs peuvent sélectionner un ou plusieurs types de documents qui déclencheront le flux de travail lorsque des documents de ces types sont traités.
4. **Finalisation du déclenchement** : Une fois la condition définie, elle devient la base pour déclencher des actions spécifiques définies dans le flux de travail. Si un document répond à la condition définie, les actions définies seront automatiquement initiées.

#### Application pratique

En pratique, ces cartes de déclenchement sont cruciales pour automatiser des processus tels que les approbations, les notifications ou toute procédure dépendant du type de document traité. Par exemple, si un type de document "est" une "Facture" et correspond aux conditions définies dans la carte "Quand", le flux de travail pourrait automatiquement acheminer le document pour le traitement des paiements.

Cette configuration garantit que les flux de travail sont non seulement efficaces, mais également adaptés aux besoins opérationnels spécifiques de l'organisation, réduisant la surveillance manuelle et accélérant les processus de traitement des documents.

En résumé, la partie "Quand" de votre configuration de flux de travail consiste à préparer le terrain pour des actions automatisées basées sur des conditions spécifiques et prédéfinies. C'est un outil puissant pour garantir que votre système ERP réagisse de manière dynamique aux besoins de l'entreprise, améliorant à la fois la productivité et la précision dans la gestion des documents.
