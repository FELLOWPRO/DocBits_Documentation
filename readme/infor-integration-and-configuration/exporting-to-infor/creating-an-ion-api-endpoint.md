# Een Infor ION API-endpoint maken voor DocBits-exporten

Een Infor-beheerder configureert het API Gateway-endpoint voor de **specifieke DocBits-omgeving en -organisatie**. De oude afbeeldingen op deze pagina toonden één historische Infor-tenant, een vast voorbeeld met `api.docbits.com` en een ouder DocBits-exportformulier. Gebruik de goedgekeurde doel-URL, API-sleutel en OpenAPI-document voor uw eigen omgeving. Er is voor deze update geen Infor-tenant gekoppeld en geen endpoint opgeslagen.

## Voordat u begint

Vraag bij uw integratiebeheerder de URL van de doel-DocBits-API op, de goedgekeurde API-sleutel en de naam van de bijbehorende header, de OpenAPI-URL en de beoogde Infor- en DocBits-omgevingen. Houd sleutels en `.ionapi`-bestanden buiten tickets, screenshots en de Git-repository. Bevestig dat een testendpoint niet naar productie kan routeren.

## Infor API Gateway configureren

1. Maak in **Available APIs** een API-suite van het type **Custom or Non-Infor** voor de doelomgeving. Zie de [instructies van Infor over API-suites](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/gyy1489512842881.html).
2. Voeg aan de suite een endpoint toe met de goedgekeurde **Target Endpoint URL**. Selecteer het authenticatietype dat dat endpoint vereist. Voor **API Key** vraagt Infor om een **Key Name** en **Key Value**; gebruik de naam die het DocBits-API-contract voorschrijft en de sleutel die voor deze organisatie is uitgegeven. Zie de [endpointvelden van Infor](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/apigatewayag_cloud/bmg1489588707659.html). Kopieer geen sleutel uit een andere omgeving.
3. Voeg de OpenAPI/Swagger-URL van de omgeving toe onder de **Documentation**-instellingen van het endpoint, volgens de [documentatie-instructies van Infor](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tzr1489597424134.html). Controleer of het endpoint verschijnt in de [API-metadata](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tdr1489674063627.html).
4. Verifieer samen met de Infor-beheerder de doel-URL, authenticatie, proxy-pad en een veilige aanroep buiten productie voordat u het endpoint gebruikt in een ION-documentstroom. Alleen een API-suite opslaan bewijst niet dat een document is afgeleverd.

## Export configureren in DocBits

Open in de beoogde DocBits-organisatie **Instellingen → Exporteren** en kies **Nieuw**. Gegevens van bestaande configuraties zijn in de afbeelding afgedekt.

<figure><img src="../../.gitbook/assets/dbdc-40-export-list-nl-20261030.png" alt="Huidige Nederlandse exportlijst met Nieuw, de melding over opeenvolgende uitvoering en tabelkoppen; bestaande configuratiegegevens zijn afgedekt."><figcaption><p>Nieuw opent een niet-opgeslagen configuratie. Bestaande configuratiegegevens zijn in deze actuele native opname afgedekt.</p></figcaption></figure>

Vul **Configuratietitel** in, kies **Documenttype** en zo nodig **Suborganisatie**. Kies bij **Exporteren** de weergegeven waarde **Infor** voor Infor en bij **Informatietype** de optie **Infor IDM + ION BOD**. Het voorbeeld gebruikt **Factuur**.

Kies bij **Implementatietype** de cloud- of lokale implementatie die bij uw omgeving past. Het formulier toont **ION API-bestand** (`.ionapi`, verplicht), **IDM-toewijzingsbestand** (`.properties`) en **BOD-kaartbestand** (`.properties`). Vraag de tenantspecifieke bestanden aan de beheerder. Titel, suborganisatie en alle drie uploadvelden zijn leeg in de afbeelding.

<figure><img src="../../.gitbook/assets/dbdc-40-export-ion-bod-nl-20261030.png" alt="Huidig Nederlands formulier Infor IDM + ION BOD met Factuur, implementatiekeuzes en drie lege uploadvelden."><figcaption><p>Huidig native formulier Infor IDM + ION BOD: Factuur en de cloudvariant zijn geselecteerd; titel, suborganisatie en alle drie uploadvelden zijn leeg. Het formulier is met Annuleren gesloten zonder op te slaan.</p></figcaption></figure>

Nadat de beheerder de ION-route heeft gevalideerd, slaat u de configuratie op en test u één document buiten productie. Controleer de status ervan in DocBits en in Infor ION. Een opgeslagen formulier of een API-metadata-item bewijst geen geslaagde export.

Voor deze documentatiecontrole zijn alleen de lijst en het nieuwe formulier bekeken. Er zijn geen bestanden geüpload, configuraties opgeslagen of geactiveerd, verbindingen getest, Infor-tenants geopend of documenten daadwerkelijk geëxporteerd.
