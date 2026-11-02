# Taken en meldingen

### Overzicht

De instelling **Taken en meldingen** schakelt het ingebouwde taakbeheer van DocBits in. Wanneer deze is ingeschakeld, kunnen teamleden taken aanmaken, elkaar documenten toewijzen (bijvoorbeeld voor validatie, correctie of goedkeuring) en daarover meldingen ontvangen.

Deze instelling is **standaard uitgeschakeld**. Wanneer deze is ingeschakeld, verschijnen eronder vier extra opties:

* **Aantal taken op het dashboard**: toont op het Dashboard welke documenten openstaande taken hebben.
* **Schakel het filter "Alles" in voor niet-beheerders**: laat gebruikers die geen beheerder zijn alle taken zien.
* **Taken verwijderen door niet-beheerders**: bepaalt welke taken gebruikers die geen beheerder zijn mogen verwijderen.
* **Taken voltooien door niet-beheerders**: bepaalt welke taken gebruikers die geen beheerder zijn mogen afsluiten.

Beheerders van de organisatie worden door deze opties nooit beperkt.

### Wat doet het?

* **Ingeschakeld**: De functies voor Taken en meldingen worden beschikbaar in DocBits. Gebruikers kunnen taken toewijzen, de status ervan volgen en een melding krijgen wanneer iets hun aandacht vereist.
* **Uitgeschakeld**: Taaktoewijzing en de bijbehorende meldingen worden uitgeschakeld. Uitschakelen schakelt ook **Aantal taken op het dashboard** uit.

### Aantal taken op het dashboard

**Aantal taken op het dashboard** bepaalt of het Dashboard toont welke documenten openstaande taken hebben.

* **Ingeschakeld**: Een document met taken in de status **Open** of **In uitvoering** krijgt een taakpictogram in de lijst op het Dashboard. Wanneer u met de muis over het pictogram gaat, ziet u hoeveel openstaande taken het document heeft, bijvoorbeeld "2 Open taak(en)". Taken die voltooid, afgewezen of verwijderd zijn, worden niet meegeteld.
* **Uitgeschakeld**: Het pictogram wordt verborgen. Taken werken gewoon normaal.

{% hint style="info" %}
**Aantal taken op het dashboard** is afhankelijk van **Taken en meldingen**. Als u Taken en meldingen uitschakelt, wordt het aantal taken op het dashboard ook uitgeschakeld.
{% endhint %}

### Schakel het filter "Alles" in voor niet-beheerders

Het takenoverzicht heeft een filter **Toegewezen aan** met de opties **Alle** en **Aan mij toegewezen**. Beheerders krijgen altijd beide opties.

* **Ingeschakeld**: Ook gebruikers die geen beheerder zijn, kunnen **Alle** kiezen en alle taken van de organisatie zien.
* **Uitgeschakeld** (standaard): Gebruikers die geen beheerder zijn, krijgen alleen **Aan mij toegewezen**, zodat het overzicht de taken toont die aan hen zijn toegewezen.

### Taken verwijderen door niet-beheerders
**Taken verwijderen door niet-beheerders** bepaalt welke taken en meldingen gebruikers die geen beheerder zijn mogen verwijderen. Beheerders kunnen altijd elke taak verwijderen.

| Optie | Gebruikers die geen beheerder zijn, mogen verwijderen |
| --- | --- |
| **Geen** | Geen taken. |
| **Alleen aangemaakte taken** | Taken die ze zelf hebben aangemaakt. |
| **Aangemaakte en toegewezen taken** | Taken die ze zelf hebben aangemaakt, en taken die aan hen of aan een van hun groepen zijn toegewezen. Dit geldt wanneer de optie nooit is gewijzigd. |
| **Alle taken** | Elke taak. |

Gebruikers kunnen de taken die ze zelf hebben aangemaakt altijd verwijderen, behalve met **Geen**. Een taak die aan niemand is toegewezen, kan daarom alleen worden verwijderd door de gebruiker die haar heeft aangemaakt, door beheerders of met **Alle taken**. Een taak zonder vastgelegde maker, bijvoorbeeld een taak die door het systeem is aangemaakt, kan alleen worden verwijderd door de gebruikers aan wie ze is toegewezen (met **Aangemaakte en toegewezen taken**), door beheerders of met **Alle taken**.

{% hint style="warning" %}
Een taak verwijderen haalt deze uit de takenlijst zonder dat er een beslissing is genomen. Als taken alleen via een beslissing mogen worden afgesloten, stel dan **Taken verwijderen door niet-beheerders** in op **Geen** en **Taken voltooien door niet-beheerders** (zie hieronder) op **Alleen voor beheerders**.
{% endhint %}

### Taken voltooien door niet-beheerders
**Taken voltooien door niet-beheerders** bepaalt welke gebruikers die geen beheerder zijn een taak mogen afsluiten, dat wil zeggen op **Klaar** of **Afgewezen** zetten. Beheerders kunnen altijd taken afsluiten, wat hier ook is geselecteerd.

| Optie | Wie een taak mag afsluiten |
| --- | --- |
| **Standaardgedrag** | De instelling voegt geen beperking toe. Gebruikers kunnen de taken afsluiten die aan hen of aan een van hun groepen zijn toegewezen, zoals vóór het bestaan van deze instelling. Dit geldt wanneer de optie nooit is gewijzigd. |
| **Beheerders en toegewezen gebruikers** | Beheerders, en de gebruikers aan wie de taak is toegewezen, direct of via een van hun groepen. Een taak die aan iemand anders of aan niemand is toegewezen, kan niet door andere gebruikers worden afgesloten. DocBits controleert dit ook wanneer een taak via de API wordt gewijzigd. |
| **Alleen voor beheerders** | Alleen beheerders. |

