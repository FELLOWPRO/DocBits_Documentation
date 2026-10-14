# Configuration d'export pour le portail fournisseur

<figure><img src="../../../.gitbook/assets/supplier_export_configuration.png" alt="Supplier Export Configuration"><figcaption><p>Page de configuration d'export fournisseur</p></figcaption></figure>

## Vue d'ensemble

Le fichier de configuration d'export est un composant essentiel du portail fournisseur ; il définit la manière dont les données sont mappées entre le portail fournisseur et le système ERP. Cette configuration garantit que les données sont transférées et synchronisées avec précision entre les systèmes, permettant des opérations fluides et efficaces.

## Structure du fichier de configuration

Le fichier de configuration d'export est structuré sous la forme d'un objet JSON contenant plusieurs mappages. Chaque mappage est associé à un programme spécifique du système ERP et définit les actions à effectuer, les champs à mapper ainsi que les conditions éventuelles à appliquer.

## Composants clés

### 1. Programme

* **Définition** : Spécifie le programme ERP auquel s'applique le mappage.
* **Exemple** : `"program": "CRS620MI"`

### 2. Actions

* **Définition** : Définit les actions qui peuvent être effectuées, telles que l'ajout ou la mise à jour d'enregistrements.
*   **Exemple** :

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

### 3. Mappage

• Définition : Spécifie le mappage entre les champs du système ERP et les champs du portail fournisseur.

• Composants :

• erp\_field\_name : Le nom du champ dans le système ERP.

• value\_field\_name : Le nom de champ correspondant dans le portail fournisseur.

• value : Une valeur statique à utiliser si aucun champ correspondant n'existe dans le portail fournisseur.

• if\_conditions : Conditions facultatives qui déterminent la valeur selon certains critères.

• Exemple :

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

### 4. Logique conditionnelle (if\_conditions)

• Définition : Spécifie les conditions qui doivent être remplies pour qu'une valeur particulière soit utilisée.

• Composants :

• field\_name : Le nom du champ dans le portail fournisseur qui est évalué.

• field\_value : La valeur qui déclenche la condition.

• then\_value : La valeur à utiliser si la condition est remplie.

• Exemple :

```json
{
    "erp_field_name": "SUTY",
    "value": "0",
    "if_conditions": [{
        "field_name": "supplier_group",
        "field_value": "FRT",
        "then_value": "5"
    }]
}
```

### 5. Boucles (loop\_on)

• Définition : Définit les sections où la configuration doit itérer sur une liste d'éléments, comme les détails d'adresse ou de référence.

• Exemple :

```json
"loop_on": "address_details"
```

### 6. Champs calculés (value\_field\_calculated)

• Définition : Spécifie les champs qui doivent être calculés au moment de l'exécution, comme la génération de la date actuelle.

• Exemple :

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

### 7. Mappages de champs avec listes (mapping\_field\_name et mapping\_list)

• Définition : Mappe des valeurs spécifiques du portail fournisseur vers les valeurs correspondantes du système ERP en fonction d'une liste prédéfinie.

• Composants :

• mapping\_field\_name : Le champ qui détermine le mappage.

• mapping\_list : Un dictionnaire qui traduit les valeurs du portail fournisseur vers le système ERP.

• Exemple :

```json
{
    "erp_field_name": "RFID",
    "mapping_field_name": "reference_type",
    "mapping_list": {
        "10": "PURCHASING",
        "15": "DLVRY PHN#",
        "20": "COA",
        "25": "QA",
        "30": "FINANCE",
        "35": "SALES"
    }
}
```

## Détail d'un exemple de configuration

### Ajout et mise à jour de fournisseur (CRS620MI)

• Programme : CRS620MI

• Actions :

• Ajouter un fournisseur : AddSupplier

• Mettre à jour un fournisseur : UpdSupplier

• Champs de mappage :

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Les champs supplémentaires incluent des valeurs statiques et des mappages conditionnels.

### Détails d'adresse (CRS620MI)

• Boucle sur : _**address\_details**_

• Actions :

• Ajouter une adresse : AddAddress

• Mettre à jour une adresse : AddAddress

• Champs de mappage :

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Les champs supplémentaires incluent des champs calculés comme now() pour la date actuelle.

### Détails de référence (CRS620MI)

• Boucle sur : _**reference\_details**_

• Actions :

• Ajouter une référence fournisseur : AddSupplierRef

• Mettre à jour une référence fournisseur : AddSupplierRef

