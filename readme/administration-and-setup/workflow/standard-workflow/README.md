# Standaardworkflow

<figure><img src="../../../../.gitbook/assets/docbits_standard_workflow_diagram_2.svg" alt="DocBits Standaardworkflow Diagram 2"><figcaption></figcaption></figure>

#### Overzicht van de workflowcomponenten:

* **AP Invoice Email**: Het proces begint waarschijnlijk met een factuur die per e-mail wordt ontvangen.
* **DocBits**: Deze tool wordt mogelijk gebruikt voor de initiële documentbeheertaken, zoals het vastleggen en digitaliseren van facturen.
* **Finance Review**: Facturen ondergaan een financiële beoordeling waarbij beslissingen worden genomen over de geldigheid en juistheid ervan.

#### Stappen in de workflow:

1. **Initiële beoordeling**:
   * Facturen worden ontvangen en in eerste instantie verwerkt met DocBits.
   * Ze worden vervolgens beoordeeld door het financiële team om ervoor te zorgen dat ze uit de workflow worden verwijderd als ze compleet zijn, of doorgestuurd voor verdere verwerking.
2. **PO- versus niet-PO-facturen**:
   * De workflow maakt onderscheid tussen PO-gerelateerde en niet-PO-facturen.
   * Niet-PO-facturen worden doorgestuurd voor verdere goedkeuring of afwijzing op basis van vooraf gedefinieerde criteria zoals leverancier-ID, hoeveelheid, eenheidsprijs en artikelnummer.
3. **Overeenkomsten en afwijkingen**:
   * Facturen worden vergeleken met goederenontvangsten om ervoor te zorgen dat de gegevens overeenkomen (zoals leverancier-ID en hoeveelheid).
   * Als er afwijkingen optreden, wordt de factuur onderworpen aan een nadere beoordeling en mogelijk afgewezen.
4. **Beoordeling door financiën en inkoper**:
   * Voor PO-gerelateerde facturen wordt een gedetailleerd matchingproces uitgevoerd waarbij een inkoper de beoordeling uitvoert.
   * Aanpassingen aan inkooporders of goederenontvangsten kunnen nodig zijn.
5. **Eindbeslissingen**:
   * Facturen die alle controles doorstaan, worden goedgekeurd en geïntegreerd in financiële systemen voor de administratie.
   * Afgewezen facturen activeren meldingen, en de inkoper kan een nieuwe factuur aanvragen.
6. **Integratie met Infor IDM & LN+M3**:
   * Goedgekeurde facturen worden waarschijnlijk naar Infor's IDM gestuurd voor documentbeheer en naar LN voor de boekhoudkundige verwerking.
   * Deze integratie zorgt ervoor dat alle financiële gegevens up-to-date zijn en dat de workflow naadloos aansluit op het bredere ERP-systeem.

#### Beslispunten:

* Door de hele workflow heen zijn er verschillende beslispunten waar een factuur kan worden goedgekeurd, afgewezen of teruggestuurd voor aanvullende informatie. Na vertragingen worden meldingen verstuurd, zodat een tijdige verwerking is gewaarborgd.

Deze workflows worden opgenomen in de standaardworkflow
