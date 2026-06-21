# Importeren

## Overzicht

In de instellingen voor **Importeren** kun je documentspecifieke opties voor de import configureren, of automatische imports via FTP of e-mail instellen. Deze pagina geeft een gedetailleerd overzicht van alle beschikbare instellingen.

## Hoe te openen

1.  Navigeer naar **Instellingen** -> **Documentverwerking** -> **Importeren**

    <figure><img src="../../../.gitbook/assets/ftp_0_es.png" alt=""><figcaption></figcaption></figure>

## **Importbeperking voor documentpagina's**

* **Beperken tot pagina's**: Met deze instelling kun je de verwerking beperken tot een bepaald aantal pagina's per document. De standaardwaarde is **60 pagina's**, wat betekent dat documenten die deze limiet overschrijden worden ingekort tot **60 pagina's**, en alle **resterende pagina's worden weggegooid.**
* **Betalingstermijn in dagen**: Definieert de standaardbetalingstermijn (in dagen) die op documenten kan worden toegepast.
* **Datumpatroon**: Stelt het patroon in voor hoe datums binnen geïmporteerde documenten herkend en geformatteerd moeten worden.

<figure><img src="../../../.gitbook/assets/document_settins_1_es.png" alt=""><figcaption></figcaption></figure>

## **FTP-import**

### Vereisten

Om FTP te gebruiken voor het automatisch importeren van gegevens, zorg ervoor dat aan de volgende vereisten wordt voldaan:

* Correct geconfigureerde, Linux-compatibele FTP-server
* FTP-hostnaam, gebruikersnaam en wachtwoord
* Een speciale importmap

### Nieuwe verbinding toevoegen

1.  Om een nieuwe verbinding toe te voegen, klik op de knop **Toevoegen** in de FTP-sectie.

    <figure><img src="../../../.gitbook/assets/ftp_7_es.png" alt=""><figcaption></figcaption></figure>
2.  Voer je FTP-gegevens in de daarvoor bestemde velden in. Het veld API-sleutel wordt automatisch ingevuld.

    * **Type:** Specificeert het te gebruiken FTP-protocol. Je kunt kiezen tussen **FTP**, **FTPS** of **SFTP**.
    * **Poort:** Specificeert het poortnummer dat gebruikt moet worden voor het geselecteerde FTP-protocol.
    * **Servernaam (vereist):** Het serveradres waarvan de documenten worden opgehaald.
    * **Gebruikersnaam (vereist):** De inlognaam die wordt gebruikt om toegang te krijgen tot de FTP-server.
    * **Wachtwoord (vereist):** Het wachtwoord dat bij de gebruikersnaam hoort om toegang te krijgen tot de FTP-server.
    * **Patronen voor overeenkomst van bestandsnaam:** Om te specificeren welke bestanden geïmporteerd moeten worden op basis van hun naam.
    * **Suborganisaties:** Selecteer op welke suborganisatie de FTP-import van toepassing moet zijn.
    * **API-sleutel (vereist):** Dit veld wordt automatisch ingevuld op basis van de organisatie waarmee je bent ingelogd.
    * **Hoofdmap:** Specificeert de map op de FTP-server waaruit de bestanden worden geïmporteerd.
    * **Importmap:** Hiermee kun je een submap binnen de hoofdmap specificeren waaruit de bestanden worden geïmporteerd.
    * **Archiveren na importeren:** Hiermee kun je bestanden archiveren na de import. Eenmaal geactiveerd, kun je de map specificeren waarheen de bestanden na een succesvolle import moeten worden verplaatst.
    * **Bestanden uit submappen opnemen:** Wanneer ingeschakeld, wordt ook gezocht naar bestanden in submappen binnen de hoofdmap.

    <figure><img src="../../../.gitbook/assets/ftp_4_es.png" alt=""><figcaption></figcaption></figure>
3. Zodra je alle benodigde gegevens van je FTP hebt ingevoerd, klik op **Opslaan**.
4. Nadat je je verbinding hebt opgeslagen, kun je deze activeren door op de drie puntjes in de kolom **Actie** van je verbinding te klikken en vervolgens **Activeren** te selecteren.

### Acties voor FTP

Je kunt op de drie puntjes in de kolom **Actie** klikken om toegang te krijgen tot de volgende opties voor je verbinding:

<figure><img src="../../../.gitbook/assets/ftp_5_es.png" alt="" width="184"><figcaption></figcaption></figure>

