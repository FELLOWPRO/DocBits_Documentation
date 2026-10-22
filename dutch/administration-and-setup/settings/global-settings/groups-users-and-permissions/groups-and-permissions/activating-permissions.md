# Machtigingen activeren

{% embed url="https://youtu.be/xE4RQnbOMug" %}
DocBits Groups & Permissions Tutorial: Set User Roles, Access Rights & Secure Your Workspace
{% endembed %}

Het in- of uitschakelen van het machtigingssysteem met de schakelaar heeft verschillende effecten op de functionaliteit in DocBits.

## **Het machtigingssysteem inschakelen:**

<figure><img src="../../../../../.gitbook/assets/prior-u007-nl.png" alt="Een groep selecteren om de rechten te bekijken."><figcaption><p>Een groep selecteren om de rechten te bekijken.</p></figcaption></figure>

* Wanneer het machtigingssysteem is ingeschakeld, worden de toegangsrechten voor gebruikers en groepen toegepast.
* Gebruikers krijgen alleen toegang tot de bronnen waarvoor ze expliciet zijn geautoriseerd op basis van de toegewezen machtigingen.
* Beheerders kunnen de machtigingen voor individuele gebruikers en groepen beheren en ervoor zorgen dat alleen geautoriseerde personen de gegevens kunnen bekijken of bewerken.

<figure><img src="../../../../../.gitbook/assets/prior-u004-nl.png" alt="Rechtenmatrix per documenttype en actie. De toegangsniveaus Owner, Everyone en No Access blijven Engelstalig."><figcaption><p>Rechtenmatrix per documenttype en actie. De toegangsniveaus Owner, Everyone en No Access blijven Engelstalig.</p></figcaption></figure>

## Only Assigned Documents

<figure><img src="../../../../../.gitbook/assets/prior-u008-nl.png" alt="Toegangsniveaus per actie in de rechtenmatrix. De toegangsniveaus Owner, Everyone en No Access blijven Engelstalig."><figcaption><p>Toegangsniveaus per actie in de rechtenmatrix. De toegangsniveaus Owner, Everyone en No Access blijven Engelstalig.</p></figcaption></figure>

De schakelaar **Alleen toegewezen documenten** bepaalt de zichtbaarheid van documenten voor gebruikers op basis van hun groepstoewijzingen. Wanneer de schakelaar aan staat, kunnen gebruikers alleen documenten zien die specifiek aan hen of aan een groep waartoe zij behoren zijn toegewezen. Wanneer de schakelaar uit staat, kunnen gebruikers met de juiste weergavemachtiging alle documenten zien, ongeacht de toewijzing.

#### Functionaliteit

* **Uit (standaard)**:
  * Wanneer de schakelaar uit staat, kunnen gebruikers die deel uitmaken van een groep alle documenten bekijken als zij de juiste weergavemachtiging hebben. De toewijzing van documenten heeft geen invloed op de zichtbaarheid.
* **Aan**:
  * Wanneer de schakelaar aan staat, kunnen gebruikers alleen documenten bekijken die expliciet aan hen of aan een groep waarvan zij deel uitmaken zijn toegewezen. Dit dwingt een strengere documentzichtbaarheid af op basis van groepstoewijzingen.

#### Voorbeeldscenario

1. **Standaard (uit)**:
   * Een gebruiker die deel uitmaakt van de groep "Sales" kan alle documenten in het systeem zien die hij of zij mag bekijken, ook als die documenten niet aan hem of haar zijn toegewezen.
2. **Ingeschakeld (aan)**:
   * Een gebruiker in de groep "Sales" kan alleen documenten bekijken die aan hem of haar of aan de groep "Sales" zijn toegewezen, waardoor de toegang tot documenten buiten de eigen toewijzingen wordt beperkt.

## Het machtigingssysteem uitschakelen:

<figure><img src="../../../../../.gitbook/assets/prior-u009-nl.png" alt="Optie om rechtenbeheer te activeren."><figcaption><p>Optie om rechtenbeheer te activeren.</p></figcaption></figure>

* Wanneer het machtigingssysteem is uitgeschakeld, worden alle toegangsrechten verwijderd en hebben gebruikers doorgaans onbeperkte toegang tot alle bronnen.
* Dit kan nuttig zijn wanneer open samenwerking tijdelijk vereist is zonder de beperkingen van toegangscontrole.
* Er kan echter een verhoogd risico zijn op gegevenslekken of ongeautoriseerde toegang, aangezien gebruikers mogelijk toegang hebben tot gevoelige informatie waarvoor ze niet zijn geautoriseerd.

Het in- of uitschakelen van het machtigingssysteem is een belangrijke beslissing op basis van de beveiligingseisen en de manier waarop de organisatie opereert. In omgevingen waar privacy en toegangscontrole cruciaal zijn, is het gebruikelijk om het machtigingssysteem ingeschakeld te laten om de integriteit en vertrouwelijkheid van gegevens te waarborgen. In andere gevallen kan het tijdelijk noodzakelijk zijn om het machtigingssysteem uit te schakelen om samenwerking te vergemakkelijken, maar dit moet met voorzichtigheid worden gedaan om mogelijke beveiligingsrisico's te minimaliseren.

De huidige interface gebruikt een rechtenmatrix per documenttype en actie. Sommige toegangsniveaus kunnen Engelstalig blijven. Instructies voor de oude schakelaar Only Assigned Documents gelden alleen voor versies die deze aanbieden.
