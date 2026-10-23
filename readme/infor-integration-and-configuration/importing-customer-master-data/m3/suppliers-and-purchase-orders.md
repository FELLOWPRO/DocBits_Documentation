# Leveranciers en inkooporders

## **Verbindingspunt**

U moet het verbindingspunt DocBits API maken om de gegevensstroom later te kunnen maken.

Navigeer in InforOS naar ION Desk → Verbinden → Verbindingspunten

![Navigatiemenu van Infor ION Desk met de items Home, Data Flows, API Flows en Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)

Eenmaal hier moet u een nieuw verbindingspunt maken.

![Pagina Connection Points in ION Desk met de werkbalkpictogrammen en een lege lijst met connectionpoints](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Geef het verbindingspunt een naam en beschrijving die de aard en omgeving beschrijft. Importeer op het tabblad Verbinding het serviceaccount dat u hebt gemaakt voor de omgeving waarmee u werkt.

![Verbindingspuntinstellingen voor DocBits-DEV-Demo-Import in ION Desk met Name, Description en serviceaccount onder het tabblad Connection](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Ga vervolgens naar het tabblad Documenten. U moet de volgende BOD's aan het verbindingspunt toevoegen. Deze zijn niet allemaal nodig voor de stamgegevens van de leverancier en de inkooporder, maar zijn wel handig wanneer andere functies, zoals automatische boekhouding, moeten worden geïmplementeerd.

![Tabblad Documents van het ION Desk-verbindingspunt met een lijst met Connection Documents waaronder Acknowledge.SupplierInvoice, Sync.PurchaseOrder, Sync.RemitToPartyMaster en Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Voorlopig concentreren we ons alleen op de noodzakelijke BOD's, namelijk: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster en Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData en Sync.SupplierPartyMaster

De configuratie voor deze twee BOD's zou er ongeveer als volgt uit moeten zien (API Oproepnaam verandert voor elk)

![Send to API-configuratie voor Sync.SupplierPartyMaster met het product DocBits-DEV en de bewerking post CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

De configuratie voor deze BOD zou er ongeveer als volgt uit moeten zien

![Send to API-configuratie voor Sync.PurchaseOrder met Product DocBits-DEV en bewerking post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Zodra deze BOD's zijn geconfigureerd, kunt u het verbindingspunt opslaan door op het pictogram rechts naast de terugknop te drukken.

## **Gegevensstroom**

De gegevensstroom ziet er ongeveer als volgt uit

![ION-gegevensstroomdiagram dat M3, een Filter en verschillende DocBits-API-applicaties koppelt aan een End-element](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(De reden voor meerdere DocBits API's is te wijten aan het feit dat elke verbinding een andere omgeving vertegenwoordigt, wat betekent dat uw gegevensstroom enigszins kan verschillen, afhankelijk van het aantal omgevingen dat u heeft)

Voor het doel van deze uitleg zullen we het voorbeeld gebruiken van vier afzonderlijke omgevingen.

### **M3**

Het begin van de datastroom bestaat uit uw M3 applicatie

### **Filter**

De configuratie van het filter ziet er als volgt uit

![Dialoogvenster Filter Properties in ION Desk met de tabbladen Properties, Attributes en Conditions en de velden Name en Description](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Tabblad Filter Attributes met Document Path Filtered Data Type-rijen voor ChartOfAccounts, PurchaseOrder, RemitToPartyMaster en SupplierPartyMaster op AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Tabblad Filter Conditions met Document ChartOfAccounts, de voorwaarde Not Filtered en de expressie AccountingEntityID_3 equals 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw)

(De boekhoudkundige entiteits-ID is uiteraard uniek voor uw organisatie)

### **DocBits-API**

Hier voegt u een applicatie toe en selecteert u de DocBits API(s) die u eerder hebt gemaakt

### **Bestanden**

De configuratie zou er als volgt uit moeten zien

![ION-gegevensstroom van M3 via een filter naar de applicaties DocBits-DEV-P, DocBits-DEV-S en DocBits-DEV-D met de documenten ChartOfAccounts, PurchaseOrder, RemitToPartyMaster en SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **BOD’s activeren in M3**

Navigeer naar de toepassing Infor M3

Eenmaal in het hoofdmenu typt u Command + R om het zoekvak van de opdrachtprompt te openen. Typ vervolgens evs006 en zoek.

![Search and Start-paneel in Infor M3 geopend boven het hoofdmenu](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o)

Eenmaal op deze pagina moet u de SupplierPartyMaster, RemitToPartyMaster en PurchaseOrder aan de lijst toevoegen.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Voor elk geval moet u op het pluspictogram drukken om ze aan de lijst toe te voegen.

![Op gebeurtenissen gebaseerde BOD-triggerlijst EVS006 in Infor M3 met een werkbalk Actions en de knop Apply](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw)

Nadat u elk van de BOD's hebt toegevoegd, klikt u met de rechtermuisknop op het zelfstandig naamwoord BOD van de BOD en selecteert u Gerelateerd → Uitvoeren

![Rechtermuisknopcontextmenu in Infor M3 met de opties Drill down, Select, Change, History, Copy, Delete en Display](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

U wordt naar het volgende menu gebracht, waar u het werkwoord BOD moet wijzigen in Sync en vervolgens op NEXT moet drukken om de BOD's te activeren.

![BOD-triggerpaneel in Infor M3 voor tabel CIDMAS met BOD-naam SupplierPartyMaster en taakstatus Pending](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Zodra u de BOD's activeert, ontvangt u een melding waarin dit wordt bevestigd.

Als dit succesvol is gedaan, zouden de leveranciers- en inkoopordertabellen nu beschikbaar moeten zijn onder Instellingen → Mastergegevens opzoeken.