• Champs de mappage :

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID est mappé à l'aide d'une liste pour traduire des types tels que « PURCHASING », « QA » et « FINANCE ».

## Utilisation de la configuration d'export

### 1. Téléversement du fichier de configuration

#### 1. Accéder à la configuration d'export :

• Accédez à la section Configuration d'export depuis le menu principal.

#### 2. Téléverser le fichier de configuration :

• Cliquez sur les sections Fichier de mappage ION ou Fichier de mappage IDM pour téléverser le fichier de configuration correspondant.

#### 3. Enregistrer la configuration :

• Après le téléversement, cliquez sur le bouton Enregistrer pour appliquer la configuration.

### 2. Utilisation des modèles par défaut

• Cliquez sur le bouton Utiliser le modèle par défaut si vous souhaitez revenir au modèle de configuration par défaut fourni par le système.

### 3. Formatage du JSON

• Utilisez le bouton Formater pour formater automatiquement le code JSON afin d'en améliorer la lisibilité.

## Conclusion

Ce fichier de configuration est essentiel pour garantir que les données entre le portail fournisseur et le système ERP sont correctement mappées et synchronisées. En comprenant la structure et les composants clés, les administrateurs peuvent gérer et personnaliser efficacement le processus d'export afin de répondre à leurs exigences métier spécifiques.

## Exemple complet&#x20;

```json
[{
    "program": "CRS620MI",
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "value_field_name": "supplier_number"
    }, {
        "erp_field_name": "SUNM",
        "value_field_name": "name"
    }, {
        "erp_field_name": "SUTY",
        "value": "0",
        "if_conditions": [{
            "field_name": "supplier_group",
            "field_value": "FRT",
            "then_value": "5"
        }]
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }, {
        "erp_field_name": "DTFM",
        "value_field_name": "date_format"
    }, {
        "erp_field_name": "ORTY",
        "value": "F20"
    }, {
        "erp_field_name": "DT4T",
        "value": "1"
    }, {
        "erp_field_name": "DTCD",
        "value": "2"
    }, {
        "erp_field_name": "CUCD",
        "value_field_name": "currency"
    }, {
        "erp_field_name": "TINO",
        "value_field_name": "tax_id"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "supplier_phone"
    }, {
        "erp_field_name": "CRTP",
        "value": "1"
    }, {
        "erp_field_name": "ATPR",
        "value": "1"
    }, {
        "erp_field_name": "SUCL",
        "value_field_name": "supplier_group"
    }, {
        "erp_field_name": "LNCD",
        "value_field_name": "language"
    }, {
        "erp_field_name": "CONO",
        "value": "781_DDD"
    }, {
        "erp_field_name": "TEDL",
        "value": "FOB"
    }, {
        "erp_field_name": "TEPY",
        "value_field_name": "payment_term"
    }, {
        "erp_field_name": "TEPA",
        "value": "001"
    }, {
        "erp_field_name": "PYME",
        "value": "CRP"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "address_details",
    "actions": {
        "add": "AddAddress",
        "update": "AddAddress"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "ADTE",
        "value_field_name": "address_type"
    }, {
        "erp_field_name": "ADID",
        "value_field_name": "address_type",
        "if_conditions": [{
            "field_name": "address_type",
            "field_value": "10",
            "then_value": ""
        }]
    }, {
        "erp_field_name": "STDT",
        "value_field_calculated": "now()"
    }, {
        "erp_field_name": "ADR1",
        "value_field_name": "address"
    }, {
        "erp_field_name": "TOWN",
        "value_field_name": "city"
    }, {
        "erp_field_name": "ECAR",
        "value_field_name": "state"
    }, {
        "erp_field_name": "PONO",
        "value_field_name": "postal_code"
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "reference_details",
    "actions": {
        "add": "AddSupplierRef",
        "update": "AddSupplierRef"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "RFTY",
        "value_field_name": "reference_type"
    }, {
        "erp_field_name": "RFID",
        "mapping_field_name": "reference_type",
        "mapping_list": {
            "10": "PURCHASING",
            "15": "DLVRY PHN#",
            "20": "COA",
            "25": "QA",
            "30": "FINANCE",
            "35": "SALES"
        }
    }, {
        "erp_field_name": "YRE1",
        "value_field_name": "reference_name"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "telephone_no"
    }, {
        "erp_field_name": "EMAL",
        "value_field_name": "email_address"
    }]
}]
```
