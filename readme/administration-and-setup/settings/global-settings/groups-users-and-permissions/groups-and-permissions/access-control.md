# Contrôle d'Accès

## Aperçu

Le Contrôle d'Accès définit, pour un seul **groupe** (rôle), exactement ce que ses membres peuvent faire — à la fois au **niveau du type de document** (quels types de documents ils voient et quelles actions ils peuvent effectuer) et au **niveau du champ** (quels champs individuels ils peuvent lire ou modifier).

Les autorisations sont toujours évaluées **par groupe**. Un utilisateur hérite des autorisations de chaque groupe auquel il appartient.

{% hint style="info" %}
Le Contrôle d'Accès n'est appliqué que lorsque le système **Groupes et Autorisations** est activé (voir [Activer les Autorisations](activating-permissions.md)). **Les administrateurs contournent toujours le Contrôle d'Accès** et peuvent tout voir et tout faire, indépendamment des réglages de cette page.
{% endhint %}

Chaque groupe peut être configuré pour :

* **Accès au document** — si le groupe peut utiliser un type de document.
* **Autorisations d'action** — quelles actions (lister, afficher, modifier, supprimer, mise à jour groupée, approuver) le groupe peut effectuer et *pour quels documents*.
* **Autorisations de champ** — si chaque champ individuel d'un type de document est modifiable, en lecture seule ou masqué.

## Activation

1. Accédez aux **Paramètres**.
2. Sélectionnez **Traitement des Documents**.
3. Sélectionnez **Module.**
4. Activez le **Contrôle d'Accès** en activant le curseur.

<figure><img src="../../../../../.gitbook/assets/Access-Control3_fr.png" alt=""><figcaption></figcaption></figure>

## Ouvrir le Contrôle d'Accès d'un groupe

1. Accédez aux **Paramètres**.
2. Allez dans **Paramètres Globaux**.
3. Sélectionnez **Groupes, Utilisateurs et Autorisations**.
4. Sélectionnez **Groupes et Autorisations**.
5. Pour gérer les autorisations d'un groupe (par exemple PROCUREMENT\_DIRECTOR), cliquez sur les trois points à droite.
6. Sélectionnez **Gérer le Contrôle d'Accès**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Ouvrir le menu de ligne d'un groupe et choisir Gérer le Contrôle d'Accès"><figcaption><p>Sur la page « Groupes et Autorisations », ouvrez le menu <strong>⋮</strong> d'un groupe et choisissez <strong>Gérer le Contrôle d'Accès</strong>.</p></figcaption></figure>

## Comment une autorisation est évaluée

Lorsqu'un utilisateur tente de faire quelque chose avec un document, DocBits vérifie, dans l'ordre :

1. **Le système Groupes et Autorisations est-il activé et l'utilisateur n'est-il pas administrateur ?** S'il est désactivé, ou si l'utilisateur est administrateur → accès complet.
2. **Le type de document est-il activé pour l'un des groupes de l'utilisateur ?** S'il est désactivé → l'utilisateur ne peut ni voir ni utiliser ce type de document.
3. **Quel périmètre d'accès est défini pour l'action ?** (par exemple *Modifier = Owner*). Le périmètre est comparé à la relation de l'utilisateur avec *ce document précis* — est-il le propriétaire, le destinataire, les deux ou aucun ?
4. **Quelle autorisation de champ s'applique ?** Même lorsqu'un utilisateur peut ouvrir un document, certains champs peuvent rester masqués ou verrouillés.

## Autorisations au niveau du type de document

Chaque ligne de la matrice est un type de document (Invoice, Credit Note, Purchase Order, …).

La première colonne est un interrupteur **Activé / Désactivé**. Désactivez-le et le groupe ne pourra pas du tout utiliser ce type de document — il disparaît de son tableau de bord. Activez-le et les sept colonnes d'action deviennent modifiables.

