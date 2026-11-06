# Rapport Pagina

De pagina **Rapport** geeft een overzicht van de documentstroom in DocBits gedurende een bepaalde periode: hoeveel documenten er binnenkwamen, hoe lang de verwerking duurde, welke velden handmatig zijn gecorrigeerd en waar de documenten uiteindelijk terechtkwamen. De pagina is bedoeld voor beheerders en teamleiders die het intake- en validatiewerk als geheel willen bekijken, niet een afzonderlijk document.

{% embed url="https://www.youtube.com/watch?v=ar9jXYJo_AM" %}

## De pagina Rapport inschakelen

De pagina wordt met een moduleschakelaar beheerd. Schakel deze eenmalig in voor de organisatie:

1. Ga naar **Instellingen → Module** en open de groep **Documentintegratie**.
2. Schakel op de kaart **Documenttype** de optie **Rapport weergeven** in.
3. Het item **Rapport** verschijnt vervolgens in de zijbalk voor de gebruikers van de organisatie.

<figure><img src="../.gitbook/assets/report-show-report-setting-nl.png" alt="De schakelaar Rapport weergeven."><figcaption><p>De schakelaar <strong>Rapport weergeven</strong>.</p></figcaption></figure>

## De pagina Rapport openen

Selecteer het grafiekpictogram in de zijbalk. De pagina wordt geopend met het tijdfilter, de kerncijfers van de periode en de veldstatistieken.

<figure><img src="../.gitbook/assets/report-sidebar-icon-nl.png" alt="De DocBits-zijbalk met het gemarkeerde grafiekpictogram en de tooltip Rapport."><figcaption><p>Het item <strong>Rapport</strong> in de zijbalk.</p></figcaption></figure>

## Het tijdsbestek kiezen

Met het filter **Tijdseenheid** bovenaan de pagina bepaalt u de periode voor alle cijfers en onderdelen eronder. U kunt kiezen uit **Laatste 7 dagen**, **Laatste 30 dagen** en **Selecteer tijdsbereik**. Met de laatste optie opent u een kalender waarin u een begin- en einddatum kiest.

<figure><img src="../.gitbook/assets/dbdc-19-report-time-options-native-20261103-nl.png" alt="Opties voor Tijdseenheid: Laatste 7 dagen, Laatste 30 dagen en Selecteer tijdsbereik. De applicatieheader en de navigatie vallen buiten de afbeelding."><figcaption><p>Opties voor <strong>Tijdseenheid</strong>: <strong>Laatste 7 dagen</strong>, <strong>Laatste 30 dagen</strong> en <strong>Selecteer tijdsbereik</strong>. De applicatieheader en de navigatie vallen buiten de afbeelding.</p></figcaption></figure>

## De cijfers naast het filter

<figure><img src="../.gitbook/assets/report-time-unit-filter-nl.png" alt="De bovenste rij van de pagina Rapport met het filter Tijdseenheid, de kaart Nieuwe documenten, de kaart Gemiddelde systeemtijd en de downloadknop."><figcaption><p><strong>Tijdseenheid</strong>, <strong>Nieuwe documenten</strong>, <strong>Gemiddelde systeemtijd</strong> en de downloadknop.</p></figcaption></figure>

- **Nieuwe documenten** geeft aan hoeveel documenten er in de geselecteerde periode zijn geïmporteerd.
- **Gemiddelde systeemtijd** geeft aan hoeveel tijd in seconden DocBits in die periode gemiddeld nodig had om een document te verwerken.
- Met de downloadknop rechts in de rij exporteert u het rapport voor de geselecteerde periode als Excel-bestand (XLSX).

## Gewijzigde velden

De grafiek **Gewijzigde velden** telt hoe vaak elk veld in de geselecteerde periode handmatig is gecorrigeerd. Wanneer er gegevens beschikbaar zijn, krijgt elk veld een eigen balk, zodat u direct ziet welke velden uw team het vaakst bewerkt. Het vraagteken naast de kop legt uit wat de grafiek telt.

<figure><img src="../.gitbook/assets/report-changed-fields-nl.png" alt="De kaart Gewijzigde velden met de melding Er zijn geen gegevensitems gevonden in het betreffende tijdsbestek. Er zijn geen balken zichtbaar; rechtsboven staat het grafiekmenu."><figcaption><p>De kaart <strong>Gewijzigde velden</strong> zonder gegevens voor het geselecteerde tijdsbestek.</p></figcaption></figure>

De kaart is leeg omdat er voor het geselecteerde tijdsbestek geen gegevens over handmatig gewijzigde velden beschikbaar zijn; daarom ziet u de melding **Er zijn geen gegevensitems gevonden in het betreffende tijdsbestek.** en geen balken.

Gebruik het menu rechtsboven in de grafiek om het diagram zelf te downloaden als **SVG**, **PNG** of **CSV**.

## Aanvullende rapportonderdelen

Onder de grafiek staan vier kaarten. Deze zijn standaard samengevouwen. Selecteer een kop om de bijbehorende tabel te openen en selecteer de kop opnieuw om deze te sluiten.

1. **Totaal aantal documenten per type** geeft elk documenttype weer met de kolommen **Type** en **Graaf**. Bij een type met subdocumenttypen staat een **+** waarmee u het aantal kunt uitsplitsen.
2. **Dagelijks gemiddelde per doctype** toont dezelfde lijst als een dagelijks gemiddelde per documenttype.
3. **Statusstatistiek** splitst de documenten uit op verwerkingsstatus, met de kolommen **Type**, **Status** en **Graaf**.
4. **Exportstatistieken** geeft eerst de organisaties van uw account weer. Vouw een organisatie uit om te zien welke exportformaten zijn gebruikt, met de kolommen **Gebruikers**, **Type** en **Geëxporteerd**.

<figure><img src="../.gitbook/assets/report-total-documents-per-type-nl.png" alt="De uitgevouwen kaart Totaal aantal documenten per type met de kolommen Type en Graaf."><figcaption><p><strong>Totaal aantal documenten per type</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-daily-average-per-doctype-nl.png" alt="De uitgevouwen kaart Dagelijks gemiddelde per doctype met de kolommen Type en Graaf."><figcaption><p><strong>Dagelijks gemiddelde per doctype</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-status-statistic-nl.png" alt="De uitgevouwen kaart Statusstatistiek met de kolommen Type, Status en Graaf."><figcaption><p><strong>Statusstatistiek</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/dbdc-19-report-export-stats-native-20261103-nl.png" alt="Exportstatistieken met een uitgevouwen gedeelte voor een bestaande organisatie. Organisatienamen en rijwaarden zijn gemaskeerd; de afbeelding toont bestaande statistieken."><figcaption><p><strong>Exportstatistieken</strong> met een uitgevouwen gedeelte voor een bestaande organisatie. Organisatienamen en rijwaarden zijn gemaskeerd; de afbeelding toont bestaande statistieken.</p></figcaption></figure>
