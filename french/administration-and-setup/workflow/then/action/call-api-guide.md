# Call External API

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

## Objectif
Cette carte vous permet d'envoyer des données à un site web ou un service externe et de recevoir des informations en retour. Considérez cela comme l'envoi d'une question à un service externe et l'obtention d'une réponse que vous pouvez utiliser dans votre flux de travail.

**Exemple concret :** Votre entreprise utilise un système de tarification sur un autre site web. Cette carte peut automatiquement demander à ce système de tarification le prix actuel d'un article et intégrer ce prix dans votre document.

---

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :
- Obtenir des informations d'un service externe (comme des données de tarification, de validation ou de recherche)
- Envoyer des informations de document à un autre système pour traitement
- Vous intégrer à des services tiers
- Récupérer automatiquement des données sans recherches manuelles
- Connecter plusieurs systèmes métier entre eux

**Scénarios courants :**
- Rechercher des informations sur un fournisseur dans une base de données
- Obtenir des tarifs en temps réel d'un service de tarification
- Valider des données par rapport à un système externe
- Récupérer des informations d'expédition d'un prestataire logistique

---

## Comment ça fonctionne

1. **Vérification de la condition** : Le flux de travail vérifie d'abord si les conditions des sections « Where » et « And » sont remplies
2. **Préparation des données** : La carte collecte les paramètres que vous avez configurés
3. **Envoi de la requête** : Elle envoie vos données à l'API/au service externe
4. **Réception de la réponse** : Le service externe répond avec des données
5. **Continuer** : Le flux de travail utilise ces données dans les cartes suivantes

---

## Explication des paramètres

### API Endpoint URL
**De quoi il s'agit :** L'adresse du service externe avec lequel vous souhaitez communiquer

**Exemple :** `https://api.supplier-system.com/product/pricing`

**Comment la trouver :** Demandez à votre équipe informatique ou au prestataire de service son point de terminaison d'API

---

### HTTP Method
**De quoi il s'agit :** Le type de requête à envoyer

**Options :**
- **GET** : Demander des informations (comme poser une question)
- **POST** : Envoyer de nouvelles données
- **PUT** : Mettre à jour des données existantes
- **DELETE** : Supprimer des données

**Le plus courant :** GET (pour récupérer des informations)

---

### Headers
**De quoi il s'agit :** Instructions supplémentaires pour le service que vous appelez

**Exemple :**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Pourquoi c'est nécessaire :** Les services exigent souvent une authentification ou des instructions de format spécifiques

---

### Parameters (Query Parameters)
**De quoi il s'agit :** Informations supplémentaires transmises dans l'URL

**Exemple :**
```
?supplier_id=12345&currency=USD
```

**Exemple concret :** Si vous demandez des prix, les paramètres peuvent inclure l'ID du fournisseur et la devise

---

### Request Data (Body)
**De quoi il s'agit :** Les informations que vous envoyez au service

**Exemple :**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Quand l'utiliser :** Lors de l'utilisation des méthodes POST ou PUT

---

## Exemple étape par étape

### Scénario : Obtenir les tarifs d'un fournisseur en temps réel

**Configuration :**
1. **Type de carte :** Call API
2. **API Endpoint :** `https://api.suppliers.com/v1/prices`
3. **Method :** POST
4. **Headers :** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data :**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Ce qui se passe :**
1. Le document arrive avec Product ID : ABC123, Quantity : 100
2. La carte envoie la requête à l'API du fournisseur
3. L'API du fournisseur répond avec : `{"unit_price": 25.50, "total_price": 2550}`
4. Le flux de travail se poursuit avec ces informations de tarification
5. La carte suivante peut utiliser ces données pour valider le prix de la facture

---

## Étapes de configuration

### 1. Obtenir les informations de l'API
Contactez le prestataire de service externe et demandez :
- [ ] L'URL du point de terminaison de l'API
- [ ] La méthode d'authentification (clé API, nom d'utilisateur/mot de passe, OAuth)
- [ ] Les paramètres requis
- [ ] Le format de réponse attendu
- [ ] Les limites de débit ou les quotas

### 2. Configurer la carte
1. Saisissez l'URL du point de terminaison de l'API
2. Sélectionnez la méthode HTTP (généralement GET ou POST)
3. Ajoutez les en-têtes d'authentification si nécessaire
4. Ajoutez les paramètres requis
5. Formatez les données de requête en JSON si nécessaire

### 3. Tester la carte
1. Utilisez un document de test
2. Exécutez le flux de travail
3. Vérifiez si la réponse est reçue correctement
4. Vérifiez que le format des données correspond aux attentes

---

## Scénarios de réponse courants

### Réponse réussie (Status Code 200)
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
✅ Les données sont disponibles pour les cartes suivantes

### Réponse d'erreur (Status Code 404)
```json
{
  "error": "Product not found"
}
```
⚠️ L'API n'a pas pu trouver ce que vous recherchez

### Délai d'expiration
Le service externe n'a pas répondu dans le délai imparti
⚠️ Vérifiez si le service est disponible ou si l'URL du point de terminaison est correcte

---

