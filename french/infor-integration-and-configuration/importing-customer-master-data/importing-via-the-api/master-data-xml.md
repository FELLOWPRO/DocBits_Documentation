---
description: Comment importer des données maîtres dans un jeu de données de recherche depuis un fichier XML
---

# Importer des Données Maîtres depuis XML

En plus des imports de BOD, DocBits peut lire des données maîtres depuis **n'importe quel fichier XML** vers le jeu de données de recherche de votre choix. Vous indiquez dans quel jeu écrire et depuis quel XPath chaque colonne doit être lue : le XML n'a donc pas du tout besoin de suivre un format BOD.

Utilisez cela pour les données maîtres qui n'arrivent pas sous forme de BOD — listes de prix, centres de coûts, attributs d'article, tout ce que votre ERP peut exporter en XML.

## Deux façons d'envoyer le XML

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Quand l'utiliser |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Vous avez les données sous forme de **fichier XML** et voulez le téléverser. |
| `/master_data_lookup/xml/import_xml_data` | Vous voulez **coller le XML** dans la requête. Contrairement aux endpoints de BOD, celui-ci accepte le XML en texte brut — sans enveloppe JSON. |

Les deux sont décrits ci-dessous. Les étapes 1 et 2 sont identiques dans les deux cas.

## Avant de commencer

Il vous faudra :

* **Une API key.** Voir [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) si vous n'en avez pas encore.
* **Le XML** — sous forme de fichier ou de contenu que vous pouvez coller.
* **Un type de données** — le nom du jeu de données de recherche dans lequel écrire.
* **Des mappages de champs** — quel XPath remplit quelle colonne.
* **Votre Org ID**, depuis **Settings → Integration & SSO**, dans la section **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Instructions pas à pas

### 1. Ouvrir le lien de l'API

Ouvrez l'interface de test de l'API pour l'environnement et la région avec lesquels vous travaillez :

* [Sandbox API (Europe)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (États-Unis)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europe)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (États-Unis)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Ces endpoints se trouvent sous **master data lookup** et non sous **import**, plus bas dans la page.

{% hint style="info" %}
Utilisez la région dans laquelle votre organisation est hébergée — la même région que celle par laquelle vous vous connectez à DocBits. Les environnements européen et américain sont séparés : un import envoyé dans la mauvaise région n'apparaîtra pas dans votre organisation.
{% endhint %}

### 2. S'autoriser

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

L'autorisation fonctionne exactement comme pour les imports de BOD : cliquez sur l'**icône de cadenas**, collez votre **Org ID** dans **X-ORG-ID**, collez votre API key dans **X-API-KEY**, et cliquez sur **Authorize** pour chacune.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Remplir les champs

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Cliquez sur **Try it out**, puis remplissez le formulaire.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Champ | |
| --- | --- |
| **data\_type** | Obligatoire. Le jeu de données de recherche dans lequel écrire. Il est automatiquement mis en minuscules : `PriceList` et `pricelist` sont donc le même jeu. |
| **field\_mappings** | Obligatoire. Un objet JSON associant chaque colonne au XPath depuis lequel elle est lue. Voir ci-dessous. |
| **file** | Obligatoire sur `import_xml_file`. Cliquez sur **Choose file** et sélectionnez votre XML. |
| **xml** | Obligatoire sur `import_xml_data` à la place du fichier — collez-y le XML en texte brut. |
| **org\_id** | Votre Org ID — la même valeur que celle saisie dans **X-ORG-ID** à l'étape 2. |
| **sub\_org\_id** | Nécessaire uniquement si vous importez dans une sous-organisation précise. |

#### Mappages de champs

`field_mappings` est un objet JSON comportant une entrée par colonne. Contrairement aux imports de BOD, où les noms sont fixés à `custom_field_1` … `custom_field_5`, c'est vous qui les choisissez ici :

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

Les noms à gauche deviennent les colonnes du jeu de données et vous appartiennent. Les valeurs à droite doivent correspondre à la structure du XML que vous téléversez — dans l'exemple ci-dessus, `//Item/ID` récupère l'élément `<ID>` à l'intérieur de chaque `<Item>`. Les deux côtés sont indépendants : le mappage ci-dessus lit `<UnitPrice>` vers une colonne nommée `Price`.

{% hint style="warning" %}
Seuls les XPath **mal formés** sont rejetés, avec un `400` nommant le champ. Un XPath valide mais qui ne correspond à rien dans votre XML passe silencieusement et laisse simplement cette colonne vide — une faute de frappe dans un chemin ressemble donc à un import qui a fonctionné mais a perdu une colonne. Si c'est le chemin `ID` qui ne correspond à rien, l'import échoue à la place et signale que la colonne `ID` manque pour cet enregistrement.
{% endhint %}

{% hint style="warning" %}
**L'une des colonnes doit s'appeler `ID`.** C'est elle qui identifie un enregistrement : réimporter les mêmes données met à jour la ligne portant cet ID au lieu d'ajouter un doublon. Le nom n'est pas sensible à la casse, donc `ID`, `Id` et `id` fonctionnent tous, mais un nom comme `ItemID` ne compte pas — la requête est rejetée avec `ID_FIELD_IS_MISSING` et rien n'est écrit.
{% endhint %}

{% hint style="warning" %}
**Une requête importe un enregistrement.** Chaque XPath est lu une fois : si votre XML contient plusieurs éléments, seule la première correspondance de chacun est utilisée. Pour charger une liste, envoyez une requête par enregistrement, ou utilisez plutôt un import CSV.
{% endhint %}

#### Choisir un type de données

`data_type` est la clé du jeu de données dans lequel vous écrivez. Il est mis en minuscules et détouré des espaces : `Items` et `items` sont donc le même jeu. Tout nom qui n'est pas déjà pris crée un jeu qui vous est propre — `items_example`, `cost_centres`, `price_list` — et y réimporter le met à jour.

{% hint style="danger" %}
Certains noms ne sont pas libres : ce sont les propres tables de données maîtres de DocBits, et importer dans l'une d'elles écrit directement dedans.

| Nom | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Rejetés avec `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Acceptés, et ils écrasent de vraies données maîtres.** Ne les utilisez que si c'est bien votre intention. |

Pour tout le reste, choisissez un nom qui vous est propre.
{% endhint %}

{% hint style="warning" %}
Vérifiez vers quel environnement et quelle organisation vous pointez avant d'exécuter. Un import écrit directement dans les données maîtres de cette organisation.
{% endhint %}

### 4. Exécuter

Avant d'exécuter, vérifiez la liste déroulante **Servers** en bas du formulaire.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Cliquez sur **Execute**. Un import réussi renvoie :

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

Contrairement aux imports de BOD, ces endpoints signalent les problèmes avec un véritable statut d'erreur plutôt qu'avec un `200` portant `"success": false` — un **400** signifie que la requête a été rejetée et que rien n'a été écrit.

### 5. Vérifier que les données sont arrivées

* Dans DocBits, allez dans **Settings → Document Processing → Lookup Master Data**.
* Sélectionnez **Imported** à gauche, puis ouvrez l'onglet correspondant à votre type de données.
* Les colonnes sont les noms que vous avez utilisés à gauche dans `field_mappings`.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
