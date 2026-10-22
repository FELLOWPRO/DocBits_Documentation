# Test: import en verwerking van meerdere e-mails

## Wat wordt getest?

Deze tests zorgen ervoor dat ons e-mailimportsysteem correct werkt. De belangrijkste doelstellingen zijn:

1. **E-mails verzenden** met bijlagen.
2. **E-mails ontvangen en verplaatsen** naar specifieke mappen.
3. **Controleer of e-mails gelezen of ongelezen zijn.**
4. **E-mails importeren in ons systeem.**
5. **Opschonen** door e-mails en geïmporteerde documenten achteraf te verwijderen.

## Benodigde stappen

1. **Setup:**
   * **Omgevingsinstellingen ophalen:** Laad de details en inloggegevens van de e-mailserver uit omgevingsvariabelen.
   * **E-mailwachtwoord coderen:** Codeer het e-mailwachtwoord veilig.
2. **E-mails verzenden en beheren:**
   * **E-mails verzenden:** Gebruik een SMTP-functie om e-mails met specifieke onderwerpen en bijlagen te verzenden.
   * **E-mails verplaatsen:** Gebruik de functies IMAP om e-mails naar de doelmap te verplaatsen.
   * **Lijstmappen:** Controleer of de doelmap bestaat.
   * **E-mails verwijderen:** Ruim e-mails op door ze uit mappen te verwijderen.
   * **E-mailstatus controleren:** Controleer of e-mails zijn gemarkeerd als ongelezen of gelezen.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verbinding controleren:** Controleer de verbinding met de e-mailserver en verkrijg de verbinding ID.
    * **Inlogtest:** Bevestig dat inloggen met opgeslagen inloggegevens werkt.
    * **Mapcontrole:** Zorg ervoor dat de doelmap op de e-mailserver bestaat.

    **Email Operations:**

    * **Test-e-mails verzenden:** Stuur drie e-mails met unieke onderwerpen.
    * **E-mail-ID's ophalen:** Haal de ID's van de verzonden e-mails op uit de inbox.
    * **E-mails verplaatsen:** Verplaats deze e-mails van de inbox naar de doelmap.
    * **E-mailstatus controleren:** Zorg ervoor dat de e-mails in de doelmap als ongelezen zijn gemarkeerd.

    **Email Importing:**

    * **E-mails ophalen:** Importeer e-mails uit de doelmap in ons systeem.
    * **Controleer geïmporteerde e-mails:** Zorg ervoor dat de geïmporteerde e-mails correct worden opgehaald en geregistreerd.

    **Log Verification:**

    * **Importlogboeken controleren:** Controleer of de onderwerpen van de verzonden e-mails zijn vastgelegd in de importlogboeken.

    **Cleanup:**

    * **Geïmporteerde documenten verwijderen:** Verwijder de documenten die uit de e-mails zijn geïmporteerd.
    * **E-mails verwijderen:** Ruim op door de verzonden en verplaatste e-mails uit de mappen te verwijderen.

### Gedetailleerde uitleg van elke test

* **Installatie en initialisatie:**
  * **Initialiseer gedeelde gegevens:** Bereid gedeelde gegevens voor op tests.
* **E-mailverbindingstests:**
  * **Get Connection ID:** Controleer of we verbinding kunnen maken met de e-mailserver en een ID krijgen voor de verbinding.
  * **Inlogverificatie:** Zorg ervoor dat het inloggen op de e-mailserver correct werkt.
* **Mapverificatietests:**
  * **Controleer doelmap:** Zorg ervoor dat de doelmap op de e-mailserver bestaat.
  * **Mappenlijst verifiëren:** Zorg ervoor dat de lijst met mappen op de server overeenkomt met onze verwachtingen.
* **E-mail verzenden en ID Ophalen:**
  * **E-mails verzenden:** Verzend drie test-e-mails met specifieke onderwerpen en bijlagen.
  * **E-mail-ID's ophalen:** Haal de unieke ID's van deze verzonden e-mails op uit de inbox.
* **E-mail verplaatsen en statuscontrole:**
  * **E-mails naar map verplaatsen:** Verplaats de test-e-mails van de inbox naar de doelmap.
  * **Ongelezen status controleren:** Zorg ervoor dat de e-mails na het verplaatsen als ongelezen worden gemarkeerd.
* **E-mail ophalen en antwoordvalidatie:**
  * **E-mails ophalen uit map:** Importeer de e-mails uit de doelmap in ons systeem.
  * **Opgehaalde e-mails valideren:** Bevestig dat de opgehaalde e-mails overeenkomen met de verzonden e-mails.
* **Logboekverificatie importeren:**
  * **Importlogboek ophalen:** Haal het logbestand van geïmporteerde e-mails op.
  * **Controleer e-mailonderwerpen in logboek:** Zorg ervoor dat de onderwerpen van de test-e-mails aanwezig zijn in het importlogboek.
* **Cleanup:**
  * **Geïmporteerde documenten verwijderen:** Verwijder de documenten die uit de e-mails zijn geïmporteerd.
  * **E-mails verwijderen:** Verwijder de test-e-mails uit de inbox en de doelmap om alles schoon te houden.

\\
