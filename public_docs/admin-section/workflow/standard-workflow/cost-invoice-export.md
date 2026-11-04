# Facture de coût - Export

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Achat Commande Exporter 4"><figcaption></figcaption></figure>

Ce titre indique que la règle est spécifiquement configurée pour gérer les factures de coût et implique une action d'exportation, peut-être pour des rapports, un traitement ultérieur ou une intégration avec d'autres systèmes.

#### Configuration de la règle :

1. **Quand…**
* **Le type de document est Facture** : Cette condition garantit que la règle n'est déclenchée que pour les documents catégorisés comme des factures, maintenant la spécificité du flux de travail pour la gestion des factures.
2. **Et…**
* **Le sous-type de facture est Égal à Facture de coût** : Cela spécifie que la règle s'applique uniquement à ces factures explicitement marquées comme "Factures de coût" dans un champ particulier du document. Cela aide à les distinguer des autres types de factures.
* **Le statut du document est En attente de la deuxième approbation** : La facture doit être dans un statut "En attente de la deuxième approbation". Cela indique que la facture a déjà été approuvée initialement et attend une deuxième, éventuellement finale, révision.

#### Action (Ensuite…):

* **Démarrer l'exportation** : Une fois que la facture répond aux conditions spécifiées (étant une facture de coût et en attente de la deuxième approbation), l'action "Démarrer l'exportation" est exécutée. Cela pourrait impliquer l'envoi des données de la facture à un autre système pour une analyse financière, des rapports ou des objectifs de conformité.

#### Objectif de cette règle :

* **Efficacité du flux de travail** : Cette règle aide à automatiser le traitement des factures de coût en garantissant qu'elles passent par les étapes d'approbation nécessaires sans intervention manuelle, augmentant la vitesse et la précision des opérations financières.
* **Contrôle et conformité** : En exigeant une deuxième approbation, le système applique un mécanisme de contrôle qui garantit que les factures de coût sont examinées en détail, renforçant la surveillance financière.
* **Intégration et rapports** : L'action d'exportation suggère qu'une fois les factures entièrement approuvées, elles peuvent être intégrées dans d'autres systèmes pour un traitement ou une analyse ultérieurs, ce qui est essentiel pour les rapports financiers et les audits.

Ce type de règle est essentiel pour les organisations qui traitent différents types de factures et doivent garantir que chaque type est traité selon des protocoles spécifiques. Cela réduit le risque d'erreurs et garantit la conformité avec les contrôles internes et les réglementations externes.
