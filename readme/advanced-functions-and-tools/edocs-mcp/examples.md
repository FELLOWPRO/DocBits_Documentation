# Exemples

Exemples de bout en bout montrant comment utiliser ensemble les outils eDocs MCP.

## Exemple 1 : Créer un aperçu personnalisé pour XRechnung

Cet exemple parcourt le cycle de vie complet d'une règle PREVIEW personnalisée :
1. Vérifier quelles règles existent déjà
2. Prévisualiser le XSLT sans l'activer
3. Créer la règle personnalisée
4. La mettre à jour vers une nouvelle version
5. Revenir à la règle par défaut

### Étape 1 : Vérifier les personnalisations existantes

Appelez `list_edoc_custom_attributes` :

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

La réponse affiche deux listes. Si `custom` est vide pour l'attribut `PREVIEW`, votre organisation utilise actuellement la feuille de style d'aperçu par défaut intégrée.

### Étape 2 : Tester votre XSLT avant de le créer

Appelez `preview_edoc_custom_xslt` avec l'ID d'un attribut existant (utilisez un attribut par défaut de la réponse de `list`) et un exemple de fichier XML encodé en base64 :

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Examinez le résultat rendu pour vérifier que votre XSLT produit le résultat attendu avant de l'enregistrer.

### Étape 3 : Créer la règle personnalisée

Appelez `create_edoc_custom_attribute` :

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Conservez l'`attribute_id` de la réponse. À partir de maintenant, chaque facture XRechnung 2.1 CII traitée par votre organisation utilisera votre aperçu personnalisé.

### Étape 4 : Mettre à jour la règle avec une nouvelle version

Plus tard, si vous souhaitez affiner le XSLT, appelez `update_edoc_custom_attribute` :

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Avec `activate: true`, la nouvelle version est immédiatement activée. La version précédente est conservée dans l'historique. Définissez `activate: false` pour l'enregistrer comme brouillon et l'activer séparément.

### Étape 5 : Revenir à la règle par défaut intégrée

Si vous souhaitez revenir à l'aperçu par défaut, appelez `delete_edoc_custom_attribute` :

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

La règle personnalisée est supprimée et le système revient automatiquement à la feuille de style par défaut partagée. Aucun autre client n'est affecté.

---

## Exemple 2 : Personnaliser les chemins d'extraction pour EDI

Votre organisation reçoit des factures EDI dont la disposition des champs n'est pas standard. Cet exemple montre comment remplacer les chemins d'extraction pour votre organisation.

### Étape 1 : Vérifier les règles actuelles

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Si vous voyez une entrée `EXTRACTION_PATHS` dans `default` mais pas dans `custom`, votre organisation hérite des règles XPath partagées.

### Étape 2 : Créer vos chemins d'extraction personnalisés

Appelez `create_edoc_custom_attribute` avec votre JSON XPath ajusté :

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Étape 3 : Vérifier avec un test à blanc

Appelez `test_electronic_document` avec un exemple de fichier EDI pour confirmer que les chemins d'extraction personnalisés récupèrent les bonnes valeurs :

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

La réponse contient `extracted_fields` et un PNG `preview.image_base64` — examinez les deux pour vérifier l'exactitude avant la mise en production.

---

## Exemple 3 : Exécuter une vérification eDoc complète

Avant de livrer une modification, vérifiez que tous les fixtures eDoc pris en charge réussissent toujours :

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

L'outil exécute chaque fixture XRechnung dans le pipeline et indique le résultat réussite/échec/avertissement pour chacun. Une exécution sans problème confirme que vos personnalisations n'ont pas altéré les autres types de documents.

Pour tester rapidement un seul type :

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Cet outil téléverse jusqu'à 3 fixtures ZUGFeRD, attend le traitement et vérifie de bout en bout la classification, l'extraction et la génération de l'aperçu.
