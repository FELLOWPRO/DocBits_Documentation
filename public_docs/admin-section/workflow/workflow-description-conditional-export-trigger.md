# Exemple de flux de travail : Déclencheur d'exportation conditionnel



<figure><img src="../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Paramètres Workflow"><figcaption></figcaption></figure>

Ce flux de travail décrit les conditions dans lesquelles un processus d'exportation doit être initié. Il garantit que seuls les documents répondant à tous les critères spécifiés sont traités pour l'exportation, améliorant ainsi l'intégrité des données et l'alignement avec les règles métier.

### Quand :

* Un document dans le système est évalué pour déterminer son admissibilité à l'exportation.

### Logique :

1. **Vérification du type de document**
* Le document doit être d'un certain type (par exemple, "Facture" ou "Reçu"). Spécifiez le type de document qui est admissible au processus d'exportation.
2. **Vérification du statut**
* Le statut actuel du document doit répondre à des critères prédéfinis (par exemple, "Approuvé" ou "Prêt pour l'exportation"), indiquant qu'il est prêt pour un traitement ultérieur.
3. **Conditions contextuelles**
* Des vérifications supplémentaires sont effectuées pour garantir que les détails du document correspondent à des exigences spécifiques. Ces vérifications peuvent impliquer la vérification des informations dans les confirmations de commande ou les bons de commande. Spécifiez les conditions particulières qui doivent être remplies. Par exemple :
* Tous les articles répertoriés dans la confirmation de commande correspondent à ceux du bon de commande.
* Le montant total dans la confirmation de commande correspond au montant total dans le bon de commande.
* Les dates de livraison spécifiées dans la confirmation de commande correspondent à celles du bon de commande.

### Ensuite :

#### Action :

* **Démarrer l'exportation**
* Si toutes les conditions ci-dessus sont satisfaites, le système lance automatiquement le processus d'exportation pour le document.
* Cela peut impliquer la génération d'un fichier d'exportation, l'envoi de données à un système externe ou le déclenchement d'un flux de travail dans une autre application.

#### Exemple d'implémentation :
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

