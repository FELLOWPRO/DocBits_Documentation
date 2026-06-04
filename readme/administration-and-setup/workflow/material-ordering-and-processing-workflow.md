---
description: >-
  Explorez le flux de travail étape par étape pour la commande de matériel, la
  réception des marchandises et le traitement des factures avec l'intégration
  d'INFOR ERP et de DocBits. Une gestion efficace des fournisseurs et des
  documents en un seul endroit.
---

# Flux de travail de commande et de traitement du matériel

Ce document décrit le flux de travail pour commander du matériel auprès des fournisseurs, réceptionner les marchandises et traiter les factures, avec une intégration entre les fournisseurs, le système INFOR ERP et DocBits pour la gestion des documents.

### Aperçu du processus

1. **Commande de matériel**
   * Initier la commande auprès du fournisseur.
   * Envoyer la commande au fournisseur via INFOR.
2. **Réception de la confirmation de commande**
   * Le fournisseur confirme la réception de la commande.
   * Création et envoi de la confirmation de commande.
3. **Réception et inspection des marchandises**
   * Réceptionner les marchandises du fournisseur.
   * Comptabiliser la réception des marchandises dans INFOR et la vérifier par rapport au bon de livraison.
4. **Traitement des factures**
   * Recevoir la facture et l'envoyer à DocBits pour traitement.
   * Vérifier et valider les détails de la facture avec la commande et la réception des marchandises.
5. **Étapes finales**
   * Archiver la commande et les documents associés dans DocBits.
   * Mettre à jour INFOR avec les détails de la transaction pour la comptabilité financière.

### Points de décision et actions

* **Les marchandises reçues correspondent-elles à la commande ?**
  * Oui : Procéder au traitement de la facture.
  * Non : Vérification et mise à jour manuelles requises.
* **La facture est-elle correcte par rapport aux marchandises reçues et aux détails de la commande ?**
  * Oui : Finaliser la transaction et mettre à jour les enregistrements financiers.
  * Non : Examen et corrections supplémentaires nécessaires.

### Points d'intégration

* **INFOR ERP** : Système principal pour le traitement des commandes, la réception des marchandises et la comptabilité financière.
* **DocBits** : Gestion des documents pour le traitement et l'archivage des factures et des confirmations de commande.

### Remarques

* Veillez à ce que tous les documents soient vérifiés et archivés à des fins de conservation des enregistrements.
* Les divergences dans les détails de la commande ou de la facture doivent être résolues rapidement pour éviter les retards.

<figure><img src="../../../.gitbook/assets/embed.svg" alt=""><figcaption></figcaption></figure>
