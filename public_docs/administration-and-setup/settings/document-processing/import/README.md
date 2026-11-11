# Importeren

## Overzicht

U hebt een beheerdersaccount nodig om een verbinding te maken. Gebruik **Import** om geautomatiseerde documentimport te configureren vanaf een FTP/SFTP-server, een gekoppeld postvak of het inkomende DocBits-e-mailadres. Controleer de huidige organisatie en omgeving voordat u verbindingsgegevens invoert.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-nl-20261109.png" alt="Pagina Import-instellingen met het diagram Import Pipeline, de lijst FTP Import met een knop New en de lijst Email Import met een knop New"><figcaption><p>De pagina Import: het alleen-lezen diagram Import Pipeline, de lijst FTP Import en de lijst Email Import, elk met een eigen knop <strong>New</strong>.</p></figcaption></figure>

## Toegang

1. Navigeer naar **Settings** → **Document Processing** → **Import**.
2. Vouw de gewenste sectie uit. **FTP Import** en **Email Import** hebben elk een eigen knop **New**.

## **Document Settings**

De huidige pagina Import bevat **Import Pipeline**, **FTP Import**, **Email Import** en, indien ingeschakeld, **Inbound Emails**. Paginabeperking, standaard betalingsvoorwaarden en datumpatroonvelden zijn geen bedieningselementen in deze Import-weergave.

**Import Pipeline** toont de FTP/SFTP-routeringstopologie, inclusief de bron- en doelregio's. Controleer elk weergegeven advies voordat u een verbinding wijzigt. Het tabblad **Email** van de pipeline toont momenteel een bericht dat de functie binnenkort beschikbaar komt; er wordt geen diagram voor e-mailverwerking weergegeven.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tabel FTP Import met de knop New en kolommen voor type, server, gebruikersnaam, poort, suborganisatie en map"><figcaption><p>Gebruik New in FTP Import om een serververbinding toe te voegen. Bestaande verbindingsregels zijn in dit voorbeeld afgeschermd.</p></figcaption></figure>

### Vereisten

* Een FTP-, FTPS- of SFTP-server die bereikbaar is voor de importdienst.
* Het serveradres, protocol, de poort, gebruikersnaam en het wachtwoord zoals verstrekt door uw beheerder.
* Een importmap en, als archivering nodig is, een goedgekeurde archiveringsmap.

### Nieuwe verbinding toevoegen

1. Klik op **New** in **FTP Import**.
2. Voer de verbindingsinstellingen in. Een nieuw formulier begint met **SFTP** en poort **22**; vervang deze waarden wanneer uw server een ander protocol of een andere poort gebruikt.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Nieuw formulier voor een FTP-verbinding met SFTP, poort 22, mapvelden, retry-instellingen en Save en Cancel"><figcaption><p>Voer de server- en inloggegevens in en controleer daarna de mappen, de routering en de retry-instellingen. De velden voor wachtwoord en API-sleutel zijn afgeschermd; dit voorbeeld is niet opgeslagen.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** en **Password** identificeren en authenticeren de serververbinding.
* **Primary Directory** stelt de basismap in. Met **Import Directory** selecteert u de map die moet worden verwerkt; mapselectie wordt beschikbaar nadat de verbinding is opgeslagen.
* **Document Type** en **Sub-Organizations** regelen de toewijzing. **File name matching patterns** beperkt welke bestandsnamen in aanmerking komen.
* **Archive after Import** maakt het mogelijk verwerkte bestanden naar de opgegeven archiveringsmap te verplaatsen. **Include Subfolder Files** breidt de verwerking uit naar submappen.
* **Retry interval (min)**, **Retry duration (hours)** en **Notification emails (comma-separated)** regelen het opnieuw proberen en de meldingen. De weergegeven standaardwaarden zijn 60 minuten en 48 uur.
* **API Key** gebruikt de bestaande app-subscription-sleutel van de organisatie. Het oogpictogram toont of verbergt die sleutel; het kopieerpictogram kopieert deze naar het klembord. Deze bedieningselementen maken geen nieuwe sleutel aan. Houd de sleutel vertrouwelijk; neem deze niet op in schermafbeeldingen of supportberichten.

