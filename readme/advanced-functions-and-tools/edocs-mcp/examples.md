# Exemples

Retrouvez les prompts et la procédure de diagnostic, brouillon, activation et retour arrière dans [Configurer DocBits avec Claude ou Codex](../docbits-mcp/configuration-with-claude-or-codex.md). Les exemples utilisent les arguments actuels. Remplacez tous les paramètres fictifs par les valeurs de votre organisation et fournissez des sources complètes correctement échappées en chaînes JSON.

## 1. Modifier une règle Custom existante

Lisez la `TRANSFORMATION` effective avec `get_edoc_attribute_source`, en utilisant le libellé exact du format renvoyé par la classification :

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Notez `attribute_id`, `active_value_id`, `active_version` et `value`. Lisez séparément `source: "default"` pour comparer, puis l’historique avec `list_edoc_attribute_versions`. La suite suppose un attribut Custom existant appartenant à votre organisation.

Prévisualisez le candidat complet sans l’enregistrer avec `preview_edoc_custom_xslt`. Utilisez un document déjà présent dans la même organisation :

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Le résultat est du XML transformé pour `TRANSFORMATION`, un PDF pour `PREVIEW` ou des champs/tableaux pour `EXTRACTION_PATHS`. L’aperçu ne sélectionne pas de brouillon enregistré et ne teste ni scripts ultérieurs ni exports.

Après examen du diff et de l’aperçu, relisez la source active puis enregistrez un brouillon avec `update_edoc_custom_attribute`. Passez explicitement `activate: false` ; la valeur par défaut est `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Après les tests dans l’organisation de test et confirmation de la modification précise, appelez `activate_edoc_attribute_version`. `draft_id` est l’ID de valeur de version. Relisez la source effective. Pour revenir en arrière, utilisez l’ancien `active_value_id` dans le même appel.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Si aucun attribut Custom n’existe

`create_edoc_custom_attribute` crée une première version immédiatement active, pas un brouillon. Testez la nouvelle personnalisation dans une organisation de test ou utilisez le parcours pris en charge par l’éditeur DocBits. Ne créez ou supprimez pas de personnalisation de production uniquement pour obtenir un aperçu. Préservez les correspondances nécessaires ; ne modifiez pas globalement les règles partagées par défaut.

## 3. Tester la configuration active

Appelez `test_electronic_document` avec le XML d’origine encodé en base64 :

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Ce test utilise les règles actives sans enregistrer de document, et non un brouillon inactif. MCP HTTP distant ne peut pas lire un `file_path` local de votre machine. `compare_edoc_extraction` compare uniquement les Extraction Paths et nécessite un attribut personnalisé de chemins d’extraction ; il ne compare pas les transformations.

`validate_all_edocs` teste à blanc les fichiers disponibles sur le serveur. `verify_electronic_documents` les téléverse et les traite, créant des documents. Aucun ne prouve la livraison à l’ERP. Utilisez des exemples représentatifs, contrôlez séparément champs/montants enregistrés et export, et ne redémarrez pas en masse les anciens documents.
