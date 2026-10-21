# Appeler une API externe

***

Ajoutez cette carte au groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

## 📌 Informations sur la version

**Version actuelle :** v2 (dernière et recommandée) **Statut :** ✅ Actif

**Historique des versions :**

* v1 → Appel API de base (plus recommandé)
* **v2 → CURRENT** (support multilingue ajouté)

**Ce qui a changé :** v2 a ajouté la prise en charge de l'internationalisation (i18n) avec les clés de traduction. La fonctionnalité reste identique.

📖 [Historique des versions et modifications](../../release.md) | [Base de données complète des cartes](../../cards-overview/export-cards-guide.md)

***

## Objectif

Cette carte vous permet d'envoyer des données à un site Web ou à un service externe et de recevoir des informations en retour. Pensez-y comme si vous envoyiez une question à un service externe et obteniez une réponse que vous pouvez utiliser dans votre flux de travail.

**Exemple concret :** Votre entreprise utilise un système de tarification sur un autre site Web. Cette carte peut automatiquement demander à ce système de tarification le prix actuel d'un article et intégrer ce prix dans votre document.

***

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :

* Obtenir des informations à partir d'un service externe (comme des données de tarification, de validation ou de recherche)
* Envoyer les informations du document à un autre système pour traitement
* Intégrer des services tiers
* Récupérer automatiquement les données sans recherches manuelles
* Connectez plusieurs systèmes d’entreprise ensemble

**Scénarios courants :**

* Rechercher des informations sur les fournisseurs dans une base de données
* Obtenez une tarification en temps réel à partir d'un service de tarification
* Valider les données par rapport à un système externe
* Récupérer des informations d'expédition auprès d'un prestataire logistique

***

## Comment ça marche

1. **Condition Check** : Le flux de travail vérifie d'abord si les conditions des sections "Quand" et "Et" sont remplies
2. **Préparer les données** : La carte collecte les paramètres que vous avez configurés
3. **Send Request** : Il envoie vos données à l'API/service externe
4. **Receive Response** : Le service externe répond avec des données
5. **Continuer** : Le workflow utilise ces données dans les cartes suivantes

***

## Paramètres expliqués

### URL du point de terminaison de l'API

**De quoi s'agit-il :** L'adresse du service externe avec lequel vous souhaitez communiquer

**Exemple :** `https://api.supplier-system.com/product/pricing`

**Comment le trouver :** Demandez à votre équipe informatique ou au fournisseur de services leur point de terminaison API

***

### Méthode HTTP

**De quoi s'agit-il :** Le type de requête à envoyer

**Options :**

* **GET** : Demander des informations (comme poser une question)
* **POST** : Envoyer de nouvelles données
* **PUT** : Mettre à jour les données existantes
* **DELETE** : Supprimer les données

**Le plus courant :** GET (pour récupérer des informations)

***

### En-têtes

**De quoi s'agit-il :** Instructions supplémentaires pour le service que vous appelez

**Exemple :**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Pourquoi est-ce nécessaire :** Les services nécessitent souvent une authentification ou des instructions de format spécifiques

***

### Paramètres (paramètres de requête)

**Qu'est-ce que c'est :** Informations supplémentaires transmises dans l'URL

**Exemple :**

```
?supplier_id=12345&currency=USD
```

**Exemple réel :** Si vous demandez des prix, les paramètres peuvent inclure l'ID du fournisseur et la devise.

***

### Demander des données (corps)

**Qu'est-ce que c'est :** Les informations que vous envoyez au service

**Exemple :**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Lorsque utilisé :** Lors de l'utilisation des méthodes POST ou PUT

***

## Exemple étape par étape

### Scénario : Obtenir les prix des fournisseurs en temps réel

**Configuration :**

1. **Type de carte :** Appeler l'API
2. **Point de terminaison API :** `https://api.suppliers.com/v1/prices`
3. **Méthode :** POST
4. **En-têtes :** `Authorization: Bearer YOUR-API-KEY`
5.  **Demande de données :**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**Que se passe-t-il :**

1. Le document arrive avec l'ID produit : ABC123, quantité : 100
2. La carte envoie une demande à l'API du fournisseur
3. L'API du fournisseur répond par : `{"unit_price": 25.50, "total_price": 2550}`
4. Le flux de travail se poursuit avec ces informations sur les prix
5. Next card peut utiliser ces données pour valider le prix facturé

***

## Étapes de configuration

### 1. Obtenez des informations sur l'API

Contactez le prestataire externe et demandez :

* [ ] URL du point de terminaison de l'API
* [ ] Méthode d'authentification (clé API, nom d'utilisateur/mot de passe, OAuth)
* [ ] Paramètres requis
* [ ] Format de réponse attendu
* [ ] Limites de taux ou quotas

### 2. Configurez la carte

1. Saisissez l'URL du point de terminaison de l'API
2. Sélectionnez la méthode HTTP (généralement GET ou POST)
3. Ajoutez des en-têtes d'authentification si nécessaire
4. Ajoutez tous les paramètres requis
5. Formater les données de la demande au format JSON si nécessaire

### 3. Testez la carte

1. Utiliser un document de test
2. Exécuter le flux de travail
3. Vérifiez si la réponse est reçue correctement
4. Vérifier que le format des données correspond aux attentes

***

## Scénarios de réponse courants

### Réponse réussie (code d'état 200)

```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```

✅ Les données sont disponibles pour les prochaines cartes à utiliser

