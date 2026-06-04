# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_rule_above_max.png" alt="DocBits Regel Above Max"><figcaption></figcaption></figure>

Deze titel geeft aan dat de regel is ontworpen om gevallen te beheren waarin het factuurtotaal hoger is dan het maximumbedrag dat een goedkeurder mag verwerken.

#### Regelconfiguratie:

1. **When…**
   * **Document Type is Invoice**: Deze voorwaarde zorgt ervoor dat de regel alleen van toepassing is op facturen, wat essentieel is om de workflow correct te sturen.
2. **And…**
   * **Document Status is Pending Approval**: De factuur moet de status "Pending Approval" hebben. Deze status is cruciaal om ervoor te zorgen dat de regel wordt toegepast op facturen die nog in behandeling zijn en nog niet zijn afgerond.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Deze voorwaarde controleert of het totaalbedrag van de factuur hoger is dan het maximumbedrag dat een goedkeurder mag verwerken. Deze vergelijking kan ook een tolerantie-instelling bevatten, waardoor kleine afwijkingen op basis van vooraf gedefinieerde criteria worden toegestaan.

#### Actie (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Als de factuur het opgegeven maximumbedrag overschrijdt, wordt deze automatisch toegewezen aan een goedkeurder op een hoger niveau, aangegeven door het veld 'Next Level Approver'. Als dit veld niet is ingevuld of de opgegeven gebruiker niet beschikbaar is, wordt een standaardgebruiker (waarschijnlijk een beheerder of een andere aangewezen medewerker) als fallback gebruikt om ervoor te zorgen dat de factuur zonder vertraging wordt beoordeeld.

#### Interface-elementen:

* **Add Card**: Met deze optie kunnen aanvullende voorwaarden of acties aan de regel worden toegevoegd, wat flexibiliteit biedt om complexe scenario's aan te pakken.
* **Save**: Met deze knop wordt de regelconfiguratie in het systeem opgeslagen.

#### Doel van deze regel:

Het doel van deze regel is ervoor te zorgen dat facturen die bepaalde financiële drempels overschrijden, worden beoordeeld door goedkeurders met de juiste autorisatieniveaus. Dit helpt bij het handhaven van financiële controle en toezicht, waarbij wordt gewaarborgd dat uitgaven worden beoordeeld door personeel met de vereiste goedkeuringslimieten, waardoor de organisatie wordt beschermd tegen ongeoorloofde of ongepaste uitgaven.

Deze regel, net als de vorige, helpt de workflow te automatiseren, vermindert handmatig werk en verbetert de naleving van het financiële beleid van de organisatie. Het is een voorbeeld van hoe workflowautomatisering effectief kan worden gebruikt om complexe financiële processen binnen een bedrijf te beheren.
