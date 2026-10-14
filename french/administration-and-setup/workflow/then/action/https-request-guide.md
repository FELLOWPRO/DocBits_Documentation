# Send HTTPS Request

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

## Objectif
Cette carte envoie un message sécurisé à un site web ou un service et peut recevoir une réponse en retour. Elle est plus simple que la carte « Call API » et est utile pour les intégrations rapides.

**Exemple concret :** Envoyer les données d'une facture à votre système comptable, ou demander à un système externe si un employé est autorisé à traiter cet achat.

---

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :
- Envoyer des notifications webhook à des services externes
- Déclencher des actions dans d'autres systèmes
- Interroger un service web simple
- Envoyer des mises à jour de statut à d'autres applications
- Effectuer des intégrations simples sans exigences d'API complexes

---

## Comment ça fonctionne

1. **Vérification du déclencheur** : Le système vérifie si les conditions « Where » et « And » sont remplies
2. **Construction de la requête** : Le système prépare la requête HTTPS avec vos paramètres
3. **Envoi sécurisé** : Les données sont envoyées via une connexion HTTPS sécurisée
4. **Réception de la réponse** : Le service externe répond
5. **Continuer** : Le flux de travail se poursuit avec les données de réponse

---

## Paramètres

### URL
L'adresse du site web à laquelle envoyer la requête

**Exemple :** `https://webhook.company.com/process`

### Headers
Instructions spéciales pour le destinataire

**Exemple :**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Method
- **GET** : Demander des informations
- **POST** : Envoyer des données
- **PUT** : Mettre à jour des données

### Parameters (Query String)
Données ajoutées à l'URL

**Exemple :** `?action=approve&user_id=123`

### Request Data
Les informations réelles envoyées (au format JSON)

**Exemple :**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Exemple étape par étape

### Scénario : Envoyer une facture au système comptable

**Configuration de la carte :**
- **URL :** `https://accounting.company.com/invoices/create`
- **Method :** POST
- **Headers :** `Authorization: Bearer YOUR-TOKEN`
- **Request Data :**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Réponse attendue :**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Cas d'usage courants

### 1. Notifications webhook
Envoyer des notifications en temps réel à d'autres systèmes chaque fois que quelque chose se produit dans DocFlow

**Exemple :**
- Document approuvé → Envoyer une notification au système d'exécution des commandes
- Fournisseur modifié → Notifier l'équipe d'achat via un webhook Slack/Teams

### 2. Intégration de systèmes externes
Connecter DocFlow à d'autres systèmes métier pour un échange de données automatique

**Exemple :**
- Après le traitement d'un document → Synchroniser avec le système ERP
- Nouveau fournisseur ajouté → Créer un enregistrement de fournisseur dans le système de données de référence

### 3. Flux de travail d'approbation
Envoyer un document à un système d'approbation externe et recevoir une décision

**Exemple :**
- Facture de valeur élevée → Envoyer à la Finance pour approbation
- Renvoyer le document au système externe avec la décision

---

## Guide de configuration

### Étape 1 : Obtenir les informations du point de terminaison
Demandez au système destinataire :
- [ ] L'URL HTTPS
- [ ] Les en-têtes requis
- [ ] La méthode d'authentification
- [ ] Le format de requête attendu
- [ ] Le format de réponse attendu

### Étape 2 : Configurer la carte
1. Saisissez l'URL HTTPS
2. Définissez la méthode HTTP (généralement POST)
3. Ajoutez l'authentification si nécessaire
4. Formatez les données de requête en JSON
5. Ajoutez les en-têtes personnalisés

### Étape 3 : Tester
Envoyez une requête de test et vérifiez la réponse

---

## Gestion des réponses

Votre requête HTTPS recevra une réponse. Réponses courantes :

### Succès (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Bad Request (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Unauthorized (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Server Error (500)
Le système destinataire a un problème interne

---

## Dépannage

### « Certificate Error »
**Cause :** Problème de certificat de sécurité HTTPS

**Solution :**
- Vérifiez que l'URL est correcte
- Vérifiez si le certificat du site web est valide
- Assurez-vous que vous utilisez HTTPS (pas HTTP)

### « Connection Refused »
**Cause :** Impossible de se connecter au serveur

**Solution :**
- Vérifiez que l'URL/l'adresse IP est correcte
- Vérifiez si le service est en cours d'exécution
- Vérifiez les règles de pare-feu
- Vérifiez la connectivité Internet

### « No Response / Timeout »
**Cause :** Le serveur ne répond pas dans le délai imparti

**Solution :**
- Vérifiez si le service est disponible
- Vérifiez l'URL du point de terminaison
- Vérifiez s'il existe des limites de débit
- Contactez l'administrateur système

### « Invalid JSON »
**Cause :** Les données de requête sont mal formées

**Solution :**
- Vérifiez les virgules manquantes dans le JSON
- Vérifiez que tous les guillemets sont corrects
- Validez le format JSON (utilisez un validateur JSON en ligne)
- Vérifiez les caractères spéciaux

---

## Exemples

### Exemple 1 : Envoyer à un service webhook
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

### Exemple 2 : Mettre à jour un système externe
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

### Exemple 3 : Interroger un service externe
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Différence avec la carte « Call API »

| Fonctionnalité | HTTPS Request | Call API |
|---------|---------------|----------|
| Simplicité | Simple | Plus complexe |
| Paramètres | Basiques | Avancés |
| Gestion des erreurs | Basique | Détaillée |
| À utiliser pour | Intégrations rapides | API complexes |
| Idéal pour | Webhooks | API professionnelles |

---

## Considérations de sécurité

✅ **Utilisez toujours HTTPS** (connexion sécurisée)

⚠️ **Ne jamais :**
- Mettre des mots de passe dans l'URL
- Exposer des clés API dans les journaux
- Inclure des données personnelles dans les paramètres
- Utiliser HTTP pour des données sensibles

---

## Bonnes pratiques

✅ **À faire :**
- Tester d'abord avec de petites quantités de données
- Inclure une gestion des erreurs
- Journaliser les requêtes importantes
- Documenter l'intégration
- Surveiller les échecs

❌ **À ne pas faire :**
- Appeler le même point de terminaison de manière répétée si ce n'est pas nécessaire
- Ignorer les erreurs de réponse
- Inclure des données sensibles en texte clair
- Dépasser les limites de débit du service

---

## Cartes associées

- **CALL_API** - Intégration d'API plus avancée
- **CONDITION_HTTPS_REQUEST_STATUS** - Vérifier si la requête a réussi
- **ACTION_SEND_EMAIL** - Envoyer par e-mail à la place
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Scripts automatisés
