# LN-configuratie

Deze handleiding combineert historische voorbeelden uit Infor ION met het actuele LN-exportformulier van DocBits. De Infor-afbeeldingen laten de afzonderlijke stappen zien; de namen van tenants en toewijzingen en de opbouw daarvan zijn voorbeelden. Laat verbindingspunten, het toewijzingspakket en de BOD-rechten door uw Infor-beheerder controleren voor uw LN-bedrijf voordat u een gegevensstroom activeert. Voor deze actualisering van de documentatie zijn geen Infor-tenantverbinding en geen facturenexport getest.

## Vereisten

U hebt het volgende aangemaakt:

* een ION-API-eindpunt;
* een ION-API-bestand;
* een BOD-toewijzingsbestand;
* een IDM-toewijzingsbestand.

## Toewijzingsbestanden importeren

Voordat u de gegevensstroom inricht, importeert u de toewijzingsbestanden in Infor OS.

Open in ION Desk → Connect het onderdeel **Mappings**.

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Historisch voorbeeld: navigatie in ION Desk met de groep Connect uitgeklapt en de onderdelen Data Flows, API Flows, Connection Points, File Templates en Enterprise Locations."><figcaption><p>Historisch voorbeeld: navigatie in ION Desk met de groep Connect uitgeklapt en de onderdelen Data Flows, API Flows, Connection Points, File Templates en Enterprise Locations. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Klik op het pictogram Importeren.

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Historisch voorbeeld: werkbalk Mappings in een oudere ION Desk met het importpictogram omcirkeld."><figcaption><p>Historisch voorbeeld: werkbalk Mappings in een oudere ION Desk met het importpictogram omcirkeld. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

* Kies daar de toewijzingsbestanden die u nodig hebt: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice en LoadSupplierInvoice\_ProcessSupplierInvoice.
* Keur na het importeren elke toewijzing goed met het vinkjespictogram in de tegel op het toewijzingsdashboard.

## Van DocBits naar LN

Stel daarna de gegevensstroom in ION Desk in: open de toepassing en kies **Data Flow → + ADD → Document Flow**, zoals hieronder.

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Historisch voorbeeld: pagina Data Flows in ION Desk met de navigatie links, de stroom DF_SLTStAPI in de lijst en de menuonderdelen Document Flow en Data Lake Flow."><figcaption><p>Historisch voorbeeld: pagina Data Flows in ION Desk met de navigatie links, de stroom DF_SLTStAPI in de lijst en de menuonderdelen Document Flow en Data Lake Flow. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Gebruik dit canvas om de informatiestroom van DocBits naar LN op te bouwen.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Historisch voorbeeld: nieuwe documentstroom met een leeg eigenschappenpaneel en de meldingen Document flow name must be specified en The document flow has no activities."><figcaption><p>Historisch voorbeeld: nieuwe documentstroom met een leeg eigenschappenpaneel en de meldingen Document flow name must be specified en The document flow has no activities. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Een LN-gegevensstroom ziet er ongeveer uit zoals hieronder. Er zijn meerdere paden, omdat elk pad voor een bepaald documenttype bedoeld is; deze uitleg richt zich op de factuurgegevensstroom.

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Historisch voorbeeld: canvas van een gegevensstroom met meerdere paden voor verschillende documenttypen, elk opgebouwd uit een verbindingspunt van DocBits, een toewijzing en een verbindingspunt van LN."><figcaption><p>Historisch voorbeeld: canvas van een gegevensstroom met meerdere paden voor verschillende documenttypen, elk opgebouwd uit een verbindingspunt van DocBits, een toewijzing en een verbindingspunt van LN. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Alle onderdelen van de keten sleept u uit het bovenste gedeelte.

In de keten zijn DocBits en LN toepassingen; daartussen staan toewijzingen die de gegevens omzetten naar een vorm die het volgende deel van de gegevensstroom begrijpt, en die de informatie naar de juiste bestemming brengen.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Historisch voorbeeld: activiteitenpalet en stroom in ION, waarbij toepassingsactiviteiten DocBits en LN voorstellen en toewijzingsactiviteiten ertussen staan."><figcaption><p>Historisch voorbeeld: activiteitenpalet en stroom in ION, waarbij toepassingsactiviteiten DocBits en LN voorstellen en toewijzingsactiviteiten ertussen staan. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

### DocBits-toepassing

Geef de toepassing een passende naam, bijvoorbeeld ‘DocBits', kies daarna het plusteken en zoek het verbindingspunt dat u eerder hebt gemaakt, bijvoorbeeld DocBits\_Export, en klik erop.

