---
description: >-
Explorez le flux de travail étape par étape pour la commande de matériaux, la réception de marchandises et le traitement des factures avec l'intégration d'INFOR ERP et de DocBits. Gestion efficace des fournisseurs et des documents en un seul endroit.
---

# Flux de travail de commande et de traitement des matériaux

Ce document décrit le flux de travail pour commander des matériaux auprès des fournisseurs, recevoir les marchandises et traiter les factures avec l'intégration entre les fournisseurs, le système INFOR ERP et DocBits pour la gestion des documents.

### Aperçu du processus

1. **Commande de matériaux**
* Initier la commande avec le fournisseur.
* Envoyer la commande au fournisseur via INFOR.
2. **Réception de la confirmation de commande**
* Le fournisseur confirme la réception de la commande.
* Création et envoi de la confirmation de commande.
3. **Réception et inspection des marchandises**
* Recevoir les marchandises du fournisseur.
* Enregistrer la réception des marchandises dans INFOR et vérifier par rapport à la facture de livraison.
4. **Traitement des factures**
* Recevoir la facture et l'envoyer à DocBits pour traitement.
* Vérifier les détails de la facture avec la commande et la réception des marchandises.
5. **Étapes finales**
* Archiver la commande et les documents associés dans DocBits.
* Mettre à jour INFOR avec les détails de la transaction pour la comptabilité financière.

### Points de décision et actions

* **Les marchandises reçues correspondent-elles à la commande?**
* Oui: Procéder au traitement de la facture.
* Non: Vérification manuelle et mise à jour requise.
* **La facture est-elle correcte selon les marchandises reçues et les détails de la commande?**
* Oui: Finaliser la transaction et mettre à jour les dossiers financiers.
* Non: Examen approfondi et corrections nécessaires.

### Points d'intégration

* **INFOR ERP**: Système principal pour le traitement des commandes, la réception des marchandises et la comptabilité financière.
* **DocBits**: Gestion des documents pour le traitement et l'archivage des factures et des confirmations de commande.

### Remarques

* Assurez-vous que tous les documents sont vérifiés et archivés pour la tenue des dossiers.
* Les divergences dans les détails de la commande ou de la facture doivent être résolues rapidement pour éviter les retards.

<figure><img src="../../.gitbook/assets/embed.svg" alt=""><figcaption></figcaption></figure>
