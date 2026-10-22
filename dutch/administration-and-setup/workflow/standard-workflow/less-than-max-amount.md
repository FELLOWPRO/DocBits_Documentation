# Onder het maximumbedrag



Deze titel duidt op een regel voor facturen waarvan het totaalbedrag kleiner dan of gelijk aan een ingesteld maximumbedrag is.

#### Regelconfiguratie:

1. **Wanneer…**
   * **Document Type is Invoice**: controleert of het verwerkte document een factuur is, zodat de regel uitsluitend op facturen wordt toegepast.
2. **En…**
   * **Document Status is Pending Approval**: de factuur moet de status "Pending Approval" hebben, dus wachten op goedkeuring.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: vergelijkt het factuurtotaal met het maximale bedrag dat de goedkeurder mag goedkeuren. Als het totaal kleiner dan of gelijk aan dat maximum is, gaat de regel verder. Mogelijk is daarbij een tolerantie voor kleine afwijkingen ingesteld.

#### Actie (dan…):

* **Assign user from field Approver Name, use user User as fallback**: als aan de voorwaarden is voldaan, wordt de factuur toegewezen aan de goedkeurder uit het veld Approver Name. Als dit veld leeg of niet beschikbaar is, wordt de ingestelde gebruiker User als terugvaloptie gebruikt om de goedkeuring af te handelen.

#### Interface-elementen:

* **Add Card**: met deze knop kunt u voorwaarden of acties aan de regel toevoegen om de workflow verder af te stemmen.
* **Save**: slaat de ingestelde regel op in het systeem.

#### Doel van deze regel:

Deze regel stroomlijnt factuurgoedkeuring door facturen op basis van hun bedrag aan de juiste goedkeurder toe te wijzen. Alleen facturen binnen de ingestelde grens worden zo afgehandeld. Dit ondersteunt financiële controles en versnelt de workflow door handmatige controles te verminderen.

\\
