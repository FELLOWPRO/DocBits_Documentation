# Touchless Intelligence

Touchless Intelligence beantwoordt twee afzonderlijke vragen: **Heeft DocBits de factuur correct uitgelezen?** en **Is het hele proces zonder verwerkingsingreep afgerond?** Correct uitlezen kan toch werk opleveren als Infor-gegevens afwijken. AP is de menselijke crediteurenadministratie.

## Video: functies van het Touchless-rapport

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/nl.mp4" %}

Deze controleversie van 4:22 toont een gevuld rapport: filters, cijfers en berekening, trends, eerste blokkades, vastgelegd bewijs, documentverloop, uitvoeringen, geleerde regels, verbeteringen en geschiedenis, advies en echte MCP-resultaten.

[Open de video met Nederlandse ondertitels en 16 hoofdstukken](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/nl.html). De luisterbeoordeling van deze nieuwe versie is nog niet afgerond.

Deze leervoorbeelden verklaren rapportfuncties. Een aanbeveling of voorvertoning bewijst geen toegepaste instelling of gemeten verbetering. Het getoonde MCP-voorstel heeft nog een specifieke doelconfiguratie nodig; voorvertoning en toepassen zijn niet beschikbaar. Sommige oorspronkelijke productteksten kunnen in hun oorspronkelijke taal blijven staan. Bij geleerde regels geeft «20 van 21» aan op hoeveel gevallen de regel van toepassing is. Het tegenvoorbeeld toont een al geaccepteerde waarde die de regel zou vervangen; sommige oorspronkelijke labels vertalen dit onjuist.

<figure><img src="../.gitbook/assets/anatomy-touchless-nl.svg" alt="Isometrische sorteerlijn: een transportband met 14 poorten, een duwer die één document naar een controlebak verplaatst, een exportbak met een stapel documenten en een wijzerplaat met 78,9 procent"><figcaption><p>Touchless als sorteerlijn, met de illustratieve getallen uit het rekenvoorbeeld: de 14 poorten zijn de fasen van het Pipeline Path, vellen die nog op de band liggen zijn in behandeling en tellen niet mee, een document dat bij een poort stopt wordt in de controlebak geduwd bij de documenten met AP Assisted (30) en procesuitzondering (10), en de Pure Touchless- (120) en alleen-goedkeuringsdocumenten (30) in de exportbak geven op de wijzerplaat 150 van 190, oftewel 78,9 %, voorbij de doelmarkering van 70 %.</p></figcaption></figure>

## Vind de juiste handleiding

| Handleiding | Inhoud |
| --- | --- |
| [Metrieken en berekening](touchless-metrics.md) | Categorieën, teller/noemer, acties en rekenvoorbeelden |
| [Het dashboard gebruiken](touchless-dashboard.md) | Filters, indicatoren, trends en eerste blokkades |
| [Voorbeelden: prijs en aantal](touchless-examples.md) | Fictieve facturen en echte Dev-beelden met prijs- en aantalverschillen |
| [Touchless Intelligence: Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md) | Leveranciers en terugkerende oorzaken prioriteren |
| [Touchless Intelligence: PO-matchingdiagnose](touchless-po-matching-diagnosis.md) | Actieve regels, toleranties en beslissingen begrijpen |
| [Touchless Intelligence: Documentspoor](touchless-document-trace.md) | Origineel, uitvoeringen, blokkades en ingrepen controleren |
| [Touchless Intelligence: Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md) | Voorbeeld, toepassing, meting en terugdraaien onderscheiden |
| [Touchless uitleggen en verbeteren met MCP](touchless-mcp.md) | Verklaren, diagnosticeren en gecontroleerd verbeteren met MCP |

<figure><img src="../.gitbook/assets/touchless-overview-nl.png" alt="Het tabblad Touchless Intelligence met vijf kerncijfers, verbetersuggesties en de grafiek van het touchless-percentage"><figcaption><p>Het tabblad Touchless Intelligence: kerncijfers, verbeteringen, het percentage in de tijd en de grafiek waar touchless het eerst verloren gaat. Voorbeeldorganisatie met demogegevens; de namen van leveranciers zijn fictief.</p></figcaption></figure>

## Toegang

Onderdeel van het [analysedashboard](analytics-dashboard.md). Beheerders hebben toegang; andere gebruikers hebben de bijbehorende rolmachtiging nodig. AI-analyse, ondersteunde wijzigingen en rapporten kunnen beheerdersrechten vereisen.

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
