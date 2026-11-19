# Leveranciers en inkooporders uit Infor LN

Dit voorbeeld beschrijft de Infor ION-route voor leveranciers- en inkooporder-BOD's en waar u deze in DocBits controleert. De veertien Infor-afbeeldingen hieronder zijn historische voorbeelden uit een klantomgeving. Bevestig verbindingspunten, API-callnamen en LN-publicatieopties met uw integratiebeheerder; ze zijn voor deze actualisering niet in een Infor-omgeving gecontroleerd. Tijdens deze actualisering is geen BOD gepubliceerd of geïmporteerd.

Infor legt de [LN-publisher voor logistieke stamgegevens](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) en de [transactionele publisher voor orderbeheer](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html) uit. De modi hebben verschillende gevolgen: **Count** meldt aantallen records zonder te publiceren; **Simulate** bouwt een proefresultaat zonder de publicatie vast te leggen; **Publish** verstuurt de geselecteerde gegevens. Een publicatie kan alle abonnees bereiken; controleer daarom het bedrijfsbereik en de abonnees voordat u publiceert.

## **Verbindingspunt**

U moet eerst het DocBits-API-verbindingspunt aanmaken om later de gegevensstroom te kunnen inrichten.

Ga in InforOS naar ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Historische navigatie in ION Desk met de groep Connect uitgeklapt en Connection Points gemarkeerd."><figcaption><p>Historisch navigatievoorbeeld: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Op dit scherm maakt u een nieuw verbindingspunt aan.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Historisch scherm Connection Points met een groene pijl die naar Toevoegen wijst."><figcaption><p>Kies Toevoegen om een verbindingspunt aan te maken; de groene markering geeft de actie in deze historische interface aan.</p></figcaption></figure>

Selecteer de API.

Geef het verbindingspunt een naam en beschrijving die de aard en de omgeving ervan weergeeft. Importeer op het tabblad Connection het serviceaccount dat u voor de betreffende omgeving hebt aangemaakt.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Historisch API-verbindingspunt DocBits-DEV-Demo-Import met het tabblad Connection geselecteerd en een importbesturing voor het serviceaccount."><figcaption><p>Historisch tabblad Connection. De getoonde serviceaccount- en verbindingsnamen horen bij de voorbeeldomgeving.</p></figcaption></figure>

Schakel vervolgens over naar het tabblad Documents. U moet de volgende BOD's aan het verbindingspunt toevoegen.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Historisch Duits tabblad Dokumente met de API-calls en ontvangen BOD's Ack-SupplierInvoice, Sync.PurchaseOrder en Sync.ReceiveDelivery."><figcaption><p>Historisch tabblad Dokumente (Documents). Deze uitsnede toont drie routes; de volledige leveranciersconfiguratie is niet zichtbaar.</p></figcaption></figure>

* Ack-SupplierInvoice

Deze BOD meldt in DocBits dat er binnen Infor een fout is opgetreden. De hieronder getoonde route Acknowledge.SupplierInvoice is een voorbeeld voor factuurbevestigingen. Bevestig de API-callnaam en of deze route voor uw leveranciers- en inkooporderstroom nodig is.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Historisch Duits tabblad ION API voor Ack-SupplierInvoice met een geselecteerde POST-bewerking."><figcaption><p>Historische bevestigingsroute. Ack-SupplierInvoice is een voorbeeld van een API-callnaam; Acknowledge.SupplierInvoice is de ontvangen BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

Het historische voorbeeld hieronder toont één ontvangende bewerking; controleer de actuele bewerking en het aanvraagformaat voor uw omgeving.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Historisch tabblad ION API met Send to API geselecteerd voor Sync.PurchaseOrder en een geconfigureerde POST-bewerking."><figcaption><p>Historische inkooporderroute. Controleer de ontvangende bewerking voor uw DocBits-omgeving in plaats van het oude proxypad over te nemen.</p></figcaption></figure>

