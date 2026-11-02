# Een OCR-fout in een bestelnummer herstellen

Het derde teken van `06O123` is de **letter O**. Levert de extractie `060123` op, gebruik dan een voorwaardelijke voorvoegseltransformatie om dit bekende patroon zonder eigen script te herstellen.

## De voorvoegselcorrectie instellen

1. Open **Instellingen → Documenttypen → tandwiel → Transformatieregels → Transformatieregels beheren**. Een organisatiebeheerder moet de functie voor het gekozen documenttype inschakelen.
2. Maak een regel voor een **kopveld** met **Bestelnummer (`Purchase Order`)** als doel. Lees uit **het veld zelf**.
3. Kies voorwaardelijke uitvoering en selecteer het bestelnummer, **begint met** en `060`.
4. Verwijder de eerste stap voor het weghalen van spaties. Voeg **Affix → Voorvoegsel verwijderen → `060`** toe, gevolgd door **Affix → Voorvoegsel toevoegen → `06O`**. Voer in de tweede stap de hoofdletter O in. De voorwaarde beperkt beide stappen tot het betrokken voorvoegsel; de overige tekens blijven behouden.
5. Controleer het livevoorbeeld, sla de regel op en open hem opnieuw. Test een document, sla het op en laad het opnieuw om het opgeslagen bestelnummer te controleren.

## Het resultaat controleren

| Voorbeeldinvoer | Verwacht resultaat | Reden |
| --- | --- | --- |
| `060123` | `06O123` | Betrokken voorvoegsel |
| `060987` | `06O987` | Andere betrokken waarde; achtervoegsel blijft behouden |
| `06O123` | `06O123` | Al correct; voorwaarde komt niet overeen |
| `160123` | `160123` | Ander voorvoegsel; voorwaarde komt niet overeen |
| `1060123` | `1060123` | `060` midden in de waarde is geen overeenkomend voorvoegsel |

Dit voorbeeld herstelt een bekend extractiepatroon. Het bewijst niet de nauwkeurigheid van OCR, het bestaan van de bestelling of een geslaagde afstemming. Gebruik de regel alleen wanneer de nummerconventie `06O` vereist: ook een geldig `060`-voorvoegsel zou veranderen. Voeg leveranciersvoorwaarden toe als de conventie alleen voor bepaalde leveranciers geldt.

## Waarom twee affixstappen?

De huidige editor vereist een apart bronveld voor positieafhankelijke stappen zoals **Zoeken en vervangen**, ook als **Slechts eenmaal per document uitvoeren** aanstaat. De twee voorvoegselstappen werken op hetzelfde veld. Na de correctie begint de waarde niet meer met `060`, waardoor de voorwaarde verdere wijzigingen bij opnieuw opslaan voorkomt.
