---
description: Envoyer des données maîtres dans DocBits manuellement via l'API
---

# Importer via l'API

Les données maîtres arrivent normalement dans DocBits automatiquement via votre flux de données ION. Les pages de cette section décrivent comment envoyer les mêmes données manuellement via l'interface de test de l'API — utile lorsque vous voulez réimporter un enregistrement, charger quelque chose qui n'est jamais arrivé, ou essayer un nouveau mappage de champs avant d'activer le flux automatique.

Chaque page suit les mêmes cinq étapes : ouvrir le lien de l'API de votre environnement, s'autoriser avec votre Org ID et votre API key, remplir le formulaire, exécuter et vérifier que les données sont bien arrivées.

* [Importer des Fournisseurs (Supplier BOD)](supplier-bod.md)
* [Importer des Commandes d'Achat (Purchase Order BOD)](purchase-order-bod.md)
* [Importer des Réceptions de Marchandises (Receive Delivery BOD)](receive-delivery-bod.md)
* [Importer des Données Maîtres depuis XML](master-data-xml.md)

## Ce dont vous avez besoin

* **Une API key** — voir [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Votre Org ID** — sous **Settings → Integration & SSO**, dans la section **ID**.
* **Les données elles-mêmes**, sous forme de fichier XML ou de contenu XML que vous pouvez coller.

{% hint style="warning" %}
Un import écrit directement dans les données maîtres de votre organisation. Vérifiez vers quel environnement, quelle région et quelle organisation vous pointez avant d'exécuter.
{% endhint %}
