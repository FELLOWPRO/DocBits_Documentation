# Types de Document

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Document Types Explained: Create, Configure & Assign Processing Settings
{% endembed %}

<figure><img src="../../../../.gitbook/assets/image (78).png" alt="Document Types"><figcaption><p>Page Document Types</p></figcaption></figure>

## Aperçu

La page Document Types répertorie tous les types de documents reconnus et traités par DocBits. Elle est divisée en deux sections :

* **Default Document Types** : types préconfigurés fournis par DocBits (Invoice, Credit Note, Delivery Note, Order Confirmation, Contract, ZUGFeRD, etc.). Ils ne peuvent pas être supprimés.
* **Custom Document Types** : types que vous créez pour vos besoins métier spécifiques. Ils peuvent être modifiés et supprimés.

## Contrôles par type de document

Chaque carte de type de document affiche :

| Contrôle                         | Description                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| **Activate**                     | Interrupteur pour activer ou désactiver ce type de document pour le traitement.      |
| **Extraction**                   | Interrupteur pour activer ou désactiver l'extraction de données par IA pour ce type. |
| **Settings** (icône d'engrenage) | Ouvre des options de configuration supplémentaires pour le type de document.         |

## Onglets de configuration

Sous chaque type de document, vous avez accès aux onglets de configuration suivants :

| Onglet                 | Description                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| **Labels**             | Gère les libellés d'affichage et les traductions du type de document.                                 |
| **Edit layout**        | Modifie l'affichage du document dans la vue de validation, y compris la position des champs.          |
| **Document Sub Types** | Configure les sous-catégories de ce type de document (p. ex. différents formats de facture).          |
| **Table columns**      | Personnalise les colonnes de données qui apparaissent dans le tableau des lignes.                     |
| **Fields**             | Gère les champs de données extraits du document (ajout, modification ou suppression de champs).       |
| **Model Training**     | Configure et entraîne le modèle d'IA utilisé pour reconnaître et extraire les données.                |
| **Regex**              | Définit des expressions régulières pour l'extraction de données basée sur des motifs.                 |
| **Scripts**            | Permet d'écrire des scripts de traitement personnalisés exécutés pendant le traitement des documents. |
| **E-Doc**              | Configure les standards de documents électroniques (XRechnung, ZUGFeRD, EDI, FatturaPA).              |

## Custom Validation Rules

Ouvrez un type de document et sélectionnez **Custom Validation Rules** pour gérer ses propres règles de validation. Pour réutiliser une règle existante sans la recréer, suivez [Duplicate a Custom Validation Rule](duplicate-a-custom-validation-rule.md). Le guide explique le nom de la règle, la clé de la règle et les contrôles de confirmation.

## Créer un type de document personnalisé

1. Faites défiler la page jusqu'à la section **Custom Document Types**.
2. Cliquez sur **+ New**.
3. Saisissez un nom pour le nouveau type de document.
4. Configurez les champs, la mise en page et les paramètres d'extraction selon vos besoins.

{% hint style="info" %}
Consultez [Setup Document Type](../../../setup/document-types/) pour des instructions de configuration détaillées.
{% endhint %}
