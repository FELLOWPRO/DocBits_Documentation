# Description du flux de travail : Déclencheur d'exportation conditionnelle



<figure><img src="../../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Paramètres Workflow"><figcaption></figcaption></figure>

Ce flux de travail décrit les conditions dans lesquelles un processus d'exportation doit être initié. Il garantit que seuls les documents répondant à tous les critères spécifiés sont traités pour l'exportation, renforçant l'intégrité des données et l'alignement sur les règles métier.

### When :

* Un document du système est évalué pour son éligibilité à l'exportation.

### Logique :

1. **Vérification du type de document**
   * Le document doit être d'un certain type (par ex. « Invoice » ou « Receipt »). Spécifiez le type de document qui qualifie pour le processus d'exportation.
2. **Vérification du statut**
   * Le statut actuel du document doit répondre à des critères prédéfinis (par ex. « Approved » ou « Ready for Export ») indiquant qu'il est prêt pour un traitement ultérieur.
3. **Conditions contextuelles**
   * Des vérifications supplémentaires sont effectuées pour garantir que les détails du document correspondent à des exigences spécifiques. Ces vérifications peuvent impliquer la validation d'informations dans les confirmations de commande ou les commandes d'achat. Spécifiez les conditions particulières à remplir. Par exemple :
     * Tous les articles répertoriés dans la confirmation de commande correspondent à ceux de la commande d'achat.
     * Le montant total de la confirmation de commande correspond au montant total de la commande d'achat.
     * Les dates de livraison spécifiées dans la confirmation de commande correspondent à celles de la commande d'achat.

### Then :

#### Action :

* **Initier l'exportation**
  * Si toutes les conditions ci-dessus sont satisfaites, le système démarre automatiquement le processus d'exportation pour le document.
  * Cela peut impliquer la génération d'un fichier d'exportation, l'envoi de données à un système externe ou le déclenchement d'un flux de travail dans une autre application.

#### Exemple de mise en œuvre :

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
