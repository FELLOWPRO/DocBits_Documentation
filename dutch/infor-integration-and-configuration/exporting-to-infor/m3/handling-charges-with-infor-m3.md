# Toeslagen verwerken met Infor M3

## Overzicht

Dit document beschrijft hoe DocBits met Infor M3 samenwerkt om kosten op facturen en inkooporders te verwerken. Het bevat scenario's voor externe kosten en de verwachte oplossingen.

## Scenario's voor kostenverwerking

| Scenario-ID | Beschrijving                                                                          | Praktijksituatie                                                                                                                          | Verwachte oplossing                                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | Externe kosten alleen op de factuur (geaccepteerd)                                 | Er staan externe kosten op de factuur die niet op de inkooporder staan. Deze kosten worden geaccepteerd.                                       | De kosten worden geboekt volgens boekingsregel PP20-228 op basis van het kostenelement dat DocBits verstuurt.                                                                                                                                        |
| 2           | Externe kosten alleen op de factuur (niet geaccepteerd)                             | Er staan externe kosten op de factuur die niet op de inkooporder staan. Deze kosten worden niet geaccepteerd of goedgekeurd.                       | Het totale factuurbedrag wordt geboekt met de niet-goedgekeurde kosten op kopniveau. Voor deze kosten wordt ook een debetnota aangemaakt.                                                                                               |
| 3           | Hogere of lagere externe kosten op de factuur (binnen tolerantie)             | De externe kosten op de factuur zijn hoger of lager dan op de inkooporder, maar vallen binnen de geaccepteerde tolerantie.                          | Extra kosten worden geboekt volgens boekingsregel PP20-228 op basis van het kostenelement dat DocBits verstuurt.                                                                                                                                      |
| 4           | Hogere externe kosten op de factuur (buiten tolerantie, niet goedgekeurd)        | De externe kosten op de factuur zijn hoger dan op de inkooporder en vallen buiten de geaccepteerde tolerantie. Ze zijn niet goedgekeurd.        | Het totale factuurbedrag wordt geboekt. De extra niet-goedgekeurde kosten worden op kopniveau toegevoegd en er wordt een debetnota voor aangemaakt.                                                             |
| 5 | Hogere externe kosten op de factuur (buiten tolerantie, goedgekeurd in DocBits) | De externe kosten op de factuur zijn hoger dan op de inkooporder en vallen buiten de geaccepteerde tolerantie. Ze zijn goedgekeurd in DocBits. | Extra kosten worden geboekt volgens PP20-228. Er worden twee opties overwogen:\<br>- Als de APS900-tolerantie > DocBits is, worden extra kosten automatisch geboekt.\<br>- Als de APS900-tolerantie = DocBits is, worden extra kosten geboekt met nieuwe kostenelementen die niet op de inkooporder staan. |
| 6           | Lagere externe kosten op de factuur (buiten tolerantie, niet goedgekeurd)         | De externe kosten op de factuur zijn lager dan op de inkooporder en vallen buiten de geaccepteerde tolerantie. Ze zijn niet goedgekeurd.         | De factuur wordt als niet-goedgekeurd geboekt in APS110. De crediteurenadministratie past de kosten aan via Invoice Control in APS110, waarmee APS360 wordt geopend.                                                                                          |
| 7           | Externe kosten op de inkooporder en geen kosten op de factuur                                      | Er staan externe kosten op de inkooporder, maar niet op de factuur.                                                        | De factuur wordt als niet-goedgekeurd geboekt in APS110. De crediteurenadministratie past de kosten aan via Invoice Control in APS110, waarmee APS360 wordt geopend.                                                                                          |

## Voorbeeld voor scenario 5

| Veld          | Inkooporderwaarde | Waarde van de leveranciersfactuur |
| -------------- | -------- | ---------------------- |
| Regel 1         | $6000    | $6000                  |
| Vrachtkosten (E001) | $1000    | $3000                  |
| **Totaal**      | $7000    | $9000                  |

**Tolerantie voor vrachtkosten:** $100 wordt automatisch goedgekeurd in M3 (APS900) en DocBits. Het totale factuurbedrag van $9000 wordt inclusief kosten handmatig goedgekeurd.

**APS451 (factuurregel):**

* Regeltype 1 (factuurregel): $9000
* Regeltype 5 (regelkosten): $1000 (element: E001 voor vrachtkosten van $1000 op de inkooporder)
* Regeltype 5 (regelkosten): $2000 (element: E101 voor vrachtkosten van $0 op de inkooporder)

### Belangrijke velden en waarden voor kostenverwerking in DocBits

| Veld                       | Beschrijving                                              |
| --------------------------- | -------------------------------------------------------- |
| Volgnummer             | Unieke identificatie van elk kostenscenario               |
| Kostenelement-ID          | Identificatie van het kostenelement                       |
| Omschrijving van het kostenelement | Omschrijving van het kostenelement                       |
| Kostentype                 | Doorgaans "External"                                    |
| Kostenfacturatie            | Relevantie moet nog worden bepaald                         |
| Verdelingsmethode         | Methode om de kosten te verdelen                 |
| Brutogewicht                | Van toepassing als het brutogewicht op de factuur staat   |
| Volume                      | Toepasselijke situaties moeten nog worden bepaald                      |
| Nettobedrag                  | Toepasselijke situaties moeten nog worden bepaald                      |
| Kosten van derden            | Aanwezigheid op de factuur en verwerkingseisen      |
| Hoeveelheid voor factuurkosten     | Verdere toelichting nodig                                     |
| Opslag                      | Verondersteld verschil tussen kosten en korting |
| Kostencategorie             | Relevantie moet nog worden bepaald                            |
| Kostenoperator            | Relevantie moet nog worden bepaald                            |

\\
