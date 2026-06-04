# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../../.gitbook/assets/docbits_rule_purchase_invoice_unit_price_export.png" alt="DocBits Regel Aankoop Factuur Unit Price Exporteren"><figcaption></figcaption></figure>

Deze titel geeft aan dat de regel is opgezet om de tweede goedkeuringsfase van inkoopfacturen te beheren, met de nadruk op de eenheidsprijs, om ervoor te zorgen dat deze overeenkomt met de overeengekomen voorwaarden.

#### Regelconfiguratie:

1. **When…**
   * **Document Type is Invoice**: Deze voorwaarde zorgt ervoor dat de regel alleen wordt geactiveerd voor documenten die als facturen zijn geïdentificeerd, wat cruciaal is om de workflow nauwkeurig te sturen.
2. **And…**
   * **Document Status is Pending Second Approval**: Dit geeft aan dat de factuur wacht op een tweede goedkeuring. Deze fase biedt vaak extra toezicht om de nauwkeurigheid te waarborgen voordat de transactie wordt afgerond.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Deze voorwaarde geeft verder aan dat de regel alleen van toepassing is op facturen die specifiek als "Purchase Invoices" zijn gecategoriseerd, om ze te onderscheiden van andere soorten facturen.
   * **Logic Unit Price in order confirmation Equals purchase order**: Deze voorwaarde controleert of de eenheidsprijs die in de orderbevestiging is vermeld, overeenkomt met de eenheidsprijs in de inkooporder. Het zorgt ervoor dat de factuurverwerking alleen wordt voortgezet als er consistentie is in de prijsstelling, wat cruciaal is voor budgettering en financiële rapportage.

#### Actie (Then…):

* **Start Export**: Zodra de factuur aan de opgegeven voorwaarden voldoet (d.w.z. de eenheidsprijzen komen overeen tussen de orderbevestiging en de inkooporder), wordt de actie "Start Export" geactiveerd. Dit houdt waarschijnlijk in dat de factuurgegevens worden geëxporteerd voor verdere verwerking, mogelijk naar een ander financieel systeem of voor rapportagedoeleinden.

#### Doel van deze regel:

* **Nauwkeurigheid en consistentie waarborgen**: Door te verifiëren dat de eenheidsprijzen overeenkomen tussen de orderbevestiging en de inkooporder, helpt het systeem de financiële nauwkeurigheid te behouden en voorkomt het te veel of te weinig in rekening brengen.
* **Financiële verwerking stroomlijnen**: Het automatiseren van de export van gegevens zodra de prijzen zijn bevestigd, vermindert handmatige verwerking en versnelt de financiële verwerkingscyclus.
* **Naleving en toezicht verbeteren**: Het vereisen van een tweede goedkeuring voor prijsverificatie voegt een extra laag toezicht toe, wat cruciaal is voor de naleving van financieel beleid en financiële controles.

Deze regel is een voorbeeld van hoe workflowautomatisering effectief kan worden ingezet om een nauwkeurige en efficiënte afhandeling van financiële documenten binnen een organisatie te waarborgen, met name in de context van grote transactievolumes die zorgvuldige validatie vereisen.
