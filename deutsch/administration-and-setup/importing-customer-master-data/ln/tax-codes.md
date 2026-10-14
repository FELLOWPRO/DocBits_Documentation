# Tax Codes

## **DocBits-Verbindungspunkt(e) erstellen**

Öffnen Sie ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/QLQB17W_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij_tDw_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Sie benötigen für diesen Datenfluss 4 Verbindungspunkte: 3 API-Verbindungspunkte für die verschiedenen Steuercode-Kategorien (voll, ermäßigt und frei) und einen Application-Verbindungspunkt, der Ihr LN-Unternehmen repräsentiert.

Um neue Verbindungspunkte zu erstellen, wählen Sie die Schaltfläche „+ADD"

![](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H_MzaKe9CDT0w1b7GKJ8GtT_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Wählen Sie „API" am unteren Ende der Optionsliste

![](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT__ZKM4jciHA5I)

Sie werden zur folgenden Seite weitergeleitet

![](https://lh7-us.googleusercontent.com/4pcN0B7aibjn_Qn8nMgkzRc_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

Hier geben Sie alle Details des TaxCode-Verbindungspunkts ein. Führen Sie für jeden der drei Verbindungspunkte, die Sie erstellen, die folgenden Schritte aus

* Geben Sie einen Namen ein: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Beschreibung: Diese kann mit dem Namen identisch oder ähnlich sein
* Importieren Sie ein von Ihnen erstelltes Service-Konto.

Wechseln Sie zum Reiter „Documents" und wählen Sie das PLUS-Symbol, um das benötigte BOD hinzuzufügen, wie unten dargestellt

![](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Suchen Sie nach dem BOD

![](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Suchen Sie nach dem BOD mit dem Namen „Sync.LnTaxCode", klicken Sie darauf und drücken Sie „OK", um das BOD hinzuzufügen.

![](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0_Lk)

Wechseln Sie zum Abschnitt ION API. Unter API Call Name können Sie den Namen des BOD verwenden: Sync.LnTaxCode

Drücken Sie die Schaltfläche „SELECT"

![](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ_Tmt_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Wählen Sie die API, die Sie für die Umgebung konfiguriert haben, mit der Sie arbeiten, und suchen Sie nach der folgenden API. Sobald Sie sie ausgewählt haben, drücken Sie „OK".

![](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR_OCzDHTG5q5KTwWMHOR5qNoNd38)

Wechseln Sie als Nächstes zum Reiter Request Body.

Hier gibt es für jeden Verbindungspunkt eine leichte Änderung; diese ist in den Feldzuordnungen zu erkennen, die Sie jedem Steuercode zuweisen, da sich diese leicht unterscheiden.

![](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi_d_hzN8CGo8gu6Ec84)

In der Zeile field\_mappings unter value tragen Sie die spezifischen Feldzuordnungen für den jeweiligen Steuercode-Verbindungspunkt ein, den Sie erstellen (voll, ermäßigt oder frei). Diese Zuordnungen sind unter https://docbits.com/doc/field-mappings/ verfügbar.

Das Endergebnis sollte mit dem Bild oben identisch oder ähnlich aussehen. Sobald dies erledigt ist, klicken Sie auf die Option SAVE, die sich hier befindet.

![](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ_09WQcQhjO7kbb2U3jSK__wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Konfiguration des Datenflusses**

Navigieren Sie zu ION Desk → Connect → Data Flows

![](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt_rVJKr4Y0UtiTf14NqTHLQ)

Klicken Sie auf „+ADD" und wählen Sie document flow

![](https://lh7-us.googleusercontent.com/HYqc_P2DQjBoc-mpsyZ_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH_zZwup7Bh4lKe4O5kr6hmAZm4)

Erstellen Sie den folgenden Datenfluss, indem Sie die Komponenten aus dem oberen Menü per Drag-and-Drop hinzufügen

![](https://lh7-us.googleusercontent.com/V_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Application (LN)**

![](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL_oJMf2QnWn2xZLtS4zjN8AzCS_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Hier wählen Sie Ihr LN-Unternehmen aus. Das Endergebnis sollte ungefähr wie folgt aussehen

![](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Document**

![](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT_Hzn5cyhp18jq_IyI)

Hier fügen Sie das zuvor erstellte BOD Sync.LnTaxCode hinzu. Das Ergebnis sieht wie folgt aus

![](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng_pKmP5VQ5w0E_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a_8y84XyLyvh61-LdoQ7f15j-wE1nl_TSYSDg)

### **Filter**

![](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filter 1 (oben) – Voll**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c_RyPk_GCTFEfiNxU_H5aA979k5hOv2coDYEJHu4K1EaTLUf8_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r_jHoHBwquN1Ore2AmyjCaf_YVT78KiKtY_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe_1lTUUEQbfXPvtrzP7iudkSaG_oiX_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filter 2 (Mitte) – Ermäßigt**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd_s-7qj2KVNOWN7s)

![](https://lh7-us.googleusercontent.com/87PoQQ5q_35buL_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr_g6a_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filter 3 (unten) – Frei**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/c_SuWaZ3gF-FbOPWkxB_eFgkT-TGJEYwV_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![](https://lh7-us.googleusercontent.com/_APmMO6A2AG2km4H4em-ZMrn6_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

Hier wählen Sie die zuvor erstellten API-Verbindungspunkte aus. Dies erfolgt, indem Sie die API im Dropdown-Menü „Select ION API Connector" auswählen.

#### **API 1 (oben) – Voll**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO_kS9Vwzg)

#### **API 2 (Mitte) – Ermäßigt**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/vw1hM3W4eCt_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx_25L1Ce-_va3ZgfKXY8)

#### **API 3 (unten) – Frei**

Name und Beschreibung hängen von der von Ihnen verwendeten Umgebung und Ihren Präferenzen ab.

![](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA_Kz6Ptx495cQbwq_EHfEGNvvpr_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK_HRn7T-fFOR8)

Sobald alle oben genannten Schritte abgeschlossen sind, SPEICHERN und AKTIVIEREN Sie den Datenfluss, indem Sie die folgenden Schaltflächen drücken

![](https://lh7-us.googleusercontent.com/f8gkYY1Z_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **Auslösen der BODs (LN)**

Öffnen Sie LN in Infor

![](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Navigieren Sie zu Common → BOD Messaging → Publish BODs → Publish Financial Master Data

![](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt_v0fv_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY_azWtqaqKA)

Wählen Sie MORE und klicken Sie auf LnTaxCode

![](https://lh7-us.googleusercontent.com/MtjE7Glgv7e_F_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Aktivieren Sie das Kontrollkästchen, um die LnTaxCode-BODs auszuwählen

![](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq_yLm6_gEw967PGp3HK0hzO-G2XiQ)

Navigieren Sie zurück zum Reiter OPTIONS; Ihre Konfiguration sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Wenn Sie die BODs veröffentlichen möchten, wählen Sie PROCESS.

Das Endergebnis sollte Ihnen eine ähnliche Tabelle in Ihrer DocBits-Umgebung liefern.

![](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
