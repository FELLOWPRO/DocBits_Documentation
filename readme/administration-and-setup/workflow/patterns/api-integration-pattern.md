# Modèle d'intégration d'API

**Type de modèle :** Intégration
**Complexité :** Moyenne
**Mise en place estimée :** 45-60 minutes
**Cas d'usage courants :** Récupération de données externes, validation des prix, recherche de données de référence

---

Vous construisez ce modèle dans le **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Cliquez sur **Add Card** pour ouvrir la bibliothèque de cartes et sélectionnez les cartes utilisées par ce modèle — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` et `CONDITION_COMPARE_TWO_DOCFIELD_VALUES` :

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card dans le Workflow Builder, regroupée par catégorie"><figcaption><p>La bibliothèque <strong>Add Card</strong> — sélectionnez les cartes d'API, de condition et de champ utilisées par ce modèle dans ces catégories.</p></figcaption></figure>

---

## Vue d'ensemble du modèle

Ce modèle montre comment intégrer DocBits à des API externes pour récupérer, valider et stocker des données provenant de systèmes externes. C'est l'un des modèles de workflow les plus courants pour connecter DocBits à des systèmes de tarification, des services de validation, des systèmes ERP et d'autres sources de données externes.

**Ce que fait ce modèle :**
1. Appelle une API externe pour récupérer des données
2. Valide la réponse de l'API
3. Stocke les données de réponse dans des champs de document
4. Prend des décisions en fonction des données récupérées
5. Route les documents en conséquence

---

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :
- ✅ Récupérer des tarifs en temps réel depuis des systèmes externes
- ✅ Valider les informations fournisseur par rapport à la base de données de référence
- ✅ Rechercher des détails produit dans des systèmes de catalogue
- ✅ Obtenir des taux de change auprès de services de devises
- ✅ Vérifier des adresses avec un service de géocodage
- ✅ Vérifier les niveaux de stock dans des systèmes d'entrepôt
- ✅ Valider les taux de taxe auprès de services fiscaux

**N'utilisez pas ce modèle lorsque :**
- ❌ les données figurent déjà dans les données de référence de DocBits (utilisez plutôt la recherche de données de référence)
- ❌ le système externe ne dispose pas d'API (utilisez plutôt le modèle DocOperator Script)
- ❌ les données changent rarement (envisagez un import manuel)

---

## Exemple complet de workflow

### Scénario : Valider le prix d'une facture par rapport à une API de tarification actuelle

**Exigence métier :**
- Le fournisseur envoie une facture
- La facture indique un prix unitaire de 52,00 €
- Nous devons vérifier que cela correspond à la tarification fournisseur actuelle
- Si le prix s'écarte de plus de 5 %, escalader pour révision

**Cartes de workflow utilisées :**
1. CALL_API – Récupérer le prix actuel depuis l'API fournisseur
2. CONDITION_HTTPS_REQUEST_STATUS – Vérifier si l'appel d'API a réussi
3. ACTION_SET_FIELD_TO_TEXT – Stocker le prix de l'API dans un champ de document
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Comparer le prix de la facture au prix de l'API
5. ACTION_ASSIGN_TO_USER – Router en fonction du résultat de la comparaison
6. tasks_create – Créer une tâche de révision si nécessaire

---

## Mise en œuvre étape par étape

### Étape 1 : Appeler l'API externe

**Carte :** CALL_API ou ACTION_CALL_EXTERNAL_API

**Configuration :**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Réponse attendue :**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Référence du guide :** [Guide Call API](../then/action/call-api-guide.md)

---

### Étape 2 : Valider la réponse de l'API

**Carte :** CONDITION_HTTPS_REQUEST_STATUS

**Configuration :**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Logique :**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Référence du guide :** [Guide des cartes de condition – Statut HTTP](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Étape 3 : Stocker la réponse de l'API dans des champs de document

**Carte :** ACTION_SET_FIELD_TO_TEXT (ou un setter de champ équivalent)

**Configuration :**

**Champ 1 : Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Champ 2 : API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Champ 3 : API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Résultat :** Les données de l'API sont désormais stockées dans des champs de document pour une utilisation ultérieure

**Référence du guide :** [Guide de manipulation des champs – Stockage des données d'API](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Étape 4 : Comparer le prix de la facture au prix de l'API

**Carte :** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuration :**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Calcul :**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Référence du guide :** [Guide des cartes de condition – Comparaison de champs](../and/condition-cards-complete-guide.md#field-comparison)

---

### Étape 5 : Router en fonction du résultat de la validation

**Scénario A : Prix dans la tolérance (Pass)**

**Cartes :**
- ACTION_SET_FIELD_TO_TEXT
  - Définir le champ « Price_Validation_Status » = « PASS »
  - Définir le champ « Price_Variance_Percent » = « 4% »
- ACTION_APPROVE_DOCUMENT
  - Approuver automatiquement le document

**Scénario B : Prix hors tolérance (Fail)**

**Cartes :**
- ACTION_SET_FIELD_TO_TEXT
  - Définir le champ « Price_Validation_Status » = « FAIL »
  - Définir le champ « Price_Variance_Percent » = « 12% » (exemple)
- tasks_create
  - Titre de la tâche : « Review Price Variance - {{DOCUMENT_NUMBER}} »
  - Description de la tâche : « Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}} »
  - Priorité : Haute
- ACTION_ASSIGN_TO_USER
  - Affecter à : Responsable des achats
- ACTION_SEND_EMAIL_TO_GROUPS
  - Envoyer une notification à l'équipe Achats

**Références des guides :**
- [Guide d'affectation](../then/assignee/assignment-user-guide.md)
- [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)
- [Guide d'envoi d'e-mails](../then/action/send-email-groups-guide.md)

---

## Diagramme de workflow complet

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Gabarits de configuration

### Gabarit 1 : Requête GET simple (recherche)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Utilisation :** Recherche de données simple par ID

---

### Gabarit 2 : Requête POST avec corps (validation)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Utilisation :** Envoyer des données de document pour validation

---

### Gabarit 3 : Requête complexe avec données imbriquées

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Utilisation :** Traitement complexe de documents avec données de tableau

---

## Gestion des erreurs

### Erreurs courantes et solutions

#### Erreur 1 : Délai de connexion dépassé

**Symptômes :**
- L'API ne répond pas
- Le workflow reste bloqué en attente

**Solution :**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Erreur 2 : 401 Unauthorized

**Symptômes :**
- L'API renvoie le statut 401
- L'authentification a échoué

**Solution :**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Erreur 3 : Format de réponse invalide

**Symptômes :**
- Réponse reçue mais impossible à analyser
- Champs attendus manquants

**Solution :**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Référence du guide :** [Call API – Dépannage](../then/action/call-api-guide.md#troubleshooting)

---

## Variantes avancées

### Variante 1 : Chaînage de plusieurs API

**Scénario :** Données requises de plusieurs API

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Variante 2 : Appels d'API conditionnels

**Scénario :** Appeler l'API uniquement sous certaines conditions

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Variante 3 : Mise en cache des réponses d'API

**Scénario :** Réduire les appels d'API en mettant en cache les réponses

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Aspects de performance

### Bonnes pratiques

✅ **Recommandé :**
- Mettre en cache les réponses d'API lorsque c'est possible
- Utiliser des réglages de délai d'attente (30-60 secondes)
- Implémenter une logique de réessai pour les échecs temporaires
- Journaliser les appels d'API pour le débogage
- Surveiller l'utilisation/les coûts de l'API
- Tester d'abord avec des documents d'exemple

❌ **Déconseillé :**
- Appeler les API de manière synchrone pour chaque document (envisager le traitement par lots)
- Ignorer les erreurs de réponse
- Coder en dur les identifiants dans le workflow
- Effectuer des appels d'API inutiles
- Laisser les délais d'attente non traités

---

## Liste de vérification de test

Avant de déployer ce modèle :

- [ ] Tester l'appel d'API avec des données valides
- [ ] Tester l'appel d'API avec des données invalides
- [ ] Tester le scénario de délai d'attente (que se passe-t-il si l'API est lente ?)
- [ ] Tester l'échec d'authentification
- [ ] Tester un format de réponse invalide
- [ ] Tester le stockage des champs (données correctement stockées ?)
- [ ] Tester la logique de comparaison (calcul correct ?)
- [ ] Tester le routage (les documents vont-ils au bon endroit ?)
- [ ] Tester la gestion des erreurs (erreurs traitées proprement ?)
- [ ] Tester avec un volume élevé (performance acceptable ?)

---

## Exemples concrets

### Exemple 1 : Recherche de taux de change

**API :** https://api.exchangerate-api.com/v4/latest/USD

**Workflow :**
1. Extraire la devise de la facture : « GBP »
2. Appeler l'API de taux de change
3. Récupérer le taux GBP→EUR
4. Calculer l'équivalent en EUR
5. Stocker dans le champ « Amount_EUR »
6. Poursuivre le traitement avec le montant en EUR

---

### Exemple 2 : Vérification de solvabilité du fournisseur

**API :** Service interne de vérification de solvabilité

**Workflow :**
1. Extraire le code fournisseur
2. Appeler l'API de vérification de solvabilité
3. Récupérer le statut de solvabilité : « APPROVED » ou « BLOCKED »
4. IF BLOCKED:
   - Arrêter le traitement
   - Créer une tâche urgente
   - Notifier l'équipe Finance
5. IF APPROVED:
   - Poursuivre le workflow normal

---

### Exemple 3 : Enrichissement des données de référence produit

**API :** Service de catalogue produit

**Workflow :**
1. Extraire le code produit de la facture
2. Appeler l'API produit
3. Récupérer : nom du produit, catégorie, compte général
4. Stocker dans des champs de document
5. Utiliser pour la comptabilisation automatique

---

## Modèles connexes

### Ce modèle fonctionne bien avec :

- **[Modèle de transformation des données](data-transformation-pattern.md)** – Transformer les données de réponse de l'API
- **[Modèle de logique de décision](decision-logic-pattern.md)** – Router en fonction des données de l'API
- **[Modèle de gestion des tâches](task-management-pattern.md)** – Créer des tâches pour les erreurs d'API
- **[Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)** – Combiner les tarifs de l'API avec la validation de commande

---

## Guides connexes

### Prérequis
- [Guide Call API](../then/action/call-api-guide.md) – Documentation de la carte d'API
- [Guide des cartes de condition](../and/condition-cards-complete-guide.md) – Logique de condition
- [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md) – Opérations sur les champs

### Cartes connexes
- **CALL_API** – [Guide Call API](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** – [Guide HTTPS Request](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** – [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md#field-comparison)

---

## Support & ressources

**Besoin d'aide ?**
- Lire [Call API – Dépannage](../then/action/call-api-guide.md#troubleshooting)
- Vérifier les [Codes de réponse d'API](../then/action/call-api-guide.md#response-scenarios)
- Tester d'abord l'API avec Postman
- Contacter le support du fournisseur d'API

**Retours :**
- Signaler les problèmes du modèle à : docs@docbits.com
- Suggérer des améliorations
- Partager vos cas d'usage

---

**Version du modèle :** 1.0
**Dernière mise à jour :** 23 octobre 2025
**Difficulté :** Moyenne
**Temps estimé :** 45-60 minutes
**Taux de réussite :** Élevé (lorsque l'API est stable)
