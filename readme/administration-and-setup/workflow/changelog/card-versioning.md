# Système de versionnage des cartes - Mise à jour d'octobre 2025

**Document :** Aperçu du versionnage des cartes de flux de travail
**Dernière mise à jour :** 23 octobre 2025
**Statut :** Complet

---

## Aperçu

Le moteur de flux de travail DocBits utilise un **versionnage basé sur des entiers** pour gérer l'évolution des cartes tout en maintenant la rétrocompatibilité. Ce document fournit un aperçu du système de versionnage.

---

## Qu'est-ce que le versionnage des cartes ?

### Concept
Chaque carte de flux de travail peut avoir plusieurs versions, permettant au système de :
- Ajouter de nouvelles fonctionnalités sans casser les flux de travail existants
- Prendre en charge les fonctionnalités obsolètes tout en les retirant progressivement
- Faire évoluer les capacités des cartes au fil du temps
- Maintenir la rétrocompatibilité

### Structure des versions
- **Format :** Valeurs entières (1, 2, 3, 4, 5...)
- **Identification :** Clé composite de (card_type, card_version)
- **Statut :** Chaque version possède des indicateurs deprecated/enabled

### Exemple
La carte `tasks_create` a évolué à travers 4 versions :
- **v1 :** Création de tâche originale (obsolète)
- **v2 :** Ajout de la prise en charge de la traduction (obsolète)
- **v3 :** Prise en charge expérimentale de l'arbre de décision (obsolète)
- **v4 :** Prise en charge du type d'élément de travail générique (active actuelle)

---

## Statistiques clés

### Aperçu du versionnage
| Métrique | Valeur |
|--------|-------|
| **Cartes avec plusieurs versions** | 30+ |
| **Total des enregistrements de version** | 90+ |
| **Versions par carte (moyenne)** | 3 |
| **Versions maximum** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Versions obsolètes** | 9 |
| **Cartes entièrement désactivées** | 2 |

### Distribution des versions
- **2 versions :** 14 cartes (évolution plus simple)
- **3 versions :** 11 cartes (évolution modérée)
- **4 versions :** 4 cartes (évolution significative)
- **5 versions :** 1 carte (la plus évoluée : CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Modèles de versionnage courants

### Modèle 1 : Adoption des clés de traduction (v1 → v2)

**Concernées :** 15+ cartes

**Changement :**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Objectif :** Activer la prise en charge multilingue

**Cartes :** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, et plus

**Migration :** Sûre - aucun changement fonctionnel

---

### Modèle 2 : Intégration de l'arbre de décision (v2 → v3)

**Concernées :** 5 cartes

**Changement :** Ajout du paramètre d'arbre de décision

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Objectif :** Prendre en charge les résultats des tables de décision

**Cartes :**
- tasks_create (v3 obsolète)
- ACTION_TASK_FOR_GROUP (v3 obsolète)
- DOC_USER_ASSIGN (v3 obsolète)
- DOC_GROUP_ASSIGN (v3 obsolète)
- ACTION_DECISION_TREE_CREATE_TASKS

**Statut :** Obsolète - l'approche de l'arbre de décision était expérimentale

---

### Modèle 3 : Évolution vers le type générique (v3 → v4)

**Concernées :** 4 cartes

**Changement :** « Task » devient un type d'élément de travail flexible

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Objectif :** Prendre en charge les Tasks, Tickets, Issues et autres types d'éléments de travail

**Cartes :**
- tasks_create (v4 actuelle)
- ACTION_TASK_FOR_GROUP (v4 actuelle)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 actuelle)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 actuelle)

**Statut actuel :** Active et recommandée

---

### Modèle 4 : Paramètres de tolérance (cartes PO)

**Concernées :** 6 cartes de comparaison de PO

**Changement :** Ajout de la prise en charge de la tolérance/des écarts

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Objectif :** Permettre un écart acceptable dans le rapprochement (par ex. une différence de prix de 2 % est acceptable)

