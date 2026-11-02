---
hidden: true
---

# De XSLT-editor gebruiken

Handleiding voor het maken en wijzigen van transformaties met de XSLT-editor, met tips om scripts te testen en te valideren en documentgegevens correct naar het vereiste EDI-formaat om te zetten.

## Transformaties maken, wijzigen, testen en valideren met de XSLT-editor

**De XSLT-editor openen:**

* Open een XSLT-editor naar keuze, zoals Oxygen XML Editor, Altova XMLSpy of een teksteditor met syntaxisaccentuering voor XSLT.

**Transformaties maken of wijzigen:**

* Definieer regels om invoergegevens, zoals XML, naar het gewenste EDI-formaat om te zetten. Gebruik XSLT-sjablonen om elementen en attributen uit de invoer-XML te selecteren en correct op te maken.
* Gebruik XSLT-functies en instructies zoals [xsl:template](xsl:template), [xsl:apply-templates](xsl:apply-templates), [xsl:for-each](xsl:for-each), [xsl:value-of](xsl:value-of) enzovoort om de transformaties uit te voeren.
* Controleer de transformaties zorgvuldig om na te gaan of alle vereiste gegevens correct worden geëxtraheerd en opgemaakt.

**XSLT-scripts testen en valideren:**

* Test uw XSLT-transformaties met voorbeeldgegevens die uiteenlopende scenario's en grensgevallen uit de werkelijke invoer afdekken.
* Voer de XSLT-scripts uit met de voorbeeldgegevens en controleer de uitvoer zorgvuldig. Ga na of de EDI-uitvoer aan de verwachte specificaties voldoet.
* Valideer de scripts tegen de XSLT-specificatie om syntaxisfouten en fouten die onverwacht gedrag veroorzaken te vinden.
* Gebruik zo nodig hulpmiddelen zoals XSLT-debuggers om stapsgewijs te testen en problemen in de transformaties op te sporen.

Door XSLT-scripts zorgvuldig te maken, testen en valideren, kunt u invoergegevens correct naar het vereiste EDI-formaat omzetten. Dit is essentieel voor een geslaagde elektronische gegevensuitwisseling tussen bedrijfssystemen.
