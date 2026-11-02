# Test: e-mailimport en -verwerking

## Doel

Deze tests zorgen ervoor dat ons systeem het importeren van e-mail correct kan verwerken. Dit omvat het verzenden van e-mails, het ontvangen en verplaatsen ervan naar specifieke mappen, het controleren of ze gelezen of ongelezen zijn, het importeren ervan in het systeem en het achteraf opruimen.

## Teststappen

1. **Setup:**
   * **Omgevingsinstellingen ophalen:** Laad noodzakelijke details zoals e-mailserverinformatie en inloggegevens uit omgevingsvariabelen.
   * **E-mailwachtwoord coderen:** Codeer het e-mailwachtwoord veilig voor veilig gebruik.
2. **E-mail verzenden en beheren:**
   * **Een e-mail verzenden:** Gebruik de functie SMTP om een e-mail met een specifiek onderwerp en bijlage te verzenden.
   * **Verplaats de e-mail:** Gebruik de functies IMAP om de e-mail naar een doelmap te verplaatsen.
   * **Lijstmappen:** Zorg ervoor dat de doelmap bestaat.
   * **Verwijder de e-mail:** Ruim op door de e-mail uit de map te verwijderen.
   * **E-mailstatus controleren:** Controleer of de e-mail is gemarkeerd als gelezen of ongelezen.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verbinding controleren:** Controleer de verbinding met de e-mailserver en verkrijg de verbinding ID.
    * **Inlogtest:** Bevestig dat inloggen met opgeslagen inloggegevens werkt.
    * **Mapcontrole:** Zorg ervoor dat de doelmap op de e-mailserver bestaat.

    **Email Operations:**

    * **Verstuur een test-e-mail:** Stuur een e-mail met een specifiek onderwerp.
    * **E-mail ophalen ID:** Haal de ID van de verzonden e-mail op uit de inbox.
    * **Verplaats de e-mail:** Verplaats de e-mail van de inbox naar de doelmap.
    * **E-mailstatus controleren:** Zorg ervoor dat de e-mail in de doelmap als ongelezen is gemarkeerd.

    **Email Importing:**

    * **Haal de e-mail op:** Importeer de e-mail uit de doelmap in ons systeem.
    * **Controleer geïmporteerde e-mail:** Zorg ervoor dat de geïmporteerde e-mail correct wordt opgehaald en geregistreerd.

    **Log Verification:**

    * **Controleer importlogboek:** Controleer of het onderwerp van de verzonden e-mail is vastgelegd in het importlogboek.

    **Cleanup:**

    * **Geïmporteerd document verwijderen:** Verwijder het document dat uit de e-mail is geïmporteerd.
    * **Verwijder de e-mail:** Verwijder de verzonden en verplaatste e-mail uit de mappen om alles schoon te houden.

## Gedetailleerde uitleg van elke test

* **Installatie en initialisatie:**
  * **Initialiseer gedeelde gegevens:** Bereid gedeelde gegevens voor op tests.
* **E-mailverbindingstests:**
  * **Get Connection ID:** Controleer of we verbinding kunnen maken met de e-mailserver en een ID krijgen voor de verbinding.
  * **Inlogverificatie:** Zorg ervoor dat het inloggen op de e-mailserver correct werkt.
* **Mapverificatietests:**
  * **Controleer doelmap:** Zorg ervoor dat de doelmap op de e-mailserver bestaat.
  * **Mappenlijst verifiëren:** Zorg ervoor dat de lijst met mappen op de server overeenkomt met onze verwachtingen.
* **E-mail verzenden en ID Ophalen:**
  * **Een e-mail verzenden:** Stuur een test-e-mail met een specifiek onderwerp en bijlage.
  * **E-mail ontvangen ID:** Haal de unieke ID van deze verzonden e-mail op uit de inbox.
* **E-mail verplaatsen en statuscontrole:**
  * **E-mail naar map verplaatsen:** Verplaats de test-e-mail van de inbox naar de doelmap.
  * **Ongelezen status controleren:** Zorg ervoor dat de e-mail na verplaatsing als ongelezen wordt gemarkeerd.
* **E-mail ophalen en antwoordvalidatie:**
  * **E-mail ophalen uit map:** Importeer de e-mail uit de doelmap in ons systeem.
  * **Opgehaalde e-mail valideren:** Bevestig dat de opgehaalde e-mail aanwezig is in het antwoord.
* **Logboekverificatie importeren:**
  * **Importlogboek ophalen:** Haal het logbestand van geïmporteerde e-mails op.
  * **Controleer e-mailonderwerp in logboek:** Zorg ervoor dat het onderwerp van de test-e-mail aanwezig is in het importlogboek.
* **Cleanup:**
  * **Geïmporteerd document verwijderen:** Verwijder het document dat uit de e-mail is geïmporteerd.
  * **Verwijder de e-mail:** Verwijder de test-e-mail uit de inbox en de doelmap om alles schoon te houden.

\\