* Sync.ReceiveDelivery

Het historische voorbeeld hieronder toont één ontvangende bewerking; controleer de actuele bewerking en het aanvraagformaat voor uw omgeving.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Historisch Duits tabblad ION API voor Sync.ReceiveDelivery met een geconfigureerde POST-bewerking."><figcaption><p>Historische route voor ontvangstgegevens. Controleer of ReceiveDelivery voor uw integratie nodig is en welke bewerking deze ontvangt.</p></figcaption></figure>

Zodra deze BOD's zijn geconfigureerd, slaat u het verbindingspunt op met het pictogram rechts naast de knop Terug.

## **Gegevensstroom**

De gegevensstroom ziet er ongeveer als volgt uit

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Historische documentstroom van een LN-knooppunt via een parallelle splitsing naar vier DocBits-API-knooppunten, gevolgd door een samenvoeging en een eindpunt."><figcaption><p>Historische stroom met vier omgevingen. De splitsing en samenvoeging zijn zichtbaar; het aantal knooppunten en hun bestemming hangen af van uw integratieontwerp.</p></figcaption></figure>

De meerdere DocBits-API-knooppunten in dit historische voorbeeld staan voor afzonderlijke omgevingen. Uw productieontwerp kan een ander aantal knooppunten gebruiken; leid testgegevens nooit naar een productieorganisatie.

De volgende afbeelding gebruikt vier omgevingen uitsluitend als voorbeeld.

### **LN**

Het begin van de gegevensstroom is uw LN-toepassing

### **DocBits-API**

Hier voegt u een toepassing toe en selecteert u de DocBits-API's die u eerder hebt aangemaakt

### **Documenten**

Controleer de documentlijst die aan de stroom is toegewezen. De hier getoonde leveranciersberichten hebben ook bijbehorende ontvangende routes in het API-verbindingspunt nodig. Hun API-callconfiguratie is niet te zien in de eerdere uitsnede met drie routes; bevestig de vereiste bewerkingen met uw integratiebeheerder.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Historisch stroomcanvas met daaronder het Duitse paneel Dokumente met Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster en Sync.SupplierPartyMaster."><figcaption><p>Historische documentlijst van de stroom. Leveranciersberichten verschijnen hier naast inkooporder- en ontvangstberichten.</p></figcaption></figure>

## **LN-BOD's activeren**

Nadat de integratiebeheerder het verbindingspunt, de documentroutes en de actieve gegevensstroom heeft gecontroleerd, gebruikt u de juiste LN-publicatiesessie. Volg elke testidentificatie door LN, ION en DocBits; het activeren van een BOD alleen bewijst niet dat een record is aangekomen.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Historische Duitse startpagina van Infor LN met een lijst met favorieten; het menu Publish BODs is niet geopend."><figcaption><p>Historische LN-startpagina. Gebruik de hieronder beschreven navigatie om de juiste publicatiesessie te vinden.</p></figcaption></figure>

### **PurchaseOrder**

Kies in het linkermenu van de bovenstaande pagina Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Open het tabblad PurchaseOrder en schakel het selectievakje in.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Historische sessie Publish Order Management Transactional Data met het tabblad PurchaseOrder en het selectievakje ingeschakeld en zichtbare velden voor het orderbereik."><figcaption><p>Historische selectie van PurchaseOrder. Controleer het orderbereik en de statussen voordat u publiceert.</p></figcaption></figure>

### **Leveranciers**

Ga vanaf de LN-startpagina in het linkermenu naar Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Open het tabblad PartyMaster en schakel het selectievakje Supplier → Buy-from of SupplierPartyMaster in.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Historische sessie Publish Logistic Master Data met PartyMaster geselecteerd en het vakje Supplier Buy-from ingeschakeld."><figcaption><p>Historische leveranciersselectie op PartyMaster. Kies de partnerrollen die uw integratie nodig heeft en controleer het selectiebereik.</p></figcaption></figure>

