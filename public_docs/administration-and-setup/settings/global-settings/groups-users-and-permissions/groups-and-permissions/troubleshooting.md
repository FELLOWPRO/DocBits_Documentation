# Problemen met toegangscontrole en machtigingen oplossen

Als gebruikers onverwachte toegangsbeperkingen ervaren, zoals ontbrekende documenten, onvermogen om velden te bewerken of geweigerde acties, gebruik dan de volgende checklist om het probleem te identificeren en op te lossen op basis van hoe machtigingen zijn geconfigureerd in DocBits.

### 1. Controleer of toegangscontrole is ingeschakeld

Toegangscontrole-instellingen zijn alleen van toepassing als de functie is **ingeschakeld**.

* Ga naar: `Instellingen` > `Documentverwerking` > `Module`.
* Zorg ervoor dat de schakelaar voor **Toegangscontrole** is ingeschakeld.
* Als deze is uitgeschakeld, hebben alle gebruikers meestal onbeperkte toegang, ongeacht groeps- of veldmachtigingen.

### 2. Controleer groepstoewijzingen

Zorg ervoor dat de gebruiker correct is toegewezen aan de juiste groep(en):

* Ga naar: `Instellingen` > `Algemene instellingen` > `Groepen, gebruikers en machtigingen`.
* Selecteer **Groepen en machtigingen**.
* Bevestig dat de gebruiker wordt vermeld onder de verwachte groep.
* Als de groep specifieke toegangscontrole gebruikt, zal een ontbrekende groepstoewijzing de toegang tot documenten en acties blokkeren.

### 3. Bekijk groepstoegangsmachtigingen

Toegang wordt verleend per documenttype en per actie:

* Controleer in het scherm **Toegangscontrole** voor de groep het documenttype (bijv. Factuur, Inkooporder).
* Valideer machtigingen zoals:
  * **Lijst**, **Weergave**, **Bewerken**, **Verwijderen**, **Massaal bijwerken**
  * **Goedkeuringsniveaus** (1e, 2e), **Document ontgrendelen**
* Zorg ervoor dat het toegangsniveau niet beperkt is tot **Eigenaar** of **Beheerder** tenzij passend.

### 4. Bevestig veldniveau-machtigingen

Toegang kan ook worden beperkt op veldniveau, wat bewerken of zichtbaarheid kan blokkeren:

* Ga naar de toegangscontroleconfiguratie van de groep, navigeer naar het documenttype en controleer de instellingen op veldniveau.
* Bevestig of velden zijn ingesteld op:
  * **Lezen/Schrijven**, **Alleen lezen**, **Eigenaar schrijven**, **Geen**
* Pas indien nodig aan op basis van de rol van de gebruiker.

### 5. Controleer de instelling "Alleen toegewezen documenten"

Deze wereldwijde instelling beperkt de zichtbaarheid van documenten:

* Ga naar: `Instellingen` > `Algemene instellingen` > `Groepen, gebruikers en machtigingen`.
* Als **Alleen toegewezen documenten** is **ingeschakeld**, kunnen gebruikers alleen documenten zien die expliciet aan hen of hun groep zijn toegewezen.
* Als gebruikers verwachte documenten niet kunnen zien:
  * Controleer documenttoewijzingen.
  * Schakel de instelling tijdelijk uit om te testen of dit de oorzaak is.

### 6. Test met een bekende werkende gebruiker of groep

Om het probleem te isoleren:

* Log in met een gebruiker van een groep met bevestigde toegang.
* Vergelijk de zichtbaarheid van documenten en beschikbare acties.
* Dit helpt te bepalen of het probleem specifiek is voor de gebruiker, de groep of het hele systeem.

### 7. Controleer documenttoewijzingen opnieuw

Als "Alleen toegewezen documenten" is **ingeschakeld**, zorg ervoor dat:

* Het document is toegewezen aan de gebruiker of een van hun groepen.
* Gebruik de toewijzingsbedieningen in de detailweergave van het document om toewijzingen te maken of te controleren.

### 8. Herstel of herconfigureer machtigingen

Als machtigingen recentelijk zijn gewijzigd of gebruikers zijn verplaatst tussen groepen:

* Bevestig dat de instellingen voor toegangscontrole de nieuwe groepsconfiguraties weerspiegelen.
* Pas veld- en documentmachtigingen aan indien nodig.
* Als u twijfelt, maak dan een testgroep met brede machtigingen en test de toegangsfunctie voordat u wijzigingen aanbrengt in live groepen.
