# Exécuter l'invite DocOperator (script d'automatisation)

***

Ajoutez cette carte au groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

## 📌 Informations sur la version

**Version actuelle :** v3 (dernière et recommandée) **Statut :** ✅ Actif

**Historique des versions :**

* v2 → Implémentation originale de DocOperator
* **v3 → CURRENT** (paramètre de contrôle d'exécution ajouté)
* v4 → Obsolète (fonctionnalités rétablies)

**Ce qui a changé :** v3 a ajouté le paramètre facultatif "Exécuter l'invite" pour plus de contrôle. La v4 a tenté d'annuler cela mais est devenue obsolète.

📖 [Historique des versions et modifications](../../release.md) | [Base de données complète des cartes](../../cards-overview/export-cards-guide.md)

***

## Objectif

Cette carte exécute une action ou un script de navigateur automatisé à l'aide de DocOperator. Considérez-le comme un robot capable d'interagir avec des sites Web ou des systèmes exactement comme le ferait un humain : cliquer sur des boutons, remplir des formulaires, extraire des données, etc.

**Exemple concret :** Votre entreprise utilise un système d'achat basé sur le Web. Cette carte peut se connecter automatiquement, rechercher un produit, vérifier la disponibilité et obtenir le prix actuel, le tout sans que personne ne le fasse manuellement.

***

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :

* Automatisez les tâches sur les sites Web qui n'ont pas d'API
* Extraire les données des pages Web
* Remplissez automatiquement les formulaires
* Connectez-vous aux systèmes et récupérez des informations
* Automatisez les tâches manuelles répétitives
* Interagissez avec les systèmes existants qui ne sont pas intégrés

**Scénarios courants :**

* Connectez-vous aux sites Web des fournisseurs et obtenez un inventaire en temps réel
* Remplissez automatiquement des formulaires sur des systèmes externes
* Extraire les données des pages Web qui n'offrent pas d'API
* Vérifiez l'état de livraison sur les sites Web de messagerie
* Obtenez les tarifs des systèmes sans accès API

***

## Comment ça marche

1. **Carte déclenchée** : le flux de travail atteint cette carte et les conditions sont remplies
2. **Le script démarre** : le bot DocOperator commence à exécuter votre script d'automatisation
3. **Actions des robots** : Le bot effectue des actions telles que cliquer, taper, faire défiler, extraire
4. **Extraction de données** : le robot collecte des informations à partir de pages Web
5. **Return Data** : Les données reviennent à DocFlow pour être utilisées dans les prochaines cartes
6. **Gestion des délais d'attente** : Si le script prend trop de temps, il s'arrête et renvoie ce qu'il a

***

## Paramètres expliqués

### Invite/Script DocOperator

Le script d'automatisation qui indique à DocOperator exactement quoi faire

**Exemple (anglais simple) :**

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

Données que vous souhaitez transmettre DANS le script

**Exemple :**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Ces variables peuvent être utilisées dans le script comme :

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Étapes maximales

Combien d'actions le bot est autorisé à effectuer

**Valeurs typiques :**

* Tâche simple (comme obtenir un prix unique) : 10 à 20 étapes
* Complexité moyenne (remplir le formulaire + extraire) : 20-50 étapes
* Workflow complexe (connexion + recherche + validation) : 50-100 étapes

**Pourquoi c'est important :** Empêche les boucles infinies et les scripts à exécution très longue

### Nombre maximal de tentatives

Si le bot échoue à une action, combien de fois doit-il réessayer ?

**Exemples :**

* 1 : Essayez une fois, si cela échoue, continuez
* 3 : Essayez 3 fois avant d’abandonner
* 5 : Très persistant – essayez 5 fois

***

## Exemple étape par étape

### Scénario : Obtenir les prix des fournisseurs à partir du site Web

**Définition du script :**

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

**Variables transmises :**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script utilisant des variables :**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Résultat attendu :**

```
price: 45.50
quantity_available: 500
```

***

## Types d'actions que DocOperator peut effectuer

### Navigation

* Aller à l'URL
* Cliquez sur les liens
* Appuyez sur les boutons
* Faire défiler la page

### Remplissage de formulaire

* Tapez du texte dans les champs
* Sélectionnez les options déroulantes
* Cocher/décocher les cases
* Cliquez sur les boutons

### Extraction de données

* Lire le texte de la page
* Extraire des numéros
* Obtenir les données du tableau
* Copier les informations

### En attente

* Attendez que la page se charge
* Attendez que les éléments apparaissent
* Attendez le contenu dynamique

### Logique conditionnelle

* Si quelque chose existe, fais ceci
* Si le texte correspond, alors...
* Comptez les résultats et agissez en conséquence

***

## Cas d'utilisation courants

### 1. Obtenez les tarifs en temps réel

**Scénario :** Le fournisseur n'a pas d'API mais le site Web affiche les prix

**Script :**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Vérifiez la disponibilité de l'inventaire

**Scénario :** Besoin de savoir si le fournisseur a du stock

**Script :**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Soumission automatique du formulaire

**Scénario :** Besoin de remplir un formulaire sur un site externe

**Script :**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Vérification de la saisie des données

**Scénario :** Vérifier les correspondances de données sur deux systèmes différents

**Script :**

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

***

## Étapes de configuration

### Étape 1 : Créer le script

1. Définissez ce que vous souhaitez accomplir
2. Divisez-le en petites étapes
3. Écrivez clairement chaque étape
4. Testez d'abord manuellement (ouvrez le site Web, faites-le vous-même)
5. Documentez exactement ce sur quoi vous cliquez, où vous tapez, ce que vous extrayez

### Étape 2 : identifier les variables

1. Quelles données changeront entre les documents ?
2. Que faut-il passer dans le script ?
3. Définir les noms de variables
4. Spécifiez où les variables sont utilisées dans le script

### Étape 3 : Définir les paramètres

* **Étapes maximales** : Basé sur la complexité du script
* **Nombre maximal de tentatives** : dans quelle mesure le bot doit-il être persistant ?
* **Délai d'attente** : Combien de temps doit-il attendre les pages ?

### Étape 4 : Tester

1. Test avec des exemples de données
2. Vérifier que le bot peut accéder au site Web
3. Vérifier que l'extraction est correcte
4. Vérifiez si les variables fonctionnent correctement

***

## Conseils pour l'écriture de scénarios

### Langage clair

✅ **Faire :**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **À ne pas faire :**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Sélecteurs spécifiques

✅ **Faire :**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **À ne pas faire :**

```
Click somewhere
Type in a field
```

### Gestion des erreurs

✅ **Faire :**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **À ne pas faire :**

```
Click "Next" (assumes it's always there)
```

***

## Dépannage

### "Script expiré"

**Cause :** Le script a mis trop de temps à se terminer

**Solutions :**

* [ ] Réduire le nombre d'actions
* [ ] Augmenter la valeur « Pas maximum »
* [ ] Optimiser le script pour une exécution plus rapide
* [ ] Simplifiez ce que vous essayez d'extraire

### "Élément introuvable"

**Cause :** DocOperator n'a pas trouvé le bouton/champ que vous avez spécifié

**Solutions :**

* [ ] Vérifiez que le nom du bouton/champ est exactement correct
* [ ] Vérifiez si la présentation du site Web a changé
* [ ] Ajouter un temps d'attente avant de cliquer
* [ ] Vérifiez si le bouton n'apparaît que sous certaines conditions

### "Échec de la connexion"

**Cause :** Échec de l'authentification

**Solutions :**

* [ ] Vérifiez que le nom d'utilisateur et le mot de passe sont corrects
* [ ] Vérifiez si le mot de passe contient des caractères spéciaux
* [ ] Vérifiez que le compte n'est pas verrouillé
* [ ] Vérifiez si le processus de connexion a changé

### "Données non extraites correctement"

**Cause :** Le script s'est exécuté mais a extrait des informations erronées

**Solutions :**

* [ ] Vérifiez que le champ correct a été sélectionné
* [ ] Vérifiez si les données se trouvent à l'emplacement prévu
* [ ] Tester manuellement la logique d'extraction
* [ ] Ajoutez des étapes de débogage pour vérifier le contenu de la page

### "Le script s'exécute lentement"

**Cause :** Trop d'étapes ou site Web lent

**Solutions :**

* [ ] Supprimer les étapes inutiles
* [ ] Optimiser les temps d'attente
* [ ] Vérifier la connexion Internet
* [ ] Déterminez s'il existe une alternative à l'API

***

## Meilleures pratiques

✅ **Faire :**

* Testez minutieusement les scripts avant de les déployer
* Gardez les scripts simples et ciblés
* Ajouter des commentaires expliquant chaque étape
* Utilisez des noms de variables significatifs
* Surveiller les performances des scripts
* Avoir une solution de secours en cas d'échec des scripts

❌ **À ne pas faire :**

* Créez des scripts extrêmement longs (> 100 étapes)
* Mettez les mots de passe sensibles dans les journaux
* Fiez-vous à des coordonnées exactes (les sites Web changent)
* Créer des boucles sans conditions de sortie
* Ignorer les messages d'erreur

***

## Conseils de performances

* **Supprimer les étapes inutilisées** - Chaque étape prend du temps
* **Combiner des actions similaires** - Regrouper les clics liés
* **Optimiser les attentes** - Utiliser uniquement les délais nécessaires
* **Cache data** - N'extrayez pas les mêmes données deux fois
* **Traitement parallèle** - Exécutez plusieurs scripts si possible

***

## Considérations de sécurité

⚠️ **Important :**

* Ne stockez pas les mots de passe dans DocFlow
* Utilisez des méthodes sécurisées pour transmettre les informations d'identification
* N'enregistrez pas de données sensibles
* Surveiller ce qui est extrait
* Assurez-vous que l’activité du robot est enregistrée et vérifiable

***

## Exemple de variables

### Variables disponibles que vous pouvez utiliser :

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script utilisant des variables :

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Comparaison : quand utiliser DocOperator et API

| Situation              | Utiliser DocOperator | Utiliser l'API     |
| ---------------------- | --------------- | ----------- |
| Le site Web a une API        | ❌ Non            | ✅ Oui       |
| Le site Web est interactif | ✅ Oui           | ❌ Non        |
| Nécessite une connexion         | ✅ Oui           | Cela dépend     |
| Très rapide nécessaire       | ❌ Non            | ✅ Oui       |
| Flux de travail complexe       | ✅ Oui           | ❌ Peut-être pas |
| Les données changent quotidiennement     | ✅ Oui           | ✅ Oui       |

***

## Cartes associées

* **CALL\_API** - À utiliser lorsque l'API est disponible à la place
* **ACTION\_HTTPS\_REQUEST** - Requêtes plus simples
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Utiliser les données extraites
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Vérifier l'état de la demande
