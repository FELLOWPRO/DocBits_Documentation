# LN-configuratie

## Vereisten

Je hebt gemaakt:

* An ION API Endpoint
* An ION API File
* Een BOD-toewijzingsbestand
* Een IDM-toewijzingsbestand

## Mappingbestanden importeren

Voordat u de gegevensstroom instelt, moet u de toewijzingsbestanden importeren in InforOS

In ION Desk → Verbinden en open Mappings

![Navigatie van ION Desk met de uitgeklapte groep Connect en de items Data Flows, API Flows, Connection Points, File Templates en Enterprise Locations](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k)

Klik op het pictogram Importeren

![Werkbalk van de pagina Mappings in ION Desk met het groene ronde importpictogram](https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Hier moet u de verschillende mappingbestanden selecteren die u nodig heeft, waaronder: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Nadat u alle toewijzingsbestanden heeft geïmporteerd, zorg ervoor dat u ze allemaal goedkeurt door op het vinkje in elk van hun vierkanten op het Mapping-dashboard te klikken.

## Van DocBits naar LN

De volgende stap is het instellen van de Data Flow in ION Desk, navigeer naar de ION Desk-applicatie en selecteer Data Flow → + ADD → Document Flow zoals hieronder

![Pagina Data Flows in ION Desk met de navigatie links, de flow DF_SLTStAPI in de lijst en de menu-items Document Flow en Data Lake Flow](https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Je ziet dan deze pagina, hier bouw je de informatiestroom op van DocBits naar M3

![Nieuwe Document Flow met een leeg eigenschappenpaneel en de meldingen Document flow name must be specified en The document flow has no activities](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Een LN gegevensstroom zal er ongeveer zo uitzien als hieronder wordt weergegeven (er zijn meerdere paden omdat elk afzonderlijk pad bedoeld is voor een specifiek documenttype, voor deze uitleg zullen we ons concentreren op de factuurgegevensstroom).

![Werkblad van de dataflow met meerdere paden voor verschillende documenttypen, elk pad opgebouwd uit een DocBits-verbindingspunt, een mapping en een LN-verbindingspunt](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U)

Alle delen van de ketting worden vanuit het bovenste gedeelte gesleept en neergezet

In de keten zijn DocBits en LN beide toepassingen, terwijl er tussenin mappings zijn die de gegevens omzetten in een vorm die kan worden begrepen door de volgende sectie van de gegevensstroom en “map” de informatie zodat deze terechtkomt waar deze ook nodig of bedoeld is.

![Detail van het werkblad van de dataflow met de knopen DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder en de LN-verbindingspunten LN-200-41 en LN-200-4](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### DocBits-applicatie

Geef het de juiste naam, zoals “DocBits”, selecteer vervolgens het plusteken en zoek naar het verbindingspunt dat u eerder hebt gemaakt, zoals DocBits\_Export of iets dergelijks, en klik erop.

Om dit verbindingspunt te maken, gaat u naar ION Desk → Verbinden → Verbindingspunten

![Navigatie van ION Desk met de uitgeklapte groep Connect en de items Data Flows, API Flows, Mappings en Connection Points](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Click “+ Add”

![Pagina Connection Points in ION Desk met de groep Connect geopend in de navigatie](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos)

Selecteer “IMS via API Gateway” en vul de volgende informatie in

![Venster Infor Application Connection Point voor IMS via API Gateway met de naam DocBits-Sandbox-Export, het ION API Client Id en het Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

De ION API Client ID bevindt zich in het ION API bestand dat u hebt gemaakt bij Een ION API bestand maken onder de waarde “ci”.

Schakel over naar het documenttabblad en voeg de Sync.CaptureDocument BOD toe aan het DocBits verbindingspunt, zoals hieronder.

![Verbindingspunt DocBits-Sandbox-Export met het tabblad Documents geopend en het toegewezen document Sync.CaptureDocument](https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg)

Sla vervolgens het verbindingspunt op door op het schijfpictogram in de linkerbovenhoek te drukken.

Navigeer terug naar de sectie Gegevensstroom van ION Desk om toegang te krijgen tot uw gegevensstroom. Uw DocBits-toepassing zou er ongeveer zo uit moeten zien als hieronder wordt weergegeven.

![Paneel Application Activity Properties van de DocBits-toepassing met de naam DocBits-Sandbox-Export en de beschrijving DocBits-Sandbox-Export](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Mapping 1

Het eerste mappingknooppunt zou er als volgt uit moeten zien

![Paneel Mapping Properties van de eerste mappingknoop met de velden Name en Description en de keuzelijst Mapping](https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mapping 2

Het tweede mappingknooppunt zou er als volgt uit moeten zien

![Paneel Mapping Properties van de tweede mappingknoop met de velden Name en Description en de keuzelijst Mapping](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### LN-applicatie

Er zou al een LN of een gelijkaardig genoemd verbindingspunt (voor het juiste LN bedrijf) aangemaakt moeten zijn in INFOR, dus net als de DocBits Applicatie selecteert u deze door op het “+” teken te klikken en het zou er als volgt uit moeten zien

![Paneel Application Activity Properties van de LN-toepassing met de naam LN-200 en de beschrijving In01_0200 LN Farm](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Werkblad van de dataflow met de knopen DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder en AdvancedShip boven de vermelding End](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

De volgende configuraties moeten er als volgt uitzien:

#### Eerste

![Keuzelijst Documents van de eerste knoop met de vermelding Sync.CaptureDocument](https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Tweede

![Keuzelijst Documents van de tweede knoop met de vermelding Load.SupplierInvoice](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Derde

![Keuzelijst Documents van de derde knoop met de vermelding Process.SupplierInvoice](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw)

Het laatste pictogram moet leeg zijn, omdat er geen document of informatie op staat.

Zodra u alle benodigde knooppunten aan de gegevensstroom heeft toegevoegd, drukt u op deze knop om de gegevensstroom te activeren

![Werkbalk van de Document Flow met de knoppen om verbindingspunten toe te voegen en te verwijderen en de knop om de dataflow te activeren, onder de naam DocBits-Export-M3](https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
