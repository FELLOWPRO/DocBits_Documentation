# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_rule_cost_invoice.png" alt="DocBits Regel Cost Factuur"><figcaption></figcaption></figure>

Deze titel geeft aan dat de regel specifiek is geconfigureerd voor het beheren van kostenfacturen en een exportactie omvat, mogelijk voor rapportage, verdere verwerking of integratie met andere systemen.

#### Regelconfiguratie:

1. **When…**
   * **Document Type is Invoice**: Deze voorwaarde zorgt ervoor dat de regel alleen wordt geactiveerd voor documenten die als facturen zijn gecategoriseerd, waardoor de workflow specifiek gericht blijft op factuurbeheer.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Dit geeft aan dat de regel alleen van toepassing is op facturen die in een bepaald veld binnen het document expliciet zijn gemarkeerd als "Cost Invoices". Dit helpt om ze te onderscheiden van andere soorten facturen.
   * **Document Status is Pending Second Approval**: De factuur moet de status "Pending Second Approval" hebben. Dit geeft aan dat de factuur al een eerste goedkeuring heeft doorlopen en wacht op een tweede, mogelijk laatste, beoordeling.

#### Actie (Then…):

* **Start Export**: Zodra de factuur aan de opgegeven voorwaarden voldoet (een kostenfactuur die in afwachting is van een tweede goedkeuring), wordt de actie "Start Export" uitgevoerd. Dit kan inhouden dat de factuurgegevens naar een ander systeem worden gestuurd voor financiële analyse, rapportage of nalevingsdoeleinden.

#### Doel van deze regel:

* **Workflowefficiëntie**: Deze regel helpt de afhandeling van kostenfacturen te automatiseren door ervoor te zorgen dat ze zonder handmatige tussenkomst door de noodzakelijke goedkeuringsfasen worden verwerkt, waardoor de snelheid en nauwkeurigheid van financiële handelingen toenemen.
* **Controle en naleving**: Door een tweede goedkeuring te vereisen, dwingt het systeem een controlemechanisme af dat ervoor zorgt dat kostenfacturen grondig worden beoordeeld, wat het financiële toezicht verbetert.
* **Integratie en rapportage**: De exportactie suggereert dat zodra facturen volledig zijn goedgekeurd, ze kunnen worden geïntegreerd in andere systemen voor verdere verwerking of analyse, wat cruciaal is voor financiële rapportage en audits.

Dit soort regels is van essentieel belang voor organisaties die met verschillende soorten facturen te maken hebben en ervoor moeten zorgen dat elk type volgens specifieke protocollen wordt afgehandeld. Het vermindert het risico op fouten en waarborgt de naleving van interne controles en externe regelgeving.
