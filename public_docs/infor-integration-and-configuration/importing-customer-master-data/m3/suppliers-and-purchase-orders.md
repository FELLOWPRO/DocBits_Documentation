# Leveranciers en inkooporders uit Infor M3

Dit voorbeeld koppelt de BOD's voor leveranciers en inkooporders uit M3 via Infor ION aan DocBits. De vijftien Infor-afbeeldingen hieronder zijn historische voorbeelden uit een tenant en vormen geen actuele controle van uw M3-installatie. Vraag de Infor-beheerder de BOD-namen, brontabellen, het bedrijf, de divisie, de namen van de API-aanroepen en de doelomgeving te bevestigen voordat u een taak uitvoert. Voor deze update zijn geen M3-initial-load en geen DocBits-import uitgevoerd.

De [handleiding voor de initial load](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) van Infor legt de definities in EVS006 uit, evenals het werkwoord en de selectie in EVS007, het indienen en de geschiedenis. Gebruik eerst een beperkte selectie; een onbeperkte uitvoering kan veel gebeurtenissen opleveren.

## **Verbindingspunt**

U moet het verbindingspunt van de DocBits-API maken om later de gegevensstroom te kunnen aanmaken.

Navigeer in InforOS naar ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Historische navigatie in ION Desk met de groep Connect uitgeklapt en Connection Points gemarkeerd."><figcaption><p>Historische navigatie: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Eenmaal hier moet u een nieuw verbindingspunt aanmaken.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Historische pagina Connection Points met een groene pijl die naar Add wijst."><figcaption><p>Historische actie Add om een verbindingspunt aan te maken.</p></figcaption></figure>

**Select API**

Geef het verbindingspunt een naam en een beschrijving die de aard en de omgeving ervan aangeeft. Importeer op het tabblad Connection het serviceaccount dat u hebt aangemaakt voor de omgeving waarmee u werkt.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Historisch verbindingspunt DocBits-DEV-Demo-Import voor de API met het tabblad Connection geselecteerd en een Import-besturingselement voor het serviceaccount."><figcaption><p>Historisch tabblad Connection. De getoonde namen horen bij de voorbeeldomgeving; gebruik uw eigen serviceaccount.</p></figcaption></figure>

Ga vervolgens naar het tabblad Documents. U moet de volgende BOD's aan het verbindingspunt toevoegen; niet allemaal zijn ze nodig voor de stamgegevens van leveranciers en inkooporders, maar ze zijn wel nuttig wanneer andere functies zoals Automatic Accounting moeten worden ingevoerd.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Historisch tabblad Documents met de documenten Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster en Sync.SupplierPartyMaster."><figcaption><p>Historische lijst met ontvangen documenten. De getoonde leveranciers-BOD is Sync.RemitToPartyMaster, zonder het achtervoegsel Data.</p></figcaption></figure>

Deze historische opzet gebruikt Sync.RemitToPartyMaster, Sync.SupplierPartyMaster en Sync.PurchaseOrder. Bevestig welke BOD's uw DocBits-mapping nodig heeft; de opzet kan per tenant en per functie verschillen.

* Sync.RemitToPartyMaster en Sync.SupplierPartyMaster

De volgende historische afbeelding toont Sync.SupplierPartyMaster. Richt elke vereiste leveranciers-BOD in met de API-aanroepnaam en de ontvangende bewerking die voor uw omgeving zijn bevestigd; de tweede leveranciersroute staat niet op de afbeelding.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Historisch tabblad ION API met Send to API geselecteerd, API Call Name Sync.SupplierPartyMaster en de bewerking POST."><figcaption><p>Historische route SupplierPartyMaster. De afbeelding toont één leveranciersroute; bevestig de ontvangende bewerking apart voor elke vereiste BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

De volgende historische afbeelding toont één ontvangende bewerking voor inkooporders. Bevestig het actuele eindpunt en het aanvraagformaat voor uw omgeving.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Historisch tabblad ION API met Send to API geselecteerd voor Sync.PurchaseOrder en de bewerking POST."><figcaption><p>Historische route PurchaseOrder. Het oude proxypad van de API Gateway is een voorbeeld, geen universeel DocBits-adres.</p></figcaption></figure>

