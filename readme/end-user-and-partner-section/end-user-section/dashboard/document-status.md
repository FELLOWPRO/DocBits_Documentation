# Documentstatus

## Drie statusvragen in plaats van één statusketen

<figure><img src="../../../.gitbook/assets/process-status-nl-20261028.png" alt="Classificeer de documentstatus correct: Verwerking, goedkeuring en export zijn verschillende toestanden."><figcaption><p>Verwerking, goedkeuring en export zijn verschillende toestanden. Het diagram is schematisch; de actieve instellingen van uw organisatie bepalen het daadwerkelijke gedrag.</p></figcaption></figure>

Het kan zijn dat een document nog steeds wacht op een zakelijke goedkeuringsbeslissing, ook al is de erkenning voltooid. Lees de weergegeven status in de context van de verwerkingsstap en uw goedkeuringsproces.

| Vraag | Betekenis | Volgende stap |
| --- | --- | --- |
| **Is de verwerking voltooid?** | OCR, classificatie en extractie bereiden het document voor op beoordeling. “Klaar voor validatie” is geen zakelijke goedkeuring. | Open het document, vergelijk de informatie met het origineel en bewerk verplichte veldfouten. |
| **Is de inhoudelijke goedkeuringsbeslissing afgerond?** | Een goedkeuring kan verschillende niveaus hebben. Een eerste goedkeuring doorloopt niet automatisch alle fasen. | Controleer het huidige niveau, de verantwoordelijke beoordelaar en de goedkeuringsgeschiedenis. |
| **Is het document overgedragen?** | Exportstatus en feedback beschrijven de technische overdracht. Een opgeslagen waarde of goedkeuringsinvoer bewijst geen ERP-verwerking. | Lees de exportdetails en reproduceer indien nodig het proces in het doelsysteem. |

De afbeelding organiseert deze vragen in drie sporen. Het is geen uitputtende lijst van technische statuscodes en vestigt geen universele orde. De daadwerkelijke transities zijn afhankelijk van het documenttype, de workflow en het exportpad.

### Als er fouten optreden, begin dan met de betreffende stap

Open de foutstatus en lees het bericht. Als een vereiste waarde ontbreekt, controleer deze dan en corrigeer deze met het origineel. Als de ontvanger een exportfout meldt, los dan de oorzaak ervan op voordat u het opnieuw probeert. Gebruik [Documentstroom](document-flow.md) voor verwerkingsstappen en de [Goedkeuring](../approve-or-reject-invoices.md)-handleiding voor zakelijke goedkeuringsbeslissingen.

Verwerkingsstatussen tonen stappen zoals OCR, classificatie of export. **Klaar voor validatie** betekent dat het document kan worden gecontroleerd. Goedkeuringsstatussen geven aan dat goedkeuring nog nodig is. **Geëxporteerd** geeft aan dat de documentexport klaar is. Klik op de status **Fout** voor beschikbare foutdetails.

Als verwerkingstijden beschikbaar zijn, houdt u de aanwijzer boven een status om de fasen en hun duur te zien. Documenten met mogelijke duplicaten tonen een duplicaatpictogram; open dit om de gerelateerde documenten te vergelijken.

Open een rij om in het validatiescherm te werken. Het actiemenu biedt toegestane bewerkingen, zoals toewijzen, downloaden, geschiedenis bekijken of de verwerking opnieuw starten. Downloadvarianten hangen van het document af en kunnen aantekeningen of elektronische factuurformaten bevatten.

Selecteer meerdere documenten met de selectievakjes en open het menu in de tabelkop voor toegestane bulkacties, zoals toewijzen, samenvoegen, herstarten, export herstarten of verwijderen. Controleer de selectie en iedere bevestiging. Deze acties kunnen documenten wijzigen; een weergave opslaan wijzigt alleen de presentatie van de werklijst.

De [dashboardhandleiding](README.md) beschrijft zoeken, documentacties en opgeslagen weergaven.


## Videohandleiding: Geblokkeerde facturen verder verwerken

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/blocked-invoices-customer/v1/nl.mp4" %}
Geblokkeerde facturen verder verwerken
{% endembed %}

[Bekijken met ondertiteling en hoofdstukken](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/blocked-invoices-customer/v1/nl.html)

Sommige oorspronkelijke productlabels kunnen in een andere taal staan. Technische veld-ID’s blijven behouden.

Ik open de factuur in de veldvalidatie. In dit voorbeeld ontbreekt het factuurnummer. De overige waarden zijn al ingevuld. Ik vergelijk ze met het origineel voordat ik iets verander.

Nu vul ik het factuurnummer in en verlaat ik het veld. Daarna sla ik de factuur op. Ik wacht op de reactie en laad het document opnieuw. Zo zie ik of de correctie echt behouden blijft.

Het nummer staat er nog steeds na het opnieuw openen. De fout van het verplichte veld is opgelost. Opslaan betekent echter nog niet dat de factuur is goedgekeurd of naar het ERP is geëxporteerd.

Bij een tweede factuur toont de lijst een exportfout. Ik open de status en lees de details. De testontvanger heeft de verzonden gegevens afgewezen met foutcode vierhonderdtweeëntwintig. Hier moet de technische mapping worden gecontroleerd. Ik start de export niet zomaar meerdere keren opnieuw.

<figure><img src="../../../.gitbook/assets/customer-error-nl-recovery-export-v1.png" alt="Exportfout en antwoord van de ontvanger"><figcaption><p>Exportfout en antwoord van de ontvanger</p></figcaption></figure>

Bij de taken op het document maak ik een duidelijke taak voor onze testbeheerder. Ik noem de foutcode en vraag om het factuurnummer in de mapping te controleren. Voor deze training blijft het verzenden van e-mails uitgeschakeld.

Na het opnieuw laden controleer ik of de taak is opgeslagen en aan de juiste persoon is toegewezen. De taak blijft open totdat de oorzaak is opgehelderd. Een aangemaakte taak is nog geen succesvolle export.

<figure><img src="../../../.gitbook/assets/customer-verify-nl-recovery-export-v1.png" alt="Opgeslagen overdrachtstaak toegewezen aan de beheerder"><figcaption><p>Opgeslagen overdrachtstaak toegewezen aan de beheerder</p></figcaption></figure>