### **BOD's activeren**

Selecteer het tabblad Options zodra alle juiste BOD's voor publicatie zijn aangevinkt.

Controleer de opties voor uw omgeving. Het historische voorbeeld markeert Publish en Use Process/Sync Verb; dat zijn geen universele instellingen voor elke integratie.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Historisch tabblad Options in LN met Publish en Use Process/Sync Verb gemarkeerd en een zichtbaar bedrijfsbereik."><figcaption><p>Historisch voorbeeld van Options. Hier zijn Publish en Use Process/Sync Verb geselecteerd; controleer modus, bedrijfsbereik en abonnees voor uw eigen uitvoering.</p></figcaption></figure>

Gebruik vóór **Process** de optie **Count** of **Simulate** en controleer het aantal records en het bedrijfsbereik, voor zover uw LN-versie deze modi biedt. Publiceer alleen met toestemming van de integratiebeheerder. Een bevestiging dat BOD's zijn geactiveerd, bewijst geen aflevering aan DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Historisch tabblad Options in LN met de knop Process gemarkeerd vóór uitvoering."><figcaption><p>Historische actie Process vóór uitvoering. Deze afbeelding bevat geen publicatieresultaat en geen bevestiging dat DocBits gegevens heeft ontvangen.</p></figcaption></figure>

## Controleren in DocBits

Controleer in Infor ION of de aflevering aan de bedoelde DocBits-organisatie is geslaagd. Open daarna **Instellingen → Documentverwerking → Stamgegevens opzoeken**. Open onder **BOD-invoergegevens** de optie **Leverancier**. Kies het identificatieveld in **Zoeken op kolom**, voer een bekend leveranciersnummer of een bekende naam in bij **Zoekopdracht Tekenreeks** en gebruik het vergrootglas om te zoeken. Open **Inkooporder** en zoek een bekend ordernummer. Controleer ook **Koptekst Van Inkooporder** als uw mapping kop en regels scheidt. Vergelijk de identificaties en het bedrijf met LN; leid niet uit een geslaagd publicatiebericht af dat alle records zijn aangekomen.

<figure><img src="../../../../.gitbook/assets/dbdc-1147-supplier-nl-20261112.png" alt="Nederlandse weergave van Stamgegevens opzoeken in DocBits met het tabblad Leverancier, de zoekvelden Zoeken op kolom en Zoekopdracht Tekenreeks en een tabel met verzonnen voorbeeldrijen."><figcaption><p>Controleweergave voor leveranciers in de DocBits-sandbox (versie 11.27.7). De getoonde rijen SUP-1001 tot en met SUP-1010 zijn verzonnen voorbeeldgegevens en bewijzen geen LN-import; de kolomkoppen van de tabel blijven in deze versie Engels.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1147-purchase-order-nl-20261112.png" alt="Nederlandse weergave van Stamgegevens opzoeken in DocBits met de tabbladen Leverancier en Inkooporder, het tabblad Inkooporder actief en een tabel met verzonnen inkooporderrijen."><figcaption><p>Controleweergave voor inkooporders in de DocBits-sandbox (versie 11.27.7). De getoonde orders PO-4500 tot en met PO-4509 zijn verzonnen voorbeeldgegevens en de kolomkoppen van de tabel blijven in deze versie Engels; vergelijk een echt testorder en het bedrijf met LN en ION.</p></figcaption></figure>

De Engelse Dev-weergaven zijn op 29 oktober 2026 gecontroleerd zonder een BOD te publiceren, een bestand te importeren of stamgegevens te wijzigen. In die Engelse afbeeldingen zijn recordrijen weggelaten; de twee Nederlandse opnamen hierboven tonen verzonnen voorbeeldrijen en alleen waar u controleert, niet een voltooide LN-overdracht. Als het verwachte record ontbreekt, controleer dan de LN-publicatielogs, de ION-routering, de organisatie en de BOD-mapping voordat u opnieuw uitvoert.
