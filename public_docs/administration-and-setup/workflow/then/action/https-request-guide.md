# Envoyer une demande HTTPS

***

Ajoutez cette carte au groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

## 📌 Informations sur la version

**Version actuelle :** v2 (dernière et recommandée) **Statut :** ✅ Actif

**Historique des versions :**

* v1 → Requête HTTP simple (plus recommandée)
* **v2 → CURRENT** (support multilingue ajouté)

**Ce qui a changé :** v2 a ajouté la prise en charge de l'internationalisation (i18n). La fonctionnalité principale du webhook/requête reste inchangée.

📖 [Historique des versions et modifications](../../release.md) | [Base de données complète des cartes](../../cards-overview/export-cards-guide.md)

***

## Objectif

La carte de requête HTTPS utilise une URL HTTPS configurée et ses propres en-têtes. `call_api` utilise un chemin relatif de l’API DocBits et le contexte de l’utilisateur courant ; son résultat vient du texte de réponse. Choisissez selon le point de terminaison et le contrat de réponse, non selon une distinction entre API simple et complexe.

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :

* Envoyer des notifications de webhook à des services externes
* Déclencher des actions dans d'autres systèmes
* Interroger un service Web simple
* Envoyer des mises à jour de statut à d'autres applications
* Effectuez des intégrations simples sans exigences API complexes

***

## Comment ça marche

1. **Trigger Check** : Le système vérifie si les conditions "Quand" et "Et" sont remplies
2. **Demande de construction** : Le système prépare la requête HTTPS avec vos paramètres
3. **Envoyer en toute sécurité** : les données sont envoyées via une connexion HTTPS sécurisée
4. **Recevoir la réponse** : le service externe répond
5. **Continuer** : le workflow continue avec les données de réponse

***

## Paramètres

### URL

L'adresse du site Web auquel envoyer la demande

**Exemple :** `https://webhook.company.com/process`

### En-têtes

Instructions particulières pour le destinataire

**Exemple :**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Méthode

* **GET** : Demander des informations
* **POST** : Envoyer des données
* **PUT** : Mettre à jour les données

### Paramètres (chaîne de requête)

Données ajoutées à l'URL

**Exemple :** `?action=approve&user_id=123`

### Demander des données

Les informations réelles envoyées (au format JSON)

**Exemple :**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Exemple étape par étape

### Scénario : Envoyer une facture au système comptable

**Configuration de la carte :**

* **URL :** `https://accounting.company.com/invoices/create`
* **Méthode :** POST
* **En-têtes :** `Authorization: Bearer YOUR-TOKEN`
* **Demande de données :**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Réponse attendue :**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## Cas d'utilisation courants

### 1. Notifications de webhooks

Envoyez des notifications en temps réel à d'autres systèmes chaque fois que quelque chose se produit dans DocFlow

**Exemple :**

* Document approuvé → Envoyer une notification au système de traitement des commandes
* Fournisseur modifié → Notifier l'équipe d'achat via le webhook Slack/Teams

### 2. Intégration du système externe

Connectez DocFlow à d'autres systèmes d'entreprise pour un échange automatique de données

**Exemple :**

* Une fois le document traité → Synchronisation avec le système ERP
* Nouveau fournisseur ajouté → Créer un enregistrement de fournisseur dans le système de données principal

### 3. Flux de travail d'approbation

Envoyer le document à un système d'approbation externe et recevoir la décision

**Exemple :**

* Facture de grande valeur → Envoyer au Finance pour approbation
* Renvoyez le document au système externe avec la décision

***

## Guide de configuration

### Étape 1 : Obtenir des informations sur le point de terminaison

Demandez au système de réception :

* [ ] URL HTTPS
* [ ] En-têtes obligatoires
* [ ] Méthode d'authentification
* [ ] Format de requête attendu
* [ ] Format de réponse attendu

### Étape 2 : configurer la carte

1. Entrez l'URL HTTPS
2. Définir la méthode HTTP (généralement POST)
3. Ajouter une authentification si nécessaire
4. Formater les données de la demande au format JSON
5. Ajoutez des en-têtes personnalisés

