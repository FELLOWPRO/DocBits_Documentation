# Run DocOperator Prompt (Automation Script)

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

## Objectif
Cette carte exécute une action de navigateur ou un script automatisé à l'aide de DocOperator. Considérez-la comme un robot capable d'interagir avec des sites web ou des systèmes exactement comme le ferait un humain - cliquer sur des boutons, remplir des formulaires, extraire des données, etc.

**Exemple concret :** Votre entreprise utilise un système d'achat basé sur le web. Cette carte peut automatiquement se connecter, rechercher un produit, vérifier la disponibilité et obtenir le prix actuel - le tout sans que personne ne le fasse manuellement.

---

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :
- Automatiser des tâches sur des sites web qui n'ont pas d'API
- Extraire des données de pages web
- Remplir des formulaires automatiquement
- Vous connecter à des systèmes et récupérer des informations
- Automatiser des tâches manuelles répétitives
- Interagir avec des systèmes hérités qui ne sont pas intégrés

**Scénarios courants :**
- Se connecter à des sites web de fournisseurs et obtenir l'inventaire en temps réel
- Remplir automatiquement des formulaires sur des systèmes externes
- Extraire des données de pages web qui n'offrent pas d'API
- Vérifier le statut de livraison sur les sites web des transporteurs
- Obtenir des tarifs depuis des systèmes sans accès API

---

## Comment ça fonctionne

1. **Carte déclenchée** : Le flux de travail atteint cette carte et les conditions sont remplies
2. **Démarrage du script** : Le bot DocOperator commence à exécuter votre script d'automatisation
3. **Actions du bot** : Le bot effectue des actions telles que cliquer, taper, faire défiler, extraire
4. **Extraction de données** : Le bot collecte des informations à partir des pages web
5. **Retour des données** : Les données reviennent à DocFlow pour être utilisées dans les cartes suivantes
6. **Gestion du délai d'expiration** : Si le script prend trop de temps, il s'arrête et renvoie ce qu'il a obtenu

---

## Explication des paramètres

### DocOperator Prompt/Script
Le script d'automatisation qui indique à DocOperator exactement quoi faire

**Exemple (en langage clair) :**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variables
Les données que vous souhaitez transmettre AU script

**Exemple :**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Ces variables peuvent être utilisées dans le script comme suit :
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
Le nombre d'actions que le bot est autorisé à effectuer

**Valeurs typiques :**
- Tâche simple (comme obtenir un prix) : 10-20 étapes
- Complexité moyenne (remplir un formulaire + extraire) : 20-50 étapes
- Flux de travail complexe (connexion + recherche + validation) : 50-100 étapes

**Pourquoi c'est important :** Empêche les boucles infinies et les scripts à très longue durée d'exécution

### Maximum Retries
Si le bot échoue à une action, combien de fois doit-il réessayer ?

**Exemples :**
- 1 : Essayer une fois, en cas d'échec passer à la suite
- 3 : Essayer 3 fois avant d'abandonner
- 5 : Très persistant - essayer 5 fois

---

## Exemple étape par étape

### Scénario : Obtenir les tarifs d'un fournisseur depuis un site web

**Définition du script :**
```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variables transmises :**
```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script utilisant les variables :**
```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Résultat attendu :**
```
price: 45.50
quantity_available: 500
```

---

## Types d'actions que DocOperator peut effectuer

### Navigation
- Aller à une URL
- Cliquer sur des liens
- Appuyer sur des boutons
- Faire défiler la page

### Remplissage de formulaires
- Taper du texte dans des champs
- Sélectionner des options de liste déroulante
- Cocher/décocher des cases
- Cliquer sur des boutons

### Extraction de données
- Lire du texte sur une page
- Extraire des nombres
- Obtenir des données de tableau
- Copier des informations

### Attente
- Attendre le chargement de la page
- Attendre l'apparition d'éléments
- Attendre du contenu dynamique

### Logique conditionnelle
- Si quelque chose existe, faire ceci
- Si le texte correspond, alors...
- Compter les résultats et agir en conséquence

---

## Cas d'usage courants

### 1. Obtenir des tarifs en temps réel
**Scénario :** Le fournisseur n'a pas d'API mais le site web affiche les prix

**Script :**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Vérifier la disponibilité des stocks
**Scénario :** Besoin de savoir si le fournisseur a du stock

**Script :**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Soumission automatique de formulaire
**Scénario :** Besoin de remplir un formulaire sur un site externe

**Script :**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Vérification de saisie de données
**Scénario :** Vérifier que les données correspondent sur deux systèmes différents

**Script :**
```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

---

## Étapes de configuration

### Étape 1 : Créer le script
1. Définissez ce que vous voulez accomplir
2. Décomposez-le en petites étapes
3. Écrivez chaque étape clairement
4. Testez d'abord manuellement (ouvrez le site web, faites-le vous-même)
5. Documentez exactement ce sur quoi vous cliquez, où vous tapez, ce que vous extrayez

### Étape 2 : Identifier les variables
1. Quelles données changeront d'un document à l'autre ?
2. Que faut-il transmettre au script ?
3. Définissez les noms des variables
4. Spécifiez où les variables sont utilisées dans le script

