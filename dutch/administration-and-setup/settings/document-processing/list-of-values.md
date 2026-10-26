# Waardenlijsten

## Videotutorial: Stamgegevens en waardelijsten

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/master-data-lists-admin/v1/nl.mp4" %}
Bronnen voor stamgegevens, waardelijsten en mastergegevensinstellingen in DocBits
{% endembed %}

De video toont de bronnen voor stamgegevens, de waardelijsten en de mastergegevensinstellingen van een documenttype.

Waardenlijsten bevatten vooraf ingestelde opties voor documentvelden. Een veld kan een lijst gebruiken om opties tijdens validatie te tonen. Labels kunnen worden vertaald; de technische waarde blijft in alle talen gelijk.

## Lijsten openen

Open in de instellingen de stamgegevens en waardenlijsten. Selecteer een lijst om de waarden te bekijken. Geconfigureerde namen zijn afgeschermd.

<figure><img src="../../../.gitbook/assets/s150-list_of_values_1-nl.png" alt="Waardenlijsten met afgeschermde geconfigureerde namen."><figcaption><p>Waardenlijsten met afgeschermde geconfigureerde namen.</p></figcaption></figure>

## Een lijst maken

1. Kies de optie om een nieuwe lijst te maken.
2. Voer een naam in en beperk de lijst zo nodig tot een suborganisatie.
3. Controleer de gegevens voordat u opslaat.

Standaardlijsten worden door het systeem geleverd en kunnen niet worden verwijderd. Controleer vóór verwijdering van een eigen lijst welke velden deze gebruiken: de actie kan direct effect hebben.

## Waarden toevoegen en wijzigen

Open de bedoelde lijst en voeg een rij toe. Controleer per waarde:

| Eigenschap | Betekenis |
| --- | --- |
| Waarde | Technische waarde die DocBits opslaat, gelijk voor alle talen. |
| Label | Tekst voor de geselecteerde taal. Zonder label voor de actieve taal verschijnt de technische waarde. |
| Taal | Taal van het label. |
| Suborganisaties | Bereik waarin de waarde beschikbaar is; zonder beperking geldt deze voor alle suborganisaties. |
| Synoniemen | Varianten die bij de waarde horen, bijvoorbeeld EURO en € voor EUR. Bevestig elk synoniem in het daarvoor bedoelde veld. |

Controleer alle eigenschappen voordat u opslaat. Bewerk- en verwijderacties hangen af van uw rechten en de geselecteerde waarde. Systeemwaarden kunnen niet worden verwijderd.

## Importeren uit CSV

Open de acties van de bedoelde lijst en kies CSV-import. Selecteer het bestand en het juiste scheidingsteken, bijvoorbeeld `;` of `,`. Controleer de structuur en inhoud voordat u importeert.

## Vertalingen toevoegen

Voeg bij een waarde een taal toe en voer het bedoelde label in. Herhaal dit voor andere benodigde talen, controleer alles en sla op. U kunt vertaalde labels toevoegen aan systeemwaarden die niet kunnen worden verwijderd.

Een vertaald label verandert de technische waarde niet. Controleer het veld na bedoelde wijzigingen in de validatie en gewenste taal. De afbeelding toont raadpleging van de lijsten en bewijst geen opgeslagen wijziging of uitgevoerde import.
