# Settings Assistant: inschakelen

De **Settings Assistant** is een chatpaneel in het gedeelte Instellingen. Je stelt een vraag in gewone taal, en de assistent leest de configuratie van je organisatie, geeft antwoord en brengt je rechtstreeks naar de juiste instelling. Hij kan je ook waarschuwen wanneer iets in je configuratie niet meer werkt en, met je bevestiging, een instelling voor je wijzigen.

Hij helpt het meest wanneer je weet **wat** je wilt ("stop met het splitsen van documenten op barcodes") maar niet **waar** de instelling staat, of wanneer je je afvraagt **waarom** iets niet gebeurt ("Why isn't PO matching active?").

<figure><img src="../../../../../.gitbook/assets/settings-assistant-panel-open-nl.png" alt="Het paneel van de Settings Assistant aan de rechterkant van het gedeelte Instellingen, met een begroeting voor de huidige pagina, drie voorbeeldvragen en het vraagveld"><figcaption><p>De Settings Assistant op de pagina Company Information: een begroeting voor de huidige pagina, drie voorbeeldvragen en het vraagveld. Boven de begroeting verschijnt een waarschuwingskaart wanneer een import niet meer werkt (zie <a href="settings-assistant-chat.md#findings-the-assistant-warns-you">Findings</a>).</p></figcaption></figure>

De assistent staat **standaard uit**. Deze pagina laat zien waar je hem inschakelt en hoe je hem opent. Wat je hem kunt vragen en wat hij kan wijzigen, staat op de pagina [Settings Assistant: wat de chat kan doen](settings-assistant-chat.md).

## Wie het kan gebruiken

* De **organisatiebeheerder** schakelt de assistent in of uit voor de hele organisatie.
* Zodra hij aan staat, kan elke beheerder die **Settings** kan openen het paneel voor zichzelf tonen of verbergen.
* Wijzigingen (een aanbeveling toepassen, een importverbinding uitschakelen of verwijderen, een regel aanmaken) zijn beperkt tot **organisatiebeheerders**. Andere gebruikers krijgen de melding *Available to administrators only.*

## Inschakelen

1. Ga naar **Settings → Organization & Access → Company Information**. De paginakop toont **Company Settings**.
2. Open de sectie **Assistants**.
3. Schakel **Enable the settings assistant** in.

<figure><img src="../../../../../.gitbook/assets/settings-assistant-org-switch-nl.png" alt="De sectie Assistants in Company Information met de schakelaars voor de settings assistant, de validation assistant en de explainer voice-over"><figcaption><p>De sectie Assistants. De settings assistant heeft een eigen schakelaar. De validation assistant en de explainer voice-over zijn afzonderlijke functies.</p></figcaption></figure>

Een korte melding bevestigt **Settings assistant enabled**. De instelling staat standaard uit. Zolang ze uit staat, verschijnen het paneel en de bijbehorende knop nergens.

{% hint style="warning" %}
De **Validation assistant** in dezelfde sectie is een andere functie. Hij legt blokkerende velden in een document uit en kan geen enkele instelling wijzigen. Het omschakelen van een van de twee heeft geen invloed op de andere.
{% endhint %}

## Het paneel openen en sluiten

Op elke pagina van het gedeelte Instellingen vind je naast het zoekveld voor instellingen een kleine **genie-lamp button**. Klik erop om de assistent te **tonen** of te **verbergen**.

<figure><img src="../../../../../.gitbook/assets/settings-assistant-in-company-settings-nl.png" alt="De pagina Company Information in Settings met de instellingennavigatie links, de pagina in het midden en het paneel van de Settings Assistant rechts"><figcaption><p>De assistent staat aan de <strong>rechterkant</strong> van elke instellingenpagina: navigatie links, de pagina in het midden, de assistent ernaast. Hier op <strong>Company Settings → Company Information</strong>. De knop om hem te tonen of te verbergen is het lampicoon naast <strong>Search Settings</strong> bovenaan de navigatie.</p></figcaption></figure>

* Het paneel onthoudt je keuze per gebruiker, dus het blijft open wanneer je terugkomt.
* Op een breed scherm (1280 pixels en meer) staat het naast de pagina. Je kunt aan de rand slepen om de breedte te wijzigen.
* Op een smal scherm opent het als overlay. **Esc** of een klik erbuiten sluit het.
* **New chat** (het spraakballonpictogram in de kop) wist het gesprek. Het gesprek blijft ook bewaard na het opnieuw laden van de pagina, maar niet na het sluiten van het browsertabblad.

## Wat je hierna kunt doen

* Stel je eerste vraag: zie [Settings Assistant: wat de chat kan doen](settings-assistant-chat.md).
* De assistent draait op het AI-niveau **Fast**. Er is geen organisatie-instelling om een ander model te kiezen.

## Probleemoplossing

| Probleem | Oorzaak en oplossing |
| --- | --- |
| Er is geen genie-lamp button in het gedeelte Instellingen | De schakelaar van de organisatie staat uit. Een organisatiebeheerder schakelt hem in onder **Company Information → Assistants** |
| De sectie **Assistants** ontbreekt in Company Information | Alleen organisatiebeheerders zien haar |
| Het paneel zegt **The assistant is being set up** | De functie is nog niet beschikbaar in je omgeving |
| Het paneel is er, maar de antwoorden zeggen *Available to administrators only.* | Je account is geen organisatiebeheerder |

## Gerelateerde pagina's

* [Settings Assistant: wat de chat kan doen](settings-assistant-chat.md)
* [Bedrijfsvoorkeuren](../company-preferences.md)
