# Als land in veld

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld.</p></figcaption></figure>

Gebruik deze voorwaarde wanneer een extra verwerkingsstap moet afhangen van een landengroep. Het voorbeeld controleert of het land uit een documentveld tot de Europese Unie behoort.

**Locatie:** Standaardworkflow → aanvullende voorwaarden (AND) → Documentveld. Stel de volgende actie afzonderlijk in onder THEN.

## Configuratie — versie 2

| Instelling | Waarde |
| --- | --- |
| Veld | Een bestaand tekstveld met de landnaam |
| Operator | `is` |
| Regio | Europese Unie (EU) |
| Vervolgwaarde | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Praktisch voorbeeld

| Landwaarde in het veld | Verwachte voorwaarde |
| --- | --- |
| `Germany` | Vervuld |
| `United States` | Niet vervuld |

De landnamen in codeopmaak zijn vaste invoerwaarden voor dit voorbeeld.

## Beperkingen en controles

`false` keert de vergelijking niet om. Ook een overeenkomend land geeft met die instelling geen positief voorwaarderesultaat. Kies voor de tegenovergestelde voorwaarde `isnot` met `true`.

Behandel ontbrekende velden en lege landwaarden afzonderlijk; ze kunnen een resultaat voor ontbrekende gegevens geven in plaats van een gewone niet-overeenkomst.

Controle van de broncode van de ontwikkelversie van 22 oktober 2026 toont een conversiefout voor ISO-invoer zoals `DE` en `DEU`. Deze voorbeelden gebruiken daarom volledige landnamen. Controleer de verwerking van ISO-codes afzonderlijk in uw geïnstalleerde versie.

De aangeboden groepen, waaronder EU, Schengen en NAFTA, komen uit de kaartimplementatie. Controleer welke landen uw versie bevat voordat u een groep in een bedrijfsregel gebruikt.