### Étape 3 : Testez

Envoyer une demande de test et vérifier la réponse

***

## Gestion des réponses

Votre requête HTTPS recevra une réponse. Réponses courantes :

### Succès (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Mauvaise demande (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Non autorisé (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Erreur de serveur (500)

Le système de réception a un problème interne

***

## Dépannage

### "Erreur de certificat"

**Cause :** Problème de certificat de sécurité HTTPS

**Solution :**

* Vérifiez que l'URL est correcte
* Vérifiez si le certificat du site Web est valide
* Assurez-vous que vous utilisez HTTPS (et non HTTP)

### "Connexion refusée"

**Cause :** Impossible de se connecter au serveur

**Solution :**

* Vérifiez que l'URL/l'adresse IP est correcte
* Vérifiez si le service est en cours d'exécution
* Vérifier les règles de pare-feu
* Vérifier la connectivité Internet

### "Aucune réponse / Délai d'attente"

**Cause :** Le serveur ne répond pas dans le délai imparti

**Solution :**

* Vérifiez si le service est disponible
* Vérifier l'URL du point de terminaison
* Vérifiez s'il y a des limites de taux
* Contacter l'administrateur système

### "JSON invalide"

**Cause :** Les données de la requête sont mal formées

**Solution :**

* Vérifier les virgules manquantes dans JSON
* Vérifiez que tous les devis sont corrects
* Valider le format JSON (utiliser le validateur JSON en ligne)
* Vérifier les caractères spéciaux

***

## Exemples

### Exemple 1 : Envoyer au service Webhook

```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Exemple 2 : Mettre à jour le système externe

```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Exemple 3 : interroger un service externe

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Différence avec la carte "Call API"

La carte de requête HTTPS utilise une URL HTTPS configurée et ses propres en-têtes. `call_api` utilise un chemin relatif de l’API DocBits et le contexte de l’utilisateur courant ; son résultat vient du texte de réponse. Choisissez selon le point de terminaison et le contrat de réponse, non selon une distinction entre API simple et complexe.

***

## Considérations de sécurité

✅ **Toujours utiliser HTTPS** (connexion sécurisée)

⚠️ **Jamais :**

* Mettez les mots de passe dans l'URL
* Exposer les clés API dans les journaux
* Inclure les données personnelles dans les paramètres
* Utiliser HTTP pour les données sensibles

***

## Meilleures pratiques

✅ **Faire :**

* Testez d'abord avec de petites quantités de données
* Inclure la gestion des erreurs
* Enregistrez les demandes importantes
* Documenter l'intégration
* Surveiller les échecs

❌ **À ne pas faire :**

* Appelez le même point de terminaison à plusieurs reprises si vous n'en avez pas besoin
* Ignorer les erreurs de réponse
* Inclure les données sensibles en texte brut
* Dépasser les limites des tarifs de service

***

## Cartes associées

* **CALL\_API** - Intégration API plus avancée
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Vérifiez si la demande a réussi
* **ACTION\_SEND\_EMAIL** - Envoyez plutôt par e-mail
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Scripts automatisés

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Exemple d'action HTTPS

**Configuration :** Sélectionnez la méthode `POST`, remplacez `DEMO_WEBHOOK_URL` par votre point de terminaison de test autorisé, ajoutez l'en-tête `Content-Type: application/json` et le corps `{"document_number":"DEMO-001"}`. Configurez l'authentification uniquement si cela est requis par ce point de terminaison ; ne copiez jamais un vrai secret dans la documentation.

**Résultat attendu et contre-exemple :** L'action envoie la requête configurée lorsque sa route de workflow s'exécute. Inspectez la réponse HTTP et le service de test de réception. Un délai d'attente n'est pas une preuve que le service n'a rien fait, et cette action Then est distincte de la carte And qui vérifie un statut HTTP. Cette demande d'illustration n'a pas été envoyée.

Il s'agit d'une configuration de test illustrative et du résultat attendu ; il n'a pas été exécuté. Utilisez les données et les destinataires configurés dans votre organisation de test.
