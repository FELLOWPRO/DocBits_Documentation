---
hidden: true
---

# Publication des cartes de flux de travail et historique des versions

## Principes de contrôle de version

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>Système de contrôle de version des flux de travail</figcaption></figure>

### Version 8.5.2024 - Fonctionnalités principales de versionnage

Le moteur de flux de travail DocBits met en œuvre un contrôle de version robuste pour toutes les cartes de flux de travail :

1. **Contrôle de version** : Chaque carte peut avoir plusieurs versions, chacune représentant un ensemble différent de conditions ou d'actions. Cela vous permet d'expérimenter ou d'ajuster les règles sans affecter le flux de travail actuellement actif.
2. **Mises à niveau transparentes** : Lorsque vous devez mettre à jour une règle ou une condition en raison de changements dans vos exigences de traitement de documents, vous pouvez créer une nouvelle version de la carte. Cette approche garantit que toute modification est délibérée et testée avant de remplacer la version actuelle. Elle minimise les erreurs et les perturbations potentielles dans votre traitement de documents.
3. **Maintien de la cohérence** : Conserver la version originale de la carte inchangée jusqu'à ce que vous décidiez de la mettre à niveau garantit que les processus en cours ne sont pas affectés. Vous pouvez exécuter des tests et des validations sur la nouvelle version sans impacter les données ou les flux de travail en production.
4. **Flexibilité et tests** : Plusieurs versions permettent de tester différents scénarios dans un environnement contrôlé. Vous pouvez observer les effets de nouvelles règles ou de changements sur votre flux de travail de traitement de documents sans apporter de modifications permanentes. Une fois satisfait des résultats, vous pouvez alors choisir d'appliquer la nouvelle version.

---

## Aperçu du versionnage des cartes

### Statistiques

| Métrique | Valeur |
|--------|-------|
| **Cartes avec plusieurs versions** | 30+ |
| **Total des enregistrements de version** | 90+ |
| **Versions actives actuelles** | 81+ |
| **Versions obsolètes** | 9 |
| **Cartes entièrement désactivées** | 2 |
| **Dernière version (max)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Plage de versions
- **Minimum :** v1
- **Maximum :** v5
- **Moyenne de versions par carte :** 3

---

## Modifications détaillées des versions de cartes

### 🔧 CARTES D'ACTION - Intégration externe et exécution

#### 1. CALL_API
**Versions :** v1, v2 (Actuelle : v2)

📖 **Guide :** [Guide d'appel d'API externe](../then/action/call-api-guide.md)

| Version | Traduction | Statut | Changements clés |
|---------|-------------|--------|-------------|
| v1 | Non | Active | Appel d'API basique sans clés de traduction |
| v2 | Oui | ✅ Actuelle | Ajout de `trnsl_%call_api` pour la prise en charge multilingue |

**Ce qui a changé :** Ajout de la prise en charge de l'internationalisation (i18n) avec des clés de traduction. La fonctionnalité reste identique.

**Avant (v1) :**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Après (v2) :**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Recommandation :** Utilisez v2 pour tous les nouveaux flux de travail (inclut la prise en charge linguistique)
**Rétrocompatibilité :** ✅ v1 fonctionne toujours

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versions :** v1, v2 (Actuelle : v2)

| Version | Traduction | Statut | Changements clés |
|---------|-------------|--------|-------------|
| v1 | Non | Active | Requête HTTP simple |
| v2 | Oui | ✅ Actuelle | Ajout des clés de traduction `trnsl_%send_https_request` |

**Ce qui a changé :** Ajout de la prise en charge de la traduction. La fonctionnalité principale de webhook/requête est inchangée.
**Recommandation :** Utilisez v2 (prise en charge multilingue)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versions :** v2 (Actuelle), v3, v4 (Obsolètes et désactivées)

| Version | Traduction | Statut | Changements clés |
|---------|-------------|--------|-------------|
| v2 | Oui | Active | Implémentation DocOperator originale |
| v3 | Oui | Active | Ajout du paramètre « Execute the prompt » pour un contrôle supplémentaire |
| v4 | Oui | ❌ OBSOLÈTE ET DÉSACTIVÉE | Suppression du paramètre « Execute » (annulé) |

**Chemin d'évolution :** v2 → v3 (paramètre ajouté) → v4 (annulé - non recommandé)

**Ce qui a changé :**
- v2 → v3 : Ajout d'un paramètre optionnel de contrôle d'exécution pour plus de flexibilité
- v3 → v4 : Suppression du paramètre après analyse approfondie (obsolète)