* **Verbinding testen:** Test de verbinding met je FTP-server.
* **Verbindingslogboeken:** Opent de logboeken van je FTP-verbinding, inclusief foutmeldingen als er problemen optreden.
* **Activeren/Deactiveren:** Activeert/deactiveert je verbinding.
* **Bewerken:** Hiermee kun je wijzigingen aanbrengen in je verbinding.
* **Verwijderen:** Verwijdert je verbinding.

## **E-mailimport**

Je kunt een e-mailimport instellen die automatisch documenten uit je inbox importeert zodra ze binnenkomen. Je kunt ervoor kiezen om een IMAP-verbinding of een OAuth-verbinding in te stellen.

<mark style="color:red;">**Opmerking**</mark>: Alleen documenten met de volgende bestandstypen worden geïmporteerd:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

### Nieuwe IMAP-verbinding toevoegen

1.  Om een nieuwe IMAP-verbinding toe te voegen, klik op de knop **Toevoegen** in de sectie **E-mailimport**.

    <figure><img src="../../../.gitbook/assets/email_1_es.png" alt=""><figcaption></figcaption></figure>
2. Selecteer IMAP als het protocol.
3. Voer je e-mailgegevens in de daarvoor bestemde velden in. Het veld API-sleutel wordt automatisch ingevuld.
   * **Versleuteling:** Selecteer het te gebruiken type versleuteling — ofwel **SSL** of **TLS**.
   * **Servernaam:** Het adres van de e-mailserver.
   * **Gebruikersnaam:** De identificatie die wordt gebruikt voor je e-mailimportconfiguratie in DocBits.
   * **E-mail:** Het e-mailadres dat wordt gebruikt om documenten in het systeem te importeren.
   * **Wachtwoord:** Het wachtwoord dat bij het opgegeven e-mailadres hoort.
   * **Suborganisaties:** Selecteer de suborganisatie waarop de e-mailimport van toepassing moet zijn.
   * **API-sleutel:** Dit veld wordt automatisch ingevuld op basis van de organisatie waarmee je bent ingelogd.
   * **Stuur importfoutmelding naar dit e-mailadres:** Specificeer een e-mailadres om foutmeldingen te ontvangen als er iets misgaat tijdens het importproces.
   * **Poort:** Specificeert het poortnummer dat gebruikt moet worden voor de geselecteerde e-mailimportconfiguratie.
   * **Map:** Selecteer een map waaruit de documenten worden geïmporteerd.\
     <mark style="color:red;">**Opmerking**</mark>: De optie **Map** wordt pas beschikbaar nadat je met succes een IMAP-verbinding hebt aangemaakt. Om een map toe te voegen na de creatie, klik op de drie puntjes in de kolom **Actie** en selecteer vervolgens **Bewerken**. De optie zou nu beschikbaar moeten zijn.
   * **E-mails naar een andere map verplaatsen:** Wanneer ingeschakeld, kun je een map specificeren waarheen de e-mails na een succesvolle import worden verplaatst.\
     <mark style="color:red;">**Opmerking**</mark>: De optie **E-mails naar een andere map verplaatsen** wordt pas beschikbaar nadat je met succes een IMAP-verbinding hebt aangemaakt. Om deze instelling te activeren, klik op de drie puntjes in de kolom **Actie** en selecteer vervolgens **Bewerken**. De optie zou nu beschikbaar moeten zijn.
   * **Bijlagen samenvoegen:** Combineert meerdere bijgevoegde documenten tot één enkel document.
   * **E-mail naar afzender sturen na import:** Stuurt een bevestigingsmail naar de oorspronkelijke afzender nadat de import is voltooid. Eenmaal geactiveerd, kun je het onderwerp en de tekst van de e-mail specificeren.
   * **Import van dubbele bestandsnamen blokkeren:** Voorkomt de import als er al een document met dezelfde naam bestaat.
4. Nadat je je verbinding hebt opgeslagen, kun je deze activeren door op de drie puntjes in de kolom **Actie** van je verbinding te klikken en vervolgens **Activeren** te selecteren.

### Acties voor IMAP

Je kunt op de drie puntjes in de kolom **Actie** klikken om toegang te krijgen tot de volgende opties voor je verbinding:

<figure><img src="../../../.gitbook/assets/email_7_es.png" alt="" width="190"><figcaption></figcaption></figure>

