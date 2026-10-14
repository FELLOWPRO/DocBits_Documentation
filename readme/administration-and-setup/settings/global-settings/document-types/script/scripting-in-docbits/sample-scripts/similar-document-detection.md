# Détection de documents similaires (recherche vectorielle)

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Utilise une recherche de similarité vectorielle pour trouver les documents sémantiquement proches du document actuel. Si un document présente plus de 95 % de similarité, le numéro de facture est signalé comme potentiellement frauduleux ou en double.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Explication étape par étape

1. **Obtenir l'ID du document actuel** à partir de `document_json`
2. **Trouver les documents similaires** avec `vector_search()`, qui retourne les 5 plus proches voisins
3. **Vérifier le seuil de similarité** : si un document dépasse 95 % de similarité, le signaler
4. **Marquer comme invalide** avec le nom du document similaire et son score de similarité

## Fonctionnement de la recherche vectorielle

Le texte OCR de chaque document est converti en un embedding vectoriel à 384 dimensions lors de l'indexation. `vector_search()` trouve les plus proches voisins dans cet espace vectoriel à l'aide de k-NN (k-Nearest Neighbors) et retourne les documents dont le contenu est sémantiquement proche, même si les mots exacts diffèrent.

**Cas d'usage :**
- Détection de fraude (factures quasi identiques provenant de « fournisseurs » différents)
- Détection de doublons qui va au-delà de la correspondance exacte du texte
- Recherche de documents liés dans différents formats ou langues

## Fonctions utilisées

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Trouver des documents sémantiquement similaires
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Afficher une erreur de validation
