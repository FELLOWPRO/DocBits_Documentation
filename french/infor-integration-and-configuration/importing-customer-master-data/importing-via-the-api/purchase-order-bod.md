---
description: Comment importer un Purchase Order BOD dans DocBits manuellement via l'API
---

# Importer des Commandes d'Achat (Purchase Order BOD)

Les commandes d'achat arrivent normalement dans DocBits automatiquement via votre flux de données ION. Cette page décrit comment envoyer un **Purchase Order BOD** manuellement — utile lorsque vous voulez réimporter une commande, charger un lot qui n'est jamais arrivé, ou tester un nouveau mappage avant d'activer le flux automatique.

## Deux façons d'envoyer le même BOD

Il y a deux endpoints, et ils font la même chose. La seule différence tient à la manière dont vous transmettez le BOD :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-endpoints.png)

| Endpoint | Quand l'utiliser |
| --- | --- |
| `/import/purchase_order_bod` | Vous avez le BOD sous forme de **fichier XML** et voulez le téléverser. |
| `/import/purchase_order_bod_xml` | Vous voulez envoyer le **contenu XML** dans la requête plutôt qu'un fichier. Le BOD doit être enveloppé dans du JSON, ce qui convient à un XML court ou à un autre système appelant l'API — pour un BOD complet à la main, téléversez le fichier. |

Les deux sont décrits ci-dessous. Les étapes 1 et 2 sont identiques dans les deux cas.

## Avant de commencer

Il vous faudra :

* **Une API key.** Voir [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) si vous n'en avez pas encore.
* **Le BOD** — un fichier XML `SyncPurchaseOrder`, ou son contenu.
* **Votre Org ID**, si vous importez dans une organisation autre que celle à laquelle appartient votre clé.

Pour trouver l'Org ID, allez dans **Settings → Integration & SSO** et ouvrez la section **ID**. Cliquez sur l'icône de copie à côté du champ.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** affiche la sous-organisation sélectionnée dans l'en-tête. Avec **CROSS** sélectionné — la vue couvrant toutes les sous-organisations — il affiche la même valeur que **Org ID**, ce qui explique que les deux champs coïncident dans la capture ci-dessus. Basculez d'abord vers une sous-organisation précise si vous avez besoin de son ID.

Si vous n'importez pas dans une sous-organisation précise, laissez le champ `sub_org_id` vide.
{% endhint %}

## Instructions pas à pas

### 1. Ouvrir le lien de l'API

Ouvrez l'interface de test de l'API pour l'environnement et la région avec lesquels vous travaillez :

* [Sandbox API (Europe)](https://eu.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Sandbox API (États-Unis)](https://us.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Europe)](https://eu.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (États-Unis)](https://us.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)

Dépliez l'endpoint souhaité en cliquant dessus.

{% hint style="info" %}
Utilisez la région dans laquelle votre organisation est hébergée — la même région que celle par laquelle vous vous connectez à DocBits. Les environnements européen et américain sont séparés : un import envoyé dans la mauvaise région n'apparaîtra pas dans votre organisation.

Les adresses sans préfixe de région — `api.docbits.com` et `sandbox.api.docbits.com` — pointent vers l'Europe. Vous les rencontrerez dans de la documentation plus ancienne et dans des configurations existantes ; il s'agit du même environnement que les adresses `eu.` ci-dessus.
{% endhint %}

### 2. S'autoriser

Tout ce qui se trouve sous **import** est verrouillé tant que vous ne vous êtes pas autorisé. Deux éléments sont à renseigner : votre organisation et votre API key.

* Cliquez sur l'**icône de cadenas** à droite de l'endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-swagger-lock.png)

* La boîte de dialogue **Available authorizations** s'ouvre avec deux entrées.
* Collez votre **Org ID** dans **X-ORG-ID** et cliquez sur **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

* L'entrée affiche maintenant **Authorized** et masque la valeur.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Descendez jusqu'à **X-API-KEY**, collez votre API key et cliquez sur **Authorize**. Dans DocBits, vous la trouverez sous **Settings → Integration & SSO**, dans la section **API Key**, ou vous pouvez [créer une nouvelle clé](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Cliquez sur **Close**.

{% hint style="info" %}
Collez la clé seule — n'écrivez pas `Bearer` devant. Les deux autorisations restent en place jusqu'à ce que vous rechargiez la page ou cliquiez sur **Logout**.
{% endhint %}

### 3. Remplir les champs

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-po.png)

Cliquez sur **Try it out**, puis remplissez le formulaire de l'endpoint que vous avez choisi.

#### Téléverser un fichier — `/import/purchase_order_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-form.png)

| Champ | |
| --- | --- |
| **file** | Obligatoire. Cliquez sur **Choose file** et sélectionnez votre fichier XML `SyncPurchaseOrder`. |
| **org\_id** | Votre Org ID — la même valeur que celle saisie dans **X-ORG-ID** à l'étape 2. La renseigner ici aussi rend la requête explicite quant à l'organisation dans laquelle elle écrit. Ce doit être une organisation à laquelle votre API key a accès ; toute autre est refusée. |
| **sub\_org\_id** | Nécessaire uniquement si vous travaillez avec des sous-organisations. Laissez vide sinon. |
| **custom\_fields\_mapping** | Facultatif. Lit des champs d'en-tête supplémentaires du BOD vers les champs personnalisés de la commande. Voir [Mappages de champs personnalisés](#mappages-de-champs-personnalises) ci-dessous. |
| **custom\_line\_fields\_mapping** | Facultatif. Idem, pour des champs supplémentaires sur les lignes de commande. |

