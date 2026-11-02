# Configuration de l'exportation pour le portail des fournisseurs pour M3

### Overview

Le fichier de configuration d'exportation est un composant crucial dans le portail fournisseur, définissant comment les données sont mappées entre le portail fournisseur et le système ERP. Cette configuration garantit que les données sont transférées et synchronisées avec précision entre les systèmes, permettant des opérations fluides et efficaces.

### Structure of the Configuration File

Le fichier de configuration d'exportation est structuré comme un objet JSON qui contient plusieurs mappages. Chaque mappage est associé à un programme spécifique dans le système ERP et définit les actions à effectuer, les champs à mapper et toutes les conditions à appliquer.

### Key Components

#### 1. Program

* **Definition**: Spécifie le programme ERP auquel le mappage s'applique.
* **Example**: `"program": "CRS620MI"`

#### 2. Actions

* **Definition**: Définit les actions qui peuvent être effectuées, telles que l'ajout ou la mise à jour d'enregistrements.
*   **Example**:

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

#### 3. Mapping

• Definition: Spécifie le mappage entre les champs dans le système ERP et les champs dans le portail fournisseur.

• Components:

• erp\_field\_name: Le nom du champ dans le système ERP.

• value\_field\_name: Le nom du champ correspondant dans le portail fournisseur.

• value: Une valeur statique à utiliser si aucun champ correspondant n'existe dans le portail fournisseur.

• if\_conditions: Conditions optionnelles qui déterminent la valeur en fonction de certains critères.

• Example:

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

#### 4. Conditional Logic (if\_conditions)

• Definition: Spécifie les conditions qui doivent être remplies pour qu'une valeur particulière soit utilisée.

• Components:

• field\_name: Le nom du champ dans le portail fournisseur qui est évalué.

• field\_value: La valeur qui déclenche la condition.

• then\_value: La valeur à utiliser si la condition est remplie.

• Example:

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

#### 5. Loops (loop\_on)

• Definition: Définit les sections où la configuration doit itérer sur une liste d'éléments, tels que les détails d'adresse ou de référence.

• Example:

```json
"loop_on": "address_details"
```

#### 6. Calculated Fields (value\_field\_calculated)

• Definition: Spécifie les champs qui doivent être calculés à l'exécution, comme la génération de la date actuelle.

• Example:

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

#### 7. Field Mappings with Lists (mapping\_field\_name and mapping\_list)

• Definition: Mappe des valeurs spécifiques du portail fournisseur aux valeurs correspondantes dans le système ERP en fonction d'une liste prédéfinie.

• Components:

• mapping\_field\_name: Le champ qui détermine le mappage.

• mapping\_list: Un dictionnaire qui traduit les valeurs du portail fournisseur vers le système ERP.

• Example:

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

### Example Configuration Breakdown

#### Supplier Addition and Update (CRS620MI)

• Program: CRS620MI

• Actions:

• Add Supplier: AddSupplier

• Update Supplier: UpdSupplier

• Mapping Fields:

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Additional fields include static values and conditional mappings.

#### Address Details (CRS620MI)

• Loop On: _**address\_details**_

• Actions:

• Add Address: AddAddress

• Update Address: AddAddress

• Mapping Fields:

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Additional fields include calculated fields like now() for the current date.

#### Reference Details (CRS620MI)

• Loop On: _**reference\_details**_

• Actions:

• Add Supplier Reference: AddSupplierRef

• Update Supplier Reference: AddSupplierRef

• Mapping Fields:

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID is mapped using a list to translate types like “PURCHASING”, “QA”, and “FINANCE”.

### Using the Export Configuration

#### 1. Uploading the Configuration File

**1. Navigate to Export Configuration:**

• Allez à la section Configuration d'exportation depuis le menu principal.

**2. Upload the Configuration File:**

• Cliquez sur les sections Fichier de mappage ION ou Fichier de mappage IDM pour télécharger le fichier de configuration respectif.

**3. Save the Configuration:**

• Après le téléchargement, cliquez sur le bouton Enregistrer pour appliquer la configuration.

#### 2. Using Default Templates

• Cliquez sur le bouton Utiliser le modèle par défaut si vous souhaitez revenir au modèle de configuration par défaut fourni par le système.

#### 3. Formatting the JSON

• Utilisez le bouton Format pour formater automatiquement le code JSON pour une meilleure lisibilité.

### Conclusion

Ce fichier de configuration est essentiel pour garantir que les données entre le portail fournisseur et le système ERP sont correctement mappées et synchronisées. En comprenant la structure et les composants clés, les administrateurs peuvent gérer et personnaliser efficacement le processus d'exportation pour répondre à leurs besoins commerciaux spécifiques.

### Full Example

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