| Action | Détermine si le groupe peut… |
|--------|------------------------------|
| **Lister** | voir le type de document dans la liste du tableau de bord. |
| **Afficher** | ouvrir un document et voir ses détails. |
| **Modifier** | modifier les valeurs des champs d'un document. |
| **Supprimer** | supprimer un document. |
| **Mise à jour groupée** | appliquer une mise à jour groupée à plusieurs documents à la fois. |
| **Première Approbation** | accorder l'approbation de premier niveau. |
| **Deuxième Approbation** | accorder l'approbation de deuxième niveau. |

### Périmètres d'accès

Chaque colonne d'action est une liste déroulante. La valeur choisie répond à la question *« pour quels documents le groupe peut-il faire cela ? »*. Les noms des périmètres apparaissent en anglais dans l'interface :

| Périmètre | Qui est autorisé | Effet sur un document |
|-----------|------------------|------------------------|
| **No Access** | Personne dans le groupe. | L'action est bloquée pour tout le groupe — le bouton est masqué ou désactivé. |
| **Everyone** | Chaque membre du groupe. | Tout membre du groupe peut effectuer l'action sur **n'importe quel** document de ce type. |
| **Owner** | Uniquement l'utilisateur qui a **créé / téléversé** le document. | L'action ne fonctionne que sur les documents que l'utilisateur a lui-même téléversés. |
| **Assignee** | Uniquement l'utilisateur (ou le groupe) auquel le document est **attribué**. | L'action ne fonctionne que sur les documents attribués à l'utilisateur ou à un groupe dont il fait partie. |
| **Owner & Assignee** | Le propriétaire **ou** le destinataire. | L'action fonctionne si l'utilisateur est *soit* celui qui a téléversé *soit* le destinataire. |

{% hint style="info" %}
**Owner** et **Assignee** dépendent de la *relation entre l'utilisateur et chaque document individuel* ; deux membres d'un même groupe peuvent donc avoir des droits différents sur la même facture — voir l'exemple concret ci-dessous.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Matrice de Contrôle d'Accès d'un groupe"><figcaption><p>La matrice des autorisations par type de document. Ici, le type <strong>Invoice</strong> est activé et ses actions ont différents périmètres d'accès ; les autres types sont désactivés.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Liste déroulante des périmètres d'accès"><figcaption><p>Chaque colonne d'action propose les mêmes cinq périmètres d'accès.</p></figcaption></figure>

### L'approbation nécessite aussi Modifier

Approuver un document déclenche **deux actions** en arrière-plan : DocBits **enregistre** d'abord le document, puis le fait passer au statut approuvé. L'étape d'enregistrement nécessite l'autorisation **Modifier** ; les deux autorisations sont donc liées.

Un utilisateur à qui l'on accorde uniquement **Première Approbation** ou **Deuxième Approbation** — mais *pas* **Modifier** — rencontre une erreur d'autorisation lors de l'étape d'enregistrement et ne peut pas approuver le document.

{% hint style="warning" %}
Chaque fois que vous accordez **Première Approbation** ou **Deuxième Approbation**, accordez également **Modifier** (et **Afficher**) pour le même type de document. Une autorisation d'approbation seule ne suffit pas.
{% endhint %}

## Autorisations au niveau du champ

Cliquez sur une ligne de type de document pour ouvrir le panneau **Autorisations de Champ** en dessous. Les champs sont organisés en onglets (par exemple *Colonnes de tableau*, *Détails de la facture*, *Détails de paiement*, *Taxes et montants*). Chaque champ a son propre niveau d'accès :

| Niveau | Effet sur le champ |
|--------|--------------------|
| **Lecture/Écriture** | Le champ est visible **et** modifiable. |
| **Lecture seule** | Le champ est visible mais **ne peut pas être modifié** (grisé). |
| **Approbation** | Le champ peut être modifié, mais la modification doit passer par un **flux d'approbation** avant d'être appliquée. |
| **Aucun accès** | Le champ est **entièrement masqué** — l'utilisateur ne le voit jamais. |