### Étape 3 : Définir les paramètres
- **Maximum Steps** : En fonction de la complexité du script
- **Maximum Retries** : Quelle persistance le bot doit-il avoir ?
- **Timeout** : Combien de temps doit-il attendre les pages ?

### Étape 4 : Tester
1. Testez avec des données d'exemple
2. Vérifiez que le bot peut accéder au site web
3. Vérifiez que l'extraction est correcte
4. Vérifiez si les variables fonctionnent correctement

---

## Conseils de rédaction de scripts

### Langage clair
✅ **À faire :**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **À ne pas faire :**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Sélecteurs spécifiques
✅ **À faire :**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **À ne pas faire :**
```
Click somewhere
Type in a field
```

### Gestion des erreurs
✅ **À faire :**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **À ne pas faire :**
```
Click "Next" (assumes it's always there)
```

---

## Dépannage

### « Script Timed Out »
**Cause :** Le script a pris trop de temps à se terminer

**Solutions :**
- [ ] Réduire le nombre d'actions
- [ ] Augmenter la valeur « Maximum Steps »
- [ ] Optimiser le script pour une exécution plus rapide
- [ ] Simplifier ce que vous essayez d'extraire

### « Element Not Found »
**Cause :** DocOperator n'a pas pu trouver le bouton/champ que vous avez spécifié

**Solutions :**
- [ ] Vérifier que le nom du bouton/champ est exactement correct
- [ ] Vérifier si la mise en page du site web a changé
- [ ] Ajouter un temps d'attente avant de cliquer
- [ ] Vérifier si le bouton n'apparaît que dans certaines conditions

### « Login Failed »
**Cause :** L'authentification a échoué

**Solutions :**
- [ ] Vérifier que le nom d'utilisateur/mot de passe sont corrects
- [ ] Vérifier si le mot de passe contient des caractères spéciaux
- [ ] Vérifier que le compte n'est pas verrouillé
- [ ] Vérifier si le processus de connexion a changé

### « Data Not Extracted Correctly »
**Cause :** Le script s'est exécuté mais a extrait les mauvaises informations

**Solutions :**
- [ ] Vérifier que le bon champ a été sélectionné
- [ ] Vérifier si les données se trouvent à l'emplacement attendu
- [ ] Tester la logique d'extraction manuellement
- [ ] Ajouter des étapes de débogage pour vérifier ce qui se trouve sur la page

### « Script Runs Slowly »
**Cause :** Trop d'étapes ou site web lent

**Solutions :**
- [ ] Supprimer les étapes inutiles
- [ ] Optimiser les temps d'attente
- [ ] Vérifier la connexion Internet
- [ ] Envisager s'il existe une alternative API

---

## Bonnes pratiques

✅ **À faire :**
- Tester minutieusement les scripts avant le déploiement
- Garder les scripts simples et ciblés
- Ajouter des commentaires expliquant chaque étape
- Utiliser des noms de variables explicites
- Surveiller les performances des scripts
- Prévoir une solution de repli en cas d'échec des scripts

❌ **À ne pas faire :**
- Créer des scripts extrêmement longs (>100 étapes)
- Mettre des mots de passe sensibles dans les journaux
- Se fier à des coordonnées exactes (les sites web changent)
- Créer des boucles sans conditions de sortie
- Ignorer les messages d'erreur

---

## Conseils de performance

- **Supprimez les étapes inutilisées** - Chaque étape prend du temps
- **Combinez les actions similaires** - Regroupez les clics connexes
- **Optimisez les attentes** - N'utilisez que les délais nécessaires
- **Mettez les données en cache** - N'extrayez pas deux fois les mêmes données
- **Traitement parallèle** - Exécutez plusieurs scripts si possible

---

## Considérations de sécurité

⚠️ **Important :**
- Ne stockez pas de mots de passe dans DocFlow
- Utilisez des méthodes sécurisées pour transmettre les identifiants
- Ne journalisez pas de données sensibles
- Surveillez ce qui est extrait
- Assurez-vous que l'activité du bot est journalisée et auditable

---

## Exemple de variables

### Variables disponibles que vous pouvez utiliser :
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script utilisant les variables :
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Comparaison : Quand utiliser DocOperator vs API

| Situation | Utiliser DocOperator | Utiliser l'API |
|-----------|-----------------|---------|
| Le site web a une API | ❌ Non | ✅ Oui |
| Le site web est interactif | ✅ Oui | ❌ Non |
| Nécessite une connexion | ✅ Oui | Dépend |
| Très grande rapidité nécessaire | ❌ Non | ✅ Oui |
| Flux de travail complexe | ✅ Oui | ❌ Peut-être pas |
| Les données changent quotidiennement | ✅ Oui | ✅ Oui |

---

## Cartes associées

- **CALL_API** - À utiliser lorsqu'une API est disponible à la place
- **ACTION_HTTPS_REQUEST** - Requêtes plus simples
- **ACTION_SET_FIELD_TO_TEXT** - Utiliser les données extraites
- **CONDITION_HTTPS_REQUEST_STATUS** - Vérifier le statut de la requête