**Recommandation :** Utilisez v3 pour les nouveaux flux de travail (dernière version active avec toutes les fonctionnalités)
**Migration :** Si vous utilisez v4, passez à v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versions :** v2, v3 (Obsolète), v4 (Actuelle)

📖 **Guide :** [Guide d'assignation de tâches](../then/task/task-assignment-guide.md)

| Version | Changements | Statut | Paramètre de type |
|---------|---------|--------|-----------------|
| v2 | Implémentation originale | Active | « Task » (fixe) |
| v3 | + Prise en charge de l'arbre de décision | ❌ OBSOLÈTE | « Task » (fixe) |
| v4 | - Arbre de décision, + Type générique | ✅ Actuelle | Type générique (flexible) |

**Évolution :** v2 → v3 (expérimentation de l'arbre de décision) → v4 (types génériques, arbre de décision supprimé)

**Changement v2 → v3 (expérimentation de l'arbre de décision) :**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Changement v3 → v4 (types génériques + suppression de l'arbre de décision) :**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Ce qui a changé :**
- v2 → v3 : Ajout du paramètre `decision tree, if available: [param]`
- v3 → v4 :
  - ❌ Suppression du paramètre d'arbre de décision
  - ✅ Changement de « Task » → `[param]` générique (prend en charge Task, Ticket, Issue, etc.)
  - Ajout de la clé de traduction `trnsl_%task_for_group_v4`

**Pourquoi :** L'approche de l'arbre de décision en v3 était expérimentale. v4 offre une meilleure flexibilité avec des types d'éléments de travail génériques.
**Recommandation :** Utilisez v4 (actuelle, la plus flexible)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versions :** v2, v3 (Actuelle)

| Version | Type de tâche | Statut | Différence clé |
|---------|-----------|--------|-----------------|
| v2 | « task » (fixe) | Active | Version originale |
| v3 | Type générique | ✅ Actuelle | Passage à `[param]` flexible |

**Ce qui a changé :** v2 → v3 : « Create a new task » → « Create a new [param] » (prend en charge tout type d'élément de travail)
**Recommandation :** Utilisez v3

---

#### 6. RUN_WORKFLOW
**Versions :** v1, v2 (Actuelle)

**Ce qui a changé :** v1 → v2 : Ajout des clés de traduction `trnsl_%run_workflow`
**Recommandation :** Utilisez v2

---

### 📊 CARTES DE COMPARAISON ET DE VALIDATION DE PO

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (La plus évoluée - 5 versions)
**Versions :** v2, v3, v4, v5 (Actuelle)

📖 **Guide :** [Guide complet du rapprochement de PO](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Version | Changements | Statut | Tolérance | Comparaison |
|---------|---------|--------|-----------|------------|
| v2 | Comparaison de prix basique | Active | ❌ Non | Basique |
| v3 | Identique à v2 | Active | ❌ Non | Basique |
| v4 | + Paramètre de mode de comparaison | Active | ❌ Non | ✅ Oui |
| v5 | + Paramètres de tolérance | ✅ Actuelle | ✅ Oui (montant + unité) | ✅ Oui |

**Chemin d'évolution :** v2 → v3 (aucun changement) → v4 (modes de comparaison) → v5 (seuils de tolérance)

**v2 → v3 :** Aucun changement fonctionnel (même clé de traduction)

**Changement v3 → v4 (ajout du mode de comparaison) :**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Changement v4 → v5 (ajout des paramètres de tolérance) :**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Ce qui a changé :**
- **v2 → v3 :** Aucun changement fonctionnel
- **v3 → v4 :** Ajout de `Compare as [param]` - Prise en charge de différents opérateurs de comparaison
- **v4 → v5 :** Ajout des paramètres de tolérance :
  - `with tolerance of [amount] [unit]`
  - Exemple : « with tolerance of 2 % » ou « with tolerance of 100 EUR »
  - Prend en charge : %, EUR, $ et autres devises

**Cas d'usage :**
- v2/v3 : Correspondance stricte (prix exacts uniquement)
- v4 : Différentes méthodes de comparaison
- v5 : Acceptation flexible des écarts (par ex. accepter des différences de prix de 2 %) ✅ RECOMMANDÉE

**Recommandation :** Utilisez v5 pour les flux de travail modernes de rapprochement de PO

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versions :** v1 (Obsolète), v2, v3, v4 (Actuelle)

| Version | Changements | Statut | Fonction de comparaison |
|---------|---------|--------|-----------------|
| v1 | Pas de traduction, pas de méthode | ❌ OBSOLÈTE | Basique |
| v2 | + Clés de traduction, + méthode | Active | Méthode basique |
| v3 | Identique à v2 | Active | Méthode basique |
| v4 | + Paramètres de mode de comparaison | ✅ Actuelle | ✅ Flexible |

**Ce qui a changé :**
- **v1 → v2 :** Ajout de `trnsl_%in_order_confirmations_matches_purchase_order` + paramètre de méthode de comparaison
- **v2 → v3 :** Aucun changement
- **v3 → v4 :** Ajout de `Compare as [param1] [param2]` pour des modes de comparaison flexibles

**Recommandation :** Utilisez v4 (évitez v1 qui est obsolète)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versions :** v2, v3 (Actuelle)

| Version | Jours de tolérance | Jours de tolérance acceptés | Statut |
|---------|-----------------|------------------------|--------|
| v2 | ❌ Non | ❌ Non | Active |
| v3 | ✅ Oui | ✅ Oui | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 : Ajout des paramètres de tolérance :
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Exemple :** Accepter les dates de livraison dans un délai de 5 jours par rapport à la date promise
**Recommandation :** Utilisez v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versions :** v2, v3, v4 (Actuelle)

| Version | Mode de comparaison | Statut |
|---------|-----------------|--------|
| v2 | Basique | Active |
| v3 | Basique (aucun changement) | Active |
| v4 | ✅ Sélection de mode flexible | ✅ Actuelle |

**Ce qui a changé :** v3 → v4 : Ajout de `compare [param]` pour différentes approches de comparaison
**Recommandation :** Utilisez v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versions :** v2, v3, v4 (Actuelle)

| Version | Mode de comparaison | Statut |
|---------|-----------------|--------|
| v2 | Standard | Active |
| v3 | Standard (aucun changement) | Active |
| v4 | ✅ Flexible | ✅ Actuelle |

**Ce qui a changé :** v3 → v4 : Ajout du paramètre `compare [param]`
**Recommandation :** Utilisez v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versions :** v2, v3 (Actuelle)

| Version | Type de livraison | Table de données de référence | Statut |
|---------|---------------|-------------------|--------|
| v2 | « Confirmed » (fixe) | Référence fixe | Active |
| v3 | [Paramètre configurable] | `[param]` dynamique | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 :
- Changement de « Confirmed delivery » → `[param] delivery` (type de livraison flexible)
- Changement de la référence de table fixe → `stored in [param]` (sélection de table dynamique)

**Flexibilité :** v3 permet différents types de dates de livraison et tables de fournisseurs
**Recommandation :** Utilisez v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versions :** v2, v3 (Actuelle)

| Version | Référence de table fournisseur | Statut |
|---------|--------------------------|--------|
| v2 | « supplier item price table » (fixe) | Active |
| v3 | `[param]` dynamique | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 : Référence de table fixe → `stored in [param]` (permet la sélection de table dynamique)
**Recommandation :** Utilisez v3

---

### 👥 CARTES D'ASSIGNATION ET DE ROUTAGE

#### 1. DOC_USER_ASSIGN
**Versions :** v1, v2, v3 (Obsolète)

| Version | Traduction | Arbre de décision | Statut |
|---------|-------------|---------------|--------|
| v1 | Non | ❌ Non | Active |
| v2 | Oui | ❌ Non | ✅ Actuelle |
| v3 | Oui | ✅ Oui | ❌ OBSOLÈTE |

**Évolution :** v1 (sans i18n) → v2 (avec i18n) → v3 (+ expérimentation de l'arbre de décision, maintenant obsolète)

**Ce qui a changé :**
- v1 → v2 : Ajout des clés de traduction
- v2 → v3 : Ajout de la prise en charge de l'arbre de décision (expérimentale, obsolète)

**Recommandation :** Utilisez v2 (stable avec prise en charge i18n)

---

#### 2. DOC_GROUP_ASSIGN
**Versions :** v2, v3 (Obsolète)

| Version | Arbre de décision | Statut |
|---------|---------------|--------|
| v2 | ❌ Non | ✅ Actuelle |
| v3 | ✅ Oui | ❌ OBSOLÈTE |

**Ce qui a changé :** v2 → v3 : Ajout de `Use decision tree, if available [param]` (ultérieurement rendu obsolète)
**Recommandation :** Utilisez v2

---

#### 3. OC_ASSIGN_DOC
**Versions :** v1, v2 (Actuelle)

**Ce qui a changé :** v1 → v2 : Ajout des clés de traduction `trnsl_%oc_assign_doc`
**Recommandation :** Utilisez v2

---

### 📋 CARTES DE GESTION DES TÂCHES

#### 1. tasks_create ⭐ (Carte de tâche la plus évoluée - 4 versions)
**Versions :** v1 (Obsolète), v2 (Obsolète), v3 (Obsolète), v4 (Actuelle)

📖 **Guide :** [Guide d'assignation de tâches](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Version | Traduction | Arbre de décision | Type d'élément de travail | Statut |
|---------|-------------|---------------|-----------------|--------|
| v1 | Non | Non | « Task » (fixe) | ❌ OBSOLÈTE |
| v2 | Oui | Non | « Task » (fixe) | ❌ OBSOLÈTE |
| v3 | Oui | Oui | « Task » (fixe) | ❌ OBSOLÈTE |
| v4 | Oui | Non | `[param]` générique | ✅ Actuelle |

**Chronologie de l'évolution :**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Changement v1 → v2 (ajout des clés de traduction) :**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Changement v2 → v3 (expérimentation de l'arbre de décision) :**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Changement v3 → v4 (types génériques + suppression de l'arbre de décision) :**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Ce qui a changé :**
- **v1 → v2 :** Ajout des clés de traduction `trnsl_%tasks_create`
- **v2 → v3 :**
  - Ajout de la prise en charge de l'arbre de décision : `Use decision tree, if available: [param]`
  - Changement de « assign to user » → « assign it to the user »
- **v3 → v4 :**
  - ❌ Suppression du paramètre d'arbre de décision
  - ✅ Changement de « Task » → `[param]` générique (prend en charge Task, Ticket, Issue, etc.)
  - Mise à jour de la clé de traduction en `trnsl_%tasks_create_v4`

**Note sur l'arbre de décision :** v3 utilisait des arbres de décision pour assigner dynamiquement les tâches. Cette approche était expérimentale et a été rendue obsolète en v4 au profit d'une sélection directe du type d'élément de travail basée sur des paramètres.

**Recommandation :** Utilisez exclusivement v4 pour les nouveaux flux de travail
**Migration :** Si vous utilisez v1, v2 ou v3, passez à v4 ✅

---

#### 2. OC_TASK
**Versions :** v1, v2 (Actuelle)

**Ce qui a changé :** v1 → v2 : Ajout des clés de traduction `trnsl_%oc_task`
**Recommandation :** Utilisez v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versions :** v1, v3 (Actuelle - v2 ignorée)

| Version | Type d'élément de travail | Statut |
|---------|-----------------|--------|
| v1 | « Task » (fixe) | Active |
| v3 | `[param]` générique | ✅ Actuelle |

**Ce qui a changé :** v1 → v3 : Évolution vers un type générique (v2 a été ignorée en production)
**Recommandation :** Utilisez v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versions :** v2, v3 (Actuelle)

| Version | Texte d'assignation | Statut |
|---------|-----------------|--------|
| v2 | « Assign task with title » | Active |
| v3 | « Assign [generic] with title » | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 :
- Changement de « Assign task » → « Assign [generic param] »
- Changement de « return of decision » → « return of decision table » (terminologie plus claire)

**Recommandation :** Utilisez v3

---

### 🔄 CARTES DE CONTRÔLE DES DOCUMENTS

#### APPROVE
**Versions :** v1, v2 (Actuelle)
**Changement :** Ajout des clés de traduction `trnsl_%approve_doc`
**Recommandation :** Utilisez v2

---

#### REJECT
**Versions :** v1, v2 (Actuelle)
**Changement :** Ajout des clés de traduction `trnsl_%reject_doc`
**Recommandation :** Utilisez v2

---

#### STAUS_CHANGE (Changement de statut)
**Versions :** v1, v2, v3 (Actuelle)

| Version | Déclencheur de flux de travail | Statut |
|---------|-----------------|--------|
| v1 | ❌ Non | Active |
| v2 | ❌ Non | Active |
| v3 | ✅ Oui | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 : Ajout de `trigger Workflows [param]` - Déclenchement automatique des flux de travail lors d'un changement de statut
**Recommandation :** Utilisez v3

---

#### EXPORT
**Versions :** v1, v2, v3 (Actuelle)

| Version | Validation | Statut |
|---------|------------|--------|
| v1 | ❌ Non | Active |
| v2 | ❌ Non | Active |
| v3 | ✅ Oui | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 : Ajout de `Start Export with Validation: [param]`
**Recommandation :** Utilisez v3

---

### 🧮 CARTES DE MANIPULATION DES DONNÉES

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Modèle :** v1 → v2 (clés de traduction ajoutées)
**Recommandation :** Utilisez v2 pour toutes

---

#### CONDITION_DECISION_TREE_DATA
**Versions :** v2, v3 (Actuelle)

| Version | Utilisation des données | Statut |
|---------|------------|--------|
| v2 | « Use return data in later cards » | Active |
| v3 | « [Explicit param] returned data for use in subsequent cards » | ✅ Actuelle |

**Ce qui a changé :** v2 → v3 : Contrôle plus explicite de l'extraction des données de l'arbre de décision
**Recommandation :** Utilisez v3

---

### ❌ CARTES DÉSACTIVÉES (Ne pas utiliser)

#### DOC_SUBORG_CHANGE
**Versions :** v1, v2 (toutes deux désactivées)
**Statut :** Plus prise en charge
**Alternative :** Utilisez les fonctionnalités d'assignation de documents

---

#### RUN_SCRIPT
**Versions :** v2, v3 (toutes deux désactivées)
**Statut :** Remplacée par ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternative :** Utilisez ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Modèles de versionnage courants

### Modèle 1 : Adoption des clés de traduction (v1 → v2)
**Concernées :** 15+ cartes

**Changement :** Ajout des clés de traduction `trnsl_%[card_name]`
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Cartes :** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, et plus
**Impact :** Active la prise en charge multilingue

---

### Modèle 2 : Intégration de l'arbre de décision (v2 → v3) - OBSOLÈTE
**Concernées :** 5 cartes (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Changement :** Ajout d'un paramètre optionnel d'arbre de décision
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Statut :** ❌ Majoritairement obsolète (sauf ACTION_DECISION_TREE_CREATE_TASKS)
**Raison :** Approche directe par paramètre, plus simple, préférée

---

### Modèle 3 : Évolution vers le type générique (v3 → v4)
**Concernées :** 4 cartes (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Changement :** « Task » → paramètre de type générique
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Impact :** Prend en charge Task, Ticket, Issue et autres types d'éléments de travail
**Avantage :** Plus grande flexibilité et réutilisabilité

---

### Modèle 4 : Paramètres de tolérance (cartes PO)
**Concernées :** 6 cartes (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, etc.)

**Changement :** Ajout de la prise en charge de la tolérance/des écarts
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Exemples :**
- « with tolerance of 2 % »
- « with tolerance of 100 EUR »
- « with 5 days as tolerance »

**Impact :** Critères de correspondance réalistes (toutes les valeurs ne doivent pas correspondre exactement)

---

### Modèle 5 : Paramètres de mode de comparaison
**Concernées :** 3 cartes (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Changement :** Ajout d'une sélection flexible de la méthode de comparaison
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Impact :** Prise en charge de différents algorithmes de comparaison

---

## ✅ Recommandations de version

### Pour les nouveaux flux de travail
**Règle :** Utilisez toujours le numéro de version activé le plus élevé
- Fournit les dernières fonctionnalités
- Meilleure prise en charge
- Le plus testé
- Approche recommandée

### Pour les flux de travail existants
**Approche sûre :**
- Continuez à utiliser la version actuelle si elle fonctionne
- Planifiez une migration progressive vers les versions plus récentes
- Testez d'abord les mises à niveau en environnement de test (sandbox)

### Priorité de migration

| Priorité | Cartes | Action |
|----------|-------|--------|
| **Haute** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Mettre à niveau vers la version actuelle |
| **Moyenne** | Autres mises à niveau de traduction v1/v2, cartes PO v2/v3 | Envisager la mise à niveau |
| **Basse** | Cartes sans changement fonctionnel | Optionnel |

---

## ⚠️ Versions obsolètes - Ne pas utiliser

| Carte | Version | Raison | Utiliser à la place |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Très anciennes, ou arbre de décision obsolète | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Approche de l'arbre de décision obsolète | v4 |
| DOC_USER_ASSIGN | v3 | Approche de l'arbre de décision obsolète | v2 |
| DOC_GROUP_ASSIGN | v3 | Approche de l'arbre de décision obsolète | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Très ancienne | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Très ancienne | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Fonctionnalités annulées | v3 |

---

## 🔄 Cartes entièrement désactivées - Inutilisables

| Carte | Versions | Raison | Alternative |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Plus prise en charge | Cartes d'assignation de documents |
| RUN_SCRIPT | v2, v3 | Remplacée par DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Documentation associée

- 📖 [Référence du versionnage des cartes](../changelog/card-versioning.md) - Informations détaillées sur les versions
- 📚 [Guides de flux de travail](../) - Utilisation des cartes étape par étape
- 🔄 [Base de données des versions de cartes](../docs/card_version.md) - Historique complet des versions
- 📋 [Journaux de flux de travail](../workflow-logs/) - Exécution et débogage

---

**Dernière mise à jour :** 23 octobre 2025
**Statut :** Historique complet des versions
**Source de la base de données :** postgres-dev-docflow
