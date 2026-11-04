# Descripteur de structure EDI

L'objectif principal du descripteur de structure est de définir les éléments d'un message EDI de manière logique et organisée, facilitant ainsi la gestion et l'analyse des données. En reflétant avec précision la hiérarchie du message.

### Éléments du descripteur de structure

**N1** - Contient les champs suivants:

* **N1** - Nom ou identifiant de l'entité (par exemple, partie, organisation).
* **N2** - Informations de nom supplémentaires (généralement un nom secondaire pour l'entité).
* **N3** - Informations d'adresse (généralement l'adresse postale).
* **N4** - Emplacement géographique (ville, état, code postal, pays).

**N9** - Contient le champ suivant:

* **N9** - Identifiant de référence (par exemple, numéro de commande d'achat ou numéro de contrôle).
* **Boucles:**
  * **MSG01** - Contient le champ suivant:
    * **MSG01** - Texte de message libre (généralement une note ou une instruction spéciale liée à la transaction).

**IT1** - Contient les champs suivants:

* **IT1** - Identifiant de l'article (par exemple, numéro d'article ou code produit).
* **QTY** - Quantité de l'article dans la transaction (par exemple, unités commandées ou expédiées).
* **TXI** - Informations fiscales (par exemple, taux d'imposition, montants ou classifications pour l'article).
* **REF** - Informations de référence (par exemple, numéro de lot, numéro de série ou autres identifiants liés à l'article).
* **Boucles:**
  * **SAC** - Peut se répéter et contient les champs suivants:
    * **SAC** - Informations de service, promotion, remise ou charge (par exemple, coûts supplémentaires ou remises liés à l'article).
    * **TXI** - Informations fiscales relatives à SAC (par exemple, taxes sur les frais ou remises).

**SAC** - Contient les champs suivants:

* **SAC** - Informations de service, promotion, remise ou charge (peut être utilisé de manière indépendante ou dans la boucle IT1 pour représenter des frais/remises supplémentaires).
* **TXI** - Informations fiscales relatives à SAC (par exemple, taxes sur les frais ou remises).

### Voici un exemple complet d'un descripteur de structure au format JSON:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
