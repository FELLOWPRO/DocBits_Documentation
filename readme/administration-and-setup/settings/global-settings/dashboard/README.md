# Dashboard

## Overzicht

De instellingen voor het Dashboard zijn ontworpen om beheerders te helpen de gegevenspresentatie en interactie binnen het DocBits-dashboard te controleren. Deze instellingen bepalen welke informatie onmiddellijk beschikbaar is bij het inloggen, zodat gebruikers snel toegang hebben tot de meest relevante gegevens voor hun taken.

![Italiaanse documentenlijst met het documentnaambereik van Delivery Note, Advance Ship Notice en Purchase Order en in totaal 2373 documenten](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Toegang tot de Dashboard Instellingen

Om toegang te krijgen tot de dashboardinstellingen, navigeer naar:\
**Instellingen → Globale instellingen → Dashboard**

![Italiaanse algemene dashboardinstellingen met de opties om filters te resetten na documentupload, herstart en export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **Algemeen**

* **Filters resetten**: Hiermee kan worden geconfigureerd wanneer dashboardfilters moeten worden gereset, zoals na documentupload, documentherstart of documentexport. Dit helpt bij het behouden van een schone lei voor gegevensweergave volgens specifieke workflowfasen.
* **Dashboardgegevens**:
  * **Automatisch uploaden van dashboard**: Beheert of het dashboard automatisch gegevens moet laden bij toegang door de gebruiker, wat kan helpen om laadtijden te verminderen en de gebruikerservaring te verbeteren door alleen gegevens te laden wanneer dat nodig is.
  *   **Dashboardgegevens exporteren**: Deze functie voegt een nieuwe **Exporteer**-knop toe aan de dashboardwerkbalk, waarmee je de huidige dashboardweergave kunt exporteren als een **.csv** of **.xlsx**-bestand.

      ![Sectie General van de dashboardinstellingen met de schakelaars Reset filters en de Dashboard data-opties Auto refresh dashboard on document updates en Export Dashboard Data](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Exportgeschiedenis**

In de **Exportgeschiedenis** zie je een tabel met alle eerdere exports, samen met belangrijke informatie over elk verzoek.

![Sectie Export History op de instellingenpagina van het Dashboard met de kolommen Email, Status, Requested At, Completed At, Format en Filters Used](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

De volgende details zijn inbegrepen:

* **E-mail**: Het e-mailadres van waaruit de export is aangevraagd.
* **Status**: De huidige status van de export (In afwachting, Voltooid).
* **Aangevraagd op**: De datum en tijd waarop de export is gestart.
* **Voltooid op**: De datum en tijd waarop de export is voltooid.
* **Formaat**: Het bestandsformaat dat is gebruikt voor de export (CSV, XLSX).
* **Gebruikte filters**: Eventuele filters die op het dashboard zijn toegepast op het moment van export.

<mark style="color:red;">**Opmerking**</mark>: Om tabellen te exporteren, moet de optie Dashboardgegevens exporteren in de [Algemeen](./#algemeen) sectie actief zijn.

## **Actie**

* **Toewijzen aan**: Deze functie stelt gebruikers in staat om machtigingen voor documenttoewijzing te definiëren.
  * **Alleen voor Admin**: Alleen admin-gebruikers kunnen documenten toewijzen, ongeacht de machtigingen die aan niet-admin gebruikers zijn verleend.
  * **Alle gebruikers**: Alle gebruikers die de nodige [machtigingen](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) hebben gekregen, kunnen documenten toewijzen.
* **Opnieuw starten**: Deze functie stelt gebruikers in staat om machtigingen voor het opnieuw starten van documenten te definiëren.
  * **Alleen voor Admin**: Alleen gebruikers met Admin-rechten kunnen documenten opnieuw starten, ongeacht de machtigingen die aan niet-admin gebruikers zijn verleend.
  * **Alleen Admin en Toegewezen**: Alleen gebruikers met Admin-rechten en de toegewezen gebruiker kunnen het document opnieuw starten.
  * **Alle gebruikers**: Alle gebruikers die de nodige [machtigingen](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) hebben gekregen, kunnen documenten opnieuw starten.

![Sectie Action op de dashboardinstellingenpagina met Assign to en Restart beide ingesteld op Only for Admin](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filters**

* **Statusfilterstijl**: Bepaalt de presentatie stijl van statusfilters, die kan worden ingesteld op standaard of aangepast volgens de operationele focus van de gebruikers.
* **Aangepast statusfilter**: Maakt het mogelijk om aangepaste filters te creëren en toe te passen die specifieke documentstatussen zoals "Nieuw", "Valideren" of "Exporteren" kunnen targeten. Dit stelt gebruikers in staat om snel toegang te krijgen tot documenten in specifieke fasen van verwerking.

![Instellingenpagina van het dashboard met de sectie Filters met Status filter style en Custom status filter plus de sectie Advance Shipment Dashboard](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Dashboard voor geavanceerde verzending

* **Zichtbaarheid van geleverde bestellingen**: Deze functie stelt de gebruiker in staat om de duur op te geven waarvoor geleverde bestellingen zichtbaar zullen zijn.

![Sectie Advance Shipment Dashboard op de instellingenpagina van het dashboard met Delivered Orders Visibility ingesteld op 14 Days](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Deze dashboardinstellingen zijn cruciaal om ervoor te zorgen dat het DocBits-platform zo responsief en nuttig mogelijk is, en gebruikers een krachtig hulpmiddel biedt om documentverwerkingsactiviteiten rechtstreeks vanuit het dashboard te monitoren en te beheren.
