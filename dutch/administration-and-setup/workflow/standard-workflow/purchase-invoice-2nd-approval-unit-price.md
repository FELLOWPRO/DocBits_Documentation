# Inkoopfactuur: tweede goedkeuring van eenheidsprijs



Deze regel behandelt de tweede goedkeuringsfase van een inkoopfactuur en controleert specifiek de eenheidsprijs.

#### Regelconfiguratie:

1. **Wanneer…**
   * **Document Type is Invoice**: de regel wordt uitsluitend geactiveerd voor documenten die als factuur zijn herkend.
2. **En…**
   * **Document Status is Pending Second Approval**: de factuur wacht op een tweede goedkeuring als extra controle vóór de definitieve verwerking.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: beperkt de regel tot facturen van het subtype "Purchase Invoice".
   * **Logic Unit Price in order confirmation Not Equals purchase order**: vergelijkt de eenheidsprijs in de orderbevestiging met die op de oorspronkelijke inkooporder. Als deze verschillen, wordt de actie geactiveerd voor verdere beoordeling.

#### Actie (dan…):

* **Assign user from field Buyer Name, use user User as fallback**: bij een verschil in eenheidsprijzen wordt de factuur toegewezen aan de inkoper uit het veld Buyer Name. Is dit veld leeg of niet ingevuld, dan wordt de ingestelde gebruiker User als terugvaloptie gebruikt voor de goedkeuring.

#### Doel van deze regel:

* **Nauwkeurigheid en naleving**: de regel helpt facturatie af te stemmen op gemaakte afspraken. Een controle bij afwijkende eenheidsprijzen helpt financiële fouten en mogelijke fraude te voorkomen.
* **Snellere goedkeuring**: automatische toewijzing bij specifieke afwijkingen zorgt dat de juiste medewerker problemen snel kan beoordelen.
* **Financiële controle**: een tweede goedkeuring op basis van prijsvergelijking versterkt het toezicht en de verantwoording binnen de organisatie.