Zodra deze BOD's zijn geconfigureerd, kunt u het verbindingspunt opslaan met het pictogram rechts van de terugknop.

## **Gegevensstroom**

Deze historische gegevensstroom is één mogelijke opzet; controleer de routes en de ontvangende organisatie in uw eigen tenant.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Historische gegevensstroom van M3 via een Yes/No-filter en een parallelle splitsing naar vier DocBits-API-knooppunten, met samenvoeg- en eindknooppunten."><figcaption><p>Historische gegevensstroom. De tak No eindigt vóór de API-knooppunten; de tak Yes bereikt de vier voorbeeldomgevingen.</p></figcaption></figure>

De meerdere DocBits-API-knooppunten staan in dit voorbeeld voor afzonderlijke omgevingen. Uw opzet kan afwijken; controleer dat testberichten de productieomgeving niet kunnen bereiken.

De vier omgevingen dienen alleen als voorbeeld.

### **M3**

Het begin van de gegevensstroom bestaat uit uw M3-toepassing

### **Filter**

De configuratie van het filter ziet er als volgt uit

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Historisch paneel Filter Properties met Properties geselecteerd en Name en Description beide ingesteld op Division."><figcaption><p>Historische filternaam en -beschrijving. De naam Division alleen bepaalt niet welke records worden gefilterd.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Historisch tabblad Attributes van Filter Properties met AccountingEntityID-attributen voor ChartOfAccounts, PurchaseOrder, RemitToPartyMaster en SupplierPartyMaster."><figcaption><p>Historische attributen: elke BOD heeft een AccountingEntityID-pad. Controleer het pad voor elk document in uw tenant.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Historisch tabblad Conditions van Filter Properties met ChartOfAccounts, Used Condition op Not Filtered en een voorbeelduitdrukking voor AccountingEntityID_3."><figcaption><p>Historisch voorbeeld van Conditions. Used Condition staat op Not Filtered terwijl er wel een uitdrukking staat; controleer de geselecteerde voorwaarde en het effect ervan in plaats van aan te nemen dat de uitdrukking actief is.</p></figcaption></figure>

(De boekhoudkundige entiteit-ID is uiteraard uniek voor uw organisatie)

### **DocBits-API**