* **Verbinding testen:** Test de verbinding met je IMAP-client.
* **Verbindingslogboeken:** Opent de logboeken van je e-mailverbinding, inclusief eventuele foutmeldingen die tijdens het proces optreden.
* **Importlogboek:** Opent de logboeken van eerdere imports voor de betreffende verbinding, inclusief eventuele foutmeldingen die tijdens het proces zijn opgetreden.
* **Activeren/Deactiveren:** Activeert/deactiveert je verbinding.
* **Bewerken:** Hiermee kun je wijzigingen aanbrengen in je verbinding.
* **Verwijderen:** Verwijdert je verbinding.

### Nieuwe OAuth Office365-verbinding toevoegen

1.  Om een nieuwe OAuth Office365-verbinding toe te voegen, klik op de knop **Toevoegen** in de sectie **E-mailimport**.

    <figure><img src="../../../.gitbook/assets/email_1_es.png" alt=""><figcaption></figcaption></figure>
2.  Selecteer **OAuth Office365** als het protocol en klik vervolgens op **Authenticeren**.

    <figure><img src="../../../.gitbook/assets/email_3_es.png" alt=""><figcaption></figcaption></figure>
3.  Je wordt doorgestuurd naar een Microsoft-pagina waar je wordt gevraagd een code in te voeren. Om deze code op te halen, ga je terug naar DocBits—de code wordt daar weergegeven, zoals hieronder getoond. Kopieer de code en voer deze in op de Microsoft-pagina. Daarna wordt je gevraagd je Microsoft-gegevens in te voeren.

    <figure><img src="../../../.gitbook/assets/email_4_es.png" alt=""><figcaption></figcaption></figure>
4. Volg de stappen op de Microsoft-pagina. Zodra je klaar bent, ga terug naar DocBits en klik op **Authenticatie voltooien**.
5.  Je kunt nu de volgende instellingen configureren:

    * **Suborganisaties:** Selecteer de suborganisatie waarop de e-mailimport van toepassing moet zijn.
    * **Map gebruiken:** Selecteer een map waaruit de documenten worden geïmporteerd.
    * **Gedeelde mailbox gebruiken:** Specificeer het gedeelde e-mailadres waaruit de documenten geïmporteerd moeten worden.
    * **E-mail naar een andere map verplaatsen:** Specificeer een map waarheen de e-mails na een succesvolle import moeten worden verplaatst.
    * **Stuur importfoutmelding naar dit e-mailadres:** Specificeer een e-mailadres om foutmeldingen te ontvangen als er iets misgaat tijdens het importproces.

    <figure><img src="../../../.gitbook/assets/email_5_es.png" alt=""><figcaption></figcaption></figure>
6. Zodra je het gewenste gedrag hebt geconfigureerd, kun je beginnen met het importeren van e-mails door op **Importeren** te klikken, of je wijzigingen opslaan door op **Opslaan** te klikken.
7. Nadat je je verbinding hebt opgeslagen, kun je deze activeren door op de drie puntjes in de kolom **Actie** van je verbinding te klikken en vervolgens **Activeren** te selecteren.

### Acties voor OAuth Office365

Je kunt op de drie puntjes in de kolom **Actie** klikken om toegang te krijgen tot de volgende opties voor je verbinding:

<figure><img src="../../../.gitbook/assets/email_6_es.png" alt="" width="189"><figcaption></figcaption></figure>

* **Verbindingslogboeken:** Opent de logboeken van je e-mailverbinding, inclusief eventuele foutmeldingen die tijdens het proces optreden.
* **Importlogboek:** Opent de logboeken van eerdere imports voor de betreffende verbinding, inclusief eventuele foutmeldingen die tijdens het proces zijn opgetreden.
* **Activeren/Deactiveren:** Activeert/deactiveert je verbinding.
* **Bewerken:** Hiermee kun je wijzigingen aanbrengen in je verbinding.
* **Verwijderen:** Verwijdert je verbinding.

### Importlogboek

Je kunt het importlogboek van alle aangemaakte e-mailverbindingen bekijken, inclusief eventuele foutmeldingen die tijdens het proces zijn opgetreden, door op de knop **Importlogboek** in de rechterbovenhoek van de sectie E-mailimport te klikken.

<figure><img src="../../../.gitbook/assets/email_8_es.png" alt=""><figcaption></figcaption></figure>

Je kunt de logboeken filteren op onderwerp of afzender, kolommen oplopend of aflopend sorteren door op de kolomkoppen te klikken, en kolommen herschikken via slepen en neerzetten.
