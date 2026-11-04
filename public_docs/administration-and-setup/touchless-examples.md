# Voorbeelden: prijs en aantal

## Volledig voorbeeld: correcte extractie, afwijkende Infor-gegevens

Illustratief geval: factuur **10 stuks × €10 = €100**, correct uitgelezen. Geïmporteerde inkooporder **10 × €9 = €90**. Neem aan dat de actieve regels dit prijsverschil blokkeren.

1. Vergelijk origineel en extractie: de waarden kloppen.
2. Vergelijk import, actuele Infor-order, prijseenheid en tijd. Een onjuiste bron en verouderde kopie zijn andere oorzaken.
3. Inkoop bevestigt €10 en corrigeert de order. Was €9 afgesproken, dan moet de leveranciersfactuur worden opgehelderd.
4. Controleer of de juiste waarden DocBits hebben bereikt.
5. AP start handmatig opnieuw; na succes is de factuur **AP Assisted**, ondanks correcte extractie.
6. Controleer nieuwe facturen zonder verdere ingreep. Eerder behandelde facturen behouden hun geschiedenis.

Verander geen correct uitgelezen waarde en verruim geen tolerantie om verkeerde brongegevens te verbergen. Los de bevestigde oorzaak op. De voorbeeldafbeeldingen bewijzen dit volledige proces niet.

## Drie demo-orders: overeenkomst, prijs en aantal

Uitsluitend op **Dev** aangemaakt, met een fictieve leverancier, artikel en facturen. Elke factuur vermeldt **10 stuks × € 10 = € 100 netto**. De kaarten behouden de echte Nederlandse interface en vergroten de cijfers. Ze bewijzen geen klantverbinding met Infor, correcte extractie of succesvol automatisch afgerond proces.

| Geval | Factuur | Geïmporteerde order | Wat dit aantoont |
| --- | --- | --- | --- |
| PO01 / RE01 | 10 × € 10 = € 100 | 10 × € 10 = € 100 | Overeenkomstige bronwaarden; Pure vereist nog correcte extractie en afronding zonder ingreep of goedkeuring |
| PO02 / RE02 | 10 × € 10 = € 100 | 10 × € 9 = € 90 | Regelverschil € 10; circa 11,11 % van de orderprijs per stuk. Actieve regels bepalen de blokkade |
| PO03 / RE03 | 10 × € 10 = € 100 | 8 × € 10 = € 80 | Twee stuks meer, 25 % van het bestelde aantal; controleer open/ontvangen aantal en vergelijkingsbasis |

<figure><img src="../.gitbook/assets/touchless-owned-po-match-nl.png" alt="Fictieve PO01 met overeenkomstige waarden. Het vergrote echte detail toont aantal, prijs en totaal; dit alleen bewijst geen correcte extractie of Pure Touchless."><figcaption><p>Fictieve PO01 met overeenkomstige waarden. Het vergrote echte detail toont aantal, prijs en totaal; dit alleen bewijst geen correcte extractie of Pure Touchless.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/touchless-owned-po-price-nl.png" alt="Prijsgeval PO02: de geïmporteerde order toont 10 × 9 = 90 tegenover 10 × 10 = 100 op de fictieve factuur. Controleer overeengekomen prijs, prijseenheid en import. Vastgelegde menselijke ingreep plus succesvolle afronding: AP Assisted."><figcaption><p>Prijsgeval PO02: de geïmporteerde order toont 10 × 9 = 90 tegenover 10 × 10 = 100 op de fictieve factuur. Controleer overeengekomen prijs, prijseenheid en import. Vastgelegde menselijke ingreep plus succesvolle afronding: AP Assisted.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/touchless-owned-po-quantity-nl.png" alt="Aantalgeval PO03: 8 stuks besteld, 10 gefactureerd. Een leeg ontvangen aantal bewijst geen levering. De kaart toont de vergelijking, geen geslaagde matching."><figcaption><p>Aantalgeval PO03: 8 stuks besteld, 10 gefactureerd. Een leeg ontvangen aantal bewijst geen levering. De kaart toont de vergelijking, geen geslaagde matching.</p></figcaption></figure>

## Gerelateerde pagina’s

* [Touchless Intelligence](touchless-intelligence.md)
* [Metrieken en berekening](touchless-metrics.md)
* [Het dashboard gebruiken](touchless-dashboard.md)
* [Touchless Intelligence: Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: PO-matchingdiagnose](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Documentspoor](touchless-document-trace.md)
* [Touchless Intelligence: Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md)
* [Touchless uitleggen en verbeteren met MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
