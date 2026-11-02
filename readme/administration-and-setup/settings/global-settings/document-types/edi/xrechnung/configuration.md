# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Tutoriel sur la facture électronique : traiter XRechnung / ZUGFeRD (Factur-X), valider les données et automatiser les flux de travail
{% endembed %}

## Vue d’ensemble

Dans le panneau d'administration XRechnung, vous rencontrerez les composants clés suivants :

## 1. Transformation

### Objectif

Le processus de transformation est essentiel pour convertir des données brutes, généralement au format XML, dans un format structuré répondant à des exigences spécifiques, comme la génération d'une facture. Dans XRechnung, ceci est principalement réalisé en utilisant XSLT (Extensible Stylesheet Language Transformations). XSLT est un langage conçu pour transformer des documents XML en d'autres types de documents, comme un autre XML, HTML ou du texte brut.

### Fonctionnement

• Modèle XSLT : Le fichier XSLT définit comment les données XML sont traitées et à quoi devrait ressembler la sortie finale. Il applique des règles et des modèles pour extraire, manipuler et générer les données du document XML.

• Éléments et attributs : Le fichier XSLT contient des éléments et des attributs spécifiques qui contrôlent le processus de transformation. Par exemple, \<xsl:value-of> est utilisé pour extraire la valeur d'un nœud spécifique du document XML.

### Fonctions d’administration

• Modifying the XSLT:

• Modifier les modèles existants : un administrateur peut modifier les modèles XSLT existants pour changer la façon dont les données d'entrée XML sont transformées. Par exemple, s'il est nécessaire d'extraire des informations supplémentaires du document XML, un administrateur peut ajouter de nouvelles règles dans le fichier XSLT.

• Créer de nouvelles versions : si des modifications sont nécessaires, un administrateur peut créer une nouvelle version du modèle XSLT. Cela garantit que les versions précédentes restent intactes pour référence historique ou restauration si nécessaire.

### Exemple :

Supposons que le modèle XSLT extrait l’ID de la facture en utilisant :

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Si un nouveau champ, tel qu'un numéro de référence client, doit être extrait, un administrateur peut ajouter :

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Aperçu

### Objectif

La fonction Aperçu permet aux administrateurs de visualiser la sortie générée par la transformation XSLT avant de la finaliser. Cette étape est cruciale pour garantir que les règles de transformation fonctionnent correctement et que le résultat répond aux normes requises.

### Fonctionnement

• Validation en temps réel : la fonction d'aperçu fournit un rendu en temps réel de l'apparence des données transformées lorsqu'elles seront appliquées à un document réel (comme une facture). Cela permet de détecter rapidement les erreurs ou les problèmes de formatage.

• Ajustements : Si l'aperçu présente des écarts ou des erreurs, des ajustements peuvent être effectués directement dans le fichier de transformation (XSLT).

### Fonctions d’administration

• Personnalisation de l'aperçu :

• Modifier les paramètres d'aperçu : un administrateur peut ajuster les parties de la transformation qui sont prévisualisées. Par exemple, ils peuvent se concentrer sur des sections spécifiques du document ou tester de nouvelles règles ajoutées au modèle XSLT.

• Enregistrer et itérer : après avoir effectué les ajustements, l'aperçu peut être actualisé pour voir les modifications. Ce processus itératif permet d'affiner jusqu'à ce que le résultat souhaité soit atteint.

### Exemple :

Si un administrateur remarque que le format de date dans l'aperçu est incorrect (par exemple, affichant YYYY-MM-DD au lieu de DD-MM-YYYY), il peut modifier le XSLT pour formater la date correctement et voir immédiatement le résultat dans l'aperçu.

## 3. Chemins d’extraction

### Objectif

Les chemins d'extraction définissent les chemins spécifiques au sein d'une structure XML ou JSON à partir de laquelle les données doivent être extraites. Ce processus est essentiel pour isoler les informations clés au sein du document qui seront utilisées dans la transformation ou pour d'autres tâches de traitement.

### Fonctionnement

• XPath et JSONPath : les chemins d'extraction utilisent des langages comme XPath (pour XML) ou JSONPath (pour JSON) pour spécifier l'emplacement des données dans le document. Ces chemins sont cruciaux pour indiquer au système exactement où trouver et comment extraire les informations requises.

### Fonctions d’administration

• Définir et modifier des chemins :

• Modifier les chemins existants : un administrateur peut modifier les chemins d'extraction si la structure des données change ou si des données supplémentaires doivent être extraites. Cela peut impliquer de modifier les expressions XPath ou JSONPath.

• Ajouter de nouveaux chemins : pour les nouveaux champs ou points de données, un administrateur peut définir de nouveaux chemins d'extraction. Cela impliquerait de spécifier le chemin correct dans le document XML ou JSON.

### Exemple :

Dans un document facture XML, si le chemin d'accès à l’ID de la facture est défini comme :

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Et un nouveau champ, tel qu'une adresse de livraison, doit être ajouté, un administrateur peut ajouter :

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Règles effectivement utilisées et activation

Les règles propres à l’organisation ont priorité sur celles par défaut pour le format eDoc détecté. Vérifiez la TRANSFORMATION active et vérifiez quel nœud fournit invoice_type dans le XML transformé ; le chemin dépend du format. Save enregistre un brouillon ; utilisez la coche pour l’activer après les tests. Le rendu Preview ne prouve pas le type de document enregistré. Consultez le [guide de diagnostic de la classification](../credit-note-recognized-as-invoice.md) pour les codes 381/261, les scripts suivants et les précautions à prendre avant un retraitement.