Hier voegt u een toepassing toe en selecteert u de DocBits-API('s) die u eerder hebt aangemaakt

### **Documenten**

Selecteer de documenten die aan de M3-bron en aan de ontvangende knooppunten zijn toegewezen. Controleer dat de filterattributen en de ontvangende routes elk vereist document dekken.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Historische M3-gegevensstroom met het documentpictogram gemarkeerd en een paneel Documents met Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster en Sync.SupplierPartyMaster."><figcaption><p>Historische documentselectie voor de M3-stroom. Dit is een BOD-documentlijst, geen configuratie van een bestandsknooppunt.</p></figcaption></figure>

## **BOD's activeren in M3**

Navigeer naar de Infor M3-toepassing

Open het besturingselement **Search and Start** van M3, voer **EVS006** in en bevestig het programma. Gebruik de navigatie die uw M3-client ondersteunt.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Historisch dialoogvenster Search and Start van M3 met evs006 en een knop OK."><figcaption><p>Historisch zoeken naar een programma: voer EVS006 in bij Search and Start.</p></figcaption></figure>

Definieer in EVS006 de BOD-namen die voor uw goedgekeurde mapping nodig zijn. Het historische voorbeeld gebruikt SupplierPartyMaster, RemitToPartyMaster en PurchaseOrder. Controleer de bijbehorende M3-tabelnamen in uw versie voordat u een initial-loaddefinitie aanmaakt.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Gebruik per goedgekeurde definitie de actie voor toevoegen. Controleer bedrijf en divisie voordat u verdergaat.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Uitgesneden historische werkbalk van EVS006 met Add gemarkeerd boven lege velden voor BOD noun, BOD variant, BOD en Table."><figcaption><p>Historische actie Add in EVS006. Deze uitsnede toont geen ingevulde initial-loaddefinities.</p></figcaption></figure>

Nadat u elk van de BOD's hebt toegevoegd, klikt u met de rechtermuisknop op de BOD-naam van de BOD en selecteert u Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Historisch contextmenu met Related uitgeklapt en Run gemarkeerd; daaronder staat History."><figcaption><p>Historische actie Related → Run. Gebruik later History om het resultaat van de initial load te controleren.</p></figcaption></figure>

De gerelateerde actie **Run** opent EVS007. Kies **Sync** alleen wanneer de ontvangende ION-stroom dat verwacht. Controleer de selectie en de filters vóór de definitieve indiening; doorgaan naar het volgende scherm bewijst niet dat de gegevens zijn afgeleverd.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Historisch scherm EVS007 Initial Load Job voor CIDMAS en SupplierPartyMaster met status Pending, het menu voor het BOD-werkwoord open en Sync aangetekend terwijl Show nog wordt getoond."><figcaption><p>Historische keuze van het werkwoord in EVS007 vóór uitvoering. De afbeelding toont een openstaande taak en een aangetekende optie Sync; ze bewijst niet dat Sync is gekozen of dat gegevens zijn geïmporteerd.</p></figcaption></figure>

Een melding bij de indiening bevestigt dat de taak is aangevraagd. Controleer in **History** van EVS006 het aantal verwerkte records en de fouten. Controleer daarna het bericht en de bestemming in Infor ION.

## Controleren in DocBits

Open in de bedoelde DocBits-organisatie **Instellingen → Documentverwerking → Stamgegevens opzoeken → BOD-invoergegevens → Leverancier**. Kies het identificatieveld in **Zoeken op kolom**, voer een bekend leveranciersnummer of een bekende naam in bij **Zoekopdracht Tekenreeks** en gebruik het vergrootglas om te zoeken. Open daarna **Inkooporder** en zoek een bekend inkoopordernummer; controleer **Koptekst Van Inkooporder** als uw mapping kop- en regelgegevens scheidt. Vergelijk de identificaties en het bedrijf met de M3-bron. Een geslaagd EVS007-verzoek alleen bewijst niet dat alle gegevens zijn aangekomen.

<figure><img src="../../../.gitbook/assets/dbdc-1140-supplier-nl-20261112.png" alt="Nederlandse DocBits-weergave Stamgegevens opzoeken met het tabblad Leverancier, de zoekvelden Zoeken op kolom en Zoekopdracht Tekenreeks en tien verzonnen leveranciersregels van SUP-1001 tot SUP-1010."><figcaption><p>Leveranciersweergave in sandboxversie 11.27.7 met verzonnen voorbeeldgegevens. Zoek een bekende testidentificatie en vergelijk die met M3 en ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1140-purchase-order-nl-20261112.png" alt="Nederlandse DocBits-weergave Stamgegevens opzoeken met de tabbladen Leverancier en Inkooporder, dezelfde zoekvelden en tien verzonnen inkooporderregels van PO-4500 tot PO-4509."><figcaption><p>Inkooporderweergave in sandboxversie 11.27.7 met verzonnen voorbeeldgegevens. De regels bewijzen geen M3-import.</p></figcaption></figure>

De Engelstalige Dev-weergaven zijn op 29 oktober 2026 gecontroleerd zonder een M3-taak uit te voeren, een bestand te importeren of stamgegevens te wijzigen; daar zijn de recordrijen weggelaten. De twee Nederlandse afbeeldingen komen uit sandboxversie 11.27.7 en tonen verzonnen voorbeeldrijen in plaats van echte stamgegevens; ze laten zien waar u controleert, niet dat een overdracht is voltooid. Ontbreekt een verwachte record, controleer dan de geschiedenis in EVS006, de routering in ION, de BOD-mapping en de DocBits-organisatie voordat u opnieuw uitvoert.
