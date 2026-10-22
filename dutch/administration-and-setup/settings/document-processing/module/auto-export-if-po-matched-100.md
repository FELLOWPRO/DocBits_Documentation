# Automatisch exporteren bij een PO-overeenkomst van 100%

### Overzicht

De instelling **Auto Export if PO matched 100%** in de module voor inkooporders (PO) bepaalt of een volledige overeenkomst met de PO de huidige factuur of het huidige document kan laten doorgaan naar automatische export. De inkooporder is de vergelijkingsreferentie; deze instelling exporteert de inkooporder zelf niet.

### Werking

Als de instelling actief is, wordt het resultaat van de PO-matching van het huidige document gecontroleerd. Een overeenkomst van 100% voldoet aan deze matchvoorwaarde, maar garandeert geen onmiddellijke export. Documentvalidatie, het geconfigureerde exportproces, vereiste goedkeuringen en openstaande taken kunnen de export nog blokkeren of vertragen. Een onvolledige overeenkomst blokkeert automatische export op grond van deze voorwaarde.

### Voordelen

* **Efficiëntie:** Kan handmatig werk verminderen voor facturen die volledig overeenkomen met hun PO en aan de overige vereisten voldoen.
* **Controle:** Gebruikt het resultaat van de PO-matching als extra exportvoorwaarde.
* **Verwerkingstijd:** Kan de verwerking van geschikte facturen versnellen; het moment van export hangt af van de andere procesvoorwaarden.

### Gebruik

1. **Functie inschakelen:**
   * Open de instellingen voor de inkooporder.
   * Zoek de schakelaar **Auto Export if PO matched 100%** en zet deze aan.
2. **Verwerking volgen:**
   * Controleer de match-, validatie- en exportstatus van de huidige factuur.
   * Wordt deze ondanks een overeenkomst van 100% niet geëxporteerd, controleer dan de exportconfiguratie, vereiste goedkeuringen en openstaande taken.
3. **Configuratie controleren:**
   * Controleer of de matchcriteria en exportinstellingen bij het gewenste proces passen.
   * Beoordeel regelmatig de geëxporteerde facturen en uitzonderingen.

### Wanneer gebruiken?

* **Veel facturen:** Wanneer veel facturen betrouwbaar met inkooporders kunnen worden vergeleken.
* **Terugkerende inkopen:** Wanneer hoeveelheden, prijzen en andere matchcriteria stabiel zijn.
* **Tijdkritische verwerking:** Wanneer geschikte facturen automatisch moeten doorgaan zodra aan alle voorwaarden is voldaan.

Als de PO-matching voor het documenttype actief is, staat de afzonderlijke optie `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` ook de status `NO_MATCHABLE_PO_LINES` toe. Andere onvolledige matches worden hierdoor niet algemeen voor export vrijgegeven.