**Cartes clés :**
- CONDITION_DOC_TO_PO_UNIT_PRICE (a évolué jusqu'à v5 avec tolérance)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Avantage :** Critères de correspondance plus réalistes

---

### Modèle 5 : Paramètres de mode de comparaison

**Concernées :** 3 cartes de comparaison de PO

**Changement :** Prise en charge de différents algorithmes de comparaison

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Objectif :** Méthodes de comparaison flexibles

**Cartes :**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Modèle 6 : Déclencheurs de flux de travail

**Concernée :** STAUS_CHANGE uniquement

**Changement :** Déclenchement automatique des flux de travail lors d'un changement de statut

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Objectif :** Propager les changements de statut entre les flux de travail

---

## Cartes les plus évoluées

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versions)

**Chemin d'évolution :** v2 → v3 → v4 → v5

- **v2 :** Comparaison basique du prix unitaire
- **v3 :** Même clé de traduction (v2)
- **v4 :** Ajout du paramètre de mode de comparaison
- **v5 :** Ajout du paramètre de seuil de tolérance

**Actuelle :** v5 (avec prise en charge de la tolérance)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versions)

**Chemin d'évolution :** v1 → v2 → v3 → v4

- **v1 :** Correspondance basique des articles (obsolète)
- **v2 :** Ajout du paramètre de méthode de comparaison
- **v3 :** Amélioration avec des clés de traduction
- **v4 :** Ajout du paramètre de mode de comparaison

**Actuelle :** v4

**À éviter :** v1 (obsolète)

---

### 3. tasks_create (4 versions)

**Chemin d'évolution :** v1 → v2 → v3 → v4

- **v1 :** Implémentation originale (obsolète)
- **v2 :** Ajout de la prise en charge de la traduction (obsolète)
- **v3 :** Ajout de l'arbre de décision (obsolète)
- **v4 :** Types d'éléments de travail génériques (actuelle)

**Actuelle :** v4 (recommandée)

**Chronologie :**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Statut d'obsolescence

### Versions entièrement obsolètes (ne pas utiliser)

| Carte | Version | Raison | Alternative |
|------|---------|--------|-------------|
| tasks_create | v1 | Très ancienne | Utilisez v4 |
| tasks_create | v3 | Arbre de décision obsolète | Utilisez v4 |
| ACTION_TASK_FOR_GROUP | v3 | Arbre de décision obsolète | Utilisez v4 |
| DOC_USER_ASSIGN | v3 | Arbre de décision obsolète | Utilisez v2 |
| DOC_GROUP_ASSIGN | v3 | Arbre de décision obsolète | Utilisez v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Très ancienne | Utilisez v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Très ancienne | Utilisez v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Fonctionnalités annulées | Utilisez v3 |

### Cartes entièrement désactivées (inutilisables)

| Carte | Versions | Remarques |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Fonctionnalité non prise en charge |
| RUN_SCRIPT | v2, v3 | Remplacée par ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Recommandations de version

### Par cas d'usage

**Création d'un nouveau flux de travail :**
- Utilisez toujours le **numéro de version activé le plus élevé**
- Fournit les dernières fonctionnalités et améliorations
- Pris en charge et documenté

**Maintenance d'un flux de travail existant :**
- Continuez à utiliser la version actuelle si elle fonctionne
- Planifiez la migration lorsque c'est faisable
- Aucun besoin urgent de mise à niveau

**Migration d'un flux de travail hérité :**
- Identifiez la version actuellement utilisée
- Planifiez le chemin de mise à niveau
- Testez minutieusement avant le déploiement

---

## Comment fonctionnent les versions

### Sélection de version
Lors de la création d'un flux de travail, vous sélectionnez la version d'une carte à utiliser. Exemple :
- Utilisez `tasks_create v4` pour la création de nouvelles tâches (recommandé)
- Utilisez `tasks_create v2` si des systèmes hérités l'exigent (plus ancienne mais fonctionne)
- N'utilisez PAS `tasks_create v1` (obsolète)

### Rétrocompatibilité
- Les versions plus récentes ne cassent pas les flux de travail plus anciens
- Les anciens flux de travail continuent de fonctionner avec leur version d'origine
- Les flux de travail peuvent être mis à niveau progressivement

