# Belastingcodes

## **DocBits-verbindingspunten maken**

Open ION Desk → Verbinden → Verbindingspunten

![Infor ION Desk met het menu Connect open op het overzicht van Connection Points](https://lh7-us.googleusercontent.com/QLQB17W_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij_tDw_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Voor deze gegevensstroom heeft u 4 verbindingspunten nodig, 3 API verbindingspunten voor de verschillende belastingcodecategorieën (standaardtarief, verlaagd tarief en vrijgesteld) en een Applicatieverbindingspunt dat uw LN bedrijf vertegenwoordigt.

Om nieuwe aansluitpunten aan te maken, selecteert u de knop “+ADD””

![Pagina Connection Points in ION Desk met de knop Add in de werkbalk](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H_MzaKe9CDT0w1b7GKJ8GtT_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Selecteer “API” onderaan de lijst met opties

![Menu van verbindingspunttypen met de optie API onderaan](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT__ZKM4jciHA5I)

U wordt naar de volgende pagina geleid

![Pagina New API connection point in ION Desk met de velden Name, Description en serviceaccount](https://lh7-us.googleusercontent.com/4pcN0B7aibjn_Qn8nMgkzRc_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

Hier vult u alle gegevens van het TaxCode aansluitpunt in. Voor elk van de drie verbindingspunten die u gaat maken, doet u het volgende

* Voer een naam in: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Beschrijving: Dit kan hetzelfde zijn als de Naam of iets dergelijks
* Importeer een serviceaccount dat u heeft gemaakt.

Schakel over naar het tabblad “Documents” en selecteer het pictogram PLUS om de BOD toe te voegen die we nodig hebben, zoals hieronder

![Tabblad Documents van het verbindingspunt met het pluspictogram en de BOD-richtingopties Get from API, Send to API en Trigger API](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Zoek naar de BOD

![Dialoogvenster Input Document foreground process voor het ION API-verzoek met de tabbladen Request Parameters, Request Body en Settings](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Zoek naar de BOD genaamd “Sync.LnTaxCode”, klik erop en druk op “OK” om de BOD toe te voegen.

![BOD-selectielijst met Sync.LnTaxCode geselecteerd en de knop OK](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0_Lk)

Ga verder naar de sectie ION API. Onder API Oproepnaam kunt u de naam van de BOD, Sync.LnTaxCode gebruiken

Druk op de knop “SELECT”

![Pagina van het connectiepunt met de sectie ION API, het veld API Call Name en de knop SELECT](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ_Tmt_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Selecteer de API die u hebt geconfigureerd voor de omgeving waarmee u werkt en zoek naar de volgende API. Zodra u het hebt geselecteerd, drukt u op “OK”.

![Dialoogvenster ION API Operation met de DocBits-stamdata-opzoekbewerkingen zoals Import Xml File en Import Xml Data](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR_OCzDHTG5q5KTwWMHOR5qNoNd38)

Ga vervolgens naar het tabblad Verzoektekst.

Hier vindt een kleine verandering plaats voor elk verbindingspunt. Dit is te zien aan de veldtoewijzingen die u aan elke belastingcode toewijst, aangezien deze enigszins verschillen.

![Tabblad Request Body met de JSON-body en het item field_mappings voor de belastingcode](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi_d_hzN8CGo8gu6Ec84)

In de rij field\_mappings, onder waarde, plaatst u de specifieke veldtoewijzingen voor het specifieke belastingcodeverbindingspunt dat u maakt (standaardtarief, verlaagd tarief of vrijgesteld). Deze toewijzingen zijn beschikbaar op https://docbits.com/doc/field-mappings/.

Het eindresultaat moet er hetzelfde uitzien als of vergelijkbaar zijn met de afbeelding hierboven. Zodra dit is gebeurd, klikt u hier op de optie SAVE.

![Menu in ION Desk met de optie SAVE voor het connectiepunt](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ_09WQcQhjO7kbb2U3jSK__wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Configuratie van de gegevensstroom**

Navigeer naar ION Desk → Verbinden → Gegevensstromen

![Infor ION Desk met het menu Connect open op het Data Flows-overzicht](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt_rVJKr4Y0UtiTf14NqTHLQ)

Klik op “+ADD” en selecteer documentstroom

![Data Flows-pagina in ION Desk met het ADD-menu en de optie document flow](https://lh7-us.googleusercontent.com/HYqc_P2DQjBoc-mpsyZ_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH_zZwup7Bh4lKe4O5kr6hmAZm4)

Creëer de volgende gegevensstroom door de componenten vanuit het menu naar te slepen en neer te zetten

![Documentflow-editor met de componenten applicatie, document, filter en API in een keten gerangschikt](https://lh7-us.googleusercontent.com/V_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Applicatie (LN)**

![Filterbeslissingsinstellingen in ION Desk met de vertakkingen Yes en No en de End-knooppunten](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL_oJMf2QnWn2xZLtS4zjN8AzCS_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Hier selecteert u uw LN bedrijf. Het eindresultaat zou er ongeveer als volgt uit moeten zien

![Gegevensstroom met de geselecteerde applicatiecomponent LN en diens bedrijf](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Document**

![Documentselectie voor het applicatieknooppunt met de BOD Sync.LnTaxCode gekozen uit de Documents-lijst](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT_Hzn5cyhp18jq_IyI)

Hier voegt u de Sync.LnTaxCode BOD van eerder toe, het resultaat ziet er als volgt uit

![Gegevensstroom met de na de applicatie toegevoegde documentcomponent Sync.LnTaxCode](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng_pKmP5VQ5w0E_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a_8y84XyLyvh61-LdoQ7f15j-wE1nl_TSYSDg)

### **Filters**

![Gegevensstroomcanvas in ION Desk met drie filterknooppunten waarvan de Yes- en No-vertakkingen naar het einde lopen](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filter 1 (boven): standaardtarief**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![Dialoogvenster Filtereigenschappen voor het volledige belastingcodefilter met de velden Name en Description](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c_RyPk_GCTFEfiNxU_H5aA979k5hOv2coDYEJHu4K1EaTLUf8_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![Paneel Filter Properties in ION Desk met de voorwaarde op LnTaxCode en het RateNumeric-documentpad](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r_jHoHBwquN1Ore2AmyjCaf_YVT78KiKtY_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![Paneel Filter Properties in ION Desk met de voorwaarde COMBI als TaxFull OR Tax16 OR Tax20 op RateNumeric](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe_1lTUUEQbfXPvtrzP7iudkSaG_oiX_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filter 2 (midden): verlaagd tarief**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![Dialoog Filtereigenschappen voor het filter van het verlaagde btw-tarief met de velden Name en Description](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd_s-7qj2KVNOWN7s)

![Paneel Filter Properties in ION Desk met het documentpad LnTaxCode en het RateNumeric-kenmerk](https://lh7-us.googleusercontent.com/87PoQQ5q_35buL_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![Paneel Filter Properties in ION Desk met de voorwaarde COMBI2 als Tax7 OR Tax5 OR Tax10 op RateNumeric](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr_g6a_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filter 3 (onder): vrijgesteld**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![Dialoogvenster Filtereigenschappen voor het vrije belastingcodefilter met de velden Name en Description](https://lh7-us.googleusercontent.com/c_SuWaZ3gF-FbOPWkxB_eFgkT-TGJEYwV_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![Paneel Filter Properties in ION Desk met de voorwaarde op LnTaxCode voor het gratis btw-tarief](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![Paneel Filter Properties in ION Desk met de voorwaarde Tax0 en RateNumeric gelijk aan 0](https://lh7-us.googleusercontent.com/_APmMO6A2AG2km4H4em-ZMrn6_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![Dataflow met de drie API-componenten voor de verbindingspunten van het btw-tarief](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

Hier selecteert u de API-verbindingspunten die u eerder hebt gemaakt. Dit doet u door API te selecteren onder het vervolgkeuzemenu “Select ION API Connector”.

#### **API 1 (boven): standaardtarief**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![API-instellingen in de dataflow met de dropdown Select ION API Connector voor de volledige btw-code](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO_kS9Vwzg)

#### **API 2 (midden): verlaagd tarief**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![API-instellingen in de dataflow met de vervolgkeuzelijst Select ION API Connector voor het verlaagde btw-tarief](https://lh7-us.googleusercontent.com/vw1hM3W4eCt_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx_25L1Ce-_va3ZgfKXY8)

#### **API 3 (onder): vrijgesteld**

De Naam en Beschrijving zijn afhankelijk van de omgeving die u gebruikt en uw voorkeuren.

![API-instellingen in de dataflow met de dropdown Select ION API Connector voor de vrije belastingcode](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA_Kz6Ptx495cQbwq_EHfEGNvvpr_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK_HRn7T-fFOR8)

Zodra al het bovenstaande is gedaan, SAVE en ACTIVATE de gegevensstroom door op de volgende knoppen te drukken

![Werkbalk van de gegevensstroom met de knoppen SAVE en ACTIVATE voor de documentstroom](https://lh7-us.googleusercontent.com/f8gkYY1Z_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **BOD’s activeren (LN)**

Open LN in Infor

![Infor-startpagina in de browser met de items Home, Master Data en Publish Logistic Master Data in de navigatie](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Navigeer naar Algemeen → BOD Berichten → BOD's publiceren → Financiële stamgegevens publiceren

![Infor LN-menu met Common, BOD Messaging, Publish BODs en Publish Financial Master Data](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt_v0fv_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY_azWtqaqKA)

Selecteer MORE en klik op LnTaxCode

![Kolommenlijst in Publish Financial Master Data met LnTaxCode naast de items voor AccountingBookDefinition en AccountingEntity](https://lh7-us.googleusercontent.com/MtjE7Glgv7e_F_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Vink het selectievakje aan om de LnTaxCode BOD's te selecteren

![Dialoog Publish Financial Master Data met de kolom LnTaxCode en de knoppen PROCESS, CLOSE, SELECT ALL en CLEAR ALL](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq_yLm6_gEw967PGp3HK0hzO-G2XiQ)

Navigeer terug naar het tabblad OPTIONS. Uw configuratie zou er als volgt uit moeten zien

![Tabblad OPTIONS in Publish Financial Master Data met de configuratie voor de LnTaxCode-BOD's](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Wanneer u de BOD's wilt publiceren, selecteert u PROCESS.

Het eindresultaat zou u een vergelijkbare tabel moeten opleveren in uw DocBits-omgeving.

![DocBits-tabel met de geïmporteerde belastingcoderijen met de codes BE_NAVL, BE_NAVLRP en BE_NAVM en hun tarieven](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
