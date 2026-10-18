---
description: "Uruguay CFE heeft algemene vermeldingen en vermeldingen voor 24 en 25. E-Factura en E-Nota Credito staan ook vermeld."
---

# Uruguay

Gebruik deze gids om de geconfigureerde familie en de versieomvang vast te stellen voordat u een bronbestand test.

[Alle landen en ondersteuningsomvang](../README.md)

## Varianten en versiebeperkingen

Uruguay CFE heeft algemene vermeldingen en vermeldingen voor 24 en 25. E-Factura en E-Nota Credito staan ook vermeld.

**Syntaxis:** XML

Creditnotavermeldingen hebben in de onderzochte status geen eigen extractiebundels. Bevestig de CFE-versie en de daadwerkelijk gebruikte toewijzing voor facturen of creditnota’s.

De tabellen beschrijven een controle van de ontwikkelcatalogus op 17 oktober 2026 en de bijbehorende verwerkingscode. Ze tonen de beschikbare regels en configuratiecomponenten; ze vormen geen certificering van elk bestand, elke wettelijke vereiste of een productie-uitrol. Uw organisatie kan de standaardinstellingen overschrijven.

## Onderzochte regels en componenten

| Exact formaatlabel | Documentsleutel van de regel | Beschikbare componenten |
| --- | --- | --- |
| `URUGUAY E-FACTURA` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY E-NOTA CREDITO` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY CFE` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 24` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 25` | `INVOICE` | C / T / P / E |
| `URUGUAY E-FACTURA` | `INVOICE` | C / T / P / E |

C = classificatie, T = Transformation, P = Preview, E = Extraction Paths. De documentsleutel is de opzoeksleutel voor regels en configuratie; deze garandeert niet de uiteindelijk opgeslagen invoice_type. Een transformatie kan een creditnota classificeren via een INVOICE-toewijzing.

Een streepje betekent dat de statuscontrole geen eigen component voor deze exacte combinatie van formaat en documentsleutel heeft gemeld. Dit sluit een gedeelde of terugvaltoewijzing niet uit. Controleer de daadwerkelijk gebruikte resolver en een representatief bestand voordat u op die route vertrouwt.

## Zoek de toewijzing in DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-uruguay-nl.png" alt="Uruguay: URUGUAY CFE 25"><figcaption><p>Werkelijke ontwikkelinterface: het representatieve formaat en de beschikbare configuratiecomponenten. Andere versies staan in de matrix.</p></figcaption></figure>

## Uitlegvideo per land

Gesproken uitleg en WebVTT-ondertitels in de gekozen taal leggen formaatselectie, configuratie en acceptatiecontroles uit.

Deze rondleiding zonder wijzigingen toont de bestaande DocBits-configuratie voor het land. Controleer de gebruikte bron en actieve versie en test representatieve facturen, creditnota’s en exports in uw eigen organisatie.

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-nl-v2.mp4" %}
Uruguay — Uitlegvideo per land
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-nl-v2.vtt" %}
WebVTT
{% endfile %}

## Acceptatiecontroles

Een componentcontrole bevestigt dat er configuratie aanwezig is. Het is geen test van de volledige verwerking voor elke versie. Test de exacte gegevensinhoud en de factuur- of creditnotaroute die uw integratie nodig heeft.

## Controleer een formaat in uw organisatie

1. Bewaar de oorspronkelijke XML of de PDF met ingesloten XML. Lees de naamruimte, het schema of de aanpassingsidentificatie en de gedeclareerde versie of het profiel.

2. Open Instellingen → Documenttypen → E-Doc voor het betreffende bedrijfsdocument. Zoek het exacte elektronische documentformaat dat in de gids staat.

3. Controleer de daadwerkelijk gebruikte bron, Default of Custom, en de actieve configuratieversie. Bekijk Transformation, Preview en Extraction Paths. Het opslaan van een concept activeert het niet.

4. Test representatieve bronbestanden voor elke syntaxis, versie en elk bedrijfsdocument dat u nodig hebt. Controleer de belangrijkste velden, bedragen, belastingen, de classificatie als factuur of creditnota en de ERP-export.

5. Bevestig het validatiebeleid en het transport afzonderlijk. Behoud aangepaste toewijzingen en controleer goedkeuringen en de exportgeschiedenis voordat u bestaande documenten opnieuw start.

## Gerelateerde formaatreferentie

- [🇺🇾 URUGUAY CFE](../uruguay-cfe.md)
- [🇺🇾 URUGUAY CFE 24](../uruguay-cfe-24.md)
- [🇺🇾 URUGUAY CFE 25](../uruguay-cfe-25.md)
- [🇺🇾 URUGUAY E-FACTURA](../uruguay-e-factura.md)
- [🇺🇾 URUGUAY E-NOTA CREDITO](../uruguay-e-nota-credito.md)
