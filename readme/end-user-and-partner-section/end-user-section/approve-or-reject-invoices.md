# Een factuur goedkeuren of afwijzen

## Wat volgt op een goedkeuringsbesluit van een bedrijf

<figure><img src="../../.gitbook/assets/process-approval-nl-20261028.png" alt="Factuur goedkeuren of afwijzen: Controle, beslissing en verdere overdracht onderscheiden."><figcaption><p>Controle, beslissing en verdere overdracht onderscheiden. Het diagram is schematisch; de actieve instellingen van uw organisatie bepalen het daadwerkelijke gedrag.</p></figcaption></figure>

Technische validatie controleert documentgegevens; goedkeuring registreert de zakelijke beslissing van een geautoriseerde beoordelaar. Zelfs voor een technisch geldige factuur kan het zijn dat er nog één of meerdere goedkeuringen nodig zijn.

1. **Controleer verantwoordelijkheid:** Open de toegewezen factuur en controleer welk goedkeuringsniveau u mag bepalen.
2. **Bekijk de factuur:** Vergelijk kopwaarden, regelitems en belasting met het originele document en uw bedrijfsvereisten.
3. **Documentbeslissing:** Een correcte factuur goedkeuren of afkeuren met een specifieke reden. Wacht op het antwoord en controleer vervolgens de goedkeuringsgeschiedenis.
4. **Identificeer de volgende stap:** Als er aanvullende goedkeuringsfasen zijn geconfigureerd, wacht de factuur op hun beslissingen. Na afwijzing, verduidelijking, correctie en eventuele herindiening volgt u uw geconfigureerde proces. Het afzonderlijke exportproces bepaalt of gegevens het doelsysteem hebben bereikt.

### Drie uitspraken die niet hetzelfde betekenen

| verklaring | Wat het niet automatisch bewijst |
| --- | --- |
| **De gegevens zijn gevalideerd.** | Dat een geautoriseerde bedrijfsreviewer het heeft goedgekeurd. |
| **Een recensent heeft het goedgekeurd.** | Dat alle vereiste goedkeuringsfasen zijn voltooid. |
| **Goedkeuringen zijn voltooid.** | Dat de factuur al is geëxporteerd of geboekt in ERP. |

Gebruik [Documenteer taken](tasks.md) om toegewezen werk te verwerken en [Documentstatus](dashboard/document-status.md) om de huidige status te classificeren.

Deze video toont het goedkeuringsproces vanuit het perspectief van een beoordelaar.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/nl.mp4" %}
Een factuur goedkeuren of afwijzen
{% endembed %}

[Bekijk video met ondertiteling](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/nl.html)

De echte applicatie wordt getoond. De namen van opties kunnen per gebruikte versie verschillen.

Gebruik goedkeuring om uw inhoudelijke beslissing vast te leggen over een factuur die al is gevalideerd. U heeft toegang tot het document nodig en toestemming voor de huidige goedkeuringsfase. De video gebruikt een gewoon beoordelaarsaccount.

## Beoordelen en beslissen

1. Open de aan u toegewezen factuur en controleer de huidige goedkeuringsfase.
2. Vergelijk het factuurnummer, de leverancier, de datums en het totaal met het origineel. Controleer ook de factuurregels en de belasting. Technische validatie vervangt uw inhoudelijke controle niet.
3. Leg een duidelijke beoordelingsnotitie vast. Keur een correcte factuur goed, of wijs deze af met een specifieke reden wanneer verduidelijking nodig is. Wacht tot de bewerking is voltooid.
4. Heropen het document en inspecteer de goedkeuringsgeschiedenis. Controleer of de beoordelaar, het tijdstip, de beslissing en de volledige notitie correct zijn opgeslagen.

<figure><img src="../../.gitbook/assets/customer-check-nl-49417d7ce1df.png" alt="Ingevuld factuurformulier vergeleken met het origineel."><figcaption><p>Ingevuld factuurformulier vergeleken met het origineel.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/customer-rejected-nl-49417d7ce1df.png" alt="Bewaarde afwijzing met reden."><figcaption><p>Bewaarde afwijzing met reden.</p></figcaption></figure>

## Controleer de volgende fase

Wanneer een tweede goedkeuring is geconfigureerd, laat uw eerste goedkeuring de factuur wachten op een andere geautoriseerde beoordelaar. De factuur is nog niet volledig goedgekeurd. Een afwijzing vereist inhoudelijke opheldering; correctie en herindiening volgen uw geconfigureerde proces.

Een vermelding in de goedkeuringsgeschiedenis bewijst niet dat gegevens een ERP-systeem hebben bereikt. In dit geïsoleerde voorbeeld heeft het ophaalkanaal geen extern ERP-doel. De technische status `pending_data_fetch`, wanneer weergegeven, betekent dat het document wacht op het ophalen van gegevens.

## Gerelateerde pagina's

- [Validatiescherm](validation-screen/README.md)
- [Documenttaken](tasks.md)