Gebruik **Cancel** of het sluitpictogram om een formulier voor een nieuwe verbinding te verlaten zonder het op te slaan.

3. Controleer de waarden en klik op **Save** wanneer de verbinding klaar is om te worden aangemaakt.
4. Kies in het menu **Actions** van de opgeslagen rij **Activate** wanneer imports mogen worden uitgevoerd.

### Acties voor FTP

Het menu **Actions** van de opgeslagen verbinding biedt:

* **Test Connection**: de geconfigureerde server benaderen om de verbinding te controleren.
* **Connection Logs**: verbindingspogingen en fouten bekijken.
* **Activate/Deactivate**: automatische verwerking voor deze verbinding inschakelen of stoppen.
* **Edit**: de configuratie wijzigen.
* **Delete**: de verbinding verwijderen.

Testen, activeren, bewerken en verwijderen hebben invloed op een echte verbinding. Controleer de geselecteerde rij en organisatie voordat u deze gebruikt.

## **Email Import**

Een gekoppeld postvak staat los van het inkomende DocBits-e-mailadres dat in de onderstaande handleiding wordt beschreven. Kies de methode die bij uw proces past.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tabel Email Import met New, het pictogram voor het importlogboek en kolommen voor de mailboxconfiguratie"><figcaption><p>Gebruik New voor een postvakverbinding of het logboekpictogram om imports te bekijken. Bestaande verbindingsregels en de informatieve link zijn afgeschermd.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Alleen documenten met de volgende bestandstypen worden geïmporteerd:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Hoe bijlagen worden herkend**

Naast de hierboven genoemde bestandsextensies identificeert DocBits een document ook op basis van de **werkelijke bestandsinhoud** (bestandssignatuur), niet alleen op basis van het inhoudstype dat het verzendende mailsysteem opgeeft. Dit is van belang bij **doorgestuurde** e-mails: tussenliggende mailservers en gateways voorzien een bijlage vaak van een generiek type (`application/octet-stream`) in plaats van bijvoorbeeld `application/pdf` of `application/xml`. DocBits herkent en importeert dergelijke bijlagen toch correct.