### Implémentation technique
Les versions sont gérées au niveau de la base de données :
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## À des fins de documentation

### Comprendre les informations de version
Lorsque vous voyez « Card v3 » dans la documentation :
- Cela fait référence à la version 3 de cette carte spécifique
- Consultez la [Référence complète du versionnage](../../docs/card_version.md) pour les détails
- Vérifiez quelle version est recommandée

### Vérifier votre version
Pour connaître la version que vous utilisez :
1. Ouvrez la carte dans votre flux de travail
2. Vérifiez le numéro de version affiché
3. Comparez avec les recommandations des guides

### Chronologie de l'évolution des versions
- **2024-2025 :** Évolution continue
- **Octobre 2025 :** Documentation complète du versionnage
- **Avenir :** Améliorations continues

---

## Documentation associée

### Référence complète
→ [Référence complète du versionnage des cartes](../../docs/card_version.md)

Inclut :
- Toutes les 30+ cartes avec versions
- Évolution détaillée du texte pour chacune
- Changements de paramètres spécifiques
- Requêtes SQL pour la recherche de version

### Guides spécifiques aux cartes
→ [Guides de flux de travail](../)

Documentation pour chaque carte avec recommandations de version

### Détails de l'historique des versions
Chaque guide inclut des informations de version et des notes de migration

---

## Référence rapide

### Cartes avec le plus de versions
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versions
2. CONDITION_OC_TO_PO_ITEMS - 4 versions
3. tasks_create - 4 versions
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versions
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versions

### Modèle d'évolution le plus courant
**Adoption des clés de traduction (v1 → v2)** - 15+ cartes

### Changement le plus significatif
**Évolution vers le type générique (v3 → v4)** - Passage de « Task » à un type d'élément de travail flexible

### Entièrement désactivées
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Questions fréquemment posées

### Q : Quelle version dois-je utiliser ?
R : Utilisez la **version activée la plus élevée**, sauf si vous avez une raison spécifique d'utiliser une version plus ancienne.

### Q : Puis-je mettre à niveau mon flux de travail vers une version plus récente ?
R : Oui, mais testez minutieusement. Certaines versions ont des exigences de paramètres différentes.

### Q : Que se passe-t-il si j'utilise une version obsolète ?
R : Elle continue de fonctionner, mais vous ne bénéficierez pas des nouvelles fonctionnalités. La migration est recommandée.

### Q : Puis-je utiliser une carte désactivée ?
R : Non, les cartes désactivées ne peuvent pas être utilisées. Utilisez plutôt l'alternative recommandée.

### Q : Comment savoir si ma carte doit être mise à niveau ?
R : Consultez la [Référence complète du versionnage](../../docs/card_version.md) pour votre type de carte et suivez les recommandations.

---

## Bonnes pratiques

1. **Nouveaux flux de travail :** Utilisez la dernière version stable
2. **Mises à jour :** Vérifiez périodiquement les nouvelles versions
3. **Tests :** Testez d'abord les mises à niveau de version en environnement de test (sandbox)
4. **Documentation :** Référez-vous aux guides spécifiques aux cartes pour les détails de version
5. **Migration :** Planifiez les mises à niveau de manière incrémentale
6. **Support :** Contactez le support si des questions de compatibilité de version se posent

---

## Tableau récapitulatif

| Type de carte | Version actuelle | Total des versions | Statut | Remarques |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Active | La plus évoluée ; v3 obsolète |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Active | Nombre de versions le plus élevé |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Active | v1 obsolète |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Active | v3 obsolète |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Active | v4 obsolète/désactivée |
| La plupart des cartes | 2 | 2 | Active | Modèle v1 → v2 |

---

## Voir aussi

- 📖 [Référence complète du versionnage des cartes](../../docs/card_version.md)
- 🔗 [Guides de flux de travail](../)
- 📋 [Notes de version d'octobre 2025](./2025-10-october.md)
- 🔄 [Analyse de la liaison des flux de travail](../../WORKFLOW_LINKING_MAP.md)

---

**Dernière mise à jour :** 23 octobre 2025
**Source :** base de données postgres-dev-docflow
**Statut :** Référence complète
