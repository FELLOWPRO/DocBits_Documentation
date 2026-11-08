# Hoe de documentatiezoekopdracht werkt

De Settings Assistant zoekt naar relevante informatie in de openbare pagina's op [docs.docbits.com](https://docs.docbits.com). Resultaten kunnen een paginatitel, een korte passage en een link naar de bronpagina bevatten. Open de link wanneer u de volledige instructies of een schermafbeelding nodig hebt.

## De juiste pagina vinden

De zoekopdracht combineert woordmatching met matching op betekenis. Dat helpt wanneer uw vraag andere woorden gebruikt dan een paginatitel. De assistent kan ook de instellingenpagina die u bekijkt gebruiken om het antwoord relevanter te maken.

Is zoeken op betekenis tijdelijk niet beschikbaar, dan kan de documentatiezoekopdracht nog steeds woordmatching gebruiken. Een specifieke vraag met de naam van de instelling is de beste manier om het opnieuw te proberen.

## Talen

De documentatiezoekopdracht gebruikt momenteel de indexen van de **Engelse** en **Duitse** helpagina's. Gebruikt uw DocBits-interface een andere taal, dan valt de assistent terug op Engelse documentatieresultaten. De gelinkte pagina toont haar eigen taal; controleer die taal voordat u stappen volgt of schermafbeeldingen vergelijkt.

## Wanneer wijzigingen doorzoekbaar worden

De zoekindex wordt vernieuwd wanneer wijzigingen in de Engelse of Duitse documentatie uit de documentatierepository worden gepubliceerd. Een regelmatige afstemming verwijdert bovendien links naar pagina's die niet meer in de documentatienavigatie staan. Het kan even duren voordat een nieuw gepubliceerde pagina in de assistent verschijnt.

### Technisch overzicht voor beheerders

Gepubliceerde helpagina's worden in secties opgesplitst en opgeslagen in een eigen **OpenSearch documentation index** per ondersteunde taal. Deze index staat los van de indexen die voor de geüploade documenten van een organisatie worden gebruikt. Verandert een pagina, dan kunnen ongewijzigde secties worden overgeslagen en worden gewijzigde secties opnieuw geïndexeerd. Verwijderde pagina's worden uit de documentatie-index verwijderd.

Voor een vraag combineert de dienst treffers op trefwoorden met vectorsimilariteit en ordent vervolgens de meest relevante passages. Is de embeddingdienst niet beschikbaar, dan blijft zoeken op trefwoorden beschikbaar. De Settings Assistant ontvangt bronlinks en korte passages uit deze documentatiezoekopdracht; hij leest daarvoor niet de documentindex van een organisatie.

Kunt u geen pagina vinden, zoek dan rechtstreeks op [docs.docbits.com](https://docs.docbits.com), probeer een preciezere vraag of neem contact op met DocBits-support.

{% hint style="info" %}
Deze zoekopdracht omvat de DocBits-helpagina's. De functie [Fulltext Search](../document-processing/module/fulltext-search.md) doorzoekt de documenten van uw organisatie en heeft eigen instellingen.
{% endhint %}

Terug naar [de Settings Assistant gebruiken](README.md).
