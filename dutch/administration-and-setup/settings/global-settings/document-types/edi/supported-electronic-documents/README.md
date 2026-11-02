---
description: "Zoek de geconfigureerde eDocs-familie, syntaxis, versie en het profiel op voordat u de documentverwerking test."
---

# eDocs-formaten, versies en landengidsen

Begin met het brondocument en de bijbehorende landengids. Alleen een landnaam identificeert geen bestandsformaat. Een versielabel, XML-syntaxis en een bedrijfsprofiel beschrijven verschillende zaken.

{% hint style="info" %}
De tabellen beschrijven een controle van de ontwikkelcatalogus op 17 oktober 2026 en de bijbehorende verwerkingscode. Ze tonen de beschikbare regels en configuratiecomponenten; ze vormen geen certificering van elk bestand, elke wettelijke vereiste of een productie-uitrol. Uw organisatie kan de standaardinstellingen overschrijven.
{% endhint %}

## Lees de ondersteuningsmatrix op de juiste manier

- Familie: het elektronische documentformaat, zoals XRechnung, Factur-X, KSeF of CFDI.
- Syntaxis: de werkelijke gegevensinhoud, zoals UBL XML, CII XML of een PDF met ingesloten XML. Een PDF-scan, JSON-export of QR-afbeelding is geen gelijkwaardige XML-inhoud.
- Versie: de gedeclareerde publicatie- of schemaversie. Een algemeen familielabel bevestigt niet dat elke versie wordt ondersteund.
- Profiel: een deelverzameling van bedrijfsregels of gegevens, zoals BASIC, EN16931, EXTENDED of selfbilling. Een profiel is geen publicatieversie.
- Regel en componenten: classificatie, Transformation, Preview en Extraction Paths staan los van elkaar. Een geconfigureerd profiel heeft niet noodzakelijk een eigen classificatieregel.
- Validatie en verzending: het weergeven van een bestand of het extraheren van gegevens bevestigt op zichzelf niet alle wettelijke regels, handtekeningen, fiscale goedkeuring of aflevering via een netwerk.

## Landengidsen

Het overzicht verwijst naar 39 landengidsen en één internationale gids. Elke gids vermeldt de exacte formaatlabels en configuratiecomponenten, gevolgd door beschikbare DocBits-schermafbeeldingen, video’s en acceptatiecontroles.

