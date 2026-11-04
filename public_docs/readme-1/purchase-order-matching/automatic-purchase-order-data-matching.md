# Correspondance automatique des données de bons de commande

Docbits est un système avancé conçu pour automatiser la correspondance des données des bons de commande (BC) avec les documents de facturation entrants. Cet outil est spécifiquement conçu pour la gestion efficace et le traitement des données de facturation au sein des systèmes ERP. Cette documentation explique les bases de la correspondance automatique à travers Docbits et définit les règles spécifiques nécessaires pour une correspondance réussie.

## **Principes fondamentaux de la correspondance automatique dans Docbits**

**Extraction des données :** Docbits commence le processus en extrayant les données pertinentes des documents de facturation numérisés. Typiquement, ces données incluent les numéros d'article, les quantités et les prix unitaires de chaque ligne de facture. La précision de cette extraction est cruciale, car elle constitue la base du processus de correspondance ultérieur.

**Comparaison avec les données des BC :** Les données extraites sont comparées aux informations correspondantes dans les bons de commande stockés. Docbits vérifie si les numéros d'article, les quantités et les prix correspondent à ceux des BC. Pour une correspondance réussie, les données des factures doivent correspondre aux données des bons de commande, en tenant compte des seuils de tolérance définis.

**Correspondance automatique :** Sur la base des résultats de la comparaison, Docbits effectue la correspondance. Le système vérifie si les critères de correspondance se situent dans les limites de tolérance définies. Si ces critères sont respectés, la correspondance est considérée comme réussie.

**Rapports :** Après avoir terminé le processus de correspondance, Docbits génère des rapports qui montrent l'état des correspondances. Ces rapports informent sur les factures correspondantes avec succès et identifient celles présentant des divergences.

## **Définition des règles de correspondance**

**Numéro d'article :** Le numéro d'article sur la facture doit correspondre exactement au numéro d'article dans le bon de commande. Aucune tolérance n'est accordée pour les écarts dans les numéros d'article.

**Quantités :** La quantité de biens livrés sur la facture peut varier dans une plage de tolérance prédéfinie. Typiquement, une tolérance de ±5% pourrait être acceptable pour tenir compte des différences mineures dans les quantités de livraison.

**Prix :** Les écarts de prix sont tolérables jusqu'à un seuil défini. Une tolérance courante pourrait être de ±2% du prix pour accepter de légères différences dans les déclarations de prix résultant de différences d'arrondi ou de fluctuations de change.

## **État de la correspondance :**

* **Correspondance complète :** Tous les points de données (numéro d'article, quantité et prix) se situent dans les limites de tolérance définies.
* **Correspondance partielle :** Un ou plusieurs points de données dévient en dehors des limites de tolérance, mais les écarts sont minimes et nécessitent une révision manuelle.
* **Aucune correspondance :** Des écarts significatifs dans un ou plusieurs points de données nécessitant une correction immédiate ou une enquête plus approfondie.

La définition précise de ces règles et le paramétrage des limites de tolérance sont cruciaux pour l'efficacité de la correspondance automatique et la réduction des interventions manuelles. Docbits permet une configuration flexible de ces paramètres pour répondre aux besoins des différentes entreprises et industries.
