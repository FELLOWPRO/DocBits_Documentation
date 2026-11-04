# Correspondance Automatique des Données de Bon de Commande

Docbits est un système avancé conçu pour automatiser la correspondance des données de bon de commande (PO) avec les documents de facture entrants. Cet outil est spécifiquement conçu pour une gestion et un traitement efficaces des données de facturation au sein des systèmes ERP. Cette documentation explique les bases de la correspondance automatique via Docbits et définit les règles spécifiques requises pour une correspondance réussie.

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice_3.svg" alt="DocBits Achat Commande Facture 3"><figcaption></figcaption></figure>

## **Principes Fondamentaux de la Correspondance Automatique dans Docbits**

**Extraction de Données :** Docbits commence le processus en extrayant les données pertinentes des documents de facture numérisés. En général, ces données incluent les numéros d'article, les quantités et les prix unitaires de chaque ligne de facture. La précision de cette extraction est cruciale, car elle constitue la base du processus de correspondance ultérieur.

**Comparaison avec les Données de PO :** Les données extraites sont comparées avec les informations correspondantes dans les bons de commande stockés. Docbits vérifie si les numéros d'article, les quantités et les prix correspondent à ceux des PO. Pour une correspondance réussie, les données des factures doivent correspondre aux données des bons de commande, en tenant compte des seuils de tolérance définis.

**Correspondance Automatique :** Sur la base des résultats de la comparaison, Docbits effectue la correspondance. Le système vérifie si les critères de correspondance se situent dans les limites de tolérance définies. Si ces critères sont remplis, la correspondance est considérée comme réussie.

**Rapport :** Après avoir terminé le processus de correspondance, Docbits génère des rapports qui montrent l'état des correspondances. Ces rapports informent sur les factures correspondantes avec succès et identifient celles présentant des écarts.

## **Définition des Règles de Correspondance**

**Numéro d'Article :** Le numéro d'article sur la facture doit correspondre exactement au numéro d'article dans le bon de commande. Il n'y a pas de tolérance pour les écarts dans les numéros d'article.

**Quantités :** La quantité de marchandises livrées sur la facture peut varier dans une plage de tolérance prédéfinie. En général, une tolérance de ±5% peut être acceptable pour tenir compte des différences mineures dans les quantités de livraison.

**Prix :** Les écarts de prix sont tolérables jusqu'à un seuil défini. Une tolérance courante peut être de ±2% du prix pour accepter de légères différences dans les déclarations de prix résultant de différences d'arrondi ou de fluctuations monétaires.

## **Statut de Correspondance :**

* **Correspondance Complète :** Tous les points de données (numéro d'article, quantité et prix) sont dans les limites de tolérance définies.
* **Correspondance Partielle :** Un ou plusieurs points de données dévient en dehors des limites de tolérance, mais les écarts sont minimes et nécessitent un examen manuel.
* **Aucune Correspondance :** Écarts significatifs dans un ou plusieurs points de données nécessitant une correction immédiate ou une enquête plus approfondie.

La définition précise de ces règles et la fixation des limites de tolérance sont cruciales pour l'efficacité de la correspondance automatique et la réduction des interventions manuelles. Docbits permet une configuration flexible de ces paramètres pour répondre aux besoins de diverses entreprises et industries.
