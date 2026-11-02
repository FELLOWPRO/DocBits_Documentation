# Aperçu de XRechnung

## Introduction

XRechnung est une norme allemande de facturation électronique conçue pour l'administration publique. Elle est basée sur la norme européenne EN 16931 et existe en deux formats techniques : **UBL** (Universal Business Language) et **CII** (Cross Industry Invoice).

DocBits offre un support complet pour XRechnung, permettant l'extraction de données structurées et l'exportation transparente vers les systèmes ERP Infor.

## Versions XRechnung supportées (CII)

DocBits prend en charge les versions XRechnung CII suivantes :

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Flux de données

Le flux de données d'un document XRechnung vers votre système ERP suit ces étapes :

1. **Extraction** : DocBits analyse les données XML en fonction de la version et du format XRechnung (CII ou UBL).
2. **DocBits Field Mapping** : les données extraites sont mappées aux champs standard DocBits.
3. **Alignement avec l’ERP** : les champs DocBits sont mappés aux champs Infor BOD (Business Object Document), généralement en utilisant les champs `SyncSupplierInvoice` BOD.
4. **Export** : Les données cartographiées sont exportées vers le système Infor.

## Standards de mappage

Le mappage est basée sur les normes suivantes :
* **UN/CEFACT CII** : La base de la structure XRechnung CII XML.
* **OAGIS/OASIS** : La norme pour les BOD d’Infor.
* **EN 16931** : La norme européenne pour la facturation électronique.

## Guides par pays

Consultez les guides par pays pour connaître les libellés exacts des formats, la syntaxe, les limites de version et l’état de configuration examiné. [Formats eDocs, versions et guides par pays](../supported-electronic-documents/README.md).
