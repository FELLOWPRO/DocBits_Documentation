# E-documenten

DocBits valideert binnenkomende elektronische facturen (e-facturen) aan de hand van de officiële standaarden — **XRechnung**, **ZUGFeRD** en **Factur-X** — en routeert eventuele gevonden problemen naar de juiste verwerker. De instellingengroep **E-documenten** (onder **Documentverwerking**) heeft twee pagina's:

* **[Validatieregels](validation-rules.md)** — kies welke e-factuurversies en -profielen u accepteert en stel de ernst van elke validatieregel in voor uw organisatie.
* **[Notificatierouting](notification-routing.md)** — koppel validatiebevindingen aan de AI Workforce-agent die ze moet afhandelen.

Samen bepaalt u hiermee **wat als een probleem geldt** op een binnenkomende e-factuur en **wie het afhandelt**.

## E-factuurvalidatie in- of uitschakelen

De twee E-documenten-pagina's werken pas zodra de **e-factuurvalidatie is ingeschakeld voor het documenttype**. De schakelaar staat op het documenttype zelf, niet in het menu E-documenten.

Ga naar **Instellingen → Documenttypen → Factuur → Geavanceerde instellingen** en open de sectie **E-factuurvalidatie**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="De schakelaars voor e-factuurvalidatie op het documenttype Factuur"><figcaption><p>Schakel e-factuurvalidatie per documenttype in of uit, met optionele leveranciersnotificatie</p></figcaption></figure>

* **Binnenkomende e-facturen valideren** — de hoofdschakelaar. Wanneer **ingeschakeld** wordt elke geüploade factuur gecontroleerd aan de hand van de KoSIT XRechnung Schematron-regels plus de semantische controles L0 (PDF/A-3) en L4 (IBAN/btw), met de ernstniveaus die u op de pagina [Validatieregels](validation-rules.md) hebt ingesteld. Ongeldige facturen worden geblokkeerd. Wanneer **uitgeschakeld** slaan facturen de e-factuurvalidatie volledig over en hebben de pagina's Validatieregels en Notificatierouting geen effect.
* **Leverancier melden bij afwijzing** — verschijnt zodra validatie is ingeschakeld. Wanneer **ingeschakeld** stuurt een afgewezen factuur een e-mail naar de leverancier met de ontbrekende of onjuiste velden, zodat hij de factuur opnieuw kan uitgeven. Wie elke bevinding ontvangt en afhandelt, configureert u op de pagina [Notificatierouting](notification-routing.md).

> E-factuurvalidatie wordt **per documenttype** geconfigureerd. Op dit moment geldt het voor het documenttype **Factuur**; schakel het in voor elk documenttype dat gevalideerd moet worden.
