# Currently Supported E-Invoice Standards

Partez du document source et du guide du pays correspondant. Le nom d’un pays ne suffit pas à identifier un format de fichier. Un libellé de version, une syntaxe XML et un profil métier décrivent des éléments différents.

Consultez les guides par pays pour connaître les libellés exacts des formats, la syntaxe, les limites de version et l’état de configuration examiné. [Formats eDocs, versions et guides par pays](../supported-electronic-documents/README.md).

Les tableaux consignent une vérification du catalogue de développement effectuée le 17 octobre 2026 et du code de traitement correspondant. Ils décrivent les règles et composants de configuration disponibles, sans certifier chaque fichier, exigence légale ou déploiement en production. Votre organisation peut remplacer les valeurs par défaut.

| Pays / région | Familles et périmètre des versions | Résultat du catalogue |
| --- | --- | --- |
| [Autriche](../supported-electronic-documents/countries/austria.md) | ebInterface 4.3, 5.0, 6.0 et 6.1 possèdent des entrées distinctes. | Entrées trouvées |
| [Danemark](../supported-electronic-documents/countries/denmark.md) | OIOUBL 2.1 est l’entrée danoise nommée. | Entrées trouvées |
| [Finlande](../supported-electronic-documents/countries/finland.md) | Finvoice 1.3, 2.0, 2.01 et 3.0 possèdent des entrées distinctes. TEAPPSXML est une autre famille. | Entrées trouvées |
| [France](../supported-electronic-documents/countries/france.md) | Factur-X possède des entrées génériques et propres à certaines publications, notamment 1.0.05, 1.08 et 1.09. VRBL FR CIUS 1.0 est distinct. | Entrées trouvées |
| [Allemagne](../supported-electronic-documents/countries/germany.md) | XRechnung possède treize libellés de version de 1.0 à 3.0.2, chacun en CII et en UBL. ZUGFeRD comprend des profils historiques et des entrées 2.5 CII et UBL. | Entrées trouvées |
| [Italie](../supported-electronic-documents/countries/italy.md) | FatturaPA est la famille italienne configurée. | Entrées trouvées |
| [Pays-Bas](../supported-electronic-documents/countries/netherlands.md) | SI-UBL 2.0 possède une entrée dédiée. | Entrées trouvées |
| [Norvège](../supported-electronic-documents/countries/norway.md) | EHF Invoice 3.0 figure aux côtés d’EHF Order, Order Response et Despatch Advice. | Entrées trouvées |
| [Pologne](../supported-electronic-documents/countries/poland.md) | KSeF possède des entrées génériques, FA2 et FA3. | Entrées trouvées |
| [Slovénie](../supported-electronic-documents/countries/slovenia.md) | e-SLOG 1.6 et 2.0 possèdent des entrées distinctes. | Entrées trouvées |
| [Espagne](../supported-electronic-documents/countries/spain.md) | Facturae possède des entrées génériques, 3.2, 3.2.1 et 3.2.2. | Entrées trouvées |
| [Suède](../supported-electronic-documents/countries/sweden.md) | Svefaktura 1.0 est l’entrée suédoise nommée. | Entrées trouvées |
| [Australie](../supported-electronic-documents/countries/australia.md) | PINT A-NZ possède des entrées de règles de facture et d’avoir partagées avec la Nouvelle-Zélande. | Entrées trouvées |
| [Nouvelle-Zélande](../supported-electronic-documents/countries/new-zealand.md) | PINT A-NZ possède des entrées de règles de facture et d’avoir partagées avec l’Australie. | Entrées trouvées |
| [Inde](../supported-electronic-documents/countries/india.md) | India GST E-Invoice et GST CreditNote possèdent des entrées distinctes. | Entrées trouvées |
| [Indonésie](../supported-electronic-documents/countries/indonesia.md) | Indonesia E-Faktur est la famille configurée. | Entrées trouvées |
| [Chine](../supported-electronic-documents/countries/china.md) | Le catalogue comprend Fapiao, E-Fapiao, General VAT Invoice et Special VAT Invoice. | Entrées trouvées |
| [Japon](../supported-electronic-documents/countries/japan.md) | JP PINT et JP PINT Self-Billing possèdent des entrées distinctes. | Entrées trouvées |
| [Corée du Sud](../supported-electronic-documents/countries/korea.md) | Korea E-Tax Invoice et Korea NTS sont des familles configurées. | Entrées trouvées |
| [Malaisie](../supported-electronic-documents/countries/malaysia.md) | MyInvois possède des entrées de règles de facture et d’avoir. | Entrées trouvées |
| [Philippines](../supported-electronic-documents/countries/philippines.md) | Philippines EIS est la famille configurée. | Entrées trouvées |
| [Singapour](../supported-electronic-documents/countries/singapore.md) | InvoiceNow possède des entrées de facture et d’avoir ; InvoiceNow SG est un autre libellé configuré. | Entrées trouvées |
| [Taïwan](../supported-electronic-documents/countries/taiwan.md) | Taiwan eGUI est la famille configurée. | Entrées trouvées |
| [Thaïlande](../supported-electronic-documents/countries/thailand.md) | Thailand E-Tax Invoice est la famille configurée. | Entrées trouvées |
| [Viêt Nam](../supported-electronic-documents/countries/vietnam.md) | Vietnam E-Invoice est la famille configurée. | Entrées trouvées |
| [Argentine](../supported-electronic-documents/countries/argentina.md) | Argentina AFIP et Factura Electronica sont des libellés configurés. | Entrées trouvées |
| [Brésil](../supported-electronic-documents/countries/brazil.md) | Le Brésil possède des entrées NF-e, NFC-e, CT-e, NFS-e et SPED NFS-e. NFS-e comprend les versions 1.00 et 2.00 à 2.04 ; SPED comprend 1.00.02 et 1.01. | Entrées trouvées |
| [Chili](../supported-electronic-documents/countries/chile.md) | Chile DTE possède des entrées de facture, d’avoir et de guide d’expédition. | Entrées trouvées |
| [Colombie](../supported-electronic-documents/countries/colombia.md) | Colombia Factura Electronica et Documento Soporte possèdent des entrées distinctes. | Entrées trouvées |
| [Costa Rica](../supported-electronic-documents/countries/costa-rica.md) | L’ancienne documentation mentionne le Costa Rica, mais aucune entrée de classification ou de configuration correspondante n’a été trouvée dans le catalogue de développement examiné. | Non confirmé |
| [Équateur](../supported-electronic-documents/countries/ecuador.md) | Ecuador SRI possède des entrées génériques, 1.0.0, 1.1.0, 2.0.0 et 2.1.0. La retenue à la source est un type de document distinct. | Entrées trouvées |
| [Mexique](../supported-electronic-documents/countries/mexico.md) | Mexico CFDI 3.3 et 4.0 possèdent des entrées distinctes. | Entrées trouvées |
| [Paraguay](../supported-electronic-documents/countries/paraguay.md) | Paraguay DTE, SIFEN et SIFEN 150 sont des libellés configurés. | Entrées trouvées |
| [Pérou](../supported-electronic-documents/countries/peru.md) | Peru CPE possède des entrées génériques, UBL 2.0 et UBL 2.1. Factura Electronica est un autre libellé. | Entrées trouvées |
| [Uruguay](../supported-electronic-documents/countries/uruguay.md) | Uruguay CFE possède des entrées génériques, 24 et 25. E-Factura et E-Nota Credito figurent également dans la liste. | Entrées trouvées |
| [Kazakhstan](../supported-electronic-documents/countries/kazakhstan.md) | Kazakhstan ESF est la famille configurée. | Entrées trouvées |
| [Arabie saoudite](../supported-electronic-documents/countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified et Tax Invoice possèdent des entrées distinctes. | Entrées trouvées |
| [Turquie](../supported-electronic-documents/countries/turkey.md) | Turkey E-Fatura et E-Arsiv sont des familles configurées distinctes. | Entrées trouvées |
| [Émirats arabes unis](../supported-electronic-documents/countries/united-arab-emirates.md) | UAE VAT Invoice est le libellé configuré. | Entrées trouvées |
| [International](../supported-electronic-documents/countries/international.md) | Les entrées internationales comprennent Peppol BIS 3.0, UBL 2.1, CII pur, EDI, INVOIC02, cXML, OCI, BOD et SPS Commerce RSX 7.7.4. | Entrées trouvées |