Met **Beheerders en toegewezen gebruikers** of **Alleen voor beheerders** geldt voor een gebruiker die een taak niet mag afsluiten:

* de groene knop **Klaar** op de taakpagina is niet zichtbaar, en de statuslijst daar biedt alleen **Open** en **In uitvoering**;
* de statuscirkel van de taak in het takenpaneel van het document is niet klikbaar. Wanneer u er met de muis over gaat, verschijnt "Je mag deze taak niet als voltooid of afgewezen markeren.";
* **Markeer als voltooid** is voor die taak niet zichtbaar in de takenlijst, en **Markeer als voltooid** voor een selectie is verborgen zolang zo'n taak geselecteerd is;
* de taak kan op het takenbord niet naar de kolom **Klaar** of **Afgewezen** worden gesleept. De kaart keert terug naar haar kolom en dezelfde melding verschijnt.

De instelling beperkt alleen het afsluiten. Gebruikers behouden alle andere rechten die ze eerder hadden: gebruikers aan wie een taak is toegewezen, kunnen die nog steeds bewerken, opslaan, tussen **Open** en **In uitvoering** verplaatsen en opnieuw openen nadat ze voltooid is. Gebruikers aan wie een taak niet is toegewezen, konden de status ervan eerder niet wijzigen, en kunnen dat nog steeds niet.

Voor documenttypen waarvoor **Goedkeuringsgeschiedenis** is ingeschakeld, voltooit **Goedkeuren** nog steeds openstaande taken van het document, wat hier ook is geselecteerd: de taken die aan de goedkeurder of aan een van zijn groepen zijn toegewezen, en de taken die aan niemand zijn toegewezen. Als de goedkeurder een beheerder is, worden alle openstaande taken van het document voltooid.

#### Taken op documenten die terug naar validatie worden gestuurd

Omdat gebruikers onder **Beheerders en toegewezen gebruikers** of **Alleen voor beheerders** hun eigen taken niet kunnen afsluiten, ruimt DocBits de openstaande taken van een document zelf op wanneer een document dat op goedkeuring wacht, terug naar validatie wordt gestuurd:

* **Workflow opnieuw starten** op het goedkeuringsscherm: alle openstaande taken van het document worden afgewezen.
* **Afwijzen en corrigeren**: alle openstaande taken van het document worden afgewezen.
* **Goedkeuren en corrigeren**: de taken die **Goedkeuren** zou voltooien (zie hierboven) worden voltooid, alleen voor documenttypen waarvoor **Goedkeuringsgeschiedenis** is ingeschakeld. Alle overige openstaande taken worden afgewezen.

De openstaande taken worden opgeruimd voordat het document terugkeert naar validatie. Workflows die bij de statuswijziging worden uitgevoerd, kunnen daarna nieuwe taken aanmaken voor alles wat nog aandacht nodig heeft.

Met **Standaardgedrag** blijven openstaande taken open wanneer een document wordt teruggestuurd, zoals voorheen.

### Voordelen

* **Duidelijke verantwoordelijkheden**: Documenten kunnen aan de juiste persoon worden toegewezen in plaats van te vertrouwen op e-mail.
* **Niets wordt vergeten**: Meldingen herinneren gebruikers aan documenten die hun actie vereisen.
* **Openstaand werk in één oogopslag**: Met Aantal taken op het dashboard toont het Dashboard welke documenten nog openstaande taken hebben.
* **Beslissingen blijven traceerbaar**: Met de opties voor verwijderen en afsluiten verlaten taken de wachtrij alleen via een beslissing of een beheerder.

### Hoe te gebruiken

1. Ga naar **Instellingen**.
2. Selecteer **Documentverwerking**.
3. Selecteer **Module**.
4. Open de sectie **Documenttype**.
5. Zet **Taken en meldingen** aan.
6. (Optioneel) Zet **Aantal taken op het dashboard** aan om het taakpictogram op het Dashboard te tonen.
7. (Optioneel) Zet **Schakel het filter "Alles" in voor niet-beheerders** aan als alle gebruikers alle taken moeten zien.
8. (Optioneel) Kies bij **Taken verwijderen door niet-beheerders** welke taken gebruikers mogen verwijderen.
9. (Optioneel) Kies bij **Taken voltooien door niet-beheerders** wie taken mag afsluiten.

De opties voor verwijderen en afsluiten worden opgeslagen zodra u een waarde kiest.

### Wanneer deze functie gebruiken

* **Teams die documentwerk delen**: Schakel in wanneer meerdere mensen documenten valideren of goedkeuren en werk aan elkaar moeten overdragen.
* **Zicht op werklast**: Schakel ook Aantal taken op het dashboard in wanneer het team op het Dashboard moet zien welke documenten nog openstaande taken hebben.
* **Taken die alleen beheerders of een beslissing mogen afsluiten**: Stel **Taken voltooien door niet-beheerders** in op **Alleen voor beheerders** of **Beheerders en toegewezen gebruikers**, en **Taken verwijderen door niet-beheerders** op **Geen**, wanneer gebruikers geen taken mogen verwijderen die niet echt zijn afgehandeld.
* **Eén-gebruiker- of volledig geautomatiseerde opstellingen**: U kunt deze uitgeschakeld laten als niemand documenten hoeft toe te wijzen of taken hoeft te volgen.
