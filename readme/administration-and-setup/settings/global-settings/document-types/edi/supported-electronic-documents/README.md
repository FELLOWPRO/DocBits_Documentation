---
description: "Identifiez la famille eDocs configurée, sa syntaxe, sa version et son profil avant de tester le traitement des documents."
---

# Formats eDocs, versions et guides par pays

Partez du document source et du guide du pays correspondant. Le nom d’un pays ne suffit pas à identifier un format de fichier. Un libellé de version, une syntaxe XML et un profil métier décrivent des éléments différents.

{% hint style="info" %}
Les tableaux consignent une vérification du catalogue de développement effectuée le 17 octobre 2026 et du code de traitement correspondant. Ils décrivent les règles et composants de configuration disponibles, sans certifier chaque fichier, exigence légale ou déploiement en production. Votre organisation peut remplacer les valeurs par défaut.
{% endhint %}

## Bien lire la matrice de prise en charge

- Famille : le format de document électronique, par exemple XRechnung, Factur-X, KSeF ou CFDI.
- Syntaxe : le contenu réel, par exemple du XML UBL, du XML CII ou un PDF avec XML intégré. Un PDF numérisé, un export JSON ou une image QR ne constitue pas un contenu XML équivalent.
- Version : la publication ou la version de schéma déclarée. Un libellé générique de famille ne démontre pas la prise en charge de toutes les versions.
- Profil : un sous-ensemble métier ou de données, par exemple BASIC, EN16931, EXTENDED ou l’autofacturation. Un profil n’est pas une version de publication.
- Règle et composants : la classification, Transformation, Preview et Extraction Paths sont distincts. Un profil configuré ne possède pas nécessairement sa propre règle de classification.
- Validation et transmission : le rendu ou l’extraction d’un fichier ne vérifie pas, à lui seul, toutes les règles légales, les signatures, la validation fiscale ou la transmission réseau.

## Guides par pays