Om dit verbindingspunt te maken, opent u ION Desk → Connect → Connection Points.

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Historisch voorbeeld: navigatie in ION Desk met de groep Connect uitgeklapt en de onderdelen Data Flows, API Flows, Mappings en Connection Points."><figcaption><p>Historisch voorbeeld: navigatie in ION Desk met de groep Connect uitgeklapt en de onderdelen Data Flows, API Flows, Mappings en Connection Points. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Klik op **+ Add**.

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Historisch voorbeeld: pagina Connection Points in ION Desk met de groep Connect open in de navigatie."><figcaption><p>Historisch voorbeeld: pagina Connection Points in ION Desk met de groep Connect open in de navigatie. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Kies **IMS via API Gateway** en vul de volgende gegevens in.

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Historisch voorbeeld: verbindingspunt IMS via API Gateway met een voorbeeld van een logische id en een afgeschermd veld ION API Client Id."><figcaption><p>Historisch voorbeeld: verbindingspunt IMS via API Gateway met een voorbeeld van een logische id en een afgeschermd veld ION API Client Id. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

De ION API-client-id is de waarde `ci` in uw `.ionapi`-bestand. Vraag het tenantbestand aan bij de bevoegde Infor-beheerder. Het bevat inloggegevens; houd het buiten schermafbeeldingen, tickets en Git. Zie de [uitleg van Infor over de ION-API-inloggegevens](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Schakel over naar het tabblad voor documenten en voeg het BOD Sync.CaptureDocument toe aan het verbindingspunt van DocBits, zoals hieronder.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Historisch voorbeeld: verbindingspunt DocBits-Sandbox-Export met het tabblad Documents open en het document Sync.CaptureDocument toegewezen."><figcaption><p>Historisch voorbeeld: verbindingspunt DocBits-Sandbox-Export met het tabblad Documents open en het document Sync.CaptureDocument toegewezen. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Sla het verbindingspunt daarna op met het diskettepictogram linksboven.

Ga terug naar het onderdeel **Dataflow** in ION Desk om uw gegevensstroom te openen. Uw DocBits-toepassing ziet er ongeveer uit zoals hieronder.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Historisch voorbeeld: eigenschappen van een toepassingsactiviteit met de naam DocBits-Sandbox en het gekozen verbindingspunt DocBits-Sandbox-Export."><figcaption><p>Historisch voorbeeld: eigenschappen van een toepassingsactiviteit met de naam DocBits-Sandbox en het gekozen verbindingspunt DocBits-Sandbox-Export. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

### Toewijzing 1

De eerste toewijzingsknoop ziet er als volgt uit.

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Historisch voorbeeld: eigenschappen van de eerste toewijzing Capture2sync met de voorbeeldtoewijzing LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Historisch voorbeeld: eigenschappen van de eerste toewijzing Capture2sync met de voorbeeldtoewijzing LN_CaptureDocumentToSupplierInvoice_1. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

### Toewijzing 2

De tweede toewijzingsknoop ziet er als volgt uit.

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Historisch voorbeeld: eigenschappen van de tweede toewijzing Load2Process met de voorbeeldtoewijzing LoadSupplierToProcessSupplierInvoice."><figcaption><p>Historisch voorbeeld: eigenschappen van de tweede toewijzing Load2Process met de voorbeeldtoewijzing LoadSupplierToProcessSupplierInvoice. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

### LN-toepassing

In Infor bestaat er al een verbindingspunt voor het juiste LN-bedrijf, bijvoorbeeld met de naam ‘LN'. Net als bij de DocBits-toepassing selecteert u het met het plusteken; het resultaat ziet er als volgt uit.

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Historisch voorbeeld: eigenschappen van de LN-toepassingsactiviteit met de voorbeeldnaam LN-200 en de gekozen toepassingsverbinding In01_0200."><figcaption><p>Historisch voorbeeld: eigenschappen van de LN-toepassingsactiviteit met de voorbeeldnaam LN-200 en de gekozen toepassingsverbinding In01_0200. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

### BOD's

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Historisch voorbeeld: canvas van een gegevensstroom met de knopen DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder en AdvancedShip boven de ingang End."><figcaption><p>Historisch voorbeeld: canvas van een gegevensstroom met de knopen DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder en AdvancedShip boven de ingang End. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

De volgende configuraties zien er als volgt uit:

#### Eerste configuratie

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Historisch voorbeeld: documentenlijst van de eerste stap met Sync.CaptureDocument."><figcaption><p>Historisch voorbeeld: documentenlijst van de eerste stap met Sync.CaptureDocument. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

#### Tweede configuratie

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Historisch voorbeeld: documentenlijst van de tweede stap met Load.SupplierInvoice."><figcaption><p>Historisch voorbeeld: documentenlijst van de tweede stap met Load.SupplierInvoice. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

#### Derde configuratie

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Historisch voorbeeld: documentenlijst van de derde stap met Process.SupplierInvoice."><figcaption><p>Historisch voorbeeld: documentenlijst van de derde stap met Process.SupplierInvoice. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

Het laatste pictogram hoort leeg te zijn, omdat het geen document en geen informatie doorgeeft.

Nadat uw Infor-beheerder alle knopen, toewijzingen en documentabonnementen heeft gecontroleerd, activeert u de bedoelde gegevensstroom met het bedieningselement voor activeren. De historische afbeelding hieronder markeert dat bedieningselement; de oude naam van de stroom bevat M3 en mag niet worden gebruikt als naam of bestemming voor uw LN-inrichting.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Historisch voorbeeld: werkbalk van een historische documentstroom met het activeringsbedieningselement omcirkeld. Het oude voorbeeld heet DocBits-Export-M3; kies de juiste LN-stroom in uw tenant."><figcaption><p>Historisch voorbeeld: werkbalk van een historische documentstroom met het activeringsbedieningselement omcirkeld. Het oude voorbeeld heet DocBits-Export-M3; kies de juiste LN-stroom in uw tenant. Controleer de bijbehorende instellingen in uw Infor-tenant.</p></figcaption></figure>

## Export configureren in DocBits

Open in de bedoelde DocBits-organisatie **Instellingen → Exporteren**. De pagina toont de bestaande exportconfiguraties; kies **Nieuw** om een nieuwe configuratie voor te bereiden.

<figure><img src="../../../.gitbook/assets/ln-configuration-export-list-nl-20261112.png" alt="Actuele Nederlandse exportlijst in DocBits met de knop Nieuw, de kolommen Type, Suborganisaties, Titel, Exportmethode en Acties en de melding dat er geen configuraties zijn gevonden."><figcaption><p>De lijst bevat in deze verzonnen voorbeeldorganisatie geen exportconfiguratie en toont de melding dat er nog geen is aangemaakt. Nieuw opent het configuratieformulier; een opgeslagen configuratie is niet geopend of gewijzigd.</p></figcaption></figure>

Vul onder **Basisgegevens** een **Configuratietitel** in, kies het **Documenttype** (voor de factuuroverdracht Factuur) en kies alleen een **Suborganisatie** als uw inrichting die nodig heeft. Kies bij **Exporteren** de waarde **Infor** en daarna bij **Informatietype** de waarde **Infor IDM + LN**.

Lever alle drie bestanden aan die een nieuwe LN-configuratie vereist: het **ION API-bestand** (`.ionapi`), het **IDM-toewijzingsbestand** (`.properties`) en het **LN-mappingbestand** (`.properties`). Vraag de bestanden voor deze tenant en dit LN-bedrijf aan bij de bevoegde Infor-beheerder. Klik daarvoor op **Klik om te uploaden** of sleep het bestand naar het veld. De afbeelding laat alle uploadvelden bewust leeg en bevat geen inloggegevens.

<figure><img src="../../../.gitbook/assets/ln-configuration-export-ln-nl-20261112.png" alt="Actueel Nederlands formulier in DocBits met de onderdelen Basisgegevens en Exportconfiguratie, het informatietype Infor IDM + LN, een nog niet gekozen documenttype en drie lege uploadvelden voor ION API-bestand, IDM-toewijzingsbestand en LN-mappingbestand."><figcaption><p>Het actuele LN-formulier scheidt de drie uploadvelden. Onder Basisgegevens worden het doeltype en het documenttype vastgelegd; in dit voorbeeld is geen bestand geüpload en is geen configuratie opgeslagen.</p></figcaption></figure>

Nadat uw beheerder de ION-stroom en de bestanden heeft bevestigd, slaat u de configuratie op met **Opslaan** en test u één toegestane factuur buiten de productieomgeving. Controleer het resultaat in DocBits, Infor ION en LN. Een opgeslagen configuratie bewijst op zichzelf niet dat LN een factuur heeft ontvangen. Met **Annuleren** verlaat u het formulier als u alleen de beschikbare velden wilt bekijken.

Voor de rol van verbindingspunten en documentstromen zie de [uitleg van Infor ION](https://docs.infor.com/ln/10.8/en-us/lnesolvh/lnoshybridng/wxa1699288671147.html).
