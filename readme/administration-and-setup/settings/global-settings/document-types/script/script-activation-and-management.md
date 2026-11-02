# Scripts activeren en beheren

## Videohandleiding: scripts beheren

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-manage-scripts/v4/nl.mp4" %}
De scripts van een documenttype beheren
{% endembed %}

De video toont de scriptlijst met filter en sortering, activeren en deactiveren, kopiëren, de versiegeschiedenis en verwijderen met bevestiging.

Open het documenttype en het bijbehorende scriptbeheer. De lijst toont scripts en acties voor bewerken, kopiëren en status. Namen zijn in het voorbeeld afgeschermd.

<figure><img src="../../../../../.gitbook/assets/s150-docbits_edit_script_icon-nl.png" alt="Scriptbeheer en bewerkingsacties; namen zijn afgeschermd."><figcaption><p>Scriptbeheer en bewerkingsacties; namen zijn afgeschermd.</p></figcaption></figure>

Filter op status of zoek het bedoelde script voordat u het opent. Controleer documenttype, uitvoeringsmoment en code voordat u opslaat.

De lijst staat standaard op uitvoeringsvolgorde; met de sorteerknoppen schakelt u naar naam (A-Z / Z-A) of naar de wijzigingsdatum. Elke kaart toont de uitvoeringsvolgorde als genummerd label naast de naam van het script.

<figure><img src="../../../../../.gitbook/assets/core2170-script-execution-order-list-nl.png" alt="Scriptlijst gesorteerd op uitvoeringsvolgorde; elke kaart toont naast de naam een genummerd label met de uitvoeringsvolgorde"><figcaption><p>Het genummerde label op elke kaart is de uitvoeringsvolgorde van het script.</p></figcaption></figure>

## Uitvoeringsvolgorde instellen

Met het veld **Execution order** bepaalt u in welke volgorde scripts lopen: lagere nummers lopen eerst. Het veld blijft ook in de Nederlandse interface Engels gelabeld.

1. Open het script in de editor.
2. Vul in het veld **Execution order** een heel getal vanaf 0 in. Laat het veld leeg om 0 te behouden.
3. Sla het script op. Letters, decimalen en negatieve getallen worden met een foutmelding bij het veld geweigerd en er wordt niets opgeslagen.

Als u de uitvoeringsvolgorde wijzigt en daarna een versie activeert, slaat DocBits eerst het script op en activeert de versie pas als dat opslaan is gelukt.

<figure><img src="../../../../../.gitbook/assets/core2170-script-execution-order-editor-nl.png" alt="Scripteditor met het veld Execution order rechts van de keuze van het uitvoeringsmoment"><figcaption><p>De uitvoeringsvolgorde in de scripteditor.</p></figcaption></figure>

De beschikbare acties hangen af van uw rechten. Test bedoelde wijzigingen met representatieve documenten voordat u ze in een echte workflow gebruikt.
