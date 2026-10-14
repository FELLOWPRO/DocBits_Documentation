# Ons Document Prioriteit Systeem

In ons documentverwerkingssysteem verwerken we dagelijks een groot aantal documenten van meerdere klanten. Om ervoor te zorgen dat de documenten van elke klant tijdig worden verwerkt, hebben we een geavanceerd prioriteitssysteem geïmplementeerd. Dit systeem past de prioriteiten dynamisch aan op basis van het aantal uitstaande documenten dat een klant heeft, wat zorgt voor **eerlijkheid** en **efficiëntie**. Laten we bekijken hoe dit prioriteitssysteem werkt en wanneer de taakcounter wordt gereset.

**Belangrijke Concepten van het Prioriteitssysteem**

Ons prioriteitssysteem draait om een paar belangrijke concepten:

1. **Uitstaande Documenten**: Dit is een telling van de documenten die een klant heeft ingediend maar nog niet zijn verwerkt.
2. **Resetinterval**: Het systeem reset periodiek de telling van uitstaande documenten naar nul om ervoor te zorgen dat geen enkele klant de verwerkingsbronnen eindeloos kan monopoliseren.

**Hoe de Prioriteit Wordt Bepaald**

Hier is een stapsgewijze uitleg van hoe de prioriteit voor het verwerken van documenten wordt bepaald:

1. **Bijhouden van Uitstaande Documenten**: Elke klant heeft een telling van uitstaande documenten. Deze telling helpt ons te weten hoeveel documenten wachten om te worden verwerkt voor elke klant.
2. **Resetten van de Telling**: Om eerlijkheid te waarborgen, resetten we de telling van uitstaande documenten naar nul als er een bepaalde tijd (het resetinterval) is verstreken sinds de laatste update. Dit interval is standaard ingesteld op 1500 seconden (of 25 minuten).
3. **Bijwerken van de Telling**: Als het resetinterval nog niet is verstreken, verminderen we de telling van uitstaande documenten met één elke keer dat we controleren, wat de verwerking van een document simuleert.
4. **Instellen van Prioriteiten**: De prioriteit voor het verwerken van taken is gebaseerd op het aantal uitstaande documenten. Hoe minder uitstaande documenten, hoe hoger de prioriteit, wat betekent dat die taken eerder worden verwerkt. We hebben specifieke drempels om prioriteitsniveaus toe te wijzen van 1 (hoogste prioriteit) tot 9 (laagste prioriteit).

**Prioriteitsniveaus**

De prioriteitsniveaus worden toegewezen op basis van de telling van uitstaande documenten als volgt:

* **Prioriteit 9**: Als de telling van uitstaande documenten minder is dan -20
* **Prioriteit 8**: Als de telling van uitstaande documenten minder is dan -14
* **Prioriteit 7**: Als de telling van uitstaande documenten minder is dan -12
* **Prioriteit 6**: Als de telling van uitstaande documenten minder is dan -10
* **Prioriteit 5**: Als de telling van uitstaande documenten minder is dan -8
* **Prioriteit 4**: Als de telling van uitstaande documenten minder is dan -6
* **Prioriteit 3**: Als de telling van uitstaande documenten minder is dan -4
* **Prioriteit 2**: Als de telling van uitstaande documenten minder is dan -2
* **Prioriteit 1**: Als de telling van uitstaande documenten groter is dan of gelijk aan -2

{% hint style="info" %}
In eenvoudigere termen, naarmate het aantal uitstaande documenten toeneemt, daalt het prioriteitsniveau, wat betekent dat die documenten later worden verwerkt in vergelijking met andere met hogere prioriteiten.
{% endhint %}

**Wanneer de Telling Wordt Gereset**

De teller van uitstaande documenten wordt op nul gezet als er meer dan het resetinterval (**1500** seconden) is verstreken sinds de laatste update. Dit mechanisme zorgt ervoor dat geen enkele klant eindeloos uitstaande documenten kan accumuleren en de systeembronnen kan monopolizeren. Door de teller periodiek te resetten, garanderen we dat elke klant een eerlijke hoeveelheid verwerkingstijd krijgt.