* **Doorgestuurde `.eml`**-berichten en Outlook-bijlagen **`winmail.dat`** (TNEF) worden uitgepakt en de documenten daarin worden geïmporteerd.
* **XML-codering:** wanneer een XML-factuur opnieuw wordt gelabeld met een generiek type (`application/octet-stream`), herkent DocBits deze aan de declaratie `<?xml` en tolereert daarbij een voorafgaande bytevolgordemarkering (BOM) in **UTF-8** of **UTF-16** (LE/BE) — momenteel worden alleen deze BOM-coderingen automatisch op basis van de inhoud gedetecteerd. Een bijlage die een `.xml`-bestandsnaam behoudt, wordt ongeacht de codering geïmporteerd.
* **Genegeerd:** inline-afbeeldingen die met een e-mail meekomen (handtekeninglogo's en ingesloten afbeeldingen — PNG, JPG, GIF, BMP) worden stilzwijgend overgeslagen en **niet** als mislukte import geteld.

Als een bijlage niet kan worden geïmporteerd en de optie **“Reply to this email if import can not be done”** is ingeschakeld voor het inkomende adres, wordt het geconfigureerde antwoordadres op de hoogte gesteld.
{% endhint %}

### Nieuwe IMAP-verbinding toevoegen

1. Klik op **New** in **Email Import** en selecteer **IMAP** onder **Protocol**.
2. Voer in **Email Server Setup** de servernaam, poort, encryptie, gebruikersnaam, het e-mailadres en het wachtwoord in. Gebruik de waarden die uw mailprovider vereist; de weergegeven 993 is een poortvoorbeeld, geen ingevulde instelling.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="IMAP Email Server Setup met protocol, server, poort, encryptie, accountgegevens en Next"><figcaption><p>Vul de vereiste server- en accountvelden in voordat u op Next klikt. Het wachtwoordgedeelte is afgeschermd; in dit voorbeeld zijn geen mailboxgegevens verzonden.</p></figcaption></figure>

Het kopieerpictogram naast **Password** kopieert het ingevoerde wachtwoord naar het klembord. Met **Cancel** of het sluitpictogram verlaat u deze wizard voor een nieuwe verbinding zonder op te slaan.

3. Klik op **Next** om **Options** te openen. Kies of u **Merge attached documents** of **Block duplicate filename import** wilt gebruiken. Met **Email Notification** schakelt u een bevestigingsmail na de import in; schakel dit alleen in wanneer dat gedrag bedoeld is.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="Stap IMAP Options met samenvoegen van bijlagen, filteren op dubbele bestandsnamen, e-mailmelding, Back en Next"><figcaption><p>Options scheidt het importgedrag van de e-mailmelding. Beide selectievakjes en de meldingsschakelaar staan uit in dit niet-opgeslagen voorbeeld.</p></figcaption></figure>

4. Klik op **Next** om **Config** te openen. Selecteer de vereiste **Sub-Organizations**, controleer de bestaande **API Key**, stel de ontvanger voor importfouten in en controleer **Document Routing**. Vouw **Advanced Settings** alleen uit wanneer het proces extra opties nodig heeft.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="Stap IMAP Config met organisatie, afgeschermde API Key, foutmeldingen, Document Routing, Advanced Settings en Save"><figcaption><p>Config brengt de organisatietoewijzing, de bestaande sleutel, foutmeldingen en de routering samen. De sleutel is afgeschermd en Save is niet gebruikt.</p></figcaption></figure>

In **Config** toont het oogpictogram de bestaande **API Key** of verbergt deze, en **Copy** kopieert de sleutel naar het klembord. Geen van beide bedieningselementen genereert een nieuwe sleutel.

5. Klik op **Save** wanneer de configuratie klaar is. Gebruik daarna **Activate** in het menu **Actions** van de opgeslagen verbinding om automatische verwerking te starten.

Voor een opgeslagen IMAP-verbinding biedt **Edit** opties voor mappen en voor de verwerking na de import. Selecteer de bronmap en de doelmap voor verplaatste e-mails pas nadat de verbinding is aangemaakt en de beschikbare mappen kunnen worden geladen.

### Acties voor IMAP

Het menu **Actions** van de opgeslagen verbinding biedt **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** en **Delete**. Bij het testen van de verbinding wordt het geconfigureerde postvak benaderd; activering schakelt de verwerking in. Controleer de logboeken voordat u een mislukte import opnieuw probeert.

### Nieuwe OAuth Office365-verbinding toevoegen

1. Klik op **New** in **Email Import** en selecteer **OAuth Office365** onder **Protocol**. Selecteer **OAuth Office365 - Tenant** voor een door een beheerder beheerde tenant-applicatie en volg [O365 Tenant](o365-tenant.md).
2. Controleer **Document Routing** vóór de authenticatie.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="OAuth Office365-configuratie met Document Routing en de knop Authenticate vóór de Microsoft-authenticatie"><figcaption><p>Selecteer de route vóór Authenticate. Deze weergave is van vóór de aanmelding; er is geen Microsoft-authenticatie gestart.</p></figcaption></figure>

3. Klik op **Authenticate** wanneer de postvakverbinding is geautoriseerd. Rond de Microsoft-aanmelding met apparaatcode af met de code die DocBits toont, ga daarna terug en selecteer **Finish Authentication**.
4. Controleer na de authenticatie de opties voor organisatie, map, gedeeld postvak, verplaatsmap en foutmeldingen die voor de verbinding worden aangeboden. Gebruik **Next** om verder te gaan naar **Config** zodra dit beschikbaar is en sla daarna de gewenste instellingen op.
5. Activeer de opgeslagen verbinding wanneer automatische imports moeten worden uitgevoerd. **Import** start, waar dit voor een opgeslagen verbinding beschikbaar is, een daadwerkelijke import; gebruik dit bewust.

### Acties voor OAuth Office365

Het menu **Actions** van de opgeslagen verbinding biedt **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** en **Delete**. Deactivering stopt de automatische verwerking; verwijdering verwijdert de configuratie.

### Import Log

Gebruik het logboekpictogram rechtsboven in **Email Import** om imports over de geconfigureerde postvakverbindingen te bekijken. Gebruik de actie **Import Log** van een opgeslagen rij voor die verbinding. Controleer het onderwerp, de afzender, de status en de beschikbare foutdetails voordat u besluit of u het opnieuw probeert.

## Inbound Emails

De twee onderstaande schermafbeeldingen uit de handleiding tonen het inkomende DocBits-adres en de bijbehorende logboeken. Dit staat los van de postvakverbindingen hierboven.

* Gebruik het kopieerpictogram naast **E-Mail** om het ontvangstadres te kopiëren dat voor de huidige organisatie en omgeving wordt weergegeven.
* **Add** voegt een extra rij met een toegestane afzender toe in het formulier. Kies de afzender en de eventueel bedoelde suborganisatie en gebruik **Save** om de configuratie op te slaan. Alleen een rij toevoegen slaat deze niet op.
* **Logs** opent het logboek voor inkomende e-mail. **Errors** filtert op fouten; **Inbound** en **Outbound** selecteren de berichtrichting.
* Vouw een logregel uit met de chevron om de bijlagedetails te bekijken. Het kopieerpictogram naast de trace-ID kopieert die ID voor probleemoplossing. **Original email** downloadt, waar beschikbaar voor een inkomende rij, het geselecteerde oorspronkelijke bericht als een `.eml`-bestand; de import wordt niet opnieuw geprobeerd.

## Videohandleiding: Inbox en foutopsporing

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/nl.mp4" %}
E-mailinbox en foutopsporing
{% endembed %}

[Bekijken met ondertiteling en hoofdstukken](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/nl.html)

Sommige oorspronkelijke productlabels kunnen in een andere taal staan. Technische veld-ID's blijven behouden.

Bij instellingen en import gebruik ik in dit voorbeeld het inkomende DocBits-adres. Een direct gekoppelde mailbox is een aparte importmethode. Voor deze training werk ik in een eigen demo-organisatie met synthetische facturen. Meldingen blijven uitgeschakeld.

Eerst controleer ik het weergegeven ontvangstadres en de reikwijdte. Het adres hoort precies bij deze organisatie en bij de bijbehorende omgeving. Voor een ander bedrijf of een productieomgeving gebruik ik altijd het adres dat daar daadwerkelijk wordt weergegeven.

Hier beperk ik de inbox tot onze goedgekeurde testafzender. Ik selecteer de toewijzing aan een suborganisatie alleen als deze bij het bedoelde proces hoort. Ik sla de instelling op en open deze opnieuw. De toegestane afzender is behouden; automatische antwoordmails blijven in deze training uitgeschakeld.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Toegestane afzender opgeslagen met meldingen uitgeschakeld"><figcaption><p>Toegestane afzender opgeslagen met meldingen uitgeschakeld</p></figcaption></figure>

Voor deze training is een testbericht rechtstreeks aan de verwerking van inkomende e-mail in DocBits aangeboden. Deze test bevestigt geen externe e-mailbezorging. In het logboek controleer ik het bijbehorende onderwerp, de afzender en de geïmporteerde bijlage. Daarna controleer ik het document dat daadwerkelijk is aangemaakt.

Ik open het bijbehorende document en vergelijk de PDF-bijlage met de factuur in DocBits. Bestandsnaam, factuurnummer, leverancier en bedrag moeten overeenkomen. Een geslaagde import zegt niets over een goedkeuring of een ERP-boeking.

Een tweede gecontroleerde test komt van een niet-goedgekeurde afzender. In het logboek zoek ik gericht naar deze inkomende e-mail en activeer ik het foutenfilter. De details noemen de afgewezen afzender. Ik controleer de oorzaak aan de hand van het onderwerp en de trace-ID, in plaats van de import meerdere keren te starten.

In een echt geval zoek ik eerst uit of deze afzender überhaupt bevoegd is. Een goedgekeurde wijziging van de afzenderlijst wordt opgeslagen en opnieuw gecontroleerd. Daarna verifieer ik een nieuwe, unieke testinvoer tot aan het aangemaakte document. Voor technische fouten geef ik de trace-ID en de concrete foutmelding door.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Mislukte import met bijlage, reden en trace"><figcaption><p>Mislukte import met bijlage, reden en trace</p></figcaption></figure>