### Réponse d'erreur (code d'état 404)

```json
{
  "error": "Product not found"
}
```

⚠️ L'API n'a pas trouvé ce que vous cherchez

### Délai d'attente

Le service externe n'a pas répondu dans le délai imparti ⚠️ Vérifiez si le service est disponible ou si l'URL du point de terminaison est correcte

***

## Exemples de flux de travail

### Exemple 1 : Validation automatique du prix

**Scénario :** Valider les prix facturés par rapport aux prix actuels du fournisseur

**Flux :**

1. Le document arrive avec la ligne de facture (Produit : A123, Prix : 50 €)
2. **Appeler la carte API** → Demande à l'API du fournisseur : "Quel est le prix actuel de l'A123 ?"
3. Le fournisseur répond : "48€"
4. **Carte d'état** → Vérifie si le prix facturé (50 €) se situe dans les 5 % du prix actuel (48 €)
5. **Carte d'approbation** → Approuve si dans les limites de tolérance

### Exemple 2 : Recherche automatique de fournisseurs

**Scénario :** Obtenir les données de base des fournisseurs à partir de la base de données centrale

**Flux :**

1. La facture arrive avec le code fournisseur : SUPP-789
2. **Appeler la carte API** → Demande au système : "Donnez-moi des détails sur le fournisseur SUPP-789"
3. Le système répond avec : Nom, Contact, Conditions, etc.
4. **Définir les cartes de champ** → Remplir les champs du document avec ces données
5. **Export Card** → Exporter avec des informations complètes

### Exemple 3 : frais d'expédition en temps réel

**Scénario :** Obtenez des frais d'expédition automatiques en fonction de la destination

**Flux :**

1. Le document a une adresse de livraison
2. **Appelez la carte API** → Demandez au transporteur : "Quel est le coût pour \[adresse] ?"
3. Le fournisseur répond avec les frais d'expédition
4. **Calculer la carte** → Ajouter les frais d'expédition au montant total de la facture
5. **Export Card** → Envoyer avec le total mis à jour

***

## Dépannage

### Erreur « Délai de connexion »

**Cause :** Le service API ne répond pas

**Solutions :**

* [ ] Vérifiez si le service est disponible (consultez le site Web)
* [ ] Vérifiez que l'URL du point de terminaison est correcte (pas de fautes de frappe)
* [ ] Vérifier la connexion Internet
* [ ] Contacter le prestataire
* [ ] Vérifiez si le service a des limites de débit (vous envoyez trop de requêtes)

### Erreur « Non autorisé » ou « 403 interdit »

**Cause :** Échec de l'authentification

**Solutions :**

* [ ] Vérifiez que votre clé API est correcte
* [ ] Vérifiez si votre clé API a expiré
* [ ] Assurez-vous que l'en-tête d'authentification est correctement formaté
* [ ] Vérifiez que vous disposez des autorisations pour ce point de terminaison

### « Mauvaise demande » ou « Erreur 400 »

**Cause :** Le format des données de la demande est incorrect

**Solutions :**

* [ ] Vérifiez la syntaxe JSON (virgules manquantes, guillemets, etc.)
* [ ] Vérifiez que tous les champs obligatoires sont inclus
* [ ] Vérifiez que les noms des paramètres correspondent à ce que le service attend
* [ ] Consulter la documentation de l'API

### "La réponse ne fonctionne pas comme prévu"

**Solutions :**

* [ ] Testez l'API à l'aide d'un outil comme Postman
* [ ] Comparez le format de réponse réel avec le format attendu
* [ ] Vérifiez si la documentation de l'API a changé
* [ ] Vérifiez que les données que vous envoyez sont correctes

***

## Utilisation des données de réponse

Une fois que vous avez récupéré les données de l'API, les cartes suivantes peuvent les utiliser :

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

***

## Notes de sécurité

⚠️ **Important :** Ne mettez jamais d'informations sensibles dans la configuration de la carte qui pourraient être visibles par d'autres utilisateurs

* Ne codez pas en dur les mots de passe
* Utilisez les clés API en toute sécurité
* Ne pas inclure de données personnelles dans les journaux
* Utiliser des points de terminaison HTTPS (et non HTTP)

***

## Conseils et bonnes pratiques

✅ **Faire :**

* Testez d'abord avec un petit échantillon de documents
* Gardez les appels API simples et ciblés
* Ajouter la gestion des erreurs avec les cartes de condition
* Surveiller l'utilisation/les coûts de l'API
* Documentez les exigences de l'API pour votre équipe

❌ **À ne pas faire :**

* Appelez des API pour chaque requête si vous pouvez mettre les données en cache
* Ignorer les codes d'erreur de réponse
* Utiliser les API de test en production
* Oublier d'ajouter des en-têtes d'authentification
* Supposons que l'API sera toujours disponible

***

## Cartes associées

* **ACTION\_HTTPS\_REQUEST** - Requêtes HTTPS similaires mais plus simples
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Vérifiez si l'appel API a réussi
* **ACTION\_SEND\_EMAIL** - Envoyer des données par e-mail au lieu de l'API
* **CALL\_API** (version différente) - Méthode d'appel API alternative

***

## Besoin d'aide ?

* Demandez à votre équipe informatique/intégration la documentation API
* Utilisez l'outil Postman pour tester d'abord les points de terminaison de l'API
* Consultez le portail d'assistance du fournisseur de services
* Consultez la documentation de l'API pour connaître les formats requis
