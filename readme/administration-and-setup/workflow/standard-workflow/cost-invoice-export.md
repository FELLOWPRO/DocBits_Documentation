# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Achat Commande Exporter 4"><figcaption></figcaption></figure>

Ce titre indique que la règle est spécifiquement configurée pour gérer les factures de coûts et implique une action d'exportation, possiblement à des fins de reporting, de traitement ultérieur ou d'intégration avec d'autres systèmes.

#### Configuration de la règle :

1. **When…**
   * **Document Type is Invoice** : Cette condition garantit que la règle n'est déclenchée que pour les documents catégorisés comme factures, maintenant la spécificité du flux de travail à la gestion des factures.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice** : Cela précise que la règle ne s'applique qu'aux factures explicitement marquées comme « Cost Invoices » dans un champ particulier du document. Cela aide à les distinguer des autres types de factures.
   * **Document Status is Pending Second Approval** : La facture doit être au statut « Pending Second Approval ». Cela indique que la facture a déjà fait l'objet d'une première approbation et est en attente d'un second examen, possiblement final.

#### Action (Then…) :

* **Start Export** : Une fois que la facture remplit les conditions spécifiées (être une facture de coûts et être en attente de seconde approbation), l'action « Start Export » est exécutée. Cela peut impliquer l'envoi des données de la facture à un autre système à des fins d'analyse financière, de reporting ou de conformité.

#### Objectif de cette règle :

* **Efficacité du flux de travail** : Cette règle aide à automatiser le traitement des factures de coûts en garantissant qu'elles passent par les étapes d'approbation nécessaires sans intervention manuelle, augmentant la vitesse et l'exactitude des opérations financières.
* **Contrôle et conformité** : En exigeant une seconde approbation, le système applique un mécanisme de contrôle qui garantit que les factures de coûts sont minutieusement examinées, renforçant la supervision financière.
* **Intégration et reporting** : L'action d'exportation suggère qu'une fois les factures entièrement approuvées, elles peuvent être intégrées à d'autres systèmes pour un traitement ou une analyse ultérieurs, ce qui est essentiel pour le reporting financier et les audits.

Ce type de règle est vital pour les organisations qui traitent différents types de factures et doivent garantir que chaque type est traité selon des protocoles spécifiques. Elle réduit le risque d'erreurs et garantit la conformité aux contrôles internes et aux réglementations externes.