| Land / regio | Families en versieomvang | Catalogusresultaat |
| --- | --- | --- |
| [Oostenrijk](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 en 6.1 hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Denemarken](countries/denmark.md) | OIOUBL 2.1 is de vermelde Deense variant. | Vermeldingen gevonden |
| [Finland](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 en 3.0 hebben afzonderlijke vermeldingen. TEAPPSXML is een andere familie. | Vermeldingen gevonden |
| [Frankrijk](countries/france.md) | Factur-X heeft algemene en versiespecifieke vermeldingen, waaronder 1.0.05, 1.08 en 1.09. VRBL FR CIUS 1.0 staat hier los van. | Vermeldingen gevonden |
| [Duitsland](countries/germany.md) | XRechnung heeft dertien versielabels van 1.0 tot 3.0.2, elk in CII en UBL. ZUGFeRD omvat oudere profielen en 2.5-vermeldingen voor CII en UBL. | Vermeldingen gevonden |
| [Italië](countries/italy.md) | FatturaPA is de geconfigureerde Italiaanse familie. | Vermeldingen gevonden |
| [Nederland](countries/netherlands.md) | SI-UBL 2.0 heeft een eigen vermelding. | Vermeldingen gevonden |
| [Noorwegen](countries/norway.md) | EHF Invoice 3.0 staat vermeld naast EHF Order, Order Response en Despatch Advice. | Vermeldingen gevonden |
| [Polen](countries/poland.md) | KSeF heeft algemene, FA2- en FA3-vermeldingen. | Vermeldingen gevonden |
| [Slovenië](countries/slovenia.md) | e-SLOG 1.6 en 2.0 hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Spanje](countries/spain.md) | Facturae heeft algemene vermeldingen en vermeldingen voor 3.2, 3.2.1 en 3.2.2. | Vermeldingen gevonden |
| [Zweden](countries/sweden.md) | Svefaktura 1.0 is de vermelde Zweedse variant. | Vermeldingen gevonden |
| [Australië](countries/australia.md) | PINT A-NZ heeft regelvermeldingen voor facturen en creditnota’s die met Nieuw-Zeeland worden gedeeld. | Vermeldingen gevonden |
| [Nieuw-Zeeland](countries/new-zealand.md) | PINT A-NZ heeft regelvermeldingen voor facturen en creditnota’s die met Australië worden gedeeld. | Vermeldingen gevonden |
| [India](countries/india.md) | India GST E-Invoice en GST CreditNote hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Indonesië](countries/indonesia.md) | Indonesia E-Faktur is de geconfigureerde familie. | Vermeldingen gevonden |
| [China](countries/china.md) | De catalogus bevat Fapiao, E-Fapiao, General VAT Invoice en Special VAT Invoice. | Vermeldingen gevonden |
| [Japan](countries/japan.md) | JP PINT en JP PINT Self-Billing zijn afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Zuid-Korea](countries/korea.md) | Korea E-Tax Invoice en Korea NTS zijn geconfigureerde families. | Vermeldingen gevonden |
| [Maleisië](countries/malaysia.md) | MyInvois heeft regelvermeldingen voor facturen en creditnota’s. | Vermeldingen gevonden |
| [Filipijnen](countries/philippines.md) | Philippines EIS is de geconfigureerde familie. | Vermeldingen gevonden |
| [Singapore](countries/singapore.md) | InvoiceNow heeft vermeldingen voor facturen en creditnota’s; InvoiceNow SG is een ander geconfigureerd label. | Vermeldingen gevonden |
| [Taiwan](countries/taiwan.md) | Taiwan eGUI is de geconfigureerde familie. | Vermeldingen gevonden |
| [Thailand](countries/thailand.md) | Thailand E-Tax Invoice is de geconfigureerde familie. | Vermeldingen gevonden |
| [Vietnam](countries/vietnam.md) | Vietnam E-Invoice is de geconfigureerde familie. | Vermeldingen gevonden |
| [Argentinië](countries/argentina.md) | Argentina AFIP en Factura Electronica zijn geconfigureerde labels. | Vermeldingen gevonden |
| [Brazilië](countries/brazil.md) | Brazilië heeft NF-e-, NFC-e-, CT-e-, NFS-e- en SPED NFS-e-vermeldingen. NFS-e omvat de versies 1.00 en 2.00 tot 2.04; SPED omvat 1.00.02 en 1.01. | Vermeldingen gevonden |
| [Chili](countries/chile.md) | Chile DTE heeft vermeldingen voor facturen, creditnota’s en verzenddocumenten. | Vermeldingen gevonden |
| [Colombia](countries/colombia.md) | Colombia Factura Electronica en Documento Soporte hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Costa Rica](countries/costa-rica.md) | De oudere documentatie noemt Costa Rica, maar in de onderzochte ontwikkelcatalogus is geen overeenkomende classificatie- of configuratievermelding gevonden. | Niet bevestigd |
| [Ecuador](countries/ecuador.md) | Ecuador SRI heeft algemene vermeldingen en vermeldingen voor 1.0.0, 1.1.0, 2.0.0 en 2.1.0. Withholding (bronbelasting) is een afzonderlijk documenttype. | Vermeldingen gevonden |
| [Mexico](countries/mexico.md) | Mexico CFDI 3.3 en 4.0 hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN en SIFEN 150 zijn geconfigureerde labels. | Vermeldingen gevonden |
| [Peru](countries/peru.md) | Peru CPE heeft algemene vermeldingen en vermeldingen voor UBL 2.0 en UBL 2.1. Factura Electronica is een ander label. | Vermeldingen gevonden |
| [Uruguay](countries/uruguay.md) | Uruguay CFE heeft algemene vermeldingen en vermeldingen voor 24 en 25. E-Factura en E-Nota Credito staan ook vermeld. | Vermeldingen gevonden |
| [Kazachstan](countries/kazakhstan.md) | Kazakhstan ESF is de geconfigureerde familie. | Vermeldingen gevonden |
| [Saoedi-Arabië](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified en Tax Invoice hebben afzonderlijke vermeldingen. | Vermeldingen gevonden |
| [Turkije](countries/turkey.md) | Turkey E-Fatura en E-Arsiv zijn afzonderlijke geconfigureerde families. | Vermeldingen gevonden |
| [Verenigde Arabische Emiraten](countries/united-arab-emirates.md) | UAE VAT Invoice is het geconfigureerde label. | Vermeldingen gevonden |
| [Internationaal](countries/international.md) | Internationale vermeldingen omvatten Peppol BIS 3.0, UBL 2.1, zuivere CII, EDI, INVOIC02, cXML, OCI, BOD en SPS Commerce RSX 7.7.4. | Vermeldingen gevonden |

## Factur-X / ZUGFeRD: verzin geen publicatieversie

Een geharmoniseerde CII Guideline ID kan een familie en profiel identificeren, terwijl meerdere versies dezelfde 1p0-markering gebruiken. Factur-X XMP Version 1.0 is een schemamarkering, geen publicatie zoals 1.08 of 1.09. ZUGFeRD XMP kan zijn versie declareren. Behoud het algemene familieresultaat wanneer gezaghebbende metadata ontbreekt en verifieer het oorspronkelijke bestand bij de afzender.

MINIMUM en BASIC WL kunnen regelgegevens weglaten die verderop in de verwerking nodig zijn. BASIC, EN16931/COMFORT en EXTENDED bieden een verschillende gegevensdekking. Een uitgebreider profiel kan velden bevatten die uw extractietoewijzing niet gebruikt. Controleer vereiste velden met echte voorbeelden.

## Controleer een formaat in uw organisatie

1. Bewaar de oorspronkelijke XML of de PDF met ingesloten XML. Lees de naamruimte, het schema of de aanpassingsidentificatie en de gedeclareerde versie of het profiel.

2. Open Instellingen → Documenttypen → E-Doc voor het betreffende bedrijfsdocument. Zoek het exacte elektronische documentformaat dat in de gids staat.

3. Controleer de daadwerkelijk gebruikte bron, Default of Custom, en de actieve configuratieversie. Bekijk Transformation, Preview en Extraction Paths. Het opslaan van een concept activeert het niet.

4. Test representatieve bronbestanden voor elke syntaxis, versie en elk bedrijfsdocument dat u nodig hebt. Controleer de belangrijkste velden, bedragen, belastingen, de classificatie als factuur of creditnota en de ERP-export.

5. Bevestig het validatiebeleid en het transport afzonderlijk. Behoud aangepaste toewijzingen en controleer goedkeuringen en de exportgeschiedenis voordat u bestaande documenten opnieuw start.

[Acceptatiecontroles](../credit-note-recognized-as-invoice.md)

[DocBits configureren met Claude of Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md): verbinding, prompts, voorbeelden, wijzigingen met versiebeheer, controles en terugdraaien.