| Pays / région | Familles et périmètre des versions | Résultat du catalogue |
| --- | --- | --- |
| [Autriche](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 et 6.1 possèdent des entrées distinctes. | Entrées trouvées |
| [Danemark](countries/denmark.md) | OIOUBL 2.1 est l’entrée danoise nommée. | Entrées trouvées |
| [Finlande](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 et 3.0 possèdent des entrées distinctes. TEAPPSXML est une autre famille. | Entrées trouvées |
| [France](countries/france.md) | Factur-X possède des entrées génériques et propres à certaines publications, notamment 1.0.05, 1.08 et 1.09. VRBL FR CIUS 1.0 est distinct. | Entrées trouvées |
| [Allemagne](countries/germany.md) | XRechnung possède treize libellés de version de 1.0 à 3.0.2, chacun en CII et en UBL. ZUGFeRD comprend des profils historiques et des entrées 2.5 CII et UBL. | Entrées trouvées |
| [Italie](countries/italy.md) | FatturaPA est la famille italienne configurée. | Entrées trouvées |
| [Pays-Bas](countries/netherlands.md) | SI-UBL 2.0 possède une entrée dédiée. | Entrées trouvées |
| [Norvège](countries/norway.md) | EHF Invoice 3.0 figure aux côtés d’EHF Order, Order Response et Despatch Advice. | Entrées trouvées |
| [Pologne](countries/poland.md) | KSeF possède des entrées génériques, FA2 et FA3. | Entrées trouvées |
| [Slovénie](countries/slovenia.md) | e-SLOG 1.6 et 2.0 possèdent des entrées distinctes. | Entrées trouvées |
| [Espagne](countries/spain.md) | Facturae possède des entrées génériques, 3.2, 3.2.1 et 3.2.2. | Entrées trouvées |
| [Suède](countries/sweden.md) | Svefaktura 1.0 est l’entrée suédoise nommée. | Entrées trouvées |
| [Australie](countries/australia.md) | PINT A-NZ possède des entrées de règles de facture et d’avoir partagées avec la Nouvelle-Zélande. | Entrées trouvées |
| [Nouvelle-Zélande](countries/new-zealand.md) | PINT A-NZ possède des entrées de règles de facture et d’avoir partagées avec l’Australie. | Entrées trouvées |
| [Inde](countries/india.md) | India GST E-Invoice et GST CreditNote possèdent des entrées distinctes. | Entrées trouvées |
| [Indonésie](countries/indonesia.md) | Indonesia E-Faktur est la famille configurée. | Entrées trouvées |
| [Chine](countries/china.md) | Le catalogue comprend Fapiao, E-Fapiao, General VAT Invoice et Special VAT Invoice. | Entrées trouvées |
| [Japon](countries/japan.md) | JP PINT et JP PINT Self-Billing possèdent des entrées distinctes. | Entrées trouvées |
| [Corée du Sud](countries/korea.md) | Korea E-Tax Invoice et Korea NTS sont des familles configurées. | Entrées trouvées |
| [Malaisie](countries/malaysia.md) | MyInvois possède des entrées de règles de facture et d’avoir. | Entrées trouvées |
| [Philippines](countries/philippines.md) | Philippines EIS est la famille configurée. | Entrées trouvées |
| [Singapour](countries/singapore.md) | InvoiceNow possède des entrées de facture et d’avoir ; InvoiceNow SG est un autre libellé configuré. | Entrées trouvées |
| [Taïwan](countries/taiwan.md) | Taiwan eGUI est la famille configurée. | Entrées trouvées |
| [Thaïlande](countries/thailand.md) | Thailand E-Tax Invoice est la famille configurée. | Entrées trouvées |
| [Viêt Nam](countries/vietnam.md) | Vietnam E-Invoice est la famille configurée. | Entrées trouvées |
| [Argentine](countries/argentina.md) | Argentina AFIP et Factura Electronica sont des libellés configurés. | Entrées trouvées |
| [Brésil](countries/brazil.md) | Le Brésil possède des entrées NF-e, NFC-e, CT-e, NFS-e et SPED NFS-e. NFS-e comprend les versions 1.00 et 2.00 à 2.04 ; SPED comprend 1.00.02 et 1.01. | Entrées trouvées |
| [Chili](countries/chile.md) | Chile DTE possède des entrées de facture, d’avoir et de guide d’expédition. | Entrées trouvées |
| [Colombie](countries/colombia.md) | Colombia Factura Electronica et Documento Soporte possèdent des entrées distinctes. | Entrées trouvées |
| [Costa Rica](countries/costa-rica.md) | L’ancienne documentation mentionne le Costa Rica, mais aucune entrée de classification ou de configuration correspondante n’a été trouvée dans le catalogue de développement examiné. | Non confirmé |
| [Équateur](countries/ecuador.md) | Ecuador SRI possède des entrées génériques, 1.0.0, 1.1.0, 2.0.0 et 2.1.0. La retenue à la source est un type de document distinct. | Entrées trouvées |
| [Mexique](countries/mexico.md) | Mexico CFDI 3.3 et 4.0 possèdent des entrées distinctes. | Entrées trouvées |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN et SIFEN 150 sont des libellés configurés. | Entrées trouvées |
| [Pérou](countries/peru.md) | Peru CPE possède des entrées génériques, UBL 2.0 et UBL 2.1. Factura Electronica est un autre libellé. | Entrées trouvées |
| [Uruguay](countries/uruguay.md) | Uruguay CFE possède des entrées génériques, 24 et 25. E-Factura et E-Nota Credito figurent également dans la liste. | Entrées trouvées |
| [Kazakhstan](countries/kazakhstan.md) | Kazakhstan ESF est la famille configurée. | Entrées trouvées |
| [Arabie saoudite](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified et Tax Invoice possèdent des entrées distinctes. | Entrées trouvées |
| [Turquie](countries/turkey.md) | Turkey E-Fatura et E-Arsiv sont des familles configurées distinctes. | Entrées trouvées |
| [Émirats arabes unis](countries/united-arab-emirates.md) | UAE VAT Invoice est le libellé configuré. | Entrées trouvées |
| [International](countries/international.md) | Les entrées internationales comprennent Peppol BIS 3.0, UBL 2.1, CII pur, EDI, INVOIC02, cXML, OCI, BOD et SPS Commerce RSX 7.7.4. | Entrées trouvées |

## Factur-X / ZUGFeRD : ne pas inventer de version de publication

Un Guideline ID CII harmonisé peut identifier une famille et un profil tout en partageant le même marqueur 1p0 entre plusieurs versions. Factur-X XMP Version 1.0 est un marqueur de schéma, et non une publication telle que 1.08 ou 1.09. Les métadonnées XMP de ZUGFeRD peuvent déclarer sa version. En l’absence de métadonnées faisant autorité, conservez le résultat de famille générique et confirmez le fichier d’origine avec l’émetteur.

MINIMUM et BASIC WL peuvent omettre des informations de lignes nécessaires aux traitements suivants. BASIC, EN16931/COMFORT et EXTENDED offrent des couvertures de données différentes. Un profil plus complet peut contenir des champs que votre correspondance d’extraction n’utilise pas. Vérifiez les champs requis à l’aide d’exemples réels.

## Vérifier un format dans votre organisation

1. Conservez le XML d’origine ou le PDF avec son XML intégré. Relevez l’espace de noms, le schéma ou l’identifiant de personnalisation, ainsi que la version et le profil déclarés.

2. Ouvrez Paramètres → Types de documents → E-Doc pour le document métier concerné. Recherchez le format exact de document électronique indiqué dans le guide.

3. Vérifiez la source Default ou Custom effectivement utilisée et sa version de configuration active. Examinez Transformation, Preview et Extraction Paths. Enregistrer un brouillon ne l’active pas.

4. Testez des fichiers source représentatifs pour chaque syntaxe, version et document métier dont vous avez besoin. Vérifiez les champs clés, les montants, les taxes, la classification facture/avoir et l’export ERP.

5. Confirmez séparément la politique de validation et le transport. Préservez les correspondances personnalisées et vérifiez les approbations ainsi que l’historique des exports avant de relancer des documents existants.

[Vérifications d’acceptation](../credit-note-recognized-as-invoice.md)

[Configurer DocBits avec Claude ou Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md) : connexion, prompts, aperçus, modifications versionnées, contrôles et retour arrière.
