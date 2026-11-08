# Het foutscherm voor een afgewezen e-factuur

> Sommige interfaceteksten zijn in deze versie nog Engels of onjuist vertaald. De handleiding legt de betekenis uit; de schermafbeeldingen tonen de ongewijzigde interface.

Wanneer u een onjuiste e-factuur uploadt, raakt DocBits die niet kwijt. Het document krijgt de status **Fout** en het foutscherm vertelt u wat er mis is, waar en wat u daarna kunt doen. Deze pagina toont twee voorbeelden: een XML-bestand dat niet goed gevormd is en een factuur die een bedrijfsregel schendt.

> Een factuur krijgt alleen de status **Fout** wanneer validatie **aan** staat en **blokkeert** voor het documenttype. Zie [Validatie voor elk documenttype](validation-per-document-type.md).

## Voorbeeld 1: het XML-bestand is beschadigd

Een leverancier stuurt een XML-bestand waarin een sluittag niet overeenkomt met de openingstag. Het bestand kan niet worden gelezen, dus DocBits stopt bij de eerste controle, **L1 · XML-vormcontrole**.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-xml-malformed-nl-20261104-v2.png" alt="Foutscherm van een fictief XML-bestand met een bewust beschadigde sluittag. Sommige interfaceteksten zijn in deze versie nog Engels of onjuist vertaald. De handleiding legt de betekenis uit; de schermafbeeldingen tonen de ongewijzigde interface."><figcaption><p>Foutscherm van een fictief XML-bestand met een bewust beschadigde sluittag. Sommige interfaceteksten zijn in deze versie nog Engels of onjuist vertaald. De handleiding legt de betekenis uit; de schermafbeeldingen tonen de ongewijzigde interface.</p></figcaption></figure>

Het scherm heeft twee kanten:

* **Links: het XML-bestand.** DocBits toont het bestand met regelnummers. De regel met het probleem is rood gemarkeerd. Met de knoppen boven het bestand kopieert u de XML of opent u die in een nieuw tabblad.
* **Rechts: de uitleg.** De kaart **Afgewezen door** noemt de controle die het bestand heeft gestopt (hier **L1 · XML-vormcontrole**) en de regelcode (hier `XML-PARSE`). Daaronder ziet u een titel (*Het XML-bestand is niet correct opgebouwd*), een korte uitleg en het blok **Volgende stap**.

Selecteer **Bekijk validatiegegevens** om het volledige [validatierapport](validation-report.md) te openen.

<figure><img src="../../../../../.gitbook/assets/einvoice-report-xml-malformed-nl-20261104-v2.png" alt="Rapport van het beschadigde fictieve XML-bestand."><figcaption><p>Rapport van het beschadigde fictieve XML-bestand.</p></figcaption></figure>

Het rapport noemt de exacte positie (regel en kolom staan in het rapport) en geeft het technische bericht van de XML-parser. Selecteer **Weergeven in XML** om naar die regel te springen. De hint **Hoe los ik dit op?** zegt dat u de afzender om een gecorrigeerd bestand moet vragen.

## Voorbeeld 2: de factuur schendt een bedrijfsregel

De XML is in orde, maar een verplicht veld ontbreekt. De verkoper kan bijvoorbeeld niet worden geïdentificeerd omdat er geen verkopersidentificatie, registratie-identificatie of btw-identificatie aanwezig is (regel `BR-CO-26`).

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view-nl-20261104-v2.png" alt="Foutscherm van een volledig fictieve voorbeeldfactuur. Sommige interfaceteksten zijn in deze versie nog Engels of onjuist vertaald. De handleiding legt de betekenis uit; de schermafbeeldingen tonen de ongewijzigde interface."><figcaption><p>Foutscherm van een volledig fictieve voorbeeldfactuur. Sommige interfaceteksten zijn in deze versie nog Engels of onjuist vertaald. De handleiding legt de betekenis uit; de schermafbeeldingen tonen de ongewijzigde interface.</p></figcaption></figure>

De kaart toont de eerste blokkerende bevinding. Het volledige rapport bevat ook de code `BR-CO-26` en de overige bevindingen van de factuur.

## De knoppen onder de kaart

| Knop | Wat hij doet |
| --- | --- |
| **Verwerking opnieuw starten** | Voert de verwerking van het document opnieuw uit, bijvoorbeeld nadat u een instelling hebt gewijzigd. De controle gebruikt de huidige instellingen. |
| **Bekijk DocFlow** | Toont de workflow van het document. |
| **Details kopiëren** | Kopieert de foutgegevens, bijvoorbeeld voor een bericht aan uw beheerder. |
| **Ticket aanmaken** | Opent een supportticket met de foutgegevens. |

Selecteer **Toon technische details** op de kaart voor de ruwe technische informatie.

## Wat u daarna doet

* **Fouten:** vraag de afzender om een gecorrigeerde factuur, of [wijs het document af](validation-next-step-and-reject.md). Een gecorrigeerde factuur is een nieuw document.
* **Alleen waarschuwingen:** het document wordt niet geblokkeerd. U kunt doorgaan.

## Gerelateerde pagina's

* [Validatierapport](validation-report.md): alle bevindingen, niveau voor niveau.
* [Volgende stap en een document afwijzen](validation-next-step-and-reject.md)
* [Validatie voor elk documenttype](validation-per-document-type.md): schakel validatie in en stel blokkeren in.
