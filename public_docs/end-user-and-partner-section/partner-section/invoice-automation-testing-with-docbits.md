# Automatisation des Tests de Factures avec DocBits

## Aperçu

Ce document décrit le plan de test pour l'automatisation des factures utilisant DocBits avec Infor LN ou M3. Il inclut des détails sur les cas de test, la préparation des tests, les étapes d'exécution et les processus de support.

## Cas de Test

| ID | Cas de Test                                                                       | Description                                                                                                                                                                                                                     | Statut   |
| -- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1  | Factures de Coût                                                                  | Les factures sans bon de commande sont traitées avec succès dans DocBits et exportées vers LN en tant que « facture de coût ».                                                                                                  | À TESTER |
| 2  | Facture Liée à un Bon de Commande avec Correspondance Parfaite                    | Les factures liées à un bon de commande sont traitées avec succès dans DocBits avec une correspondance parfaite entre la facture et le bon de commande, car le numéro d'article, la quantité et le prix unitaire correspondent. | À TESTER |
| 3  | Factures Liées à un Bon de Commande avec Quantité Différente                      | Les factures liées à un bon de commande sont traitées dans DocBits mais dans le module de correspondance des bons de commande, nous avons un écart sur la quantité.                                                             | À TESTER |
| 4  | Factures Liées à un Bon de Commande avec Prix Unitaire Différent                  | Les factures liées à un bon de commande sont traitées dans DocBits mais dans le module de correspondance des bons de commande, nous avons un écart sur le prix unitaire.                                                        | À TESTER |
| 5  | Factures Liées à un Bon de Commande avec Numéro d'Article Différent ou Inexistant | Les factures liées à un bon de commande sont traitées dans DocBits mais dans le module de correspondance des bons de commande, nous avons un écart ou un numéro d'article inexistant.                                           | À TESTER |
| 6  | Factures Liées à un Bon de Commande avec un Écart dans la Tolérance               | Les factures liées à un bon de commande sont traitées dans DocBits mais dans le module de correspondance des bons de commande, nous avons un écart sur la quantité ou le prix unitaire, mais cela reste dans la tolérance.      | À TESTER |
| 7  | Notes de Crédit                                                                   | Les notes de crédit sont traitées avec succès dans DocBits et exportées vers LN. Clarifiez si les montants doivent être exportés avec un signe positif ou négatif.                                                              | À TESTER |

## Plan de Test avec le Client

### 1. Mise en Place

* **Réunion Initiale** : Planifiez une réunion de lancement avec le client pour expliquer le processus de test et les objectifs.
* **Accès et Permissions** : Assurez-vous que le client dispose de tous les accès nécessaires à DocBits et Infor LN ou M3 à des fins de test.

### 2. Préparation des Tests

* **Formation** : Fournissez une formation complète à l'équipe du client sur l'utilisation de DocBits pour le traitement des factures.
* **Documentation** : Partagez une documentation détaillée sur les procédures de test, y compris les résultats attendus pour chaque cas de test.

### 3. Exécution des Cas de Test

* **Environnement de Test** : Mettez en place un environnement de test qui reproduit le système de production du client aussi fidèlement que possible.
* **Tests Étape par Étape** : Travaillez avec le client pour exécuter chaque cas de test, en veillant à ce qu'il comprenne chaque étape :
  * Traitez les factures via DocBits.
  * Vérifiez la sortie dans le module de correspondance des bons de commande.
  * Vérifiez les résultats d'exportation dans LN ou M3.

### 4. Résolution des Problèmes

* **Suivi** : Utilisez un système de suivi (comme Jira ou une simple feuille de calcul) pour enregistrer tout problème ou écart survenant pendant les tests.
* **Support** : Fournissez un support immédiat pour résoudre les problèmes et clarifier tout doute.

### 5. Vérification et Retour d'Information

* **Vérification** : Après chaque cas de test, vérifiez les résultats avec le client pour garantir l'exactitude.
* **Boucle de Retour d'Information** : Collectez les retours du client sur le processus et les améliorations nécessaires.

### 6. Finalisation

* **Documentation des Résultats** : Documentez les résultats de chaque cas de test et fournissez un rapport récapitulatif au client.
* **Réunion de Revue** : Organisez une réunion de revue pour discuter des résultats des tests et des étapes supplémentaires nécessaires avant le passage en production.

### 7. Préparation au Lancement

* **Rafraîchissement de la Formation** : Proposez une session de formation de rafraîchissement si nécessaire.
* **Plan de Support** : Développez un plan de support pour la phase de lancement initial afin d'assurer une transition en douceur.
