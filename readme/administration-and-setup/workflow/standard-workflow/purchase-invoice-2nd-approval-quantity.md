# Inkoopfactuur: tweede goedkeuring van hoeveelheid



Deze regel behandelt inkoopfacturen tijdens een tweede goedkeuringsfase en richt zich op de juistheid van de vermelde aantallen.

#### Regelconfiguratie:

1. **Wanneer…**
   * **Document Type is Invoice**: de regel wordt alleen geactiveerd voor documenten die als factuur zijn geclassificeerd.
2. **En…**
   * **Document Status is Pending Second Approval**: de factuur wacht op een tweede goedkeuring, bedoeld als extra controle vóór de definitieve verwerking.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: beperkt de regel tot facturen van het subtype "Purchase Invoice".
   * **Logic Quantity in order confirmation Not Equals purchase order**: vergelijkt het aantal in de orderbevestiging met het aantal op de oorspronkelijke inkooporder. Een verschil activeert de actie, zodat een mogelijke fout kan worden onderzocht.

#### Actie (dan…):

* **Assign user from field Buyer Name, use user User as fallback**: bij een verschil in aantallen wordt de factuur ter controle toegewezen aan de persoon uit het veld Buyer Name. Is dit veld leeg of is de persoon niet beschikbaar, dan wordt de ingestelde gebruiker User als terugvaloptie gebruikt.

#### Doel van deze regel:

* **Nauwkeurigheid en naleving**: de regel helpt facturatie af te stemmen op de afspraken in de inkooporder en financiële verschillen en voorraadfouten te voorkomen.
* **Snellere goedkeuring**: automatische toewijzing bij specifieke afwijkingen zorgt dat de juiste medewerker problemen snel kan beoordelen.
* **Sterkere financiële controle**: een tweede goedkeuring voor de controle van aantallen versterkt het toezicht en de verantwoording binnen de organisatie.

Dit voorbeeld laat zien hoe workflowautomatisering de efficiëntie en financiële betrouwbaarheid kan verbeteren bij complexe inkoopprocessen.