## Exemples de flux de travail

### Exemple 1 : Validation automatique des prix
**Scénario :** Valider les prix des factures par rapport aux tarifs actuels du fournisseur

**Flux :**
1. Le document arrive avec une ligne d'article de facture (Product : A123, Price : 50 €)
2. **Carte Call API** → Demande à l'API du fournisseur : « Quel est le prix actuel de A123 ? »
3. Le fournisseur répond : « 48 € »
4. **Carte de condition** → Vérifie si le prix de la facture (50 €) est à 5 % près du prix actuel (48 €)
5. **Carte d'approbation** → Approuve si dans la tolérance

### Exemple 2 : Recherche automatique de fournisseur
**Scénario :** Obtenir les données de référence du fournisseur depuis une base de données centrale

**Flux :**
1. La facture arrive avec un Supplier Code : SUPP-789
2. **Carte Call API** → Demande au système : « Donne-moi les détails du fournisseur SUPP-789 »
3. Le système répond avec : Nom, Contact, Conditions, etc.
4. **Cartes Set Field** → Renseignent les champs du document avec ces données
5. **Carte d'exportation** → Exporte avec des informations complètes

### Exemple 3 : Coûts d'expédition en temps réel
**Scénario :** Obtenir un coût d'expédition automatique en fonction de la destination

**Flux :**
1. Le document contient une adresse de livraison
2. **Carte Call API** → Demande au prestataire d'expédition : « Quel est le coût vers [adresse] ? »
3. Le prestataire répond avec le coût d'expédition
4. **Carte Calculate** → Ajoute l'expédition au montant total de la facture
5. **Carte d'exportation** → Envoie avec le total mis à jour

---

## Dépannage

### Erreur « Connection Timeout »
**Cause :** Le service API ne répond pas

**Solutions :**
- [ ] Vérifier si le service est disponible (visiter le site web)
- [ ] Vérifier que l'URL du point de terminaison est correcte (pas de fautes de frappe)
- [ ] Vérifier la connexion Internet
- [ ] Contacter le prestataire de service
- [ ] Vérifier si le service a des limites de débit (vous envoyez trop de requêtes)

### Erreur « Unauthorized » ou « 403 Forbidden »
**Cause :** L'authentification a échoué

**Solutions :**
- [ ] Vérifier que votre clé API est correcte
- [ ] Vérifier si votre clé API a expiré
- [ ] S'assurer que l'en-tête d'authentification est correctement formaté
- [ ] Vérifier que vous avez les permissions pour ce point de terminaison

### Erreur « Bad Request » ou « 400 Error »
**Cause :** Le format des données de requête est incorrect

**Solutions :**
- [ ] Vérifier la syntaxe JSON (virgules, guillemets manquants, etc.)
- [ ] Vérifier que tous les champs requis sont inclus
- [ ] Vérifier que les noms des paramètres correspondent à ce que le service attend
- [ ] Consulter la documentation de l'API

### « La réponse ne fonctionne pas comme prévu »
**Solutions :**
- [ ] Tester l'API à l'aide d'un outil comme Postman
- [ ] Comparer le format de réponse réel avec le format attendu
- [ ] Vérifier si la documentation de l'API a changé
- [ ] Vérifier que les données que vous envoyez sont correctes

---

## Utilisation des données de réponse

Une fois que vous récupérez des données de l'API, les cartes suivantes peuvent les utiliser :

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

---

## Notes de sécurité

⚠️ **Important :** Ne mettez jamais d'informations sensibles dans la configuration de la carte qui pourraient être visibles par d'autres utilisateurs

- Ne codez pas en dur les mots de passe
- Utilisez les clés API de manière sécurisée
- N'incluez pas de données personnelles dans les journaux
- Utilisez des points de terminaison HTTPS (pas HTTP)

---

## Conseils et bonnes pratiques

✅ **À faire :**
- Tester d'abord avec un petit échantillon de documents
- Garder les appels d'API simples et ciblés
- Ajouter une gestion des erreurs avec des cartes de condition
- Surveiller l'utilisation/les coûts de l'API
- Documenter les exigences de l'API pour votre équipe

❌ **À ne pas faire :**
- Appeler les API pour chaque requête si vous pouvez mettre les données en cache
- Ignorer les codes d'erreur des réponses
- Utiliser des API de test en production
- Oublier d'ajouter les en-têtes d'authentification
- Supposer que l'API sera toujours disponible

---

## Cartes associées

- **ACTION_HTTPS_REQUEST** - Requêtes HTTPS similaires mais plus simples
- **CONDITION_HTTPS_REQUEST_STATUS** - Vérifier si l'appel d'API a réussi
- **ACTION_SEND_EMAIL** - Envoyer des données par e-mail au lieu de l'API
- **CALL_API** (version différente) - Méthode alternative d'appel d'API

---

## Besoin d'aide ?

- Demandez à votre équipe informatique/d'intégration la documentation de l'API
- Utilisez l'outil Postman pour tester d'abord les points de terminaison de l'API
- Consultez le portail de support du prestataire de service
- Consultez la documentation de l'API pour connaître les formats requis
