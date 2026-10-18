# eDocs MCP

L'API DocBits expose un serveur **Model Context Protocol (MCP)** doté d'outils pour inspecter et personnaliser le traitement des documents électroniques (eDoc). Tout client compatible MCP — Claude Code, Claude Desktop ou des intégrations personnalisées — peut s'y connecter et utiliser ces outils.

## Que pouvez-vous faire ?

Avec les outils eDocs MCP, vous pouvez :

- **Inspecter** la façon dont chaque type de document électronique est classifié et quelles règles d'extraction s'appliquent
- **Tester** des documents dans l'ensemble du pipeline de traitement sans les enregistrer dans la base de données
- **Créer des règles personnalisées** pour votre organisation — aperçus XSLT, chemins d'extraction, transformations
- **Mettre à jour** une règle personnalisée avec une nouvelle version (avec ou sans activation immédiate)
- **Supprimer** une règle personnalisée pour revenir à la règle intégrée par défaut
- **Vérifier** que tous les fixtures eDoc pris en charge sont traités correctement

## Modèle d'autorisations

DocBits fournit une bibliothèque de règles par défaut intégrées, partagées entre tous les clients. Ces règles par défaut utilisent l'ID d'organisation réservé `00000000-0000-0000-0000-000000000000`.

**Les règles par défaut sont immuables via MCP.** Chaque outil d'écriture vérifie l'ID de votre organisation avant d'effectuer la moindre requête. S'il correspond à l'organisation par défaut, l'opération est immédiatement rejetée — aucun appel API n'est jamais effectué.

Les clients peuvent uniquement créer, modifier ou supprimer des règles **au sein de leur propre organisation**. Lorsqu'une règle personnalisée existe pour votre organisation, elle est prioritaire sur la règle par défaut. La suppression d'une règle personnalisée rétablit automatiquement le comportement par défaut.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Aperçu des outils

### Inspection (lecture seule)

| Outil | Description |
|------|-------------|
| `test_electronic_document` | Exécute à blanc l'ensemble du pipeline eDoc — classification, extraction, aperçu — sans enregistrement |
| `list_electronic_document_types` | Liste tous les types d'eDoc pris en charge avec leur état de configuration |
| `get_extraction_rules` | Affiche les règles XPath utilisées pour extraire les champs d'un type de document donné |
| `get_extracted_fields` | Récupère les champs d'en-tête extraits d'un document traité |
| `get_extracted_tables` | Récupère les lignes extraites d'un document traité |
| `get_preview_pdf` | Récupère le PDF d'aperçu généré par XSLT pour un document |
| `get_preview_image` | Récupère une image de page rendue pour un document traité |
| `extract_edoc_table` | Extrait un fichier XML/EDI que vous transmettez et renvoie les champs sous forme de tableau plat, avec la règle qui a produit chacun d'eux |
| `compare_edoc_extraction` | Compare l'extraction par défaut et votre extraction personnalisée (et éventuellement une règle candidate) sur un document |

### Personnalisation (limitée à l'organisation, organisation par défaut bloquée)

| Outil | Description |
|------|-------------|
| `list_edoc_custom_attributes` | Liste les remplacements personnalisés de votre organisation par rapport aux règles par défaut intégrées pour un type de document |
| `create_edoc_custom_attribute` | Crée une nouvelle règle personnalisée (EXTRACTION_PATHS, TRANSFORMATION ou PREVIEW) |
| `update_edoc_custom_attribute` | Ajoute une nouvelle version d'une règle personnalisée, avec activation immédiate en option |
| `delete_edoc_custom_attribute` | Supprime une règle personnalisée — le système revient automatiquement à la règle par défaut |
| `preview_edoc_custom_xslt` | Exécute à blanc une transformation XSLT sur un document XML avant l'activation |
| `get_edoc_attribute_source` | Récupère la source modifiable d'un attribut (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) afin de la modifier |
| `list_edoc_attribute_versions` | Historique des versions d'un attribut personnalisé : brouillons et version active |
| `activate_edoc_attribute_version` | Active une version ou un brouillon précis (c'est ainsi que l'on effectue un retour arrière) |
| `delete_edoc_attribute_draft` | Supprime un brouillon qui n'a jamais été activé |

### Vérification

| Outil | Description |
|------|-------------|
| `verify_electronic_documents` | Téléverse des fixtures et vérifie de bout en bout la classification, l'extraction et l'aperçu |
| `validate_all_edocs` | Exécute tous les fixtures eDoc dans un pipeline à blanc et signale les problèmes |

## Types d'attributs

Chaque règle personnalisable possède un type et un format spécifiques :

| Nom de l'attribut | Format | Objectif |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | Expressions XPath qui associent les nœuds XML aux champs DocBits |
| `TRANSFORMATION` | XSLT | Feuille de style appliquée au XML avant l'extraction |
| `PREVIEW` | XSLT | Feuille de style qui génère l'aperçu PDF lisible par l'humain |
| `STRUCTURE_DESCRIPTOR` | JSON | Carte de structure pour les documents EDI uniquement |

L'outil `create_edoc_custom_attribute` déduit automatiquement le format correct à partir du nom de l'attribut.

## Démarrage rapide

### Lister ce que votre organisation a personnalisé

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Renvoie deux listes : `custom` (les remplacements de votre organisation) et `default` (les règles partagées dont vous héritez).

### Créer un aperçu personnalisé pour XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Renvoie le nouvel `attribute_id` — conservez-le pour les mises à jour et la suppression.

### Mettre à jour une règle personnalisée existante

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Crée une nouvelle version et l'active. La version précédente est conservée dans l'historique.

### Revenir à la règle par défaut

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Supprime le remplacement personnalisé. Le système revient immédiatement à la règle par défaut intégrée.

## Règles de sécurité

| Action | Autorisée |
|--------|---------|
| Lire les règles par défaut | ✅ Oui |
| Créer une règle personnalisée pour votre organisation | ✅ Oui |
| Mettre à jour une règle personnalisée de votre organisation | ✅ Oui |
| Supprimer une règle personnalisée de votre organisation | ✅ Oui |
| Modifier ou supprimer les règles par défaut | ❌ **Jamais** — bloqué au niveau de la couche MCP |

Toute tentative d'écriture sur `00000000-0000-0000-0000-000000000000` renvoie :

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

## Règles effectivement utilisées et activation

Si un avoir électronique apparaît comme Invoice, suivez le [guide de diagnostic de la classification](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md). Il couvre la source personnalisée ou par défaut effectivement utilisée, les codes de type, Extraction Paths et l’activation en toute sécurité.

[Configurer DocBits avec Claude ou Codex](../docbits-mcp/configuration-with-claude-or-codex.md) : connexion, prompts, aperçus, modifications versionnées, contrôles et retour arrière.
