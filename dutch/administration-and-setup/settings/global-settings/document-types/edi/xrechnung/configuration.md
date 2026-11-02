# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-factuur-tutorial: proces XRechnung / ZUGFeRD (Factur-X), gegevens valideren en workflows automatiseren
{% endembed %}

## Overzicht

In het XRechnung administratiepaneel kom je de volgende belangrijke onderdelen tegen:

## 1. Transformatie

### Doel

Het transformatieproces is essentieel voor het omzetten van ruwe gegevens, meestal in XML-formaat, naar een gestructureerd formaat dat aan specifieke eisen voldoet, zoals het genereren van een factuur. In XRechnung wordt dit voornamelijk bereikt met behulp van XSLT (Extensible Stylesheet Language Transformations). XSLT is een taal die is ontworpen voor het transformeren van XML-documenten in andere typen documenten, zoals een andere XML, HTML of platte tekst.

### Hoe het werkt

• XSLT Sjabloon: het XSLT bestand definieert hoe de XML gegevens worden verwerkt en hoe de uiteindelijke uitvoer eruit moet zien. Het past regels en sjablonen toe om de gegevens uit het XML-document te extraheren, manipuleren en uit te voeren.

• Elementen en attributen: het XSLT-bestand bevat specifieke elementen en attributen die het transformatieproces besturen. \<xsl:value-of> wordt bijvoorbeeld gebruikt om de waarde van een specifiek knooppunt uit het XML-document te extraheren.

### Beheermogelijkheden

• Modifying the XSLT:

• Bestaande sjablonen bewerken: een beheerder kan de bestaande XSLT sjablonen wijzigen om te wijzigen hoe de invoer XML gegevens worden getransformeerd. Als er bijvoorbeeld aanvullende informatie uit het XML-document moet worden gehaald, kan een beheerder nieuwe regels toevoegen aan het XSLT-bestand.

• Nieuwe versies maken: als er wijzigingen nodig zijn, kan een beheerder een nieuwe versie van de XSLT-sjabloon maken. Dit zorgt ervoor dat eerdere versies intact blijven voor historische referentie of indien nodig terugdraaien.

### Voorbeeld:

Stel dat de XSLT-sjabloon de factuur-ID extraheert met behulp van:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Als een nieuw veld, zoals een klantreferentienummer, moet worden geëxtraheerd, kan een beheerder het volgende toevoegen:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Voorbeeld

### Doel

Met de Preview-functie kunnen beheerders de uitvoer bekijken die is gegenereerd door de XSLT-transformatie voordat deze wordt voltooid. Deze stap is cruciaal om ervoor te zorgen dat de transformatieregels correct werken en dat de output aan de vereiste normen voldoet.

### Hoe het werkt

• Real-time validatie: de preview-functie biedt een real-time weergave van hoe de getransformeerde gegevens eruit zullen zien wanneer ze worden toegepast op een daadwerkelijk document (zoals een factuur). Dit helpt bij het vroegtijdig onderkennen van fouten of opmaakproblemen.

• Aanpassingen: Als het voorbeeld discrepanties of fouten vertoont, kunnen aanpassingen rechtstreeks in het transformatiebestand (XSLT) worden aangebracht.

### Beheermogelijkheden

• Het voorbeeld aanpassen:

• Voorbeeldinstellingen wijzigen: een beheerder kan aanpassen van welke delen van de transformatie een voorbeeld wordt weergegeven. Ze kunnen zich bijvoorbeeld concentreren op specifieke secties van het document of nieuwe regels testen die zijn toegevoegd aan de XSLT-sjabloon.

• Opslaan en herhalen: na het maken van aanpassingen kan het voorbeeld worden vernieuwd om de wijzigingen te zien. Dit iteratieve proces maakt afstemming mogelijk totdat de gewenste output is bereikt.

### Voorbeeld:

Als een beheerder merkt dat de datumnotatie in het voorbeeld onjuist is (bijvoorbeeld door YYYY-MM-DD weer te geven in plaats van DD-MM-YYYY), kan hij of zij de XSLT aanpassen om de datum correct op te maken en onmiddellijk het resultaat in het voorbeeld te zien.

## 3. Extractiepaden

### Doel

Extractiepaden definiëren de specifieke paden binnen een XML- of JSON-structuur waaruit gegevens moeten worden geëxtraheerd. Dit proces is essentieel voor het isoleren van belangrijke stukjes informatie binnen het document die zullen worden gebruikt bij de transformatie of voor andere verwerkingstaken.

### Hoe het werkt

• XPath en JSONPath: Extractiepaden gebruiken talen zoals XPath (voor XML) of JSONPath (voor JSON) om de locatie van de gegevens in het document op te geven. Deze paden zijn cruciaal om het systeem precies te vertellen waar het de vereiste informatie moet vinden en hoe het eruit moet halen.

### Beheermogelijkheden

• Paden definiëren en wijzigen:

• Bestaande paden wijzigen: een beheerder kan de extractiepaden wijzigen als de gegevensstructuur verandert of als er aanvullende gegevens moeten worden geëxtraheerd. Dit kan gepaard gaan met het wijzigen van de XPath- of JSONPath-expressies.

• Nieuwe paden toevoegen: voor nieuwe velden of gegevenspunten kan een beheerder nieuwe extractiepaden definiëren. Dit houdt in dat u het juiste pad opgeeft in het XML- of JSON-document.

### Voorbeeld:

Als in een XML factuurdocument het pad naar de factuur-ID is gedefinieerd als:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

En er moet een nieuw veld, zoals een verzendadres, worden toegevoegd, een beheerder kan toevoegen:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Effectieve regels en activering

Organisatiespecifieke regels hebben voorrang op de standaardregels voor het gedetecteerde eDoc-formaat. Controleer de actieve TRANSFORMATION en controleer welke node invoice_type levert in de getransformeerde XML; het pad hangt af van het formaat. Save slaat een concept op; gebruik na het testen het vinkje om het te activeren. Een weergegeven Preview bewijst niet wat het opgeslagen documenttype is. Raadpleeg de [handleiding voor het oplossen van classificatieproblemen](../credit-note-recognized-as-invoice.md) voor codes 381/261, latere scripts en voorzorgsmaatregelen bij opnieuw verwerken.