{% hint style="warning" %}
**`string` est une valeur, pas un espace réservé.** Swagger remplit les champs facultatifs avec le mot `string`, et il est envoyé tel quel si vous le laissez — un import avec `org_id` à `string` échouera.

Pour chaque champ facultatif que vous ne voulez pas utiliser, videz le champ. Le vider active la case **Send empty value** en dessous, que vous pouvez alors cocher. Dans la capture ci-dessus, cela a été fait pour `sub_org_id`.
{% endhint %}

#### Mappages de champs personnalisés

Les deux champs de mappage attendent un objet JSON. Le **nom à gauche doit être l'un des champs personnalisés propres à DocBits** — de `custom_field_1` à `custom_field_5` pour les commandes d'achat. Tout autre nom est ignoré sans avertissement : une faute de frappe ici ressemble donc exactement à un mappage qui n'a pas fonctionné.

La valeur à droite est le XPath depuis lequel lire. Écrivez-le sans préfixes d'espace de noms — DocBits les ajoute lui-même :

```json
{"custom_field_2": "//PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Les mappages de lignes utilisent les mêmes noms `custom_field_1` … `custom_field_5`, mais leurs XPath sont lus **relativement à chaque ligne de commande** et commencent donc par `./` :

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Coller le XML — `/import/purchase_order_bod_xml`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-xml-form.png)

Cet endpoint n'accepte pas le BOD sous forme de simple collage. Le champ **xml** est un objet, prérempli avec :

```json
{
  "xml": "string"
}
```

Remplacez `string` par le contenu de votre BOD, en conservant les guillemets et les accolades qui l'entourent :

```json
{
  "xml": "<SyncPurchaseOrder ...>...</SyncPurchaseOrder>"
}
```

{% hint style="warning" %}
Le BOD se trouve à l'intérieur d'une chaîne JSON : chaque guillemet double du XML doit donc être échappé en `\"` — et un BOD en est plein (`releaseID="9.2"`, `xmlns="..."`). Si le résultat n'est pas du JSON valide, la requête échoue avec un **422** et rien n'est importé.

Pour un vrai BOD, c'est fastidieux à faire à la main : préférez donc le **téléversement du fichier**. Cet endpoint est le meilleur choix lorsque le XML est court, ou lorsqu'un autre système construit la requête et peut encoder le JSON lui-même.
{% endhint %}

Les champs `org_id`, `sub_org_id` et `custom_fields_mapping` fonctionnent exactement comme ci-dessus. Cet endpoint n'a pas de champ pour les mappages de lignes.

{% hint style="warning" %}
Vérifiez vers quel environnement et quelle organisation vous pointez avant d'exécuter. Un import écrit directement dans les données maîtres de cette organisation.
{% endhint %}

### 4. Exécuter

Avant d'exécuter, vérifiez la liste déroulante **Servers** en bas du formulaire. Elle détermine l'environnement vers lequel la requête est réellement envoyée, et elle peut différer de la page que vous avez ouverte.

Cliquez sur **Execute**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

**Si vous avez téléversé un fichier**, la réponse est :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-response.png)

```json
{
  "success": true,
  "message": "BOD processing started in the background."
}
```

{% hint style="info" %}
**Cela signifie que le fichier a été accepté, pas que l'import est terminé.** Les fichiers de commandes d'achat téléversés sont traités en arrière-plan afin que les commandes volumineuses ne bloquent pas le reste du système. Patientez un instant, puis vérifiez le résultat comme décrit ci-dessous.
{% endhint %}

**Si vous avez collé le XML**, l'import s'exécute immédiatement et la réponse est `"BOD processed successfully."` — lorsque vous la voyez, les données sont déjà en place.

Si quelque chose n'allait pas dans la requête, vous obtenez `"success": false` accompagné d'un message décrivant le problème. Les causes les plus fréquentes sont un contenu qui n'est pas un BOD `SyncPurchaseOrder` et un Org ID auquel votre API key n'a pas accès.

### 5. Vérifier que les données sont arrivées

* Dans DocBits, allez dans **Settings → Document Processing → Lookup Master Data**.
* Sélectionnez **BOD Input Data** à gauche, puis ouvrez l'onglet **Purchase Order**.
* Recherchez le numéro de commande de votre BOD.

<!-- SCREENSHOT F: Lookup Master Data with BOD Input Data selected and the Purchase Order tab open -->

Si la commande est listée, l'import a fonctionné et la commande d'achat est disponible pour le PO matching.

{% hint style="info" %}
DocBits décide quoi faire du BOD en lisant le type qu'il contient, et non d'après l'endpoint d'import utilisé. Si vous envoyez ici un supplier BOD par erreur, il est importé en tant que données fournisseur plutôt que rejeté — vérifiez donc que l'onglet dans lequel vous retrouvez les données est bien celui attendu.
{% endhint %}
