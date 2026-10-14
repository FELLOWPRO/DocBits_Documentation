# Données Floues

### **Aperçu**

Les champs de données floues (Fuzzy Data) permettent aux utilisateurs de renseigner des champs associés à partir de correspondances approximatives dans les données maîtres. Ces champs sont identifiés par une **icône bleue** à côté d'eux.

<figure><img src="../../../.gitbook/assets/fuzzy_data_field_icon.png" alt="Icône de champ de données floues"><figcaption></figcaption></figure>

### **Fonctionnalité**

#### **Que font les champs de données floues ?**

* Ils renseignent des champs associés en fonction de leur valeur ou de la saisie.
* Les trois champs standard utilisant les données floues sont :
  * **Purchase Order**
  * **Supplier**
  * **Vendor ID**

#### **Utiliser les champs de données floues**

1. **Sélectionner une commande d'achat**
   *   Cliquer sur l'**icône bleue** à côté du champ Purchase Order ouvre une **fenêtre de sélection**.


       <figure><img src="../../../.gitbook/assets/fuzzy_data_selection_window.png" alt="Fenêtre de sélection des données floues"><figcaption></figcaption></figure>
   * Cette fenêtre contient un tableau avec toutes les commandes d'achat de la **table de consultation des données maîtres**.
   * L'activation de l'option **"Display all columns"** affiche des détails supplémentaires.
   * Sélectionnez une **commande d'achat** et cliquez sur **Proceed** :
     * Si le système trouve une commande d'achat dans le document, il filtre automatiquement dessus.
     * Si aucune correspondance n'est trouvée, vous pouvez **créer des filtres personnalisés** pour trouver la bonne commande d'achat.
     * Plusieurs filtres peuvent être ajoutés ; l'activation de **"Match all filters"** garantit que toutes les conditions doivent être remplies.
     * Options de filtre disponibles :
       * **Smart**
       * **Contains**
       * **Exact**
       * **Starts with**
       * **Ends with**
   * Un bouton à côté de **Proceed** permet de **créer une nouvelle tâche/notification**.
2. **Sélectionner un fournisseur ou un Vendor ID**
   * Le processus est le même que pour les commandes d'achat.
   * La différence est que les champs **Supplier et Vendor ID utilisent la table des données maîtres fournisseurs** au lieu de la table des données maîtres d'en-tête de commande d'achat.

#### **Indication de remplissage du champ**

* Si un champ est renseigné à l'aide des données floues plutôt qu'extrait du document, une **petite icône d'indication ou d'information** apparaît pour signaler que la donnée **n'a pas été extraite du document** mais renseignée à partir des données maîtres.

### **Configuration par l'administrateur**

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}

{% content-ref url="../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md" %}
[fuzzy-data-configuration-with-list-of-values.md](../../../administration-and-setup/setup/document-types/fuzzy-data-configuration-with-list-of-values.md)
{% endcontent-ref %}



{% embed url="https://www.youtube.com/watch?v=vT5HuGjAYV0" %}