{% hint style="info" %}
Les règles de champ s'appliquent de la même manière à **tous** les membres du groupe — elles ne dépendent pas du propriétaire/destinataire. Utilisez-les pour masquer ou verrouiller des champs sensibles (par exemple une remise ou un montant total) pour un groupe entier.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Panneau Autorisations de Champ"><figcaption><p>Le panneau « Autorisations de Champ » pour le type Invoice. <code>CUSTOMER_DISCOUNT</code> est masqué (Aucun accès) tandis que les autres champs restent en Lecture/Écriture.</p></figcaption></figure>

## Exemple concret : ce que le Contrôle d'Accès fait sur une facture réelle

Supposons que vous créiez un groupe **AP_CLERK** pour vos comptables fournisseurs et que vous configuriez le type de document **Invoice** ainsi :

**Autorisations de type de document pour Invoice**

| Action | Périmètre |
|--------|-----------|
| Activé | ✅ Oui |
| Lister | Everyone |
| Afficher | Everyone |
| Modifier | Owner & Assignee |
| Supprimer | No Access |
| Mise à jour groupée | No Access |
| Première Approbation | Assignee |
| Deuxième Approbation | No Access |

**Autorisations de champ pour Invoice**

| Champ | Niveau |
|-------|--------|
| `TOTAL_AMOUNT` | Lecture seule |
| `CUSTOMER_DISCOUNT` | Aucun accès |
| *(tous les autres champs)* | Lecture/Écriture |

Suivez maintenant un document précis — la facture **INV-4711**, que **Maria a téléversée** et qui est **attribuée à Maria**. Maria et son collègue Tom font tous deux partie du groupe **AP_CLERK**.

**Maria (propriétaire *et* destinataire d'INV-4711) :**

* ✅ Voit INV-4711 dans la liste du tableau de bord *(Lister = Everyone)*.
* ✅ L'ouvre *(Afficher = Everyone)*.
* ✅ Modifie le nom du fournisseur et les lignes *(Modifier = Owner & Assignee — elle est la propriétaire)*.
* 🔒 Voit `TOTAL_AMOUNT`, mais le champ est grisé et elle ne peut pas le modifier *(Lecture seule)*.
* 🚫 Ne voit jamais le champ `CUSTOMER_DISCOUNT` *(Aucun accès)*.
* 🚫 Le bouton **Supprimer** est masqué *(Supprimer = No Access — personne dans le groupe ne peut supprimer)*.
* ✅ Peut accorder la **première approbation** *(Première Approbation = Assignee — elle est la destinataire)*.

**Tom (même groupe, mais il n'a *pas* téléversé INV-4711 et elle ne lui est *pas* attribuée) :**

* ✅ La voit dans la liste et ✅ l'ouvre *(Lister et Afficher = Everyone)*.
* 🚫 Ne peut rien modifier — le document s'ouvre en **lecture seule** *(Modifier = Owner & Assignee — Tom n'est ni l'un ni l'autre)*.
* 🔒 / 🚫 Voit exactement la même visibilité de champs que Maria : `TOTAL_AMOUNT` verrouillé, `CUSTOMER_DISCOUNT` masqué *(les règles de champ s'appliquent à tout le groupe)*.
* 🚫 Ne peut pas accorder la première approbation *(Première Approbation = Assignee — pas Tom)*.
* 🚫 Ne peut pas supprimer *(No Access)*.

**Ce que montre cet exemple**

* **Everyone** ouvre un document à tous les membres du groupe ; **Owner / Assignee** restreint une action aux personnes liées à ce document précis.
* **No Access** supprime une action (Supprimer) ou masque un champ (`CUSTOMER_DISCOUNT`) pour tout le groupe.
* **Lecture seule** garde un champ visible pour référence (`TOTAL_AMOUNT`) mais empêche les modifications.
* Deux personnes d'un **même groupe** peuvent avoir des **droits différents sur la même facture**, uniquement en fonction de qui l'a téléversée et à qui elle est attribuée.
