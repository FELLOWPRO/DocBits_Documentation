# Recherche de données de référence

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

La **Recherche de données de référence** (barre latérale : **Lookup Master Data**) vous permet de consulter et de gérer les données de référence que DocBits utilise pour valider les données extraites des documents par rapport à votre système ERP. Elle est essentielle pour un PO matching précis, la validation des fournisseurs et la saisie automatique des champs. Ouvrez-la depuis **Paramètres → Traitement des documents → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Recherche de données de référence"><figcaption><p>Page Recherche de données de référence : sources de données et tableau de données</p></figcaption></figure>

## Sources de données

Le panneau de gauche répertorie quatre catégories de sources de données :

| Source | Description |
|--------|-------------|
| **BOD Input Data** | Données reçues via des messages Infor BOD (Business Object Document). |
| **ERP API Data** | Données récupérées directement depuis votre système ERP via une API. Cliquez sur l'icône en forme d'engrenage pour configurer la connexion API. |
| **Imported** | Données importées manuellement (par exemple via un téléversement CSV). Cliquez sur l'icône **+** pour ajouter de nouvelles données. |
| **DocBits Master Data** | Données de référence internes gérées au sein de DocBits. |

## Tableau de données

La sélection d'une source de données ouvre ses données dans un tableau consultable et triable à droite :

* **Onglets** : chaque onglet correspond à un type de données de référence (par exemple Fournisseur, Bon de commande, Article).
* **Recherche** : filtrez par colonne (**Search by column**) ou recherchez par texte (**Search String**).
* **Actions** : mettre à jour les libellés de colonnes, masquer les colonnes vides, mettre à jour les alias ou télécharger les données au format CSV.
* **Pagination** : parcourez de grands ensembles de données à l'aide des commandes de page.

Les tableaux Fournisseur et Bon de commande comprennent des colonnes telles que ID fournisseur, Nom du fournisseur, Adresse, Bank Id, Numéro de BC, ID article, Description, Quantité, Prix unitaire, Montant total, Devise et Statut, ainsi que les champs personnalisés.

## Paramètres

Cliquez sur **Settings** (icône en forme d'engrenage) en bas à gauche du panneau des sources de données pour ouvrir les paramètres des données de référence.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Paramètres de la Recherche de données de référence"><figcaption><p>Paramètres Supplier BOD et suppression des bons de commande</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Activé** : un même fournisseur peut avoir plusieurs éléments `<FinancialParty>` dans le BOD (souvent en raison de plusieurs IBAN ou comptes financiers). Toutes les entrées `<FinancialParty>` sont extraites et enregistrées dans la table des fournisseurs, ce qui permet de stocker plusieurs attributs financiers.
* **Désactivé** : seul le dernier élément `<FinancialParty>` trouvé pour le fournisseur est extrait. Les attributs financiers antérieurs (par exemple des IBAN supplémentaires) sont ignorés et seules les données de la dernière occurrence sont enregistrées.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** : choisissez quand les bons de commande clôturés doivent être supprimés. Après la période sélectionnée, les enregistrements sont supprimés automatiquement.

{% hint style="info" %}
Pour savoir comment charger des données de référence dans DocBits, consultez [Importer des données de référence](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
